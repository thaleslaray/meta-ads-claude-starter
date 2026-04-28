"""Auto-generated Meta Marketing API tools — ads."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_FIELDS = [
    "account_id",
    "ad_active_time",
    "ad_review_feedback",
    "ad_schedule_end_time",
    "ad_schedule_start_time",
    "adlabels",
    "adset",
    "adset_id",
    "bid_amount",
    "bid_info",
    "bid_type",
    "campaign",
    "campaign_id",
    "configured_status",
    "conversion_domain",
    "conversion_specs",
    "created_time",
    "creative",
    "creative_asset_groups_spec",
    "demolink_hash",
    "display_sequence",
    "effective_status",
    "engagement_audience",
    "failed_delivery_checks",
    "id",
    "issues_info",
    "last_updated_by_app_id",
    "name",
    "placement",
    "preview_shareable_link",
    "priority",
    "recommendations",
    "source_ad",
    "source_ad_id",
    "status",
    "targeting",
    "tracking_and_conversion_with_defaults",
    "tracking_specs",
    "updated_time"
]


async def get_ad_adcreatives(ad_id: str, fields: Optional[str] = None) -> str:
    """GET /adcreatives on Ad.

    Args:
        ad_id: The ID of the Ad object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_id}/adcreatives", params=params)
    return json.dumps(result, indent=2)


async def get_ad_copies(
    ad_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    time_range: Optional[str] = None,
    updated_since: Optional[int] = None,
) -> str:
    """GET /copies on Ad.

    Args:
        ad_id: The ID of the Ad object.
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
    result = await get_client().get(f"{ad_id}/copies", params=params)
    return json.dumps(result, indent=2)


async def copy_ad(
    ad_id: str,
    adset_id: Optional[str] = None,
    creative_parameters: Optional[str] = None,
    rename_options: Optional[str] = None,
    status_option: Optional[str] = None,
) -> str:
    """POST /copies on Ad.

    Args:
        ad_id: The ID of the Ad object.
        adset_id: Optional.
        creative_parameters: Optional.
        rename_options: Optional.
        status_option: Optional. Values: ACTIVE, INHERITED_FROM_SOURCE, PAUSED
    """
    params = {}
    if adset_id is not None:
        params["adset_id"] = adset_id
    if creative_parameters is not None:
        params["creative_parameters"] = creative_parameters
    if rename_options is not None:
        params["rename_options"] = rename_options
    if status_option is not None:
        params["status_option"] = status_option
    result = await get_client().post(f"{ad_id}/copies", data=params)
    return json.dumps(result, indent=2)


async def get_ad_insights(
    ad_id: str,
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
    """GET /insights on Ad.

    Args:
        ad_id: The ID of the Ad object.
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
    result = await get_client().get(f"{ad_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def create_ad_insights(
    ad_id: str,
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
    """POST /insights on Ad.

    Args:
        ad_id: The ID of the Ad object.
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
    result = await get_client().post(f"{ad_id}/insights", data=params)
    return json.dumps(result, indent=2)


async def get_ad_leads(ad_id: str, fields: Optional[str] = None) -> str:
    """GET /leads on Ad.

    Args:
        ad_id: The ID of the Ad object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_id}/leads", params=params)
    return json.dumps(result, indent=2)


