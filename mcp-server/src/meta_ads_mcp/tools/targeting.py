"""Targeting search tools — manually defined (not a codegen node)."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


async def search_targeting(
    type: str,
    q: str,
    locale: Optional[str] = None,
    limit: Optional[int] = None,
) -> str:
    """Search for targeting options (interests, behaviors, demographics, etc).

    Args:
        type: Search type — adinterest, adinterestsuggestion, adinterestvalid,
              adTargetingCategory, adgeolocation, adlocale, adeducationschool,
              adeducationmajor, adworkemployer, adworkposition
        q: Search query string
        locale: Locale for results (e.g., 'pt_BR', 'en_US')
        limit: Max results to return
    """
    params: dict = {"type": type, "q": q}
    if locale:
        params["locale"] = locale
    if limit:
        params["limit"] = limit
    result = await get_client().get("search", params=params)
    return json.dumps(result, indent=2)


async def get_broad_targeting_categories(
    account_id: str,
) -> str:
    """Get broad targeting categories for an ad account.

    Args:
        account_id: Ad account ID (without 'act_' prefix — added automatically)
    """
    result = await get_client().get(f"act_{account_id}/broadtargetingcategories")
    return json.dumps(result, indent=2)


async def get_targeting_sentence_lines(
    account_id: str,
    targeting_spec: str,
) -> str:
    """Get human-readable description of a targeting spec.

    Args:
        account_id: Ad account ID
        targeting_spec: JSON string of targeting spec to describe
    """
    params = {"targeting_spec": targeting_spec}
    result = await get_client().get(f"act_{account_id}/targetingsentencelines", params=params)
    return json.dumps(result, indent=2)
