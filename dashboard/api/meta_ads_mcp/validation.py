"""Input validation for Meta Graph API requests.

Validates parameters before sending to prevent user errors (HTTP 400s)
that actively reduce the rate limit quota via Meta's formula:
    Calls/hour = base + factor * Active_Ads - 0.001 * User_Errors

Catching bad requests client-side preserves rate limit headroom.
"""

import re
from typing import Any, Optional

# Valid ad account ID pattern
_AD_ACCOUNT_RE = re.compile(r"^act_\d+$")

# Valid object ID pattern (numeric or act_ prefixed)
_OBJECT_ID_RE = re.compile(r"^(act_)?\d+$")

# Known date presets from Meta docs
VALID_DATE_PRESETS = {
    "today", "yesterday", "this_month", "last_month",
    "this_quarter", "maximum", "data_maximum",
    "last_3d", "last_7d", "last_14d", "last_28d", "last_30d",
    "last_90d", "last_week_mon_sun", "last_week_sun_sat",
    "last_quarter", "last_year", "this_week_mon_today",
    "this_week_sun_today", "this_year",
}

# Known effective statuses
VALID_EFFECTIVE_STATUSES = {
    "ACTIVE", "PAUSED", "DELETED", "ARCHIVED",
    "IN_PROCESS", "WITH_ISSUES", "CAMPAIGN_PAUSED",
    "ADSET_PAUSED", "DISAPPROVED", "PENDING_REVIEW",
    "PREAPPROVED", "PENDING_BILLING_INFO",
}

# Known campaign objectives
VALID_OBJECTIVES = {
    "OUTCOME_AWARENESS", "OUTCOME_ENGAGEMENT", "OUTCOME_LEADS",
    "OUTCOME_SALES", "OUTCOME_TRAFFIC", "OUTCOME_APP_PROMOTION",
}

# Characters that should never appear in field names
_INVALID_FIELD_CHARS = re.compile(r"[^a-zA-Z0-9_,.\s]")


class ValidationError(Exception):
    """Raised when input validation fails. Not sent to Meta API."""
    pass


def validate_object_id(value: str, name: str = "object_id") -> str:
    """Validate a Meta object ID (numeric or act_ prefixed)."""
    value = value.strip()
    if not value:
        raise ValidationError(f"{name} cannot be empty")
    if not _OBJECT_ID_RE.match(value):
        raise ValidationError(
            f"{name}='{value}' is not a valid Meta object ID. "
            f"Expected numeric ID or 'act_' prefix (e.g., 'act_123456', '789012')."
        )
    return value


def validate_ad_account_id(value: str) -> str:
    """Validate an ad account ID (must be act_ prefixed)."""
    value = value.strip()
    if not value:
        raise ValidationError("ad_account_id cannot be empty")
    if not _AD_ACCOUNT_RE.match(value):
        raise ValidationError(
            f"ad_account_id='{value}' is not valid. "
            f"Expected format: 'act_123456'. "
            f"Did you forget the 'act_' prefix?"
        )
    return value


def validate_fields(fields: Optional[str]) -> Optional[str]:
    """Validate a comma-separated fields parameter."""
    if not fields:
        return fields
    fields = fields.strip()
    if _INVALID_FIELD_CHARS.search(fields):
        raise ValidationError(
            f"fields='{fields}' contains invalid characters. "
            f"Fields should be comma-separated alphanumeric names (e.g., 'id,name,status')."
        )
    return fields


def validate_date_preset(preset: Optional[str]) -> Optional[str]:
    """Validate a date_preset parameter."""
    if not preset:
        return preset
    preset = preset.strip().lower()
    if preset not in VALID_DATE_PRESETS:
        raise ValidationError(
            f"date_preset='{preset}' is not valid. "
            f"Valid values: {', '.join(sorted(VALID_DATE_PRESETS))}"
        )
    return preset


def validate_effective_status(status: Optional[str]) -> Optional[str]:
    """Validate effective_status filter values."""
    if not status:
        return status
    invalid = []
    for s in status.split(","):
        s = s.strip().upper()
        if s and s not in VALID_EFFECTIVE_STATUSES:
            invalid.append(s)
    if invalid:
        raise ValidationError(
            f"effective_status contains invalid values: {invalid}. "
            f"Valid values: {', '.join(sorted(VALID_EFFECTIVE_STATUSES))}"
        )
    return status


def validate_limit(limit: Optional[int], max_value: int = 500) -> Optional[int]:
    """Validate a pagination limit parameter."""
    if limit is None:
        return limit
    if not isinstance(limit, int) or limit < 1:
        raise ValidationError(f"limit must be a positive integer, got {limit}")
    if limit > max_value:
        raise ValidationError(
            f"limit={limit} exceeds maximum ({max_value}). "
            f"Large limits increase response time and rate limit cost."
        )
    return limit


def validate_time_range(time_range: Optional[str]) -> Optional[str]:
    """Validate a time_range JSON parameter."""
    if not time_range:
        return time_range
    import json
    try:
        data = json.loads(time_range)
    except json.JSONDecodeError:
        raise ValidationError(
            f"time_range must be valid JSON. "
            f'Expected format: \'{{"since":"2026-01-01","until":"2026-03-01"}}\''
        )
    if not isinstance(data, dict):
        raise ValidationError("time_range must be a JSON object with 'since' and 'until' keys")
    if "since" not in data or "until" not in data:
        raise ValidationError(
            f"time_range must contain 'since' and 'until' keys. "
            f'Got: {list(data.keys())}'
        )
    return time_range


def validate_request_params(
    endpoint: str,
    params: Optional[dict[str, Any]] = None,
) -> Optional[dict[str, Any]]:
    """Validate common parameters in a request before sending to Meta.

    Does not modify params — raises ValidationError on bad input.
    Returns params unchanged if valid.
    """
    if not params:
        return params

    if "fields" in params:
        validate_fields(params["fields"])

    if "date_preset" in params:
        validate_date_preset(params["date_preset"])

    if "effective_status" in params:
        validate_effective_status(params["effective_status"])

    if "limit" in params:
        validate_limit(params["limit"])

    if "time_range" in params and isinstance(params["time_range"], str):
        validate_time_range(params["time_range"])

    return params
