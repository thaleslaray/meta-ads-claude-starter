"""Auto-generated Meta Marketing API tools — rules."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_RULE_FIELDS = [
    "account_id",
    "created_by",
    "created_time",
    "disable_error_code",
    "evaluation_spec",
    "execution_spec",
    "id",
    "name",
    "schedule_spec",
    "status",
    "updated_time"
]


async def create_ad_rule_execute(ad_rule_id: str) -> str:
    """POST /execute on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
    """
    params = {}
    result = await get_client().post(f"{ad_rule_id}/execute", data=params)
    return json.dumps(result, indent=2)


async def get_ad_rule_history(
    ad_rule_id: str,
    fields: Optional[str] = None,
    action: Optional[str] = None,
    hide_no_changes: Optional[bool] = None,
    object_id: Optional[str] = None,
) -> str:
    """GET /history on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
        fields: Comma-separated list of fields to return.
        action: Optional. Values: BUDGET_NOT_REDISTRIBUTED, CHANGED_BID, CHANGED_BUDGET, CONSOLIDATE_ASC_FRAGMENTATION, CONSOLIDATE_FRAGMENTATION, CONVERT_ASC_CP_SINGLE_INSTANCE, EMAIL, ENABLE_ADVANTAGE_CAMPAIGN_BUDGET, ENABLE_ADVANTAGE_PLUS_AUDIENCE, ENABLE_ADVANTAGE_PLUS_CREATIVE, ENABLE_ADVANTAGE_PLUS_PLACEMENTS, ENABLE_AUTOFLOW, ENABLE_GEN_UNCROP, ENABLE_LANDING_PAGE_VIEWS, ENABLE_MUSIC, ENABLE_PRODUCT_SET_BOOSTING, ENABLE_REELS_PLACEMENTS, ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION, ENABLE_SHOPS_ADS, ENDPOINT_PINGED, ERROR, FACEBOOK_NOTIFICATION_SENT, MESSAGE_SENT, NOT_CHANGED, PAUSED, UNPAUSED
        hide_no_changes: Optional.
        object_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if action is not None:
        params["action"] = action
    if hide_no_changes is not None:
        params["hide_no_changes"] = hide_no_changes
    if object_id is not None:
        params["object_id"] = object_id
    result = await get_client().get(f"{ad_rule_id}/history", params=params)
    return json.dumps(result, indent=2)


async def create_ad_rule_preview(ad_rule_id: str) -> str:
    """POST /preview on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
    """
    params = {}
    result = await get_client().post(f"{ad_rule_id}/preview", data=params)
    return json.dumps(result, indent=2)


async def delete_ad_rule(ad_rule_id: str) -> str:
    """DELETE /#delete on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
    """
    params = {}
    result = await get_client().delete(f"{ad_rule_id}")
    return json.dumps(result, indent=2)


async def get_ad_rule(ad_rule_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
        fields: Comma-separated list of fields to return. Available: account_id, created_by, created_time, disable_error_code, evaluation_spec, execution_spec, id, name, schedule_spec, status, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_rule_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_rule(
    ad_rule_id: str,
    evaluation_spec: Optional[str] = None,
    execution_spec: Optional[str] = None,
    name: Optional[str] = None,
    schedule_spec: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """POST /#update on AdRule.

    Args:
        ad_rule_id: The ID of the AdRule object.
        evaluation_spec: Optional.
        execution_spec: Optional.
        name: Optional.
        schedule_spec: Optional.
        status: Optional.
    """
    params = {}
    if evaluation_spec is not None:
        params["evaluation_spec"] = evaluation_spec
    if execution_spec is not None:
        params["execution_spec"] = execution_spec
    if name is not None:
        params["name"] = name
    if schedule_spec is not None:
        params["schedule_spec"] = schedule_spec
    if status is not None:
        params["status"] = status
    result = await get_client().post(f"{ad_rule_id}", data=params)
    return json.dumps(result, indent=2)

