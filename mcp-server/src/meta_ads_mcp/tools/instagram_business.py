"""Auto-generated Meta Marketing API tools — instagram_business."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


INSTAGRAM_BUSINESS_ASSET_FIELDS = [
    "id",
    "ig_user_id",
    "ig_username"
]


async def delete_instagram_business_asset_agencies(instagram_business_asset_id: str, business: str) -> str:
    """DELETE /agencies on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{instagram_business_asset_id}/agencies")
    return json.dumps(result, indent=2)


async def get_instagram_business_asset_agencies(instagram_business_asset_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{instagram_business_asset_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_instagram_business_asset_agencies(instagram_business_asset_id: str, business: str, permitted_tasks: str) -> str:
    """POST /agencies on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        business: Required.
        permitted_tasks: Required. Values: ADVERTISE, ANALYZE, COMMUNITY_ACTIVITY, CONTENT, MESSAGES
    """
    params = {}
    params["business"] = business
    params["permitted_tasks"] = permitted_tasks
    result = await get_client().post(f"{instagram_business_asset_id}/agencies", data=params)
    return json.dumps(result, indent=2)


async def delete_instagram_business_asset_assigned_users(instagram_business_asset_id: str, user: int) -> str:
    """DELETE /assigned_users on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{instagram_business_asset_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_instagram_business_asset_assigned_users(instagram_business_asset_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{instagram_business_asset_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_instagram_business_asset_assigned_users(instagram_business_asset_id: str, user: int, tasks: Optional[str] = None) -> str:
    """POST /assigned_users on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        tasks: Optional. Values: ADVERTISE, ANALYZE, COMMUNITY_ACTIVITY, CONTENT, MESSAGES
        user: Required.
    """
    params = {}
    if tasks is not None:
        params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"{instagram_business_asset_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def get_instagram_business_asset(instagram_business_asset_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on InstagramBusinessAsset.

    Args:
        instagram_business_asset_id: The ID of the InstagramBusinessAsset object.
        fields: Comma-separated list of fields to return. Available: id, ig_user_id, ig_username
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{instagram_business_asset_id}", params=params)
    return json.dumps(result, indent=2)


INSTAGRAM_USER_FIELDS = [
    "follow_count",
    "followed_by_count",
    "has_profile_picture",
    "id",
    "ig_user_id",
    "is_private",
    "is_published",
    "media_count",
    "mini_shop_storefront",
    "owner_business",
    "profile_pic",
    "username"
]


async def get_instagram_user_agencies(instagram_user_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on InstagramUser.

    Args:
        instagram_user_id: The ID of the InstagramUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{instagram_user_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def get_instagram_user_ar_effects(instagram_user_id: str, fields: Optional[str] = None) -> str:
    """GET /ar_effects on InstagramUser.

    Args:
        instagram_user_id: The ID of the InstagramUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{instagram_user_id}/ar_effects", params=params)
    return json.dumps(result, indent=2)


async def get_instagram_user_authorized_adaccounts(instagram_user_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /authorized_adaccounts on InstagramUser.

    Args:
        instagram_user_id: The ID of the InstagramUser object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{instagram_user_id}/authorized_adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_instagram_user_upcoming_events(instagram_user_id: str, fields: Optional[str] = None) -> str:
    """GET /upcoming_events on InstagramUser.

    Args:
        instagram_user_id: The ID of the InstagramUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{instagram_user_id}/upcoming_events", params=params)
    return json.dumps(result, indent=2)


async def get_instagram_user(
    instagram_user_id: str,
    fields: Optional[str] = None,
    adgroup_id: Optional[str] = None,
) -> str:
    """GET /#get on InstagramUser.

    Args:
        instagram_user_id: The ID of the InstagramUser object.
        fields: Comma-separated list of fields to return. Available: follow_count, followed_by_count, has_profile_picture, id, ig_user_id, is_private, is_published, media_count, mini_shop_storefront, owner_business, profile_pic, username
        adgroup_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if adgroup_id is not None:
        params["adgroup_id"] = adgroup_id
    result = await get_client().get(f"{instagram_user_id}", params=params)
    return json.dumps(result, indent=2)


IG_USER_EXPORT_FOR_CAM_FIELDS = [
    "age_bucket",
    "biography",
    "country",
    "email",
    "gender",
    "has_brand_partnership_experience",
    "id",
    "is_account_verified",
    "is_paid_partnership_messages_enabled",
    "messaging_id",
    "onboarded_status",
    "past_brand_partnership_partners",
    "portfolio_url",
    "username"
]


async def get_ig_user_export_for_cam_branded_content_media(ig_user_export_for_cam_id: str, fields: Optional[str] = None) -> str:
    """GET /branded_content_media on IGUserExportForCAM.

    Args:
        ig_user_export_for_cam_id: The ID of the IGUserExportForCAM object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_export_for_cam_id}/branded_content_media", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_export_for_cam_insights(
    ig_user_export_for_cam_id: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    metrics: Optional[str] = None,
    period: Optional[str] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /insights on IGUserExportForCAM.

    Args:
        ig_user_export_for_cam_id: The ID of the IGUserExportForCAM object.
        fields: Comma-separated list of fields to return.
        breakdown: Optional. Values: AGE, FOLLOW_TYPE, GENDER, MEDIA_TYPE, TOP_CITIES, TOP_COUNTRIES
        metrics: Optional. Values: CREATOR_ENGAGED_ACCOUNTS, CREATOR_REACH, REELS_HOOK_RATE, REELS_INTERACTION_RATE, TOTAL_FOLLOWERS
        period: Optional. Values: DAY, OVERALL
        time_range: Optional. Values: LAST_14_DAYS, LAST_90_DAYS, LIFETIME, THIS_MONTH, THIS_WEEK
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdown is not None:
        params["breakdown"] = breakdown
    if metrics is not None:
        params["metrics"] = metrics
    if period is not None:
        params["period"] = period
    if time_range is not None:
        params["time_range"] = time_range
    result = await get_client().get(f"{ig_user_export_for_cam_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_export_for_cam_recent_media(ig_user_export_for_cam_id: str, fields: Optional[str] = None) -> str:
    """GET /recent_media on IGUserExportForCAM.

    Args:
        ig_user_export_for_cam_id: The ID of the IGUserExportForCAM object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_export_for_cam_id}/recent_media", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_export_for_cam(ig_user_export_for_cam_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on IGUserExportForCAM.

    Args:
        ig_user_export_for_cam_id: The ID of the IGUserExportForCAM object.
        fields: Comma-separated list of fields to return. Available: age_bucket, biography, country, email, gender, has_brand_partnership_experience, id, is_account_verified, is_paid_partnership_messages_enabled, messaging_id, onboarded_status, past_brand_partnership_partners, portfolio_url, username
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_export_for_cam_id}", params=params)
    return json.dumps(result, indent=2)

