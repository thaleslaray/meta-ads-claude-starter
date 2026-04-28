"""Proactive rate limiter for Meta Graph API.

Monitors response headers and enforces throttling before hitting limits.
Implements circuit breaker for abuse detection (error 613 without subcode).
"""

import asyncio
import json
import logging
import random
import time
from dataclasses import dataclass, field
from typing import Any, Optional

import httpx

logger = logging.getLogger("meta_ads_mcp.rate_limiter")

# Rate limit error codes from Meta's official docs
RATE_LIMIT_CODES = {4, 17, 32, 613, 80000, 80001, 80002, 80003, 80004, 80005, 80006, 80008, 80009, 80014}

# BUC error codes that carry estimated_time_to_regain_access in headers
BUC_CODES = {80000, 80001, 80002, 80003, 80004, 80005, 80006, 80008, 80009, 80014}

# Abuse prevention — these indicate behavioral anomaly detection
ABUSE_CODES = {(613, 0), (613, 1996)}  # (code, subcode) pairs


@dataclass
class UsageSnapshot:
    """Parsed rate limit usage from Meta response headers."""
    call_count: float = 0.0
    total_cputime: float = 0.0
    total_time: float = 0.0
    estimated_time_to_regain_access: int = 0
    acc_id_util_pct: float = 0.0
    ads_api_access_tier: str = "development_access"
    timestamp: float = field(default_factory=time.monotonic)


class CircuitBreakerOpen(Exception):
    """Raised when circuit breaker is open due to abuse detection."""

    def __init__(self, message: str, reset_at: float):
        self.reset_at = reset_at
        super().__init__(message)


