"""Auto-generated Meta Marketing API tools — publisher_block_lists."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


PUBLISHER_BLOCK_LIST_FIELDS = [
    "app_publishers",
    "business_owner_id",
    "id",
    "is_auto_blocking_on",
    "is_eligible_at_campaign_level",
    "last_update_time",
    "last_update_user",
    "name",
    "owner_ad_account_id",
    "web_publishers"
]


async def create_publisher_block_list_append_publisher_urls(publisher_block_list_id: str, publisher_urls: str) -> str:
    """POST /append_publisher_urls on PublisherBlockList.

    Args:
        publisher_block_list_id: The ID of the PublisherBlockList object.
        publisher_urls: Required.
    """
    params = {}
    params["publisher_urls"] = publisher_urls
    result = await get_client().post(f"{publisher_block_list_id}/append_publisher_urls", data=params)
    return json.dumps(result, indent=2)


async def get_publisher_block_list_paged_web_publishers(
    publisher_block_list_id: str,
    fields: Optional[str] = None,
    draft_id: Optional[str] = None,
) -> str:
    """GET /paged_web_publishers on PublisherBlockList.

    Args:
        publisher_block_list_id: The ID of the PublisherBlockList object.
        fields: Comma-separated list of fields to return.
        draft_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if draft_id is not None:
        params["draft_id"] = draft_id
    result = await get_client().get(f"{publisher_block_list_id}/paged_web_publishers", params=params)
    return json.dumps(result, indent=2)


async def delete_publisher_block_list(publisher_block_list_id: str) -> str:
    """DELETE /#delete on PublisherBlockList.

    Args:
        publisher_block_list_id: The ID of the PublisherBlockList object.
    """
    params = {}
    result = await get_client().delete(f"{publisher_block_list_id}")
    return json.dumps(result, indent=2)


async def get_publisher_block_list(
    publisher_block_list_id: str,
    fields: Optional[str] = None,
    account_id: Optional[int] = None,
    business_id: Optional[str] = None,
    draft_id: Optional[str] = None,
) -> str:
    """GET /#get on PublisherBlockList.

    Args:
        publisher_block_list_id: The ID of the PublisherBlockList object.
        fields: Comma-separated list of fields to return. Available: app_publishers, business_owner_id, id, is_auto_blocking_on, is_eligible_at_campaign_level, last_update_time, last_update_user, name, owner_ad_account_id, web_publishers
        account_id: Optional.
        business_id: Optional.
        draft_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if account_id is not None:
        params["account_id"] = account_id
    if business_id is not None:
        params["business_id"] = business_id
    if draft_id is not None:
        params["draft_id"] = draft_id
    result = await get_client().get(f"{publisher_block_list_id}", params=params)
    return json.dumps(result, indent=2)


async def update_publisher_block_list(publisher_block_list_id: str, spec: str) -> str:
    """POST /#update on PublisherBlockList.

    Args:
        publisher_block_list_id: The ID of the PublisherBlockList object.
        spec: Required.
    """
    params = {}
    params["spec"] = spec
    result = await get_client().post(f"{publisher_block_list_id}", data=params)
    return json.dumps(result, indent=2)


CONTENT_BLOCK_LIST_FIELDS = [
    "business",
    "id",
    "name"
]


async def get_content_block_list_applied_ad_accounts(content_block_list_id: str, fields: Optional[str] = None) -> str:
    """GET /applied_ad_accounts on ContentBlockList.

    Args:
        content_block_list_id: The ID of the ContentBlockList object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{content_block_list_id}/applied_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_content_block_list_facebook_content(content_block_list_id: str, fields: Optional[str] = None) -> str:
    """GET /facebook_content on ContentBlockList.

    Args:
        content_block_list_id: The ID of the ContentBlockList object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{content_block_list_id}/facebook_content", params=params)
    return json.dumps(result, indent=2)


async def get_content_block_list_instagram_content(content_block_list_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_content on ContentBlockList.

    Args:
        content_block_list_id: The ID of the ContentBlockList object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{content_block_list_id}/instagram_content", params=params)
    return json.dumps(result, indent=2)


async def get_content_block_list(content_block_list_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ContentBlockList.

    Args:
        content_block_list_id: The ID of the ContentBlockList object.
        fields: Comma-separated list of fields to return. Available: business, id, name
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{content_block_list_id}", params=params)
    return json.dumps(result, indent=2)

