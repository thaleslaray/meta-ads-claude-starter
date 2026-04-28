"""Generic Meta Graph API tool — the escape hatch for any endpoint."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


async def meta_api_call(
    method: str,
    endpoint: str,
    params: Optional[str] = None,
    data: Optional[str] = None,
) -> str:
    """Make a raw Meta Graph API v25.0 call to ANY endpoint.

    Use this when no specific tool exists for what you need.
    The base URL is https://graph.facebook.com/v25.0 — pass only the path.

    Args:
        method: HTTP method — GET, POST, DELETE
        endpoint: API path — e.g. "act_123/customaudiences", "123456/feed"
        params: JSON string of query parameters
        data: JSON string of POST body data

    Examples:
        Get page posts: method="GET", endpoint="{page_id}/feed", params='{"fields":"message,created_time"}'
        Create custom audience: method="POST", endpoint="act_123/customaudiences", data='{"name":"My Audience","subtype":"CUSTOM"}'
    """
    parsed_params = json.loads(params) if params else None
    parsed_data = json.loads(data) if data else None
    result = await get_client().request(method, endpoint, params=parsed_params, data=parsed_data)
    return json.dumps(result, indent=2)
