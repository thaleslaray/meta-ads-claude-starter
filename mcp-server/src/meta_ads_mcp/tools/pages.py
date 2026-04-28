"""Auto-generated Meta Marketing API tools — pages."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


PAGE_FIELDS = [
    "about",
    "access_token",
    "ad_campaign",
    "affiliation",
    "app_id",
    "artists_we_like",
    "attire",
    "available_promo_offer_ids",
    "awards",
    "band_interests",
    "band_members",
    "best_page",
    "bio",
    "birthday",
    "booking_agent",
    "breaking_news_usage",
    "built",
    "business",
    "can_checkin",
    "can_post",
    "category",
    "category_list",
    "checkins",
    "company_overview",
    "connected_instagram_account",
    "connected_page_backed_instagram_account",
    "contact_address",
    "copyright_attribution_insights",
    "copyright_whitelisted_ig_partners",
    "country_page_likes",
    "cover",
    "culinary_team",
    "current_location",
    "delivery_and_pickup_option_info",
    "description",
    "description_html",
    "differently_open_offerings",
    "directed_by",
    "display_subtext",
    "displayed_message_response_time",
    "does_viewer_have_page_permission_link_ig",
    "emails",
    "engagement",
    "fan_count",
    "featured_video",
    "features",
    "followers_count",
    "food_styles",
    "founded",
    "general_info",
    "general_manager",
    "genre",
    "global_brand_page_name",
    "global_brand_root_id",
    "has_added_app",
    "has_lead_access",
    "has_transitioned_to_new_page_experience",
    "has_whatsapp_business_number",
    "has_whatsapp_number",
    "hometown",
    "hours",
    "id",
    "impressum",
    "influences",
    "instagram_business_account",
    "is_always_open",
    "is_calling_eligible",
    "is_chain",
    "is_community_page",
    "is_eligible_for_branded_content",
    "is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web",
    "is_messenger_bot_get_started_enabled",
    "is_messenger_platform_bot",
    "is_owned",
    "is_permanently_closed",
    "is_published",
    "is_unclaimed",
    "is_verified",
    "is_webhooks_subscribed",
    "keywords",
    "leadgen_tos_acceptance_time",
    "leadgen_tos_accepted",
    "leadgen_tos_accepting_user",
    "link",
    "location",
    "members",
    "merchant_id",
    "merchant_review_status",
    "messaging_feature_status",
    "messenger_ads_default_icebreakers",
    "messenger_ads_default_quick_replies",
    "messenger_ads_quick_replies_type",
    "mini_shop_storefront",
    "mission",
    "mpg",
    "name",
    "name_with_location_descriptor",
    "network",
    "new_like_count",
    "offer_eligible",
    "overall_star_rating",
    "owner_business",
    "page_token",
    "parent_page",
    "parking",
    "payment_options",
    "personal_info",
    "personal_interests",
    "pharma_safety_info",
    "phone",
    "pickup_options",
    "place_type",
    "plot_outline",
    "preferred_audience",
    "press_contact",
    "price_range",
    "privacy_info_url",
    "produced_by",
    "products",
    "promotion_eligible",
    "promotion_ineligible_reason",
    "public_transit",
    "rating_count",
    "recipient",
    "record_label",
    "release_date",
    "restaurant_services",
    "restaurant_specialties",
    "schedule",
    "screenplay_by",
    "season",
    "single_line_address",
    "starring",
    "start_info",
    "store_code",
    "store_location_descriptor",
    "store_number",
    "studio",
    "supports_donate_button_in_live_video",
    "talking_about_count",
    "temporary_status",
    "unread_message_count",
    "unread_notif_count",
    "unseen_message_count",
    "user_access_expire_time",
    "username",
    "verification_status",
    "voip_info",
    "website",
    "were_here_count",
    "whatsapp_number",
    "written_by"
]


async def get_page_ab_tests(page_id: str, fields: Optional[str] = None) -> str:
    """GET /ab_tests on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/ab_tests", params=params)
    return json.dumps(result, indent=2)


async def create_page_ab_tests(
    page_id: str,
    control_video_id: str,
    description: str,
    duration: int,
    experiment_video_ids: str,
    name: str,
    optimization_goal: str,
    scheduled_experiment_timestamp: Optional[int] = None,
) -> str:
    """POST /ab_tests on Page.

    Args:
        page_id: The ID of the Page object.
        control_video_id: Required.
        description: Required.
        duration: Required.
        experiment_video_ids: Required.
        name: Required.
        optimization_goal: Required. Values: AUTO_RESOLVE_TO_CONTROL, AVG_TIME_WATCHED, COMMENTS, IMPRESSIONS, IMPRESSIONS_UNIQUE, LINK_CLICKS, OTHER, REACTIONS, REELS_PLAYS, SHARES, VIDEO_VIEWS_60S
        scheduled_experiment_timestamp: Optional.
    """
    params = {}
    params["control_video_id"] = control_video_id
    params["description"] = description
    params["duration"] = duration
    params["experiment_video_ids"] = experiment_video_ids
    params["name"] = name
    params["optimization_goal"] = optimization_goal
    if scheduled_experiment_timestamp is not None:
        params["scheduled_experiment_timestamp"] = scheduled_experiment_timestamp
    result = await get_client().post(f"{page_id}/ab_tests", data=params)
    return json.dumps(result, indent=2)


async def create_page_acknowledge_orders(page_id: str, idempotency_key: str, orders: str) -> str:
    """POST /acknowledge_orders on Page.

    Args:
        page_id: The ID of the Page object.
        idempotency_key: Required.
        orders: Required.
    """
    params = {}
    params["idempotency_key"] = idempotency_key
    params["orders"] = orders
    result = await get_client().post(f"{page_id}/acknowledge_orders", data=params)
    return json.dumps(result, indent=2)


async def get_page_ads_eligibility(page_id: str, fields: Optional[str] = None, ads_account_id: Optional[str] = None) -> str:
    """GET /ads_eligibility on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        ads_account_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ads_account_id is not None:
        params["ads_account_id"] = ads_account_id
    result = await get_client().get(f"{page_id}/ads_eligibility", params=params)
    return json.dumps(result, indent=2)


async def get_page_ads_posts(
    page_id: str,
    fields: Optional[str] = None,
    exclude_dynamic_ads: Optional[bool] = None,
    include_inline_create: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /ads_posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        exclude_dynamic_ads: Optional.
        include_inline_create: Optional.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if exclude_dynamic_ads is not None:
        params["exclude_dynamic_ads"] = exclude_dynamic_ads
    if include_inline_create is not None:
        params["include_inline_create"] = include_inline_create
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{page_id}/ads_posts", params=params)
    return json.dumps(result, indent=2)


async def delete_page_agencies(page_id: str, business: str) -> str:
    """DELETE /agencies on Page.

    Args:
        page_id: The ID of the Page object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{page_id}/agencies")
    return json.dumps(result, indent=2)


