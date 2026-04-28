"""Auto-generated Meta Marketing API tools — pixels."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


ADS_PIXEL_FIELDS = [
    "automatic_matching_fields",
    "can_proxy",
    "code",
    "config",
    "creation_time",
    "creator",
    "data_use_setting",
    "description",
    "duplicate_entries",
    "enable_auto_assign_to_accounts",
    "enable_automatic_matching",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_party_cookie_status",
    "has_1p_pixel_event",
    "id",
    "is_consolidated_container",
    "is_created_by_business",
    "is_crm",
    "is_mta_use",
    "is_restricted_use",
    "is_unavailable",
    "last_fired_time",
    "last_upload_app",
    "last_upload_app_changed_time",
    "match_rate_approx",
    "matched_entries",
    "name",
    "owner_ad_account",
    "owner_business",
    "usage",
    "user_access_expire_time",
    "valid_entries"
]


async def get_ads_pixel_adaccounts(ads_pixel_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /adaccounts on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{ads_pixel_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def delete_ads_pixel_agencies(ads_pixel_id: str, business: str) -> str:
    """DELETE /agencies on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{ads_pixel_id}/agencies")
    return json.dumps(result, indent=2)


async def get_ads_pixel_agencies(ads_pixel_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_pixel_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_agencies(ads_pixel_id: str, business: str, permitted_tasks: str) -> str:
    """POST /agencies on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        business: Required.
        permitted_tasks: Required. Values: ADVERTISE, ANALYZE, EDIT, UPLOAD
    """
    params = {}
    params["business"] = business
    params["permitted_tasks"] = permitted_tasks
    result = await get_client().post(f"{ads_pixel_id}/agencies", data=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_ahp_configs(ads_pixel_id: str, applink_autosetup: bool) -> str:
    """POST /ahp_configs on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        applink_autosetup: Required.
    """
    params = {}
    params["applink_autosetup"] = applink_autosetup
    result = await get_client().post(f"{ads_pixel_id}/ahp_configs", data=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_assigned_users(ads_pixel_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{ads_pixel_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_assigned_users(ads_pixel_id: str, tasks: str, user: int) -> str:
    """POST /assigned_users on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        tasks: Required. Values: AA_ANALYZE, ADVERTISE, ANALYZE, EDIT, UPLOAD
        user: Required.
    """
    params = {}
    params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"{ads_pixel_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_da_checks(
    ads_pixel_id: str,
    fields: Optional[str] = None,
    checks: Optional[str] = None,
    connection_method: Optional[str] = None,
) -> str:
    """GET /da_checks on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
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
    result = await get_client().get(f"{ads_pixel_id}/da_checks", params=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_events(
    ads_pixel_id: str,
    data: str,
    namespace_id: Optional[str] = None,
    partner_agent: Optional[str] = None,
    platforms: Optional[str] = None,
    progress: Optional[str] = None,
    test_event_code: Optional[str] = None,
    trace: Optional[int] = None,
    upload_id: Optional[str] = None,
    upload_source: Optional[str] = None,
    upload_tag: Optional[str] = None,
) -> str:
    """POST /events on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        data: Required.
        namespace_id: Optional.
        partner_agent: Optional.
        platforms: Optional.
        progress: Optional.
        test_event_code: Optional.
        trace: Optional.
        upload_id: Optional.
        upload_source: Optional.
        upload_tag: Optional.
    """
    params = {}
    params["data"] = data
    if namespace_id is not None:
        params["namespace_id"] = namespace_id
    if partner_agent is not None:
        params["partner_agent"] = partner_agent
    if platforms is not None:
        params["platforms"] = platforms
    if progress is not None:
        params["progress"] = progress
    if test_event_code is not None:
        params["test_event_code"] = test_event_code
    if trace is not None:
        params["trace"] = trace
    if upload_id is not None:
        params["upload_id"] = upload_id
    if upload_source is not None:
        params["upload_source"] = upload_source
    if upload_tag is not None:
        params["upload_tag"] = upload_tag
    result = await get_client().post(f"{ads_pixel_id}/events", data=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_offline_event_uploads(
    ads_pixel_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    order: Optional[str] = None,
    sort_by: Optional[str] = None,
    start_time: Optional[str] = None,
    upload_tag: Optional[str] = None,
) -> str:
    """GET /offline_event_uploads on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        order: Optional. Values: ASCENDING, DESCENDING
        sort_by: Optional. Values: API_CALLS, CREATION_TIME, EVENT_TIME_MAX, EVENT_TIME_MIN, FIRST_UPLOAD_TIME, IS_EXCLUDED_FOR_LIFT, LAST_UPLOAD_TIME
        start_time: Optional.
        upload_tag: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if order is not None:
        params["order"] = order
    if sort_by is not None:
        params["sort_by"] = sort_by
    if start_time is not None:
        params["start_time"] = start_time
    if upload_tag is not None:
        params["upload_tag"] = upload_tag
    result = await get_client().get(f"{ads_pixel_id}/offline_event_uploads", params=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_openbridge_configurations(ads_pixel_id: str, fields: Optional[str] = None) -> str:
    """GET /openbridge_configurations on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_pixel_id}/openbridge_configurations", params=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_shadowtraffichelper(ads_pixel_id: str) -> str:
    """POST /shadowtraffichelper on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
    """
    params = {}
    result = await get_client().post(f"{ads_pixel_id}/shadowtraffichelper", data=params)
    return json.dumps(result, indent=2)


async def delete_ads_pixel_shared_accounts(ads_pixel_id: str, account_id: str, business: str) -> str:
    """DELETE /shared_accounts on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        account_id: Required.
        business: Required.
    """
    params = {}
    params["account_id"] = account_id
    params["business"] = business
    result = await get_client().delete(f"{ads_pixel_id}/shared_accounts")
    return json.dumps(result, indent=2)


async def get_ads_pixel_shared_accounts(ads_pixel_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /shared_accounts on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{ads_pixel_id}/shared_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_ads_pixel_shared_accounts(ads_pixel_id: str, account_id: str, business: str) -> str:
    """POST /shared_accounts on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        account_id: Required.
        business: Required.
    """
    params = {}
    params["account_id"] = account_id
    params["business"] = business
    result = await get_client().post(f"{ads_pixel_id}/shared_accounts", data=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_shared_agencies(ads_pixel_id: str, fields: Optional[str] = None) -> str:
    """GET /shared_agencies on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_pixel_id}/shared_agencies", params=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel_stats(
    ads_pixel_id: str,
    fields: Optional[str] = None,
    aggregation: Optional[str] = None,
    end_time: Optional[str] = None,
    event: Optional[str] = None,
    event_source: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /stats on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return.
        aggregation: Optional. Values: browser_type, custom_data_field, device_os, device_type, event, event_detection_method, event_processing_results, event_source, event_total_counts, event_value_count, had_pii, host, match_keys, pixel_fire, url, url_by_rule
        end_time: Optional.
        event: Optional.
        event_source: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggregation is not None:
        params["aggregation"] = aggregation
    if end_time is not None:
        params["end_time"] = end_time
    if event is not None:
        params["event"] = event
    if event_source is not None:
        params["event_source"] = event_source
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{ads_pixel_id}/stats", params=params)
    return json.dumps(result, indent=2)


async def get_ads_pixel(ads_pixel_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        fields: Comma-separated list of fields to return. Available: automatic_matching_fields, can_proxy, code, config, creation_time, creator, data_use_setting, description, duplicate_entries, enable_auto_assign_to_accounts, enable_automatic_matching, event_stats, event_time_max, event_time_min, first_party_cookie_status, has_1p_pixel_event, id, is_consolidated_container, is_created_by_business, is_crm, is_mta_use, is_restricted_use, is_unavailable, last_fired_time, last_upload_app, last_upload_app_changed_time, match_rate_approx, matched_entries, name, owner_ad_account, owner_business, usage, user_access_expire_time, valid_entries
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_pixel_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ads_pixel(
    ads_pixel_id: str,
    automatic_matching_fields: Optional[str] = None,
    data_use_setting: Optional[str] = None,
    enable_automatic_matching: Optional[bool] = None,
    first_party_cookie_status: Optional[str] = None,
    name: Optional[str] = None,
    server_events_business_ids: Optional[str] = None,
) -> str:
    """POST /#update on AdsPixel.

    Args:
        ads_pixel_id: The ID of the AdsPixel object.
        automatic_matching_fields: Optional.
        data_use_setting: Optional.
        enable_automatic_matching: Optional.
        first_party_cookie_status: Optional.
        name: Optional.
        server_events_business_ids: Optional.
    """
    params = {}
    if automatic_matching_fields is not None:
        params["automatic_matching_fields"] = automatic_matching_fields
    if data_use_setting is not None:
        params["data_use_setting"] = data_use_setting
    if enable_automatic_matching is not None:
        params["enable_automatic_matching"] = enable_automatic_matching
    if first_party_cookie_status is not None:
        params["first_party_cookie_status"] = first_party_cookie_status
    if name is not None:
        params["name"] = name
    if server_events_business_ids is not None:
        params["server_events_business_ids"] = server_events_business_ids
    result = await get_client().post(f"{ads_pixel_id}", data=params)
    return json.dumps(result, indent=2)


OFFLINE_CONVERSION_DATA_SET_FIELDS = [
    "automatic_matching_fields",
    "business",
    "can_proxy",
    "config",
    "creation_time",
    "creator",
    "data_use_setting",
    "description",
    "duplicate_entries",
    "enable_auto_assign_to_accounts",
    "enable_automatic_matching",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_party_cookie_status",
    "id",
    "is_consolidated_container",
    "is_created_by_business",
    "is_crm",
    "is_mta_use",
    "is_restricted_use",
    "is_unavailable",
    "last_fired_time",
    "last_upload_app",
    "last_upload_app_changed_time",
    "match_rate_approx",
    "matched_entries",
    "name",
    "owner_ad_account",
    "owner_business",
    "usage",
    "valid_entries"
]


async def get_offline_conversion_data_set_adaccounts(offline_conversion_data_set_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /adaccounts on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{offline_conversion_data_set_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_agencies(offline_conversion_data_set_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_audiences(
    offline_conversion_data_set_id: str,
    fields: Optional[str] = None,
    action_source: Optional[str] = None,
    ad_account: Optional[str] = None,
) -> str:
    """GET /audiences on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        action_source: Optional. Values: PHYSICAL_STORE, WEBSITE
        ad_account: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if action_source is not None:
        params["action_source"] = action_source
    if ad_account is not None:
        params["ad_account"] = ad_account
    result = await get_client().get(f"{offline_conversion_data_set_id}/audiences", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_customconversions(
    offline_conversion_data_set_id: str,
    fields: Optional[str] = None,
    ad_account: Optional[str] = None,
) -> str:
    """GET /customconversions on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        ad_account: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_account is not None:
        params["ad_account"] = ad_account
    result = await get_client().get(f"{offline_conversion_data_set_id}/customconversions", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_server_events_permitted_business(offline_conversion_data_set_id: str, fields: Optional[str] = None) -> str:
    """GET /server_events_permitted_business on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_id}/server_events_permitted_business", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_shared_accounts(
    offline_conversion_data_set_id: str,
    action_source: str,
    business: str,
    fields: Optional[str] = None,
) -> str:
    """GET /shared_accounts on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        action_source: Required. Values: PHYSICAL_STORE, WEBSITE
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["action_source"] = action_source
    params["business"] = business
    result = await get_client().get(f"{offline_conversion_data_set_id}/shared_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_shared_agencies(
    offline_conversion_data_set_id: str,
    action_source: str,
    fields: Optional[str] = None,
) -> str:
    """GET /shared_agencies on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        action_source: Required. Values: PHYSICAL_STORE, WEBSITE
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["action_source"] = action_source
    result = await get_client().get(f"{offline_conversion_data_set_id}/shared_agencies", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_stats(
    offline_conversion_data_set_id: str,
    fields: Optional[str] = None,
    aggr_time: Optional[str] = None,
    end: Optional[int] = None,
    granularity: Optional[str] = None,
    skip_empty_values: Optional[bool] = None,
    start: Optional[int] = None,
    user_timezone_id: Optional[int] = None,
) -> str:
    """GET /stats on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        aggr_time: Optional. Values: event_time, upload_time
        end: Optional.
        granularity: Optional. Values: daily, hourly, six_hourly
        skip_empty_values: Optional.
        start: Optional.
        user_timezone_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggr_time is not None:
        params["aggr_time"] = aggr_time
    if end is not None:
        params["end"] = end
    if granularity is not None:
        params["granularity"] = granularity
    if skip_empty_values is not None:
        params["skip_empty_values"] = skip_empty_values
    if start is not None:
        params["start"] = start
    if user_timezone_id is not None:
        params["user_timezone_id"] = user_timezone_id
    result = await get_client().get(f"{offline_conversion_data_set_id}/stats", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_uploads(
    offline_conversion_data_set_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    order: Optional[str] = None,
    sort_by: Optional[str] = None,
    start_time: Optional[str] = None,
    upload_tag: Optional[str] = None,
) -> str:
    """GET /uploads on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        order: Optional. Values: ASCENDING, DESCENDING
        sort_by: Optional. Values: API_CALLS, CREATION_TIME, EVENT_TIME_MAX, EVENT_TIME_MIN, FIRST_UPLOAD_TIME, IS_EXCLUDED_FOR_LIFT, LAST_UPLOAD_TIME
        start_time: Optional.
        upload_tag: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if order is not None:
        params["order"] = order
    if sort_by is not None:
        params["sort_by"] = sort_by
    if start_time is not None:
        params["start_time"] = start_time
    if upload_tag is not None:
        params["upload_tag"] = upload_tag
    result = await get_client().get(f"{offline_conversion_data_set_id}/uploads", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set(offline_conversion_data_set_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OfflineConversionDataSet.

    Args:
        offline_conversion_data_set_id: The ID of the OfflineConversionDataSet object.
        fields: Comma-separated list of fields to return. Available: automatic_matching_fields, business, can_proxy, config, creation_time, creator, data_use_setting, description, duplicate_entries, enable_auto_assign_to_accounts, enable_automatic_matching, event_stats, event_time_max, event_time_min, first_party_cookie_status, id, is_consolidated_container, is_created_by_business, is_crm, is_mta_use, is_restricted_use, is_unavailable, last_fired_time, last_upload_app, last_upload_app_changed_time, match_rate_approx, matched_entries, name, owner_ad_account, owner_business, usage, valid_entries
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_id}", params=params)
    return json.dumps(result, indent=2)


CUSTOM_CONVERSION_FIELDS = [
    "account_id",
    "aggregation_rule",
    "business",
    "creation_time",
    "custom_event_type",
    "data_sources",
    "default_conversion_value",
    "description",
    "event_source_type",
    "first_fired_time",
    "id",
    "is_archived",
    "is_unavailable",
    "last_fired_time",
    "name",
    "offline_conversion_data_set",
    "pixel",
    "retention_days",
    "rule"
]


async def get_custom_conversion_stats(
    custom_conversion_id: str,
    fields: Optional[str] = None,
    aggregation: Optional[str] = None,
    end_time: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /stats on CustomConversion.

    Args:
        custom_conversion_id: The ID of the CustomConversion object.
        fields: Comma-separated list of fields to return.
        aggregation: Optional. Values: count, device_type, host, pixel_fire, unmatched_count, unmatched_usd_amount, url, usd_amount
        end_time: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggregation is not None:
        params["aggregation"] = aggregation
    if end_time is not None:
        params["end_time"] = end_time
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{custom_conversion_id}/stats", params=params)
    return json.dumps(result, indent=2)


async def delete_custom_conversion(custom_conversion_id: str) -> str:
    """DELETE /#delete on CustomConversion.

    Args:
        custom_conversion_id: The ID of the CustomConversion object.
    """
    params = {}
    result = await get_client().delete(f"{custom_conversion_id}")
    return json.dumps(result, indent=2)


async def get_custom_conversion(custom_conversion_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on CustomConversion.

    Args:
        custom_conversion_id: The ID of the CustomConversion object.
        fields: Comma-separated list of fields to return. Available: account_id, aggregation_rule, business, creation_time, custom_event_type, data_sources, default_conversion_value, description, event_source_type, first_fired_time, id, is_archived, is_unavailable, last_fired_time, name, offline_conversion_data_set, pixel, retention_days, rule
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{custom_conversion_id}", params=params)
    return json.dumps(result, indent=2)


async def update_custom_conversion(
    custom_conversion_id: str,
    default_conversion_value: Optional[float] = None,
    description: Optional[str] = None,
    name: Optional[str] = None,
) -> str:
    """POST /#update on CustomConversion.

    Args:
        custom_conversion_id: The ID of the CustomConversion object.
        default_conversion_value: Optional.
        description: Optional.
        name: Optional.
    """
    params = {}
    if default_conversion_value is not None:
        params["default_conversion_value"] = default_conversion_value
    if description is not None:
        params["description"] = description
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"{custom_conversion_id}", data=params)
    return json.dumps(result, indent=2)


OFFLINE_CONVERSION_DATA_SET_UPLOAD_FIELDS = [
    "api_calls",
    "creation_time",
    "duplicate_entries",
    "event_stats",
    "event_time_max",
    "event_time_min",
    "first_upload_time",
    "id",
    "is_excluded_for_lift",
    "last_upload_time",
    "match_rate_approx",
    "matched_entries",
    "upload_tag",
    "valid_entries"
]


async def get_offline_conversion_data_set_upload_progress(offline_conversion_data_set_upload_id: str, fields: Optional[str] = None) -> str:
    """GET /progress on OfflineConversionDataSetUpload.

    Args:
        offline_conversion_data_set_upload_id: The ID of the OfflineConversionDataSetUpload object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_upload_id}/progress", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_upload_pull_sessions(offline_conversion_data_set_upload_id: str, fields: Optional[str] = None) -> str:
    """GET /pull_sessions on OfflineConversionDataSetUpload.

    Args:
        offline_conversion_data_set_upload_id: The ID of the OfflineConversionDataSetUpload object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_upload_id}/pull_sessions", params=params)
    return json.dumps(result, indent=2)


async def get_offline_conversion_data_set_upload(offline_conversion_data_set_upload_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OfflineConversionDataSetUpload.

    Args:
        offline_conversion_data_set_upload_id: The ID of the OfflineConversionDataSetUpload object.
        fields: Comma-separated list of fields to return. Available: api_calls, creation_time, duplicate_entries, event_stats, event_time_max, event_time_min, first_upload_time, id, is_excluded_for_lift, last_upload_time, match_rate_approx, matched_entries, upload_tag, valid_entries
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_conversion_data_set_upload_id}", params=params)
    return json.dumps(result, indent=2)


OFFSITE_SIGNAL_CONTAINER_BUSINESS_OBJECT_FIELDS = [
    "business",
    "id",
    "is_eligible_for_sharing_to_ad_account",
    "is_eligible_for_sharing_to_business",
    "is_unavailable",
    "name",
    "primary_container_id"
]


async def get_offsite_signal_container_business_object_linked_application(offsite_signal_container_business_object_id: str, fields: Optional[str] = None) -> str:
    """GET /linked_application on OffsiteSignalContainerBusinessObject.

    Args:
        offsite_signal_container_business_object_id: The ID of the OffsiteSignalContainerBusinessObject object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offsite_signal_container_business_object_id}/linked_application", params=params)
    return json.dumps(result, indent=2)


async def get_offsite_signal_container_business_object_linked_page(offsite_signal_container_business_object_id: str, fields: Optional[str] = None) -> str:
    """GET /linked_page on OffsiteSignalContainerBusinessObject.

    Args:
        offsite_signal_container_business_object_id: The ID of the OffsiteSignalContainerBusinessObject object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offsite_signal_container_business_object_id}/linked_page", params=params)
    return json.dumps(result, indent=2)


async def get_offsite_signal_container_business_object(offsite_signal_container_business_object_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OffsiteSignalContainerBusinessObject.

    Args:
        offsite_signal_container_business_object_id: The ID of the OffsiteSignalContainerBusinessObject object.
        fields: Comma-separated list of fields to return. Available: business, id, is_eligible_for_sharing_to_ad_account, is_eligible_for_sharing_to_business, is_unavailable, name, primary_container_id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offsite_signal_container_business_object_id}", params=params)
    return json.dumps(result, indent=2)


OPEN_BRIDGE_CONFIGURATION_FIELDS = [
    "active",
    "blocked_event_types",
    "blocked_websites",
    "browser_agent",
    "cloud_provider",
    "cloud_region",
    "destination_id",
    "endpoint",
    "event_enrichment_state",
    "fallback_domain",
    "first_party_domain",
    "host_business_id",
    "id",
    "instance_id",
    "instance_version",
    "is_sgw_instance",
    "is_sgw_pixel_from_meta_pixel",
    "partner_name",
    "pixel_id",
    "sgw_account_id",
    "sgw_instance_url",
    "sgw_pixel_id"
]


async def delete_open_bridge_configuration(open_bridge_configuration_id: str) -> str:
    """DELETE /#delete on OpenBridgeConfiguration.

    Args:
        open_bridge_configuration_id: The ID of the OpenBridgeConfiguration object.
    """
    params = {}
    result = await get_client().delete(f"{open_bridge_configuration_id}")
    return json.dumps(result, indent=2)


async def get_open_bridge_configuration(open_bridge_configuration_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OpenBridgeConfiguration.

    Args:
        open_bridge_configuration_id: The ID of the OpenBridgeConfiguration object.
        fields: Comma-separated list of fields to return. Available: active, blocked_event_types, blocked_websites, browser_agent, cloud_provider, cloud_region, destination_id, endpoint, event_enrichment_state, fallback_domain, first_party_domain, host_business_id, id, instance_id, instance_version, is_sgw_instance, is_sgw_pixel_from_meta_pixel, partner_name, pixel_id, sgw_account_id, sgw_instance_url, sgw_pixel_id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{open_bridge_configuration_id}", params=params)
    return json.dumps(result, indent=2)


async def update_open_bridge_configuration(
    open_bridge_configuration_id: str,
    active: Optional[bool] = None,
    blocked_event_types: Optional[str] = None,
    blocked_websites: Optional[str] = None,
    cloud_provider: Optional[str] = None,
    cloud_region: Optional[str] = None,
    destination_id: Optional[str] = None,
    endpoint: Optional[str] = None,
    event_enrichment_state: Optional[str] = None,
    fallback_domain: Optional[str] = None,
    first_party_domain: Optional[str] = None,
    host_business_id: Optional[int] = None,
    instance_id: Optional[str] = None,
    instance_version: Optional[str] = None,
    is_sgw_instance: Optional[bool] = None,
    is_sgw_pixel_from_meta_pixel: Optional[bool] = None,
    partner_name: Optional[str] = None,
    sgw_account_id: Optional[str] = None,
    sgw_instance_url: Optional[str] = None,
    sgw_pixel_id: Optional[int] = None,
) -> str:
    """POST /#update on OpenBridgeConfiguration.

    Args:
        open_bridge_configuration_id: The ID of the OpenBridgeConfiguration object.
        active: Optional.
        blocked_event_types: Optional.
        blocked_websites: Optional.
        cloud_provider: Optional.
        cloud_region: Optional.
        destination_id: Optional.
        endpoint: Optional.
        event_enrichment_state: Optional.
        fallback_domain: Optional.
        first_party_domain: Optional.
        host_business_id: Optional.
        instance_id: Optional.
        instance_version: Optional.
        is_sgw_instance: Optional.
        is_sgw_pixel_from_meta_pixel: Optional.
        partner_name: Optional.
        sgw_account_id: Optional.
        sgw_instance_url: Optional.
        sgw_pixel_id: Optional.
    """
    params = {}
    if active is not None:
        params["active"] = active
    if blocked_event_types is not None:
        params["blocked_event_types"] = blocked_event_types
    if blocked_websites is not None:
        params["blocked_websites"] = blocked_websites
    if cloud_provider is not None:
        params["cloud_provider"] = cloud_provider
    if cloud_region is not None:
        params["cloud_region"] = cloud_region
    if destination_id is not None:
        params["destination_id"] = destination_id
    if endpoint is not None:
        params["endpoint"] = endpoint
    if event_enrichment_state is not None:
        params["event_enrichment_state"] = event_enrichment_state
    if fallback_domain is not None:
        params["fallback_domain"] = fallback_domain
    if first_party_domain is not None:
        params["first_party_domain"] = first_party_domain
    if host_business_id is not None:
        params["host_business_id"] = host_business_id
    if instance_id is not None:
        params["instance_id"] = instance_id
    if instance_version is not None:
        params["instance_version"] = instance_version
    if is_sgw_instance is not None:
        params["is_sgw_instance"] = is_sgw_instance
    if is_sgw_pixel_from_meta_pixel is not None:
        params["is_sgw_pixel_from_meta_pixel"] = is_sgw_pixel_from_meta_pixel
    if partner_name is not None:
        params["partner_name"] = partner_name
    if sgw_account_id is not None:
        params["sgw_account_id"] = sgw_account_id
    if sgw_instance_url is not None:
        params["sgw_instance_url"] = sgw_instance_url
    if sgw_pixel_id is not None:
        params["sgw_pixel_id"] = sgw_pixel_id
    result = await get_client().post(f"{open_bridge_configuration_id}", data=params)
    return json.dumps(result, indent=2)


EVENT_SOURCE_GROUP_FIELDS = [
    "business",
    "event_sources",
    "id",
    "name",
    "owner_business"
]


async def get_event_source_group_shared_accounts(event_source_group_id: str, fields: Optional[str] = None) -> str:
    """GET /shared_accounts on EventSourceGroup.

    Args:
        event_source_group_id: The ID of the EventSourceGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_source_group_id}/shared_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_event_source_group_shared_accounts(event_source_group_id: str, accounts: str) -> str:
    """POST /shared_accounts on EventSourceGroup.

    Args:
        event_source_group_id: The ID of the EventSourceGroup object.
        accounts: Required.
    """
    params = {}
    params["accounts"] = accounts
    result = await get_client().post(f"{event_source_group_id}/shared_accounts", data=params)
    return json.dumps(result, indent=2)


async def get_event_source_group(event_source_group_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on EventSourceGroup.

    Args:
        event_source_group_id: The ID of the EventSourceGroup object.
        fields: Comma-separated list of fields to return. Available: business, event_sources, id, name, owner_business
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_source_group_id}", params=params)
    return json.dumps(result, indent=2)


async def update_event_source_group(event_source_group_id: str, event_sources: str, name: str) -> str:
    """POST /#update on EventSourceGroup.

    Args:
        event_source_group_id: The ID of the EventSourceGroup object.
        event_sources: Required.
        name: Required.
    """
    params = {}
    params["event_sources"] = event_sources
    params["name"] = name
    result = await get_client().post(f"{event_source_group_id}", data=params)
    return json.dumps(result, indent=2)