class RateLimiter:
    """Proactive rate limiter that reads Meta API response headers.

    Tracks usage per ad account and enforces:
    - Proactive throttling at 75% usage
    - Hard pause at 90% usage
    - Circuit breaker for abuse prevention errors (613/no subcode, 613/1996)
    - Minimum delay between requests (configurable)
    """

    def __init__(
        self,
        min_delay: float = 0.2,
        throttle_threshold: float = 60.0,
        pause_threshold: float = 80.0,
        circuit_breaker_cooldown: float = 300.0,
    ):
        self.min_delay = min_delay
        self.throttle_threshold = throttle_threshold
        self.pause_threshold = pause_threshold
        self.circuit_breaker_cooldown = circuit_breaker_cooldown

        self._usage: dict[str, UsageSnapshot] = {}  # per ad account
        self._app_usage = UsageSnapshot()
        self._last_request_time: float = 0.0
        self._circuit_breaker_reset_at: float = 0.0
        self._lock = asyncio.Lock()
        self._dev_tier_warned: set[str] = set()  # accounts already warned about dev tier

    @property
    def is_circuit_open(self) -> bool:
        return time.monotonic() < self._circuit_breaker_reset_at

    def trip_circuit_breaker(self, cooldown: Optional[float] = None):
        """Trip the circuit breaker — stops ALL requests for cooldown period."""
        cd = cooldown or self.circuit_breaker_cooldown
        self._circuit_breaker_reset_at = time.monotonic() + cd
        logger.warning(
            "CIRCUIT BREAKER TRIPPED — all requests blocked for %.0fs. "
            "This likely means Meta detected anomalous API behavior. "
            "Reduce request volume and frequency.",
            cd,
        )

    async def wait_if_needed(self, ad_account_id: Optional[str] = None):
        """Wait before making a request if needed. Raises CircuitBreakerOpen if tripped."""
        async with self._lock:
            # Circuit breaker check
            if self.is_circuit_open:
                wait_remaining = self._circuit_breaker_reset_at - time.monotonic()
                raise CircuitBreakerOpen(
                    f"Circuit breaker open — Meta abuse detection triggered. "
                    f"All requests blocked for {wait_remaining:.0f}s more. "
                    f"DO NOT retry — reduce your request volume.",
                    reset_at=self._circuit_breaker_reset_at,
                )

            delay = self.min_delay

            # Check per-account usage
            if ad_account_id and ad_account_id in self._usage:
                usage = self._usage[ad_account_id]
                max_pct = max(usage.call_count, usage.total_cputime, usage.total_time)

                if max_pct >= self.pause_threshold:
                    wait_time = max(usage.estimated_time_to_regain_access * 60, 60)
                    logger.warning(
                        "Ad account %s at %.0f%% usage — pausing for %ds",
                        ad_account_id, max_pct, wait_time,
                    )
                    delay = max(delay, wait_time)
                elif max_pct >= self.throttle_threshold:
                    # Slow down proportionally
                    factor = (max_pct - self.throttle_threshold) / (self.pause_threshold - self.throttle_threshold)
                    throttle_delay = 1.0 + factor * 4.0  # 1s at 75%, 5s at 90%
                    delay = max(delay, throttle_delay)
                    logger.info(
                        "Ad account %s at %.0f%% — throttling (%.1fs delay)",
                        ad_account_id, max_pct, throttle_delay,
                    )

            # Check app-level usage
            app_max = max(self._app_usage.call_count, self._app_usage.total_cputime, self._app_usage.total_time)
            if app_max >= self.pause_threshold:
                delay = max(delay, 60)
            elif app_max >= self.throttle_threshold:
                factor = (app_max - self.throttle_threshold) / (self.pause_threshold - self.throttle_threshold)
                delay = max(delay, 1.0 + factor * 4.0)

            # Enforce minimum delay between requests
            elapsed = time.monotonic() - self._last_request_time
            if elapsed < delay:
                wait = delay - elapsed
                # Add jitter to avoid thundering herd
                jitter = random.uniform(0, wait * 0.2)
                await asyncio.sleep(wait + jitter)

            self._last_request_time = time.monotonic()

    def update_from_response(self, response: httpx.Response, ad_account_id: Optional[str] = None):
        """Parse rate limit headers from a Meta API response and update internal state."""
        self._parse_app_usage(response)
        self._parse_buc_usage(response, ad_account_id)
        self._parse_ad_account_usage(response, ad_account_id)
        self._parse_insights_throttle(response)
        self._check_access_tier(ad_account_id)

    def _parse_app_usage(self, response: httpx.Response):
        """Parse X-App-Usage header."""
        header = response.headers.get("x-app-usage")
        if not header:
            return
        try:
            data = json.loads(header)
            self._app_usage = UsageSnapshot(
                call_count=data.get("call_count", 0),
                total_cputime=data.get("total_cputime", 0),
                total_time=data.get("total_time", 0),
            )
        except (json.JSONDecodeError, TypeError):
            pass

    def _parse_buc_usage(self, response: httpx.Response, ad_account_id: Optional[str] = None):
        """Parse X-Business-Use-Case-Usage header."""
        header = response.headers.get("x-business-use-case-usage")
        if not header:
            return
        try:
            data = json.loads(header)
            for obj_id, entries in data.items():
                account_id = ad_account_id or obj_id
                if not isinstance(entries, list):
                    continue
                for entry in entries:
                    self._usage[account_id] = UsageSnapshot(
                        call_count=entry.get("call_count", 0),
                        total_cputime=entry.get("total_cputime", 0),
                        total_time=entry.get("total_time", 0),
                        estimated_time_to_regain_access=entry.get("estimated_time_to_regain_access", 0),
                        ads_api_access_tier=entry.get("ads_api_access_tier", "development_access"),
                    )
        except (json.JSONDecodeError, TypeError):
            pass

    def _parse_ad_account_usage(self, response: httpx.Response, ad_account_id: Optional[str] = None):
        """Parse X-Ad-Account-Usage header."""
        header = response.headers.get("x-ad-account-usage")
        if not header:
            return
        try:
            data = json.loads(header)
            acc_pct = data.get("acc_id_util_pct", 0)
            tier = data.get("ads_api_access_tier", "development_access")
            if ad_account_id:
                if ad_account_id not in self._usage:
                    self._usage[ad_account_id] = UsageSnapshot()
                self._usage[ad_account_id].acc_id_util_pct = float(acc_pct)
                self._usage[ad_account_id].ads_api_access_tier = tier
        except (json.JSONDecodeError, TypeError, ValueError):
            pass

    def _parse_insights_throttle(self, response: httpx.Response):
        """Parse X-FB-Ads-Insights-Throttle header."""
        header = response.headers.get("x-fb-ads-insights-throttle")
        if not header:
            return
        try:
            data = json.loads(header)
            app_pct = data.get("app_id_util_pct", 0)
            if float(app_pct) > self._app_usage.call_count:
                self._app_usage.call_count = float(app_pct)
        except (json.JSONDecodeError, TypeError, ValueError):
            pass

    def _check_access_tier(self, ad_account_id: Optional[str] = None):
        """Warn once per account if operating on development_access tier."""
        if not ad_account_id or ad_account_id not in self._usage:
            return
        usage = self._usage[ad_account_id]
        if usage.ads_api_access_tier == "development_access" and ad_account_id not in self._dev_tier_warned:
            self._dev_tier_warned.add(ad_account_id)
            logger.warning(
                "AD ACCOUNT %s IS ON DEVELOPMENT ACCESS TIER. "
                "Rate limit: 60 points/hour (reads=1pt, writes=3pts). "
                "An AI agent can exhaust this in seconds. "
                "Apply for Advanced Access (9,000 pts/hr) at "
                "developers.facebook.com → App Review → Permissions and Resources → "
                "Ads Management Standard Access → Solicitar acesso avançado. "
                "Run 'python scripts/warmup.py' to accumulate the required 1,500 calls.",
                ad_account_id,
            )

    def should_retry(self, error_code: int, error_subcode: int) -> bool:
        """Determine if an error is retryable (rate limit) vs fatal (abuse detection)."""
        if (error_code, error_subcode) in ABUSE_CODES:
            return False  # Abuse detection — do NOT retry, circuit breaker
        return error_code in RATE_LIMIT_CODES

    def get_usage_summary(self, ad_account_id: Optional[str] = None) -> dict[str, Any]:
        """Get current usage summary for debugging."""
        result: dict[str, Any] = {
            "circuit_breaker_open": self.is_circuit_open,
            "app_usage": {
                "call_count": self._app_usage.call_count,
                "total_cputime": self._app_usage.total_cputime,
                "total_time": self._app_usage.total_time,
            },
        }
        if ad_account_id and ad_account_id in self._usage:
            u = self._usage[ad_account_id]
            result["account_usage"] = {
                "call_count": u.call_count,
                "total_cputime": u.total_cputime,
                "total_time": u.total_time,
                "estimated_time_to_regain_access_min": u.estimated_time_to_regain_access,
                "acc_id_util_pct": u.acc_id_util_pct,
                "ads_api_access_tier": u.ads_api_access_tier,
            }
        return result
