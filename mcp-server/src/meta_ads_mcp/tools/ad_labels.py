"""Auto-generated Meta Marketing API tools — ad_labels."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_LABEL_FIELDS = [
    "account",
    "created_time",
    "id",
    "name",
    "updated_time"
]


async def get_ad_label_adcreatives(ad_label_id: str, fields: Optional[str] = None) -> str:
    """GET /adcreatives on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_label_id}/adcreatives", params=params)
    return json.dumps(result, indent=2)


async def get_ad_label_ads(ad_label_id: str, fields: Optional[str] = None) -> str:
    """GET /ads on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_label_id}/ads", params=params)
    return json.dumps(result, indent=2)


async def get_ad_label_adsets(ad_label_id: str, fields: Optional[str] = None) -> str:
    """GET /adsets on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_label_id}/adsets", params=params)
    return json.dumps(result, indent=2)


async def get_ad_label_campaigns(ad_label_id: str, fields: Optional[str] = None) -> str:
    """GET /campaigns on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_label_id}/campaigns", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_label(ad_label_id: str) -> str:
    """DELETE /#delete on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
    """
    params = {}
    result = await get_client().delete(f"{ad_label_id}")
    return json.dumps(result, indent=2)


async def get_ad_label(ad_label_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        fields: Comma-separated list of fields to return. Available: account, created_time, id, name, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_label_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_label(ad_label_id: str, name: str) -> str:
    """POST /#update on AdLabel.

    Args:
        ad_label_id: The ID of the AdLabel object.
        name: Required.
    """
    params = {}
    params["name"] = name
    result = await get_client().post(f"{ad_label_id}", data=params)
    return json.dumps(result, indent=2)

