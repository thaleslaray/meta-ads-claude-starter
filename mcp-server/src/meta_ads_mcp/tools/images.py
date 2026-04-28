"""Auto-generated Meta Marketing API tools — images."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_IMAGE_FIELDS = [
    "account_id",
    "created_time",
    "creatives",
    "hash",
    "height",
    "id",
    "is_associated_creatives_in_adgroups",
    "name",
    "original_height",
    "original_width",
    "owner_business",
    "permalink_url",
    "status",
    "updated_time",
    "url",
    "url_128",
    "width"
]


async def get_ad_image(ad_image_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdImage.

    Args:
        ad_image_id: The ID of the AdImage object.
        fields: Comma-separated list of fields to return. Available: account_id, created_time, creatives, hash, height, id, is_associated_creatives_in_adgroups, name, original_height, original_width, owner_business, permalink_url, status, updated_time, url, url_128, width
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_image_id}", params=params)
    return json.dumps(result, indent=2)

