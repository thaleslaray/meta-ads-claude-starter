"""Auto-generated Meta Marketing API tools — campaigns."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


CAMPAIGN_FIELDS = [
    "account_id",
    "adlabels",
    "advantage_state_info",
    "bid_strategy",
    "boosted_object_id",
    "brand_lift_studies",
    "budget_rebalance_flag",
    "budget_remaining",
    "buying_type",
    "campaign_group_active_time",
    "can_create_brand_lift_study",
    "can_use_spend_cap",
    "configured_status",
    "created_time",
    "daily_budget",
    "effective_status",
    "has_secondary_skadnetwork_reporting",
    "id",
    "is_adset_budget_sharing_enabled",
    "is_budget_schedule_enabled",
    "is_direct_send_campaign",
    "is_message_campaign",
    "is_skadnetwork_attribution",
    "issues_info",
    "last_budget_toggling_time",
    "lifetime_budget",
    "name",
    "objective",
    "pacing_type",
    "primary_attribution",
    "promoted_object",
    "recommendations",
    "smart_promotion_type",
    "source_campaign",
    "source_campaign_id",
    "source_recommendation_type",
    "special_ad_categories",
    "special_ad_category",
    "special_ad_category_country",
    "spend_cap",
    "start_time",
    "status",
    "stop_time",
    "topline_id",
    "updated_time"
]


async def get_campaign_ad_studies(campaign_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_studies on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{campaign_id}/ad_studies", params=params)
    return json.dumps(result, indent=2)


async def get_campaign_ads(
    campaign_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    time_range: Optional[str] = None,
    updated_since: Optional[int] = None,
) -> str:
    """GET /ads on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return.
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        effective_status: Optional.
        time_range: Optional.
        updated_since: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if date_preset is not None:
        params["date_preset"] = date_preset
    if effective_status is not None:
        params["effective_status"] = effective_status
    if time_range is not None:
        params["time_range"] = time_range
    if updated_since is not None:
        params["updated_since"] = updated_since
    result = await get_client().get(f"{campaign_id}/ads", params=params)
    return json.dumps(result, indent=2)


