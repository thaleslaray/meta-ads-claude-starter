"""Rate limit status and usage monitoring tools."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


async def rate_limit_status(ad_account_id: Optional[str] = None) -> str:
    """Check current Meta API rate limit usage and remaining quota.

    Shows how much of your rate limit budget you've consumed, which tier
    you're on (development=60pts/hr vs standard=9,000pts/hr), and whether
    the circuit breaker is active.

    Call this anytime to check if it's safe to make more API calls.

    Args:
        ad_account_id: Ad account to check (e.g. "act_487731909607599").
            If not provided, shows app-level usage only.

    Returns:
        JSON with current usage percentages, tier, and status.
    """
    client = get_client()
    summary = client.rate_limiter.get_usage_summary(ad_account_id)

    # Add human-readable interpretation
    status = "OK"
    if summary.get("circuit_breaker_open"):
        status = "BLOCKED — Circuit breaker active (abuse detection triggered)"
    elif "account_usage" in summary:
        max_pct = max(
            summary["account_usage"].get("call_count", 0),
            summary["account_usage"].get("total_cputime", 0),
            summary["account_usage"].get("total_time", 0),
        )
        if max_pct >= 80:
            status = f"PAUSED — Usage at {max_pct:.0f}% (waiting for reset)"
        elif max_pct >= 60:
            status = f"THROTTLED — Usage at {max_pct:.0f}% (slowing down)"
        else:
            status = f"OK — Usage at {max_pct:.0f}%"

    # Calculate remaining points estimate
    tier = "development_access"
    max_points = 60
    if "account_usage" in summary:
        tier = summary["account_usage"].get("ads_api_access_tier", "development_access")
        if tier == "standard_access":
            max_points = 9000
        used_pct = summary["account_usage"].get("acc_id_util_pct", 0)
        remaining_points = max(0, max_points - (max_points * used_pct / 100))
    else:
        used_pct = summary["app_usage"].get("call_count", 0)
        remaining_points = max(0, max_points - (max_points * used_pct / 100))

    result = {
        "status": status,
        "tier": tier,
        "max_points_per_hour": max_points,
        "used_percentage": round(used_pct, 1),
        "remaining_points_estimate": round(remaining_points),
        "read_calls_remaining": round(remaining_points),  # reads = 1 point
        "write_calls_remaining": round(remaining_points / 3),  # writes = 3 points
        "circuit_breaker": summary["circuit_breaker_open"],
        "raw": summary,
    }

    return json.dumps(result, indent=2)