async def get_page_agencies(page_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_page_agencies(page_id: str, business: str, permitted_tasks: Optional[str] = None) -> str:
    """POST /agencies on Page.

    Args:
        page_id: The ID of the Page object.
        business: Required.
        permitted_tasks: Optional. Values: ADVERTISE, ANALYZE, CASHIER_ROLE, CREATE_CONTENT, GLOBAL_STRUCTURE_MANAGEMENT, MANAGE, MANAGE_JOBS, MANAGE_LEADS, MESSAGING, MODERATE, MODERATE_COMMUNITY, PAGES_MESSAGING, PAGES_MESSAGING_SUBSCRIPTIONS, PROFILE_PLUS_ADVERTISE, PROFILE_PLUS_ANALYZE, PROFILE_PLUS_CREATE_CONTENT, PROFILE_PLUS_FACEBOOK_ACCESS, PROFILE_PLUS_FULL_CONTROL, PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT, PROFILE_PLUS_MANAGE, PROFILE_PLUS_MANAGE_LEADS, PROFILE_PLUS_MESSAGING, PROFILE_PLUS_MODERATE, PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY, PROFILE_PLUS_REVENUE, READ_PAGE_MAILBOXES, VIEW_MONETIZATION_INSIGHTS
    """
    params = {}
    params["business"] = business
    if permitted_tasks is not None:
        params["permitted_tasks"] = permitted_tasks
    result = await get_client().post(f"{page_id}/agencies", data=params)
    return json.dumps(result, indent=2)


async def get_page_albums(page_id: str, fields: Optional[str] = None) -> str:
    """GET /albums on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/albums", params=params)
    return json.dumps(result, indent=2)


async def get_page_ar_experience(page_id: str, fields: Optional[str] = None) -> str:
    """GET /ar_experience on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/ar_experience", params=params)
    return json.dumps(result, indent=2)


async def delete_page_assigned_users(page_id: str, user: int) -> str:
    """DELETE /assigned_users on Page.

    Args:
        page_id: The ID of the Page object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{page_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_page_assigned_users(page_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{page_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_page_assigned_users(page_id: str, user: int, tasks: Optional[str] = None) -> str:
    """POST /assigned_users on Page.

    Args:
        page_id: The ID of the Page object.
        tasks: Optional. Values: ADVERTISE, ANALYZE, CASHIER_ROLE, CREATE_CONTENT, GLOBAL_STRUCTURE_MANAGEMENT, MANAGE, MANAGE_JOBS, MANAGE_LEADS, MESSAGING, MODERATE, MODERATE_COMMUNITY, PAGES_MESSAGING, PAGES_MESSAGING_SUBSCRIPTIONS, PROFILE_PLUS_ADVERTISE, PROFILE_PLUS_ANALYZE, PROFILE_PLUS_CREATE_CONTENT, PROFILE_PLUS_FACEBOOK_ACCESS, PROFILE_PLUS_FULL_CONTROL, PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT, PROFILE_PLUS_MANAGE, PROFILE_PLUS_MANAGE_LEADS, PROFILE_PLUS_MESSAGING, PROFILE_PLUS_MODERATE, PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY, PROFILE_PLUS_REVENUE, READ_PAGE_MAILBOXES, VIEW_MONETIZATION_INSIGHTS
        user: Required.
    """
    params = {}
    if tasks is not None:
        params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"{page_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def delete_page_blocked(
    page_id: str,
    asid: Optional[str] = None,
    psid: Optional[int] = None,
    uid: Optional[int] = None,
    user: Optional[int] = None,
) -> str:
    """DELETE /blocked on Page.

    Args:
        page_id: The ID of the Page object.
        asid: Optional.
        psid: Optional.
        uid: Optional.
        user: Optional.
    """
    params = {}
    if asid is not None:
        params["asid"] = asid
    if psid is not None:
        params["psid"] = psid
    if uid is not None:
        params["uid"] = uid
    if user is not None:
        params["user"] = user
    result = await get_client().delete(f"{page_id}/blocked")
    return json.dumps(result, indent=2)


async def get_page_blocked(
    page_id: str,
    fields: Optional[str] = None,
    uid: Optional[int] = None,
    user: Optional[int] = None,
) -> str:
    """GET /blocked on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        uid: Optional.
        user: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if uid is not None:
        params["uid"] = uid
    if user is not None:
        params["user"] = user
    result = await get_client().get(f"{page_id}/blocked", params=params)
    return json.dumps(result, indent=2)


async def create_page_blocked(
    page_id: str,
    asid: Optional[str] = None,
    psid: Optional[str] = None,
    uid: Optional[str] = None,
    user: Optional[str] = None,
) -> str:
    """POST /blocked on Page.

    Args:
        page_id: The ID of the Page object.
        asid: Optional.
        psid: Optional.
        uid: Optional.
        user: Optional.
    """
    params = {}
    if asid is not None:
        params["asid"] = asid
    if psid is not None:
        params["psid"] = psid
    if uid is not None:
        params["uid"] = uid
    if user is not None:
        params["user"] = user
    result = await get_client().post(f"{page_id}/blocked", data=params)
    return json.dumps(result, indent=2)


async def create_page_business_data(
    page_id: str,
    data: str,
    partner_agent: str,
    processing_type: Optional[str] = None,
) -> str:
    """POST /business_data on Page.

    Args:
        page_id: The ID of the Page object.
        data: Required.
        partner_agent: Required.
        processing_type: Optional.
    """
    params = {}
    params["data"] = data
    params["partner_agent"] = partner_agent
    if processing_type is not None:
        params["processing_type"] = processing_type
    result = await get_client().post(f"{page_id}/business_data", data=params)
    return json.dumps(result, indent=2)


async def create_page_business_messaging_feature_status(page_id: str, features: str) -> str:
    """POST /business_messaging_feature_status on Page.

    Args:
        page_id: The ID of the Page object.
        features: Required.
    """
    params = {}
    params["features"] = features
    result = await get_client().post(f"{page_id}/business_messaging_feature_status", data=params)
    return json.dumps(result, indent=2)


async def get_page_businessprojects(page_id: str, fields: Optional[str] = None, business: Optional[str] = None) -> str:
    """GET /businessprojects on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        business: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if business is not None:
        params["business"] = business
    result = await get_client().get(f"{page_id}/businessprojects", params=params)
    return json.dumps(result, indent=2)


async def get_page_call_to_actions(page_id: str, fields: Optional[str] = None) -> str:
    """GET /call_to_actions on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/call_to_actions", params=params)
    return json.dumps(result, indent=2)


async def create_page_calls(
    page_id: str,
    action: str,
    call_id: Optional[str] = None,
    from_version: Optional[int] = None,
    platform: Optional[str] = None,
    session: Optional[str] = None,
    to: Optional[str] = None,
    to_version: Optional[int] = None,
    tracks: Optional[str] = None,
) -> str:
    """POST /calls on Page.

    Args:
        page_id: The ID of the Page object.
        action: Required. Values: ACCEPT, CONNECT, MEDIA_UPDATE, REJECT, TERMINATE
        call_id: Optional.
        from_version: Optional.
        platform: Optional. Values: INSTAGRAM, MESSENGER
        session: Optional.
        to: Optional.
        to_version: Optional.
        tracks: Optional.
    """
    params = {}
    params["action"] = action
    if call_id is not None:
        params["call_id"] = call_id
    if from_version is not None:
        params["from_version"] = from_version
    if platform is not None:
        params["platform"] = platform
    if session is not None:
        params["session"] = session
    if to is not None:
        params["to"] = to
    if to_version is not None:
        params["to_version"] = to_version
    if tracks is not None:
        params["tracks"] = tracks
    result = await get_client().post(f"{page_id}/calls", data=params)
    return json.dumps(result, indent=2)


async def get_page_canvas_elements(page_id: str, fields: Optional[str] = None) -> str:
    """GET /canvas_elements on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/canvas_elements", params=params)
    return json.dumps(result, indent=2)


async def create_page_canvas_elements(
    page_id: str,
    canvas_button: Optional[str] = None,
    canvas_carousel: Optional[str] = None,
    canvas_existing_post: Optional[str] = None,
    canvas_footer: Optional[str] = None,
    canvas_header: Optional[str] = None,
    canvas_lead_form: Optional[str] = None,
    canvas_photo: Optional[str] = None,
    canvas_product_list: Optional[str] = None,
    canvas_product_set: Optional[str] = None,
    canvas_store_locator: Optional[str] = None,
    canvas_template_video: Optional[str] = None,
    canvas_text: Optional[str] = None,
    canvas_video: Optional[str] = None,
) -> str:
    """POST /canvas_elements on Page.

    Args:
        page_id: The ID of the Page object.
        canvas_button: Optional.
        canvas_carousel: Optional.
        canvas_existing_post: Optional.
        canvas_footer: Optional.
        canvas_header: Optional.
        canvas_lead_form: Optional.
        canvas_photo: Optional.
        canvas_product_list: Optional.
        canvas_product_set: Optional.
        canvas_store_locator: Optional.
        canvas_template_video: Optional.
        canvas_text: Optional.
        canvas_video: Optional.
    """
    params = {}
    if canvas_button is not None:
        params["canvas_button"] = canvas_button
    if canvas_carousel is not None:
        params["canvas_carousel"] = canvas_carousel
    if canvas_existing_post is not None:
        params["canvas_existing_post"] = canvas_existing_post
    if canvas_footer is not None:
        params["canvas_footer"] = canvas_footer
    if canvas_header is not None:
        params["canvas_header"] = canvas_header
    if canvas_lead_form is not None:
        params["canvas_lead_form"] = canvas_lead_form
    if canvas_photo is not None:
        params["canvas_photo"] = canvas_photo
    if canvas_product_list is not None:
        params["canvas_product_list"] = canvas_product_list
    if canvas_product_set is not None:
        params["canvas_product_set"] = canvas_product_set
    if canvas_store_locator is not None:
        params["canvas_store_locator"] = canvas_store_locator
    if canvas_template_video is not None:
        params["canvas_template_video"] = canvas_template_video
    if canvas_text is not None:
        params["canvas_text"] = canvas_text
    if canvas_video is not None:
        params["canvas_video"] = canvas_video
    result = await get_client().post(f"{page_id}/canvas_elements", data=params)
    return json.dumps(result, indent=2)


async def get_page_canvases(
    page_id: str,
    fields: Optional[str] = None,
    is_hidden: Optional[bool] = None,
    is_published: Optional[bool] = None,
) -> str:
    """GET /canvases on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        is_hidden: Optional.
        is_published: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if is_hidden is not None:
        params["is_hidden"] = is_hidden
    if is_published is not None:
        params["is_published"] = is_published
    result = await get_client().get(f"{page_id}/canvases", params=params)
    return json.dumps(result, indent=2)


async def create_page_canvases(
    page_id: str,
    background_color: Optional[str] = None,
    body_element_ids: Optional[str] = None,
    enable_swipe_to_open: Optional[bool] = None,
    hero_asset_facebook_post_id: Optional[str] = None,
    hero_asset_instagram_media_id: Optional[str] = None,
    is_hidden: Optional[bool] = None,
    is_published: Optional[bool] = None,
    name: Optional[str] = None,
    source_template_id: Optional[str] = None,
) -> str:
    """POST /canvases on Page.

    Args:
        page_id: The ID of the Page object.
        background_color: Optional.
        body_element_ids: Optional.
        enable_swipe_to_open: Optional.
        hero_asset_facebook_post_id: Optional.
        hero_asset_instagram_media_id: Optional.
        is_hidden: Optional.
        is_published: Optional.
        name: Optional.
        source_template_id: Optional.
    """
    params = {}
    if background_color is not None:
        params["background_color"] = background_color
    if body_element_ids is not None:
        params["body_element_ids"] = body_element_ids
    if enable_swipe_to_open is not None:
        params["enable_swipe_to_open"] = enable_swipe_to_open
    if hero_asset_facebook_post_id is not None:
        params["hero_asset_facebook_post_id"] = hero_asset_facebook_post_id
    if hero_asset_instagram_media_id is not None:
        params["hero_asset_instagram_media_id"] = hero_asset_instagram_media_id
    if is_hidden is not None:
        params["is_hidden"] = is_hidden
    if is_published is not None:
        params["is_published"] = is_published
    if name is not None:
        params["name"] = name
    if source_template_id is not None:
        params["source_template_id"] = source_template_id
    result = await get_client().post(f"{page_id}/canvases", data=params)
    return json.dumps(result, indent=2)


async def get_page_chat_plugin(page_id: str, fields: Optional[str] = None) -> str:
    """GET /chat_plugin on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/chat_plugin", params=params)
    return json.dumps(result, indent=2)


async def get_page_commerce_merchant_settings(page_id: str, fields: Optional[str] = None) -> str:
    """GET /commerce_merchant_settings on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/commerce_merchant_settings", params=params)
    return json.dumps(result, indent=2)


async def get_page_commerce_orders(
    page_id: str,
    fields: Optional[str] = None,
    filters: Optional[str] = None,
    state: Optional[str] = None,
    updated_after: Optional[str] = None,
    updated_before: Optional[str] = None,
) -> str:
    """GET /commerce_orders on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        filters: Optional. Values: HAS_CANCELLATIONS, HAS_FULFILLMENTS, HAS_REFUNDS, NO_CANCELLATIONS, NO_REFUNDS, NO_SHIPMENTS
        state: Optional. Values: COMPLETED, CREATED, FB_PROCESSING, IN_PROGRESS
        updated_after: Optional.
        updated_before: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if filters is not None:
        params["filters"] = filters
    if state is not None:
        params["state"] = state
    if updated_after is not None:
        params["updated_after"] = updated_after
    if updated_before is not None:
        params["updated_before"] = updated_before
    result = await get_client().get(f"{page_id}/commerce_orders", params=params)
    return json.dumps(result, indent=2)


async def get_page_commerce_payouts(
    page_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /commerce_payouts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{page_id}/commerce_payouts", params=params)
    return json.dumps(result, indent=2)


async def get_page_commerce_transactions(
    page_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    payout_reference_id: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /commerce_transactions on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        payout_reference_id: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if payout_reference_id is not None:
        params["payout_reference_id"] = payout_reference_id
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{page_id}/commerce_transactions", params=params)
    return json.dumps(result, indent=2)


async def get_page_conversations(
    page_id: str,
    fields: Optional[str] = None,
    folder: Optional[str] = None,
    platform: Optional[str] = None,
    tags: Optional[str] = None,
    user_id: Optional[str] = None,
) -> str:
    """GET /conversations on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        folder: Optional.
        platform: Optional. Values: INSTAGRAM, MESSENGER
        tags: Optional.
        user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if folder is not None:
        params["folder"] = folder
    if platform is not None:
        params["platform"] = platform
    if tags is not None:
        params["tags"] = tags
    if user_id is not None:
        params["user_id"] = user_id
    result = await get_client().get(f"{page_id}/conversations", params=params)
    return json.dumps(result, indent=2)


async def create_page_copyright_manual_claims(
    page_id: str,
    match_content_type: str,
    matched_asset_id: str,
    reference_asset_id: str,
    action: Optional[str] = None,
    action_reason: Optional[str] = None,
    countries: Optional[str] = None,
    selected_segments: Optional[str] = None,
) -> str:
    """POST /copyright_manual_claims on Page.

    Args:
        page_id: The ID of the Page object.
        action: Optional. Values: BLOCK, CLAIM_AD_EARNINGS, MANUAL_REVIEW, MONITOR, REQUEST_TAKEDOWN
        action_reason: Optional. Values: ARTICLE_17_PREFLAGGING, ARTIST_OBJECTION, OBJECTIONABLE_CONTENT, PREMIUM_MUSIC_VIDEO, PRERELEASE_CONTENT, PRODUCT_PARAMETERS, RESTRICTED_CONTENT, UNAUTHORIZED_COMMERCIAL_USE
        countries: Optional.
        match_content_type: Required. Values: AUDIO_ONLY, VIDEO_AND_AUDIO, VIDEO_ONLY
        matched_asset_id: Required.
        reference_asset_id: Required.
        selected_segments: Optional.
    """
    params = {}
    if action is not None:
        params["action"] = action
    if action_reason is not None:
        params["action_reason"] = action_reason
    if countries is not None:
        params["countries"] = countries
    params["match_content_type"] = match_content_type
    params["matched_asset_id"] = matched_asset_id
    params["reference_asset_id"] = reference_asset_id
    if selected_segments is not None:
        params["selected_segments"] = selected_segments
    result = await get_client().post(f"{page_id}/copyright_manual_claims", data=params)
    return json.dumps(result, indent=2)


async def get_page_crosspost_whitelisted_pages(page_id: str, fields: Optional[str] = None) -> str:
    """GET /crosspost_whitelisted_pages on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/crosspost_whitelisted_pages", params=params)
    return json.dumps(result, indent=2)


async def get_page_ctx_optimization_eligibility(page_id: str, fields: Optional[str] = None) -> str:
    """GET /ctx_optimization_eligibility on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/ctx_optimization_eligibility", params=params)
    return json.dumps(result, indent=2)


async def get_page_custom_labels(page_id: str, fields: Optional[str] = None) -> str:
    """GET /custom_labels on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/custom_labels", params=params)
    return json.dumps(result, indent=2)


async def create_page_custom_labels(page_id: str, page_label_name: str, name: Optional[str] = None) -> str:
    """POST /custom_labels on Page.

    Args:
        page_id: The ID of the Page object.
        name: Optional.
        page_label_name: Required.
    """
    params = {}
    if name is not None:
        params["name"] = name
    params["page_label_name"] = page_label_name
    result = await get_client().post(f"{page_id}/custom_labels", data=params)
    return json.dumps(result, indent=2)


async def delete_page_custom_user_settings(page_id: str, params: str, psid: str) -> str:
    """DELETE /custom_user_settings on Page.

    Args:
        page_id: The ID of the Page object.
        params: Required. Values: PERSISTENT_MENU
        psid: Required.
    """
    params = {}
    params["params"] = params
    params["psid"] = psid
    result = await get_client().delete(f"{page_id}/custom_user_settings")
    return json.dumps(result, indent=2)


async def get_page_custom_user_settings(page_id: str, psid: str, fields: Optional[str] = None) -> str:
    """GET /custom_user_settings on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        psid: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["psid"] = psid
    result = await get_client().get(f"{page_id}/custom_user_settings", params=params)
    return json.dumps(result, indent=2)


async def create_page_custom_user_settings(page_id: str, psid: str, persistent_menu: Optional[str] = None) -> str:
    """POST /custom_user_settings on Page.

    Args:
        page_id: The ID of the Page object.
        persistent_menu: Optional.
        psid: Required.
    """
    params = {}
    if persistent_menu is not None:
        params["persistent_menu"] = persistent_menu
    params["psid"] = psid
    result = await get_client().post(f"{page_id}/custom_user_settings", data=params)
    return json.dumps(result, indent=2)


async def get_page_dataset(page_id: str, fields: Optional[str] = None) -> str:
    """GET /dataset on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/dataset", params=params)
    return json.dumps(result, indent=2)


async def create_page_dataset(page_id: str, dataset_name: Optional[str] = None) -> str:
    """POST /dataset on Page.

    Args:
        page_id: The ID of the Page object.
        dataset_name: Optional.
    """
    params = {}
    if dataset_name is not None:
        params["dataset_name"] = dataset_name
    result = await get_client().post(f"{page_id}/dataset", data=params)
    return json.dumps(result, indent=2)


async def get_page_events(
    page_id: str,
    fields: Optional[str] = None,
    event_state_filter: Optional[str] = None,
    include_canceled: Optional[bool] = None,
    time_filter: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /events on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        event_state_filter: Optional. Values: canceled, draft, published, scheduled_draft_for_publication
        include_canceled: Optional.
        time_filter: Optional. Values: past, upcoming
        type_: Optional. Values: attending, created, declined, maybe, not_replied
    """
    params = {}
    params["fields"] = fields or "id,name"
    if event_state_filter is not None:
        params["event_state_filter"] = event_state_filter
    if include_canceled is not None:
        params["include_canceled"] = include_canceled
    if time_filter is not None:
        params["time_filter"] = time_filter
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{page_id}/events", params=params)
    return json.dumps(result, indent=2)


async def create_page_extend_thread_control(page_id: str, recipient: str, duration: Optional[int] = None) -> str:
    """POST /extend_thread_control on Page.

    Args:
        page_id: The ID of the Page object.
        duration: Optional.
        recipient: Required.
    """
    params = {}
    if duration is not None:
        params["duration"] = duration
    params["recipient"] = recipient
    result = await get_client().post(f"{page_id}/extend_thread_control", data=params)
    return json.dumps(result, indent=2)


async def get_page_fantasy_games(page_id: str, fields: Optional[str] = None) -> str:
    """GET /fantasy_games on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/fantasy_games", params=params)
    return json.dumps(result, indent=2)


async def get_page_feed(
    page_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    limit: Optional[int] = None,
    show_expired: Optional[bool] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /feed on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        include_hidden: Optional.
        limit: Optional.
        show_expired: Optional.
        with_: Optional. Values: LOCATION
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_hidden is not None:
        params["include_hidden"] = include_hidden
    if limit is not None:
        params["limit"] = limit
    if show_expired is not None:
        params["show_expired"] = show_expired
    if with_ is not None:
        params["with"] = with_
    result = await get_client().get(f"{page_id}/feed", params=params)
    return json.dumps(result, indent=2)


async def create_page_feed(
    page_id: str,
    actions: Optional[str] = None,
    album_id: Optional[str] = None,
    android_key_hash: Optional[str] = None,
    application_id: Optional[str] = None,
    asked_fun_fact_prompt_id: Optional[int] = None,
    asset3d_id: Optional[str] = None,
    associated_id: Optional[str] = None,
    attach_place_suggestion: Optional[bool] = None,
    attached_media: Optional[str] = None,
    audience_exp: Optional[bool] = None,
    backdated_time: Optional[str] = None,
    backdated_time_granularity: Optional[str] = None,
    breaking_news: Optional[bool] = None,
    breaking_news_expiration: Optional[int] = None,
    call_to_action: Optional[str] = None,
    caption: Optional[str] = None,
    child_attachments: Optional[str] = None,
    client_mutation_id: Optional[str] = None,
    composer_entry_picker: Optional[str] = None,
    composer_entry_point: Optional[str] = None,
    composer_entry_time: Optional[int] = None,
    composer_session_events_log: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    composer_source_surface: Optional[str] = None,
    composer_type: Optional[str] = None,
    connection_class: Optional[str] = None,
    content_attachment: Optional[str] = None,
    coordinates: Optional[str] = None,
    cta_link: Optional[str] = None,
    cta_type: Optional[str] = None,
    description: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    enforce_link_ownership: Optional[bool] = None,
    expanded_height: Optional[int] = None,
    expanded_width: Optional[int] = None,
    feed_targeting: Optional[str] = None,
    formatting: Optional[str] = None,
    fun_fact_prompt_id: Optional[str] = None,
    fun_fact_toastee_id: Optional[int] = None,
    height: Optional[int] = None,
    home_checkin_city_id: Optional[str] = None,
    image_crops: Optional[str] = None,
    implicit_with_tags: Optional[str] = None,
    instant_game_entry_point_data: Optional[str] = None,
    ios_bundle_id: Optional[str] = None,
    is_backout_draft: Optional[bool] = None,
    is_boost_intended: Optional[bool] = None,
    is_explicit_location: Optional[bool] = None,
    is_explicit_share: Optional[bool] = None,
    is_group_linking_post: Optional[bool] = None,
    is_photo_container: Optional[bool] = None,
    link: Optional[str] = None,
    location_source_id: Optional[str] = None,
    manual_privacy: Optional[bool] = None,
    message: Optional[str] = None,
    multi_share_end_card: Optional[bool] = None,
    multi_share_optimized: Optional[bool] = None,
    name: Optional[str] = None,
    nectar_module: Optional[str] = None,
    object_attachment: Optional[str] = None,
    og_action_type_id: Optional[str] = None,
    og_hide_object_attachment: Optional[bool] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_set_profile_badge: Optional[bool] = None,
    og_suggestion_mechanism: Optional[str] = None,
    page_recommendation: Optional[str] = None,
    picture: Optional[str] = None,
    place: Optional[str] = None,
    place_attachment_setting: Optional[str] = None,
    place_list: Optional[str] = None,
    place_list_data: Optional[str] = None,
    post_surfaces_blacklist: Optional[str] = None,
    posting_to_redspace: Optional[str] = None,
    privacy: Optional[str] = None,
    prompt_id: Optional[str] = None,
    prompt_tracking_string: Optional[str] = None,
    properties: Optional[str] = None,
    proxied_app_id: Optional[str] = None,
    publish_event_id: Optional[int] = None,
    published: Optional[bool] = None,
    quote: Optional[str] = None,
    ref: Optional[str] = None,
    referenceable_image_ids: Optional[str] = None,
    referral_id: Optional[str] = None,
    scheduled_publish_time: Optional[str] = None,
    source: Optional[str] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    suggested_place_id: Optional[str] = None,
    tags: Optional[str] = None,
    target_surface: Optional[str] = None,
    targeting: Optional[str] = None,
    text_format_metadata: Optional[str] = None,
    text_format_preset_id: Optional[str] = None,
    text_only_place: Optional[str] = None,
    thumbnail: Optional[str] = None,
    time_since_original_post: Optional[int] = None,
    title: Optional[str] = None,
    tracking_info: Optional[str] = None,
    unpublished_content_type: Optional[str] = None,
    user_selected_tags: Optional[bool] = None,
    video_start_time_ms: Optional[int] = None,
    viewer_coordinates: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """POST /feed on Page.

    Args:
        page_id: The ID of the Page object.
        actions: Optional.
        album_id: Optional.
        android_key_hash: Optional.
        application_id: Optional.
        asked_fun_fact_prompt_id: Optional.
        asset3d_id: Optional.
        associated_id: Optional.
        attach_place_suggestion: Optional.
        attached_media: Optional.
        audience_exp: Optional.
        backdated_time: Optional.
        backdated_time_granularity: Optional. Values: day, hour, min, month, none, year
        breaking_news: Optional.
        breaking_news_expiration: Optional.
        call_to_action: Optional.
        caption: Optional.
        child_attachments: Optional.
        client_mutation_id: Optional.
        composer_entry_picker: Optional.
        composer_entry_point: Optional.
        composer_entry_time: Optional.
        composer_session_events_log: Optional.
        composer_session_id: Optional.
        composer_source_surface: Optional.
        composer_type: Optional.
        connection_class: Optional.
        content_attachment: Optional.
        coordinates: Optional.
        cta_link: Optional.
        cta_type: Optional.
        description: Optional.
        direct_share_status: Optional.
        enforce_link_ownership: Optional.
        expanded_height: Optional.
        expanded_width: Optional.
        feed_targeting: Optional.
        formatting: Optional. Values: MARKDOWN, PLAINTEXT
        fun_fact_prompt_id: Optional.
        fun_fact_toastee_id: Optional.
        height: Optional.
        home_checkin_city_id: Optional.
        image_crops: Optional.
        implicit_with_tags: Optional.
        instant_game_entry_point_data: Optional.
        ios_bundle_id: Optional.
        is_backout_draft: Optional.
        is_boost_intended: Optional.
        is_explicit_location: Optional.
        is_explicit_share: Optional.
        is_group_linking_post: Optional.
        is_photo_container: Optional.
        link: Optional.
        location_source_id: Optional.
        manual_privacy: Optional.
        message: Optional.
        multi_share_end_card: Optional.
        multi_share_optimized: Optional.
        name: Optional.
        nectar_module: Optional.
        object_attachment: Optional.
        og_action_type_id: Optional.
        og_hide_object_attachment: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_set_profile_badge: Optional.
        og_suggestion_mechanism: Optional.
        page_recommendation: Optional.
        picture: Optional.
        place: Optional.
        place_attachment_setting: Optional. Values: 1, 2
        place_list: Optional.
        place_list_data: Optional.
        post_surfaces_blacklist: Optional. Values: 1, 2, 3, 4, 5
        posting_to_redspace: Optional. Values: disabled, enabled
        privacy: Optional.
        prompt_id: Optional.
        prompt_tracking_string: Optional.
        properties: Optional.
        proxied_app_id: Optional.
        publish_event_id: Optional.
        published: Optional.
        quote: Optional.
        ref: Optional.
        referenceable_image_ids: Optional.
        referral_id: Optional.
        scheduled_publish_time: Optional.
        source: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        suggested_place_id: Optional.
        tags: Optional.
        target_surface: Optional. Values: STORY, TIMELINE
        targeting: Optional.
        text_format_metadata: Optional.
        text_format_preset_id: Optional.
        text_only_place: Optional.
        thumbnail: Optional.
        time_since_original_post: Optional.
        title: Optional.
        tracking_info: Optional.
        unpublished_content_type: Optional. Values: ADS_POST, DRAFT, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT, SCHEDULED, SCHEDULED_RECURRING
        user_selected_tags: Optional.
        video_start_time_ms: Optional.
        viewer_coordinates: Optional.
        width: Optional.
    """
    params = {}
    if actions is not None:
        params["actions"] = actions
    if album_id is not None:
        params["album_id"] = album_id
    if android_key_hash is not None:
        params["android_key_hash"] = android_key_hash
    if application_id is not None:
        params["application_id"] = application_id
    if asked_fun_fact_prompt_id is not None:
        params["asked_fun_fact_prompt_id"] = asked_fun_fact_prompt_id
    if asset3d_id is not None:
        params["asset3d_id"] = asset3d_id
    if associated_id is not None:
        params["associated_id"] = associated_id
    if attach_place_suggestion is not None:
        params["attach_place_suggestion"] = attach_place_suggestion
    if attached_media is not None:
        params["attached_media"] = attached_media
    if audience_exp is not None:
        params["audience_exp"] = audience_exp
    if backdated_time is not None:
        params["backdated_time"] = backdated_time
    if backdated_time_granularity is not None:
        params["backdated_time_granularity"] = backdated_time_granularity
    if breaking_news is not None:
        params["breaking_news"] = breaking_news
    if breaking_news_expiration is not None:
        params["breaking_news_expiration"] = breaking_news_expiration
    if call_to_action is not None:
        params["call_to_action"] = call_to_action
    if caption is not None:
        params["caption"] = caption
    if child_attachments is not None:
        params["child_attachments"] = child_attachments
    if client_mutation_id is not None:
        params["client_mutation_id"] = client_mutation_id
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
    if connection_class is not None:
        params["connection_class"] = connection_class
    if content_attachment is not None:
        params["content_attachment"] = content_attachment
    if coordinates is not None:
        params["coordinates"] = coordinates
    if cta_link is not None:
        params["cta_link"] = cta_link
    if cta_type is not None:
        params["cta_type"] = cta_type
    if description is not None:
        params["description"] = description
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if enforce_link_ownership is not None:
        params["enforce_link_ownership"] = enforce_link_ownership
    if expanded_height is not None:
        params["expanded_height"] = expanded_height
    if expanded_width is not None:
        params["expanded_width"] = expanded_width
    if feed_targeting is not None:
        params["feed_targeting"] = feed_targeting
    if formatting is not None:
        params["formatting"] = formatting
    if fun_fact_prompt_id is not None:
        params["fun_fact_prompt_id"] = fun_fact_prompt_id
    if fun_fact_toastee_id is not None:
        params["fun_fact_toastee_id"] = fun_fact_toastee_id
    if height is not None:
        params["height"] = height
    if home_checkin_city_id is not None:
        params["home_checkin_city_id"] = home_checkin_city_id
    if image_crops is not None:
        params["image_crops"] = image_crops
    if implicit_with_tags is not None:
        params["implicit_with_tags"] = implicit_with_tags
    if instant_game_entry_point_data is not None:
        params["instant_game_entry_point_data"] = instant_game_entry_point_data
    if ios_bundle_id is not None:
        params["ios_bundle_id"] = ios_bundle_id
    if is_backout_draft is not None:
        params["is_backout_draft"] = is_backout_draft
    if is_boost_intended is not None:
        params["is_boost_intended"] = is_boost_intended
    if is_explicit_location is not None:
        params["is_explicit_location"] = is_explicit_location
    if is_explicit_share is not None:
        params["is_explicit_share"] = is_explicit_share
    if is_group_linking_post is not None:
        params["is_group_linking_post"] = is_group_linking_post
    if is_photo_container is not None:
        params["is_photo_container"] = is_photo_container
    if link is not None:
        params["link"] = link
    if location_source_id is not None:
        params["location_source_id"] = location_source_id
    if manual_privacy is not None:
        params["manual_privacy"] = manual_privacy
    if message is not None:
        params["message"] = message
    if multi_share_end_card is not None:
        params["multi_share_end_card"] = multi_share_end_card
    if multi_share_optimized is not None:
        params["multi_share_optimized"] = multi_share_optimized
    if name is not None:
        params["name"] = name
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if object_attachment is not None:
        params["object_attachment"] = object_attachment
    if og_action_type_id is not None:
        params["og_action_type_id"] = og_action_type_id
    if og_hide_object_attachment is not None:
        params["og_hide_object_attachment"] = og_hide_object_attachment
    if og_icon_id is not None:
        params["og_icon_id"] = og_icon_id
    if og_object_id is not None:
        params["og_object_id"] = og_object_id
    if og_phrase is not None:
        params["og_phrase"] = og_phrase
    if og_set_profile_badge is not None:
        params["og_set_profile_badge"] = og_set_profile_badge
    if og_suggestion_mechanism is not None:
        params["og_suggestion_mechanism"] = og_suggestion_mechanism
    if page_recommendation is not None:
        params["page_recommendation"] = page_recommendation
    if picture is not None:
        params["picture"] = picture
    if place is not None:
        params["place"] = place
    if place_attachment_setting is not None:
        params["place_attachment_setting"] = place_attachment_setting
    if place_list is not None:
        params["place_list"] = place_list
    if place_list_data is not None:
        params["place_list_data"] = place_list_data
    if post_surfaces_blacklist is not None:
        params["post_surfaces_blacklist"] = post_surfaces_blacklist
    if posting_to_redspace is not None:
        params["posting_to_redspace"] = posting_to_redspace
    if privacy is not None:
        params["privacy"] = privacy
    if prompt_id is not None:
        params["prompt_id"] = prompt_id
    if prompt_tracking_string is not None:
        params["prompt_tracking_string"] = prompt_tracking_string
    if properties is not None:
        params["properties"] = properties
    if proxied_app_id is not None:
        params["proxied_app_id"] = proxied_app_id
    if publish_event_id is not None:
        params["publish_event_id"] = publish_event_id
    if published is not None:
        params["published"] = published
    if quote is not None:
        params["quote"] = quote
    if ref is not None:
        params["ref"] = ref
    if referenceable_image_ids is not None:
        params["referenceable_image_ids"] = referenceable_image_ids
    if referral_id is not None:
        params["referral_id"] = referral_id
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if source is not None:
        params["source"] = source
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if suggested_place_id is not None:
        params["suggested_place_id"] = suggested_place_id
    if tags is not None:
        params["tags"] = tags
    if target_surface is not None:
        params["target_surface"] = target_surface
    if targeting is not None:
        params["targeting"] = targeting
    if text_format_metadata is not None:
        params["text_format_metadata"] = text_format_metadata
    if text_format_preset_id is not None:
        params["text_format_preset_id"] = text_format_preset_id
    if text_only_place is not None:
        params["text_only_place"] = text_only_place
    if thumbnail is not None:
        params["thumbnail"] = thumbnail
    if time_since_original_post is not None:
        params["time_since_original_post"] = time_since_original_post
    if title is not None:
        params["title"] = title
    if tracking_info is not None:
        params["tracking_info"] = tracking_info
    if unpublished_content_type is not None:
        params["unpublished_content_type"] = unpublished_content_type
    if user_selected_tags is not None:
        params["user_selected_tags"] = user_selected_tags
    if video_start_time_ms is not None:
        params["video_start_time_ms"] = video_start_time_ms
    if viewer_coordinates is not None:
        params["viewer_coordinates"] = viewer_coordinates
    if width is not None:
        params["width"] = width
    result = await get_client().post(f"{page_id}/feed", data=params)
    return json.dumps(result, indent=2)


async def get_page_global_brand_children(page_id: str, fields: Optional[str] = None) -> str:
    """GET /global_brand_children on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/global_brand_children", params=params)
    return json.dumps(result, indent=2)


async def get_page_image_copyrights(page_id: str, fields: Optional[str] = None) -> str:
    """GET /image_copyrights on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/image_copyrights", params=params)
    return json.dumps(result, indent=2)


async def create_page_image_copyrights(
    page_id: str,
    filename: str,
    geo_ownership: str,
    reference_photo: str,
    artist: Optional[str] = None,
    attribution_link: Optional[str] = None,
    creator: Optional[str] = None,
    custom_id: Optional[str] = None,
    description: Optional[str] = None,
    original_content_creation_date: Optional[int] = None,
    title: Optional[str] = None,
) -> str:
    """POST /image_copyrights on Page.

    Args:
        page_id: The ID of the Page object.
        artist: Optional.
        attribution_link: Optional.
        creator: Optional.
        custom_id: Optional.
        description: Optional.
        filename: Required.
        geo_ownership: Required. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TP, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        original_content_creation_date: Optional.
        reference_photo: Required.
        title: Optional.
    """
    params = {}
    if artist is not None:
        params["artist"] = artist
    if attribution_link is not None:
        params["attribution_link"] = attribution_link
    if creator is not None:
        params["creator"] = creator
    if custom_id is not None:
        params["custom_id"] = custom_id
    if description is not None:
        params["description"] = description
    params["filename"] = filename
    params["geo_ownership"] = geo_ownership
    if original_content_creation_date is not None:
        params["original_content_creation_date"] = original_content_creation_date
    params["reference_photo"] = reference_photo
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{page_id}/image_copyrights", data=params)
    return json.dumps(result, indent=2)


async def get_page_indexed_videos(page_id: str, fields: Optional[str] = None) -> str:
    """GET /indexed_videos on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/indexed_videos", params=params)
    return json.dumps(result, indent=2)


async def get_page_insights(
    page_id: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    date_preset: Optional[str] = None,
    metric: Optional[str] = None,
    period: Optional[str] = None,
    show_description_from_api_doc: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        breakdown: Optional.
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        metric: Optional.
        period: Optional. Values: day, days_28, lifetime, month, total_over_range, week
        show_description_from_api_doc: Optional.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdown is not None:
        params["breakdown"] = breakdown
    if date_preset is not None:
        params["date_preset"] = date_preset
    if metric is not None:
        params["metric"] = metric
    if period is not None:
        params["period"] = period
    if show_description_from_api_doc is not None:
        params["show_description_from_api_doc"] = show_description_from_api_doc
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{page_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_page_instagram_accounts(page_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_accounts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_page_leadgen_forms(page_id: str, fields: Optional[str] = None) -> str:
    """GET /leadgen_forms on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/leadgen_forms", params=params)
    return json.dumps(result, indent=2)


async def create_page_leadgen_forms(
    page_id: str,
    name: str,
    questions: str,
    allow_organic_lead_retrieval: Optional[bool] = None,
    block_display_for_non_targeted_viewer: Optional[bool] = None,
    context_card: Optional[str] = None,
    cover_photo: Optional[str] = None,
    custom_disclaimer: Optional[str] = None,
    follow_up_action_url: Optional[str] = None,
    is_for_canvas: Optional[bool] = None,
    is_optimized_for_quality: Optional[bool] = None,
    is_phone_sms_verify_enabled: Optional[bool] = None,
    locale: Optional[str] = None,
    privacy_policy: Optional[str] = None,
    question_page_custom_headline: Optional[str] = None,
    should_enforce_work_email: Optional[bool] = None,
    thank_you_page: Optional[str] = None,
    tracking_parameters: Optional[str] = None,
    upload_gated_file: Optional[str] = None,
) -> str:
    """POST /leadgen_forms on Page.

    Args:
        page_id: The ID of the Page object.
        allow_organic_lead_retrieval: Optional.
        block_display_for_non_targeted_viewer: Optional.
        context_card: Optional.
        cover_photo: Optional.
        custom_disclaimer: Optional.
        follow_up_action_url: Optional.
        is_for_canvas: Optional.
        is_optimized_for_quality: Optional.
        is_phone_sms_verify_enabled: Optional.
        locale: Optional. Values: AR_AR, CS_CZ, DA_DK, DE_DE, EL_GR, EN_GB, EN_US, ES_ES, ES_LA, FI_FI, FR_FR, HE_IL, HI_IN, HU_HU, ID_ID, IT_IT, JA_JP, KO_KR, NB_NO, NL_NL, PL_PL, PT_BR, PT_PT, RO_RO, RU_RU, SV_SE, TH_TH, TR_TR, VI_VN, ZH_CN, ZH_HK, ZH_TW
        name: Required.
        privacy_policy: Optional.
        question_page_custom_headline: Optional.
        questions: Required.
        should_enforce_work_email: Optional.
        thank_you_page: Optional.
        tracking_parameters: Optional.
        upload_gated_file: Optional.
    """
    params = {}
    if allow_organic_lead_retrieval is not None:
        params["allow_organic_lead_retrieval"] = allow_organic_lead_retrieval
    if block_display_for_non_targeted_viewer is not None:
        params["block_display_for_non_targeted_viewer"] = block_display_for_non_targeted_viewer
    if context_card is not None:
        params["context_card"] = context_card
    if cover_photo is not None:
        params["cover_photo"] = cover_photo
    if custom_disclaimer is not None:
        params["custom_disclaimer"] = custom_disclaimer
    if follow_up_action_url is not None:
        params["follow_up_action_url"] = follow_up_action_url
    if is_for_canvas is not None:
        params["is_for_canvas"] = is_for_canvas
    if is_optimized_for_quality is not None:
        params["is_optimized_for_quality"] = is_optimized_for_quality
    if is_phone_sms_verify_enabled is not None:
        params["is_phone_sms_verify_enabled"] = is_phone_sms_verify_enabled
    if locale is not None:
        params["locale"] = locale
    params["name"] = name
    if privacy_policy is not None:
        params["privacy_policy"] = privacy_policy
    if question_page_custom_headline is not None:
        params["question_page_custom_headline"] = question_page_custom_headline
    params["questions"] = questions
    if should_enforce_work_email is not None:
        params["should_enforce_work_email"] = should_enforce_work_email
    if thank_you_page is not None:
        params["thank_you_page"] = thank_you_page
    if tracking_parameters is not None:
        params["tracking_parameters"] = tracking_parameters
    if upload_gated_file is not None:
        params["upload_gated_file"] = upload_gated_file
    result = await get_client().post(f"{page_id}/leadgen_forms", data=params)
    return json.dumps(result, indent=2)


async def get_page_likes(page_id: str, fields: Optional[str] = None, target_id: Optional[str] = None) -> str:
    """GET /likes on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        target_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if target_id is not None:
        params["target_id"] = target_id
    result = await get_client().get(f"{page_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def get_page_live_videos(
    page_id: str,
    fields: Optional[str] = None,
    broadcast_status: Optional[str] = None,
    source: Optional[str] = None,
) -> str:
    """GET /live_videos on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        broadcast_status: Optional. Values: LIVE, LIVE_STOPPED, PROCESSING, SCHEDULED_CANCELED, SCHEDULED_EXPIRED, SCHEDULED_LIVE, SCHEDULED_UNPUBLISHED, UNPUBLISHED, VOD
        source: Optional. Values: owner, target
    """
    params = {}
    params["fields"] = fields or "id,name"
    if broadcast_status is not None:
        params["broadcast_status"] = broadcast_status
    if source is not None:
        params["source"] = source
    result = await get_client().get(f"{page_id}/live_videos", params=params)
    return json.dumps(result, indent=2)


async def create_page_live_videos(
    page_id: str,
    content_tags: Optional[str] = None,
    crossposting_actions: Optional[str] = None,
    custom_labels: Optional[str] = None,
    description: Optional[str] = None,
    enable_backup_ingest: Optional[bool] = None,
    encoding_settings: Optional[str] = None,
    event_params: Optional[str] = None,
    fisheye_video_cropped: Optional[bool] = None,
    front_z_rotation: Optional[float] = None,
    game_show: Optional[str] = None,
    is_audio_only: Optional[bool] = None,
    is_spherical: Optional[bool] = None,
    original_fov: Optional[int] = None,
    privacy: Optional[str] = None,
    projection: Optional[str] = None,
    published: Optional[bool] = None,
    schedule_custom_profile_image: Optional[str] = None,
    spatial_audio_format: Optional[str] = None,
    status: Optional[str] = None,
    stereoscopic_mode: Optional[str] = None,
    stop_on_delete_stream: Optional[bool] = None,
    stream_type: Optional[str] = None,
    targeting: Optional[str] = None,
    title: Optional[str] = None,
) -> str:
    """POST /live_videos on Page.

    Args:
        page_id: The ID of the Page object.
        content_tags: Optional.
        crossposting_actions: Optional.
        custom_labels: Optional.
        description: Optional.
        enable_backup_ingest: Optional.
        encoding_settings: Optional.
        event_params: Optional.
        fisheye_video_cropped: Optional.
        front_z_rotation: Optional.
        game_show: Optional.
        is_audio_only: Optional.
        is_spherical: Optional.
        original_fov: Optional.
        privacy: Optional.
        projection: Optional. Values: CUBEMAP, EQUIRECTANGULAR, HALF_EQUIRECTANGULAR
        published: Optional.
        schedule_custom_profile_image: Optional.
        spatial_audio_format: Optional. Values: ambiX_4
        status: Optional. Values: LIVE_NOW, SCHEDULED_CANCELED, SCHEDULED_LIVE, SCHEDULED_UNPUBLISHED, UNPUBLISHED
        stereoscopic_mode: Optional. Values: LEFT_RIGHT, MONO, TOP_BOTTOM
        stop_on_delete_stream: Optional.
        stream_type: Optional. Values: AMBIENT, REGULAR
        targeting: Optional.
        title: Optional.
    """
    params = {}
    if content_tags is not None:
        params["content_tags"] = content_tags
    if crossposting_actions is not None:
        params["crossposting_actions"] = crossposting_actions
    if custom_labels is not None:
        params["custom_labels"] = custom_labels
    if description is not None:
        params["description"] = description
    if enable_backup_ingest is not None:
        params["enable_backup_ingest"] = enable_backup_ingest
    if encoding_settings is not None:
        params["encoding_settings"] = encoding_settings
    if event_params is not None:
        params["event_params"] = event_params
    if fisheye_video_cropped is not None:
        params["fisheye_video_cropped"] = fisheye_video_cropped
    if front_z_rotation is not None:
        params["front_z_rotation"] = front_z_rotation
    if game_show is not None:
        params["game_show"] = game_show
    if is_audio_only is not None:
        params["is_audio_only"] = is_audio_only
    if is_spherical is not None:
        params["is_spherical"] = is_spherical
    if original_fov is not None:
        params["original_fov"] = original_fov
    if privacy is not None:
        params["privacy"] = privacy
    if projection is not None:
        params["projection"] = projection
    if published is not None:
        params["published"] = published
    if schedule_custom_profile_image is not None:
        params["schedule_custom_profile_image"] = schedule_custom_profile_image
    if spatial_audio_format is not None:
        params["spatial_audio_format"] = spatial_audio_format
    if status is not None:
        params["status"] = status
    if stereoscopic_mode is not None:
        params["stereoscopic_mode"] = stereoscopic_mode
    if stop_on_delete_stream is not None:
        params["stop_on_delete_stream"] = stop_on_delete_stream
    if stream_type is not None:
        params["stream_type"] = stream_type
    if targeting is not None:
        params["targeting"] = targeting
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{page_id}/live_videos", data=params)
    return json.dumps(result, indent=2)


async def delete_page_locations(page_id: str, location_page_ids: str, store_numbers: str) -> str:
    """DELETE /locations on Page.

    Args:
        page_id: The ID of the Page object.
        location_page_ids: Required.
        store_numbers: Required.
    """
    params = {}
    params["location_page_ids"] = location_page_ids
    params["store_numbers"] = store_numbers
    result = await get_client().delete(f"{page_id}/locations")
    return json.dumps(result, indent=2)


async def get_page_locations(page_id: str, fields: Optional[str] = None) -> str:
    """GET /locations on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/locations", params=params)
    return json.dumps(result, indent=2)


async def create_page_locations(
    page_id: str,
    store_number: int,
    always_open: Optional[bool] = None,
    delivery_and_pickup_option_info: Optional[str] = None,
    differently_open_offerings: Optional[str] = None,
    hours: Optional[str] = None,
    ignore_warnings: Optional[bool] = None,
    location: Optional[str] = None,
    location_page_id: Optional[str] = None,
    old_store_number: Optional[int] = None,
    page_username: Optional[str] = None,
    permanently_closed: Optional[bool] = None,
    phone: Optional[str] = None,
    pickup_options: Optional[str] = None,
    place_topics: Optional[str] = None,
    price_range: Optional[str] = None,
    recommendation_action: Optional[str] = None,
    recommendation_ds: Optional[str] = None,
    recommendation_store_id: Optional[int] = None,
    store_code: Optional[str] = None,
    store_location_descriptor: Optional[str] = None,
    store_name: Optional[str] = None,
    temporary_status: Optional[str] = None,
    type_: Optional[str] = None,
    website: Optional[str] = None,
) -> str:
    """POST /locations on Page.

    Args:
        page_id: The ID of the Page object.
        always_open: Optional.
        delivery_and_pickup_option_info: Optional.
        differently_open_offerings: Optional.
        hours: Optional.
        ignore_warnings: Optional.
        location: Optional.
        location_page_id: Optional.
        old_store_number: Optional.
        page_username: Optional.
        permanently_closed: Optional.
        phone: Optional.
        pickup_options: Optional. Values: CURBSIDE, IN_STORE, OTHER
        place_topics: Optional.
        price_range: Optional.
        recommendation_action: Optional. Values: ACCEPT_CLOSED, ACCEPT_NEW, REJECT_CLOSED, REJECT_NEW
        recommendation_ds: Optional.
        recommendation_store_id: Optional.
        store_code: Optional.
        store_location_descriptor: Optional.
        store_name: Optional.
        store_number: Required.
        temporary_status: Optional. Values: DIFFERENTLY_OPEN, NO_DATA, OPERATING_AS_USUAL, TEMPORARILY_CLOSED
        type_: Optional.
        website: Optional.
    """
    params = {}
    if always_open is not None:
        params["always_open"] = always_open
    if delivery_and_pickup_option_info is not None:
        params["delivery_and_pickup_option_info"] = delivery_and_pickup_option_info
    if differently_open_offerings is not None:
        params["differently_open_offerings"] = differently_open_offerings
    if hours is not None:
        params["hours"] = hours
    if ignore_warnings is not None:
        params["ignore_warnings"] = ignore_warnings
    if location is not None:
        params["location"] = location
    if location_page_id is not None:
        params["location_page_id"] = location_page_id
    if old_store_number is not None:
        params["old_store_number"] = old_store_number
    if page_username is not None:
        params["page_username"] = page_username
    if permanently_closed is not None:
        params["permanently_closed"] = permanently_closed
    if phone is not None:
        params["phone"] = phone
    if pickup_options is not None:
        params["pickup_options"] = pickup_options
    if place_topics is not None:
        params["place_topics"] = place_topics
    if price_range is not None:
        params["price_range"] = price_range
    if recommendation_action is not None:
        params["recommendation_action"] = recommendation_action
    if recommendation_ds is not None:
        params["recommendation_ds"] = recommendation_ds
    if recommendation_store_id is not None:
        params["recommendation_store_id"] = recommendation_store_id
    if store_code is not None:
        params["store_code"] = store_code
    if store_location_descriptor is not None:
        params["store_location_descriptor"] = store_location_descriptor
    if store_name is not None:
        params["store_name"] = store_name
    params["store_number"] = store_number
    if temporary_status is not None:
        params["temporary_status"] = temporary_status
    if type_ is not None:
        params["type"] = type_
    if website is not None:
        params["website"] = website
    result = await get_client().post(f"{page_id}/locations", data=params)
    return json.dumps(result, indent=2)


async def get_page_media_fingerprints(
    page_id: str,
    fields: Optional[str] = None,
    universal_content_id: Optional[str] = None,
) -> str:
    """GET /media_fingerprints on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        universal_content_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if universal_content_id is not None:
        params["universal_content_id"] = universal_content_id
    result = await get_client().get(f"{page_id}/media_fingerprints", params=params)
    return json.dumps(result, indent=2)


async def create_page_media_fingerprints(
    page_id: str,
    fingerprint_content_type: str,
    metadata: str,
    source: str,
    title: str,
    universal_content_id: Optional[str] = None,
) -> str:
    """POST /media_fingerprints on Page.

    Args:
        page_id: The ID of the Page object.
        fingerprint_content_type: Required. Values: AM_SONGTRACK, EPISODE, MOVIE, OTHER, SONGTRACK
        metadata: Required.
        source: Required.
        title: Required.
        universal_content_id: Optional.
    """
    params = {}
    params["fingerprint_content_type"] = fingerprint_content_type
    params["metadata"] = metadata
    params["source"] = source
    params["title"] = title
    if universal_content_id is not None:
        params["universal_content_id"] = universal_content_id
    result = await get_client().post(f"{page_id}/media_fingerprints", data=params)
    return json.dumps(result, indent=2)


async def create_page_message_attachments(page_id: str, message: str, platform: Optional[str] = None) -> str:
    """POST /message_attachments on Page.

    Args:
        page_id: The ID of the Page object.
        message: Required.
        platform: Optional. Values: INSTAGRAM, MESSENGER
    """
    params = {}
    params["message"] = message
    if platform is not None:
        params["platform"] = platform
    result = await get_client().post(f"{page_id}/message_attachments", data=params)
    return json.dumps(result, indent=2)


async def delete_page_message_templates(page_id: str, name: str, template_id: Optional[str] = None) -> str:
    """DELETE /message_templates on Page.

    Args:
        page_id: The ID of the Page object.
        name: Required.
        template_id: Optional.
    """
    params = {}
    params["name"] = name
    if template_id is not None:
        params["template_id"] = template_id
    result = await get_client().delete(f"{page_id}/message_templates")
    return json.dumps(result, indent=2)


async def get_page_message_templates(
    page_id: str,
    fields: Optional[str] = None,
    category: Optional[str] = None,
    content: Optional[str] = None,
    language: Optional[str] = None,
    name: Optional[str] = None,
    name_or_content: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """GET /message_templates on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        category: Optional. Values: UTILITY
        content: Optional.
        language: Optional.
        name: Optional.
        name_or_content: Optional.
        status: Optional. Values: APPROVED, ARCHIVED, DELETED, DISABLED, IN_APPEAL, LIMIT_EXCEEDED, PAUSED, PENDING, PENDING_DELETION, REJECTED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if category is not None:
        params["category"] = category
    if content is not None:
        params["content"] = content
    if language is not None:
        params["language"] = language
    if name is not None:
        params["name"] = name
    if name_or_content is not None:
        params["name_or_content"] = name_or_content
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{page_id}/message_templates", params=params)
    return json.dumps(result, indent=2)


async def create_page_message_templates(
    page_id: str,
    category: str,
    language: str,
    name: str,
    components: Optional[str] = None,
    library_template_button_inputs: Optional[str] = None,
    library_template_name: Optional[str] = None,
) -> str:
    """POST /message_templates on Page.

    Args:
        page_id: The ID of the Page object.
        category: Required. Values: UTILITY
        components: Optional.
        language: Required.
        library_template_button_inputs: Optional.
        library_template_name: Optional.
        name: Required.
    """
    params = {}
    params["category"] = category
    if components is not None:
        params["components"] = components
    params["language"] = language
    if library_template_button_inputs is not None:
        params["library_template_button_inputs"] = library_template_button_inputs
    if library_template_name is not None:
        params["library_template_name"] = library_template_name
    params["name"] = name
    result = await get_client().post(f"{page_id}/message_templates", data=params)
    return json.dumps(result, indent=2)


async def create_page_messages(
    page_id: str,
    recipient: str,
    message: Optional[str] = None,
    messaging_type: Optional[str] = None,
    notification_type: Optional[str] = None,
    payload: Optional[str] = None,
    persona_id: Optional[str] = None,
    reply_to: Optional[str] = None,
    sender_action: Optional[str] = None,
    suggestion_action: Optional[str] = None,
    tag: Optional[str] = None,
    thread_control: Optional[str] = None,
) -> str:
    """POST /messages on Page.

    Args:
        page_id: The ID of the Page object.
        message: Optional.
        messaging_type: Optional. Values: MESSAGE_TAG, RESPONSE, UPDATE, UTILITY
        notification_type: Optional. Values: NO_PUSH, REGULAR, SILENT_PUSH
        payload: Optional.
        persona_id: Optional.
        recipient: Required.
        reply_to: Optional.
        sender_action: Optional. Values: MARK_SEEN, REACT, TYPING_OFF, TYPING_ON, UNREACT
        suggestion_action: Optional. Values: ACCEPT, DISMISS, IMPRESSION
        tag: Optional.
        thread_control: Optional.
    """
    params = {}
    if message is not None:
        params["message"] = message
    if messaging_type is not None:
        params["messaging_type"] = messaging_type
    if notification_type is not None:
        params["notification_type"] = notification_type
    if payload is not None:
        params["payload"] = payload
    if persona_id is not None:
        params["persona_id"] = persona_id
    params["recipient"] = recipient
    if reply_to is not None:
        params["reply_to"] = reply_to
    if sender_action is not None:
        params["sender_action"] = sender_action
    if suggestion_action is not None:
        params["suggestion_action"] = suggestion_action
    if tag is not None:
        params["tag"] = tag
    if thread_control is not None:
        params["thread_control"] = thread_control
    result = await get_client().post(f"{page_id}/messages", data=params)
    return json.dumps(result, indent=2)


async def get_page_messaging_feature_review(page_id: str, fields: Optional[str] = None) -> str:
    """GET /messaging_feature_review on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/messaging_feature_review", params=params)
    return json.dumps(result, indent=2)


async def get_page_messenger_call_settings(page_id: str, fields: Optional[str] = None) -> str:
    """GET /messenger_call_settings on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/messenger_call_settings", params=params)
    return json.dumps(result, indent=2)


async def create_page_messenger_call_settings(
    page_id: str,
    audio_enabled: Optional[bool] = None,
    call_hours: Optional[str] = None,
    call_routing: Optional[str] = None,
    icon_enabled: Optional[bool] = None,
    video: Optional[str] = None,
) -> str:
    """POST /messenger_call_settings on Page.

    Args:
        page_id: The ID of the Page object.
        audio_enabled: Optional.
        call_hours: Optional.
        call_routing: Optional.
        icon_enabled: Optional.
        video: Optional.
    """
    params = {}
    if audio_enabled is not None:
        params["audio_enabled"] = audio_enabled
    if call_hours is not None:
        params["call_hours"] = call_hours
    if call_routing is not None:
        params["call_routing"] = call_routing
    if icon_enabled is not None:
        params["icon_enabled"] = icon_enabled
    if video is not None:
        params["video"] = video
    result = await get_client().post(f"{page_id}/messenger_call_settings", data=params)
    return json.dumps(result, indent=2)


async def get_page_messenger_lead_forms(page_id: str, fields: Optional[str] = None) -> str:
    """GET /messenger_lead_forms on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/messenger_lead_forms", params=params)
    return json.dumps(result, indent=2)


async def create_page_messenger_lead_forms(
    page_id: str,
    step_list: str,
    account_id: Optional[int] = None,
    block_send_api: Optional[bool] = None,
    exit_keyphrases: Optional[str] = None,
    handover_app_id: Optional[int] = None,
    handover_summary: Optional[bool] = None,
    privacy_url: Optional[str] = None,
    reminder_text: Optional[str] = None,
    stop_question_message: Optional[str] = None,
    template_name: Optional[str] = None,
    tracking_parameters: Optional[str] = None,
) -> str:
    """POST /messenger_lead_forms on Page.

    Args:
        page_id: The ID of the Page object.
        account_id: Optional.
        block_send_api: Optional.
        exit_keyphrases: Optional.
        handover_app_id: Optional.
        handover_summary: Optional.
        privacy_url: Optional.
        reminder_text: Optional.
        step_list: Required.
        stop_question_message: Optional.
        template_name: Optional.
        tracking_parameters: Optional.
    """
    params = {}
    if account_id is not None:
        params["account_id"] = account_id
    if block_send_api is not None:
        params["block_send_api"] = block_send_api
    if exit_keyphrases is not None:
        params["exit_keyphrases"] = exit_keyphrases
    if handover_app_id is not None:
        params["handover_app_id"] = handover_app_id
    if handover_summary is not None:
        params["handover_summary"] = handover_summary
    if privacy_url is not None:
        params["privacy_url"] = privacy_url
    if reminder_text is not None:
        params["reminder_text"] = reminder_text
    params["step_list"] = step_list
    if stop_question_message is not None:
        params["stop_question_message"] = stop_question_message
    if template_name is not None:
        params["template_name"] = template_name
    if tracking_parameters is not None:
        params["tracking_parameters"] = tracking_parameters
    result = await get_client().post(f"{page_id}/messenger_lead_forms", data=params)
    return json.dumps(result, indent=2)


async def delete_page_messenger_profile(page_id: str, fields: str, platform: Optional[str] = None) -> str:
    """DELETE /messenger_profile on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Required. Values: ACCOUNT_LINKING_URL, COMMANDS, DESCRIPTION, GET_STARTED, GREETING, HOME_URL, ICE_BREAKERS, PERSISTENT_MENU, PLATFORM, SUBJECT_TO_NEW_EU_PRIVACY_RULES, TITLE, WHITELISTED_DOMAINS
        platform: Optional. Values: INSTAGRAM, MESSENGER
    """
    params = {}
    params["fields"] = fields
    if platform is not None:
        params["platform"] = platform
    result = await get_client().delete(f"{page_id}/messenger_profile")
    return json.dumps(result, indent=2)


async def get_page_messenger_profile(page_id: str, fields: Optional[str] = None, platform: Optional[str] = None) -> str:
    """GET /messenger_profile on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        platform: Optional. Values: INSTAGRAM, MESSENGER
    """
    params = {}
    params["fields"] = fields or "id,name"
    if platform is not None:
        params["platform"] = platform
    result = await get_client().get(f"{page_id}/messenger_profile", params=params)
    return json.dumps(result, indent=2)


async def create_page_messenger_profile(
    page_id: str,
    account_linking_url: Optional[str] = None,
    commands: Optional[str] = None,
    description: Optional[str] = None,
    get_started: Optional[str] = None,
    greeting: Optional[str] = None,
    ice_breakers: Optional[str] = None,
    persistent_menu: Optional[str] = None,
    platform: Optional[str] = None,
    title: Optional[str] = None,
    whitelisted_domains: Optional[str] = None,
) -> str:
    """POST /messenger_profile on Page.

    Args:
        page_id: The ID of the Page object.
        account_linking_url: Optional.
        commands: Optional.
        description: Optional.
        get_started: Optional.
        greeting: Optional.
        ice_breakers: Optional.
        persistent_menu: Optional.
        platform: Optional. Values: INSTAGRAM, MESSENGER
        title: Optional.
        whitelisted_domains: Optional.
    """
    params = {}
    if account_linking_url is not None:
        params["account_linking_url"] = account_linking_url
    if commands is not None:
        params["commands"] = commands
    if description is not None:
        params["description"] = description
    if get_started is not None:
        params["get_started"] = get_started
    if greeting is not None:
        params["greeting"] = greeting
    if ice_breakers is not None:
        params["ice_breakers"] = ice_breakers
    if persistent_menu is not None:
        params["persistent_menu"] = persistent_menu
    if platform is not None:
        params["platform"] = platform
    if title is not None:
        params["title"] = title
    if whitelisted_domains is not None:
        params["whitelisted_domains"] = whitelisted_domains
    result = await get_client().post(f"{page_id}/messenger_profile", data=params)
    return json.dumps(result, indent=2)


async def create_page_moderate_conversations(page_id: str, actions: str, user_ids: str) -> str:
    """POST /moderate_conversations on Page.

    Args:
        page_id: The ID of the Page object.
        actions: Required. Values: BAN_USER, BLOCK_USER, MOVE_TO_SPAM, UNBAN_USER, UNBLOCK_USER
        user_ids: Required.
    """
    params = {}
    params["actions"] = actions
    params["user_ids"] = user_ids
    result = await get_client().post(f"{page_id}/moderate_conversations", data=params)
    return json.dumps(result, indent=2)


async def create_page_nlp_configs(
    page_id: str,
    api_version: Optional[str] = None,
    custom_token: Optional[str] = None,
    model: Optional[str] = None,
    n_best: Optional[int] = None,
    nlp_enabled: Optional[bool] = None,
    other_language_support: Optional[str] = None,
    verbose: Optional[bool] = None,
) -> str:
    """POST /nlp_configs on Page.

    Args:
        page_id: The ID of the Page object.
        api_version: Optional.
        custom_token: Optional.
        model: Optional. Values: ARABIC, CHINESE, CROATIAN, CUSTOM, DANISH, DUTCH, ENGLISH, FRENCH_STANDARD, GEORGIAN, GERMAN_STANDARD, GREEK, HEBREW, HUNGARIAN, IRISH, ITALIAN_STANDARD, KOREAN, NORWEGIAN_BOKMAL, POLISH, PORTUGUESE, ROMANIAN, SPANISH, SWEDISH, VIETNAMESE
        n_best: Optional.
        nlp_enabled: Optional.
        other_language_support: Optional.
        verbose: Optional.
    """
    params = {}
    if api_version is not None:
        params["api_version"] = api_version
    if custom_token is not None:
        params["custom_token"] = custom_token
    if model is not None:
        params["model"] = model
    if n_best is not None:
        params["n_best"] = n_best
    if nlp_enabled is not None:
        params["nlp_enabled"] = nlp_enabled
    if other_language_support is not None:
        params["other_language_support"] = other_language_support
    if verbose is not None:
        params["verbose"] = verbose
    result = await get_client().post(f"{page_id}/nlp_configs", data=params)
    return json.dumps(result, indent=2)


async def get_page_notification_message_tokens(
    page_id: str,
    fields: Optional[str] = None,
    custom_audience_ids: Optional[str] = None,
) -> str:
    """GET /notification_message_tokens on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        custom_audience_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if custom_audience_ids is not None:
        params["custom_audience_ids"] = custom_audience_ids
    result = await get_client().get(f"{page_id}/notification_message_tokens", params=params)
    return json.dumps(result, indent=2)


async def create_page_notification_messages_dev_support(page_id: str, developer_action: str, recipient: str) -> str:
    """POST /notification_messages_dev_support on Page.

    Args:
        page_id: The ID of the Page object.
        developer_action: Required. Values: ENABLE_FOLLOWUP_MESSAGE
        recipient: Required.
    """
    params = {}
    params["developer_action"] = developer_action
    params["recipient"] = recipient
    result = await get_client().post(f"{page_id}/notification_messages_dev_support", data=params)
    return json.dumps(result, indent=2)


async def get_page_page_backed_instagram_accounts(page_id: str, fields: Optional[str] = None) -> str:
    """GET /page_backed_instagram_accounts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/page_backed_instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_page_page_backed_instagram_accounts(page_id: str) -> str:
    """POST /page_backed_instagram_accounts on Page.

    Args:
        page_id: The ID of the Page object.
    """
    params = {}
    result = await get_client().post(f"{page_id}/page_backed_instagram_accounts", data=params)
    return json.dumps(result, indent=2)


async def create_page_page_whatsapp_number_verification(page_id: str, whatsapp_number: str, verification_code: Optional[str] = None) -> str:
    """POST /page_whatsapp_number_verification on Page.

    Args:
        page_id: The ID of the Page object.
        verification_code: Optional.
        whatsapp_number: Required.
    """
    params = {}
    if verification_code is not None:
        params["verification_code"] = verification_code
    params["whatsapp_number"] = whatsapp_number
    result = await get_client().post(f"{page_id}/page_whatsapp_number_verification", data=params)
    return json.dumps(result, indent=2)


async def create_page_pass_thread_control(
    page_id: str,
    recipient: str,
    metadata: Optional[str] = None,
    target_app_id: Optional[str] = None,
) -> str:
    """POST /pass_thread_control on Page.

    Args:
        page_id: The ID of the Page object.
        metadata: Optional.
        recipient: Required.
        target_app_id: Optional.
    """
    params = {}
    if metadata is not None:
        params["metadata"] = metadata
    params["recipient"] = recipient
    if target_app_id is not None:
        params["target_app_id"] = target_app_id
    result = await get_client().post(f"{page_id}/pass_thread_control", data=params)
    return json.dumps(result, indent=2)


async def get_page_personas(page_id: str, fields: Optional[str] = None) -> str:
    """GET /personas on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/personas", params=params)
    return json.dumps(result, indent=2)


async def create_page_personas(page_id: str, name: str, profile_picture_url: str) -> str:
    """POST /personas on Page.

    Args:
        page_id: The ID of the Page object.
        name: Required.
        profile_picture_url: Required.
    """
    params = {}
    params["name"] = name
    params["profile_picture_url"] = profile_picture_url
    result = await get_client().post(f"{page_id}/personas", data=params)
    return json.dumps(result, indent=2)


async def create_page_photo_stories(page_id: str, photo_id: Optional[str] = None) -> str:
    """POST /photo_stories on Page.

    Args:
        page_id: The ID of the Page object.
        photo_id: Optional.
    """
    params = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    result = await get_client().post(f"{page_id}/photo_stories", data=params)
    return json.dumps(result, indent=2)


async def get_page_photos(
    page_id: str,
    fields: Optional[str] = None,
    biz_tag_id: Optional[int] = None,
    business_id: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /photos on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        biz_tag_id: Optional.
        business_id: Optional.
        type_: Optional. Values: profile, tagged, uploaded
    """
    params = {}
    params["fields"] = fields or "id,name"
    if biz_tag_id is not None:
        params["biz_tag_id"] = biz_tag_id
    if business_id is not None:
        params["business_id"] = business_id
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{page_id}/photos", params=params)
    return json.dumps(result, indent=2)


async def create_page_photos(
    page_id: str,
    aid: Optional[str] = None,
    allow_spherical_photo: Optional[bool] = None,
    alt_text_custom: Optional[str] = None,
    android_key_hash: Optional[str] = None,
    application_id: Optional[str] = None,
    attempt: Optional[int] = None,
    audience_exp: Optional[bool] = None,
    backdated_time: Optional[str] = None,
    backdated_time_granularity: Optional[str] = None,
    caption: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    feed_targeting: Optional[str] = None,
    filter_type: Optional[int] = None,
    full_res_is_coming_later: Optional[bool] = None,
    initial_view_heading_override_degrees: Optional[int] = None,
    initial_view_pitch_override_degrees: Optional[int] = None,
    initial_view_vertical_fov_override_degrees: Optional[int] = None,
    ios_bundle_id: Optional[str] = None,
    is_explicit_location: Optional[bool] = None,
    is_explicit_place: Optional[bool] = None,
    location_source_id: Optional[str] = None,
    manual_privacy: Optional[bool] = None,
    message: Optional[str] = None,
    name: Optional[str] = None,
    nectar_module: Optional[str] = None,
    no_story: Optional[bool] = None,
    offline_id: Optional[int] = None,
    og_action_type_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_set_profile_badge: Optional[bool] = None,
    og_suggestion_mechanism: Optional[str] = None,
    parent_media_id: Optional[int] = None,
    place: Optional[str] = None,
    privacy: Optional[str] = None,
    profile_id: Optional[int] = None,
    provenance_info: Optional[str] = None,
    proxied_app_id: Optional[str] = None,
    published: Optional[bool] = None,
    qn: Optional[str] = None,
    scheduled_publish_time: Optional[int] = None,
    spherical_metadata: Optional[str] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    tags: Optional[str] = None,
    target_id: Optional[int] = None,
    targeting: Optional[str] = None,
    temporary: Optional[bool] = None,
    time_since_original_post: Optional[int] = None,
    uid: Optional[int] = None,
    unpublished_content_type: Optional[str] = None,
    url: Optional[str] = None,
    user_selected_tags: Optional[bool] = None,
    vault_image_id: Optional[str] = None,
) -> str:
    """POST /photos on Page.

    Args:
        page_id: The ID of the Page object.
        aid: Optional.
        allow_spherical_photo: Optional.
        alt_text_custom: Optional.
        android_key_hash: Optional.
        application_id: Optional.
        attempt: Optional.
        audience_exp: Optional.
        backdated_time: Optional.
        backdated_time_granularity: Optional. Values: day, hour, min, month, none, year
        caption: Optional.
        composer_session_id: Optional.
        direct_share_status: Optional.
        feed_targeting: Optional.
        filter_type: Optional.
        full_res_is_coming_later: Optional.
        initial_view_heading_override_degrees: Optional.
        initial_view_pitch_override_degrees: Optional.
        initial_view_vertical_fov_override_degrees: Optional.
        ios_bundle_id: Optional.
        is_explicit_location: Optional.
        is_explicit_place: Optional.
        location_source_id: Optional.
        manual_privacy: Optional.
        message: Optional.
        name: Optional.
        nectar_module: Optional.
        no_story: Optional.
        offline_id: Optional.
        og_action_type_id: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_set_profile_badge: Optional.
        og_suggestion_mechanism: Optional.
        parent_media_id: Optional.
        place: Optional.
        privacy: Optional.
        profile_id: Optional.
        provenance_info: Optional.
        proxied_app_id: Optional.
        published: Optional.
        qn: Optional.
        scheduled_publish_time: Optional.
        spherical_metadata: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        tags: Optional.
        target_id: Optional.
        targeting: Optional.
        temporary: Optional.
        time_since_original_post: Optional.
        uid: Optional.
        unpublished_content_type: Optional. Values: ADS_POST, DRAFT, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT, SCHEDULED, SCHEDULED_RECURRING
        url: Optional.
        user_selected_tags: Optional.
        vault_image_id: Optional.
    """
    params = {}
    if aid is not None:
        params["aid"] = aid
    if allow_spherical_photo is not None:
        params["allow_spherical_photo"] = allow_spherical_photo
    if alt_text_custom is not None:
        params["alt_text_custom"] = alt_text_custom
    if android_key_hash is not None:
        params["android_key_hash"] = android_key_hash
    if application_id is not None:
        params["application_id"] = application_id
    if attempt is not None:
        params["attempt"] = attempt
    if audience_exp is not None:
        params["audience_exp"] = audience_exp
    if backdated_time is not None:
        params["backdated_time"] = backdated_time
    if backdated_time_granularity is not None:
        params["backdated_time_granularity"] = backdated_time_granularity
    if caption is not None:
        params["caption"] = caption
    if composer_session_id is not None:
        params["composer_session_id"] = composer_session_id
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if feed_targeting is not None:
        params["feed_targeting"] = feed_targeting
    if filter_type is not None:
        params["filter_type"] = filter_type
    if full_res_is_coming_later is not None:
        params["full_res_is_coming_later"] = full_res_is_coming_later
    if initial_view_heading_override_degrees is not None:
        params["initial_view_heading_override_degrees"] = initial_view_heading_override_degrees
    if initial_view_pitch_override_degrees is not None:
        params["initial_view_pitch_override_degrees"] = initial_view_pitch_override_degrees
    if initial_view_vertical_fov_override_degrees is not None:
        params["initial_view_vertical_fov_override_degrees"] = initial_view_vertical_fov_override_degrees
    if ios_bundle_id is not None:
        params["ios_bundle_id"] = ios_bundle_id
    if is_explicit_location is not None:
        params["is_explicit_location"] = is_explicit_location
    if is_explicit_place is not None:
        params["is_explicit_place"] = is_explicit_place
    if location_source_id is not None:
        params["location_source_id"] = location_source_id
    if manual_privacy is not None:
        params["manual_privacy"] = manual_privacy
    if message is not None:
        params["message"] = message
    if name is not None:
        params["name"] = name
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if no_story is not None:
        params["no_story"] = no_story
    if offline_id is not None:
        params["offline_id"] = offline_id
    if og_action_type_id is not None:
        params["og_action_type_id"] = og_action_type_id
    if og_icon_id is not None:
        params["og_icon_id"] = og_icon_id
    if og_object_id is not None:
        params["og_object_id"] = og_object_id
    if og_phrase is not None:
        params["og_phrase"] = og_phrase
    if og_set_profile_badge is not None:
        params["og_set_profile_badge"] = og_set_profile_badge
    if og_suggestion_mechanism is not None:
        params["og_suggestion_mechanism"] = og_suggestion_mechanism
    if parent_media_id is not None:
        params["parent_media_id"] = parent_media_id
    if place is not None:
        params["place"] = place
    if privacy is not None:
        params["privacy"] = privacy
    if profile_id is not None:
        params["profile_id"] = profile_id
    if provenance_info is not None:
        params["provenance_info"] = provenance_info
    if proxied_app_id is not None:
        params["proxied_app_id"] = proxied_app_id
    if published is not None:
        params["published"] = published
    if qn is not None:
        params["qn"] = qn
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if spherical_metadata is not None:
        params["spherical_metadata"] = spherical_metadata
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if tags is not None:
        params["tags"] = tags
    if target_id is not None:
        params["target_id"] = target_id
    if targeting is not None:
        params["targeting"] = targeting
    if temporary is not None:
        params["temporary"] = temporary
    if time_since_original_post is not None:
        params["time_since_original_post"] = time_since_original_post
    if uid is not None:
        params["uid"] = uid
    if unpublished_content_type is not None:
        params["unpublished_content_type"] = unpublished_content_type
    if url is not None:
        params["url"] = url
    if user_selected_tags is not None:
        params["user_selected_tags"] = user_selected_tags
    if vault_image_id is not None:
        params["vault_image_id"] = vault_image_id
    result = await get_client().post(f"{page_id}/photos", data=params)
    return json.dumps(result, indent=2)


async def get_page_picture(
    page_id: str,
    fields: Optional[str] = None,
    height: Optional[int] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /picture on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        height: Optional.
        redirect: Optional.
        type_: Optional. Values: album, large, normal, small, square
        width: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if height is not None:
        params["height"] = height
    if redirect is not None:
        params["redirect"] = redirect
    if type_ is not None:
        params["type"] = type_
    if width is not None:
        params["width"] = width
    result = await get_client().get(f"{page_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def create_page_picture(
    page_id: str,
    android_key_hash: Optional[str] = None,
    burn_media_effect: Optional[bool] = None,
    caption: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    frame_entrypoint: Optional[str] = None,
    has_umg: Optional[bool] = None,
    height: Optional[int] = None,
    ios_bundle_id: Optional[str] = None,
    media_effect_ids: Optional[str] = None,
    media_effect_source_object_id: Optional[int] = None,
    msqrd_mask_id: Optional[str] = None,
    photo: Optional[str] = None,
    picture: Optional[str] = None,
    profile_pic_method: Optional[str] = None,
    profile_pic_source: Optional[str] = None,
    proxied_app_id: Optional[int] = None,
    qn: Optional[str] = None,
    reuse: Optional[bool] = None,
    scaled_crop_rect: Optional[str] = None,
    set_profile_photo_shield: Optional[str] = None,
    sticker_id: Optional[int] = None,
    sticker_source_object_id: Optional[int] = None,
    suppress_stories: Optional[bool] = None,
    width: Optional[int] = None,
    x: Optional[int] = None,
    y: Optional[int] = None,
) -> str:
    """POST /picture on Page.

    Args:
        page_id: The ID of the Page object.
        android_key_hash: Optional.
        burn_media_effect: Optional.
        caption: Optional.
        composer_session_id: Optional.
        frame_entrypoint: Optional.
        has_umg: Optional.
        height: Optional.
        ios_bundle_id: Optional.
        media_effect_ids: Optional.
        media_effect_source_object_id: Optional.
        msqrd_mask_id: Optional.
        photo: Optional.
        picture: Optional.
        profile_pic_method: Optional.
        profile_pic_source: Optional.
        proxied_app_id: Optional.
        qn: Optional.
        reuse: Optional.
        scaled_crop_rect: Optional.
        set_profile_photo_shield: Optional.
        sticker_id: Optional.
        sticker_source_object_id: Optional.
        suppress_stories: Optional.
        width: Optional.
        x: Optional.
        y: Optional.
    """
    params = {}
    if android_key_hash is not None:
        params["android_key_hash"] = android_key_hash
    if burn_media_effect is not None:
        params["burn_media_effect"] = burn_media_effect
    if caption is not None:
        params["caption"] = caption
    if composer_session_id is not None:
        params["composer_session_id"] = composer_session_id
    if frame_entrypoint is not None:
        params["frame_entrypoint"] = frame_entrypoint
    if has_umg is not None:
        params["has_umg"] = has_umg
    if height is not None:
        params["height"] = height
    if ios_bundle_id is not None:
        params["ios_bundle_id"] = ios_bundle_id
    if media_effect_ids is not None:
        params["media_effect_ids"] = media_effect_ids
    if media_effect_source_object_id is not None:
        params["media_effect_source_object_id"] = media_effect_source_object_id
    if msqrd_mask_id is not None:
        params["msqrd_mask_id"] = msqrd_mask_id
    if photo is not None:
        params["photo"] = photo
    if picture is not None:
        params["picture"] = picture
    if profile_pic_method is not None:
        params["profile_pic_method"] = profile_pic_method
    if profile_pic_source is not None:
        params["profile_pic_source"] = profile_pic_source
    if proxied_app_id is not None:
        params["proxied_app_id"] = proxied_app_id
    if qn is not None:
        params["qn"] = qn
    if reuse is not None:
        params["reuse"] = reuse
    if scaled_crop_rect is not None:
        params["scaled_crop_rect"] = scaled_crop_rect
    if set_profile_photo_shield is not None:
        params["set_profile_photo_shield"] = set_profile_photo_shield
    if sticker_id is not None:
        params["sticker_id"] = sticker_id
    if sticker_source_object_id is not None:
        params["sticker_source_object_id"] = sticker_source_object_id
    if suppress_stories is not None:
        params["suppress_stories"] = suppress_stories
    if width is not None:
        params["width"] = width
    if x is not None:
        params["x"] = x
    if y is not None:
        params["y"] = y
    result = await get_client().post(f"{page_id}/picture", data=params)
    return json.dumps(result, indent=2)


async def get_page_posts(
    page_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    limit: Optional[int] = None,
    q: Optional[str] = None,
    show_expired: Optional[bool] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        include_hidden: Optional.
        limit: Optional.
        q: Optional.
        show_expired: Optional.
        with_: Optional. Values: LOCATION
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_hidden is not None:
        params["include_hidden"] = include_hidden
    if limit is not None:
        params["limit"] = limit
    if q is not None:
        params["q"] = q
    if show_expired is not None:
        params["show_expired"] = show_expired
    if with_ is not None:
        params["with"] = with_
    result = await get_client().get(f"{page_id}/posts", params=params)
    return json.dumps(result, indent=2)


async def get_page_product_catalogs(page_id: str, fields: Optional[str] = None) -> str:
    """GET /product_catalogs on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_page_published_posts(
    page_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    limit: Optional[int] = None,
    show_expired: Optional[bool] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /published_posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        include_hidden: Optional.
        limit: Optional.
        show_expired: Optional.
        with_: Optional. Values: LOCATION
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_hidden is not None:
        params["include_hidden"] = include_hidden
    if limit is not None:
        params["limit"] = limit
    if show_expired is not None:
        params["show_expired"] = show_expired
    if with_ is not None:
        params["with"] = with_
    result = await get_client().get(f"{page_id}/published_posts", params=params)
    return json.dumps(result, indent=2)


async def get_page_ratings(page_id: str, fields: Optional[str] = None) -> str:
    """GET /ratings on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/ratings", params=params)
    return json.dumps(result, indent=2)


async def create_page_release_thread_control(page_id: str, recipient: str) -> str:
    """POST /release_thread_control on Page.

    Args:
        page_id: The ID of the Page object.
        recipient: Required.
    """
    params = {}
    params["recipient"] = recipient
    result = await get_client().post(f"{page_id}/release_thread_control", data=params)
    return json.dumps(result, indent=2)


async def create_page_request_thread_control(page_id: str, recipient: str, metadata: Optional[str] = None) -> str:
    """POST /request_thread_control on Page.

    Args:
        page_id: The ID of the Page object.
        metadata: Optional.
        recipient: Required.
    """
    params = {}
    if metadata is not None:
        params["metadata"] = metadata
    params["recipient"] = recipient
    result = await get_client().post(f"{page_id}/request_thread_control", data=params)
    return json.dumps(result, indent=2)


async def get_page_roles(
    page_id: str,
    fields: Optional[str] = None,
    include_deactivated: Optional[bool] = None,
    uid: Optional[int] = None,
) -> str:
    """GET /roles on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        include_deactivated: Optional.
        uid: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_deactivated is not None:
        params["include_deactivated"] = include_deactivated
    if uid is not None:
        params["uid"] = uid
    result = await get_client().get(f"{page_id}/roles", params=params)
    return json.dumps(result, indent=2)


async def get_page_rtb_dynamic_posts(page_id: str, fields: Optional[str] = None) -> str:
    """GET /rtb_dynamic_posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/rtb_dynamic_posts", params=params)
    return json.dumps(result, indent=2)


async def get_page_scheduled_posts(page_id: str, fields: Optional[str] = None) -> str:
    """GET /scheduled_posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/scheduled_posts", params=params)
    return json.dumps(result, indent=2)


async def get_page_secondary_receivers(page_id: str, fields: Optional[str] = None, platform: Optional[str] = None) -> str:
    """GET /secondary_receivers on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        platform: Optional. Values: INSTAGRAM, MESSENGER
    """
    params = {}
    params["fields"] = fields or "id,name"
    if platform is not None:
        params["platform"] = platform
    result = await get_client().get(f"{page_id}/secondary_receivers", params=params)
    return json.dumps(result, indent=2)


async def get_page_settings(page_id: str, fields: Optional[str] = None) -> str:
    """GET /settings on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/settings", params=params)
    return json.dumps(result, indent=2)


async def create_page_settings(page_id: str, option: Optional[str] = None) -> str:
    """POST /settings on Page.

    Args:
        page_id: The ID of the Page object.
        option: Optional.
    """
    params = {}
    if option is not None:
        params["option"] = option
    result = await get_client().post(f"{page_id}/settings", data=params)
    return json.dumps(result, indent=2)


async def get_page_shop_setup_status(page_id: str, fields: Optional[str] = None) -> str:
    """GET /shop_setup_status on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/shop_setup_status", params=params)
    return json.dumps(result, indent=2)


async def get_page_store_locations(page_id: str, fields: Optional[str] = None) -> str:
    """GET /store_locations on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/store_locations", params=params)
    return json.dumps(result, indent=2)


async def get_page_stories(
    page_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    status: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /stories on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        since: Optional.
        status: Optional. Values: ARCHIVED, PUBLISHED
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if since is not None:
        params["since"] = since
    if status is not None:
        params["status"] = status
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{page_id}/stories", params=params)
    return json.dumps(result, indent=2)


async def delete_page_subscribed_apps(page_id: str) -> str:
    """DELETE /subscribed_apps on Page.

    Args:
        page_id: The ID of the Page object.
    """
    params = {}
    result = await get_client().delete(f"{page_id}/subscribed_apps")
    return json.dumps(result, indent=2)


async def get_page_subscribed_apps(page_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_apps on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/subscribed_apps", params=params)
    return json.dumps(result, indent=2)


async def create_page_subscribed_apps(page_id: str, subscribed_fields: str) -> str:
    """POST /subscribed_apps on Page.

    Args:
        page_id: The ID of the Page object.
        subscribed_fields: Required. Values: affiliation, attire, awards, bio, birthday, business_integrity, call_permission_reply, call_settings_update, calls, category, checkins, comment_poll_response, company_overview, conversations, culinary_team, current_location, description, email, feature_access_list, feed, follow, founded, general_info, general_manager, group_feed, hometown, hours, inbox_labels, invalid_topic_placeholder, invoice_access_bank_slip_events, invoice_access_invoice_change, invoice_access_invoice_draft_change, invoice_access_onboarding_status_active, leadgen, leadgen_fat, live_videos, local_delivery, location, marketing_message_delivery_failed, marketing_message_echoes, marketing_messages_subscriber_upload_status, mcom_invoice_change, members, mention, merchant_review, message_context, message_deliveries, message_echoes, message_edits, message_mention, message_reactions, message_reads, message_template_status_update, messages, messaging_account_linking, messaging_appointments, messaging_checkout_updates, messaging_customer_information, messaging_direct_sends, messaging_fblogin_account_linking, messaging_feedback, messaging_game_plays, messaging_handovers, messaging_in_thread_lead_form_submit, messaging_integrity, messaging_optins, messaging_optouts, messaging_payments, messaging_policy_enforcement, messaging_postbacks, messaging_pre_checkouts, messaging_referrals, mission, name, page_about_story, page_change_proposal, page_upcoming_change, parking, payment_options, payment_request_update, personal_info, personal_interests, phone, picture, price_range, product_review, products, public_transit, publisher_subscriptions, ratings, registration, response_feedback, send_cart, standby, story_poll_response, story_share, user_action, video_text_question_responses, videos, website
    """
    params = {}
    params["subscribed_fields"] = subscribed_fields
    result = await get_client().post(f"{page_id}/subscribed_apps", data=params)
    return json.dumps(result, indent=2)


async def get_page_tabs(page_id: str, fields: Optional[str] = None, tab: Optional[str] = None) -> str:
    """GET /tabs on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        tab: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if tab is not None:
        params["tab"] = tab
    result = await get_client().get(f"{page_id}/tabs", params=params)
    return json.dumps(result, indent=2)


async def get_page_tagged(page_id: str, fields: Optional[str] = None) -> str:
    """GET /tagged on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/tagged", params=params)
    return json.dumps(result, indent=2)


async def create_page_take_thread_control(page_id: str, recipient: str, metadata: Optional[str] = None) -> str:
    """POST /take_thread_control on Page.

    Args:
        page_id: The ID of the Page object.
        metadata: Optional.
        recipient: Required.
    """
    params = {}
    if metadata is not None:
        params["metadata"] = metadata
    params["recipient"] = recipient
    result = await get_client().post(f"{page_id}/take_thread_control", data=params)
    return json.dumps(result, indent=2)


async def get_page_thread_owner(page_id: str, recipient: str, fields: Optional[str] = None) -> str:
    """GET /thread_owner on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        recipient: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["recipient"] = recipient
    result = await get_client().get(f"{page_id}/thread_owner", params=params)
    return json.dumps(result, indent=2)


async def get_page_threads(
    page_id: str,
    fields: Optional[str] = None,
    folder: Optional[str] = None,
    platform: Optional[str] = None,
    tags: Optional[str] = None,
    user_id: Optional[str] = None,
) -> str:
    """GET /threads on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        folder: Optional.
        platform: Optional. Values: INSTAGRAM, MESSENGER
        tags: Optional.
        user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if folder is not None:
        params["folder"] = folder
    if platform is not None:
        params["platform"] = platform
    if tags is not None:
        params["tags"] = tags
    if user_id is not None:
        params["user_id"] = user_id
    result = await get_client().get(f"{page_id}/threads", params=params)
    return json.dumps(result, indent=2)


async def create_page_unlink_accounts(page_id: str, psid: str) -> str:
    """POST /unlink_accounts on Page.

    Args:
        page_id: The ID of the Page object.
        psid: Required.
    """
    params = {}
    params["psid"] = psid
    result = await get_client().post(f"{page_id}/unlink_accounts", data=params)
    return json.dumps(result, indent=2)


async def get_page_video_copyright_rules(
    page_id: str,
    fields: Optional[str] = None,
    selected_rule_id: Optional[str] = None,
    source: Optional[str] = None,
) -> str:
    """GET /video_copyright_rules on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        selected_rule_id: Optional.
        source: Optional. Values: MATCH_SETTINGS_DIALOG, RULES_SELECTOR, RULES_TAB
    """
    params = {}
    params["fields"] = fields or "id,name"
    if selected_rule_id is not None:
        params["selected_rule_id"] = selected_rule_id
    if source is not None:
        params["source"] = source
    result = await get_client().get(f"{page_id}/video_copyright_rules", params=params)
    return json.dumps(result, indent=2)


async def create_page_video_copyright_rules(page_id: str, condition_groups: str, name: str) -> str:
    """POST /video_copyright_rules on Page.

    Args:
        page_id: The ID of the Page object.
        condition_groups: Required.
        name: Required.
    """
    params = {}
    params["condition_groups"] = condition_groups
    params["name"] = name
    result = await get_client().post(f"{page_id}/video_copyright_rules", data=params)
    return json.dumps(result, indent=2)


async def create_page_video_copyrights(
    page_id: str,
    copyright_content_id: str,
    attribution_id: Optional[str] = None,
    content_category: Optional[str] = None,
    excluded_ownership_countries: Optional[str] = None,
    excluded_ownership_segments: Optional[str] = None,
    is_reference_disabled: Optional[bool] = None,
    is_reference_video: Optional[bool] = None,
    monitoring_type: Optional[str] = None,
    ownership_countries: Optional[str] = None,
    rule_id: Optional[str] = None,
    tags: Optional[str] = None,
    whitelisted_ids: Optional[str] = None,
    whitelisted_ig_user_ids: Optional[str] = None,
) -> str:
    """POST /video_copyrights on Page.

    Args:
        page_id: The ID of the Page object.
        attribution_id: Optional.
        content_category: Optional. Values: episode, movie, web
        copyright_content_id: Required.
        excluded_ownership_countries: Optional.
        excluded_ownership_segments: Optional.
        is_reference_disabled: Optional.
        is_reference_video: Optional.
        monitoring_type: Optional. Values: AUDIO_ONLY, VIDEO_AND_AUDIO, VIDEO_ONLY
        ownership_countries: Optional.
        rule_id: Optional.
        tags: Optional.
        whitelisted_ids: Optional.
        whitelisted_ig_user_ids: Optional.
    """
    params = {}
    if attribution_id is not None:
        params["attribution_id"] = attribution_id
    if content_category is not None:
        params["content_category"] = content_category
    params["copyright_content_id"] = copyright_content_id
    if excluded_ownership_countries is not None:
        params["excluded_ownership_countries"] = excluded_ownership_countries
    if excluded_ownership_segments is not None:
        params["excluded_ownership_segments"] = excluded_ownership_segments
    if is_reference_disabled is not None:
        params["is_reference_disabled"] = is_reference_disabled
    if is_reference_video is not None:
        params["is_reference_video"] = is_reference_video
    if monitoring_type is not None:
        params["monitoring_type"] = monitoring_type
    if ownership_countries is not None:
        params["ownership_countries"] = ownership_countries
    if rule_id is not None:
        params["rule_id"] = rule_id
    if tags is not None:
        params["tags"] = tags
    if whitelisted_ids is not None:
        params["whitelisted_ids"] = whitelisted_ids
    if whitelisted_ig_user_ids is not None:
        params["whitelisted_ig_user_ids"] = whitelisted_ig_user_ids
    result = await get_client().post(f"{page_id}/video_copyrights", data=params)
    return json.dumps(result, indent=2)


async def get_page_video_lists(page_id: str, fields: Optional[str] = None) -> str:
    """GET /video_lists on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_id}/video_lists", params=params)
    return json.dumps(result, indent=2)


async def get_page_video_reels(
    page_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /video_reels on Page.

    Args:
        page_id: The ID of the Page object.
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
    result = await get_client().get(f"{page_id}/video_reels", params=params)
    return json.dumps(result, indent=2)


async def create_page_video_reels(
    page_id: str,
    upload_phase: str,
    description: Optional[str] = None,
    feed_targeting: Optional[str] = None,
    place: Optional[str] = None,
    scheduled_publish_time: Optional[str] = None,
    targeting: Optional[str] = None,
    title: Optional[str] = None,
    video_id: Optional[str] = None,
    video_state: Optional[str] = None,
) -> str:
    """POST /video_reels on Page.

    Args:
        page_id: The ID of the Page object.
        description: Optional.
        feed_targeting: Optional.
        place: Optional.
        scheduled_publish_time: Optional.
        targeting: Optional.
        title: Optional.
        upload_phase: Required. Values: FINISH, START
        video_id: Optional.
        video_state: Optional. Values: DRAFT, PUBLISHED, SCHEDULED
    """
    params = {}
    if description is not None:
        params["description"] = description
    if feed_targeting is not None:
        params["feed_targeting"] = feed_targeting
    if place is not None:
        params["place"] = place
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if targeting is not None:
        params["targeting"] = targeting
    if title is not None:
        params["title"] = title
    params["upload_phase"] = upload_phase
    if video_id is not None:
        params["video_id"] = video_id
    if video_state is not None:
        params["video_state"] = video_state
    result = await get_client().post(f"{page_id}/video_reels", data=params)
    return json.dumps(result, indent=2)


async def create_page_video_stories(
    page_id: str,
    upload_phase: str,
    description: Optional[str] = None,
    feed_targeting: Optional[str] = None,
    place: Optional[str] = None,
    scheduled_publish_time: Optional[str] = None,
    targeting: Optional[str] = None,
    title: Optional[str] = None,
    video_id: Optional[str] = None,
    video_state: Optional[str] = None,
) -> str:
    """POST /video_stories on Page.

    Args:
        page_id: The ID of the Page object.
        description: Optional.
        feed_targeting: Optional.
        place: Optional.
        scheduled_publish_time: Optional.
        targeting: Optional.
        title: Optional.
        upload_phase: Required. Values: FINISH, START
        video_id: Optional.
        video_state: Optional. Values: DRAFT, PUBLISHED, SCHEDULED
    """
    params = {}
    if description is not None:
        params["description"] = description
    if feed_targeting is not None:
        params["feed_targeting"] = feed_targeting
    if place is not None:
        params["place"] = place
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if targeting is not None:
        params["targeting"] = targeting
    if title is not None:
        params["title"] = title
    params["upload_phase"] = upload_phase
    if video_id is not None:
        params["video_id"] = video_id
    if video_state is not None:
        params["video_state"] = video_state
    result = await get_client().post(f"{page_id}/video_stories", data=params)
    return json.dumps(result, indent=2)


async def get_page_videos(page_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /videos on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: TAGGED, UPLOADED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{page_id}/videos", params=params)
    return json.dumps(result, indent=2)


async def create_page_videos(
    page_id: str,
    ad_breaks: Optional[str] = None,
    application_id: Optional[str] = None,
    asked_fun_fact_prompt_id: Optional[int] = None,
    audio_story_wave_animation_handle: Optional[str] = None,
    backdated_post: Optional[str] = None,
    call_to_action: Optional[str] = None,
    composer_entry_picker: Optional[str] = None,
    composer_entry_point: Optional[str] = None,
    composer_entry_time: Optional[int] = None,
    composer_session_events_log: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    composer_source_surface: Optional[str] = None,
    composer_type: Optional[str] = None,
    container_type: Optional[str] = None,
    content_category: Optional[str] = None,
    content_tags: Optional[str] = None,
    creative_tools: Optional[str] = None,
    crossposted_video_id: Optional[str] = None,
    custom_labels: Optional[str] = None,
    description: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    embeddable: Optional[bool] = None,
    end_offset: Optional[int] = None,
    expiration: Optional[str] = None,
    fbuploader_video_file_chunk: Optional[str] = None,
    feed_targeting: Optional[str] = None,
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
    is_explicit_share: Optional[bool] = None,
    is_group_linking_post: Optional[bool] = None,
    is_partnership_ad: Optional[bool] = None,
    is_voice_clip: Optional[bool] = None,
    location_source_id: Optional[str] = None,
    manual_privacy: Optional[bool] = None,
    multilingual_data: Optional[str] = None,
    no_story: Optional[bool] = None,
    og_action_type_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_suggestion_mechanism: Optional[str] = None,
    original_fov: Optional[int] = None,
    original_projection_type: Optional[str] = None,
    partnership_ad_ad_code: Optional[str] = None,
    publish_event_id: Optional[int] = None,
    published: Optional[bool] = None,
    reference_only: Optional[bool] = None,
    referenced_sticker_id: Optional[str] = None,
    replace_video_id: Optional[str] = None,
    scheduled_publish_time: Optional[int] = None,
    secret: Optional[bool] = None,
    slideshow_spec: Optional[str] = None,
    social_actions: Optional[bool] = None,
    source: Optional[str] = None,
    source_instagram_media_id: Optional[str] = None,
    specified_dialect: Optional[str] = None,
    spherical: Optional[bool] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    start_offset: Optional[int] = None,
    swap_mode: Optional[str] = None,
    targeting: Optional[str] = None,
    text_format_metadata: Optional[str] = None,
    thumb: Optional[str] = None,
    time_since_original_post: Optional[int] = None,
    title: Optional[str] = None,
    transcode_setting_properties: Optional[str] = None,
    universal_video_id: Optional[str] = None,
    unpublished_content_type: Optional[str] = None,
    upload_phase: Optional[str] = None,
    upload_session_id: Optional[str] = None,
    upload_setting_properties: Optional[str] = None,
    video_asset_id: Optional[str] = None,
    video_file_chunk: Optional[str] = None,
    video_id_original: Optional[str] = None,
    video_start_time_ms: Optional[int] = None,
    waterfall_id: Optional[str] = None,
) -> str:
    """POST /videos on Page.

    Args:
        page_id: The ID of the Page object.
        ad_breaks: Optional.
        application_id: Optional.
        asked_fun_fact_prompt_id: Optional.
        audio_story_wave_animation_handle: Optional.
        backdated_post: Optional.
        call_to_action: Optional.
        composer_entry_picker: Optional.
        composer_entry_point: Optional.
        composer_entry_time: Optional.
        composer_session_events_log: Optional.
        composer_session_id: Optional.
        composer_source_surface: Optional.
        composer_type: Optional.
        container_type: Optional. Values: ACO_VIDEO_VARIATION, ADS_AI_GENERATED, AD_BREAK_PREVIEW, AD_DERIVATIVE, AD_LIBRARY_WATERMARK, ALBUM_MULTIMEDIA_POST, ALOHA_SUPERFRAME, APP_REREVIEW_SCREENCAST, APP_REVIEW_SCREENCAST, ASSET_MANAGER, ATLAS_VIDEO, AUDIO_BROADCAST, AUDIO_COMMENT, BROADCAST, CANVAS, CMS_MEDIA_MANAGER, CONTAINED_POST_ATTACHMENT, CONTAINED_POST_AUDIO_BROADCAST, CONTAINED_POST_COPYRIGHT_REFERENCE_BROADCAST, COPYRIGHT_REFERENCE_BROADCAST, COPYRIGHT_REFERENCE_IG_XPOST_VIDEO, COPYRIGHT_REFERENCE_VIDEO, CREATION_ML_PRECREATION, CREATOR_FAN_CHALLENGE, CREATOR_STOREFRONT_PERSONALIZED_VIDEO, CREATOR_STOREFRONT_PROMOTIONAL_VIDEO, DATAGENIX_VIDEO, DCO_AD_ASSET_FEED, DCO_AUTOGEN_VIDEO, DCO_TRIMMED_VIDEO, DIM_SUM, DIRECTED_POST_ATTACHMENT, DIRECT_INBOX, DOUBLE_PROD_EXPERIMENT, DROPS_SHOPPING_EVENT_PAGE, DYNAMIC_ITEM_VIDEO, DYNAMIC_TEMPLATE_VIDEO, EVENT_COVER_VIDEO, EVENT_TOUR, FACECAST_DVR, FB_AVATAR_ANIMATED_SATP, FB_COLLECTIBLE_VIDEO, FB_SHORTS, FB_SHORTS_CONTENT_REMIXABLE, FB_SHORTS_GROUP_POST, FB_SHORTS_LINKED_PRODUCT, FB_SHORTS_PMV_POST, FB_SHORTS_POST, FB_SHORTS_REMIX_POST, FUNDRAISER_COVER_VIDEO, GAME_CLIP, GIF_TO_VIDEO, GOODWILL_ANNIVERSARY_DEPRECATED, GOODWILL_ANNIVERSARY_PROMOTION_DEPRECATED, GOODWILL_VIDEO_CONTAINED_SHARE, GOODWILL_VIDEO_PROMOTION, GOODWILL_VIDEO_SHARE, GOODWILL_VIDEO_TOKEN_REQUIRED, GROUP_POST, HEURISTIC_CLUSTER_VIDEO, HIGHLIGHT_CLIP_VIDEO, HORIZON_WORLDS_TV, HUDDLE_BROADCAST, IG_REELS_XPV, INSPIRATION_VIDEO, INSTAGRAM_VIDEO_COPY, INSTANT_APPLICATION_PREVIEW, INSTANT_ARTICLE, ISSUE_MODULE, LEARN, LEGACY, LEGACY_CONTAINED_POST_BROADCAST, LIVE_AUDIO_ROOM_BROADCAST, LIVE_CLIP_PREVIEW, LIVE_CLIP_WORKCHAT, LIVE_CREATIVE_KIT_VIDEO, LIVE_PHOTO, LOOK_NOW_DEPRECATED, MARKETPLACE_LISTING_VIDEO, MARKETPLACE_PRE_RECORDED_VIDEO, MOMENTS_VIDEO, MUSIC_CLIP, MUSIC_CLIP_IN_COMMENT, MUSIC_CLIP_IN_LIGHTWEIGHT_STATUS, MUSIC_CLIP_IN_MAPLE_POST, MUSIC_CLIP_IN_MSGR_NOTE, MUSIC_CLIP_IN_POLL_OPTION, MUSIC_CLIP_ON_DATING_PROFILE, NEO_ASYNC_GAME_VIDEO, NEW_CONTAINED_POST_BROADCAST, NO_STORY, OCULUS_CREATOR_PORTAL, OCULUS_VENUES_BROADCAST, ORIGINALITY_SELF_ADVOCACY, PAGES_COVER_VIDEO, PAGE_REVIEW_SCREENCAST, PAGE_SLIDESHOW_VIDEO, PAID_CONTENT_PREVIEW, PAID_CONTENT_VIDEO, PAID_CONTENT_VIDEO__POST, PIXELCLOUD, PODCAST_HIGHLIGHT, PODCAST_ML_PREVIEW, PODCAST_ML_PREVIEW_NO_NEWSFEED_STORY, PODCAST_RSS, PODCAST_RSS_EPHEMERAL, PODCAST_RSS_NO_NEWSFEED_STORY, PODCAST_VOICES, PODCAST_VOICES_NO_NEWSFEED_STORY, PREMIERE_SOURCE, PREMIUM_MUSIC_VIDEO_CLIP, PREMIUM_MUSIC_VIDEO_CROPPED_CLIP, PREMIUM_MUSIC_VIDEO_NO_NEWSFEED_STORY, PREMIUM_MUSIC_VIDEO_WITH_NEWSFEED_STORY, PRIVATE_GALLERY_VIDEO, PRODUCT_VIDEO, PROFILE_COVER_VIDEO, PROFILE_INTRO_CARD, PROFILE_VIDEO, PROTON, QUICK_CLIP_WORKPLACE_POST, QUICK_PROMOTION, REPLACE_VIDEO, SHOWREEL_NATIVE_DUMMY_VIDEO, SLIDESHOW_ANIMOTO, SLIDESHOW_SHAKR, SLIDESHOW_VARIATION_VIDEO, SOUND_PLATFORM_STREAM, SRT_ATTACHMENT, STORIES_VIDEO, STORYLINE, STORYLINE_WITH_EXTERNAL_MUSIC, STORY_ARCHIVE_VIDEO, STORY_CARD_TEMPLATE, STREAM_HIGHLIGHTS_VIDEO, TAROT_DIGEST, TEMPORARY, TEMPORARY_UNLISTED, TEMP_VIDEO_COPYRIGHT_SCAN, UNLISTED, UNLISTED_OCULUS, VIDEO_COMMENT, VIDEO_COMPOSITION_VARIATION, VIDEO_CREATIVE_EDITOR_AUTOGEN_AD_VIDEO, VIDEO_SUPERRES, VU_GENERATED_VIDEO, WOODHENGE, WORK_KNOWLEDGE_VIDEO, YOUR_DAY
        content_category: Optional. Values: BEAUTY_FASHION, BUSINESS, CARS_TRUCKS, COMEDY, CUTE_ANIMALS, ENTERTAINMENT, FAMILY, FOOD_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, OTHER, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO_GAMING
        content_tags: Optional.
        creative_tools: Optional.
        crossposted_video_id: Optional.
        custom_labels: Optional.
        description: Optional.
        direct_share_status: Optional.
        embeddable: Optional.
        end_offset: Optional.
        expiration: Optional.
        fbuploader_video_file_chunk: Optional.
        feed_targeting: Optional.
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
        is_explicit_share: Optional.
        is_group_linking_post: Optional.
        is_partnership_ad: Optional.
        is_voice_clip: Optional.
        location_source_id: Optional.
        manual_privacy: Optional.
        multilingual_data: Optional.
        no_story: Optional.
        og_action_type_id: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_suggestion_mechanism: Optional.
        original_fov: Optional.
        original_projection_type: Optional. Values: cubemap, equirectangular, half_equirectangular
        partnership_ad_ad_code: Optional.
        publish_event_id: Optional.
        published: Optional.
        reference_only: Optional.
        referenced_sticker_id: Optional.
        replace_video_id: Optional.
        scheduled_publish_time: Optional.
        secret: Optional.
        slideshow_spec: Optional.
        social_actions: Optional.
        source: Optional.
        source_instagram_media_id: Optional.
        specified_dialect: Optional.
        spherical: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        start_offset: Optional.
        swap_mode: Optional. Values: replace
        targeting: Optional.
        text_format_metadata: Optional.
        thumb: Optional.
        time_since_original_post: Optional.
        title: Optional.
        transcode_setting_properties: Optional.
        universal_video_id: Optional.
        unpublished_content_type: Optional. Values: ADS_POST, DRAFT, INLINE_CREATED, PUBLISHED, REVIEWABLE_BRANDED_CONTENT, SCHEDULED, SCHEDULED_RECURRING
        upload_phase: Optional. Values: cancel, finish, start, transfer
        upload_session_id: Optional.
        upload_setting_properties: Optional.
        video_asset_id: Optional.
        video_file_chunk: Optional.
        video_id_original: Optional.
        video_start_time_ms: Optional.
        waterfall_id: Optional.
    """
    params = {}
    if ad_breaks is not None:
        params["ad_breaks"] = ad_breaks
    if application_id is not None:
        params["application_id"] = application_id
    if asked_fun_fact_prompt_id is not None:
        params["asked_fun_fact_prompt_id"] = asked_fun_fact_prompt_id
    if audio_story_wave_animation_handle is not None:
        params["audio_story_wave_animation_handle"] = audio_story_wave_animation_handle
    if backdated_post is not None:
        params["backdated_post"] = backdated_post
    if call_to_action is not None:
        params["call_to_action"] = call_to_action
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
    if content_tags is not None:
        params["content_tags"] = content_tags
    if creative_tools is not None:
        params["creative_tools"] = creative_tools
    if crossposted_video_id is not None:
        params["crossposted_video_id"] = crossposted_video_id
    if custom_labels is not None:
        params["custom_labels"] = custom_labels
    if description is not None:
        params["description"] = description
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if embeddable is not None:
        params["embeddable"] = embeddable
    if end_offset is not None:
        params["end_offset"] = end_offset
    if expiration is not None:
        params["expiration"] = expiration
    if fbuploader_video_file_chunk is not None:
        params["fbuploader_video_file_chunk"] = fbuploader_video_file_chunk
    if feed_targeting is not None:
        params["feed_targeting"] = feed_targeting
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
    if is_explicit_share is not None:
        params["is_explicit_share"] = is_explicit_share
    if is_group_linking_post is not None:
        params["is_group_linking_post"] = is_group_linking_post
    if is_partnership_ad is not None:
        params["is_partnership_ad"] = is_partnership_ad
    if is_voice_clip is not None:
        params["is_voice_clip"] = is_voice_clip
    if location_source_id is not None:
        params["location_source_id"] = location_source_id
    if manual_privacy is not None:
        params["manual_privacy"] = manual_privacy
    if multilingual_data is not None:
        params["multilingual_data"] = multilingual_data
    if no_story is not None:
        params["no_story"] = no_story
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
    if published is not None:
        params["published"] = published
    if reference_only is not None:
        params["reference_only"] = reference_only
    if referenced_sticker_id is not None:
        params["referenced_sticker_id"] = referenced_sticker_id
    if replace_video_id is not None:
        params["replace_video_id"] = replace_video_id
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if secret is not None:
        params["secret"] = secret
    if slideshow_spec is not None:
        params["slideshow_spec"] = slideshow_spec
    if social_actions is not None:
        params["social_actions"] = social_actions
    if source is not None:
        params["source"] = source
    if source_instagram_media_id is not None:
        params["source_instagram_media_id"] = source_instagram_media_id
    if specified_dialect is not None:
        params["specified_dialect"] = specified_dialect
    if spherical is not None:
        params["spherical"] = spherical
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if start_offset is not None:
        params["start_offset"] = start_offset
    if swap_mode is not None:
        params["swap_mode"] = swap_mode
    if targeting is not None:
        params["targeting"] = targeting
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
    if universal_video_id is not None:
        params["universal_video_id"] = universal_video_id
    if unpublished_content_type is not None:
        params["unpublished_content_type"] = unpublished_content_type
    if upload_phase is not None:
        params["upload_phase"] = upload_phase
    if upload_session_id is not None:
        params["upload_session_id"] = upload_session_id
    if upload_setting_properties is not None:
        params["upload_setting_properties"] = upload_setting_properties
    if video_asset_id is not None:
        params["video_asset_id"] = video_asset_id
    if video_file_chunk is not None:
        params["video_file_chunk"] = video_file_chunk
    if video_id_original is not None:
        params["video_id_original"] = video_id_original
    if video_start_time_ms is not None:
        params["video_start_time_ms"] = video_start_time_ms
    if waterfall_id is not None:
        params["waterfall_id"] = waterfall_id
    result = await get_client().post(f"{page_id}/videos", data=params)
    return json.dumps(result, indent=2)


async def get_page_visitor_posts(
    page_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    limit: Optional[int] = None,
    show_expired: Optional[bool] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /visitor_posts on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        include_hidden: Optional.
        limit: Optional.
        show_expired: Optional.
        with_: Optional. Values: LOCATION
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_hidden is not None:
        params["include_hidden"] = include_hidden
    if limit is not None:
        params["limit"] = limit
    if show_expired is not None:
        params["show_expired"] = show_expired
    if with_ is not None:
        params["with"] = with_
    result = await get_client().get(f"{page_id}/visitor_posts", params=params)
    return json.dumps(result, indent=2)


async def delete_page_welcome_message_flows(page_id: str, flow_id: str) -> str:
    """DELETE /welcome_message_flows on Page.

    Args:
        page_id: The ID of the Page object.
        flow_id: Required.
    """
    params = {}
    params["flow_id"] = flow_id
    result = await get_client().delete(f"{page_id}/welcome_message_flows")
    return json.dumps(result, indent=2)


async def get_page_welcome_message_flows(
    page_id: str,
    fields: Optional[str] = None,
    app_id: Optional[str] = None,
    flow_id: Optional[str] = None,
) -> str:
    """GET /welcome_message_flows on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return.
        app_id: Optional.
        flow_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app_id is not None:
        params["app_id"] = app_id
    if flow_id is not None:
        params["flow_id"] = flow_id
    result = await get_client().get(f"{page_id}/welcome_message_flows", params=params)
    return json.dumps(result, indent=2)


async def create_page_welcome_message_flows(
    page_id: str,
    eligible_platforms: Optional[str] = None,
    flow_id: Optional[str] = None,
    name: Optional[str] = None,
    welcome_message_flow: Optional[str] = None,
) -> str:
    """POST /welcome_message_flows on Page.

    Args:
        page_id: The ID of the Page object.
        eligible_platforms: Optional. Values: INSTAGRAM, MESSENGER, WHATSAPP
        flow_id: Optional.
        name: Optional.
        welcome_message_flow: Optional.
    """
    params = {}
    if eligible_platforms is not None:
        params["eligible_platforms"] = eligible_platforms
    if flow_id is not None:
        params["flow_id"] = flow_id
    if name is not None:
        params["name"] = name
    if welcome_message_flow is not None:
        params["welcome_message_flow"] = welcome_message_flow
    result = await get_client().post(f"{page_id}/welcome_message_flows", data=params)
    return json.dumps(result, indent=2)


async def get_page(
    page_id: str,
    fields: Optional[str] = None,
    account_linking_token: Optional[str] = None,
) -> str:
    """GET /#get on Page.

    Args:
        page_id: The ID of the Page object.
        fields: Comma-separated list of fields to return. Available: about, access_token, ad_campaign, affiliation, app_id, artists_we_like, attire, available_promo_offer_ids, awards, band_interests, band_members, best_page, bio, birthday, booking_agent, breaking_news_usage, built, business, can_checkin, can_post, category, category_list, checkins, company_overview, connected_instagram_account, connected_page_backed_instagram_account, contact_address, copyright_attribution_insights, copyright_whitelisted_ig_partners, country_page_likes, cover, culinary_team, current_location, delivery_and_pickup_option_info, description, description_html, differently_open_offerings, directed_by, display_subtext, displayed_message_response_time, does_viewer_have_page_permission_link_ig, emails, engagement, fan_count, featured_video, features, followers_count, food_styles, founded, general_info, general_manager, genre, global_brand_page_name, global_brand_root_id, has_added_app, has_lead_access, has_transitioned_to_new_page_experience, has_whatsapp_business_number, has_whatsapp_number, hometown, hours, id, impressum, influences, instagram_business_account, is_always_open, is_calling_eligible, is_chain, is_community_page, is_eligible_for_branded_content, is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web, is_messenger_bot_get_started_enabled, is_messenger_platform_bot, is_owned, is_permanently_closed, is_published, is_unclaimed, is_verified, is_webhooks_subscribed, keywords, leadgen_tos_acceptance_time, leadgen_tos_accepted, leadgen_tos_accepting_user, link, location, members, merchant_id, merchant_review_status, messaging_feature_status, messenger_ads_default_icebreakers, messenger_ads_default_quick_replies, messenger_ads_quick_replies_type, mini_shop_storefront, mission, mpg, name, name_with_location_descriptor, network, new_like_count, offer_eligible, overall_star_rating, owner_business, page_token, parent_page, parking, payment_options, personal_info, personal_interests, pharma_safety_info, phone, pickup_options, place_type, plot_outline, preferred_audience, press_contact, price_range, privacy_info_url, produced_by, products, promotion_eligible, promotion_ineligible_reason, public_transit, rating_count, recipient, record_label, release_date, restaurant_services, restaurant_specialties, schedule, screenplay_by, season, single_line_address, starring, start_info, store_code, store_location_descriptor, store_number, studio, supports_donate_button_in_live_video, talking_about_count, temporary_status, unread_message_count, unread_notif_count, unseen_message_count, user_access_expire_time, username, verification_status, voip_info, website, were_here_count, whatsapp_number, written_by
        account_linking_token: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if account_linking_token is not None:
        params["account_linking_token"] = account_linking_token
    result = await get_client().get(f"{page_id}", params=params)
    return json.dumps(result, indent=2)


async def update_page(
    page_id: str,
    about: Optional[str] = None,
    accept_crossposting_handshake: Optional[str] = None,
    allow_spherical_photo: Optional[bool] = None,
    attire: Optional[str] = None,
    begin_crossposting_handshake: Optional[str] = None,
    bio: Optional[str] = None,
    category_list: Optional[str] = None,
    company_overview: Optional[str] = None,
    contact_address: Optional[str] = None,
    cover: Optional[str] = None,
    culinary_team: Optional[str] = None,
    delivery_and_pickup_option_info: Optional[str] = None,
    description: Optional[str] = None,
    differently_open_offerings: Optional[str] = None,
    directed_by: Optional[str] = None,
    displayed_message_response_time: Optional[str] = None,
    emails: Optional[str] = None,
    focus_x: Optional[float] = None,
    focus_y: Optional[float] = None,
    food_styles: Optional[str] = None,
    gen_ai_provenance_type: Optional[str] = None,
    general_info: Optional[str] = None,
    general_manager: Optional[str] = None,
    genre: Optional[str] = None,
    hours: Optional[str] = None,
    ignore_coordinate_warnings: Optional[bool] = None,
    impressum: Optional[str] = None,
    is_always_open: Optional[bool] = None,
    is_permanently_closed: Optional[bool] = None,
    is_published: Optional[bool] = None,
    is_webhooks_subscribed: Optional[bool] = None,
    location: Optional[str] = None,
    menu: Optional[str] = None,
    mission: Optional[str] = None,
    no_feed_story: Optional[bool] = None,
    no_notification: Optional[bool] = None,
    offset_x: Optional[int] = None,
    offset_y: Optional[int] = None,
    parking: Optional[str] = None,
    payment_options: Optional[str] = None,
    phone: Optional[str] = None,
    pickup_options: Optional[str] = None,
    plot_outline: Optional[str] = None,
    price_range: Optional[str] = None,
    priority_hours: Optional[str] = None,
    public_transit: Optional[str] = None,
    restaurant_services: Optional[str] = None,
    restaurant_specialties: Optional[str] = None,
    scrape: Optional[bool] = None,
    service_details: Optional[str] = None,
    spherical_metadata: Optional[str] = None,
    start_info: Optional[str] = None,
    store_location_descriptor: Optional[str] = None,
    temporary_status: Optional[str] = None,
    website: Optional[str] = None,
    zoom_scale_x: Optional[float] = None,
    zoom_scale_y: Optional[float] = None,
) -> str:
    """POST /#update on Page.

    Args:
        page_id: The ID of the Page object.
        about: Optional.
        accept_crossposting_handshake: Optional.
        allow_spherical_photo: Optional.
        attire: Optional.
        begin_crossposting_handshake: Optional.
        bio: Optional.
        category_list: Optional.
        company_overview: Optional.
        contact_address: Optional.
        cover: Optional.
        culinary_team: Optional.
        delivery_and_pickup_option_info: Optional.
        description: Optional.
        differently_open_offerings: Optional.
        directed_by: Optional.
        displayed_message_response_time: Optional.
        emails: Optional.
        focus_x: Optional.
        focus_y: Optional.
        food_styles: Optional.
        gen_ai_provenance_type: Optional.
        general_info: Optional.
        general_manager: Optional.
        genre: Optional.
        hours: Optional.
        ignore_coordinate_warnings: Optional.
        impressum: Optional.
        is_always_open: Optional.
        is_permanently_closed: Optional.
        is_published: Optional.
        is_webhooks_subscribed: Optional.
        location: Optional.
        menu: Optional.
        mission: Optional.
        no_feed_story: Optional.
        no_notification: Optional.
        offset_x: Optional.
        offset_y: Optional.
        parking: Optional.
        payment_options: Optional.
        phone: Optional.
        pickup_options: Optional.
        plot_outline: Optional.
        price_range: Optional.
        priority_hours: Optional.
        public_transit: Optional.
        restaurant_services: Optional.
        restaurant_specialties: Optional.
        scrape: Optional.
        service_details: Optional.
        spherical_metadata: Optional.
        start_info: Optional.
        store_location_descriptor: Optional.
        temporary_status: Optional.
        website: Optional.
        zoom_scale_x: Optional.
        zoom_scale_y: Optional.
    """
    params = {}
    if about is not None:
        params["about"] = about
    if accept_crossposting_handshake is not None:
        params["accept_crossposting_handshake"] = accept_crossposting_handshake
    if allow_spherical_photo is not None:
        params["allow_spherical_photo"] = allow_spherical_photo
    if attire is not None:
        params["attire"] = attire
    if begin_crossposting_handshake is not None:
        params["begin_crossposting_handshake"] = begin_crossposting_handshake
    if bio is not None:
        params["bio"] = bio
    if category_list is not None:
        params["category_list"] = category_list
    if company_overview is not None:
        params["company_overview"] = company_overview
    if contact_address is not None:
        params["contact_address"] = contact_address
    if cover is not None:
        params["cover"] = cover
    if culinary_team is not None:
        params["culinary_team"] = culinary_team
    if delivery_and_pickup_option_info is not None:
        params["delivery_and_pickup_option_info"] = delivery_and_pickup_option_info
    if description is not None:
        params["description"] = description
    if differently_open_offerings is not None:
        params["differently_open_offerings"] = differently_open_offerings
    if directed_by is not None:
        params["directed_by"] = directed_by
    if displayed_message_response_time is not None:
        params["displayed_message_response_time"] = displayed_message_response_time
    if emails is not None:
        params["emails"] = emails
    if focus_x is not None:
        params["focus_x"] = focus_x
    if focus_y is not None:
        params["focus_y"] = focus_y
    if food_styles is not None:
        params["food_styles"] = food_styles
    if gen_ai_provenance_type is not None:
        params["gen_ai_provenance_type"] = gen_ai_provenance_type
    if general_info is not None:
        params["general_info"] = general_info
    if general_manager is not None:
        params["general_manager"] = general_manager
    if genre is not None:
        params["genre"] = genre
    if hours is not None:
        params["hours"] = hours
    if ignore_coordinate_warnings is not None:
        params["ignore_coordinate_warnings"] = ignore_coordinate_warnings
    if impressum is not None:
        params["impressum"] = impressum
    if is_always_open is not None:
        params["is_always_open"] = is_always_open
    if is_permanently_closed is not None:
        params["is_permanently_closed"] = is_permanently_closed
    if is_published is not None:
        params["is_published"] = is_published
    if is_webhooks_subscribed is not None:
        params["is_webhooks_subscribed"] = is_webhooks_subscribed
    if location is not None:
        params["location"] = location
    if menu is not None:
        params["menu"] = menu
    if mission is not None:
        params["mission"] = mission
    if no_feed_story is not None:
        params["no_feed_story"] = no_feed_story
    if no_notification is not None:
        params["no_notification"] = no_notification
    if offset_x is not None:
        params["offset_x"] = offset_x
    if offset_y is not None:
        params["offset_y"] = offset_y
    if parking is not None:
        params["parking"] = parking
    if payment_options is not None:
        params["payment_options"] = payment_options
    if phone is not None:
        params["phone"] = phone
    if pickup_options is not None:
        params["pickup_options"] = pickup_options
    if plot_outline is not None:
        params["plot_outline"] = plot_outline
    if price_range is not None:
        params["price_range"] = price_range
    if priority_hours is not None:
        params["priority_hours"] = priority_hours
    if public_transit is not None:
        params["public_transit"] = public_transit
    if restaurant_services is not None:
        params["restaurant_services"] = restaurant_services
    if restaurant_specialties is not None:
        params["restaurant_specialties"] = restaurant_specialties
    if scrape is not None:
        params["scrape"] = scrape
    if service_details is not None:
        params["service_details"] = service_details
    if spherical_metadata is not None:
        params["spherical_metadata"] = spherical_metadata
    if start_info is not None:
        params["start_info"] = start_info
    if store_location_descriptor is not None:
        params["store_location_descriptor"] = store_location_descriptor
    if temporary_status is not None:
        params["temporary_status"] = temporary_status
    if website is not None:
        params["website"] = website
    if zoom_scale_x is not None:
        params["zoom_scale_x"] = zoom_scale_x
    if zoom_scale_y is not None:
        params["zoom_scale_y"] = zoom_scale_y
    result = await get_client().post(f"{page_id}", data=params)
    return json.dumps(result, indent=2)


PAGE_POST_FIELDS = [
    "actions",
    "admin_creator",
    "allowed_advertising_objectives",
    "application",
    "backdated_time",
    "call_to_action",
    "can_reply_privately",
    "child_attachments",
    "comments_mirroring_domain",
    "coordinates",
    "created_time",
    "event",
    "expanded_height",
    "expanded_width",
    "feed_targeting",
    "from",
    "full_picture",
    "height",
    "icon",
    "id",
    "instagram_eligibility",
    "is_app_share",
    "is_eligible_for_promotion",
    "is_expired",
    "is_hidden",
    "is_inline_created",
    "is_instagram_eligible",
    "is_popular",
    "is_published",
    "is_spherical",
    "message",
    "message_tags",
    "multi_share_end_card",
    "multi_share_optimized",
    "parent_id",
    "permalink_url",
    "picture",
    "place",
    "privacy",
    "promotable_id",
    "promotion_status",
    "properties",
    "scheduled_publish_time",
    "shares",
    "status_type",
    "story",
    "story_tags",
    "subscribed",
    "target",
    "targeting",
    "timeline_visibility",
    "updated_time",
    "via",
    "video_buying_eligibility",
    "width"
]


async def get_page_post_attachments(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /attachments on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/attachments", params=params)
    return json.dumps(result, indent=2)


async def get_page_post_comments(
    page_post_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
        filter_: Optional. Values: stream, toplevel
        live_filter: Optional. Values: filter_low_quality, no_filter
        order: Optional. Values: chronological, reverse_chronological
        since: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if filter_ is not None:
        params["filter"] = filter_
    if live_filter is not None:
        params["live_filter"] = live_filter
    if order is not None:
        params["order"] = order
    if since is not None:
        params["since"] = since
    result = await get_client().get(f"{page_post_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_page_post_comments(
    page_post_id: str,
    attachment_id: Optional[str] = None,
    attachment_share_url: Optional[str] = None,
    attachment_url: Optional[str] = None,
    comment: Optional[str] = None,
    comment_privacy_value: Optional[str] = None,
    feedback_source: Optional[str] = None,
    message: Optional[str] = None,
    nectar_module: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    post_id: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /comments on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        attachment_id: Optional.
        attachment_share_url: Optional.
        attachment_url: Optional.
        comment: Optional.
        comment_privacy_value: Optional. Values: DECLINED_BY_ADMIN_ASSISTANT, DEFAULT_PRIVACY, FRIENDS_AND_POST_OWNER, FRIENDS_ONLY, GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE, OWNER_OR_COMMENTER, PENDING_APPROVAL, REMOVED_BY_ADMIN_ASSISTANT, SIDE_CONVERSATION, SIDE_CONVERSATION_AND_POST_OWNER, SPOTLIGHT_TAB
        feedback_source: Optional.
        message: Optional.
        nectar_module: Optional.
        parent_comment_id: Optional.
        post_id: Optional.
        tracking: Optional.
    """
    params = {}
    if attachment_id is not None:
        params["attachment_id"] = attachment_id
    if attachment_share_url is not None:
        params["attachment_share_url"] = attachment_share_url
    if attachment_url is not None:
        params["attachment_url"] = attachment_url
    if comment is not None:
        params["comment"] = comment
    if comment_privacy_value is not None:
        params["comment_privacy_value"] = comment_privacy_value
    if feedback_source is not None:
        params["feedback_source"] = feedback_source
    if message is not None:
        params["message"] = message
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if parent_comment_id is not None:
        params["parent_comment_id"] = parent_comment_id
    if post_id is not None:
        params["post_id"] = post_id
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().post(f"{page_post_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_page_post_dynamic_posts(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /dynamic_posts on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/dynamic_posts", params=params)
    return json.dumps(result, indent=2)


async def get_page_post_insights(
    page_post_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    metric: Optional[str] = None,
    period: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
        date_preset: Optional. Values: data_maximum, last_14d, last_28d, last_30d, last_3d, last_7d, last_90d, last_month, last_quarter, last_week_mon_sun, last_week_sun_sat, last_year, maximum, this_month, this_quarter, this_week_mon_today, this_week_sun_today, this_year, today, yesterday
        metric: Optional.
        period: Optional. Values: day, days_28, lifetime, month, total_over_range, week
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if date_preset is not None:
        params["date_preset"] = date_preset
    if metric is not None:
        params["metric"] = metric
    if period is not None:
        params["period"] = period
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{page_post_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def delete_page_post_likes(
    page_post_id: str,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """DELETE /likes on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        nectar_module: Optional.
        tracking: Optional.
    """
    params = {}
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().delete(f"{page_post_id}/likes")
    return json.dumps(result, indent=2)


async def get_page_post_likes(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def create_page_post_likes(
    page_post_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        feedback_source: Optional.
        nectar_module: Optional.
        tracking: Optional.
    """
    params = {}
    if feedback_source is not None:
        params["feedback_source"] = feedback_source
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().post(f"{page_post_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_page_post_reactions(page_post_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /reactions on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: ANGRY, CARE, FIRE, HAHA, HUNDRED, LIKE, LOVE, NONE, PRIDE, SAD, THANKFUL, WOW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{page_post_id}/reactions", params=params)
    return json.dumps(result, indent=2)


async def get_page_post_sharedposts(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /sharedposts on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/sharedposts", params=params)
    return json.dumps(result, indent=2)


async def get_page_post_sponsor_tags(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /sponsor_tags on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/sponsor_tags", params=params)
    return json.dumps(result, indent=2)


async def get_page_post_to(page_post_id: str, fields: Optional[str] = None) -> str:
    """GET /to on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_id}/to", params=params)
    return json.dumps(result, indent=2)


async def delete_page_post(page_post_id: str) -> str:
    """DELETE /#delete on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
    """
    params = {}
    result = await get_client().delete(f"{page_post_id}")
    return json.dumps(result, indent=2)


async def get_page_post(
    page_post_id: str,
    fields: Optional[str] = None,
    primary_fb_page_id: Optional[str] = None,
    primary_ig_user_id: Optional[str] = None,
) -> str:
    """GET /#get on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        fields: Comma-separated list of fields to return. Available: actions, admin_creator, allowed_advertising_objectives, application, backdated_time, call_to_action, can_reply_privately, child_attachments, comments_mirroring_domain, coordinates, created_time, event, expanded_height, expanded_width, feed_targeting, from, full_picture, height, icon, id, instagram_eligibility, is_app_share, is_eligible_for_promotion, is_expired, is_hidden, is_inline_created, is_instagram_eligible, is_popular, is_published, is_spherical, message, message_tags, multi_share_end_card, multi_share_optimized, parent_id, permalink_url, picture, place, privacy, promotable_id, promotion_status, properties, scheduled_publish_time, shares, status_type, story, story_tags, subscribed, target, targeting, timeline_visibility, updated_time, via, video_buying_eligibility, width
        primary_fb_page_id: Optional.
        primary_ig_user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if primary_fb_page_id is not None:
        params["primary_fb_page_id"] = primary_fb_page_id
    if primary_ig_user_id is not None:
        params["primary_ig_user_id"] = primary_ig_user_id
    result = await get_client().get(f"{page_post_id}", params=params)
    return json.dumps(result, indent=2)


async def update_page_post(
    page_post_id: str,
    attached_media: Optional[str] = None,
    backdated_time: Optional[str] = None,
    backdated_time_granularity: Optional[str] = None,
    composer_session_id: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    explicitly_added_mentionee_ids: Optional[str] = None,
    feed_story_visibility: Optional[str] = None,
    is_explicit_location: Optional[bool] = None,
    is_hidden: Optional[bool] = None,
    is_pinned: Optional[bool] = None,
    is_published: Optional[bool] = None,
    message: Optional[str] = None,
    og_action_type_id: Optional[str] = None,
    og_hide_object_attachment: Optional[bool] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_set_profile_badge: Optional[bool] = None,
    og_suggestion_mechanism: Optional[str] = None,
    place: Optional[str] = None,
    privacy: Optional[str] = None,
    product_item: Optional[str] = None,
    scheduled_publish_time: Optional[int] = None,
    should_sync_product_edit: Optional[bool] = None,
    source_type: Optional[str] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    tags: Optional[str] = None,
    text_format_preset_id: Optional[str] = None,
    timeline_visibility: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /#update on PagePost.

    Args:
        page_post_id: The ID of the PagePost object.
        attached_media: Optional.
        backdated_time: Optional.
        backdated_time_granularity: Optional.
        composer_session_id: Optional.
        direct_share_status: Optional.
        explicitly_added_mentionee_ids: Optional.
        feed_story_visibility: Optional.
        is_explicit_location: Optional.
        is_hidden: Optional.
        is_pinned: Optional.
        is_published: Optional.
        message: Optional.
        og_action_type_id: Optional.
        og_hide_object_attachment: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_set_profile_badge: Optional.
        og_suggestion_mechanism: Optional.
        place: Optional.
        privacy: Optional.
        product_item: Optional.
        scheduled_publish_time: Optional.
        should_sync_product_edit: Optional.
        source_type: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        tags: Optional.
        text_format_preset_id: Optional.
        timeline_visibility: Optional.
        tracking: Optional.
    """
    params = {}
    if attached_media is not None:
        params["attached_media"] = attached_media
    if backdated_time is not None:
        params["backdated_time"] = backdated_time
    if backdated_time_granularity is not None:
        params["backdated_time_granularity"] = backdated_time_granularity
    if composer_session_id is not None:
        params["composer_session_id"] = composer_session_id
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if explicitly_added_mentionee_ids is not None:
        params["explicitly_added_mentionee_ids"] = explicitly_added_mentionee_ids
    if feed_story_visibility is not None:
        params["feed_story_visibility"] = feed_story_visibility
    if is_explicit_location is not None:
        params["is_explicit_location"] = is_explicit_location
    if is_hidden is not None:
        params["is_hidden"] = is_hidden
    if is_pinned is not None:
        params["is_pinned"] = is_pinned
    if is_published is not None:
        params["is_published"] = is_published
    if message is not None:
        params["message"] = message
    if og_action_type_id is not None:
        params["og_action_type_id"] = og_action_type_id
    if og_hide_object_attachment is not None:
        params["og_hide_object_attachment"] = og_hide_object_attachment
    if og_icon_id is not None:
        params["og_icon_id"] = og_icon_id
    if og_object_id is not None:
        params["og_object_id"] = og_object_id
    if og_phrase is not None:
        params["og_phrase"] = og_phrase
    if og_set_profile_badge is not None:
        params["og_set_profile_badge"] = og_set_profile_badge
    if og_suggestion_mechanism is not None:
        params["og_suggestion_mechanism"] = og_suggestion_mechanism
    if place is not None:
        params["place"] = place
    if privacy is not None:
        params["privacy"] = privacy
    if product_item is not None:
        params["product_item"] = product_item
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if should_sync_product_edit is not None:
        params["should_sync_product_edit"] = should_sync_product_edit
    if source_type is not None:
        params["source_type"] = source_type
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if tags is not None:
        params["tags"] = tags
    if text_format_preset_id is not None:
        params["text_format_preset_id"] = text_format_preset_id
    if timeline_visibility is not None:
        params["timeline_visibility"] = timeline_visibility
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().post(f"{page_post_id}", data=params)
    return json.dumps(result, indent=2)


PAGE_CALL_TO_ACTION_FIELDS = [
    "android_app",
    "android_deeplink",
    "android_destination_type",
    "android_package_name",
    "android_url",
    "created_time",
    "email_address",
    "from",
    "id",
    "intl_number_with_plus",
    "iphone_app",
    "iphone_deeplink",
    "iphone_destination_type",
    "iphone_url",
    "status",
    "type",
    "updated_time",
    "web_destination_type",
    "web_url"
]


async def delete_page_call_to_action(page_call_to_action_id: str) -> str:
    """DELETE /#delete on PageCallToAction.

    Args:
        page_call_to_action_id: The ID of the PageCallToAction object.
    """
    params = {}
    result = await get_client().delete(f"{page_call_to_action_id}")
    return json.dumps(result, indent=2)


async def get_page_call_to_action(page_call_to_action_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on PageCallToAction.

    Args:
        page_call_to_action_id: The ID of the PageCallToAction object.
        fields: Comma-separated list of fields to return. Available: android_app, android_deeplink, android_destination_type, android_package_name, android_url, created_time, email_address, from, id, intl_number_with_plus, iphone_app, iphone_deeplink, iphone_destination_type, iphone_url, status, type, updated_time, web_destination_type, web_url
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_call_to_action_id}", params=params)
    return json.dumps(result, indent=2)


async def update_page_call_to_action(
    page_call_to_action_id: str,
    android_app_id: Optional[int] = None,
    android_destination_type: Optional[str] = None,
    android_package_name: Optional[str] = None,
    android_url: Optional[str] = None,
    email_address: Optional[str] = None,
    intl_number_with_plus: Optional[str] = None,
    iphone_app_id: Optional[int] = None,
    iphone_destination_type: Optional[str] = None,
    iphone_url: Optional[str] = None,
    type_: Optional[str] = None,
    web_destination_type: Optional[str] = None,
    web_url: Optional[str] = None,
) -> str:
    """POST /#update on PageCallToAction.

    Args:
        page_call_to_action_id: The ID of the PageCallToAction object.
        android_app_id: Optional.
        android_destination_type: Optional.
        android_package_name: Optional.
        android_url: Optional.
        email_address: Optional.
        intl_number_with_plus: Optional.
        iphone_app_id: Optional.
        iphone_destination_type: Optional.
        iphone_url: Optional.
        type_: Optional.
        web_destination_type: Optional.
        web_url: Optional.
    """
    params = {}
    if android_app_id is not None:
        params["android_app_id"] = android_app_id
    if android_destination_type is not None:
        params["android_destination_type"] = android_destination_type
    if android_package_name is not None:
        params["android_package_name"] = android_package_name
    if android_url is not None:
        params["android_url"] = android_url
    if email_address is not None:
        params["email_address"] = email_address
    if intl_number_with_plus is not None:
        params["intl_number_with_plus"] = intl_number_with_plus
    if iphone_app_id is not None:
        params["iphone_app_id"] = iphone_app_id
    if iphone_destination_type is not None:
        params["iphone_destination_type"] = iphone_destination_type
    if iphone_url is not None:
        params["iphone_url"] = iphone_url
    if type_ is not None:
        params["type"] = type_
    if web_destination_type is not None:
        params["web_destination_type"] = web_destination_type
    if web_url is not None:
        params["web_url"] = web_url
    result = await get_client().post(f"{page_call_to_action_id}", data=params)
    return json.dumps(result, indent=2)


PAGE_POST_EXPERIMENT_FIELDS = [
    "auto_resolve_settings",
    "control_video_id",
    "creation_time",
    "creator",
    "declared_winning_time",
    "declared_winning_video_id",
    "description",
    "experiment_video_ids",
    "id",
    "insight_snapshots",
    "name",
    "optimization_goal",
    "publish_status",
    "publish_time",
    "scheduled_experiment_timestamp",
    "updated_time"
]


async def get_page_post_experiment_video_insights(page_post_experiment_id: str, fields: Optional[str] = None) -> str:
    """GET /video_insights on PagePostExperiment.

    Args:
        page_post_experiment_id: The ID of the PagePostExperiment object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_experiment_id}/video_insights", params=params)
    return json.dumps(result, indent=2)


async def delete_page_post_experiment(page_post_experiment_id: str) -> str:
    """DELETE /#delete on PagePostExperiment.

    Args:
        page_post_experiment_id: The ID of the PagePostExperiment object.
    """
    params = {}
    result = await get_client().delete(f"{page_post_experiment_id}")
    return json.dumps(result, indent=2)


async def get_page_post_experiment(page_post_experiment_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on PagePostExperiment.

    Args:
        page_post_experiment_id: The ID of the PagePostExperiment object.
        fields: Comma-separated list of fields to return. Available: auto_resolve_settings, control_video_id, creation_time, creator, declared_winning_time, declared_winning_video_id, description, experiment_video_ids, id, insight_snapshots, name, optimization_goal, publish_status, publish_time, scheduled_experiment_timestamp, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_post_experiment_id}", params=params)
    return json.dumps(result, indent=2)


PAGE_USER_MESSAGE_THREAD_LABEL_FIELDS = [
    "id",
    "page_label_name"
]


async def delete_page_user_message_thread_label_label(page_user_message_thread_label_id: str, user: int) -> str:
    """DELETE /label on PageUserMessageThreadLabel.

    Args:
        page_user_message_thread_label_id: The ID of the PageUserMessageThreadLabel object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{page_user_message_thread_label_id}/label")
    return json.dumps(result, indent=2)


async def create_page_user_message_thread_label_label(page_user_message_thread_label_id: str, user: int) -> str:
    """POST /label on PageUserMessageThreadLabel.

    Args:
        page_user_message_thread_label_id: The ID of the PageUserMessageThreadLabel object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().post(f"{page_user_message_thread_label_id}/label", data=params)
    return json.dumps(result, indent=2)


async def delete_page_user_message_thread_label(page_user_message_thread_label_id: str) -> str:
    """DELETE /#delete on PageUserMessageThreadLabel.

    Args:
        page_user_message_thread_label_id: The ID of the PageUserMessageThreadLabel object.
    """
    params = {}
    result = await get_client().delete(f"{page_user_message_thread_label_id}")
    return json.dumps(result, indent=2)


async def get_page_user_message_thread_label(page_user_message_thread_label_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on PageUserMessageThreadLabel.

    Args:
        page_user_message_thread_label_id: The ID of the PageUserMessageThreadLabel object.
        fields: Comma-separated list of fields to return. Available: id, page_label_name
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{page_user_message_thread_label_id}", params=params)
    return json.dumps(result, indent=2)