async def get_ad_previews(
    ad_id: str,
    ad_format: str,
    fields: Optional[str] = None,
    creative_feature: Optional[str] = None,
    dynamic_asset_label: Optional[str] = None,
    dynamic_creative_spec: Optional[str] = None,
    dynamic_customization: Optional[str] = None,
    end_date: Optional[str] = None,
    height: Optional[int] = None,
    locale: Optional[str] = None,
    place_page_id: Optional[int] = None,
    post: Optional[str] = None,
    product_item_ids: Optional[str] = None,
    render_type: Optional[str] = None,
    start_date: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /previews on Ad.

    Args:
        ad_id: The ID of the Ad object.
        fields: Comma-separated list of fields to return.
        ad_format: Required. Values: AUDIENCE_NETWORK_INSTREAM_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE, AUDIENCE_NETWORK_OUTSTREAM_VIDEO, AUDIENCE_NETWORK_REWARDED_VIDEO, BIZ_DISCO_FEED_MOBILE, DESKTOP_FEED_STANDARD, FACEBOOK_IFU_REELS_MOBILE, FACEBOOK_PROFILE_FEED_DESKTOP, FACEBOOK_PROFILE_FEED_MOBILE, FACEBOOK_PROFILE_REELS_MOBILE, FACEBOOK_REELS_BANNER, FACEBOOK_REELS_BANNER_DESKTOP, FACEBOOK_REELS_BANNER_FEED_ANDROID, FACEBOOK_REELS_BANNER_FEED_ANDROID_LARGE, FACEBOOK_REELS_BANNER_FULLSCREEN_IOS, FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE, FACEBOOK_REELS_MOBILE, FACEBOOK_REELS_POSTLOOP, FACEBOOK_REELS_POSTLOOP_FEED, FACEBOOK_REELS_STICKER, FACEBOOK_STORY_MOBILE, FACEBOOK_STORY_STICKER_MOBILE, INSTAGRAM_EXPLORE_CONTEXTUAL, INSTAGRAM_EXPLORE_GRID_HOME, INSTAGRAM_EXPLORE_IMMERSIVE, INSTAGRAM_FEED_WEB, INSTAGRAM_FEED_WEB_M_SITE, INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS, INSTAGRAM_PROFILE_FEED, INSTAGRAM_PROFILE_REELS, INSTAGRAM_REELS, INSTAGRAM_REELS_INSTREAM, INSTAGRAM_REELS_OVERLAY, INSTAGRAM_REELS_WEB, INSTAGRAM_REELS_WEB_M_SITE, INSTAGRAM_SEARCH_CHAIN, INSTAGRAM_SEARCH_GRID, INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTAGRAM_STORY_EFFECT_TRAY, INSTAGRAM_STORY_WEB, INSTAGRAM_STORY_WEB_M_SITE, INSTANT_ARTICLE_RECIRCULATION_AD, INSTANT_ARTICLE_STANDARD, INSTREAM_BANNER_DESKTOP, INSTREAM_BANNER_FEED_IOS, INSTREAM_BANNER_FULLSCREEN_IOS, INSTREAM_BANNER_FULLSCREEN_MOBILE, INSTREAM_BANNER_IMMERSIVE_MOBILE, INSTREAM_BANNER_MOBILE, INSTREAM_VIDEO_DESKTOP, INSTREAM_VIDEO_FULLSCREEN_IOS, INSTREAM_VIDEO_FULLSCREEN_MOBILE, INSTREAM_VIDEO_IMAGE, INSTREAM_VIDEO_IMMERSIVE_MOBILE, INSTREAM_VIDEO_MOBILE, JOB_BROWSER_DESKTOP, JOB_BROWSER_MOBILE, MARKETPLACE_MOBILE, MESSENGER_MOBILE_INBOX_MEDIA, MESSENGER_MOBILE_STORY_MEDIA, MOBILE_BANNER, MOBILE_FEED_BASIC, MOBILE_FEED_STANDARD, MOBILE_FULLWIDTH, MOBILE_INTERSTITIAL, MOBILE_MEDIUM_RECTANGLE, MOBILE_NATIVE, RIGHT_COLUMN_STANDARD, SUGGESTED_VIDEO_DESKTOP, SUGGESTED_VIDEO_FULLSCREEN_MOBILE, SUGGESTED_VIDEO_IMMERSIVE_MOBILE, SUGGESTED_VIDEO_MOBILE, WATCH_FEED_HOME, WATCH_FEED_MOBILE
        creative_feature: Optional. Values: product_metadata_automation, profile_card, standard_enhancements_catalog, text_overlay_translation
        dynamic_asset_label: Optional.
        dynamic_creative_spec: Optional.
        dynamic_customization: Optional.
        end_date: Optional.
        height: Optional.
        locale: Optional.
        place_page_id: Optional.
        post: Optional.
        product_item_ids: Optional.
        render_type: Optional. Values: FALLBACK
        start_date: Optional.
        width: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["ad_format"] = ad_format
    if creative_feature is not None:
        params["creative_feature"] = creative_feature
    if dynamic_asset_label is not None:
        params["dynamic_asset_label"] = dynamic_asset_label
    if dynamic_creative_spec is not None:
        params["dynamic_creative_spec"] = dynamic_creative_spec
    if dynamic_customization is not None:
        params["dynamic_customization"] = dynamic_customization
    if end_date is not None:
        params["end_date"] = end_date
    if height is not None:
        params["height"] = height
    if locale is not None:
        params["locale"] = locale
    if place_page_id is not None:
        params["place_page_id"] = place_page_id
    if post is not None:
        params["post"] = post
    if product_item_ids is not None:
        params["product_item_ids"] = product_item_ids
    if render_type is not None:
        params["render_type"] = render_type
    if start_date is not None:
        params["start_date"] = start_date
    if width is not None:
        params["width"] = width
    result = await get_client().get(f"{ad_id}/previews", params=params)
    return json.dumps(result, indent=2)


async def get_ad_targetingsentencelines(ad_id: str, fields: Optional[str] = None) -> str:
    """GET /targetingsentencelines on Ad.

    Args:
        ad_id: The ID of the Ad object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_id}/targetingsentencelines", params=params)
    return json.dumps(result, indent=2)


async def delete_ad(ad_id: str) -> str:
    """DELETE /#delete on Ad.

    Args:
        ad_id: The ID of the Ad object.
    """
    params = {}
    result = await get_client().delete(f"{ad_id}")
    return json.dumps(result, indent=2)


async def get_ad(
    ad_id: str,
    fields: Optional[str] = None,
    am_call_tags: Optional[str] = None,
    date_preset: Optional[str] = None,
    from_adtable: Optional[bool] = None,
    review_feedback_breakdown: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /#get on Ad.

    Args:
        ad_id: The ID of the Ad object.
        fields: Comma-separated list of fields to return. Available: account_id, ad_active_time, ad_review_feedback, ad_schedule_end_time, ad_schedule_start_time, adlabels, adset, adset_id, bid_amount, bid_info, bid_type, campaign, campaign_id, configured_status, conversion_domain, conversion_specs, created_time, creative, creative_asset_groups_spec, demolink_hash, display_sequence, effective_status, engagement_audience, failed_delivery_checks, id, issues_info, last_updated_by_app_id, name, placement, preview_shareable_link, priority, recommendations, source_ad, source_ad_id, status, targeting, tracking_and_conversion_with_defaults, tracking_specs, updated_time
        am_call_tags: Optional.
        date_preset: Optional.
        from_adtable: Optional.
        review_feedback_breakdown: Optional.
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
    if review_feedback_breakdown is not None:
        params["review_feedback_breakdown"] = review_feedback_breakdown
    if time_range is not None:
        params["time_range"] = time_range
    result = await get_client().get(f"{ad_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad(
    ad_id: str,
    ad_schedule_end_time: Optional[str] = None,
    ad_schedule_start_time: Optional[str] = None,
    adlabels: Optional[str] = None,
    adset_spec: Optional[str] = None,
    audience_id: Optional[str] = None,
    bid_amount: Optional[int] = None,
    conversion_domain: Optional[str] = None,
    creative: Optional[str] = None,
    creative_asset_groups_spec: Optional[str] = None,
    display_sequence: Optional[int] = None,
    draft_adgroup_id: Optional[str] = None,
    engagement_audience: Optional[bool] = None,
    execution_options: Optional[str] = None,
    include_demolink_hashes: Optional[bool] = None,
    name: Optional[str] = None,
    priority: Optional[int] = None,
    status: Optional[str] = None,
    tracking_specs: Optional[str] = None,
) -> str:
    """POST /#update on Ad.

    Args:
        ad_id: The ID of the Ad object.
        ad_schedule_end_time: Optional.
        ad_schedule_start_time: Optional.
        adlabels: Optional.
        adset_spec: Optional.
        audience_id: Optional.
        bid_amount: Optional.
        conversion_domain: Optional.
        creative: Optional.
        creative_asset_groups_spec: Optional.
        display_sequence: Optional.
        draft_adgroup_id: Optional.
        engagement_audience: Optional.
        execution_options: Optional.
        include_demolink_hashes: Optional.
        name: Optional.
        priority: Optional.
        status: Optional.
        tracking_specs: Optional.
    """
    params = {}
    if ad_schedule_end_time is not None:
        params["ad_schedule_end_time"] = ad_schedule_end_time
    if ad_schedule_start_time is not None:
        params["ad_schedule_start_time"] = ad_schedule_start_time
    if adlabels is not None:
        params["adlabels"] = adlabels
    if adset_spec is not None:
        params["adset_spec"] = adset_spec
    if audience_id is not None:
        params["audience_id"] = audience_id
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    if conversion_domain is not None:
        params["conversion_domain"] = conversion_domain
    if creative is not None:
        params["creative"] = creative
    if creative_asset_groups_spec is not None:
        params["creative_asset_groups_spec"] = creative_asset_groups_spec
    if display_sequence is not None:
        params["display_sequence"] = display_sequence
    if draft_adgroup_id is not None:
        params["draft_adgroup_id"] = draft_adgroup_id
    if engagement_audience is not None:
        params["engagement_audience"] = engagement_audience
    if execution_options is not None:
        params["execution_options"] = execution_options
    if include_demolink_hashes is not None:
        params["include_demolink_hashes"] = include_demolink_hashes
    if name is not None:
        params["name"] = name
    if priority is not None:
        params["priority"] = priority
    if status is not None:
        params["status"] = status
    if tracking_specs is not None:
        params["tracking_specs"] = tracking_specs
    result = await get_client().post(f"{ad_id}", data=params)
    return json.dumps(result, indent=2)