async def get_campaign_adsets(
    campaign_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    is_completed: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /adsets on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return.
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        effective_status: Optional. Values: ACTIVE, ADSET_PAUSED, ARCHIVED, CAMPAIGN_PAUSED, DELETED, DISAPPROVED, IN_PROCESS, PAUSED, PENDING_BILLING_INFO, PENDING_REVIEW, PREAPPROVED, WITH_ISSUES
        is_completed: Optional.
        time_range: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if date_preset is not None:
        params["date_preset"] = date_preset
    if effective_status is not None:
        params["effective_status"] = effective_status
    if is_completed is not None:
        params["is_completed"] = is_completed
    if time_range is not None:
        params["time_range"] = time_range
    result = await get_client().get(f"{campaign_id}/adsets", params=params)
    return json.dumps(result, indent=2)


async def get_campaign_budget_schedules(
    campaign_id: str,
    fields: Optional[str] = None,
    time_start: Optional[str] = None,
    time_stop: Optional[str] = None,
) -> str:
    """GET /budget_schedules on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return.
        time_start: Optional.
        time_stop: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if time_start is not None:
        params["time_start"] = time_start
    if time_stop is not None:
        params["time_stop"] = time_stop
    result = await get_client().get(f"{campaign_id}/budget_schedules", params=params)
    return json.dumps(result, indent=2)


async def create_campaign_budget_schedules(
    campaign_id: str,
    budget_value: int,
    budget_value_type: str,
    time_end: int,
    time_start: int,
) -> str:
    """POST /budget_schedules on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        budget_value: Required.
        budget_value_type: Required. Values: ABSOLUTE, MULTIPLIER
        time_end: Required.
        time_start: Required.
    """
    params = {}
    params["budget_value"] = budget_value
    params["budget_value_type"] = budget_value_type
    params["time_end"] = time_end
    params["time_start"] = time_start
    result = await get_client().post(f"{campaign_id}/budget_schedules", data=params)
    return json.dumps(result, indent=2)


async def get_campaign_copies(
    campaign_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    is_completed: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /copies on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return.
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        effective_status: Optional. Values: ACTIVE, ADSET_PAUSED, ARCHIVED, CAMPAIGN_PAUSED, DELETED, DISAPPROVED, IN_PROCESS, PAUSED, PENDING_BILLING_INFO, PENDING_REVIEW, PREAPPROVED, WITH_ISSUES
        is_completed: Optional.
        time_range: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if date_preset is not None:
        params["date_preset"] = date_preset
    if effective_status is not None:
        params["effective_status"] = effective_status
    if is_completed is not None:
        params["is_completed"] = is_completed
    if time_range is not None:
        params["time_range"] = time_range
    result = await get_client().get(f"{campaign_id}/copies", params=params)
    return json.dumps(result, indent=2)


async def copy_campaign(
    campaign_id: str,
    deep_copy: Optional[bool] = None,
    end_time: Optional[str] = None,
    migrate_to_advantage_plus: Optional[bool] = None,
    parameter_overrides: Optional[str] = None,
    rename_options: Optional[str] = None,
    start_time: Optional[str] = None,
    status_option: Optional[str] = None,
) -> str:
    """POST /copies on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        deep_copy: Optional.
        end_time: Optional.
        migrate_to_advantage_plus: Optional.
        parameter_overrides: Optional.
        rename_options: Optional.
        start_time: Optional.
        status_option: Optional. Values: ACTIVE, INHERITED_FROM_SOURCE, PAUSED
    """
    params = {}
    if deep_copy is not None:
        params["deep_copy"] = deep_copy
    if end_time is not None:
        params["end_time"] = end_time
    if migrate_to_advantage_plus is not None:
        params["migrate_to_advantage_plus"] = migrate_to_advantage_plus
    if parameter_overrides is not None:
        params["parameter_overrides"] = parameter_overrides
    if rename_options is not None:
        params["rename_options"] = rename_options
    if start_time is not None:
        params["start_time"] = start_time
    if status_option is not None:
        params["status_option"] = status_option
    result = await get_client().post(f"{campaign_id}/copies", data=params)
    return json.dumps(result, indent=2)


async def get_campaign_insights(
    campaign_id: str,
    action_attribution_windows: Optional[str] = None,
    action_breakdowns: Optional[str] = None,
    action_report_time: Optional[str] = None,
    breakdowns: Optional[str] = None,
    date_preset: Optional[str] = None,
    default_summary: Optional[bool] = None,
    export_columns: Optional[str] = None,
    export_format: Optional[str] = None,
    export_name: Optional[str] = None,
    fields: Optional[str] = None,
    filtering: Optional[str] = None,
    graph_cache: Optional[bool] = None,
    level: Optional[str] = None,
    limit: Optional[int] = None,
    product_id_limit: Optional[int] = None,
    sort: Optional[str] = None,
    summary: Optional[str] = None,
    summary_action_breakdowns: Optional[str] = None,
    time_increment: Optional[str] = None,
    time_range: Optional[str] = None,
    time_ranges: Optional[str] = None,
    use_account_attribution_setting: Optional[bool] = None,
    use_unified_attribution_setting: Optional[bool] = None,
) -> str:
    """GET /insights on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        action_attribution_windows: Optional. Values: 1d_click, 1d_ev, 1d_view, 28d_click, 28d_view, 28d_view_all_conversions, 28d_view_first_conversion, 7d_click, 7d_view, 7d_view_all_conversions, 7d_view_first_conversion, dda, default, skan_click, skan_click_second_postback, skan_click_third_postback, skan_view, skan_view_second_postback, skan_view_third_postback
        action_breakdowns: Optional. Values: action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_device, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type
        action_report_time: Optional. Values: conversion, impression, lifetime, mixed
        breakdowns: Optional. Values: ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, conversion_destination, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, device_platform, dma, fidelity_type, flexible_format_asset_type, frequency_value, gen_ai_asset_type, gender, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, hsid, image_asset, impression_device, impression_view_time_advertiser_hour_v2, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, marketing_messages_btn_name, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, mmm, place_page_id, platform_position, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_group_id, product_id, product_set_id_breakdown, publisher_platform, redownload, region, rta_ugc_topic, rule_set_id, rule_set_name, signal_source_bucket, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, standard_event_content_type, title_asset, user_persona_id, user_persona_name, video_asset
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        default_summary: Optional.
        export_columns: Optional.
        export_format: Optional.
        export_name: Optional.
        fields: Optional.
        filtering: Optional.
        graph_cache: Optional.
        level: Optional. Values: account, ad, adset, campaign
        limit: Optional.
        product_id_limit: Optional.
        sort: Optional.
        summary: Optional.
        summary_action_breakdowns: Optional. Values: action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_device, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type
        time_increment: Optional.
        time_range: Optional.
        time_ranges: Optional.
        use_account_attribution_setting: Optional.
        use_unified_attribution_setting: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if action_attribution_windows is not None:
        params["action_attribution_windows"] = action_attribution_windows
    if action_breakdowns is not None:
        params["action_breakdowns"] = action_breakdowns
    if action_report_time is not None:
        params["action_report_time"] = action_report_time
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if date_preset is not None:
        params["date_preset"] = date_preset
    if default_summary is not None:
        params["default_summary"] = default_summary
    if export_columns is not None:
        params["export_columns"] = export_columns
    if export_format is not None:
        params["export_format"] = export_format
    if export_name is not None:
        params["export_name"] = export_name
    if fields is not None:
        params["fields"] = fields
    if filtering is not None:
        params["filtering"] = filtering
    if graph_cache is not None:
        params["graph_cache"] = graph_cache
    if level is not None:
        params["level"] = level
    if limit is not None:
        params["limit"] = limit
    if product_id_limit is not None:
        params["product_id_limit"] = product_id_limit
    if sort is not None:
        params["sort"] = sort
    if summary is not None:
        params["summary"] = summary
    if summary_action_breakdowns is not None:
        params["summary_action_breakdowns"] = summary_action_breakdowns
    if time_increment is not None:
        params["time_increment"] = time_increment
    if time_range is not None:
        params["time_range"] = time_range
    if time_ranges is not None:
        params["time_ranges"] = time_ranges
    if use_account_attribution_setting is not None:
        params["use_account_attribution_setting"] = use_account_attribution_setting
    if use_unified_attribution_setting is not None:
        params["use_unified_attribution_setting"] = use_unified_attribution_setting
    result = await get_client().get(f"{campaign_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def create_campaign_insights(
    campaign_id: str,
    action_attribution_windows: Optional[str] = None,
    action_breakdowns: Optional[str] = None,
    action_report_time: Optional[str] = None,
    breakdowns: Optional[str] = None,
    date_preset: Optional[str] = None,
    default_summary: Optional[bool] = None,
    export_columns: Optional[str] = None,
    export_format: Optional[str] = None,
    export_name: Optional[str] = None,
    fields: Optional[str] = None,
    filtering: Optional[str] = None,
    graph_cache: Optional[bool] = None,
    level: Optional[str] = None,
    limit: Optional[int] = None,
    product_id_limit: Optional[int] = None,
    sort: Optional[str] = None,
    summary: Optional[str] = None,
    summary_action_breakdowns: Optional[str] = None,
    time_increment: Optional[str] = None,
    time_range: Optional[str] = None,
    time_ranges: Optional[str] = None,
    use_account_attribution_setting: Optional[bool] = None,
    use_unified_attribution_setting: Optional[bool] = None,
) -> str:
    """POST /insights on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        action_attribution_windows: Optional. Values: 1d_click, 1d_ev, 1d_view, 28d_click, 28d_view, 28d_view_all_conversions, 28d_view_first_conversion, 7d_click, 7d_view, 7d_view_all_conversions, 7d_view_first_conversion, dda, default, skan_click, skan_click_second_postback, skan_click_third_postback, skan_view, skan_view_second_postback, skan_view_third_postback
        action_breakdowns: Optional. Values: action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_device, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type
        action_report_time: Optional. Values: conversion, impression, lifetime, mixed
        breakdowns: Optional. Values: ad_extension_domain, ad_extension_url, ad_format_asset, age, app_id, body_asset, breakdown_ad_objective, breakdown_reporting_ad_id, call_to_action_asset, coarse_conversion_value, comscore_market, conversion_destination, country, creative_automation_asset_id, creative_relaxation_asset_type, crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id, crm_advertiser_vertical_id, crm_ult_advertiser_id, description_asset, device_platform, dma, fidelity_type, flexible_format_asset_type, frequency_value, gen_ai_asset_type, gender, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone, hsid, image_asset, impression_device, impression_view_time_advertiser_hour_v2, is_auto_advance, is_conversion_id_modeled, is_rendered_as_delayed_skip_ad, landing_destination, link_url_asset, marketing_messages_btn_name, mdsa_landing_destination, media_asset_url, media_creator, media_destination_url, media_format, media_origin_url, media_text_content, media_type, mmm, place_page_id, platform_position, postback_sequence_index, product_brand_breakdown, product_category_breakdown, product_custom_label_0_breakdown, product_custom_label_1_breakdown, product_custom_label_2_breakdown, product_custom_label_3_breakdown, product_custom_label_4_breakdown, product_group_content_id_breakdown, product_group_id, product_id, product_set_id_breakdown, publisher_platform, redownload, region, rta_ugc_topic, rule_set_id, rule_set_name, signal_source_bucket, skan_campaign_id, skan_conversion_id, skan_version, sot_attribution_model_type, sot_attribution_window, sot_channel, sot_event_type, sot_source, standard_event_content_type, title_asset, user_persona_id, user_persona_name, video_asset
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        default_summary: Optional.
        export_columns: Optional.
        export_format: Optional.
        export_name: Optional.
        fields: Optional.
        filtering: Optional.
        graph_cache: Optional.
        level: Optional. Values: account, ad, adset, campaign
        limit: Optional.
        product_id_limit: Optional.
        sort: Optional.
        summary: Optional.
        summary_action_breakdowns: Optional. Values: action_canvas_component_name, action_carousel_card_id, action_carousel_card_name, action_destination, action_device, action_reaction, action_target_id, action_type, action_video_sound, action_video_type, conversion_destination, matched_persona_id, matched_persona_name, signal_source_bucket, standard_event_content_type
        time_increment: Optional.
        time_range: Optional.
        time_ranges: Optional.
        use_account_attribution_setting: Optional.
        use_unified_attribution_setting: Optional.
    """
    params = {}
    if action_attribution_windows is not None:
        params["action_attribution_windows"] = action_attribution_windows
    if action_breakdowns is not None:
        params["action_breakdowns"] = action_breakdowns
    if action_report_time is not None:
        params["action_report_time"] = action_report_time
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if date_preset is not None:
        params["date_preset"] = date_preset
    if default_summary is not None:
        params["default_summary"] = default_summary
    if export_columns is not None:
        params["export_columns"] = export_columns
    if export_format is not None:
        params["export_format"] = export_format
    if export_name is not None:
        params["export_name"] = export_name
    if fields is not None:
        params["fields"] = fields
    if filtering is not None:
        params["filtering"] = filtering
    if graph_cache is not None:
        params["graph_cache"] = graph_cache
    if level is not None:
        params["level"] = level
    if limit is not None:
        params["limit"] = limit
    if product_id_limit is not None:
        params["product_id_limit"] = product_id_limit
    if sort is not None:
        params["sort"] = sort
    if summary is not None:
        params["summary"] = summary
    if summary_action_breakdowns is not None:
        params["summary_action_breakdowns"] = summary_action_breakdowns
    if time_increment is not None:
        params["time_increment"] = time_increment
    if time_range is not None:
        params["time_range"] = time_range
    if time_ranges is not None:
        params["time_ranges"] = time_ranges
    if use_account_attribution_setting is not None:
        params["use_account_attribution_setting"] = use_account_attribution_setting
    if use_unified_attribution_setting is not None:
        params["use_unified_attribution_setting"] = use_unified_attribution_setting
    result = await get_client().post(f"{campaign_id}/insights", data=params)
    return json.dumps(result, indent=2)


async def delete_campaign(campaign_id: str) -> str:
    """DELETE /#delete on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
    """
    params = {}
    result = await get_client().delete(f"{campaign_id}")
    return json.dumps(result, indent=2)


async def get_campaign(
    campaign_id: str,
    fields: Optional[str] = None,
    am_call_tags: Optional[str] = None,
    date_preset: Optional[str] = None,
    from_adtable: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /#get on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        fields: Comma-separated list of fields to return. Available: account_id, adlabels, advantage_state_info, bid_strategy, boosted_object_id, brand_lift_studies, budget_rebalance_flag, budget_remaining, buying_type, campaign_group_active_time, can_create_brand_lift_study, can_use_spend_cap, configured_status, created_time, daily_budget, effective_status, has_secondary_skadnetwork_reporting, id, is_adset_budget_sharing_enabled, is_budget_schedule_enabled, is_direct_send_campaign, is_message_campaign, is_skadnetwork_attribution, issues_info, last_budget_toggling_time, lifetime_budget, name, objective, pacing_type, primary_attribution, promoted_object, recommendations, smart_promotion_type, source_campaign, source_campaign_id, source_recommendation_type, special_ad_categories, special_ad_category, special_ad_category_country, spend_cap, start_time, status, stop_time, topline_id, updated_time
        am_call_tags: Optional.
        date_preset: Optional.
        from_adtable: Optional.
        time_range: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if am_call_tags is not None:
        params["am_call_tags"] = am_call_tags
    if date_preset is not None:
        params["date_preset"] = date_preset
    if from_adtable is not None:
        params["from_adtable"] = from_adtable
    if time_range is not None:
        params["time_range"] = time_range
    result = await get_client().get(f"{campaign_id}", params=params)
    return json.dumps(result, indent=2)


async def update_campaign(
    campaign_id: str,
    adlabels: Optional[str] = None,
    adset_bid_amounts: Optional[str] = None,
    adset_budgets: Optional[str] = None,
    bid_strategy: Optional[str] = None,
    budget_rebalance_flag: Optional[bool] = None,
    budget_schedule_specs: Optional[str] = None,
    daily_budget: Optional[int] = None,
    execution_options: Optional[str] = None,
    is_adset_budget_sharing_enabled: Optional[bool] = None,
    is_budget_schedule_enabled: Optional[bool] = None,
    is_direct_send_campaign: Optional[bool] = None,
    is_message_campaign: Optional[bool] = None,
    is_skadnetwork_attribution: Optional[bool] = None,
    iterative_split_test_configs: Optional[str] = None,
    lifetime_budget: Optional[int] = None,
    migrate_to_advantage_plus: Optional[bool] = None,
    name: Optional[str] = None,
    objective: Optional[str] = None,
    pacing_type: Optional[str] = None,
    promoted_object: Optional[str] = None,
    smart_promotion_type: Optional[str] = None,
    special_ad_categories: Optional[str] = None,
    special_ad_category: Optional[str] = None,
    special_ad_category_country: Optional[str] = None,
    spend_cap: Optional[int] = None,
    start_time: Optional[str] = None,
    status: Optional[str] = None,
    stop_time: Optional[str] = None,
) -> str:
    """POST /#update on Campaign.

    Args:
        campaign_id: The ID of the Campaign object.
        adlabels: Optional.
        adset_bid_amounts: Optional.
        adset_budgets: Optional.
        bid_strategy: Optional.
        budget_rebalance_flag: Optional.
        budget_schedule_specs: Optional.
        daily_budget: Optional.
        execution_options: Optional.
        is_adset_budget_sharing_enabled: Optional.
        is_budget_schedule_enabled: Optional.
        is_direct_send_campaign: Optional.
        is_message_campaign: Optional.
        is_skadnetwork_attribution: Optional.
        iterative_split_test_configs: Optional.
        lifetime_budget: Optional.
        migrate_to_advantage_plus: Optional.
        name: Optional.
        objective: Optional.
        pacing_type: Optional.
        promoted_object: Optional.
        smart_promotion_type: Optional.
        special_ad_categories: Optional.
        special_ad_category: Optional.
        special_ad_category_country: Optional.
        spend_cap: Optional.
        start_time: Optional.
        status: Optional.
        stop_time: Optional.
    """
    params = {}
    if adlabels is not None:
        params["adlabels"] = adlabels
    if adset_bid_amounts is not None:
        params["adset_bid_amounts"] = adset_bid_amounts
    if adset_budgets is not None:
        params["adset_budgets"] = adset_budgets
    if bid_strategy is not None:
        params["bid_strategy"] = bid_strategy
    if budget_rebalance_flag is not None:
        params["budget_rebalance_flag"] = budget_rebalance_flag
    if budget_schedule_specs is not None:
        params["budget_schedule_specs"] = budget_schedule_specs
    if daily_budget is not None:
        params["daily_budget"] = daily_budget
    if execution_options is not None:
        params["execution_options"] = execution_options
    if is_adset_budget_sharing_enabled is not None:
        params["is_adset_budget_sharing_enabled"] = is_adset_budget_sharing_enabled
    if is_budget_schedule_enabled is not None:
        params["is_budget_schedule_enabled"] = is_budget_schedule_enabled
    if is_direct_send_campaign is not None:
        params["is_direct_send_campaign"] = is_direct_send_campaign
    if is_message_campaign is not None:
        params["is_message_campaign"] = is_message_campaign
    if is_skadnetwork_attribution is not None:
        params["is_skadnetwork_attribution"] = is_skadnetwork_attribution
    if iterative_split_test_configs is not None:
        params["iterative_split_test_configs"] = iterative_split_test_configs
    if lifetime_budget is not None:
        params["lifetime_budget"] = lifetime_budget
    if migrate_to_advantage_plus is not None:
        params["migrate_to_advantage_plus"] = migrate_to_advantage_plus
    if name is not None:
        params["name"] = name
    if objective is not None:
        params["objective"] = objective
    if pacing_type is not None:
        params["pacing_type"] = pacing_type
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    if smart_promotion_type is not None:
        params["smart_promotion_type"] = smart_promotion_type
    if special_ad_categories is not None:
        params["special_ad_categories"] = special_ad_categories
    if special_ad_category is not None:
        params["special_ad_category"] = special_ad_category
    if special_ad_category_country is not None:
        params["special_ad_category_country"] = special_ad_category_country
    if spend_cap is not None:
        params["spend_cap"] = spend_cap
    if start_time is not None:
        params["start_time"] = start_time
    if status is not None:
        params["status"] = status
    if stop_time is not None:
        params["stop_time"] = stop_time
    result = await get_client().post(f"{campaign_id}", data=params)
    return json.dumps(result, indent=2)

