"""Meta Graph API async HTTP client with auth, rate limiting, and compliance hardening.

Implements Meta's official rate limiting best practices:
- Monitors all 4 response headers (X-Business-Use-Case-Usage, X-Ad-Account-Usage,
  X-App-Usage, X-FB-Ads-Insights-Throttle)
- Handles all documented error codes (4, 17, 32, 613, 80000-80014)
- Circuit breaker for abuse detection (error 613 without subcode / subcode 1996)
- Exponential backoff with jitter and estimated_time_to_regain_access
- Proactive throttling at configurable thresholds (75% slow, 90% pause)
"""

import asyncio
import hashlib
import hmac
import logging
import os
import random
import re
from typing import Any, Optional

import httpx

from meta_ads_mcp.rate_limiter import (
    ABUSE_CODES,
    RATE_LIMIT_CODES,
    CircuitBreakerOpen,
    RateLimiter,
)
from meta_ads_mcp.audit import get_audit_log, warn_outside_business_hours
from meta_ads_mcp.validation import ValidationError, validate_request_params

logger = logging.getLogger("meta_ads_mcp.client")

API_VERSION = "v25.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"
USER_AGENT = "meta-ads-mcp/0.1.0"

# Token pattern for sanitization in logs/error messages
_TOKEN_RE = re.compile(r"(access_token=|token[\"':\s=]+)([A-Za-z0-9|_-]{20,})", re.IGNORECASE)


def sanitize_token(text: str) -> str:
    """Mask access tokens in strings to prevent accidental exposure in logs."""
    return _TOKEN_RE.sub(lambda m: m.group(1) + m.group(2)[:8] + "..." + m.group(2)[-4:], text)

# Max retries for rate limit errors (not abuse detection)
MAX_RETRIES = 5
# Base delay for exponential backoff (seconds)
BASE_BACKOFF = 1.0
# Max backoff cap (seconds)
MAX_BACKOFF = 60.0


class MetaAPIError(Exception):
    """Error from Meta Graph API."""

    def __init__(self, message: str, code: int = 0, subcode: int = 0, fbtrace_id: str = ""):
        self.code = code
        self.subcode = subcode
        self.fbtrace_id = fbtrace_id
        super().__init__(message)


class RateLimitError(MetaAPIError):
    """Rate limit hit — caller should retry with backoff."""
    pass


class AbuseDetectionError(MetaAPIError):
    """Abuse/anomaly detection triggered — do NOT retry. Reduce volume immediately."""
    pass


class TokenExpiredError(MetaAPIError):
    """Access token has expired or been invalidated. Generate a new token."""
    pass


# Error code 190 = expired/invalid OAuthException
TOKEN_EXPIRED_CODE = 190


# Regex to extract ad account ID from endpoints like "act_123456/campaigns"
_AD_ACCOUNT_RE = re.compile(r"(act_\d+)")


def _extract_ad_account(endpoint: str) -> Optional[str]:
    """Extract ad account ID from an API endpoint path."""
    match = _AD_ACCOUNT_RE.search(endpoint)
    return match.group(1) if match else None


def _extract_resource_id(endpoint: str, ad_account: Optional[str] = None) -> str:
    """Extract the primary resource ID from an endpoint for audit logging.

    Returns the ad account if the endpoint targets it, otherwise the first
    numeric ID segment (campaign/adset/ad/etc), otherwise the bare endpoint.
    """
    if ad_account and endpoint.rstrip("/").endswith(ad_account):
        return ad_account
    # Match the first numeric ID (10+ digits — Meta IDs are large)
    match = re.search(r"(\d{10,})", endpoint)
    if match:
        return match.group(1)
    return ad_account or endpoint.lstrip("/").split("/")[0]


