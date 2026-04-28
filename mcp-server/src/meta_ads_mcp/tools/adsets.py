"""Auto-generated Meta Marketing API tools — adsets."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_SET_FIELDS = [
    "account_id",
    "adlabels",
    "adset_schedule",
    "anchor_event_attribution_window_days",
    "asset_feed_id",
    "attribution_spec",
    "automatic_manual_state",
    "bid_adjustments",
    "bid_amount",
    "bid_constraints",
    "bid_info",
    "bid_strategy",
    "billing_event",
    "brand_safety_config",
    "budget_remaining",
    "campaign",
    "campaign_active_time",
    "campaign_attribution",
    "campaign_id",
    "configured_status",
    "created_time",
    "creative_sequence",
    "creative_sequence_repetition_pattern",
    "daily_budget",
    "daily_min_spend_target",
    "daily_spend_cap",
    "destination_type",
    "dsa_beneficiary",
    "dsa_payor",
    "effective_status",
    "end_time",
    "existing_customer_budget_percentage",
    "frequency_control_specs",
    "full_funnel_exploration_mode",
    "id",
    "instagram_user_id",
    "is_ba_skip_delayed_eligible",
    "is_budget_schedule_enabled",
    "is_dynamic_creative",
    "is_incremental_attribution_enabled",
    "issues_info",
    "learning_stage_info",
    "lifetime_budget",
    "lifetime_imps",
    "lifetime_min_spend_target",
    "lifetime_spend_cap",
    "max_budget_spend_percentage",
    "min_budget_spend_percentage",
    "multi_optimization_goal_weight",
    "name",
    "optimization_goal",
    "optimization_sub_event",
    "pacing_type",
    "placement_soft_opt_out",
    "promoted_object",
    "recommendations",
    "recurring_budget_semantics",
    "regional_regulated_categories",
    "regional_regulation_identities",
    "review_feedback",
    "rf_prediction_id",
    "source_adset",
    "source_adset_id",
    "start_time",
    "status",
    "targeting",
    "targeting_optimization_types",
    "time_based_ad_rotation_id_blocks",
    "time_based_ad_rotation_intervals",
    "trending_topics_spec",
    "updated_time",
    "use_new_app_click",
    "value_rule_set_id",
    "value_rules_applied"
]


async def get_ad_set_ad_studies(ad_set_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_studies on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_set_id}/ad_studies", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_adcreatives(ad_set_id: str, fields: Optional[str] = None) -> str:
    """GET /adcreatives on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_set_id}/adcreatives", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_ads(
    ad_set_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    time_range: Optional[str] = None,
    updated_since: Optional[int] = None,
) -> str:
    """GET /ads on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().get(f"{ad_set_id}/ads", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_asyncadrequests(ad_set_id: str, fields: Optional[str] = None, statuses: Optional[str] = None) -> str:
    """GET /asyncadrequests on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
        statuses: Optional. Values: CANCELED, CANCELED_DEPENDENCY, ERROR, ERROR_CONFLICTS, ERROR_DEPENDENCY, INITIAL, IN_PROGRESS, PENDING_DEPENDENCY, PROCESS_BY_AD_ASYNC_ENGINE, PROCESS_BY_EVENT_PROCESSOR, SUCCESS, USER_CANCELED, USER_CANCELED_DEPENDENCY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if statuses is not None:
        params["statuses"] = statuses
    result = await get_client().get(f"{ad_set_id}/asyncadrequests", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_budget_schedules(
    ad_set_id: str,
    fields: Optional[str] = None,
    time_start: Optional[str] = None,
    time_stop: Optional[str] = None,
) -> str:
    """GET /budget_schedules on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().get(f"{ad_set_id}/budget_schedules", params=params)
    return json.dumps(result, indent=2)


async def create_ad_set_budget_schedules(
    ad_set_id: str,
    budget_value: int,
    budget_value_type: str,
    time_end: int,
    time_start: int,
) -> str:
    """POST /budget_schedules on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().post(f"{ad_set_id}/budget_schedules", data=params)
    return json.dumps(result, indent=2)


async def get_ad_set_copies(
    ad_set_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    is_completed: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /copies on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().get(f"{ad_set_id}/copies", params=params)
    return json.dumps(result, indent=2)


async def copy_ad_set(
    ad_set_id: str,
    campaign_id: Optional[str] = None,
    create_dco_adset: Optional[bool] = None,
    deep_copy: Optional[bool] = None,
    end_time: Optional[str] = None,
    rename_options: Optional[str] = None,
    start_time: Optional[str] = None,
    status_option: Optional[str] = None,
) -> str:
    """POST /copies on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        campaign_id: Optional.
        create_dco_adset: Optional.
        deep_copy: Optional.
        end_time: Optional.
        rename_options: Optional.
        start_time: Optional.
        status_option: Optional. Values: ACTIVE, INHERITED_FROM_SOURCE, PAUSED
    """
    params = {}
    if campaign_id is not None:
        params["campaign_id"] = campaign_id
    if create_dco_adset is not None:
        params["create_dco_adset"] = create_dco_adset
    if deep_copy is not None:
        params["deep_copy"] = deep_copy
    if end_time is not None:
        params["end_time"] = end_time
    if rename_options is not None:
        params["rename_options"] = rename_options
    if start_time is not None:
        params["start_time"] = start_time
    if status_option is not None:
        params["status_option"] = status_option
    result = await get_client().post(f"{ad_set_id}/copies", data=params)
    return json.dumps(result, indent=2)


async def get_ad_set_delivery_estimate(
    ad_set_id: str,
    fields: Optional[str] = None,
    optimization_goal: Optional[str] = None,
    promoted_object: Optional[str] = None,
    targeting_spec: Optional[str] = None,
) -> str:
    """GET /delivery_estimate on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
        optimization_goal: Optional. Values: ADVERTISER_SILOED_VALUE, AD_RECALL_LIFT, APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, AUTOMATIC_OBJECTIVE, CONVERSATIONS, DERIVED_EVENTS, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, IN_APP_VALUE, LANDING_PAGE_VIEWS, LEAD_GENERATION, LINK_CLICKS, MEANINGFUL_CALL_ATTEMPT, MESSAGING_APPOINTMENT_CONVERSION, MESSAGING_PURCHASE_CONVERSION, NONE, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, PROFILE_AND_PAGE_ENGAGEMENT, PROFILE_VISIT, QUALITY_CALL, QUALITY_LEAD, REACH, REMINDERS_SET, SUBSCRIBERS, THRUPLAY, VALUE, VISIT_INSTAGRAM_PROFILE
        promoted_object: Optional.
        targeting_spec: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if optimization_goal is not None:
        params["optimization_goal"] = optimization_goal
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    if targeting_spec is not None:
        params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_set_id}/delivery_estimate", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_insights(
    ad_set_id: str,
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
    """GET /insights on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().get(f"{ad_set_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def create_ad_set_insights(
    ad_set_id: str,
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
    """POST /insights on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
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
    result = await get_client().post(f"{ad_set_id}/insights", data=params)
    return json.dumps(result, indent=2)


async def get_ad_set_message_delivery_estimate(
    ad_set_id: str,
    fields: Optional[str] = None,
    bid_amount: Optional[int] = None,
    daily_budget: Optional[int] = None,
    is_direct_send_campaign: Optional[bool] = None,
    lifetime_budget: Optional[int] = None,
    lifetime_in_days: Optional[int] = None,
    optimization_goal: Optional[str] = None,
    pacing_type: Optional[str] = None,
    promoted_object: Optional[str] = None,
    targeting_spec: Optional[str] = None,
) -> str:
    """GET /message_delivery_estimate on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
        bid_amount: Optional.
        daily_budget: Optional.
        is_direct_send_campaign: Optional.
        lifetime_budget: Optional.
        lifetime_in_days: Optional.
        optimization_goal: Optional. Values: ADVERTISER_SILOED_VALUE, AD_RECALL_LIFT, APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, AUTOMATIC_OBJECTIVE, CONVERSATIONS, DERIVED_EVENTS, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, IN_APP_VALUE, LANDING_PAGE_VIEWS, LEAD_GENERATION, LINK_CLICKS, MEANINGFUL_CALL_ATTEMPT, MESSAGING_APPOINTMENT_CONVERSION, MESSAGING_PURCHASE_CONVERSION, NONE, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, PROFILE_AND_PAGE_ENGAGEMENT, PROFILE_VISIT, QUALITY_CALL, QUALITY_LEAD, REACH, REMINDERS_SET, SUBSCRIBERS, THRUPLAY, VALUE, VISIT_INSTAGRAM_PROFILE
        pacing_type: Optional. Values: DAY_PARTING, DISABLED, NO_PACING, PROBABILISTIC_PACING, PROBABILISTIC_PACING_V2, STANDARD
        promoted_object: Optional.
        targeting_spec: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    if daily_budget is not None:
        params["daily_budget"] = daily_budget
    if is_direct_send_campaign is not None:
        params["is_direct_send_campaign"] = is_direct_send_campaign
    if lifetime_budget is not None:
        params["lifetime_budget"] = lifetime_budget
    if lifetime_in_days is not None:
        params["lifetime_in_days"] = lifetime_in_days
    if optimization_goal is not None:
        params["optimization_goal"] = optimization_goal
    if pacing_type is not None:
        params["pacing_type"] = pacing_type
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    if targeting_spec is not None:
        params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_set_id}/message_delivery_estimate", params=params)
    return json.dumps(result, indent=2)


async def get_ad_set_targetingsentencelines(ad_set_id: str, fields: Optional[str] = None) -> str:
    """GET /targetingsentencelines on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_set_id}/targetingsentencelines", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_set(ad_set_id: str) -> str:
    """DELETE /#delete on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
    """
    params = {}
    result = await get_client().delete(f"{ad_set_id}")
    return json.dumps(result, indent=2)


async def get_ad_set(
    ad_set_id: str,
    fields: Optional[str] = None,
    am_call_tags: Optional[str] = None,
    date_preset: Optional[str] = None,
    from_adtable: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /#get on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        fields: Comma-separated list of fields to return. Available: account_id, adlabels, adset_schedule, anchor_event_attribution_window_days, asset_feed_id, attribution_spec, automatic_manual_state, bid_adjustments, bid_amount, bid_constraints, bid_info, bid_strategy, billing_event, brand_safety_config, budget_remaining, campaign, campaign_active_time, campaign_attribution, campaign_id, configured_status, created_time, creative_sequence, creative_sequence_repetition_pattern, daily_budget, daily_min_spend_target, daily_spend_cap, destination_type, dsa_beneficiary, dsa_payor, effective_status, end_time, existing_customer_budget_percentage, frequency_control_specs, full_funnel_exploration_mode, id, instagram_user_id, is_ba_skip_delayed_eligible, is_budget_schedule_enabled, is_dynamic_creative, is_incremental_attribution_enabled, issues_info, learning_stage_info, lifetime_budget, lifetime_imps, lifetime_min_spend_target, lifetime_spend_cap, max_budget_spend_percentage, min_budget_spend_percentage, multi_optimization_goal_weight, name, optimization_goal, optimization_sub_event, pacing_type, placement_soft_opt_out, promoted_object, recommendations, recurring_budget_semantics, regional_regulated_categories, regional_regulation_identities, review_feedback, rf_prediction_id, source_adset, source_adset_id, start_time, status, targeting, targeting_optimization_types, time_based_ad_rotation_id_blocks, time_based_ad_rotation_intervals, trending_topics_spec, updated_time, use_new_app_click, value_rule_set_id, value_rules_applied
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
    result = await get_client().get(f"{ad_set_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_set(
    ad_set_id: str,
    account_id: Optional[str] = None,
    adlabels: Optional[str] = None,
    adset_schedule: Optional[str] = None,
    attribution_spec: Optional[str] = None,
    automatic_manual_state: Optional[str] = None,
    bid_adjustments: Optional[str] = None,
    bid_amount: Optional[int] = None,
    bid_constraints: Optional[str] = None,
    bid_strategy: Optional[str] = None,
    billing_event: Optional[str] = None,
    budget_schedule_specs: Optional[str] = None,
    campaign_attribution: Optional[str] = None,
    campaign_spec: Optional[str] = None,
    creative_sequence: Optional[str] = None,
    creative_sequence_repetition_pattern: Optional[str] = None,
    daily_budget: Optional[int] = None,
    daily_imps: Optional[int] = None,
    daily_min_spend_target: Optional[int] = None,
    daily_spend_cap: Optional[int] = None,
    date_format: Optional[str] = None,
    destination_type: Optional[str] = None,
    dsa_beneficiary: Optional[str] = None,
    dsa_payor: Optional[str] = None,
    end_time: Optional[str] = None,
    execution_options: Optional[str] = None,
    existing_customer_budget_percentage: Optional[int] = None,
    full_funnel_exploration_mode: Optional[str] = None,
    is_ba_skip_delayed_eligible: Optional[bool] = None,
    is_budget_schedule_enabled: Optional[bool] = None,
    is_incremental_attribution_enabled: Optional[bool] = None,
    is_sac_cfca_terms_certified: Optional[bool] = None,
    lifetime_budget: Optional[int] = None,
    lifetime_imps: Optional[int] = None,
    lifetime_min_spend_target: Optional[int] = None,
    lifetime_spend_cap: Optional[int] = None,
    max_budget_spend_percentage: Optional[int] = None,
    min_budget_spend_percentage: Optional[int] = None,
    multi_optimization_goal_weight: Optional[str] = None,
    name: Optional[str] = None,
    optimization_goal: Optional[str] = None,
    optimization_sub_event: Optional[str] = None,
    pacing_type: Optional[str] = None,
    placement_soft_opt_out: Optional[str] = None,
    promoted_object: Optional[str] = None,
    rb_prediction_id: Optional[str] = None,
    regional_regulated_categories: Optional[str] = None,
    regional_regulation_identities: Optional[str] = None,
    rf_prediction_id: Optional[str] = None,
    start_time: Optional[str] = None,
    status: Optional[str] = None,
    targeting: Optional[str] = None,
    time_based_ad_rotation_id_blocks: Optional[str] = None,
    time_based_ad_rotation_intervals: Optional[str] = None,
    time_start: Optional[str] = None,
    time_stop: Optional[str] = None,
    trending_topics_spec: Optional[str] = None,
    tune_for_category: Optional[str] = None,
    value_rule_set_id: Optional[str] = None,
    value_rules_applied: Optional[bool] = None,
) -> str:
    """POST /#update on AdSet.

    Args:
        ad_set_id: The ID of the AdSet object.
        account_id: Optional.
        adlabels: Optional.
        adset_schedule: Optional.
        attribution_spec: Optional.
        automatic_manual_state: Optional.
        bid_adjustments: Optional.
        bid_amount: Optional.
        bid_constraints: Optional.
        bid_strategy: Optional.
        billing_event: Optional.
        budget_schedule_specs: Optional.
        campaign_attribution: Optional.
        campaign_spec: Optional.
        creative_sequence: Optional.
        creative_sequence_repetition_pattern: Optional.
        daily_budget: Optional.
        daily_imps: Optional.
        daily_min_spend_target: Optional.
        daily_spend_cap: Optional.
        date_format: Optional.
        destination_type: Optional.
        dsa_beneficiary: Optional.
        dsa_payor: Optional.
        end_time: Optional.
        execution_options: Optional.
        existing_customer_budget_percentage: Optional.
        full_funnel_exploration_mode: Optional.
        is_ba_skip_delayed_eligible: Optional.
        is_budget_schedule_enabled: Optional.
        is_incremental_attribution_enabled: Optional.
        is_sac_cfca_terms_certified: Optional.
        lifetime_budget: Optional.
        lifetime_imps: Optional.
        lifetime_min_spend_target: Optional.
        lifetime_spend_cap: Optional.
        max_budget_spend_percentage: Optional.
        min_budget_spend_percentage: Optional.
        multi_optimization_goal_weight: Optional.
        name: Optional.
        optimization_goal: Optional.
        optimization_sub_event: Optional.
        pacing_type: Optional.
        placement_soft_opt_out: Optional.
        promoted_object: Optional.
        rb_prediction_id: Optional.
        regional_regulated_categories: Optional.
        regional_regulation_identities: Optional.
        rf_prediction_id: Optional.
        start_time: Optional.
        status: Optional.
        targeting: Optional.
        time_based_ad_rotation_id_blocks: Optional.
        time_based_ad_rotation_intervals: Optional.
        time_start: Optional.
        time_stop: Optional.
        trending_topics_spec: Optional.
        tune_for_category: Optional.
        value_rule_set_id: Optional.
        value_rules_applied: Optional.
    """
    params = {}
    if account_id is not None:
        params["account_id"] = account_id
    if adlabels is not None:
        params["adlabels"] = adlabels
    if adset_schedule is not None:
        params["adset_schedule"] = adset_schedule
    if attribution_spec is not None:
        params["attribution_spec"] = attribution_spec
    if automatic_manual_state is not None:
        params["automatic_manual_state"] = automatic_manual_state
    if bid_adjustments is not None:
        params["bid_adjustments"] = bid_adjustments
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    if bid_constraints is not None:
        params["bid_constraints"] = bid_constraints
    if bid_strategy is not None:
        params["bid_strategy"] = bid_strategy
    if billing_event is not None:
        params["billing_event"] = billing_event
    if budget_schedule_specs is not None:
        params["budget_schedule_specs"] = budget_schedule_specs
    if campaign_attribution is not None:
        params["campaign_attribution"] = campaign_attribution
    if campaign_spec is not None:
        params["campaign_spec"] = campaign_spec
    if creative_sequence is not None:
        params["creative_sequence"] = creative_sequence
    if creative_sequence_repetition_pattern is not None:
        params["creative_sequence_repetition_pattern"] = creative_sequence_repetition_pattern
    if daily_budget is not None:
        params["daily_budget"] = daily_budget
    if daily_imps is not None:
        params["daily_imps"] = daily_imps
    if daily_min_spend_target is not None:
        params["daily_min_spend_target"] = daily_min_spend_target
    if daily_spend_cap is not None:
        params["daily_spend_cap"] = daily_spend_cap
    if date_format is not None:
        params["date_format"] = date_format
    if destination_type is not None:
        params["destination_type"] = destination_type
    if dsa_beneficiary is not None:
        params["dsa_beneficiary"] = dsa_beneficiary
    if dsa_payor is not None:
        params["dsa_payor"] = dsa_payor
    if end_time is not None:
        params["end_time"] = end_time
    if execution_options is not None:
        params["execution_options"] = execution_options
    if existing_customer_budget_percentage is not None:
        params["existing_customer_budget_percentage"] = existing_customer_budget_percentage
    if full_funnel_exploration_mode is not None:
        params["full_funnel_exploration_mode"] = full_funnel_exploration_mode
    if is_ba_skip_delayed_eligible is not None:
        params["is_ba_skip_delayed_eligible"] = is_ba_skip_delayed_eligible
    if is_budget_schedule_enabled is not None:
        params["is_budget_schedule_enabled"] = is_budget_schedule_enabled
    if is_incremental_attribution_enabled is not None:
        params["is_incremental_attribution_enabled"] = is_incremental_attribution_enabled
    if is_sac_cfca_terms_certified is not None:
        params["is_sac_cfca_terms_certified"] = is_sac_cfca_terms_certified
    if lifetime_budget is not None:
        params["lifetime_budget"] = lifetime_budget
    if lifetime_imps is not None:
        params["lifetime_imps"] = lifetime_imps
    if lifetime_min_spend_target is not None:
        params["lifetime_min_spend_target"] = lifetime_min_spend_target
    if lifetime_spend_cap is not None:
        params["lifetime_spend_cap"] = lifetime_spend_cap
    if max_budget_spend_percentage is not None:
        params["max_budget_spend_percentage"] = max_budget_spend_percentage
    if min_budget_spend_percentage is not None:
        params["min_budget_spend_percentage"] = min_budget_spend_percentage
    if multi_optimization_goal_weight is not None:
        params["multi_optimization_goal_weight"] = multi_optimization_goal_weight
    if name is not None:
        params["name"] = name
    if optimization_goal is not None:
        params["optimization_goal"] = optimization_goal
    if optimization_sub_event is not None:
        params["optimization_sub_event"] = optimization_sub_event
    if pacing_type is not None:
        params["pacing_type"] = pacing_type
    if placement_soft_opt_out is not None:
        params["placement_soft_opt_out"] = placement_soft_opt_out
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    if rb_prediction_id is not None:
        params["rb_prediction_id"] = rb_prediction_id
    if regional_regulated_categories is not None:
        params["regional_regulated_categories"] = regional_regulated_categories
    if regional_regulation_identities is not None:
        params["regional_regulation_identities"] = regional_regulation_identities
    if rf_prediction_id is not None:
        params["rf_prediction_id"] = rf_prediction_id
    if start_time is not None:
        params["start_time"] = start_time
    if status is not None:
        params["status"] = status
    if targeting is not None:
        params["targeting"] = targeting
    if time_based_ad_rotation_id_blocks is not None:
        params["time_based_ad_rotation_id_blocks"] = time_based_ad_rotation_id_blocks
    if time_based_ad_rotation_intervals is not None:
        params["time_based_ad_rotation_intervals"] = time_based_ad_rotation_intervals
    if time_start is not None:
        params["time_start"] = time_start
    if time_stop is not None:
        params["time_stop"] = time_stop
    if trending_topics_spec is not None:
        params["trending_topics_spec"] = trending_topics_spec
    if tune_for_category is not None:
        params["tune_for_category"] = tune_for_category
    if value_rule_set_id is not None:
        params["value_rule_set_id"] = value_rule_set_id
    if value_rules_applied is not None:
        params["value_rules_applied"] = value_rules_applied
    result = await get_client().post(f"{ad_set_id}", data=params)
    return json.dumps(result, indent=2)

