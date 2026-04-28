"""Token introspection and validation for Meta API access tokens.

Validates tokens on startup by calling the debug_token endpoint and /me.
Detects token type, permissions, expiration, and access tier.
"""

import logging
import time
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger("meta_ads_mcp.token_info")

# Error code 190 = expired/invalid token
TOKEN_EXPIRED_CODE = 190


@dataclass
class TokenInfo:
    """Parsed token metadata from Meta's debug_token endpoint."""
    is_valid: bool = False
    token_type: str = "unknown"  # "USER", "SYSTEM_USER", "PAGE", "APP"
    app_id: str = ""
    user_id: str = ""
    scopes: list[str] = field(default_factory=list)
    expires_at: int = 0  # Unix timestamp, 0 = never expires
    issued_at: int = 0
    error_message: str = ""

    @property
    def is_system_user(self) -> bool:
        return self.token_type == "SYSTEM_USER"

    @property
    def is_personal(self) -> bool:
        return self.token_type == "USER"

    @property
    def never_expires(self) -> bool:
        return self.expires_at == 0

    @property
    def is_expired(self) -> bool:
        if self.never_expires:
            return False
        return self.expires_at < time.time()

    @property
    def expires_in_days(self) -> Optional[float]:
        if self.never_expires:
            return None
        remaining = self.expires_at - time.time()
        return max(0, remaining / 86400)

    @property
    def has_ads_read(self) -> bool:
        return "ads_read" in self.scopes

    @property
    def has_ads_management(self) -> bool:
        return "ads_management" in self.scopes

    @property
    def has_business_management(self) -> bool:
        return "business_management" in self.scopes


async def validate_token(client: Any) -> TokenInfo:
    """Validate the access token by calling /me and debug_token.

    Makes two lightweight API calls:
    1. GET /me — verifies token works, gets user/system user ID
    2. GET /debug_token — gets token metadata (type, scopes, expiration)

    Args:
        client: MetaClient instance (uses its raw httpx client to avoid
                circular validation — we need to check the token before
                the rate limiter is fully active).

    Returns:
        TokenInfo with all discovered metadata.
    """
    info = TokenInfo()

    # Step 1: Quick validation via /me
    try:
        me_result = await client.get("me", params={"fields": "id,name"})
        info.user_id = me_result.get("id", "")
        info.is_valid = True
    except Exception as e:
        info.is_valid = False
        info.error_message = str(e)
        return info

    # Step 2: Token introspection via debug_token
    try:
        debug_result = await client.get(
            "debug_token",
            params={"input_token": client._token},
        )
        data = debug_result.get("data", {})

        info.token_type = data.get("type", "unknown").upper()
        info.app_id = str(data.get("app_id", ""))
        info.scopes = data.get("scopes", [])
        info.expires_at = data.get("expires_at", 0)
        info.issued_at = data.get("issued_at", 0)
        info.is_valid = data.get("is_valid", False)

        if not info.is_valid:
            error = data.get("error", {})
            info.error_message = error.get("message", "Token is not valid")

    except Exception as e:
        # debug_token may fail if token lacks app-level access,
        # but /me succeeded so the token works for API calls
        logger.debug("debug_token failed (token still usable): %s", e)

    return info


def log_token_warnings(info: TokenInfo, write_mode: bool = False) -> list[str]:
    """Log warnings about token issues and return list of warning messages.

    Args:
        info: TokenInfo from validate_token()
        write_mode: Whether write operations are enabled

    Returns:
        List of warning message strings (empty if no issues)
    """
    warnings = []

    if not info.is_valid:
        msg = f"TOKEN INVALID: {info.error_message}"
        logger.error(msg)
        warnings.append(msg)
        return warnings

    # Token type warnings
    if info.is_personal:
        msg = (
            "Using PERSONAL user token — this is NOT recommended for production. "
            "Personal tokens expire and are tied to your personal Facebook account. "
            "Use a System User token from Business Manager instead."
        )
        logger.warning(msg)
        warnings.append(msg)

    if info.is_system_user:
        logger.info("Using System User token (recommended)")

    # Expiration warnings
    if info.is_expired:
        msg = "TOKEN EXPIRED — all API calls will fail. Generate a new token."
        logger.error(msg)
        warnings.append(msg)
    elif not info.never_expires and info.expires_in_days is not None:
        days = info.expires_in_days
        if days < 7:
            msg = f"Token expires in {days:.1f} days — renew soon!"
            logger.warning(msg)
            warnings.append(msg)
        elif days < 30:
            msg = f"Token expires in {days:.0f} days"
            logger.info(msg)

    # Permission warnings
    if not info.has_ads_read:
        msg = (
            "Token lacks 'ads_read' permission — most ad-related tools will fail. "
            "Request this permission in App Review."
        )
        logger.warning(msg)
        warnings.append(msg)

    if write_mode and not info.has_ads_management:
        msg = (
            "META_ADS_WRITE_MODE is enabled but token lacks 'ads_management' permission. "
            "Write operations will fail. Request this permission in App Review."
        )
        logger.warning(msg)
        warnings.append(msg)

    # Scope summary
    if info.scopes:
        logger.info("Token scopes: %s", ", ".join(info.scopes))

    return warnings
