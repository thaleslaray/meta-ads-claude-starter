"""Auto-generated Meta Marketing API tools — accounts."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_ACCOUNT_FIELDS = [
    "account_id",
    "account_status",
    "ad_account_promotable_objects",
    "age",
    "agency_client_declaration",
    "all_capabilities",
    "amount_spent",
    "attribution_spec",
    "balance",
    "brand_safety_content_filter_levels",
    "business",
    "business_city",
    "business_country_code",
    "business_name",
    "business_state",
    "business_street",
    "business_street2",
    "business_zip",
    "can_create_brand_lift_study",
    "capabilities",
    "created_time",
    "currency",
    "custom_audience_info",
    "default_dsa_beneficiary",
    "default_dsa_payor",
    "disable_reason",
    "end_advertiser",
    "end_advertiser_name",
    "existing_customers",
    "expired_funding_source_details",
    "extended_credit_invoice_group",
    "failed_delivery_checks",
    "fb_entity",
    "funding_source",
    "funding_source_details",
    "has_migrated_permissions",
    "has_page_authorized_adaccount",
    "id",
    "io_number",
    "is_attribution_spec_system_default",
    "is_ba_skip_delayed_eligible",
    "is_direct_deals_enabled",
    "is_in_3ds_authorization_enabled_market",
    "is_notifications_enabled",
    "is_personal",
    "is_prepay_account",
    "is_tax_id_required",
    "liable_address",
    "line_numbers",
    "media_agency",
    "min_campaign_group_spend_cap",
    "min_daily_budget",
    "name",
    "offsite_pixels_tos_accepted",
    "opportunity_score",
    "owner",
    "owner_business",
    "partner",
    "rf_spec",
    "send_bill_to_address",
    "show_checkout_experience",
    "sold_to_address",
    "spend_cap",
    "tax_id",
    "tax_id_status",
    "tax_id_type",
    "timezone_id",
    "timezone_name",
    "timezone_offset_hours_utc",
    "tos_accepted",
    "user_access_expire_time",
    "user_tasks",
    "user_tos_accepted",
    "viewable_business"
]


async def get_ad_account_account_controls(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /account_controls on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/account_controls", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_account_controls(
    account_id: str,
    audience_controls: str,
    placement_controls: Optional[str] = None,
) -> str:
    """POST /account_controls on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        audience_controls: Required.
        placement_controls: Optional.
    """
    params = {}
    params["audience_controls"] = audience_controls
    if placement_controls is not None:
        params["placement_controls"] = placement_controls
    result = await get_client().post(f"act_{account_id}/account_controls", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ad_place_page_sets(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_place_page_sets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/ad_place_page_sets", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_ad_place_page_sets(
    account_id: str,
    name: str,
    parent_page: str,
    location_types: Optional[str] = None,
    targeted_area_type: Optional[str] = None,
) -> str:
    """POST /ad_place_page_sets on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        location_types: Optional. Values: home, recent
        name: Required.
        parent_page: Required.
        targeted_area_type: Optional. Values: CUSTOM_RADIUS, MARKETING_AREA, NONE
    """
    params = {}
    if location_types is not None:
        params["location_types"] = location_types
    params["name"] = name
    params["parent_page"] = parent_page
    if targeted_area_type is not None:
        params["targeted_area_type"] = targeted_area_type
    result = await get_client().post(f"act_{account_id}/ad_place_page_sets", data=params)
    return json.dumps(result, indent=2)


async def create_ad_account_ad_place_page_sets_async(
    account_id: str,
    name: str,
    parent_page: str,
    location_types: Optional[str] = None,
    targeted_area_type: Optional[str] = None,
) -> str:
    """POST /ad_place_page_sets_async on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        location_types: Optional. Values: home, recent
        name: Required.
        parent_page: Required.
        targeted_area_type: Optional. Values: CUSTOM_RADIUS, MARKETING_AREA, NONE
    """
    params = {}
    if location_types is not None:
        params["location_types"] = location_types
    params["name"] = name
    params["parent_page"] = parent_page
    if targeted_area_type is not None:
        params["targeted_area_type"] = targeted_area_type
    result = await get_client().post(f"act_{account_id}/ad_place_page_sets_async", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ad_saved_keywords(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_saved_keywords on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if fields is not None:
        params["fields"] = fields
    result = await get_client().get(f"{ad_account_id}/ad_saved_keywords", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ad_studies(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_studies on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/ad_studies", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adcloudplayables(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /adcloudplayables on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/adcloudplayables", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adcreatives(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /adcreatives on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/adcreatives", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adcreatives(
    account_id: str,
    actor_id: Optional[int] = None,
    ad_disclaimer_spec: Optional[str] = None,
    adlabels: Optional[str] = None,
    applink_treatment: Optional[str] = None,
    asset_feed_spec: Optional[str] = None,
    authorization_category: Optional[str] = None,
    body: Optional[str] = None,
    branded_content: Optional[str] = None,
    branded_content_sponsor_page_id: Optional[str] = None,
    bundle_folder_id: Optional[str] = None,
    call_to_action: Optional[str] = None,
    categorization_criteria: Optional[str] = None,
    category_media_source: Optional[str] = None,
    contextual_multi_ads: Optional[str] = None,
    creative_sourcing_spec: Optional[str] = None,
    degrees_of_freedom_spec: Optional[str] = None,
    destination_set_id: Optional[str] = None,
    destination_spec: Optional[str] = None,
    dynamic_ad_voice: Optional[str] = None,
    enable_launch_instant_app: Optional[bool] = None,
    execution_options: Optional[str] = None,
    facebook_branded_content: Optional[str] = None,
    format_transformation_spec: Optional[str] = None,
    image_crops: Optional[str] = None,
    image_file: Optional[str] = None,
    image_hash: Optional[str] = None,
    image_url: Optional[str] = None,
    instagram_branded_content: Optional[str] = None,
    instagram_permalink_url: Optional[str] = None,
    instagram_user_id: Optional[str] = None,
    interactive_components_spec: Optional[str] = None,
    is_dco_internal: Optional[bool] = None,
    link_og_id: Optional[str] = None,
    link_url: Optional[str] = None,
    media_sourcing_spec: Optional[str] = None,
    name: Optional[str] = None,
    object_id: Optional[int] = None,
    object_story_id: Optional[str] = None,
    object_story_spec: Optional[str] = None,
    object_type: Optional[str] = None,
    object_url: Optional[str] = None,
    omnichannel_link_spec: Optional[str] = None,
    page_welcome_message: Optional[str] = None,
    place_page_set_id: Optional[str] = None,
    platform_customizations: Optional[str] = None,
    playable_asset_id: Optional[str] = None,
    portrait_customizations: Optional[str] = None,
    product_set_id: Optional[str] = None,
    recommender_settings: Optional[str] = None,
    regional_regulation_disclaimer_spec: Optional[str] = None,
    source_instagram_media_id: Optional[str] = None,
    template_url: Optional[str] = None,
    template_url_spec: Optional[str] = None,
    thumbnail_url: Optional[str] = None,
    title: Optional[str] = None,
    url_tags: Optional[str] = None,
    use_page_actor_override: Optional[bool] = None,
) -> str:
    """POST /adcreatives on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        actor_id: Optional.
        ad_disclaimer_spec: Optional.
        adlabels: Optional.
        applink_treatment: Optional. Values: automatic, deeplink_with_appstore_fallback, deeplink_with_web_fallback, web_only
        asset_feed_spec: Optional.
        authorization_category: Optional. Values: NONE, POLITICAL, POLITICAL_WITH_DIGITALLY_CREATED_MEDIA
        body: Optional.
        branded_content: Optional.
        branded_content_sponsor_page_id: Optional.
        bundle_folder_id: Optional.
        call_to_action: Optional.
        categorization_criteria: Optional. Values: brand, category, product_type
        category_media_source: Optional. Values: CATEGORY, MIXED, PRODUCTS_COLLAGE, PRODUCTS_SLIDESHOW
        contextual_multi_ads: Optional.
        creative_sourcing_spec: Optional.
        degrees_of_freedom_spec: Optional.
        destination_set_id: Optional.
        destination_spec: Optional.
        dynamic_ad_voice: Optional. Values: DYNAMIC, STORY_OWNER
        enable_launch_instant_app: Optional.
        execution_options: Optional. Values: validate_only
        facebook_branded_content: Optional.
        format_transformation_spec: Optional.
        image_crops: Optional.
        image_file: Optional.
        image_hash: Optional.
        image_url: Optional.
        instagram_branded_content: Optional.
        instagram_permalink_url: Optional.
        instagram_user_id: Optional.
        interactive_components_spec: Optional.
        is_dco_internal: Optional.
        link_og_id: Optional.
        link_url: Optional.
        media_sourcing_spec: Optional.
        name: Optional.
        object_id: Optional.
        object_story_id: Optional.
        object_story_spec: Optional.
        object_type: Optional.
        object_url: Optional.
        omnichannel_link_spec: Optional.
        page_welcome_message: Optional.
        place_page_set_id: Optional.
        platform_customizations: Optional.
        playable_asset_id: Optional.
        portrait_customizations: Optional.
        product_set_id: Optional.
        recommender_settings: Optional.
        regional_regulation_disclaimer_spec: Optional.
        source_instagram_media_id: Optional.
        template_url: Optional.
        template_url_spec: Optional.
        thumbnail_url: Optional.
        title: Optional.
        url_tags: Optional.
        use_page_actor_override: Optional.
    """
    params = {}
    if actor_id is not None:
        params["actor_id"] = actor_id
    if ad_disclaimer_spec is not None:
        params["ad_disclaimer_spec"] = ad_disclaimer_spec
    if adlabels is not None:
        params["adlabels"] = adlabels
    if applink_treatment is not None:
        params["applink_treatment"] = applink_treatment
    if asset_feed_spec is not None:
        params["asset_feed_spec"] = asset_feed_spec
    if authorization_category is not None:
        params["authorization_category"] = authorization_category
    if body is not None:
        params["body"] = body
    if branded_content is not None:
        params["branded_content"] = branded_content
    if branded_content_sponsor_page_id is not None:
        params["branded_content_sponsor_page_id"] = branded_content_sponsor_page_id
    if bundle_folder_id is not None:
        params["bundle_folder_id"] = bundle_folder_id
    if call_to_action is not None:
        params["call_to_action"] = call_to_action
    if categorization_criteria is not None:
        params["categorization_criteria"] = categorization_criteria
    if category_media_source is not None:
        params["category_media_source"] = category_media_source
    if contextual_multi_ads is not None:
        params["contextual_multi_ads"] = contextual_multi_ads
    if creative_sourcing_spec is not None:
        params["creative_sourcing_spec"] = creative_sourcing_spec
    if degrees_of_freedom_spec is not None:
        params["degrees_of_freedom_spec"] = degrees_of_freedom_spec
    if destination_set_id is not None:
        params["destination_set_id"] = destination_set_id
    if destination_spec is not None:
        params["destination_spec"] = destination_spec
    if dynamic_ad_voice is not None:
        params["dynamic_ad_voice"] = dynamic_ad_voice
    if enable_launch_instant_app is not None:
        params["enable_launch_instant_app"] = enable_launch_instant_app
    if execution_options is not None:
        params["execution_options"] = execution_options
    if facebook_branded_content is not None:
        params["facebook_branded_content"] = facebook_branded_content
    if format_transformation_spec is not None:
        params["format_transformation_spec"] = format_transformation_spec
    if image_crops is not None:
        params["image_crops"] = image_crops
    if image_file is not None:
        params["image_file"] = image_file
    if image_hash is not None:
        params["image_hash"] = image_hash
    if image_url is not None:
        params["image_url"] = image_url
    if instagram_branded_content is not None:
        params["instagram_branded_content"] = instagram_branded_content
    if instagram_permalink_url is not None:
        params["instagram_permalink_url"] = instagram_permalink_url
    if instagram_user_id is not None:
        params["instagram_user_id"] = instagram_user_id
    if interactive_components_spec is not None:
        params["interactive_components_spec"] = interactive_components_spec
    if is_dco_internal is not None:
        params["is_dco_internal"] = is_dco_internal
    if link_og_id is not None:
        params["link_og_id"] = link_og_id
    if link_url is not None:
        params["link_url"] = link_url
    if media_sourcing_spec is not None:
        params["media_sourcing_spec"] = media_sourcing_spec
    if name is not None:
        params["name"] = name
    if object_id is not None:
        params["object_id"] = object_id
    if object_story_id is not None:
        params["object_story_id"] = object_story_id
    if object_story_spec is not None:
        params["object_story_spec"] = object_story_spec
    if object_type is not None:
        params["object_type"] = object_type
    if object_url is not None:
        params["object_url"] = object_url
    if omnichannel_link_spec is not None:
        params["omnichannel_link_spec"] = omnichannel_link_spec
    if page_welcome_message is not None:
        params["page_welcome_message"] = page_welcome_message
    if place_page_set_id is not None:
        params["place_page_set_id"] = place_page_set_id
    if platform_customizations is not None:
        params["platform_customizations"] = platform_customizations
    if playable_asset_id is not None:
        params["playable_asset_id"] = playable_asset_id
    if portrait_customizations is not None:
        params["portrait_customizations"] = portrait_customizations
    if product_set_id is not None:
        params["product_set_id"] = product_set_id
    if recommender_settings is not None:
        params["recommender_settings"] = recommender_settings
    if regional_regulation_disclaimer_spec is not None:
        params["regional_regulation_disclaimer_spec"] = regional_regulation_disclaimer_spec
    if source_instagram_media_id is not None:
        params["source_instagram_media_id"] = source_instagram_media_id
    if template_url is not None:
        params["template_url"] = template_url
    if template_url_spec is not None:
        params["template_url_spec"] = template_url_spec
    if thumbnail_url is not None:
        params["thumbnail_url"] = thumbnail_url
    if title is not None:
        params["title"] = title
    if url_tags is not None:
        params["url_tags"] = url_tags
    if use_page_actor_override is not None:
        params["use_page_actor_override"] = use_page_actor_override
    result = await get_client().post(f"act_{account_id}/adcreatives", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adcreativesbylabels(
    ad_account_id: str,
    ad_label_ids: str,
    fields: Optional[str] = None,
    operator: Optional[str] = None,
) -> str:
    """GET /adcreativesbylabels on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        ad_label_ids: Required.
        operator: Optional. Values: ALL, ANY
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["ad_label_ids"] = ad_label_ids
    if operator is not None:
        params["operator"] = operator
    result = await get_client().get(f"{ad_account_id}/adcreativesbylabels", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_adimages(ad_account_id: str, hash_: str) -> str:
    """DELETE /adimages on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        hash_: Required.
    """
    params = {}
    params["hash"] = hash_
    result = await get_client().delete(f"{ad_account_id}/adimages")
    return json.dumps(result, indent=2)


async def get_ad_account_adimages(
    ad_account_id: str,
    fields: Optional[str] = None,
    biz_tag_id: Optional[int] = None,
    business_id: Optional[str] = None,
    hashes: Optional[str] = None,
    minheight: Optional[int] = None,
    minwidth: Optional[int] = None,
    name: Optional[str] = None,
    selected_hashes: Optional[str] = None,
) -> str:
    """GET /adimages on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        biz_tag_id: Optional.
        business_id: Optional.
        hashes: Optional.
        minheight: Optional.
        minwidth: Optional.
        name: Optional.
        selected_hashes: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if biz_tag_id is not None:
        params["biz_tag_id"] = biz_tag_id
    if business_id is not None:
        params["business_id"] = business_id
    if hashes is not None:
        params["hashes"] = hashes
    if minheight is not None:
        params["minheight"] = minheight
    if minwidth is not None:
        params["minwidth"] = minwidth
    if name is not None:
        params["name"] = name
    if selected_hashes is not None:
        params["selected_hashes"] = selected_hashes
    result = await get_client().get(f"{ad_account_id}/adimages", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adimages(account_id: str, bytes_: Optional[str] = None, copy_from: Optional[str] = None) -> str:
    """POST /adimages on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        bytes_: Optional.
        copy_from: Optional.
    """
    params = {}
    if bytes_ is not None:
        params["bytes"] = bytes_
    if copy_from is not None:
        params["copy_from"] = copy_from
    result = await get_client().post(f"act_{account_id}/adimages", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adplayables(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /adplayables on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/adplayables", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adplayables(
    account_id: str,
    name: str,
    app_id: Optional[str] = None,
    session_id: Optional[str] = None,
    source: Optional[str] = None,
    source_url: Optional[str] = None,
    source_zip: Optional[str] = None,
) -> str:
    """POST /adplayables on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        app_id: Optional.
        name: Required.
        session_id: Optional.
        source: Optional.
        source_url: Optional.
        source_zip: Optional.
    """
    params = {}
    if app_id is not None:
        params["app_id"] = app_id
    params["name"] = name
    if session_id is not None:
        params["session_id"] = session_id
    if source is not None:
        params["source"] = source
    if source_url is not None:
        params["source_url"] = source_url
    if source_zip is not None:
        params["source_zip"] = source_zip
    result = await get_client().post(f"act_{account_id}/adplayables", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adrules_history(
    ad_account_id: str,
    fields: Optional[str] = None,
    action: Optional[str] = None,
    evaluation_type: Optional[str] = None,
    hide_no_changes: Optional[bool] = None,
    object_id: Optional[str] = None,
) -> str:
    """GET /adrules_history on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        action: Optional. Values: BUDGET_NOT_REDISTRIBUTED, CHANGED_BID, CHANGED_BUDGET, CONSOLIDATE_ASC_FRAGMENTATION, CONSOLIDATE_FRAGMENTATION, CONVERT_ASC_CP_SINGLE_INSTANCE, EMAIL, ENABLE_ADVANTAGE_CAMPAIGN_BUDGET, ENABLE_ADVANTAGE_PLUS_AUDIENCE, ENABLE_ADVANTAGE_PLUS_CREATIVE, ENABLE_ADVANTAGE_PLUS_PLACEMENTS, ENABLE_AUTOFLOW, ENABLE_GEN_UNCROP, ENABLE_LANDING_PAGE_VIEWS, ENABLE_MUSIC, ENABLE_PRODUCT_SET_BOOSTING, ENABLE_REELS_PLACEMENTS, ENABLE_SEMANTIC_BASED_AUDIENCE_EXPANSION, ENABLE_SHOPS_ADS, ENDPOINT_PINGED, ERROR, FACEBOOK_NOTIFICATION_SENT, MESSAGE_SENT, NOT_CHANGED, PAUSED, UNPAUSED
        evaluation_type: Optional. Values: SCHEDULE, TRIGGER
        hide_no_changes: Optional.
        object_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if action is not None:
        params["action"] = action
    if evaluation_type is not None:
        params["evaluation_type"] = evaluation_type
    if hide_no_changes is not None:
        params["hide_no_changes"] = hide_no_changes
    if object_id is not None:
        params["object_id"] = object_id
    result = await get_client().get(f"{ad_account_id}/adrules_history", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adrules_library(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /adrules_library on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/adrules_library", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adrules_library(
    account_id: str,
    evaluation_spec: str,
    execution_spec: str,
    name: str,
    schedule_spec: Optional[str] = None,
    status: Optional[str] = None,
    ui_creation_source: Optional[str] = None,
) -> str:
    """POST /adrules_library on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        evaluation_spec: Required.
        execution_spec: Required.
        name: Required.
        schedule_spec: Optional.
        status: Optional. Values: DELETED, DISABLED, ENABLED, HAS_ISSUES
        ui_creation_source: Optional. Values: AM_ACCOUNT_OVERVIEW_RECOMMENDATIONS, AM_ACTIVITY_HISTORY_TABLE, AM_AD_OBJECT_NAME_CARD, AM_AMFE_L3_RECOMMENDATION, AM_AUTOFLOW_GUIDANCE_CARD, AM_AUTO_APPLY_WIDGET, AM_EDITOR_CARD, AM_INFO_CARD, AM_NAME_CELL_DROPDOWN, AM_OPTIMIZATION_TIP_GUIDANCE_CARD, AM_PERFORMANCE_SUMMARY, AM_RULE_LANDING_PAGE_BANNER, AM_SYD_RESOLUTION_FLOW, AM_SYD_RESOLUTION_FLOW_MODAL, AM_TABLE_DELIVERY_COLUMN_POPOVER, AM_TABLE_MORE_RULES_DROPDOWN, AM_TABLE_TOGGLE_POPOVER, AM_TOOLBAR_CREATE_RULE_DROPDOWN, PE_CAMPAIGN_STRUCTURE_MENU, PE_EDITOR_CARD, PE_INFO_CARD, PE_TOOLBAR_CREATE_RULE_DROPDOWN, RULES_MANAGEMENT_PAGE_ACTION_DROPDOWN, RULES_MANAGEMENT_PAGE_RULE_GROUP, RULES_MANAGEMENT_PAGE_RULE_NAME, RULES_MANAGEMENT_PAGE_TOP_NAV, RULES_VIEW_ACTIVE_RULES_DIALOG, RULE_CREATION_SUCCESS_DIALOG, RULE_SYD_REDIRECT, RULE_TEMPLATES_DIALOG
    """
    params = {}
    if account_id is not None:
        params["account_id"] = account_id
    params["evaluation_spec"] = evaluation_spec
    params["execution_spec"] = execution_spec
    params["name"] = name
    if schedule_spec is not None:
        params["schedule_spec"] = schedule_spec
    if status is not None:
        params["status"] = status
    if ui_creation_source is not None:
        params["ui_creation_source"] = ui_creation_source
    result = await get_client().post(f"act_{account_id}/adrules_library", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ads(
    ad_account_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    time_range: Optional[str] = None,
    updated_since: Optional[int] = None,
) -> str:
    """GET /ads on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
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
    result = await get_client().get(f"{ad_account_id}/ads", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_ads(
    account_id: str,
    creative: str,
    name: str,
    ad_schedule_end_time: Optional[str] = None,
    ad_schedule_start_time: Optional[str] = None,
    adlabels: Optional[str] = None,
    adset_id: Optional[int] = None,
    adset_spec: Optional[str] = None,
    audience_id: Optional[str] = None,
    bid_amount: Optional[int] = None,
    conversion_domain: Optional[str] = None,
    creative_asset_groups_spec: Optional[str] = None,
    date_format: Optional[str] = None,
    display_sequence: Optional[int] = None,
    draft_adgroup_id: Optional[str] = None,
    engagement_audience: Optional[bool] = None,
    execution_options: Optional[str] = None,
    include_demolink_hashes: Optional[bool] = None,
    priority: Optional[int] = None,
    source_ad_id: Optional[str] = None,
    status: Optional[str] = None,
    tracking_specs: Optional[str] = None,
) -> str:
    """POST /ads on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        ad_schedule_end_time: Optional.
        ad_schedule_start_time: Optional.
        adlabels: Optional.
        adset_id: Optional.
        adset_spec: Optional.
        audience_id: Optional.
        bid_amount: Optional.
        conversion_domain: Optional.
        creative: Required.
        creative_asset_groups_spec: Optional.
        date_format: Optional.
        display_sequence: Optional.
        draft_adgroup_id: Optional.
        engagement_audience: Optional.
        execution_options: Optional. Values: include_recommendations, synchronous_ad_review, validate_only
        include_demolink_hashes: Optional.
        name: Required.
        priority: Optional.
        source_ad_id: Optional.
        status: Optional. Values: ACTIVE, ARCHIVED, DELETED, PAUSED
        tracking_specs: Optional.
    """
    params = {}
    if ad_schedule_end_time is not None:
        params["ad_schedule_end_time"] = ad_schedule_end_time
    if ad_schedule_start_time is not None:
        params["ad_schedule_start_time"] = ad_schedule_start_time
    if adlabels is not None:
        params["adlabels"] = adlabels
    if adset_id is not None:
        params["adset_id"] = adset_id
    if adset_spec is not None:
        params["adset_spec"] = adset_spec
    if audience_id is not None:
        params["audience_id"] = audience_id
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    if conversion_domain is not None:
        params["conversion_domain"] = conversion_domain
    params["creative"] = creative
    if creative_asset_groups_spec is not None:
        params["creative_asset_groups_spec"] = creative_asset_groups_spec
    if date_format is not None:
        params["date_format"] = date_format
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
    params["name"] = name
    if priority is not None:
        params["priority"] = priority
    if source_ad_id is not None:
        params["source_ad_id"] = source_ad_id
    if status is not None:
        params["status"] = status
    if tracking_specs is not None:
        params["tracking_specs"] = tracking_specs
    result = await get_client().post(f"act_{account_id}/ads", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ads_reporting_mmm_reports(
    ad_account_id: str,
    fields: Optional[str] = None,
    filtering: Optional[str] = None,
) -> str:
    """GET /ads_reporting_mmm_reports on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        filtering: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if filtering is not None:
        params["filtering"] = filtering
    result = await get_client().get(f"{ad_account_id}/ads_reporting_mmm_reports", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ads_reporting_mmm_schedulers(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /ads_reporting_mmm_schedulers on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/ads_reporting_mmm_schedulers", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ads_volume(
    ad_account_id: str,
    fields: Optional[str] = None,
    page_id: Optional[str] = None,
    recommendation_type: Optional[str] = None,
    show_breakdown_by_actor: Optional[bool] = None,
) -> str:
    """GET /ads_volume on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        page_id: Optional.
        recommendation_type: Optional. Values: AAC_CREATION_PACKAGE, AB_TEST, ACCOUNT_ERROR, ACCOUNT_NEEDS_CREDIT, ACCOUNT_SPEND_LIMIT, ACCOUNT_SPEND_LIMIT_DUPLICATION, ACO_TOGGLE, ADSET_BUDGET_SHARING, ADS_REPORTING, ADS_STATUS, ADVANCED_CAMPAIGN_BUDGET, ADVANTAGE_APP_CAMPAIGN, ADVANTAGE_CAMPAIGN_BUDGET_DUPLICATION, ADVANTAGE_CUSTOM_AUDIENCE, ADVANTAGE_CUSTOM_AUDIENCE_DUPLICATION, ADVANTAGE_CUSTOM_AUDIENCE_UPSELL, ADVANTAGE_DETAILED_TARGETING, ADVANTAGE_LOOKALIKE_AUDIENCE, ADVANTAGE_LOOKALIKE_DUPLICATION, ADVANTAGE_PLUS_APP_CAMPAIGN, ADVANTAGE_PLUS_APP_CAMPAIGN_PRECREATE, ADVANTAGE_PLUS_AUDIENCE, ADVANTAGE_PLUS_AUDIENCE_DUPLICATION, ADVANTAGE_PLUS_AUDIENCE_FRICTION, ADVANTAGE_PLUS_AUDIENCE_TOGGLE, ADVANTAGE_PLUS_AUDIENCE_V2, ADVANTAGE_PLUS_CAMPAIGN_BUDGET, ADVANTAGE_PLUS_CATALOG_ADS, ADVANTAGE_PLUS_CATALOG_ADS_V2, ADVANTAGE_PLUS_CREATIVE, ADVANTAGE_PLUS_CREATIVE_CATALOG, ADVANTAGE_PLUS_CREATIVE_SE, ADVANTAGE_PLUS_LEAD_CAMPAIGN, ADVANTAGE_PLUS_PLACEMENTS_DUPLICATION, ADVANTAGE_PLUS_PLACEMENTS_FRICTION, ADVANTAGE_PLUS_PLACEMENTS_V2_DUPLICATION, ADVANTAGE_SHOPPING_CAMPAIGN, ADVANTAGE_SHOPPING_CAMPAIGN_FRAGMENTATION, AD_ACCOUNT_PLACEMENT_CONTROLS_UPSELL, AD_LIFT_RECALL_GOAL, AD_LIFT_RECALL_GOAL_PRECREATE, AD_LIFT_RECALL_OPTIMIZATION_GOAL, AD_OBJECTIVE, AD_SET_BUDGET_SHARING_GUIDANCE, AEM_V2_INELIGIBLE, AGGREGATED_BID_LIMITED, AGGREGATED_BUDGET_LIMITED, AGGREGATED_COST_LIMITED, AI_GENERATED_ICEBREAKERS, AMA_UPSELL, APLUSC_ADD_OVERLAYS, APLUSC_BIZ_AI_AGENT, APLUSC_DYNAMIC_DESCRIPTION, APLUSC_FLEXIBLE_MEDIA, APLUSC_IMAGE_BACKGROUND_GENERATION, APLUSC_MUSIC, APLUSC_RELEVANT_COMMENTS, APLUSC_STANDARD_ENHANCEMENTS_BUNDLE, APLUSC_TEXT_IMPROVEMENTS, APLUSC_VIDEO_EXPANSION, APLUSC_VISUAL_TOUCHUPS, APLUS_C_CATALOG_DUPLICATION, APP_AEM_V2_INSTALLATION_PROMOTION, APP_ENGAGED_VIEW_CONVERSIONS_DUPLICATION, ASC_AUTOMATION, ASC_BUDGET_OPTIMIZATION, ASC_CREATION_PACKAGE, ASC_FRAGMENTATION_V2, ASC_PRECREATE, ASPECT_RATIO, ATLEAST_6_PLACEMENTS, AUCTION_OVERLAP, AUCTION_OVERLAP_CONSOLIDATION, AUDIENCE_EXPANSION, AUDIENCE_EXPANSION_GEORADIUS, AUDIENCE_EXPANSION_LOOKALIKE, AUDIENCE_EXPANSION_RETARGETING, AUDIENCE_LEARNING_LIMITED, AUTOBID_TO_MANUAL_BID, AUTOFLOW_OPT_IN, AUTOFLOW_OPT_IN_FALLBACK_DUPLICATION_FLOW, AUTOFLOW_OPT_IN_V2, AUTOMATIC_PLACEMENTS, AUTOMATIC_PLACEMENTS_V2, AUTOMATIC_PLACEMENTS_V3, AUTOMATIC_PLACEMENTS_V4, AUTO_BID, AUTO_CAT_SELECTION_ENHANCEMENT, B2P_MESSAGING_UPSELL, BACKGROUND_GENERATION, BID_LIMITED_SENSITIVE, BID_LIMITED_STARVING, BLENDED_ADS, BLENDED_ADS_DUPLICATION, BLENDED_ADS_FOR_SHOPS_ADS_DUPLICATION, BPBAA_WITH_CAPI_UPSELL, BROADGEO_AM_UPSELL_GUIDANCE, BROAD_TARGETING, BUDGET_AMORTIZATION, BUDGET_LIMITED, BUDGET_REALLOCATION, BUDGET_SEASONAL_GUIDANCE, BUSINESS_AI_AGENT_UPSELL, CALL_ADS_DAYPARTING_L3_RECOMMENDATION, CAMPAIGN_CONSOLIDATION_WITH_FLEX, CAMPAIGN_GUIDANCE_NAVIGATOR_REELS_TIPS, CAMPAIGN_SPEND_LIMIT, CAPI, CAPI_CRM_FUNNEL, CAPI_CRM_GUIDANCE, CAPI_CRM_GUIDANCE_V2, CAPI_CRM_SETUP, CAPI_EVENT_COVERAGE, CAPI_PENETRATION, CAPI_PERFORMANCE_MATCH_KEY, CAPI_PERFORMANCE_MATCH_KEY_V2, CASH_REWARDS_OPT_IN, CATALOG_DYNAMIC_MEDIA, CATALOG_MATCH_RATE, COMMERCE_SHOPS_ADS_DUPLICATION, CONNECTED_SOURCES, CONNECTED_SOURCES_DUPLICATION, CONNECT_FACEBOOK_PAGE_TO_INSTAGRAM, CONNECT_FACEBOOK_PAGE_TO_WHATSAPP, CONVERSION_LEADS_OPTIMIZATION, CONVERSION_LEADS_OPTIMIZATION_DUPLICATION, CONVERSION_LEADS_OPTIMIZATION_INTEGRATED, CONVERSION_LEADS_OPTIMIZATION_V2, CONVERSION_LEAD_ADS, COST_GOAL, COST_GOAL_BUDGET_LIMITED, COST_GOAL_CPA_LIMITED, COST_PER_RESULT, CREATION_PACKAGE_UPGRADE_TO_ASC, CREATION_PACKAGE_UPGRADE_TO_CTX, CREATION_PACKAGE_UPGRADE_TO_TLA, CREATION_PACKAGE_UPGRADE_TO_TMC, CREATIVE_BADGE, CREATIVE_DIVERSITY, CREATIVE_FATIGUE, CREATIVE_FATIGUE_DUPLICATION, CREATIVE_FATIGUE_HOURLY, CREATIVE_LIMITED, CREATIVE_LIMITED_DUPLICATION, CREATIVE_LIMITED_HOURLY, CREATOR_ADS_PA_CONVERSION, CTA, CTD_LEADS_OPTIMIZATION, CTD_PURCHASE_OPTIMIZATION, CTM_AD_OBJECTIVE_GROWTH, CTM_LEADS_OPTIMIZATION_UPSELL, CTM_LO_ODAX_PHASE_2, CTM_PO_ODAX_PHASE_2, CTM_VO_ODAX_PHASE_2, CTX_BUDGET_OPTIMIZATION, CTX_CREATION_PACKAGE, CTX_CREATION_PACKAGE_V2, CTX_CREATIVE_LOW_OUTCOME_WARNING, CTX_CTA_UPGRADE_IN_DUPLICATION, CTX_CTMPO_UPGRADE, CTX_CTWALO_UPGRADE, CTX_CTWAPO_UPGRADE, CTX_GUIDANCE, CTX_HVS, CTX_HVS_V2, CTX_MULTI_MESSAGE_DESTINATION, CTX_PRECREATE, CTX_PRODUCT_EXTENSION_DUPLICATION, CTX_SABR_CBO, CTX_SABR_NON_CBO, CTX_SMART_DEFAULTING, CTX_VALUE_OPTIMIZATION_CTM_PO_TO_VO, CTX_ZO_CBO, CTX_ZO_NON_CBO, CUSTOM_AUDIENCE_RELAXATION, DA_ADVANTAGE_PLUS_CREATIVE_INFO_LABELS, DA_DUPLICATION_PRODUCT_TAGS, DEAD_LINK, DEFRAGMENTATION_ACB, DEFRAGMENTATION_ACB_DUPLICATION, DEFRAGMENTATION_USING_VALUE_RULES_TEST_V2, DELIVERY_DEPENDENT_CREATIVE_LIMITED, DELIVERY_ERROR, DELIVERY_ERROR_V2, DELIVERY_WARNING, DYNAMIC_ADVANTAGE_CAMPAIGN_BUDGET, ECOSYSTEM_BID_REDUCE_L1_CARDINALITY, EMAIL_CAPTURE_UPSELL_GUIDANCE, ENABLE_WHATS_APP_ADS_DATA_SHARING, ENGAGED_VIEW_CONVERSIONS_CREATION, EVC_APP_DUPLICATION_UPGRADE, EVC_WEB_DUPLICATION_UPGRADE, F2_CONVERSION_LOCATION, FRAGMENTATION, FRAGMENTATION_RESOLUTION_UPDATE, FRAGMENTATION_V2, FRAGMENTATION_V3, FRAGMENTATION_V4, GENERATIVE_UNCROP_DUPLICATION, GEN_AI_MVP, GES_TEST, GUIDANCE_CENTER_CODE_GEN, HEURISTIC_DEFAULT_DURATION, HIGH_COST, HISTORICAL_BENCHMARK, IAA_ROAS_OPTIMIZATION, IG_MULTI_ADS, IG_SURFACES_MANUAL_PLACEMENTS, INCREMENTAL_ATTRIBUTION, INSTANT_FORMS_LEADS, IN_APP_AD_IMPRESSION_ROAS_ANDROID, LANDING_PAGE_VIEW, LANDING_PAGE_VIEW_OPTIMIZATION_GOAL, LANDING_PAGE_VIEW_OPTIMIZATION_GOAL_V2, LANDING_PAGE_VIEW_PRECREATE, LEAD_ADS_DFCA_LOOKALIKE_ADOPTION, LEAD_ADS_GUIDANCE, LEARNING_LIMITED, LEARNING_PAUSE_FRICTION, LEARNING_PHASE_BUDGET_EDITS, LIVE_VIDEO_ADS, LOW_BUDGET_UTILIZATION, LOW_OUTCOME, MARKETING_MESSAGES, MERLIN_GUIDANCE, MESSAGING_EVENTS, MESSAGING_EVENTS_PRECREATE, MESSAGING_PARTNERS, MESSAGING_PARTNERS_PRECREATE, MESSAGING_PARTNERS_V2, META_VERIFIED_ADS_PERFORMANCE_GUIDANCE, MISSING_OR_INVALID_PARAMETERS, MIXED_FORMATS, MIXED_FORMATS_V2, MIXED_FORMATS_V3, MIXED_PA_COMBINE_ADSETS, MMT_CAROUSEL_TO_VIDEO, MOBILE_FIRST_CREATIVE, MOBILE_FIRST_VIDEO, MR_AEMV2SUB_KCONSOLIDATION, MULTI_ADVERTISER_ADS, MULTI_TEXT, MUSIC, MUSIC_V2, NARROW_WEBSITE_CUSTOM_AUDIENCE, NOT_APPLICABLE, NO_DELIVERY_STATUS, OFFSITE_CONVERSION, OFFSITE_CONVERSION_AR, OFFSITE_CONVERSION_BASED_ON_SIGNALS, OFFSITE_CONVERSION_LEADS_OPTIMIZATION, OFFSITE_CONVERSION_V2, OMNI_OPTIMIZATION, OPTIMAL_BAU, OUTCOME_FORECASTER_BUDGET_RECOMMENDATION, OUTCOME_FORECASTER_SHADOW_LOGGING, PARTNERSHIP_ADS, PARTNERSHIP_ADS_DYNAMIC_HEADER, PAYMENT_METHOD, PERFORMANT_CREATIVE_REELS_OPT_IN, PERFORMANT_CREATIVE_REELS_OPT_IN_V2, PFR_L1_INLINE_MMT, PIXELLESS_LPV_OPTIMIZATION_GOAL, PIXEL_OPTIMIZATION_AAM, PIXEL_OPTIMIZATION_AAM_PRECREATE, PIXEL_OPTIMIZATION_HIE, PIXEL_OPTIMIZATION_HIE_PRECREATE, PIXEL_OPTIMIZATION_HIE_V2, PIXEL_SETUP, PIXEL_SETUP_PRECREATE, PIXEL_UPSELL, PIXEL_UPSELL_V2, PLACEMENTS_LIQUIDITY_AUTOMATIC_GUIDANCE, PREDICTIVE_CREATIVE_LIMITED, PREDICTIVE_CREATIVE_LIMITED_HOURLY, PREPARING_STATUS, PRODUCT_EXTENSIONS_GUIDANCE, PRODUCT_SET_BOOSTING, PROMO_ADS_UPSELL_GUIDANCE, PURCHASE_OPTIMIZATION, RAPID_LEARNING_LIMITED, RAPID_LEARNING_PHASE, REACH_OPTIMIZATION_GOAL, REACH_OPTIMIZATION_GOAL_PRECREATE, REELS_DUPLICATION_UPSELL, REELS_MUSIC_DUPLICATION, REELS_PC_AND_MOBILE_FIRST_CREATIVE, REELS_PC_RECOMMENDATION, REELS_PC_RECOMMENDATION_V2, REELS_PERFORMANT_CREATIVE, REELS_PLACEMENT, REVERT, REVIEW_CREATIVE_DUPLICATED_REJECTED_ADS, SABR_DEFAULT_DURATION, SALES_CONVERSION, SAVED_AUDIENCE, SCALE_GOOD_CAMPAIGN, SCALE_GOOD_CAMPAIGN_DUPLICATION, SCALE_GOOD_CAMPAIGN_SMB, SCALE_GOOD_CAMPAIGN_V2, SCALE_GOOD_CAMPAIGN_V2_DUPLICATION, SCALE_GOOD_CTX_CAMPAIGN, SCALE_GOOD_CTX_CAMPAIGNS_DUPLICATION, SEASONAL_CAMPAIGNS, SEMANTIC_BASED_AUDIENCE_DUPLICATION, SEMANTIC_BASED_AUDIENCE_EXPANSION, SETUP_PIXEL, SHOPS_ADS, SHOPS_ADS_DUPLICATION, SHOPS_ADS_SAOFF, SHOPS_ADS_TRAFFIC_CAP_SETTINGS, SHOP_ADS_V2, SIGNALS_DOWN_FUNNEL_EVENT_OPTIMIZATION, SIGNALS_GROWTH_CAPI, SIGNALS_GROWTH_CAPI_PRECREATE, SIGNALS_GROWTH_CAPI_TABLE, SIGNALS_GROWTH_CAPI_V2, SIGNALS_VO_USING_CO_MODEL, SIMILAR_ADVERTISER_BUDGET_RECOMMENDATION, SITE_EXTENSIONS_DUPLICATION, SITE_EXTENSIONS_GUIDANCE, SIX_PLUS_MANUAL_PLACEMENTS, SIX_PLUS_PLACEMENTS_DUPLICATION, SPEND_LIMIT, SYD_TEST_MODE, TAILORED_LEAD_AD_CAMPAIGN, TAILORED_MESSAGES_CAMPAIGN, TARGETING_CREATIVE_FRAGMENTATION, THREECO_WEB_PLUS_APP_UPSELL, TLA_CREATION_PACKAGE, TOP_ADSETS_WITH_ADS_UNDER_CAP, TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP, TWO_P_GUIDANCE_CARD_AAA, TWO_P_GUIDANCE_CARD_AUTO_PLACEMENT, TWO_P_GUIDANCE_CARD_CBO_OFF, TWO_P_GUIDANCE_CARD_CTM_PREFLIGHT, UNCROP_IMAGE, UNECONOMICAL_ADS_THROTTLING, UNIFIED_INBOX, UNUSED_BUDGET, UPPER_FUNNEL_TO_LEAD_INSTANT_FORM, VALUE_CO_CAMPAIGNS_LOW_PURCHASE_DQ, VALUE_DIAGNOSTICS_GUIDANCE, VALUE_OPTIMIZATION_GOAL, VALUE_RULES_GUIDANCE, VIDEO_LENGTH, VIDEO_VIEWS_UPSELL, VIDEO_VIEWS_UPSELL_PRECREATE, VO_IN_APP_PURCHASE, VO_VT_1D_DEFAULTING, WA_MESSAGING_PARTNERS, WA_MESSAGING_PARTNERS_PRECREATE, WA_MESSAGING_PARTNERS_V2, WEBSITE_AND_CALLS_UPSELL, WEBSITE_AND_INSTANT_FORM_L2, WEB_ENGAGED_VIEW_CONVERSIONS, WTWA_UPSELL_IN_DUPLICATION, WTWA_UPSELL_IN_SYD_AND_AM_TABLE, YI_TEST, ZERO_CONVERSION, ZERO_IMPRESSION, ZERO_OUTCOME_BUDGET
        show_breakdown_by_actor: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if page_id is not None:
        params["page_id"] = page_id
    if recommendation_type is not None:
        params["recommendation_type"] = recommendation_type
    if show_breakdown_by_actor is not None:
        params["show_breakdown_by_actor"] = show_breakdown_by_actor
    result = await get_client().get(f"{ad_account_id}/ads_volume", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adsbylabels(
    ad_account_id: str,
    ad_label_ids: str,
    fields: Optional[str] = None,
    operator: Optional[str] = None,
) -> str:
    """GET /adsbylabels on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        ad_label_ids: Required.
        operator: Optional. Values: ALL, ANY
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["ad_label_ids"] = ad_label_ids
    if operator is not None:
        params["operator"] = operator
    result = await get_client().get(f"{ad_account_id}/adsbylabels", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adsets(
    ad_account_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    is_completed: Optional[bool] = None,
    time_range: Optional[str] = None,
    updated_since: Optional[int] = None,
) -> str:
    """GET /adsets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        date_preset: Optional. Values: DATA_MAXIMUM, LAST_14D, LAST_28D, LAST_30D, LAST_3D, LAST_7D, LAST_90D, LAST_MONTH, LAST_QUARTER, LAST_WEEK_MON_SUN, LAST_WEEK_SUN_SAT, LAST_YEAR, MAXIMUM, THIS_MONTH, THIS_QUARTER, THIS_WEEK_MON_TODAY, THIS_WEEK_SUN_TODAY, THIS_YEAR, TODAY, YESTERDAY
        effective_status: Optional. Values: ACTIVE, ADSET_PAUSED, ARCHIVED, CAMPAIGN_PAUSED, DELETED, DISAPPROVED, IN_PROCESS, PAUSED, PENDING_BILLING_INFO, PENDING_REVIEW, PREAPPROVED, WITH_ISSUES
        is_completed: Optional.
        time_range: Optional.
        updated_since: Optional.
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
    if updated_since is not None:
        params["updated_since"] = updated_since
    result = await get_client().get(f"{ad_account_id}/adsets", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adsets(
    account_id: str,
    name: str,
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
    budget_source: Optional[str] = None,
    budget_split_set_id: Optional[str] = None,
    campaign_attribution: Optional[str] = None,
    campaign_id: Optional[str] = None,
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
    frequency_control_specs: Optional[str] = None,
    full_funnel_exploration_mode: Optional[str] = None,
    is_ba_skip_delayed_eligible: Optional[bool] = None,
    is_budget_schedule_enabled: Optional[bool] = None,
    is_dynamic_creative: Optional[bool] = None,
    is_incremental_attribution_enabled: Optional[bool] = None,
    is_sac_cfca_terms_certified: Optional[bool] = None,
    lifetime_budget: Optional[int] = None,
    lifetime_imps: Optional[int] = None,
    lifetime_min_spend_target: Optional[int] = None,
    lifetime_spend_cap: Optional[int] = None,
    line_number: Optional[int] = None,
    max_budget_spend_percentage: Optional[int] = None,
    min_budget_spend_percentage: Optional[int] = None,
    multi_optimization_goal_weight: Optional[str] = None,
    optimization_goal: Optional[str] = None,
    optimization_sub_event: Optional[str] = None,
    pacing_type: Optional[str] = None,
    placement_soft_opt_out: Optional[str] = None,
    promoted_object: Optional[str] = None,
    rb_prediction_id: Optional[str] = None,
    regional_regulated_categories: Optional[str] = None,
    regional_regulation_identities: Optional[str] = None,
    rf_prediction_id: Optional[str] = None,
    source_adset_id: Optional[str] = None,
    start_time: Optional[str] = None,
    status: Optional[str] = None,
    targeting: Optional[str] = None,
    time_based_ad_rotation_id_blocks: Optional[str] = None,
    time_based_ad_rotation_intervals: Optional[str] = None,
    time_start: Optional[str] = None,
    time_stop: Optional[str] = None,
    topline_id: Optional[str] = None,
    trending_topics_spec: Optional[str] = None,
    tune_for_category: Optional[str] = None,
    value_rule_set_id: Optional[str] = None,
    value_rules_applied: Optional[bool] = None,
) -> str:
    """POST /adsets on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        adlabels: Optional.
        adset_schedule: Optional.
        attribution_spec: Optional.
        automatic_manual_state: Optional. Values: AUTOMATIC, MANUAL, UNSET
        bid_adjustments: Optional.
        bid_amount: Optional.
        bid_constraints: Optional.
        bid_strategy: Optional. Values: COST_CAP, LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, LOWEST_COST_WITH_MIN_ROAS
        billing_event: Optional. Values: APP_INSTALLS, CLICKS, IMPRESSIONS, LINK_CLICKS, LISTING_INTERACTION, NONE, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PURCHASE, THRUPLAY
        budget_schedule_specs: Optional.
        budget_source: Optional. Values: NONE, RMN
        budget_split_set_id: Optional.
        campaign_attribution: Optional.
        campaign_id: Optional.
        campaign_spec: Optional.
        creative_sequence: Optional.
        creative_sequence_repetition_pattern: Optional. Values: FULL_SEQUENCE, LAST_AD
        daily_budget: Optional.
        daily_imps: Optional.
        daily_min_spend_target: Optional.
        daily_spend_cap: Optional.
        date_format: Optional.
        destination_type: Optional. Values: APP, APPLINKS_AUTOMATIC, FACEBOOK, FACEBOOK_LIVE, FACEBOOK_PAGE, IMAGINE, INSTAGRAM_DIRECT, INSTAGRAM_LIVE, INSTAGRAM_PROFILE, INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE, MESSAGING_INSTAGRAM_DIRECT_MESSENGER, MESSAGING_INSTAGRAM_DIRECT_MESSENGER_WHATSAPP, MESSAGING_INSTAGRAM_DIRECT_WHATSAPP, MESSAGING_MESSENGER_WHATSAPP, MESSENGER, ON_AD, ON_EVENT, ON_PAGE, ON_POST, ON_VIDEO, SHOP_AUTOMATIC, WEBSITE, WHATSAPP
        dsa_beneficiary: Optional.
        dsa_payor: Optional.
        end_time: Optional.
        execution_options: Optional. Values: include_recommendations, validate_only
        existing_customer_budget_percentage: Optional.
        frequency_control_specs: Optional.
        full_funnel_exploration_mode: Optional. Values: EXTENDED_EXPLORATION, LIMITED_EXPLORATION, NONE_EXPLORATION
        is_ba_skip_delayed_eligible: Optional.
        is_budget_schedule_enabled: Optional.
        is_dynamic_creative: Optional.
        is_incremental_attribution_enabled: Optional.
        is_sac_cfca_terms_certified: Optional.
        lifetime_budget: Optional.
        lifetime_imps: Optional.
        lifetime_min_spend_target: Optional.
        lifetime_spend_cap: Optional.
        line_number: Optional.
        max_budget_spend_percentage: Optional.
        min_budget_spend_percentage: Optional.
        multi_optimization_goal_weight: Optional. Values: BALANCED, PREFER_EVENT, PREFER_INSTALL, UNDEFINED
        name: Required.
        optimization_goal: Optional. Values: ADVERTISER_SILOED_VALUE, AD_RECALL_LIFT, APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, AUTOMATIC_OBJECTIVE, CONVERSATIONS, DERIVED_EVENTS, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, IN_APP_VALUE, LANDING_PAGE_VIEWS, LEAD_GENERATION, LINK_CLICKS, MEANINGFUL_CALL_ATTEMPT, MESSAGING_APPOINTMENT_CONVERSION, MESSAGING_PURCHASE_CONVERSION, NONE, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, PROFILE_AND_PAGE_ENGAGEMENT, PROFILE_VISIT, QUALITY_CALL, QUALITY_LEAD, REACH, REMINDERS_SET, SUBSCRIBERS, THRUPLAY, VALUE, VISIT_INSTAGRAM_PROFILE
        optimization_sub_event: Optional. Values: NONE, POST_INTERACTION, TRAVEL_INTENT, TRAVEL_INTENT_BUCKET_01, TRAVEL_INTENT_BUCKET_02, TRAVEL_INTENT_BUCKET_03, TRAVEL_INTENT_BUCKET_04, TRAVEL_INTENT_BUCKET_05, TRAVEL_INTENT_NO_DESTINATION_INTENT, TRIP_CONSIDERATION, VIDEO_SOUND_ON
        pacing_type: Optional.
        placement_soft_opt_out: Optional.
        promoted_object: Optional.
        rb_prediction_id: Optional.
        regional_regulated_categories: Optional. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
        regional_regulation_identities: Optional.
        rf_prediction_id: Optional.
        source_adset_id: Optional.
        start_time: Optional.
        status: Optional. Values: ACTIVE, ARCHIVED, DELETED, PAUSED
        targeting: Optional.
        time_based_ad_rotation_id_blocks: Optional.
        time_based_ad_rotation_intervals: Optional.
        time_start: Optional.
        time_stop: Optional.
        topline_id: Optional.
        trending_topics_spec: Optional.
        tune_for_category: Optional. Values: CREDIT, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, HOUSING, ISSUES_ELECTIONS_POLITICS, NONE, ONLINE_GAMBLING_AND_GAMING
        value_rule_set_id: Optional.
        value_rules_applied: Optional.
    """
    params = {}
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
    if budget_source is not None:
        params["budget_source"] = budget_source
    if budget_split_set_id is not None:
        params["budget_split_set_id"] = budget_split_set_id
    if campaign_attribution is not None:
        params["campaign_attribution"] = campaign_attribution
    if campaign_id is not None:
        params["campaign_id"] = campaign_id
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
    if frequency_control_specs is not None:
        params["frequency_control_specs"] = frequency_control_specs
    if full_funnel_exploration_mode is not None:
        params["full_funnel_exploration_mode"] = full_funnel_exploration_mode
    if is_ba_skip_delayed_eligible is not None:
        params["is_ba_skip_delayed_eligible"] = is_ba_skip_delayed_eligible
    if is_budget_schedule_enabled is not None:
        params["is_budget_schedule_enabled"] = is_budget_schedule_enabled
    if is_dynamic_creative is not None:
        params["is_dynamic_creative"] = is_dynamic_creative
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
    if line_number is not None:
        params["line_number"] = line_number
    if max_budget_spend_percentage is not None:
        params["max_budget_spend_percentage"] = max_budget_spend_percentage
    if min_budget_spend_percentage is not None:
        params["min_budget_spend_percentage"] = min_budget_spend_percentage
    if multi_optimization_goal_weight is not None:
        params["multi_optimization_goal_weight"] = multi_optimization_goal_weight
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
    if source_adset_id is not None:
        params["source_adset_id"] = source_adset_id
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
    if topline_id is not None:
        params["topline_id"] = topline_id
    if trending_topics_spec is not None:
        params["trending_topics_spec"] = trending_topics_spec
    if tune_for_category is not None:
        params["tune_for_category"] = tune_for_category
    if value_rule_set_id is not None:
        params["value_rule_set_id"] = value_rule_set_id
    if value_rules_applied is not None:
        params["value_rules_applied"] = value_rules_applied
    result = await get_client().post(f"act_{account_id}/adsets", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adsetsbylabels(
    ad_account_id: str,
    ad_label_ids: str,
    fields: Optional[str] = None,
    operator: Optional[str] = None,
) -> str:
    """GET /adsetsbylabels on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        ad_label_ids: Required.
        operator: Optional. Values: ALL, ANY
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["ad_label_ids"] = ad_label_ids
    if operator is not None:
        params["operator"] = operator
    result = await get_client().get(f"{ad_account_id}/adsetsbylabels", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_adspixels(ad_account_id: str, fields: Optional[str] = None, sort_by: Optional[str] = None) -> str:
    """GET /adspixels on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        sort_by: Optional. Values: LAST_FIRED_TIME, NAME
    """
    params = {}
    params["fields"] = fields or "id,name"
    if sort_by is not None:
        params["sort_by"] = sort_by
    result = await get_client().get(f"{ad_account_id}/adspixels", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_adspixels(account_id: str, name: Optional[str] = None) -> str:
    """POST /adspixels on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        name: Optional.
    """
    params = {}
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"act_{account_id}/adspixels", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_advertisable_applications(
    ad_account_id: str,
    fields: Optional[str] = None,
    app_id: Optional[str] = None,
    business_id: Optional[str] = None,
) -> str:
    """GET /advertisable_applications on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        app_id: Optional.
        business_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app_id is not None:
        params["app_id"] = app_id
    if business_id is not None:
        params["business_id"] = business_id
    result = await get_client().get(f"{ad_account_id}/advertisable_applications", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_advideos(ad_account_id: str, video_id: str) -> str:
    """DELETE /advideos on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        video_id: Required.
    """
    params = {}
    params["video_id"] = video_id
    result = await get_client().delete(f"{ad_account_id}/advideos")
    return json.dumps(result, indent=2)


async def get_ad_account_advideos(
    ad_account_id: str,
    fields: Optional[str] = None,
    max_aspect_ratio: Optional[float] = None,
    maxheight: Optional[int] = None,
    maxlength: Optional[int] = None,
    maxwidth: Optional[int] = None,
    min_aspect_ratio: Optional[float] = None,
    minheight: Optional[int] = None,
    minlength: Optional[int] = None,
    minwidth: Optional[int] = None,
    title: Optional[str] = None,
) -> str:
    """GET /advideos on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        max_aspect_ratio: Optional.
        maxheight: Optional.
        maxlength: Optional.
        maxwidth: Optional.
        min_aspect_ratio: Optional.
        minheight: Optional.
        minlength: Optional.
        minwidth: Optional.
        title: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if max_aspect_ratio is not None:
        params["max_aspect_ratio"] = max_aspect_ratio
    if maxheight is not None:
        params["maxheight"] = maxheight
    if maxlength is not None:
        params["maxlength"] = maxlength
    if maxwidth is not None:
        params["maxwidth"] = maxwidth
    if min_aspect_ratio is not None:
        params["min_aspect_ratio"] = min_aspect_ratio
    if minheight is not None:
        params["minheight"] = minheight
    if minlength is not None:
        params["minlength"] = minlength
    if minwidth is not None:
        params["minwidth"] = minwidth
    if title is not None:
        params["title"] = title
    result = await get_client().get(f"{ad_account_id}/advideos", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_advideos(
    account_id: str,
    application_id: Optional[str] = None,
    asked_fun_fact_prompt_id: Optional[int] = None,
    audio_story_wave_animation_handle: Optional[str] = None,
    chunk_session_id: Optional[str] = None,
    composer_entry_picker: Optional[str] = None,
    composer_entry_point: Optional[str] = None,
    composer_entry_time: Optional[int] = None,
    composer_session_events_log: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    composer_source_surface: Optional[str] = None,
    composer_type: Optional[str] = None,
    container_type: Optional[str] = None,
    content_category: Optional[str] = None,
    creative_tools: Optional[str] = None,
    description: Optional[str] = None,
    embeddable: Optional[bool] = None,
    end_offset: Optional[int] = None,
    fbuploader_video_file_chunk: Optional[str] = None,
    file_size: Optional[int] = None,
    file_url: Optional[str] = None,
    fisheye_video_cropped: Optional[bool] = None,
    formatting: Optional[str] = None,
    fov: Optional[int] = None,
    front_z_rotation: Optional[float] = None,
    fun_fact_prompt_id: Optional[str] = None,
    fun_fact_toastee_id: Optional[int] = None,
    guide: Optional[str] = None,
    guide_enabled: Optional[bool] = None,
    initial_heading: Optional[int] = None,
    initial_pitch: Optional[int] = None,
    instant_game_entry_point_data: Optional[str] = None,
    is_boost_intended: Optional[bool] = None,
    is_group_linking_post: Optional[bool] = None,
    is_partnership_ad: Optional[bool] = None,
    is_voice_clip: Optional[bool] = None,
    location_source_id: Optional[str] = None,
    name: Optional[str] = None,
    og_action_type_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_suggestion_mechanism: Optional[str] = None,
    original_fov: Optional[int] = None,
    original_projection_type: Optional[str] = None,
    partnership_ad_ad_code: Optional[str] = None,
    publish_event_id: Optional[int] = None,
    referenced_sticker_id: Optional[str] = None,
    replace_video_id: Optional[str] = None,
    slideshow_spec: Optional[str] = None,
    source: Optional[str] = None,
    source_instagram_media_id: Optional[str] = None,
    spherical: Optional[bool] = None,
    start_offset: Optional[int] = None,
    swap_mode: Optional[str] = None,
    text_format_metadata: Optional[str] = None,
    thumb: Optional[str] = None,
    time_since_original_post: Optional[int] = None,
    title: Optional[str] = None,
    transcode_setting_properties: Optional[str] = None,
    unpublished_content_type: Optional[str] = None,
    upload_phase: Optional[str] = None,
    upload_session_id: Optional[str] = None,
    upload_setting_properties: Optional[str] = None,
    video_file_chunk: Optional[str] = None,
    video_id_original: Optional[str] = None,
    video_start_time_ms: Optional[int] = None,
    waterfall_id: Optional[str] = None,
) -> str:
    """POST /advideos on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        application_id: Optional.
        asked_fun_fact_prompt_id: Optional.
        audio_story_wave_animation_handle: Optional.
        chunk_session_id: Optional.
        composer_entry_picker: Optional.
        composer_entry_point: Optional.
        composer_entry_time: Optional.
        composer_session_events_log: Optional.
        composer_session_id: Optional.
        composer_source_surface: Optional.
        composer_type: Optional.
        container_type: Optional. Values: ACO_VIDEO_VARIATION, ADS_AI_GENERATED, AD_BREAK_PREVIEW, AD_DERIVATIVE, AD_LIBRARY_WATERMARK, ALBUM_MULTIMEDIA_POST, ALOHA_SUPERFRAME, APP_REREVIEW_SCREENCAST, APP_REVIEW_SCREENCAST, ASSET_MANAGER, ATLAS_VIDEO, AUDIO_BROADCAST, AUDIO_COMMENT, BROADCAST, CANVAS, CMS_MEDIA_MANAGER, CONTAINED_POST_ATTACHMENT, CONTAINED_POST_AUDIO_BROADCAST, CONTAINED_POST_COPYRIGHT_REFERENCE_BROADCAST, COPYRIGHT_REFERENCE_BROADCAST, COPYRIGHT_REFERENCE_IG_XPOST_VIDEO, COPYRIGHT_REFERENCE_VIDEO, CREATION_ML_PRECREATION, CREATOR_FAN_CHALLENGE, CREATOR_STOREFRONT_PERSONALIZED_VIDEO, CREATOR_STOREFRONT_PROMOTIONAL_VIDEO, DATAGENIX_VIDEO, DCO_AD_ASSET_FEED, DCO_AUTOGEN_VIDEO, DCO_TRIMMED_VIDEO, DIM_SUM, DIRECTED_POST_ATTACHMENT, DIRECT_INBOX, DOUBLE_PROD_EXPERIMENT, DROPS_SHOPPING_EVENT_PAGE, DYNAMIC_ITEM_VIDEO, DYNAMIC_TEMPLATE_VIDEO, EVENT_COVER_VIDEO, EVENT_TOUR, FACECAST_DVR, FB_AVATAR_ANIMATED_SATP, FB_COLLECTIBLE_VIDEO, FB_SHORTS, FB_SHORTS_CONTENT_REMIXABLE, FB_SHORTS_GROUP_POST, FB_SHORTS_LINKED_PRODUCT, FB_SHORTS_PMV_POST, FB_SHORTS_POST, FB_SHORTS_REMIX_POST, FUNDRAISER_COVER_VIDEO, GAME_CLIP, GIF_TO_VIDEO, GOODWILL_ANNIVERSARY_DEPRECATED, GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED, GOODWILL_VIDEO_CONTAINED_SHARE, GOODWILL_VIDEO_PROMOTION, GOODWILL_VIDEO_SHARE, GOODWILL_VIDEO_TOKEN_REQUIRED, GROUP_POST, HEURISTIC_CLUSTER_VIDEO, HIGHLIGHT_CLIP_VIDEO, HORIZON_WORLDS_TV, HUDDLE_BROADCAST, IG_REELS_XPV, INSPIRATION_VIDEO, INSTAGRAM_VIDEO_COPY, INSTANT_APPLICATION_PREVIEW, INSTANT_ARTICLE, ISSUE_MODULE, LEARN, LEGACY, LEGACY_CONTAINED_POST_BROADCAST, LIVE_AUDIO_ROOM_BROADCAST, LIVE_CLIP_PREVIEW, LIVE_CLIP_WORKCHAT, LIVE_CREATIVE_KIT_VIDEO, LIVE_PHOTO, LOOK_NOW_DEPRECATED, MARKETPLACE_LISTING_VIDEO, MARKETPLACE_PRE_RECORDED_VIDEO, MOMENTS_VIDEO, MUSIC_CLIP, MUSIC_CLIP_IN_COMMENT, MUSIC_CLIP_IN_LIGHTWEIGHT_STATUS, MUSIC_CLIP_IN_MAPLE_POST, MUSIC_CLIP_IN_MSGR_NOTE, MUSIC_CLIP_IN_POLL_OPTION, MUSIC_CLIP_ON_DATING_PROFILE, NEO_ASYNC_GAME_VIDEO, NEW_CONTAINED_POST_BROADCAST, NO_STORY, OCULUS_CREATOR_PORTAL, OCULUS_VENUES_BROADCAST, ORIGINALITY_SELF_ADVOCACY, PAGES_COVER_VIDEO, PAGE_REVIEW_SCREENCAST, PAGE_SLIDESHOW_VIDEO, PAID_CONTENT_PREVIEW, PAID_CONTENT_VIDEO, PAID_CONTENT_VIDEO__POST, PIXELCLOUD, PODCAST_HIGHLIGHT, PODCAST_ML_PREVIEW, PODCAST_ML_PREVIEW_NO_NEWSFEED_STORY, PODCAST_RSS, PODCAST_RSS_EPHEMERAL, PODCAST_RSS_NO_NEWSFEED_STORY, PODCAST_VOICES, PODCAST_VOICES_NO_NEWSFEED_STORY, PREMIERE_SOURCE, PREMIUM_MUSIC_VIDEO_CLIP, PREMIUM_MUSIC_VIDEO_CROPPED_CLIP, PREMIUM_MUSIC_VIDEO_NO_NEWSFEED_STORY, PREMIUM_MUSIC_VIDEO_WITH_NEWSFEED_STORY, PRIVATE_GALLERY_VIDEO, PRODUCT_VIDEO, PROFILE_COVER_VIDEO, PROFILE_INTRO_CARD, PROFILE_VIDEO, PROTON, QUICK_CLIP_WORKPLACE_POST, QUICK_PROMOTION, REPLACE_VIDEO, SHOWREEL_NATIVE_DUMMY_VIDEO, SLIDESHOW_ANIMOTO, SLIDESHOW_SHAKR, SLIDESHOW_VARIATION_VIDEO, SOUND_PLATFORM_STREAM, SRT_ATTACHMENT, STORIES_VIDEO, STORYLINE, STORYLINE_WITH_EXTERNAL_MUSIC, STORY_ARCHIVE_VIDEO, STORY_CARD_TEMPLATE, STREAM_HIGHLIGHTS_VIDEO, TAROT_DIGEST, TEMPORARY, TEMPORARY_UNLISTED, TEMP_VIDEO_COPYRIGHT_SCAN, UNLISTED, UNLISTED_OCULUS, VIDEO_COMMENT, VIDEO_COMPOSITION_VARIATION, VIDEO_CREATIVE_EDITOR_AUTOGEN_AD_VIDEO, VIDEO_SUPERRES, VU_GENERATED_VIDEO, WOODHENGE, WORK_KNOWLEDGE_VIDEO, YOUR_DAY
        content_category: Optional. Values: BEAUTY_FASHION, BUSINESS, CARS_TRUCKS, COMEDY, CUTE_ANIMALS, ENTERTAINMENT, FAMILY, FOOD_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, OTHER, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO_GAMING
        creative_tools: Optional.
        description: Optional.
        embeddable: Optional.
        end_offset: Optional.
        fbuploader_video_file_chunk: Optional.
        file_size: Optional.
        file_url: Optional.
        fisheye_video_cropped: Optional.
        formatting: Optional. Values: MARKDOWN, PLAINTEXT
        fov: Optional.
        front_z_rotation: Optional.
        fun_fact_prompt_id: Optional.
        fun_fact_toastee_id: Optional.
        guide: Optional.
        guide_enabled: Optional.
        initial_heading: Optional.
        initial_pitch: Optional.
        instant_game_entry_point_data: Optional.
        is_boost_intended: Optional.
        is_group_linking_post: Optional.
        is_partnership_ad: Optional.
        is_voice_clip: Optional.
        location_source_id: Optional.
        name: Optional.
        og_action_type_id: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_suggestion_mechanism: Optional.
        original_fov: Optional.
        original_projection_type: Optional. Values: cubemap, equirectangular, half_equirectangular
        partnership_ad_ad_code: Optional.
        publish_event_id: Optional.
        referenced_sticker_id: Optional.
        replace_video_id: Optional.
        slideshow_spec: Optional.
        source: Optional.
        source_instagram_media_id: Optional.
        spherical: Optional.
        start_offset: Optional.
        swap_mode: Optional. Values: replace
        text_format_metadata: Optional.
        thumb: Optional.
        time_since_original_post: Optional.
        title: Optional.
        transcode_setting_properties: Optional.
        unpublished_content_type: Optional. Values: ADS_POST, DRAFT, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT, SCHEDULED, SCHEDULED_RECURRING
        upload_phase: Optional. Values: cancel, finish, start, transfer
        upload_session_id: Optional.
        upload_setting_properties: Optional.
        video_file_chunk: Optional.
        video_id_original: Optional.
        video_start_time_ms: Optional.
        waterfall_id: Optional.
    """
    params = {}
    if application_id is not None:
        params["application_id"] = application_id
    if asked_fun_fact_prompt_id is not None:
        params["asked_fun_fact_prompt_id"] = asked_fun_fact_prompt_id
    if audio_story_wave_animation_handle is not None:
        params["audio_story_wave_animation_handle"] = audio_story_wave_animation_handle
    if chunk_session_id is not None:
        params["chunk_session_id"] = chunk_session_id
    if composer_entry_picker is not None:
        params["composer_entry_picker"] = composer_entry_picker
    if composer_entry_point is not None:
        params["composer_entry_point"] = composer_entry_point
    if composer_entry_time is not None:
        params["composer_entry_time"] = composer_entry_time
    if composer_session_events_log is not None:
        params["composer_session_events_log"] = composer_session_events_log
    if composer_session_id is not None:
        params["composer_session_id"] = composer_session_id
    if composer_source_surface is not None:
        params["composer_source_surface"] = composer_source_surface
    if composer_type is not None:
        params["composer_type"] = composer_type
    if container_type is not None:
        params["container_type"] = container_type
    if content_category is not None:
        params["content_category"] = content_category
    if creative_tools is not None:
        params["creative_tools"] = creative_tools
    if description is not None:
        params["description"] = description
    if embeddable is not None:
        params["embeddable"] = embeddable
    if end_offset is not None:
        params["end_offset"] = end_offset
    if fbuploader_video_file_chunk is not None:
        params["fbuploader_video_file_chunk"] = fbuploader_video_file_chunk
    if file_size is not None:
        params["file_size"] = file_size
    if file_url is not None:
        params["file_url"] = file_url
    if fisheye_video_cropped is not None:
        params["fisheye_video_cropped"] = fisheye_video_cropped
    if formatting is not None:
        params["formatting"] = formatting
    if fov is not None:
        params["fov"] = fov
    if front_z_rotation is not None:
        params["front_z_rotation"] = front_z_rotation
    if fun_fact_prompt_id is not None:
        params["fun_fact_prompt_id"] = fun_fact_prompt_id
    if fun_fact_toastee_id is not None:
        params["fun_fact_toastee_id"] = fun_fact_toastee_id
    if guide is not None:
        params["guide"] = guide
    if guide_enabled is not None:
        params["guide_enabled"] = guide_enabled
    if initial_heading is not None:
        params["initial_heading"] = initial_heading
    if initial_pitch is not None:
        params["initial_pitch"] = initial_pitch
    if instant_game_entry_point_data is not None:
        params["instant_game_entry_point_data"] = instant_game_entry_point_data
    if is_boost_intended is not None:
        params["is_boost_intended"] = is_boost_intended
    if is_group_linking_post is not None:
        params["is_group_linking_post"] = is_group_linking_post
    if is_partnership_ad is not None:
        params["is_partnership_ad"] = is_partnership_ad
    if is_voice_clip is not None:
        params["is_voice_clip"] = is_voice_clip
    if location_source_id is not None:
        params["location_source_id"] = location_source_id
    if name is not None:
        params["name"] = name
    if og_action_type_id is not None:
        params["og_action_type_id"] = og_action_type_id
    if og_icon_id is not None:
        params["og_icon_id"] = og_icon_id
    if og_object_id is not None:
        params["og_object_id"] = og_object_id
    if og_phrase is not None:
        params["og_phrase"] = og_phrase
    if og_suggestion_mechanism is not None:
        params["og_suggestion_mechanism"] = og_suggestion_mechanism
    if original_fov is not None:
        params["original_fov"] = original_fov
    if original_projection_type is not None:
        params["original_projection_type"] = original_projection_type
    if partnership_ad_ad_code is not None:
        params["partnership_ad_ad_code"] = partnership_ad_ad_code
    if publish_event_id is not None:
        params["publish_event_id"] = publish_event_id
    if referenced_sticker_id is not None:
        params["referenced_sticker_id"] = referenced_sticker_id
    if replace_video_id is not None:
        params["replace_video_id"] = replace_video_id
    if slideshow_spec is not None:
        params["slideshow_spec"] = slideshow_spec
    if source is not None:
        params["source"] = source
    if source_instagram_media_id is not None:
        params["source_instagram_media_id"] = source_instagram_media_id
    if spherical is not None:
        params["spherical"] = spherical
    if start_offset is not None:
        params["start_offset"] = start_offset
    if swap_mode is not None:
        params["swap_mode"] = swap_mode
    if text_format_metadata is not None:
        params["text_format_metadata"] = text_format_metadata
    if thumb is not None:
        params["thumb"] = thumb
    if time_since_original_post is not None:
        params["time_since_original_post"] = time_since_original_post
    if title is not None:
        params["title"] = title
    if transcode_setting_properties is not None:
        params["transcode_setting_properties"] = transcode_setting_properties
    if unpublished_content_type is not None:
        params["unpublished_content_type"] = unpublished_content_type
    if upload_phase is not None:
        params["upload_phase"] = upload_phase
    if upload_session_id is not None:
        params["upload_session_id"] = upload_session_id
    if upload_setting_properties is not None:
        params["upload_setting_properties"] = upload_setting_properties
    if video_file_chunk is not None:
        params["video_file_chunk"] = video_file_chunk
    if video_id_original is not None:
        params["video_id_original"] = video_id_original
    if video_start_time_ms is not None:
        params["video_start_time_ms"] = video_start_time_ms
    if waterfall_id is not None:
        params["waterfall_id"] = waterfall_id
    result = await get_client().post(f"act_{account_id}/advideos", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_affectedadsets(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /affectedadsets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/affectedadsets", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_agencies(ad_account_id: str, business: str) -> str:
    """DELETE /agencies on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{ad_account_id}/agencies")
    return json.dumps(result, indent=2)


async def get_ad_account_agencies(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_agencies(account_id: str, business: str, permitted_tasks: Optional[str] = None) -> str:
    """POST /agencies on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        business: Required.
        permitted_tasks: Optional. Values: AA_ANALYZE, ADVERTISE, ANALYZE, DRAFT, MANAGE
    """
    params = {}
    params["business"] = business
    if permitted_tasks is not None:
        params["permitted_tasks"] = permitted_tasks
    result = await get_client().post(f"act_{account_id}/agencies", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_applications(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /applications on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/applications", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_assigned_users(ad_account_id: str, user: int) -> str:
    """DELETE /assigned_users on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{ad_account_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_ad_account_assigned_users(ad_account_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{ad_account_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_assigned_users(account_id: str, user: int, tasks: Optional[str] = None) -> str:
    """POST /assigned_users on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        tasks: Optional. Values: AA_ANALYZE, ADVERTISE, ANALYZE, DRAFT, MANAGE
        user: Required.
    """
    params = {}
    if tasks is not None:
        params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"act_{account_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def create_ad_account_async_batch_requests(account_id: str, adbatch: str, name: str) -> str:
    """POST /async_batch_requests on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        adbatch: Required.
        name: Required.
    """
    params = {}
    params["adbatch"] = adbatch
    params["name"] = name
    result = await get_client().post(f"act_{account_id}/async_batch_requests", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_async_requests(
    ad_account_id: str,
    fields: Optional[str] = None,
    status: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /async_requests on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        status: Optional. Values: ERROR, EXECUTING, FINISHED, INITIALIZED
        type_: Optional. Values: ASYNC_ADGROUP_CREATION, BATCH_API, DRAFTS
    """
    params = {}
    params["fields"] = fields or "id,name"
    if status is not None:
        params["status"] = status
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{ad_account_id}/async_requests", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_asyncadcreatives(
    ad_account_id: str,
    fields: Optional[str] = None,
    is_completed: Optional[bool] = None,
) -> str:
    """GET /asyncadcreatives on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        is_completed: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if is_completed is not None:
        params["is_completed"] = is_completed
    result = await get_client().get(f"{ad_account_id}/asyncadcreatives", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_asyncadcreatives(
    account_id: str,
    creative_spec: str,
    name: str,
    notification_mode: Optional[str] = None,
    notification_uri: Optional[str] = None,
) -> str:
    """POST /asyncadcreatives on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        creative_spec: Required.
        name: Required.
        notification_mode: Optional. Values: OFF, ON_COMPLETE
        notification_uri: Optional.
    """
    params = {}
    params["creative_spec"] = creative_spec
    params["name"] = name
    if notification_mode is not None:
        params["notification_mode"] = notification_mode
    if notification_uri is not None:
        params["notification_uri"] = notification_uri
    result = await get_client().post(f"act_{account_id}/asyncadcreatives", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_asyncadrequestsets(
    ad_account_id: str,
    fields: Optional[str] = None,
    is_completed: Optional[bool] = None,
) -> str:
    """GET /asyncadrequestsets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        is_completed: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if is_completed is not None:
        params["is_completed"] = is_completed
    result = await get_client().get(f"{ad_account_id}/asyncadrequestsets", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_asyncadrequestsets(
    account_id: str,
    ad_specs: str,
    name: str,
    notification_mode: Optional[str] = None,
    notification_uri: Optional[str] = None,
) -> str:
    """POST /asyncadrequestsets on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        ad_specs: Required.
        name: Required.
        notification_mode: Optional. Values: OFF, ON_COMPLETE
        notification_uri: Optional.
    """
    params = {}
    params["ad_specs"] = ad_specs
    params["name"] = name
    if notification_mode is not None:
        params["notification_mode"] = notification_mode
    if notification_uri is not None:
        params["notification_uri"] = notification_uri
    result = await get_client().post(f"act_{account_id}/asyncadrequestsets", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_audience_funnel(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /audience_funnel on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/audience_funnel", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_block_list_drafts(account_id: str, publisher_urls_file: str) -> str:
    """POST /block_list_drafts on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        publisher_urls_file: Required.
    """
    params = {}
    params["publisher_urls_file"] = publisher_urls_file
    result = await get_client().post(f"act_{account_id}/block_list_drafts", data=params)
    return json.dumps(result, indent=2)


async def create_ad_account_brand_safety_content_filter_levels(
    account_id: str,
    brand_safety_content_filter_levels: str,
    business_id: Optional[str] = None,
) -> str:
    """POST /brand_safety_content_filter_levels on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        brand_safety_content_filter_levels: Required. Values: AN_RELAXED, AN_STANDARD, AN_STRICT, FACEBOOK_RELAXED, FACEBOOK_STANDARD, FACEBOOK_STRICT, FEED_DNM, FEED_RELAXED, FEED_STANDARD, FEED_STRICT, UNINITIALIZED, UNKNOWN
        business_id: Optional.
    """
    params = {}
    params["brand_safety_content_filter_levels"] = brand_safety_content_filter_levels
    if business_id is not None:
        params["business_id"] = business_id
    result = await get_client().post(f"act_{account_id}/brand_safety_content_filter_levels", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_broadtargetingcategories(
    ad_account_id: str,
    fields: Optional[str] = None,
    custom_categories_only: Optional[bool] = None,
) -> str:
    """GET /broadtargetingcategories on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        custom_categories_only: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if custom_categories_only is not None:
        params["custom_categories_only"] = custom_categories_only
    result = await get_client().get(f"{ad_account_id}/broadtargetingcategories", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_businessprojects(ad_account_id: str, fields: Optional[str] = None, business: Optional[str] = None) -> str:
    """GET /businessprojects on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        business: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business is not None:
        params["business"] = business
    result = await get_client().get(f"{ad_account_id}/businessprojects", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_campaigns(
    ad_account_id: str,
    delete_strategy: str,
    before_date: Optional[str] = None,
    delete_offset: Optional[int] = None,
    object_count: Optional[int] = None,
) -> str:
    """DELETE /campaigns on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        before_date: Optional.
        delete_offset: Optional.
        delete_strategy: Required. Values: DELETE_ANY, DELETE_ARCHIVED_BEFORE, DELETE_OLDEST
        object_count: Optional.
    """
    params = {}
    if before_date is not None:
        params["before_date"] = before_date
    if delete_offset is not None:
        params["delete_offset"] = delete_offset
    params["delete_strategy"] = delete_strategy
    if object_count is not None:
        params["object_count"] = object_count
    result = await get_client().delete(f"{ad_account_id}/campaigns")
    return json.dumps(result, indent=2)


async def get_ad_account_campaigns(
    ad_account_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    effective_status: Optional[str] = None,
    is_completed: Optional[bool] = None,
    time_range: Optional[str] = None,
) -> str:
    """GET /campaigns on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
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
    result = await get_client().get(f"{ad_account_id}/campaigns", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_campaigns(
    account_id: str,
    special_ad_categories: str,
    adlabels: Optional[str] = None,
    bid_strategy: Optional[str] = None,
    budget_schedule_specs: Optional[str] = None,
    buying_type: Optional[str] = None,
    daily_budget: Optional[int] = None,
    execution_options: Optional[str] = None,
    is_adset_budget_sharing_enabled: Optional[bool] = None,
    is_budget_schedule_enabled: Optional[bool] = None,
    is_direct_send_campaign: Optional[bool] = None,
    is_message_campaign: Optional[bool] = None,
    is_skadnetwork_attribution: Optional[bool] = None,
    iterative_split_test_configs: Optional[str] = None,
    lifetime_budget: Optional[int] = None,
    name: Optional[str] = None,
    objective: Optional[str] = None,
    pacing_type: Optional[str] = None,
    promoted_object: Optional[str] = None,
    smart_promotion_type: Optional[str] = None,
    source_campaign_id: Optional[str] = None,
    special_ad_category_country: Optional[str] = None,
    spend_cap: Optional[int] = None,
    start_time: Optional[str] = None,
    status: Optional[str] = None,
    stop_time: Optional[str] = None,
    topline_id: Optional[str] = None,
) -> str:
    """POST /campaigns on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        adlabels: Optional.
        bid_strategy: Optional. Values: COST_CAP, LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, LOWEST_COST_WITH_MIN_ROAS
        budget_schedule_specs: Optional.
        buying_type: Optional.
        daily_budget: Optional.
        execution_options: Optional. Values: include_recommendations, validate_only
        is_adset_budget_sharing_enabled: Optional.
        is_budget_schedule_enabled: Optional.
        is_direct_send_campaign: Optional.
        is_message_campaign: Optional.
        is_skadnetwork_attribution: Optional.
        iterative_split_test_configs: Optional.
        lifetime_budget: Optional.
        name: Optional.
        objective: Optional. Values: APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS
        pacing_type: Optional.
        promoted_object: Optional.
        smart_promotion_type: Optional. Values: GUIDED_CREATION, SMART_APP_PROMOTION
        source_campaign_id: Optional.
        special_ad_categories: Required. Values: CREDIT, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, HOUSING, ISSUES_ELECTIONS_POLITICS, NONE, ONLINE_GAMBLING_AND_GAMING
        special_ad_category_country: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        spend_cap: Optional.
        start_time: Optional.
        status: Optional. Values: ACTIVE, ARCHIVED, DELETED, PAUSED
        stop_time: Optional.
        topline_id: Optional.
    """
    params = {}
    if adlabels is not None:
        params["adlabels"] = adlabels
    if bid_strategy is not None:
        params["bid_strategy"] = bid_strategy
    if budget_schedule_specs is not None:
        params["budget_schedule_specs"] = budget_schedule_specs
    if buying_type is not None:
        params["buying_type"] = buying_type
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
    if source_campaign_id is not None:
        params["source_campaign_id"] = source_campaign_id
    params["special_ad_categories"] = special_ad_categories
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
    if topline_id is not None:
        params["topline_id"] = topline_id
    result = await get_client().post(f"act_{account_id}/campaigns", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_campaignsbylabels(
    ad_account_id: str,
    ad_label_ids: str,
    fields: Optional[str] = None,
    operator: Optional[str] = None,
) -> str:
    """GET /campaignsbylabels on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        ad_label_ids: Required.
        operator: Optional. Values: ALL, ANY
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["ad_label_ids"] = ad_label_ids
    if operator is not None:
        params["operator"] = operator
    result = await get_client().get(f"{ad_account_id}/campaignsbylabels", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_connected_instagram_accounts(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /connected_instagram_accounts on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/connected_instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_connected_instagram_accounts_with_iabp(
    ad_account_id: str,
    fields: Optional[str] = None,
    business_id: Optional[str] = None,
) -> str:
    """GET /connected_instagram_accounts_with_iabp on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        business_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business_id is not None:
        params["business_id"] = business_id
    result = await get_client().get(f"{ad_account_id}/connected_instagram_accounts_with_iabp", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_conversion_goals(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /conversion_goals on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/conversion_goals", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_customaudiences(
    ad_account_id: str,
    business_id: Optional[str] = None,
    fetch_primary_audience: Optional[bool] = None,
    fields: Optional[str] = None,
    filtering: Optional[str] = None,
    pixel_id: Optional[str] = None,
) -> str:
    """GET /customaudiences on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        business_id: Optional.
        fetch_primary_audience: Optional.
        fields: Optional.
        filtering: Optional.
        pixel_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business_id is not None:
        params["business_id"] = business_id
    if fetch_primary_audience is not None:
        params["fetch_primary_audience"] = fetch_primary_audience
    if fields is not None:
        params["fields"] = fields
    if filtering is not None:
        params["filtering"] = filtering
    if pixel_id is not None:
        params["pixel_id"] = pixel_id
    result = await get_client().get(f"{ad_account_id}/customaudiences", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_customaudiences(
    account_id: str,
    allowed_domains: Optional[str] = None,
    associated_audience_id: Optional[int] = None,
    claim_objective: Optional[str] = None,
    content_type: Optional[str] = None,
    countries: Optional[str] = None,
    creation_params: Optional[str] = None,
    customer_file_source: Optional[str] = None,
    dataset_id: Optional[str] = None,
    description: Optional[str] = None,
    enable_fetch_or_create: Optional[bool] = None,
    event_source_group: Optional[str] = None,
    event_sources: Optional[str] = None,
    exclusions: Optional[str] = None,
    facebook_page_id: Optional[str] = None,
    inclusionOperator: Optional[str] = None,
    inclusions: Optional[str] = None,
    is_snapshot: Optional[bool] = None,
    is_value_based: Optional[bool] = None,
    list_of_accounts: Optional[str] = None,
    lookalike_spec: Optional[str] = None,
    marketing_message_channels: Optional[str] = None,
    name: Optional[str] = None,
    opt_out_link: Optional[str] = None,
    origin_audience_id: Optional[str] = None,
    parent_audience_id: Optional[int] = None,
    partner_reference_key: Optional[str] = None,
    pixel_id: Optional[str] = None,
    prefill: Optional[bool] = None,
    product_set_id: Optional[str] = None,
    regulated_audience_spec: Optional[str] = None,
    retention_days: Optional[int] = None,
    rev_share_policy_id: Optional[int] = None,
    rule: Optional[str] = None,
    rule_aggregation: Optional[str] = None,
    subscription_info: Optional[str] = None,
    subtype: Optional[str] = None,
    use_for_products: Optional[str] = None,
    use_in_campaigns: Optional[bool] = None,
    video_group_ids: Optional[str] = None,
    whats_app_business_phone_number_id: Optional[str] = None,
) -> str:
    """POST /customaudiences on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        allowed_domains: Optional.
        associated_audience_id: Optional.
        claim_objective: Optional. Values: AUTOMOTIVE_MODEL, COLLABORATIVE_ADS, HOME_LISTING, MEDIA_TITLE, PRODUCT, TRAVEL, VEHICLE, VEHICLE_OFFER
        content_type: Optional. Values: AUTOMOTIVE_MODEL, DESTINATION, FLIGHT, GENERIC, HOME_LISTING, HOTEL, LOCAL_SERVICE_BUSINESS, MEDIA_TITLE, OFFLINE_PRODUCT, PRODUCT, VEHICLE, VEHICLE_OFFER
        countries: Optional.
        creation_params: Optional.
        customer_file_source: Optional. Values: BOTH_USER_AND_PARTNER_PROVIDED, PARTNER_PROVIDED_ONLY, USER_PROVIDED_ONLY
        dataset_id: Optional.
        description: Optional.
        enable_fetch_or_create: Optional.
        event_source_group: Optional.
        event_sources: Optional.
        exclusions: Optional.
        facebook_page_id: Optional.
        inclusionOperator: Optional.
        inclusions: Optional.
        is_snapshot: Optional.
        is_value_based: Optional.
        list_of_accounts: Optional.
        lookalike_spec: Optional.
        marketing_message_channels: Optional.
        name: Optional.
        opt_out_link: Optional.
        origin_audience_id: Optional.
        parent_audience_id: Optional.
        partner_reference_key: Optional.
        pixel_id: Optional.
        prefill: Optional.
        product_set_id: Optional.
        regulated_audience_spec: Optional.
        retention_days: Optional.
        rev_share_policy_id: Optional.
        rule: Optional.
        rule_aggregation: Optional.
        subscription_info: Optional. Values: MESSENGER, WHATSAPP
        subtype: Optional. Values: APP, BAG_OF_ACCOUNTS, BIDDING, CLAIM, CUSTOM, ENGAGEMENT, EXCLUSION, FOX, LOOKALIKE, MANAGED, MEASUREMENT, MESSENGER_SUBSCRIBER_LIST, OFFLINE_CONVERSION, PARTNER, PRIMARY, REGULATED_CATEGORIES_AUDIENCE, STUDY_RULE_AUDIENCE, VIDEO, WEBSITE
        use_for_products: Optional. Values: ADS, MARKETING_MESSAGES
        use_in_campaigns: Optional.
        video_group_ids: Optional.
        whats_app_business_phone_number_id: Optional.
    """
    params = {}
    if allowed_domains is not None:
        params["allowed_domains"] = allowed_domains
    if associated_audience_id is not None:
        params["associated_audience_id"] = associated_audience_id
    if claim_objective is not None:
        params["claim_objective"] = claim_objective
    if content_type is not None:
        params["content_type"] = content_type
    if countries is not None:
        params["countries"] = countries
    if creation_params is not None:
        params["creation_params"] = creation_params
    if customer_file_source is not None:
        params["customer_file_source"] = customer_file_source
    if dataset_id is not None:
        params["dataset_id"] = dataset_id
    if description is not None:
        params["description"] = description
    if enable_fetch_or_create is not None:
        params["enable_fetch_or_create"] = enable_fetch_or_create
    if event_source_group is not None:
        params["event_source_group"] = event_source_group
    if event_sources is not None:
        params["event_sources"] = event_sources
    if exclusions is not None:
        params["exclusions"] = exclusions
    if facebook_page_id is not None:
        params["facebook_page_id"] = facebook_page_id
    if inclusionOperator is not None:
        params["inclusionOperator"] = inclusionOperator
    if inclusions is not None:
        params["inclusions"] = inclusions
    if is_snapshot is not None:
        params["is_snapshot"] = is_snapshot
    if is_value_based is not None:
        params["is_value_based"] = is_value_based
    if list_of_accounts is not None:
        params["list_of_accounts"] = list_of_accounts
    if lookalike_spec is not None:
        params["lookalike_spec"] = lookalike_spec
    if marketing_message_channels is not None:
        params["marketing_message_channels"] = marketing_message_channels
    if name is not None:
        params["name"] = name
    if opt_out_link is not None:
        params["opt_out_link"] = opt_out_link
    if origin_audience_id is not None:
        params["origin_audience_id"] = origin_audience_id
    if parent_audience_id is not None:
        params["parent_audience_id"] = parent_audience_id
    if partner_reference_key is not None:
        params["partner_reference_key"] = partner_reference_key
    if pixel_id is not None:
        params["pixel_id"] = pixel_id
    if prefill is not None:
        params["prefill"] = prefill
    if product_set_id is not None:
        params["product_set_id"] = product_set_id
    if regulated_audience_spec is not None:
        params["regulated_audience_spec"] = regulated_audience_spec
    if retention_days is not None:
        params["retention_days"] = retention_days
    if rev_share_policy_id is not None:
        params["rev_share_policy_id"] = rev_share_policy_id
    if rule is not None:
        params["rule"] = rule
    if rule_aggregation is not None:
        params["rule_aggregation"] = rule_aggregation
    if subscription_info is not None:
        params["subscription_info"] = subscription_info
    if subtype is not None:
        params["subtype"] = subtype
    if use_for_products is not None:
        params["use_for_products"] = use_for_products
    if use_in_campaigns is not None:
        params["use_in_campaigns"] = use_in_campaigns
    if video_group_ids is not None:
        params["video_group_ids"] = video_group_ids
    if whats_app_business_phone_number_id is not None:
        params["whats_app_business_phone_number_id"] = whats_app_business_phone_number_id
    result = await get_client().post(f"act_{account_id}/customaudiences", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_customaudiencestos(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /customaudiencestos on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/customaudiencestos", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_customaudiencestos(account_id: str, tos_id: str, business_id: Optional[str] = None) -> str:
    """POST /customaudiencestos on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        business_id: Optional.
        tos_id: Required.
    """
    params = {}
    if business_id is not None:
        params["business_id"] = business_id
    params["tos_id"] = tos_id
    result = await get_client().post(f"act_{account_id}/customaudiencestos", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_customconversions(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /customconversions on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/customconversions", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_customconversions(
    account_id: str,
    name: str,
    action_source_type: Optional[str] = None,
    advanced_rule: Optional[str] = None,
    custom_event_type: Optional[str] = None,
    default_conversion_value: Optional[float] = None,
    description: Optional[str] = None,
    event_source_id: Optional[str] = None,
    rule: Optional[str] = None,
) -> str:
    """POST /customconversions on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        action_source_type: Optional. Values: app, business_messaging, chat, email, other, phone_call, physical_store, system_generated, website
        advanced_rule: Optional.
        custom_event_type: Optional. Values: ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, COMPLETE_REGISTRATION, CONTACT, CONTENT_VIEW, CUSTOMIZE_PRODUCT, DONATE, FACEBOOK_SELECTED, FIND_LOCATION, INITIATED_CHECKOUT, LEAD, LISTING_INTERACTION, OTHER, PURCHASE, SCHEDULE, SEARCH, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE
        default_conversion_value: Optional.
        description: Optional.
        event_source_id: Optional.
        name: Required.
        rule: Optional.
    """
    params = {}
    if action_source_type is not None:
        params["action_source_type"] = action_source_type
    if advanced_rule is not None:
        params["advanced_rule"] = advanced_rule
    if custom_event_type is not None:
        params["custom_event_type"] = custom_event_type
    if default_conversion_value is not None:
        params["default_conversion_value"] = default_conversion_value
    if description is not None:
        params["description"] = description
    if event_source_id is not None:
        params["event_source_id"] = event_source_id
    params["name"] = name
    if rule is not None:
        params["rule"] = rule
    result = await get_client().post(f"act_{account_id}/customconversions", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_delivery_estimate(
    ad_account_id: str,
    optimization_goal: str,
    targeting_spec: str,
    fields: Optional[str] = None,
    promoted_object: Optional[str] = None,
) -> str:
    """GET /delivery_estimate on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        optimization_goal: Required. Values: ADVERTISER_SILOED_VALUE, AD_RECALL_LIFT, APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, AUTOMATIC_OBJECTIVE, CONVERSATIONS, DERIVED_EVENTS, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, IN_APP_VALUE, LANDING_PAGE_VIEWS, LEAD_GENERATION, LINK_CLICKS, MEANINGFUL_CALL_ATTEMPT, MESSAGING_APPOINTMENT_CONVERSION, MESSAGING_PURCHASE_CONVERSION, NONE, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, PROFILE_AND_PAGE_ENGAGEMENT, PROFILE_VISIT, QUALITY_CALL, QUALITY_LEAD, REACH, REMINDERS_SET, SUBSCRIBERS, THRUPLAY, VALUE, VISIT_INSTAGRAM_PROFILE
        promoted_object: Optional.
        targeting_spec: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["optimization_goal"] = optimization_goal
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_account_id}/delivery_estimate", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_deprecatedtargetingadsets(ad_account_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /deprecatedtargetingadsets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        type_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{ad_account_id}/deprecatedtargetingadsets", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_dsa_recommendations(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /dsa_recommendations on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/dsa_recommendations", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_generatepreviews(
    ad_account_id: str,
    ad_format: str,
    creative: str,
    fields: Optional[str] = None,
    creative_feature: Optional[str] = None,
    dynamic_asset_label: Optional[str] = None,
    dynamic_creative_spec: Optional[str] = None,
    dynamic_customization: Optional[str] = None,
    end_date: Optional[str] = None,
    height: Optional[int] = None,
    locale: Optional[str] = None,
    message: Optional[str] = None,
    place_page_id: Optional[int] = None,
    post: Optional[str] = None,
    product_item_ids: Optional[str] = None,
    render_type: Optional[str] = None,
    start_date: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /generatepreviews on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        ad_format: Required. Values: AUDIENCE_NETWORK_INSTREAM_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE, AUDIENCE_NETWORK_OUTSTREAM_VIDEO, AUDIENCE_NETWORK_REWARDED_VIDEO, BIZ_DISCO_FEED_MOBILE, DESKTOP_FEED_STANDARD, FACEBOOK_IFU_REELS_MOBILE, FACEBOOK_PROFILE_FEED_DESKTOP, FACEBOOK_PROFILE_FEED_MOBILE, FACEBOOK_PROFILE_REELS_MOBILE, FACEBOOK_REELS_BANNER, FACEBOOK_REELS_BANNER_DESKTOP, FACEBOOK_REELS_BANNER_FEED_ANDROID, FACEBOOK_REELS_BANNER_FEED_ANDROID_LARGE, FACEBOOK_REELS_BANNER_FULLSCREEN_IOS, FACEBOOK_REELS_BANNER_FULLSCREEN_MOBILE, FACEBOOK_REELS_MOBILE, FACEBOOK_REELS_POSTLOOP, FACEBOOK_REELS_POSTLOOP_FEED, FACEBOOK_REELS_STICKER, FACEBOOK_STORY_MOBILE, FACEBOOK_STORY_STICKER_MOBILE, INSTAGRAM_EXPLORE_CONTEXTUAL, INSTAGRAM_EXPLORE_GRID_HOME, INSTAGRAM_EXPLORE_IMMERSIVE, INSTAGRAM_FEED_WEB, INSTAGRAM_FEED_WEB_M_SITE, INSTAGRAM_LEAD_GEN_MULTI_SUBMIT_ADS, INSTAGRAM_PROFILE_FEED, INSTAGRAM_PROFILE_REELS, INSTAGRAM_REELS, INSTAGRAM_REELS_INSTREAM, INSTAGRAM_REELS_OVERLAY, INSTAGRAM_REELS_WEB, INSTAGRAM_REELS_WEB_M_SITE, INSTAGRAM_SEARCH_CHAIN, INSTAGRAM_SEARCH_GRID, INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTAGRAM_STORY_EFFECT_TRAY, INSTAGRAM_STORY_WEB, INSTAGRAM_STORY_WEB_M_SITE, INSTANT_ARTICLE_RECIRCULATION_AD, INSTANT_ARTICLE_STANDARD, INSTREAM_BANNER_DESKTOP, INSTREAM_BANNER_FEED_IOS, INSTREAM_BANNER_FULLSCREEN_IOS, INSTREAM_BANNER_FULLSCREEN_MOBILE, INSTREAM_BANNER_IMMERSIVE_MOBILE, INSTREAM_BANNER_MOBILE, INSTREAM_VIDEO_DESKTOP, INSTREAM_VIDEO_FULLSCREEN_IOS, INSTREAM_VIDEO_FULLSCREEN_MOBILE, INSTREAM_VIDEO_IMAGE, INSTREAM_VIDEO_IMMERSIVE_MOBILE, INSTREAM_VIDEO_MOBILE, JOB_BROWSER_DESKTOP, JOB_BROWSER_MOBILE, MARKETPLACE_MOBILE, MESSENGER_MOBILE_INBOX_MEDIA, MESSENGER_MOBILE_STORY_MEDIA, MOBILE_BANNER, MOBILE_FEED_BASIC, MOBILE_FEED_STANDARD, MOBILE_FULLWIDTH, MOBILE_INTERSTITIAL, MOBILE_MEDIUM_RECTANGLE, MOBILE_NATIVE, RIGHT_COLUMN_STANDARD, SUGGESTED_VIDEO_DESKTOP, SUGGESTED_VIDEO_FULLSCREEN_MOBILE, SUGGESTED_VIDEO_IMMERSIVE_MOBILE, SUGGESTED_VIDEO_MOBILE, WATCH_FEED_HOME, WATCH_FEED_MOBILE
        creative: Required.
        creative_feature: Optional. Values: product_metadata_automation, profile_card, standard_enhancements_catalog, text_overlay_translation
        dynamic_asset_label: Optional.
        dynamic_creative_spec: Optional.
        dynamic_customization: Optional.
        end_date: Optional.
        height: Optional.
        locale: Optional.
        message: Optional.
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
    params["creative"] = creative
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
    if message is not None:
        params["message"] = message
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
    result = await get_client().get(f"{ad_account_id}/generatepreviews", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_impacting_ad_studies(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /impacting_ad_studies on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/impacting_ad_studies", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_insights(
    ad_account_id: str,
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
    """GET /insights on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
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
    result = await get_client().get(f"{ad_account_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_insights(
    account_id: str,
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
    """POST /insights on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
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
    result = await get_client().post(f"act_{account_id}/insights", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_instagram_accounts(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_accounts on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_ios_fourteen_campaign_limits(ad_account_id: str, app_id: str, fields: Optional[str] = None) -> str:
    """GET /ios_fourteen_campaign_limits on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        app_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["app_id"] = app_id
    result = await get_client().get(f"{ad_account_id}/ios_fourteen_campaign_limits", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_matched_search_applications(
    ad_account_id: str,
    app_store: str,
    query_term: str,
    fields: Optional[str] = None,
    allow_incomplete_app: Optional[bool] = None,
    app_store_country: Optional[str] = None,
    business_id: Optional[str] = None,
    is_skadnetwork_search: Optional[bool] = None,
    only_apps_with_permission: Optional[bool] = None,
    stores_to_filter: Optional[str] = None,
) -> str:
    """GET /matched_search_applications on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        allow_incomplete_app: Optional.
        app_store: Required. Values: ALL_APP_STORES_FOR_ANDROID_AND_IOS, AMAZON_APP_STORE, APK_MIRROR, APK_MONK, APK_PURE, APTOIDE_A1_STORE, BEMOBI_MOBILE_STORE, DIGITAL_TURBINE_STORE, DOES_NOT_EXIST, FB_ANDROID_STORE, FB_CANVAS, FB_GAMEROOM, GALAXY_STORE, GOOGLE_PLAY, INSTANT_GAME, ITUNES, ITUNES_IPAD, NEON_ANDROID_STORE, NONE, OCULUS_APP_STORE, OPPO, ROKU_STORE, UPTODOWN, VIVO, WINDOWS_10_STORE, WINDOWS_STORE, XIAOMI
        app_store_country: Optional.
        business_id: Optional.
        is_skadnetwork_search: Optional.
        only_apps_with_permission: Optional.
        query_term: Required.
        stores_to_filter: Optional. Values: ALL_APP_STORES_FOR_ANDROID_AND_IOS, AMAZON_APP_STORE, APK_MIRROR, APK_MONK, APK_PURE, APTOIDE_A1_STORE, BEMOBI_MOBILE_STORE, DIGITAL_TURBINE_STORE, DOES_NOT_EXIST, FB_ANDROID_STORE, FB_CANVAS, FB_GAMEROOM, GALAXY_STORE, GOOGLE_PLAY, INSTANT_GAME, ITUNES, ITUNES_IPAD, NEON_ANDROID_STORE, NONE, OCULUS_APP_STORE, OPPO, ROKU_STORE, UPTODOWN, VIVO, WINDOWS_10_STORE, WINDOWS_STORE, XIAOMI
    """
    params = {}
    params["fields"] = fields or "id,name"
    if allow_incomplete_app is not None:
        params["allow_incomplete_app"] = allow_incomplete_app
    params["app_store"] = app_store
    if app_store_country is not None:
        params["app_store_country"] = app_store_country
    if business_id is not None:
        params["business_id"] = business_id
    if is_skadnetwork_search is not None:
        params["is_skadnetwork_search"] = is_skadnetwork_search
    if only_apps_with_permission is not None:
        params["only_apps_with_permission"] = only_apps_with_permission
    params["query_term"] = query_term
    if stores_to_filter is not None:
        params["stores_to_filter"] = stores_to_filter
    result = await get_client().get(f"{ad_account_id}/matched_search_applications", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_max_bid(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /max_bid on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/max_bid", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_mcmeconversions(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /mcmeconversions on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/mcmeconversions", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_message_campaign(
    account_id: str,
    name: str,
    page_id: str,
    bid_amount: Optional[int] = None,
    daily_budget: Optional[int] = None,
    lifetime_budget: Optional[int] = None,
) -> str:
    """POST /message_campaign on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        bid_amount: Optional.
        daily_budget: Optional.
        lifetime_budget: Optional.
        name: Required.
        page_id: Required.
    """
    params = {}
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    if daily_budget is not None:
        params["daily_budget"] = daily_budget
    if lifetime_budget is not None:
        params["lifetime_budget"] = lifetime_budget
    params["name"] = name
    params["page_id"] = page_id
    result = await get_client().post(f"act_{account_id}/message_campaign", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_message_delivery_estimate(
    ad_account_id: str,
    promoted_object: str,
    targeting_spec: str,
    fields: Optional[str] = None,
    bid_amount: Optional[int] = None,
    daily_budget: Optional[int] = None,
    is_direct_send_campaign: Optional[bool] = None,
    lifetime_budget: Optional[int] = None,
    lifetime_in_days: Optional[int] = None,
    optimization_goal: Optional[str] = None,
    pacing_type: Optional[str] = None,
) -> str:
    """GET /message_delivery_estimate on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        bid_amount: Optional.
        daily_budget: Optional.
        is_direct_send_campaign: Optional.
        lifetime_budget: Optional.
        lifetime_in_days: Optional.
        optimization_goal: Optional. Values: ADVERTISER_SILOED_VALUE, AD_RECALL_LIFT, APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, AUTOMATIC_OBJECTIVE, CONVERSATIONS, DERIVED_EVENTS, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, IN_APP_VALUE, LANDING_PAGE_VIEWS, LEAD_GENERATION, LINK_CLICKS, MEANINGFUL_CALL_ATTEMPT, MESSAGING_APPOINTMENT_CONVERSION, MESSAGING_PURCHASE_CONVERSION, NONE, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, PROFILE_AND_PAGE_ENGAGEMENT, PROFILE_VISIT, QUALITY_CALL, QUALITY_LEAD, REACH, REMINDERS_SET, SUBSCRIBERS, THRUPLAY, VALUE, VISIT_INSTAGRAM_PROFILE
        pacing_type: Optional. Values: DAY_PARTING, DISABLED, NO_PACING, PROBABILISTIC_PACING, PROBABILISTIC_PACING_V2, STANDARD
        promoted_object: Required.
        targeting_spec: Required.
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
    params["promoted_object"] = promoted_object
    params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_account_id}/message_delivery_estimate", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_messages(
    account_id: str,
    message_id: int,
    messenger_delivery_data: str,
    message: Optional[str] = None,
) -> str:
    """POST /messages on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        message: Optional.
        message_id: Required.
        messenger_delivery_data: Required.
    """
    params = {}
    if message is not None:
        params["message"] = message
    params["message_id"] = message_id
    params["messenger_delivery_data"] = messenger_delivery_data
    result = await get_client().post(f"act_{account_id}/messages", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_minimum_budgets(
    ad_account_id: str,
    fields: Optional[str] = None,
    bid_amount: Optional[int] = None,
) -> str:
    """GET /minimum_budgets on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        bid_amount: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bid_amount is not None:
        params["bid_amount"] = bid_amount
    result = await get_client().get(f"{ad_account_id}/minimum_budgets", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_onbehalf_requests(ad_account_id: str, fields: Optional[str] = None, status: Optional[str] = None) -> str:
    """GET /onbehalf_requests on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        status: Optional. Values: APPROVE, CANCELED, DECLINE, EXPIRED, IN_PROGRESS, MMA_DIRECT_ASSETS_APPROVED, MMA_DIRECT_ASSETS_DECLINED, MMA_DIRECT_ASSETS_EXPIRED, MMA_DIRECT_ASSETS_PENDING, PENDING, PENDING_EMAIL_VERIFICATION, PENDING_INTEGRITY_REVIEW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{ad_account_id}/onbehalf_requests", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_product_audiences(
    account_id: str,
    name: str,
    product_set_id: str,
    allowed_domains: Optional[str] = None,
    associated_audience_id: Optional[int] = None,
    claim_objective: Optional[str] = None,
    content_type: Optional[str] = None,
    creation_params: Optional[str] = None,
    description: Optional[str] = None,
    enable_fetch_or_create: Optional[bool] = None,
    event_source_group: Optional[str] = None,
    event_sources: Optional[str] = None,
    exclusions: Optional[str] = None,
    inclusionOperator: Optional[str] = None,
    inclusions: Optional[str] = None,
    is_snapshot: Optional[bool] = None,
    is_value_based: Optional[bool] = None,
    opt_out_link: Optional[str] = None,
    parent_audience_id: Optional[int] = None,
    rev_share_policy_id: Optional[int] = None,
    subtype: Optional[str] = None,
) -> str:
    """POST /product_audiences on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        allowed_domains: Optional.
        associated_audience_id: Optional.
        claim_objective: Optional. Values: AUTOMOTIVE_MODEL, COLLABORATIVE_ADS, HOME_LISTING, MEDIA_TITLE, PRODUCT, TRAVEL, VEHICLE, VEHICLE_OFFER
        content_type: Optional. Values: AUTOMOTIVE_MODEL, DESTINATION, FLIGHT, GENERIC, HOME_LISTING, HOTEL, LOCAL_SERVICE_BUSINESS, MEDIA_TITLE, OFFLINE_PRODUCT, PRODUCT, VEHICLE, VEHICLE_OFFER
        creation_params: Optional.
        description: Optional.
        enable_fetch_or_create: Optional.
        event_source_group: Optional.
        event_sources: Optional.
        exclusions: Optional.
        inclusionOperator: Optional.
        inclusions: Optional.
        is_snapshot: Optional.
        is_value_based: Optional.
        name: Required.
        opt_out_link: Optional.
        parent_audience_id: Optional.
        product_set_id: Required.
        rev_share_policy_id: Optional.
        subtype: Optional. Values: APP, BAG_OF_ACCOUNTS, BIDDING, CLAIM, CUSTOM, ENGAGEMENT, EXCLUSION, FOX, LOOKALIKE, MANAGED, MEASUREMENT, MESSENGER_SUBSCRIBER_LIST, OFFLINE_CONVERSION, PARTNER, PRIMARY, REGULATED_CATEGORIES_AUDIENCE, STUDY_RULE_AUDIENCE, VIDEO, WEBSITE
    """
    params = {}
    if allowed_domains is not None:
        params["allowed_domains"] = allowed_domains
    if associated_audience_id is not None:
        params["associated_audience_id"] = associated_audience_id
    if claim_objective is not None:
        params["claim_objective"] = claim_objective
    if content_type is not None:
        params["content_type"] = content_type
    if creation_params is not None:
        params["creation_params"] = creation_params
    if description is not None:
        params["description"] = description
    if enable_fetch_or_create is not None:
        params["enable_fetch_or_create"] = enable_fetch_or_create
    if event_source_group is not None:
        params["event_source_group"] = event_source_group
    if event_sources is not None:
        params["event_sources"] = event_sources
    if exclusions is not None:
        params["exclusions"] = exclusions
    if inclusionOperator is not None:
        params["inclusionOperator"] = inclusionOperator
    if inclusions is not None:
        params["inclusions"] = inclusions
    if is_snapshot is not None:
        params["is_snapshot"] = is_snapshot
    if is_value_based is not None:
        params["is_value_based"] = is_value_based
    params["name"] = name
    if opt_out_link is not None:
        params["opt_out_link"] = opt_out_link
    if parent_audience_id is not None:
        params["parent_audience_id"] = parent_audience_id
    params["product_set_id"] = product_set_id
    if rev_share_policy_id is not None:
        params["rev_share_policy_id"] = rev_share_policy_id
    if subtype is not None:
        params["subtype"] = subtype
    result = await get_client().post(f"act_{account_id}/product_audiences", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_promote_pages(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /promote_pages on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/promote_pages", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_publisher_block_lists(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /publisher_block_lists on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/publisher_block_lists", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_publisher_block_lists(account_id: str, name: Optional[str] = None) -> str:
    """POST /publisher_block_lists on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        name: Optional.
    """
    params = {}
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"act_{account_id}/publisher_block_lists", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_reachestimate(
    ad_account_id: str,
    targeting_spec: str,
    fields: Optional[str] = None,
    adgroup_ids: Optional[str] = None,
    caller_id: Optional[str] = None,
    concepts: Optional[str] = None,
    creative_action_spec: Optional[str] = None,
    is_debug: Optional[bool] = None,
    object_store_url: Optional[str] = None,
) -> str:
    """GET /reachestimate on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        adgroup_ids: Optional.
        caller_id: Optional.
        concepts: Optional.
        creative_action_spec: Optional.
        is_debug: Optional.
        object_store_url: Optional.
        targeting_spec: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if adgroup_ids is not None:
        params["adgroup_ids"] = adgroup_ids
    if caller_id is not None:
        params["caller_id"] = caller_id
    if concepts is not None:
        params["concepts"] = concepts
    if creative_action_spec is not None:
        params["creative_action_spec"] = creative_action_spec
    if is_debug is not None:
        params["is_debug"] = is_debug
    if object_store_url is not None:
        params["object_store_url"] = object_store_url
    params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_account_id}/reachestimate", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_reachfrequencypredictions(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /reachfrequencypredictions on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/reachfrequencypredictions", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_reachfrequencypredictions(
    account_id: str,
    action: Optional[str] = None,
    ad_formats: Optional[str] = None,
    auction_entry_option_index: Optional[int] = None,
    budget: Optional[int] = None,
    buying_type: Optional[str] = None,
    campaign_group_id: Optional[str] = None,
    day_parting_schedule: Optional[str] = None,
    deal_id: Optional[str] = None,
    destination_id: Optional[int] = None,
    destination_ids: Optional[str] = None,
    end_time: Optional[int] = None,
    exceptions: Optional[bool] = None,
    existing_campaign_id: Optional[str] = None,
    expiration_time: Optional[int] = None,
    frequency_cap: Optional[int] = None,
    grp_buying: Optional[bool] = None,
    impression: Optional[int] = None,
    instream_packages: Optional[str] = None,
    interval_frequency_cap_reset_period: Optional[int] = None,
    is_balanced_frequency: Optional[bool] = None,
    is_bonus_media: Optional[bool] = None,
    is_conversion_goal: Optional[bool] = None,
    is_full_view: Optional[bool] = None,
    is_higher_average_frequency: Optional[bool] = None,
    is_reach_and_frequency_io_buying: Optional[bool] = None,
    is_reserved_buying: Optional[bool] = None,
    num_curve_points: Optional[int] = None,
    objective: Optional[str] = None,
    optimization_goal: Optional[str] = None,
    prediction_mode: Optional[int] = None,
    reach: Optional[int] = None,
    rf_prediction_id: Optional[str] = None,
    rf_prediction_id_to_release: Optional[str] = None,
    rf_prediction_id_to_share: Optional[str] = None,
    start_time: Optional[int] = None,
    stop_time: Optional[int] = None,
    story_event_type: Optional[int] = None,
    target_cpm: Optional[int] = None,
    target_frequency: Optional[int] = None,
    target_frequency_reset_period: Optional[int] = None,
    target_spec: Optional[str] = None,
    trending_topics_spec: Optional[str] = None,
    video_view_length_constraint: Optional[int] = None,
) -> str:
    """POST /reachfrequencypredictions on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        action: Optional. Values: cancel, quote, reserve
        ad_formats: Optional.
        auction_entry_option_index: Optional.
        budget: Optional.
        buying_type: Optional. Values: AUCTION, DEPRECATED_REACH_BLOCK, FIXED_CPM, MIXED, REACHBLOCK, RESEARCH_POLL, RESERVED
        campaign_group_id: Optional.
        day_parting_schedule: Optional.
        deal_id: Optional.
        destination_id: Optional.
        destination_ids: Optional.
        end_time: Optional.
        exceptions: Optional.
        existing_campaign_id: Optional.
        expiration_time: Optional.
        frequency_cap: Optional.
        grp_buying: Optional.
        impression: Optional.
        instream_packages: Optional. Values: BEAUTY, ENTERTAINMENT, FOOD, NORMAL, PREMIUM, REGULAR_ANIMALS_PETS, REGULAR_FOOD, REGULAR_GAMES, REGULAR_POLITICS, REGULAR_SPORTS, REGULAR_STYLE, REGULAR_TV_MOVIES, SPANISH, SPORTS
        interval_frequency_cap_reset_period: Optional.
        is_balanced_frequency: Optional.
        is_bonus_media: Optional.
        is_conversion_goal: Optional.
        is_full_view: Optional.
        is_higher_average_frequency: Optional.
        is_reach_and_frequency_io_buying: Optional.
        is_reserved_buying: Optional.
        num_curve_points: Optional.
        objective: Optional.
        optimization_goal: Optional.
        prediction_mode: Optional.
        reach: Optional.
        rf_prediction_id: Optional.
        rf_prediction_id_to_release: Optional.
        rf_prediction_id_to_share: Optional.
        start_time: Optional.
        stop_time: Optional.
        story_event_type: Optional.
        target_cpm: Optional.
        target_frequency: Optional.
        target_frequency_reset_period: Optional.
        target_spec: Optional.
        trending_topics_spec: Optional.
        video_view_length_constraint: Optional.
    """
    params = {}
    if action is not None:
        params["action"] = action
    if ad_formats is not None:
        params["ad_formats"] = ad_formats
    if auction_entry_option_index is not None:
        params["auction_entry_option_index"] = auction_entry_option_index
    if budget is not None:
        params["budget"] = budget
    if buying_type is not None:
        params["buying_type"] = buying_type
    if campaign_group_id is not None:
        params["campaign_group_id"] = campaign_group_id
    if day_parting_schedule is not None:
        params["day_parting_schedule"] = day_parting_schedule
    if deal_id is not None:
        params["deal_id"] = deal_id
    if destination_id is not None:
        params["destination_id"] = destination_id
    if destination_ids is not None:
        params["destination_ids"] = destination_ids
    if end_time is not None:
        params["end_time"] = end_time
    if exceptions is not None:
        params["exceptions"] = exceptions
    if existing_campaign_id is not None:
        params["existing_campaign_id"] = existing_campaign_id
    if expiration_time is not None:
        params["expiration_time"] = expiration_time
    if frequency_cap is not None:
        params["frequency_cap"] = frequency_cap
    if grp_buying is not None:
        params["grp_buying"] = grp_buying
    if impression is not None:
        params["impression"] = impression
    if instream_packages is not None:
        params["instream_packages"] = instream_packages
    if interval_frequency_cap_reset_period is not None:
        params["interval_frequency_cap_reset_period"] = interval_frequency_cap_reset_period
    if is_balanced_frequency is not None:
        params["is_balanced_frequency"] = is_balanced_frequency
    if is_bonus_media is not None:
        params["is_bonus_media"] = is_bonus_media
    if is_conversion_goal is not None:
        params["is_conversion_goal"] = is_conversion_goal
    if is_full_view is not None:
        params["is_full_view"] = is_full_view
    if is_higher_average_frequency is not None:
        params["is_higher_average_frequency"] = is_higher_average_frequency
    if is_reach_and_frequency_io_buying is not None:
        params["is_reach_and_frequency_io_buying"] = is_reach_and_frequency_io_buying
    if is_reserved_buying is not None:
        params["is_reserved_buying"] = is_reserved_buying
    if num_curve_points is not None:
        params["num_curve_points"] = num_curve_points
    if objective is not None:
        params["objective"] = objective
    if optimization_goal is not None:
        params["optimization_goal"] = optimization_goal
    if prediction_mode is not None:
        params["prediction_mode"] = prediction_mode
    if reach is not None:
        params["reach"] = reach
    if rf_prediction_id is not None:
        params["rf_prediction_id"] = rf_prediction_id
    if rf_prediction_id_to_release is not None:
        params["rf_prediction_id_to_release"] = rf_prediction_id_to_release
    if rf_prediction_id_to_share is not None:
        params["rf_prediction_id_to_share"] = rf_prediction_id_to_share
    if start_time is not None:
        params["start_time"] = start_time
    if stop_time is not None:
        params["stop_time"] = stop_time
    if story_event_type is not None:
        params["story_event_type"] = story_event_type
    if target_cpm is not None:
        params["target_cpm"] = target_cpm
    if target_frequency is not None:
        params["target_frequency"] = target_frequency
    if target_frequency_reset_period is not None:
        params["target_frequency_reset_period"] = target_frequency_reset_period
    if target_spec is not None:
        params["target_spec"] = target_spec
    if trending_topics_spec is not None:
        params["trending_topics_spec"] = trending_topics_spec
    if video_view_length_constraint is not None:
        params["video_view_length_constraint"] = video_view_length_constraint
    result = await get_client().post(f"act_{account_id}/reachfrequencypredictions", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_recommendations(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /recommendations on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/recommendations", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_recommendations(
    account_id: str,
    recommendation_signature: str,
    asc_fragmentation_parameters: Optional[str] = None,
    autoflow_parameters: Optional[str] = None,
    fragmentation_parameters: Optional[str] = None,
    music_parameters: Optional[str] = None,
    scale_good_campaign_parameters: Optional[str] = None,
) -> str:
    """POST /recommendations on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        asc_fragmentation_parameters: Optional.
        autoflow_parameters: Optional.
        fragmentation_parameters: Optional.
        music_parameters: Optional.
        recommendation_signature: Required.
        scale_good_campaign_parameters: Optional.
    """
    params = {}
    if asc_fragmentation_parameters is not None:
        params["asc_fragmentation_parameters"] = asc_fragmentation_parameters
    if autoflow_parameters is not None:
        params["autoflow_parameters"] = autoflow_parameters
    if fragmentation_parameters is not None:
        params["fragmentation_parameters"] = fragmentation_parameters
    if music_parameters is not None:
        params["music_parameters"] = music_parameters
    params["recommendation_signature"] = recommendation_signature
    if scale_good_campaign_parameters is not None:
        params["scale_good_campaign_parameters"] = scale_good_campaign_parameters
    result = await get_client().post(f"act_{account_id}/recommendations", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_saved_audiences(
    ad_account_id: str,
    business_id: Optional[str] = None,
    fields: Optional[str] = None,
    filtering: Optional[str] = None,
) -> str:
    """GET /saved_audiences on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        business_id: Optional.
        fields: Optional.
        filtering: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business_id is not None:
        params["business_id"] = business_id
    if fields is not None:
        params["fields"] = fields
    if filtering is not None:
        params["filtering"] = filtering
    result = await get_client().get(f"{ad_account_id}/saved_audiences", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_subscribed_apps(ad_account_id: str, app_id: Optional[str] = None) -> str:
    """DELETE /subscribed_apps on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        app_id: Optional.
    """
    params = {}
    if app_id is not None:
        params["app_id"] = app_id
    result = await get_client().delete(f"{ad_account_id}/subscribed_apps")
    return json.dumps(result, indent=2)


async def get_ad_account_subscribed_apps(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_apps on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/subscribed_apps", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_subscribed_apps(account_id: str, app_id: Optional[str] = None) -> str:
    """POST /subscribed_apps on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        app_id: Optional.
    """
    params = {}
    if app_id is not None:
        params["app_id"] = app_id
    result = await get_client().post(f"act_{account_id}/subscribed_apps", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_targetingbrowse(
    ad_account_id: str,
    fields: Optional[str] = None,
    excluded_category: Optional[str] = None,
    include_nodes: Optional[bool] = None,
    is_exclusion: Optional[bool] = None,
    limit_type: Optional[str] = None,
    regulated_categories: Optional[str] = None,
    regulated_countries: Optional[str] = None,
    whitelisted_types: Optional[str] = None,
) -> str:
    """GET /targetingbrowse on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        excluded_category: Optional.
        include_nodes: Optional.
        is_exclusion: Optional.
        limit_type: Optional. Values: behaviors, college_years, education_majors, education_schools, education_statuses, ethnic_affinity, family_statuses, generation, home_ownership, home_type, home_value, household_composition, income, industries, interested_in, interests, life_events, location_categories, moms, net_worth, office_type, politics, relationship_statuses, user_adclusters, work_employers, work_positions
        regulated_categories: Optional. Values: CREDIT, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, HOUSING, ISSUES_ELECTIONS_POLITICS, NONE, ONLINE_GAMBLING_AND_GAMING
        regulated_countries: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        whitelisted_types: Optional. Values: adgroup_id, age_max, age_min, age_range, alternate_auto_targeting_option, app_install_state, audience_network_positions, behaviors, brand_safety_content_filter_levels, brand_safety_content_severity_levels, cafe_ca_contraction_targeting_signal, cafe_ca_expansion_targeting_signal, catalog_based_targeting, cities, city_keys, college_years, conjunctive_user_adclusters, connections, contextual_targeting_categories, countries, country, country_groups, custom_audiences, device_platforms, direct_install_devices, dt_consolidation_state, dynamic_audience_ids, education_majors, education_schools, education_statuses, effective_audience_network_positions, effective_device_platforms, effective_facebook_positions, effective_instagram_positions, effective_messenger_positions, effective_oculus_positions, effective_publisher_platforms, effective_threads_positions, effective_whatsapp_positions, engagement_specs, ethnic_affinity, exclude_previous_days, exclude_reached_since, excluded_brand_safety_content_types, excluded_connections, excluded_custom_audiences, excluded_dynamic_audience_ids, excluded_engagement_specs, excluded_geo_locations, excluded_mobile_device_model, excluded_product_audience_specs, excluded_publisher_categories, excluded_publisher_list_ids, excluded_user_adclusters, excluded_user_device, exclusions, expanded_implicit_custom_audiences, facebook_positions, family_statuses, fb_deal_id, flexible_spec, follow_profiles, follow_profiles_negative, format, friends_of_connections, gatekeepers, genders, generation, geo_locations, home_ownership, home_type, home_value, household_composition, household_income, id, income, industries, instagram_hashtags, instagram_positions, install_state_application, instream_video_skippable_excluded, instream_video_sponsorship_placements, interest_defaults_source, interested_in, interests, is_instagram_destination_ad, is_whatsapp_destination_ad, keywords, life_events, locales, location_categories, location_cluster_ids, location_expansion, marketing_message_channels, marketplace_product_categories, messenger_positions, mobile_device_model, moms, net_worth, oculus_positions, office_type, page_types, place_page_set_ids, political_views, politics, product_audience_specs, prospecting_audience, publisher_platforms, radius, region_keys, regions, relationship_statuses, rtb_flag, site_category, subscriber_universe, tafe_ca_mitigation_strategy, targeting_automation, targeting_optimization, targeting_relaxation_types, threads_positions, timezones, topic, trending, user_adclusters, user_age_unknown, user_device, user_event, user_os, user_page_threads, user_page_threads_excluded, whatsapp_positions, wireless_carrier, work_employers, work_positions, zips
    """
    params = {}
    params["fields"] = fields or "id,name"
    if excluded_category is not None:
        params["excluded_category"] = excluded_category
    if include_nodes is not None:
        params["include_nodes"] = include_nodes
    if is_exclusion is not None:
        params["is_exclusion"] = is_exclusion
    if limit_type is not None:
        params["limit_type"] = limit_type
    if regulated_categories is not None:
        params["regulated_categories"] = regulated_categories
    if regulated_countries is not None:
        params["regulated_countries"] = regulated_countries
    if whitelisted_types is not None:
        params["whitelisted_types"] = whitelisted_types
    result = await get_client().get(f"{ad_account_id}/targetingbrowse", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_targetingsearch(
    ad_account_id: str,
    q: str,
    fields: Optional[str] = None,
    allow_only_fat_head_interests: Optional[bool] = None,
    app_store: Optional[str] = None,
    countries: Optional[str] = None,
    is_account_level_brand_safety_exclusion: Optional[bool] = None,
    is_account_level_employer_exclusion: Optional[bool] = None,
    is_exclusion: Optional[bool] = None,
    limit_type: Optional[str] = None,
    objective: Optional[str] = None,
    promoted_object: Optional[str] = None,
    regulated_categories: Optional[str] = None,
    regulated_countries: Optional[str] = None,
    session_id: Optional[int] = None,
    targeting_list: Optional[str] = None,
    whitelisted_types: Optional[str] = None,
) -> str:
    """GET /targetingsearch on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        allow_only_fat_head_interests: Optional.
        app_store: Optional. Values: all_app_stores_for_android_and_ios, amazon_app_store, apk_mirror, apk_monk, apk_pure, aptoide_a1_store, bemobi_mobile_store, digital_turbine_store, does_not_exist, fb_android_store, fb_canvas, fb_gameroom, galaxy_store, google_play, instant_game, itunes, itunes_ipad, neon_android_store, none, oculus_app_store, oppo, roku_channel_store, uptodown, vivo, windows_10_store, windows_store, xiaomi
        countries: Optional.
        is_account_level_brand_safety_exclusion: Optional.
        is_account_level_employer_exclusion: Optional.
        is_exclusion: Optional.
        limit_type: Optional. Values: adgroup_id, age_max, age_min, age_range, alternate_auto_targeting_option, app_install_state, audience_network_positions, behaviors, brand_safety_content_filter_levels, brand_safety_content_severity_levels, cafe_ca_contraction_targeting_signal, cafe_ca_expansion_targeting_signal, catalog_based_targeting, cities, city_keys, college_years, conjunctive_user_adclusters, connections, contextual_targeting_categories, countries, country, country_groups, custom_audiences, device_platforms, direct_install_devices, dt_consolidation_state, dynamic_audience_ids, education_majors, education_schools, education_statuses, effective_audience_network_positions, effective_device_platforms, effective_facebook_positions, effective_instagram_positions, effective_messenger_positions, effective_oculus_positions, effective_publisher_platforms, effective_threads_positions, effective_whatsapp_positions, engagement_specs, ethnic_affinity, exclude_previous_days, exclude_reached_since, excluded_brand_safety_content_types, excluded_connections, excluded_custom_audiences, excluded_dynamic_audience_ids, excluded_engagement_specs, excluded_geo_locations, excluded_mobile_device_model, excluded_product_audience_specs, excluded_publisher_categories, excluded_publisher_list_ids, excluded_user_adclusters, excluded_user_device, exclusions, expanded_implicit_custom_audiences, facebook_positions, family_statuses, fb_deal_id, flexible_spec, follow_profiles, follow_profiles_negative, format, friends_of_connections, gatekeepers, genders, generation, geo_locations, home_ownership, home_type, home_value, household_composition, household_income, id, income, industries, instagram_hashtags, instagram_positions, install_state_application, instream_video_skippable_excluded, instream_video_sponsorship_placements, interest_defaults_source, interested_in, interests, is_instagram_destination_ad, is_whatsapp_destination_ad, keywords, life_events, locales, location_categories, location_cluster_ids, location_expansion, marketing_message_channels, marketplace_product_categories, messenger_positions, mobile_device_model, moms, net_worth, oculus_positions, office_type, page_types, place_page_set_ids, political_views, politics, product_audience_specs, prospecting_audience, publisher_platforms, radius, region_keys, regions, relationship_statuses, rtb_flag, site_category, subscriber_universe, tafe_ca_mitigation_strategy, targeting_automation, targeting_optimization, targeting_relaxation_types, threads_positions, timezones, topic, trending, user_adclusters, user_age_unknown, user_device, user_event, user_os, user_page_threads, user_page_threads_excluded, whatsapp_positions, wireless_carrier, work_employers, work_positions, zips
        objective: Optional. Values: APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS
        promoted_object: Optional.
        q: Required.
        regulated_categories: Optional. Values: CREDIT, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, HOUSING, ISSUES_ELECTIONS_POLITICS, NONE, ONLINE_GAMBLING_AND_GAMING
        regulated_countries: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        session_id: Optional.
        targeting_list: Optional.
        whitelisted_types: Optional. Values: adgroup_id, age_max, age_min, age_range, alternate_auto_targeting_option, app_install_state, audience_network_positions, behaviors, brand_safety_content_filter_levels, brand_safety_content_severity_levels, cafe_ca_contraction_targeting_signal, cafe_ca_expansion_targeting_signal, catalog_based_targeting, cities, city_keys, college_years, conjunctive_user_adclusters, connections, contextual_targeting_categories, countries, country, country_groups, custom_audiences, device_platforms, direct_install_devices, dt_consolidation_state, dynamic_audience_ids, education_majors, education_schools, education_statuses, effective_audience_network_positions, effective_device_platforms, effective_facebook_positions, effective_instagram_positions, effective_messenger_positions, effective_oculus_positions, effective_publisher_platforms, effective_threads_positions, effective_whatsapp_positions, engagement_specs, ethnic_affinity, exclude_previous_days, exclude_reached_since, excluded_brand_safety_content_types, excluded_connections, excluded_custom_audiences, excluded_dynamic_audience_ids, excluded_engagement_specs, excluded_geo_locations, excluded_mobile_device_model, excluded_product_audience_specs, excluded_publisher_categories, excluded_publisher_list_ids, excluded_user_adclusters, excluded_user_device, exclusions, expanded_implicit_custom_audiences, facebook_positions, family_statuses, fb_deal_id, flexible_spec, follow_profiles, follow_profiles_negative, format, friends_of_connections, gatekeepers, genders, generation, geo_locations, home_ownership, home_type, home_value, household_composition, household_income, id, income, industries, instagram_hashtags, instagram_positions, install_state_application, instream_video_skippable_excluded, instream_video_sponsorship_placements, interest_defaults_source, interested_in, interests, is_instagram_destination_ad, is_whatsapp_destination_ad, keywords, life_events, locales, location_categories, location_cluster_ids, location_expansion, marketing_message_channels, marketplace_product_categories, messenger_positions, mobile_device_model, moms, net_worth, oculus_positions, office_type, page_types, place_page_set_ids, political_views, politics, product_audience_specs, prospecting_audience, publisher_platforms, radius, region_keys, regions, relationship_statuses, rtb_flag, site_category, subscriber_universe, tafe_ca_mitigation_strategy, targeting_automation, targeting_optimization, targeting_relaxation_types, threads_positions, timezones, topic, trending, user_adclusters, user_age_unknown, user_device, user_event, user_os, user_page_threads, user_page_threads_excluded, whatsapp_positions, wireless_carrier, work_employers, work_positions, zips
    """
    params = {}
    params["fields"] = fields or "id,name"
    if allow_only_fat_head_interests is not None:
        params["allow_only_fat_head_interests"] = allow_only_fat_head_interests
    if app_store is not None:
        params["app_store"] = app_store
    if countries is not None:
        params["countries"] = countries
    if is_account_level_brand_safety_exclusion is not None:
        params["is_account_level_brand_safety_exclusion"] = is_account_level_brand_safety_exclusion
    if is_account_level_employer_exclusion is not None:
        params["is_account_level_employer_exclusion"] = is_account_level_employer_exclusion
    if is_exclusion is not None:
        params["is_exclusion"] = is_exclusion
    if limit_type is not None:
        params["limit_type"] = limit_type
    if objective is not None:
        params["objective"] = objective
    if promoted_object is not None:
        params["promoted_object"] = promoted_object
    params["q"] = q
    if regulated_categories is not None:
        params["regulated_categories"] = regulated_categories
    if regulated_countries is not None:
        params["regulated_countries"] = regulated_countries
    if session_id is not None:
        params["session_id"] = session_id
    if targeting_list is not None:
        params["targeting_list"] = targeting_list
    if whitelisted_types is not None:
        params["whitelisted_types"] = whitelisted_types
    result = await get_client().get(f"{ad_account_id}/targetingsearch", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_targetingsentencelines(
    ad_account_id: str,
    targeting_spec: str,
    fields: Optional[str] = None,
    discard_ages: Optional[bool] = None,
    discard_placements: Optional[bool] = None,
    hide_targeting_spec_from_return: Optional[bool] = None,
) -> str:
    """GET /targetingsentencelines on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        discard_ages: Optional.
        discard_placements: Optional.
        hide_targeting_spec_from_return: Optional.
        targeting_spec: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if discard_ages is not None:
        params["discard_ages"] = discard_ages
    if discard_placements is not None:
        params["discard_placements"] = discard_placements
    if hide_targeting_spec_from_return is not None:
        params["hide_targeting_spec_from_return"] = hide_targeting_spec_from_return
    params["targeting_spec"] = targeting_spec
    result = await get_client().get(f"{ad_account_id}/targetingsentencelines", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_targetingsuggestions(
    ad_account_id: str,
    fields: Optional[str] = None,
    app_store: Optional[str] = None,
    countries: Optional[str] = None,
    limit_type: Optional[str] = None,
    mode: Optional[str] = None,
    objective: Optional[str] = None,
    objects: Optional[str] = None,
    regulated_categories: Optional[str] = None,
    regulated_countries: Optional[str] = None,
    session_id: Optional[int] = None,
    targeting_list: Optional[str] = None,
    whitelisted_types: Optional[str] = None,
) -> str:
    """GET /targetingsuggestions on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        app_store: Optional. Values: all_app_stores_for_android_and_ios, amazon_app_store, apk_mirror, apk_monk, apk_pure, aptoide_a1_store, bemobi_mobile_store, digital_turbine_store, does_not_exist, fb_android_store, fb_canvas, fb_gameroom, galaxy_store, google_play, instant_game, itunes, itunes_ipad, neon_android_store, none, oculus_app_store, oppo, roku_channel_store, uptodown, vivo, windows_10_store, windows_store, xiaomi
        countries: Optional.
        limit_type: Optional. Values: behaviors, college_years, education_majors, education_schools, education_statuses, family_statuses, home_value, income, industries, interested_in, interests, life_events, location_categories, relationship_statuses, user_adclusters, work_employers, work_positions
        mode: Optional. Values: best_performing, recently_used, related, suggestions
        objective: Optional. Values: APP_INSTALLS, BRAND_AWARENESS, CONVERSIONS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, OUTCOME_APP_PROMOTION, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS
        objects: Optional.
        regulated_categories: Optional. Values: CREDIT, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, HOUSING, ISSUES_ELECTIONS_POLITICS, NONE, ONLINE_GAMBLING_AND_GAMING
        regulated_countries: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        session_id: Optional.
        targeting_list: Optional.
        whitelisted_types: Optional. Values: behaviors, college_years, education_majors, education_schools, education_statuses, family_statuses, home_value, income, industries, interested_in, interests, life_events, location_categories, relationship_statuses, user_adclusters, work_employers, work_positions
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app_store is not None:
        params["app_store"] = app_store
    if countries is not None:
        params["countries"] = countries
    if limit_type is not None:
        params["limit_type"] = limit_type
    if mode is not None:
        params["mode"] = mode
    if objective is not None:
        params["objective"] = objective
    if objects is not None:
        params["objects"] = objects
    if regulated_categories is not None:
        params["regulated_categories"] = regulated_categories
    if regulated_countries is not None:
        params["regulated_countries"] = regulated_countries
    if session_id is not None:
        params["session_id"] = session_id
    if targeting_list is not None:
        params["targeting_list"] = targeting_list
    if whitelisted_types is not None:
        params["whitelisted_types"] = whitelisted_types
    result = await get_client().get(f"{ad_account_id}/targetingsuggestions", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_targetingvalidation(
    ad_account_id: str,
    fields: Optional[str] = None,
    id_list: Optional[str] = None,
    is_exclusion: Optional[bool] = None,
    name_list: Optional[str] = None,
    targeting_list: Optional[str] = None,
) -> str:
    """GET /targetingvalidation on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        id_list: Optional.
        is_exclusion: Optional.
        name_list: Optional.
        targeting_list: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if id_list is not None:
        params["id_list"] = id_list
    if is_exclusion is not None:
        params["is_exclusion"] = is_exclusion
    if name_list is not None:
        params["name_list"] = name_list
    if targeting_list is not None:
        params["targeting_list"] = targeting_list
    result = await get_client().get(f"{ad_account_id}/targetingvalidation", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_tracking(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /tracking on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/tracking", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_tracking(account_id: str, tracking_specs: str) -> str:
    """POST /tracking on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        tracking_specs: Required.
    """
    params = {}
    params["tracking_specs"] = tracking_specs
    result = await get_client().post(f"act_{account_id}/tracking", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_users(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /users on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}/users", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_account_usersofanyaudience(
    ad_account_id: str,
    namespace: Optional[str] = None,
    payload: Optional[str] = None,
    session: Optional[str] = None,
) -> str:
    """DELETE /usersofanyaudience on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        namespace: Optional.
        payload: Optional.
        session: Optional.
    """
    params = {}
    if namespace is not None:
        params["namespace"] = namespace
    if payload is not None:
        params["payload"] = payload
    if session is not None:
        params["session"] = session
    result = await get_client().delete(f"{ad_account_id}/usersofanyaudience")
    return json.dumps(result, indent=2)


async def get_ad_account_value_rule_set(
    ad_account_id: str,
    fields: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """GET /value_rule_set on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        product_type: Optional. Values: AUDIENCE, LEADGEN_ADS, OMNI_CHANNEL
        status: Optional. Values: ACTIVE, DELETED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if product_type is not None:
        params["product_type"] = product_type
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{ad_account_id}/value_rule_set", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_value_rule_set(account_id: str, name: str, rules: str, product_type: Optional[str] = None) -> str:
    """POST /value_rule_set on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        name: Required.
        product_type: Optional. Values: AUDIENCE, LEADGEN_ADS, OMNI_CHANNEL
        rules: Required.
    """
    params = {}
    params["name"] = name
    if product_type is not None:
        params["product_type"] = product_type
    params["rules"] = rules
    result = await get_client().post(f"act_{account_id}/value_rule_set", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account_video_ads(
    ad_account_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /video_ads on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{ad_account_id}/video_ads", params=params)
    return json.dumps(result, indent=2)


async def create_ad_account_video_ads(
    account_id: str,
    upload_phase: str,
    description: Optional[str] = None,
    privacy: Optional[str] = None,
    title: Optional[str] = None,
    video_id: Optional[str] = None,
    video_state: Optional[str] = None,
) -> str:
    """POST /video_ads on AdAccount.

    Args:
        account_id: The ID of the AdAccount object.
        description: Optional.
        privacy: Optional.
        title: Optional.
        upload_phase: Required. Values: FINISH, START
        video_id: Optional.
        video_state: Optional. Values: DRAFT, PUBLISHED, SCHEDULED
    """
    params = {}
    if description is not None:
        params["description"] = description
    if privacy is not None:
        params["privacy"] = privacy
    if title is not None:
        params["title"] = title
    params["upload_phase"] = upload_phase
    if video_id is not None:
        params["video_id"] = video_id
    if video_state is not None:
        params["video_state"] = video_state
    result = await get_client().post(f"act_{account_id}/video_ads", data=params)
    return json.dumps(result, indent=2)


async def get_ad_account(ad_account_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        fields: Comma-separated list of fields to return. Available: account_id, account_status, ad_account_promotable_objects, age, agency_client_declaration, all_capabilities, amount_spent, attribution_spec, balance, brand_safety_content_filter_levels, business, business_city, business_country_code, business_name, business_state, business_street, business_street2, business_zip, can_create_brand_lift_study, capabilities, created_time, currency, custom_audience_info, default_dsa_beneficiary, default_dsa_payor, disable_reason, end_advertiser, end_advertiser_name, existing_customers, expired_funding_source_details, extended_credit_invoice_group, failed_delivery_checks, fb_entity, funding_source, funding_source_details, has_migrated_permissions, has_page_authorized_adaccount, id, io_number, is_attribution_spec_system_default, is_ba_skip_delayed_eligible, is_direct_deals_enabled, is_in_3ds_authorization_enabled_market, is_notifications_enabled, is_personal, is_prepay_account, is_tax_id_required, liable_address, line_numbers, media_agency, min_campaign_group_spend_cap, min_daily_budget, name, offsite_pixels_tos_accepted, opportunity_score, owner, owner_business, partner, rf_spec, send_bill_to_address, show_checkout_experience, sold_to_address, spend_cap, tax_id, tax_id_status, tax_id_type, timezone_id, timezone_name, timezone_offset_hours_utc, tos_accepted, user_access_expire_time, user_tasks, user_tos_accepted, viewable_business
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_account(
    ad_account_id: str,
    agency_client_declaration: Optional[str] = None,
    attribution_spec: Optional[str] = None,
    business_info: Optional[str] = None,
    currency: Optional[str] = None,
    custom_audience_info: Optional[str] = None,
    default_dsa_beneficiary: Optional[str] = None,
    default_dsa_payor: Optional[str] = None,
    end_advertiser: Optional[str] = None,
    existing_customers: Optional[str] = None,
    is_ba_skip_delayed_eligible: Optional[bool] = None,
    is_notifications_enabled: Optional[bool] = None,
    media_agency: Optional[str] = None,
    name: Optional[str] = None,
    partner: Optional[str] = None,
    spend_cap: Optional[float] = None,
    spend_cap_action: Optional[str] = None,
    timezone_id: Optional[int] = None,
    tos_accepted: Optional[str] = None,
) -> str:
    """POST /#update on AdAccount.

    Args:
        ad_account_id: The ID of the AdAccount object.
        agency_client_declaration: Optional.
        attribution_spec: Optional.
        business_info: Optional.
        currency: Optional.
        custom_audience_info: Optional.
        default_dsa_beneficiary: Optional.
        default_dsa_payor: Optional.
        end_advertiser: Optional.
        existing_customers: Optional.
        is_ba_skip_delayed_eligible: Optional.
        is_notifications_enabled: Optional.
        media_agency: Optional.
        name: Optional.
        partner: Optional.
        spend_cap: Optional.
        spend_cap_action: Optional.
        timezone_id: Optional.
        tos_accepted: Optional.
    """
    params = {}
    if agency_client_declaration is not None:
        params["agency_client_declaration"] = agency_client_declaration
    if attribution_spec is not None:
        params["attribution_spec"] = attribution_spec
    if business_info is not None:
        params["business_info"] = business_info
    if currency is not None:
        params["currency"] = currency
    if custom_audience_info is not None:
        params["custom_audience_info"] = custom_audience_info
    if default_dsa_beneficiary is not None:
        params["default_dsa_beneficiary"] = default_dsa_beneficiary
    if default_dsa_payor is not None:
        params["default_dsa_payor"] = default_dsa_payor
    if end_advertiser is not None:
        params["end_advertiser"] = end_advertiser
    if existing_customers is not None:
        params["existing_customers"] = existing_customers
    if is_ba_skip_delayed_eligible is not None:
        params["is_ba_skip_delayed_eligible"] = is_ba_skip_delayed_eligible
    if is_notifications_enabled is not None:
        params["is_notifications_enabled"] = is_notifications_enabled
    if media_agency is not None:
        params["media_agency"] = media_agency
    if name is not None:
        params["name"] = name
    if partner is not None:
        params["partner"] = partner
    if spend_cap is not None:
        params["spend_cap"] = spend_cap
    if spend_cap_action is not None:
        params["spend_cap_action"] = spend_cap_action
    if timezone_id is not None:
        params["timezone_id"] = timezone_id
    if tos_accepted is not None:
        params["tos_accepted"] = tos_accepted
    result = await get_client().post(f"{ad_account_id}", data=params)
    return json.dumps(result, indent=2)


AD_ACCOUNT_CREATION_REQUEST_FIELDS = [
    "ad_accounts_currency",
    "ad_accounts_info",
    "additional_comment",
    "address_in_chinese",
    "address_in_english",
    "address_in_local_language",
    "advertiser_business",
    "appeal_reason",
    "business",
    "business_registration_id",
    "chinese_legal_entity_name",
    "contact",
    "creator",
    "credit_card_id",
    "disapproval_reasons",
    "english_legal_entity_name",
    "extended_credit_id",
    "id",
    "is_smb",
    "is_test",
    "legal_entity_name_in_local_language",
    "oe_request_id",
    "official_website_url",
    "planning_agency_business",
    "planning_agency_business_id",
    "promotable_app_ids",
    "promotable_page_ids",
    "promotable_urls",
    "request_change_reasons",
    "status",
    "subvertical",
    "subvertical_v2",
    "time_created",
    "vertical",
    "vertical_v2"
]


async def get_ad_account_creation_request_adaccounts(ad_account_creation_request_id: str, fields: Optional[str] = None) -> str:
    """GET /adaccounts on AdAccountCreationRequest.

    Args:
        ad_account_creation_request_id: The ID of the AdAccountCreationRequest object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_creation_request_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_ad_account_creation_request(ad_account_creation_request_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdAccountCreationRequest.

    Args:
        ad_account_creation_request_id: The ID of the AdAccountCreationRequest object.
        fields: Comma-separated list of fields to return. Available: ad_accounts_currency, ad_accounts_info, additional_comment, address_in_chinese, address_in_english, address_in_local_language, advertiser_business, appeal_reason, business, business_registration_id, chinese_legal_entity_name, contact, creator, credit_card_id, disapproval_reasons, english_legal_entity_name, extended_credit_id, id, is_smb, is_test, legal_entity_name_in_local_language, oe_request_id, official_website_url, planning_agency_business, planning_agency_business_id, promotable_app_ids, promotable_page_ids, promotable_urls, request_change_reasons, status, subvertical, subvertical_v2, time_created, vertical, vertical_v2
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_account_creation_request_id}", params=params)
    return json.dumps(result, indent=2)

