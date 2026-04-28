"""Auto-generated Meta Marketing API tools — applications."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


APPLICATION_FIELDS = [
    "aam_rules",
    "an_ad_space_limit",
    "an_platforms",
    "android_key_hash",
    "android_sdk_error_categories",
    "app_domains",
    "app_events_config",
    "app_events_feature_bitmask",
    "app_events_session_timeout",
    "app_install_tracked",
    "app_name",
    "app_signals_binding_ios",
    "app_type",
    "auth_dialog_data_help_url",
    "auth_dialog_headline",
    "auth_dialog_perms_explanation",
    "auth_referral_default_activity_privacy",
    "auth_referral_enabled",
    "auth_referral_extended_perms",
    "auth_referral_friend_perms",
    "auth_referral_response_type",
    "auth_referral_user_perms",
    "auto_event_mapping_android",
    "auto_event_mapping_ios",
    "auto_event_setup_enabled",
    "auto_log_app_events_default",
    "auto_log_app_events_enabled",
    "business",
    "canvas_fluid_height",
    "canvas_fluid_width",
    "canvas_url",
    "category",
    "client_config",
    "company",
    "configured_ios_sso",
    "contact_email",
    "created_time",
    "creator_uid",
    "daily_active_users",
    "daily_active_users_rank",
    "deauth_callback_url",
    "default_share_mode",
    "description",
    "enigma_config",
    "financial_id",
    "gdpv4_chrome_custom_tabs_enabled",
    "gdpv4_enabled",
    "gdpv4_nux_content",
    "gdpv4_nux_enabled",
    "has_messenger_product",
    "hosting_url",
    "icon_url",
    "id",
    "ios_bundle_id",
    "ios_sdk_dialog_flows",
    "ios_sdk_error_categories",
    "ios_sfvc_attr",
    "ios_supports_native_proxy_auth_flow",
    "ios_supports_system_auth",
    "ipad_app_store_id",
    "iphone_app_store_id",
    "latest_sdk_version",
    "link",
    "logging_token",
    "logo_url",
    "migrations",
    "mobile_profile_section_url",
    "mobile_web_url",
    "monthly_active_users",
    "monthly_active_users_rank",
    "name",
    "namespace",
    "object_store_urls",
    "owner_business",
    "page_tab_default_name",
    "page_tab_url",
    "photo_url",
    "privacy_policy_url",
    "profile_section_url",
    "property_id",
    "protected_mode_rules",
    "real_time_mode_devices",
    "restrictions",
    "restrictive_data_filter_params",
    "restrictive_data_filter_rules",
    "sdk_update_message",
    "seamless_login",
    "secure_canvas_url",
    "secure_page_tab_url",
    "server_ip_whitelist",
    "smart_login_bookmark_icon_url",
    "smart_login_menu_icon_url",
    "social_discovery",
    "subcategory",
    "suggested_events_setting",
    "supported_platforms",
    "supports_apprequests_fast_app_switch",
    "supports_attribution",
    "supports_implicit_sdk_logging",
    "suppress_native_ios_gdp",
    "terms_of_service_url",
    "url_scheme_suffix",
    "user_support_email",
    "user_support_url",
    "website_url",
    "weekly_active_users"
]


async def delete_application_accounts(application_id: str, uid: int, type_: Optional[str] = None) -> str:
    """DELETE /accounts on Application.

    Args:
        application_id: The ID of the Application object.
        type_: Optional. Values: test-users
        uid: Required.
    """
    params = {}
    if type_ is not None:
        params["type"] = type_
    params["uid"] = uid
    result = await get_client().delete(f"{application_id}/accounts")
    return json.dumps(result, indent=2)


async def get_application_accounts(application_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /accounts on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: test-users
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{application_id}/accounts", params=params)
    return json.dumps(result, indent=2)


async def create_application_accounts(
    application_id: str,
    installed: Optional[bool] = None,
    minor: Optional[bool] = None,
    name: Optional[str] = None,
    owner_access_token: Optional[str] = None,
    permissions: Optional[str] = None,
    type_: Optional[str] = None,
    uid: Optional[int] = None,
) -> str:
    """POST /accounts on Application.

    Args:
        application_id: The ID of the Application object.
        installed: Optional.
        minor: Optional.
        name: Optional.
        owner_access_token: Optional.
        permissions: Optional.
        type_: Optional. Values: test-users
        uid: Optional.
    """
    params = {}
    if installed is not None:
        params["installed"] = installed
    if minor is not None:
        params["minor"] = minor
    if name is not None:
        params["name"] = name
    if owner_access_token is not None:
        params["owner_access_token"] = owner_access_token
    if permissions is not None:
        params["permissions"] = permissions
    if type_ is not None:
        params["type"] = type_
    if uid is not None:
        params["uid"] = uid
    result = await get_client().post(f"{application_id}/accounts", data=params)
    return json.dumps(result, indent=2)


async def get_application_ad_placement_groups(application_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_placement_groups on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/ad_placement_groups", params=params)
    return json.dumps(result, indent=2)


async def get_application_adnetwork_placements(
    application_id: str,
    fields: Optional[str] = None,
    request_id: Optional[str] = None,
) -> str:
    """GET /adnetwork_placements on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        request_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if request_id is not None:
        params["request_id"] = request_id
    result = await get_client().get(f"{application_id}/adnetwork_placements", params=params)
    return json.dumps(result, indent=2)