class MetaClient:
    """Async HTTP client for Meta Graph API v25.0 with compliance hardening.

    Features:
    - Proactive rate limiting via response header monitoring
    - Circuit breaker for abuse detection (error 613)
    - Exponential backoff with jitter
    - Configurable min delay between requests
    - Custom User-Agent header
    - App secret proof support
    """

    def __init__(self, rate_limiter: Optional[RateLimiter] = None):
        self._token = os.environ.get("META_ACCESS_TOKEN", "")
        self._app_secret = os.environ.get("META_APP_SECRET", "")
        self._client: Optional[httpx.AsyncClient] = None
        self.rate_limiter = rate_limiter or RateLimiter()
        self._etag_cache: dict[str, tuple[str, dict[str, Any]]] = {}  # url -> (etag, cached_response)

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=BASE_URL,
                timeout=httpx.Timeout(30.0, read=60.0),
                limits=httpx.Limits(max_connections=5),
                headers={"User-Agent": USER_AGENT},
            )
        return self._client

    def _auth_params(self) -> dict[str, str]:
        params = {"access_token": self._token}
        if self._app_secret:
            proof = hmac.new(
                self._app_secret.encode(),
                self._token.encode(),
                hashlib.sha256,
            ).hexdigest()
            params["appsecret_proof"] = proof
        return params

    async def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        audit_context: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make an authenticated request to the Meta Graph API.

        Handles rate limiting, retries with backoff, and circuit breaker.

        Args:
            method: HTTP method (GET, POST, DELETE).
            endpoint: API path (e.g. "me", "act_123/campaigns") or full URL for pagination.
            params: Query parameters.
            data: POST body data.
            audit_context: Caller-supplied context to enrich the audit log entry
                for write ops. Recognized keys: operation (semantic name like
                "update_status"), before_state, after_state, user_confirmed.
                When omitted, the entry is logged with only HTTP-level fields.

        Returns:
            Parsed JSON response.

        Raises:
            MetaAPIError: On API errors.
            RateLimitError: On rate limit errors after retries exhausted.
            AbuseDetectionError: On abuse/anomaly detection (613/no subcode or 613/1996).
            CircuitBreakerOpen: When circuit breaker is tripped.
            ValidationError: On invalid parameters (caught before sending to Meta).
        """
        # Validate params before sending — user errors reduce rate limit quota
        validate_request_params(endpoint, params)

        # Soft signal for write operations outside business hours (POST, DELETE).
        # The HITL approval flow is the primary defense — this only logs.
        is_write = method in ("POST", "DELETE")
        if is_write:
            warn_outside_business_hours(f"{method} {endpoint}")

        client = await self._get_client()
        all_params = {**self._auth_params(), **(params or {})}
        ad_account = _extract_ad_account(endpoint)

        # Proactive rate limiting — wait if needed, raises CircuitBreakerOpen if tripped
        await self.rate_limiter.wait_if_needed(ad_account)

        last_error: Optional[Exception] = None

        # Build request headers (ETag support for GET requests)
        request_headers: dict[str, str] = {}
        url_key = endpoint if endpoint.startswith("http") else f"/{endpoint.lstrip('/')}"
        cache_key = f"{method}:{url_key}:{sorted((params or {}).items())}"

        if method == "GET" and cache_key in self._etag_cache:
            etag, _ = self._etag_cache[cache_key]
            request_headers["If-None-Match"] = etag

        for attempt in range(MAX_RETRIES):
            response = await client.request(
                method,
                endpoint if endpoint.startswith("http") else f"/{endpoint.lstrip('/')}",
                params=all_params,
                data=data,
                headers=request_headers,
            )

            # ALWAYS parse rate limit headers, even on success or 304
            self.rate_limiter.update_from_response(response, ad_account)

            # ETag cache hit — return cached response (still counts toward rate limits)
            if response.status_code == 304 and cache_key in self._etag_cache:
                _, cached = self._etag_cache[cache_key]
                return cached

            if response.status_code == 200:
                result = response.json()
                # Cache ETag if present
                etag = response.headers.get("etag")
                if etag and method == "GET":
                    self._etag_cache[cache_key] = (etag, result)
                # Invalidate the full ETag cache on any write — Meta may still
                # return 304 on subsequent reads for list/parent endpoints even
                # though a child resource changed, serving stale state to the UI.
                # Writes on a sub-resource (campaign/adset/ad) often have no
                # ad_account in the endpoint path, so scoping by account misses
                # these. A full clear is cheap and correct.
                if is_write:
                    self._etag_cache.clear()
                # Audit log every API call. Writes are enriched via audit_context;
                # reads get a lightweight entry so the trail reflects all activity.
                ctx = audit_context or {}
                audit = get_audit_log()
                if is_write:
                    audit.log_write(
                        operation=ctx.get("operation", method.lower()),
                        endpoint=endpoint,
                        resource_id=ctx.get("resource_id") or _extract_resource_id(endpoint, ad_account),
                        before_state=ctx.get("before_state"),
                        after_state=ctx.get("after_state"),
                        request_payload=data,
                        response_code=200,
                        response_body=result,
                        buc_utilization=self.rate_limiter.get_usage_summary(ad_account),
                        user_confirmed=ctx.get("user_confirmed", False),
                    )
                else:
                    audit.log_read(
                        endpoint=endpoint,
                        ad_account=ad_account,
                        operation=ctx.get("operation", "read"),
                        resource_id=ctx.get("resource_id") or _extract_resource_id(endpoint, ad_account),
                        response_code=200,
                    )
                return result

            # Parse error
            body = response.json() if response.headers.get("content-type", "").startswith("application/json") else {}
            error = body.get("error", {})
            code = error.get("code", 0)
            subcode = error.get("error_subcode", 0)
            msg = sanitize_token(error.get("message", response.text))
            fbtrace = error.get("fbtrace_id", "")

            # Token expired/invalid — do NOT retry, token needs replacement
            if code == TOKEN_EXPIRED_CODE:
                raise TokenExpiredError(
                    f"Access token expired or invalidated: {msg}. "
                    f"Generate a new token (System User tokens are recommended).",
                    code=code, subcode=subcode, fbtrace_id=fbtrace,
                )

            # Abuse detection — circuit breaker, do NOT retry
            if (code, subcode) in ABUSE_CODES:
                self.rate_limiter.trip_circuit_breaker()
                raise AbuseDetectionError(
                    f"Meta abuse detection triggered (code={code}, subcode={subcode}): {msg}. "
                    f"All requests blocked for {self.rate_limiter.circuit_breaker_cooldown}s. "
                    f"Reduce your request volume and frequency immediately.",
                    code=code, subcode=subcode, fbtrace_id=fbtrace,
                )

            # Rate limit — retry with backoff
            if code in RATE_LIMIT_CODES or response.status_code == 429:
                if attempt < MAX_RETRIES - 1:
                    # Use estimated_time_to_regain_access from headers if available
                    wait = self._calculate_backoff(attempt, ad_account)
                    logger.warning(
                        "Rate limited (code=%d, subcode=%d, attempt=%d/%d) — waiting %.1fs: %s",
                        code, subcode, attempt + 1, MAX_RETRIES, wait, msg,
                    )
                    await asyncio.sleep(wait)
                    # Re-check circuit breaker and proactive limits before retry
                    await self.rate_limiter.wait_if_needed(ad_account)
                    continue
                last_error = RateLimitError(msg, code=code, subcode=subcode, fbtrace_id=fbtrace)
                break

            # Non-retryable API error
            raise MetaAPIError(msg, code=code, subcode=subcode, fbtrace_id=fbtrace)

        if last_error:
            raise last_error
        raise MetaAPIError("Max retries exceeded")

    def _calculate_backoff(self, attempt: int, ad_account: Optional[str] = None) -> float:
        """Calculate backoff delay with jitter and header-based wait time."""
        # Exponential backoff: 1, 2, 4, 8, 16...
        base = min(BASE_BACKOFF * (2 ** attempt), MAX_BACKOFF)

        # Check if we have estimated_time_to_regain_access from headers
        if ad_account and ad_account in self.rate_limiter._usage:
            eta_minutes = self.rate_limiter._usage[ad_account].estimated_time_to_regain_access
            if eta_minutes > 0:
                base = max(base, eta_minutes * 60)

        # Add jitter (0-25% of base)
        jitter = random.uniform(0, base * 0.25)
        return base + jitter

    async def get(self, endpoint: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """Make an authenticated GET request."""
        return await self.request("GET", endpoint, params=params)

    async def post(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Make an authenticated POST request."""
        return await self.request("POST", endpoint, params=params, data=data)

    async def delete(self, endpoint: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """Make an authenticated DELETE request."""
        return await self.request("DELETE", endpoint, params=params)

    async def post_files(
        self,
        endpoint: str,
        files: dict[str, Any],
        params: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Upload files via multipart POST.

        Args:
            endpoint: API path (e.g. "act_123/adimages").
            files: Dict of file fields for multipart upload.
            params: Additional query parameters.

        Returns:
            Parsed JSON response.

        Raises:
            MetaAPIError: On API errors.
        """
        ad_account = _extract_ad_account(endpoint)
        await self.rate_limiter.wait_if_needed(ad_account)

        client = await self._get_client()
        all_params = {**self._auth_params(), **(params or {})}
        response = await client.post(
            f"/{endpoint.lstrip('/')}",
            params=all_params,
            files=files,
        )

        self.rate_limiter.update_from_response(response, ad_account)

        if response.status_code == 200:
            return response.json()
        body = response.json() if response.headers.get("content-type", "").startswith("application/json") else {}
        error = body.get("error", {})
        raise MetaAPIError(
            sanitize_token(error.get("message", response.text)),
            code=error.get("code", 0),
            subcode=error.get("error_subcode", 0),
            fbtrace_id=error.get("fbtrace_id", ""),
        )

    async def get_all_pages(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
        max_pages: int = 50,
    ) -> list[dict[str, Any]]:
        """Fetch all pages of a paginated GET endpoint.

        Uses cursor-based pagination with rate-limit-aware delays between pages.

        Args:
            endpoint: API path.
            params: Query parameters for the first request.
            max_pages: Maximum number of pages to fetch (safety limit).

        Returns:
            Combined list of all data items across all pages.
        """
        all_data: list[dict[str, Any]] = []
        result = await self.get(endpoint, params=params)
        all_data.extend(result.get("data", []))

        pages = 1
        while pages < max_pages:
            next_url = result.get("paging", {}).get("next")
            if not next_url:
                break
            result = await self.get(next_url)
            all_data.extend(result.get("data", []))
            pages += 1

        return all_data

    async def batch(
        self,
        requests: list[dict[str, Any]],
        max_batch_size: int = 50,
    ) -> list[dict[str, Any]]:
        """Execute multiple API calls in a single batch request.

        Each request in the batch counts individually toward rate limits,
        but reduces HTTP overhead. Meta allows up to 50 requests per batch.

        Args:
            requests: List of dicts with keys:
                - method: HTTP method (GET, POST, DELETE)
                - relative_url: API path (e.g. "v25.0/act_123/campaigns")
                - body: (optional) URL-encoded body for POST
            max_batch_size: Max requests per batch (Meta limit: 50).

        Returns:
            List of response dicts with keys: code, headers, body.

        Example:
            results = await client.batch([
                {"method": "GET", "relative_url": "v25.0/act_123/campaigns?fields=name,status"},
                {"method": "GET", "relative_url": "v25.0/act_456/campaigns?fields=name,status"},
            ])
        """
        all_results: list[dict[str, Any]] = []

        for i in range(0, len(requests), max_batch_size):
            chunk = requests[i:i + max_batch_size]
            await self.rate_limiter.wait_if_needed()

            client = await self._get_client()
            import json as _json
            response = await client.post(
                "/",
                params=self._auth_params(),
                data={"batch": _json.dumps(chunk)},
            )

            self.rate_limiter.update_from_response(response)

            if response.status_code != 200:
                body = response.json() if response.headers.get("content-type", "").startswith("application/json") else {}
                error = body.get("error", {})
                raise MetaAPIError(
                    error.get("message", response.text),
                    code=error.get("code", 0),
                    subcode=error.get("error_subcode", 0),
                )

            batch_results = response.json()
            for item in batch_results:
                if item is None:
                    # Timed out — Meta returns null for unfinished items
                    all_results.append({"code": 504, "body": '{"error": "Batch item timed out"}'})
                else:
                    all_results.append(item)

        return all_results

    async def get_insights_async(
        self,
        ad_object_id: str,
        params: Optional[dict[str, Any]] = None,
        poll_interval: float = 5.0,
        max_poll_attempts: int = 120,
    ) -> list[dict[str, Any]]:
        """Fetch insights using async report pattern (POST -> poll -> GET).

        For large datasets, Meta recommends async reports over synchronous calls.
        This method creates a report run, polls until complete, then fetches results.

        Args:
            ad_object_id: The ad object ID (e.g. "act_123", campaign ID, etc.)
            params: Query parameters (fields, breakdowns, date_preset, etc.)
            poll_interval: Seconds between poll attempts (default 5s).
            max_poll_attempts: Max polls before timeout (default 120 = 10 minutes).

        Returns:
            List of insight data dicts.

        Raises:
            MetaAPIError: If the report job fails or times out.
        """
        # Step 1: Create async report run
        result = await self.post(f"{ad_object_id}/insights", params=params)
        report_run_id = result.get("report_run_id")
        if not report_run_id:
            # If response has data directly, it was a sync response — return it
            if "data" in result:
                return result["data"]
            raise MetaAPIError(f"No report_run_id in response: {result}")

        # Step 2: Poll until complete
        for attempt in range(max_poll_attempts):
            await asyncio.sleep(poll_interval)
            status = await self.get(report_run_id)

            async_status = status.get("async_status")
            pct = status.get("async_percent_completion", 0)

            if async_status == "Job Completed" and pct == 100:
                break
            elif async_status in ("Job Failed", "Job Skipped"):
                raise MetaAPIError(
                    f"Async insights job {async_status}: {status}",
                    code=0, subcode=0,
                )

            logger.info(
                "Insights report %s: %s (%d%%) — poll %d/%d",
                report_run_id, async_status, pct, attempt + 1, max_poll_attempts,
            )
        else:
            raise MetaAPIError(
                f"Async insights job timed out after {max_poll_attempts} polls "
                f"({max_poll_attempts * poll_interval}s)",
            )

        # Step 3: Fetch results (paginated)
        return await self.get_all_pages(f"{report_run_id}/insights")

    async def close(self):
        """Close the underlying HTTP client."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()


# ---------------------------------------------------------------------------
# Singleton factory — all tool modules share ONE client with ONE rate limiter
# Pattern: facebook-python-business-sdk FacebookAdsApi.get_default_api()
# ---------------------------------------------------------------------------

_shared_client: Optional[MetaClient] = None


def get_client() -> MetaClient:
    """Get or create the shared MetaClient singleton.

    All tool modules should use this instead of creating their own MetaClient.
    This ensures a single RateLimiter and httpx connection pool across all tools.
    """
    global _shared_client
    if _shared_client is None:
        _shared_client = MetaClient()
    return _shared_client


async def close_client():
    """Close and reset the shared MetaClient. Called by server lifespan on shutdown."""
    global _shared_client
    if _shared_client is not None:
        await _shared_client.close()
        _shared_client = None