async def get_application_adnetworkanalytics(
    application_id: str,
    metrics: str,
    fields: Optional[str] = None,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    should_include_until: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /adnetworkanalytics on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        should_include_until: Optional.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if should_include_until is not None:
        params["should_include_until"] = should_include_until
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{application_id}/adnetworkanalytics", params=params)
    return json.dumps(result, indent=2)


async def create_application_adnetworkanalytics(
    application_id: str,
    metrics: str,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """POST /adnetworkanalytics on Application.

    Args:
        application_id: The ID of the Application object.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        since: Optional.
        until: Optional.
    """
    params = {}
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().post(f"{application_id}/adnetworkanalytics", data=params)
    return json.dumps(result, indent=2)


async def get_application_adnetworkanalytics_results(
    application_id: str,
    fields: Optional[str] = None,
    query_ids: Optional[str] = None,
) -> str:
    """GET /adnetworkanalytics_results on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        query_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if query_ids is not None:
        params["query_ids"] = query_ids
    result = await get_client().get(f"{application_id}/adnetworkanalytics_results", params=params)
    return json.dumps(result, indent=2)


async def get_application_aem_attribution(
    application_id: str,
    fields: Optional[str] = None,
    advertiser_ids: Optional[str] = None,
    fb_content_data: Optional[str] = None,
) -> str:
    """GET /aem_attribution on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        advertiser_ids: Optional.
        fb_content_data: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if advertiser_ids is not None:
        params["advertiser_ids"] = advertiser_ids
    if fb_content_data is not None:
        params["fb_content_data"] = fb_content_data
    result = await get_client().get(f"{application_id}/aem_attribution", params=params)
    return json.dumps(result, indent=2)


async def get_application_aem_conversion_configs(
    application_id: str,
    fields: Optional[str] = None,
    advertiser_ids: Optional[str] = None,
) -> str:
    """GET /aem_conversion_configs on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        advertiser_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if advertiser_ids is not None:
        params["advertiser_ids"] = advertiser_ids
    result = await get_client().get(f"{application_id}/aem_conversion_configs", params=params)
    return json.dumps(result, indent=2)


async def get_application_aem_conversion_filter(
    application_id: str,
    fields: Optional[str] = None,
    catalog_id: Optional[str] = None,
    fb_content_ids: Optional[str] = None,
) -> str:
    """GET /aem_conversion_filter on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        catalog_id: Optional.
        fb_content_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if catalog_id is not None:
        params["catalog_id"] = catalog_id
    if fb_content_ids is not None:
        params["fb_content_ids"] = fb_content_ids
    result = await get_client().get(f"{application_id}/aem_conversion_filter", params=params)
    return json.dumps(result, indent=2)


async def create_application_aem_conversions(application_id: str, aem_conversions: str) -> str:
    """POST /aem_conversions on Application.

    Args:
        application_id: The ID of the Application object.
        aem_conversions: Required.
    """
    params = {}
    params["aem_conversions"] = aem_conversions
    result = await get_client().post(f"{application_id}/aem_conversions", data=params)
    return json.dumps(result, indent=2)


async def create_application_aem_skan_readiness(
    application_id: str,
    app_id: int,
    is_aem_ready: Optional[bool] = None,
    is_app_aem_install_ready: Optional[bool] = None,
    is_app_aem_ready: Optional[bool] = None,
    is_skan_ready: Optional[bool] = None,
    message: Optional[str] = None,
) -> str:
    """POST /aem_skan_readiness on Application.

    Args:
        application_id: The ID of the Application object.
        app_id: Required.
        is_aem_ready: Optional.
        is_app_aem_install_ready: Optional.
        is_app_aem_ready: Optional.
        is_skan_ready: Optional.
        message: Optional.
    """
    params = {}
    params["app_id"] = app_id
    if is_aem_ready is not None:
        params["is_aem_ready"] = is_aem_ready
    if is_app_aem_install_ready is not None:
        params["is_app_aem_install_ready"] = is_app_aem_install_ready
    if is_app_aem_ready is not None:
        params["is_app_aem_ready"] = is_app_aem_ready
    if is_skan_ready is not None:
        params["is_skan_ready"] = is_skan_ready
    if message is not None:
        params["message"] = message
    result = await get_client().post(f"{application_id}/aem_skan_readiness", data=params)
    return json.dumps(result, indent=2)


async def get_application_agencies(application_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_application_aggregate_revenue(
    application_id: str,
    ecpms: Optional[str] = None,
    query_ids: Optional[str] = None,
    request_id: Optional[str] = None,
    sync_api: Optional[bool] = None,
) -> str:
    """POST /aggregate_revenue on Application.

    Args:
        application_id: The ID of the Application object.
        ecpms: Optional.
        query_ids: Optional.
        request_id: Optional.
        sync_api: Optional.
    """
    params = {}
    if ecpms is not None:
        params["ecpms"] = ecpms
    if query_ids is not None:
        params["query_ids"] = query_ids
    if request_id is not None:
        params["request_id"] = request_id
    if sync_api is not None:
        params["sync_api"] = sync_api
    result = await get_client().post(f"{application_id}/aggregate_revenue", data=params)
    return json.dumps(result, indent=2)


async def get_application_android_dialog_configs(application_id: str, fields: Optional[str] = None) -> str:
    """GET /android_dialog_configs on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/android_dialog_configs", params=params)
    return json.dumps(result, indent=2)


async def get_application_app_capi_settings(application_id: str, fields: Optional[str] = None) -> str:
    """GET /app_capi_settings on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/app_capi_settings", params=params)
    return json.dumps(result, indent=2)


async def get_application_app_event_types(application_id: str, fields: Optional[str] = None) -> str:
    """GET /app_event_types on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/app_event_types", params=params)
    return json.dumps(result, indent=2)


async def create_application_app_indexing(
    application_id: str,
    app_version: str,
    platform: str,
    tree: str,
    device_session_id: Optional[str] = None,
    extra_info: Optional[str] = None,
    request_type: Optional[str] = None,
) -> str:
    """POST /app_indexing on Application.

    Args:
        application_id: The ID of the Application object.
        app_version: Required.
        device_session_id: Optional.
        extra_info: Optional.
        platform: Required. Values: ANDROID, IOS
        request_type: Optional. Values: APP_INDEXING, BUTTON_SAMPLING, PLUGIN
        tree: Required.
    """
    params = {}
    params["app_version"] = app_version
    if device_session_id is not None:
        params["device_session_id"] = device_session_id
    if extra_info is not None:
        params["extra_info"] = extra_info
    params["platform"] = platform
    if request_type is not None:
        params["request_type"] = request_type
    params["tree"] = tree
    result = await get_client().post(f"{application_id}/app_indexing", data=params)
    return json.dumps(result, indent=2)


async def create_application_app_indexing_session(application_id: str, device_session_id: str, extinfo: Optional[str] = None) -> str:
    """POST /app_indexing_session on Application.

    Args:
        application_id: The ID of the Application object.
        device_session_id: Required.
        extinfo: Optional.
    """
    params = {}
    params["device_session_id"] = device_session_id
    if extinfo is not None:
        params["extinfo"] = extinfo
    result = await get_client().post(f"{application_id}/app_indexing_session", data=params)
    return json.dumps(result, indent=2)


async def get_application_app_installed_groups(
    application_id: str,
    fields: Optional[str] = None,
    group_id: Optional[str] = None,
) -> str:
    """GET /app_installed_groups on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        group_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if group_id is not None:
        params["group_id"] = group_id
    result = await get_client().get(f"{application_id}/app_installed_groups", params=params)
    return json.dumps(result, indent=2)


async def create_application_app_push_device_token(
    application_id: str,
    device_id: str,
    device_token: str,
    platform: Optional[str] = None,
) -> str:
    """POST /app_push_device_token on Application.

    Args:
        application_id: The ID of the Application object.
        device_id: Required.
        device_token: Required.
        platform: Optional. Values: ANDROID, IOS, UNKNOWN
    """
    params = {}
    params["device_id"] = device_id
    params["device_token"] = device_token
    if platform is not None:
        params["platform"] = platform
    result = await get_client().post(f"{application_id}/app_push_device_token", data=params)
    return json.dumps(result, indent=2)


async def get_application_appassets(application_id: str, fields: Optional[str] = None) -> str:
    """GET /appassets on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/appassets", params=params)
    return json.dumps(result, indent=2)


async def create_application_assets(application_id: str, asset: str, type_: str, comment: Optional[str] = None) -> str:
    """POST /assets on Application.

    Args:
        application_id: The ID of the Application object.
        asset: Required.
        comment: Optional.
        type_: Required.
    """
    params = {}
    params["asset"] = asset
    if comment is not None:
        params["comment"] = comment
    params["type"] = type_
    result = await get_client().post(f"{application_id}/assets", data=params)
    return json.dumps(result, indent=2)


async def get_application_authorized_adaccounts(
    application_id: str,
    fields: Optional[str] = None,
    business: Optional[str] = None,
) -> str:
    """GET /authorized_adaccounts on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        business: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business is not None:
        params["business"] = business
    result = await get_client().get(f"{application_id}/authorized_adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_application_button_auto_detection_device_selection(
    application_id: str,
    fields: Optional[str] = None,
    device_id: Optional[str] = None,
) -> str:
    """GET /button_auto_detection_device_selection on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        device_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if device_id is not None:
        params["device_id"] = device_id
    result = await get_client().get(f"{application_id}/button_auto_detection_device_selection", params=params)
    return json.dumps(result, indent=2)


async def get_application_cloudbridge_settings(application_id: str, fields: Optional[str] = None) -> str:
    """GET /cloudbridge_settings on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/cloudbridge_settings", params=params)
    return json.dumps(result, indent=2)


async def create_application_codeless_event_mappings(
    application_id: str,
    mappings: str,
    mutation_method: str,
    platform: str,
    post_method: Optional[str] = None,
) -> str:
    """POST /codeless_event_mappings on Application.

    Args:
        application_id: The ID of the Application object.
        mappings: Required.
        mutation_method: Required. Values: ADD, DELETE, REPLACE
        platform: Required. Values: ANDROID, IOS
        post_method: Optional. Values: CODELESS, EYMT
    """
    params = {}
    params["mappings"] = mappings
    params["mutation_method"] = mutation_method
    params["platform"] = platform
    if post_method is not None:
        params["post_method"] = post_method
    result = await get_client().post(f"{application_id}/codeless_event_mappings", data=params)
    return json.dumps(result, indent=2)


async def get_application_connected_client_businesses(application_id: str, fields: Optional[str] = None) -> str:
    """GET /connected_client_businesses on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/connected_client_businesses", params=params)
    return json.dumps(result, indent=2)


async def get_application_da_checks(
    application_id: str,
    fields: Optional[str] = None,
    checks: Optional[str] = None,
    connection_method: Optional[str] = None,
) -> str:
    """GET /da_checks on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        checks: Optional.
        connection_method: Optional. Values: ALL, APP, BROWSER, SERVER
    """
    params = {}
    params["fields"] = fields or "id,name"
    if checks is not None:
        params["checks"] = checks
    if connection_method is not None:
        params["connection_method"] = connection_method
    result = await get_client().get(f"{application_id}/da_checks", params=params)
    return json.dumps(result, indent=2)


async def create_application_domain_reports(application_id: str, tracking_domains: str) -> str:
    """POST /domain_reports on Application.

    Args:
        application_id: The ID of the Application object.
        tracking_domains: Required.
    """
    params = {}
    params["tracking_domains"] = tracking_domains
    result = await get_client().post(f"{application_id}/domain_reports", data=params)
    return json.dumps(result, indent=2)


async def get_application_iap_purchases(application_id: str, order_id: str, fields: Optional[str] = None) -> str:
    """GET /iap_purchases on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        order_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["order_id"] = order_id
    result = await get_client().get(f"{application_id}/iap_purchases", params=params)
    return json.dumps(result, indent=2)


async def get_application_ios_dialog_configs(application_id: str, fields: Optional[str] = None) -> str:
    """GET /ios_dialog_configs on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/ios_dialog_configs", params=params)
    return json.dumps(result, indent=2)


async def get_application_linked_dataset(application_id: str, fields: Optional[str] = None) -> str:
    """GET /linked_dataset on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/linked_dataset", params=params)
    return json.dumps(result, indent=2)


async def create_application_mmp_auditing(
    application_id: str,
    event: str,
    is_fb: bool,
    advertiser_id: Optional[str] = None,
    attribution: Optional[str] = None,
    attribution_method: Optional[str] = None,
    attribution_model: Optional[str] = None,
    attribution_referrer: Optional[str] = None,
    auditing_token: Optional[str] = None,
    click_attr_window: Optional[int] = None,
    custom_events: Optional[str] = None,
    decline_reason: Optional[str] = None,
    device_os: Optional[str] = None,
    engagement_type: Optional[str] = None,
    event_id: Optional[str] = None,
    event_reported_time: Optional[int] = None,
    fb_ad_id: Optional[int] = None,
    fb_adgroup_id: Optional[int] = None,
    fb_click_time: Optional[int] = None,
    fb_view_time: Optional[int] = None,
    google_install_referrer: Optional[str] = None,
    inactivity_window_hours: Optional[int] = None,
    install_id: Optional[str] = None,
    meta_install_referrer: Optional[str] = None,
    used_install_referrer: Optional[bool] = None,
    view_attr_window: Optional[int] = None,
) -> str:
    """POST /mmp_auditing on Application.

    Args:
        application_id: The ID of the Application object.
        advertiser_id: Optional.
        attribution: Optional.
        attribution_method: Optional.
        attribution_model: Optional.
        attribution_referrer: Optional.
        auditing_token: Optional.
        click_attr_window: Optional.
        custom_events: Optional.
        decline_reason: Optional.
        device_os: Optional.
        engagement_type: Optional.
        event: Required.
        event_id: Optional.
        event_reported_time: Optional.
        fb_ad_id: Optional.
        fb_adgroup_id: Optional.
        fb_click_time: Optional.
        fb_view_time: Optional.
        google_install_referrer: Optional.
        inactivity_window_hours: Optional.
        install_id: Optional.
        is_fb: Required.
        meta_install_referrer: Optional.
        used_install_referrer: Optional.
        view_attr_window: Optional.
    """
    params = {}
    if advertiser_id is not None:
        params["advertiser_id"] = advertiser_id
    if attribution is not None:
        params["attribution"] = attribution
    if attribution_method is not None:
        params["attribution_method"] = attribution_method
    if attribution_model is not None:
        params["attribution_model"] = attribution_model
    if attribution_referrer is not None:
        params["attribution_referrer"] = attribution_referrer
    if auditing_token is not None:
        params["auditing_token"] = auditing_token
    if click_attr_window is not None:
        params["click_attr_window"] = click_attr_window
    if custom_events is not None:
        params["custom_events"] = custom_events
    if decline_reason is not None:
        params["decline_reason"] = decline_reason
    if device_os is not None:
        params["device_os"] = device_os
    if engagement_type is not None:
        params["engagement_type"] = engagement_type
    params["event"] = event
    if event_id is not None:
        params["event_id"] = event_id
    if event_reported_time is not None:
        params["event_reported_time"] = event_reported_time
    if fb_ad_id is not None:
        params["fb_ad_id"] = fb_ad_id
    if fb_adgroup_id is not None:
        params["fb_adgroup_id"] = fb_adgroup_id
    if fb_click_time is not None:
        params["fb_click_time"] = fb_click_time
    if fb_view_time is not None:
        params["fb_view_time"] = fb_view_time
    if google_install_referrer is not None:
        params["google_install_referrer"] = google_install_referrer
    if inactivity_window_hours is not None:
        params["inactivity_window_hours"] = inactivity_window_hours
    if install_id is not None:
        params["install_id"] = install_id
    params["is_fb"] = is_fb
    if meta_install_referrer is not None:
        params["meta_install_referrer"] = meta_install_referrer
    if used_install_referrer is not None:
        params["used_install_referrer"] = used_install_referrer
    if view_attr_window is not None:
        params["view_attr_window"] = view_attr_window
    result = await get_client().post(f"{application_id}/mmp_auditing", data=params)
    return json.dumps(result, indent=2)


async def get_application_mobile_sdk_gk(
    application_id: str,
    platform: str,
    sdk_version: str,
    fields: Optional[str] = None,
    device_id: Optional[str] = None,
    extinfo: Optional[str] = None,
    os_version: Optional[str] = None,
) -> str:
    """GET /mobile_sdk_gk on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        device_id: Optional.
        extinfo: Optional.
        os_version: Optional.
        platform: Required. Values: ANDROID, IOS
        sdk_version: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if device_id is not None:
        params["device_id"] = device_id
    if extinfo is not None:
        params["extinfo"] = extinfo
    if os_version is not None:
        params["os_version"] = os_version
    params["platform"] = platform
    params["sdk_version"] = sdk_version
    result = await get_client().get(f"{application_id}/mobile_sdk_gk", params=params)
    return json.dumps(result, indent=2)


async def get_application_monetized_digital_store_objects(application_id: str, fields: Optional[str] = None) -> str:
    """GET /monetized_digital_store_objects on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/monetized_digital_store_objects", params=params)
    return json.dumps(result, indent=2)


async def create_application_monetized_digital_store_objects(application_id: str, content_id: str, store: str) -> str:
    """POST /monetized_digital_store_objects on Application.

    Args:
        application_id: The ID of the Application object.
        content_id: Required.
        store: Required.
    """
    params = {}
    params["content_id"] = content_id
    params["store"] = store
    result = await get_client().post(f"{application_id}/monetized_digital_store_objects", data=params)
    return json.dumps(result, indent=2)


async def get_application_object_types(application_id: str, fields: Optional[str] = None) -> str:
    """GET /object_types on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/object_types", params=params)
    return json.dumps(result, indent=2)


async def get_application_objects(application_id: str, fields: Optional[str] = None) -> str:
    """GET /objects on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/objects", params=params)
    return json.dumps(result, indent=2)


async def create_application_occludespopups(application_id: str, flash: Optional[bool] = None, unity: Optional[bool] = None) -> str:
    """POST /occludespopups on Application.

    Args:
        application_id: The ID of the Application object.
        flash: Optional.
        unity: Optional.
    """
    params = {}
    if flash is not None:
        params["flash"] = flash
    if unity is not None:
        params["unity"] = unity
    result = await get_client().post(f"{application_id}/occludespopups", data=params)
    return json.dumps(result, indent=2)


async def get_application_permissions(
    application_id: str,
    fields: Optional[str] = None,
    android_key_hash: Optional[str] = None,
    ios_bundle_id: Optional[str] = None,
    permission: Optional[str] = None,
    proxied_app_id: Optional[int] = None,
    status: Optional[str] = None,
) -> str:
    """GET /permissions on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        android_key_hash: Optional.
        ios_bundle_id: Optional.
        permission: Optional.
        proxied_app_id: Optional.
        status: Optional. Values: live, unapproved
    """
    params = {}
    params["fields"] = fields or "id,name"
    if android_key_hash is not None:
        params["android_key_hash"] = android_key_hash
    if ios_bundle_id is not None:
        params["ios_bundle_id"] = ios_bundle_id
    if permission is not None:
        params["permission"] = permission
    if proxied_app_id is not None:
        params["proxied_app_id"] = proxied_app_id
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{application_id}/permissions", params=params)
    return json.dumps(result, indent=2)


async def get_application_products(
    application_id: str,
    fields: Optional[str] = None,
    product_ids: Optional[str] = None,
) -> str:
    """GET /products on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        product_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if product_ids is not None:
        params["product_ids"] = product_ids
    result = await get_client().get(f"{application_id}/products", params=params)
    return json.dumps(result, indent=2)


async def get_application_purchases(application_id: str, fields: Optional[str] = None) -> str:
    """GET /purchases on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/purchases", params=params)
    return json.dumps(result, indent=2)


async def get_application_roles(application_id: str, fields: Optional[str] = None) -> str:
    """GET /roles on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/roles", params=params)
    return json.dumps(result, indent=2)


async def get_application_server_domain_infos(application_id: str, fields: Optional[str] = None) -> str:
    """GET /server_domain_infos on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/server_domain_infos", params=params)
    return json.dumps(result, indent=2)


async def get_application_sgw_dataset_status(application_id: str, dataset_id: int, fields: Optional[str] = None) -> str:
    """GET /sgw_dataset_status on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        dataset_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["dataset_id"] = dataset_id
    result = await get_client().get(f"{application_id}/sgw_dataset_status", params=params)
    return json.dumps(result, indent=2)


async def get_application_sgw_install_deferral_link(
    application_id: str,
    dataset_id: int,
    fields: Optional[str] = None,
    client_ip: Optional[str] = None,
) -> str:
    """GET /sgw_install_deferral_link on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        client_ip: Optional.
        dataset_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if client_ip is not None:
        params["client_ip"] = client_ip
    params["dataset_id"] = dataset_id
    result = await get_client().get(f"{application_id}/sgw_install_deferral_link", params=params)
    return json.dumps(result, indent=2)


async def get_application_subscribed_domains(application_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_domains on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/subscribed_domains", params=params)
    return json.dumps(result, indent=2)


async def get_application_subscribed_domains_phishing(application_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_domains_phishing on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/subscribed_domains_phishing", params=params)
    return json.dumps(result, indent=2)


async def delete_application_subscriptions(application_id: str, fields: Optional[str] = None, object_: Optional[str] = None) -> str:
    """DELETE /subscriptions on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Optional.
        object_: Optional.
    """
    params = {}
    if fields is not None:
        params["fields"] = fields
    if object_ is not None:
        params["object"] = object_
    result = await get_client().delete(f"{application_id}/subscriptions")
    return json.dumps(result, indent=2)


async def get_application_subscriptions(application_id: str, fields: Optional[str] = None) -> str:
    """GET /subscriptions on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{application_id}/subscriptions", params=params)
    return json.dumps(result, indent=2)


async def create_application_subscriptions(
    application_id: str,
    object_: str,
    callback_url: Optional[str] = None,
    fields: Optional[str] = None,
    include_values: Optional[bool] = None,
    verify_token: Optional[str] = None,
) -> str:
    """POST /subscriptions on Application.

    Args:
        application_id: The ID of the Application object.
        callback_url: Optional.
        fields: Optional.
        include_values: Optional.
        object_: Required.
        verify_token: Optional.
    """
    params = {}
    if callback_url is not None:
        params["callback_url"] = callback_url
    if fields is not None:
        params["fields"] = fields
    if include_values is not None:
        params["include_values"] = include_values
    params["object"] = object_
    if verify_token is not None:
        params["verify_token"] = verify_token
    result = await get_client().post(f"{application_id}/subscriptions", data=params)
    return json.dumps(result, indent=2)


async def create_application_uploads(
    application_id: str,
    file_length: Optional[int] = None,
    file_name: Optional[str] = None,
    file_type: Optional[str] = None,
    session_type: Optional[str] = None,
) -> str:
    """POST /uploads on Application.

    Args:
        application_id: The ID of the Application object.
        file_length: Optional.
        file_name: Optional.
        file_type: Optional.
        session_type: Optional. Values: attachment
    """
    params = {}
    if file_length is not None:
        params["file_length"] = file_length
    if file_name is not None:
        params["file_name"] = file_name
    if file_type is not None:
        params["file_type"] = file_type
    if session_type is not None:
        params["session_type"] = session_type
    result = await get_client().post(f"{application_id}/uploads", data=params)
    return json.dumps(result, indent=2)


async def create_application_whatsapp_business_solution(
    application_id: str,
    owner_permissions: str,
    partner_app_id: str,
    partner_permissions: str,
    solution_name: str,
) -> str:
    """POST /whatsapp_business_solution on Application.

    Args:
        application_id: The ID of the Application object.
        owner_permissions: Required. Values: DEVELOP, MANAGE, MANAGE_EXTENSIONS, MANAGE_PHONE, MANAGE_PHONE_ASSETS, MANAGE_TEMPLATES, MESSAGING, VIEW_COST, VIEW_PHONE_ASSETS, VIEW_TEMPLATES
        partner_app_id: Required.
        partner_permissions: Required. Values: DEVELOP, MANAGE, MANAGE_EXTENSIONS, MANAGE_PHONE, MANAGE_PHONE_ASSETS, MANAGE_TEMPLATES, MESSAGING, VIEW_COST, VIEW_PHONE_ASSETS, VIEW_TEMPLATES
        solution_name: Required.
    """
    params = {}
    params["owner_permissions"] = owner_permissions
    params["partner_app_id"] = partner_app_id
    params["partner_permissions"] = partner_permissions
    params["solution_name"] = solution_name
    result = await get_client().post(f"{application_id}/whatsapp_business_solution", data=params)
    return json.dumps(result, indent=2)


async def get_application_whatsapp_business_solutions(application_id: str, fields: Optional[str] = None, role: Optional[str] = None) -> str:
    """GET /whatsapp_business_solutions on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return.
        role: Optional. Values: OWNER, PARTNER
    """
    params = {}
    params["fields"] = fields or "id,name"
    if role is not None:
        params["role"] = role
    result = await get_client().get(f"{application_id}/whatsapp_business_solutions", params=params)
    return json.dumps(result, indent=2)


async def get_application(
    application_id: str,
    fields: Optional[str] = None,
    advertiser_id: Optional[str] = None,
) -> str:
    """GET /#get on Application.

    Args:
        application_id: The ID of the Application object.
        fields: Comma-separated list of fields to return. Available: aam_rules, an_ad_space_limit, an_platforms, android_key_hash, android_sdk_error_categories, app_domains, app_events_config, app_events_feature_bitmask, app_events_session_timeout, app_install_tracked, app_name, app_signals_binding_ios, app_type, auth_dialog_data_help_url, auth_dialog_headline, auth_dialog_perms_explanation, auth_referral_default_activity_privacy, auth_referral_enabled, auth_referral_extended_perms, auth_referral_friend_perms, auth_referral_response_type, auth_referral_user_perms, auto_event_mapping_android, auto_event_mapping_ios, auto_event_setup_enabled, auto_log_app_events_default, auto_log_app_events_enabled, business, canvas_fluid_height, canvas_fluid_width, canvas_url, category, client_config, company, configured_ios_sso, contact_email, created_time, creator_uid, daily_active_users, daily_active_users_rank, deauth_callback_url, default_share_mode, description, enigma_config, financial_id, gdpv4_chrome_custom_tabs_enabled, gdpv4_enabled, gdpv4_nux_content, gdpv4_nux_enabled, has_messenger_product, hosting_url, icon_url, id, ios_bundle_id, ios_sdk_dialog_flows, ios_sdk_error_categories, ios_sfvc_attr, ios_supports_native_proxy_auth_flow, ios_supports_system_auth, ipad_app_store_id, iphone_app_store_id, latest_sdk_version, link, logging_token, logo_url, migrations, mobile_profile_section_url, mobile_web_url, monthly_active_users, monthly_active_users_rank, name, namespace, object_store_urls, owner_business, page_tab_default_name, page_tab_url, photo_url, privacy_policy_url, profile_section_url, property_id, protected_mode_rules, real_time_mode_devices, restrictions, restrictive_data_filter_params, restrictive_data_filter_rules, sdk_update_message, seamless_login, secure_canvas_url, secure_page_tab_url, server_ip_whitelist, smart_login_bookmark_icon_url, smart_login_menu_icon_url, social_discovery, subcategory, suggested_events_setting, supported_platforms, supports_apprequests_fast_app_switch, supports_attribution, supports_implicit_sdk_logging, suppress_native_ios_gdp, terms_of_service_url, url_scheme_suffix, user_support_email, user_support_url, website_url, weekly_active_users
        advertiser_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if advertiser_id is not None:
        params["advertiser_id"] = advertiser_id
    result = await get_client().get(f"{application_id}", params=params)
    return json.dumps(result, indent=2)


async def update_application(
    application_id: str,
    allow_cycle_app_secret: Optional[bool] = None,
    an_platforms: Optional[str] = None,
    app_domains: Optional[str] = None,
    app_name: Optional[str] = None,
    app_type: Optional[bool] = None,
    auth_dialog_headline: Optional[str] = None,
    auth_dialog_perms_explanation: Optional[str] = None,
    auth_referral_enabled: Optional[bool] = None,
    auth_referral_extended_perms: Optional[str] = None,
    auth_referral_friend_perms: Optional[str] = None,
    auth_referral_response_type: Optional[str] = None,
    auth_referral_user_perms: Optional[str] = None,
    canvas_fluid_height: Optional[bool] = None,
    canvas_fluid_width: Optional[bool] = None,
    canvas_url: Optional[str] = None,
    contact_email: Optional[str] = None,
    deauth_callback_url: Optional[str] = None,
    mobile_web_url: Optional[str] = None,
    namespace: Optional[str] = None,
    page_tab_default_name: Optional[str] = None,
    privacy_policy_url: Optional[str] = None,
    restrictions: Optional[str] = None,
    secure_canvas_url: Optional[str] = None,
    secure_page_tab_url: Optional[str] = None,
    server_ip_whitelist: Optional[str] = None,
    terms_of_service_url: Optional[str] = None,
    url_scheme_suffix: Optional[str] = None,
    user_support_email: Optional[str] = None,
    user_support_url: Optional[str] = None,
    website_url: Optional[str] = None,
) -> str:
    """POST /#update on Application.

    Args:
        application_id: The ID of the Application object.
        allow_cycle_app_secret: Optional.
        an_platforms: Optional.
        app_domains: Optional.
        app_name: Optional.
        app_type: Optional.
        auth_dialog_headline: Optional.
        auth_dialog_perms_explanation: Optional.
        auth_referral_enabled: Optional.
        auth_referral_extended_perms: Optional.
        auth_referral_friend_perms: Optional.
        auth_referral_response_type: Optional.
        auth_referral_user_perms: Optional.
        canvas_fluid_height: Optional.
        canvas_fluid_width: Optional.
        canvas_url: Optional.
        contact_email: Optional.
        deauth_callback_url: Optional.
        mobile_web_url: Optional.
        namespace: Optional.
        page_tab_default_name: Optional.
        privacy_policy_url: Optional.
        restrictions: Optional.
        secure_canvas_url: Optional.
        secure_page_tab_url: Optional.
        server_ip_whitelist: Optional.
        terms_of_service_url: Optional.
        url_scheme_suffix: Optional.
        user_support_email: Optional.
        user_support_url: Optional.
        website_url: Optional.
    """
    params = {}
    if allow_cycle_app_secret is not None:
        params["allow_cycle_app_secret"] = allow_cycle_app_secret
    if an_platforms is not None:
        params["an_platforms"] = an_platforms
    if app_domains is not None:
        params["app_domains"] = app_domains
    if app_name is not None:
        params["app_name"] = app_name
    if app_type is not None:
        params["app_type"] = app_type
    if auth_dialog_headline is not None:
        params["auth_dialog_headline"] = auth_dialog_headline
    if auth_dialog_perms_explanation is not None:
        params["auth_dialog_perms_explanation"] = auth_dialog_perms_explanation
    if auth_referral_enabled is not None:
        params["auth_referral_enabled"] = auth_referral_enabled
    if auth_referral_extended_perms is not None:
        params["auth_referral_extended_perms"] = auth_referral_extended_perms
    if auth_referral_friend_perms is not None:
        params["auth_referral_friend_perms"] = auth_referral_friend_perms
    if auth_referral_response_type is not None:
        params["auth_referral_response_type"] = auth_referral_response_type
    if auth_referral_user_perms is not None:
        params["auth_referral_user_perms"] = auth_referral_user_perms
    if canvas_fluid_height is not None:
        params["canvas_fluid_height"] = canvas_fluid_height
    if canvas_fluid_width is not None:
        params["canvas_fluid_width"] = canvas_fluid_width
    if canvas_url is not None:
        params["canvas_url"] = canvas_url
    if contact_email is not None:
        params["contact_email"] = contact_email
    if deauth_callback_url is not None:
        params["deauth_callback_url"] = deauth_callback_url
    if mobile_web_url is not None:
        params["mobile_web_url"] = mobile_web_url
    if namespace is not None:
        params["namespace"] = namespace
    if page_tab_default_name is not None:
        params["page_tab_default_name"] = page_tab_default_name
    if privacy_policy_url is not None:
        params["privacy_policy_url"] = privacy_policy_url
    if restrictions is not None:
        params["restrictions"] = restrictions
    if secure_canvas_url is not None:
        params["secure_canvas_url"] = secure_canvas_url
    if secure_page_tab_url is not None:
        params["secure_page_tab_url"] = secure_page_tab_url
    if server_ip_whitelist is not None:
        params["server_ip_whitelist"] = server_ip_whitelist
    if terms_of_service_url is not None:
        params["terms_of_service_url"] = terms_of_service_url
    if url_scheme_suffix is not None:
        params["url_scheme_suffix"] = url_scheme_suffix
    if user_support_email is not None:
        params["user_support_email"] = user_support_email
    if user_support_url is not None:
        params["user_support_url"] = user_support_url
    if website_url is not None:
        params["website_url"] = website_url
    result = await get_client().post(f"{application_id}", data=params)
    return json.dumps(result, indent=2)


APP_REQUEST_FIELDS = [
    "action_type",
    "application",
    "created_time",
    "data",
    "from",
    "id",
    "message",
    "object",
    "to"
]


async def delete_app_request(app_request_id: str, ids: str) -> str:
    """DELETE /#delete on AppRequest.

    Args:
        app_request_id: The ID of the AppRequest object.
        ids: Required.
    """
    params = {}
    params["ids"] = ids
    result = await get_client().delete(f"{app_request_id}")
    return json.dumps(result, indent=2)


async def get_app_request(app_request_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AppRequest.

    Args:
        app_request_id: The ID of the AppRequest object.
        fields: Comma-separated list of fields to return. Available: action_type, application, created_time, data, from, id, message, object, to
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{app_request_id}", params=params)
    return json.dumps(result, indent=2)

