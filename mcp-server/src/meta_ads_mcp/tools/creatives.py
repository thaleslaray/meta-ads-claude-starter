"""Auto-generated Meta Marketing API tools — creatives."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_CREATIVE_FIELDS = [
    "account_id",
    "actor_id",
    "ad_disclaimer_spec",
    "adlabels",
    "applink_treatment",
    "asset_feed_spec",
    "authorization_category",
    "auto_update",
    "body",
    "branded_content",
    "branded_content_sponsor_page_id",
    "bundle_folder_id",
    "call_to_action",
    "call_to_action_type",
    "categorization_criteria",
    "category_media_source",
    "collaborative_ads_lsb_image_bank_id",
    "contextual_multi_ads",
    "creative_sourcing_spec",
    "degrees_of_freedom_spec",
    "destination_set_id",
    "destination_spec",
    "dynamic_ad_voice",
    "effective_authorization_category",
    "effective_instagram_media_id",
    "effective_object_story_id",
    "enable_direct_install",
    "enable_launch_instant_app",
    "facebook_branded_content",
    "format_transformation_spec",
    "id",
    "image_crops",
    "image_hash",
    "image_url",
    "instagram_branded_content",
    "instagram_permalink_url",
    "instagram_user_id",
    "interactive_components_spec",
    "link_deep_link_url",
    "link_destination_display_url",
    "link_og_id",
    "link_url",
    "media_sourcing_spec",
    "messenger_sponsored_message",
    "name",
    "object_id",
    "object_store_url",
    "object_story_id",
    "object_story_spec",
    "object_type",
    "object_url",
    "omnichannel_link_spec",
    "page_welcome_message",
    "photo_album_source_object_story_id",
    "place_page_set_id",
    "platform_customizations",
    "playable_asset_id",
    "portrait_customizations",
    "product_data",
    "product_set_id",
    "recommender_settings",
    "regional_regulation_disclaimer_spec",
    "source_facebook_post_id",
    "source_instagram_media_id",
    "status",
    "template_url",
    "template_url_spec",
    "thumbnail_id",
    "thumbnail_url",
    "title",
    "url_tags",
    "use_page_actor_override",
    "video_id"
]


async def get_ad_creative_creative_insights(ad_creative_id: str, fields: Optional[str] = None) -> str:
    """GET /creative_insights on AdCreative.

    Args:
        ad_creative_id: The ID of the AdCreative object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_creative_id}/creative_insights", params=params)
    return json.dumps(result, indent=2)


async def get_ad_creative_previews(
    ad_creative_id: str,
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
    """GET /previews on AdCreative.

    Args:
        ad_creative_id: The ID of the AdCreative object.
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
    result = await get_client().get(f"{ad_creative_id}/previews", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_creative(
    ad_creative_id: str,
    account_id: Optional[str] = None,
    adlabels: Optional[str] = None,
    name: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """DELETE /#delete on AdCreative.

    Args:
        ad_creative_id: The ID of the AdCreative object.
        account_id: Optional.
        adlabels: Optional.
        name: Optional.
        status: Optional.
    """
    params = {}
    if account_id is not None:
        params["account_id"] = account_id
    if adlabels is not None:
        params["adlabels"] = adlabels
    if name is not None:
        params["name"] = name
    if status is not None:
        params["status"] = status
    result = await get_client().delete(f"{ad_creative_id}")
    return json.dumps(result, indent=2)


async def get_ad_creative(
    ad_creative_id: str,
    fields: Optional[str] = None,
    thumbnail_height: Optional[int] = None,
    thumbnail_width: Optional[int] = None,
) -> str:
    """GET /#get on AdCreative.

    Args:
        ad_creative_id: The ID of the AdCreative object.
        fields: Comma-separated list of fields to return. Available: account_id, actor_id, ad_disclaimer_spec, adlabels, applink_treatment, asset_feed_spec, authorization_category, auto_update, body, branded_content, branded_content_sponsor_page_id, bundle_folder_id, call_to_action, call_to_action_type, categorization_criteria, category_media_source, collaborative_ads_lsb_image_bank_id, contextual_multi_ads, creative_sourcing_spec, degrees_of_freedom_spec, destination_set_id, destination_spec, dynamic_ad_voice, effective_authorization_category, effective_instagram_media_id, effective_object_story_id, enable_direct_install, enable_launch_instant_app, facebook_branded_content, format_transformation_spec, id, image_crops, image_hash, image_url, instagram_branded_content, instagram_permalink_url, instagram_user_id, interactive_components_spec, link_deep_link_url, link_destination_display_url, link_og_id, link_url, media_sourcing_spec, messenger_sponsored_message, name, object_id, object_store_url, object_story_id, object_story_spec, object_type, object_url, omnichannel_link_spec, page_welcome_message, photo_album_source_object_story_id, place_page_set_id, platform_customizations, playable_asset_id, portrait_customizations, product_data, product_set_id, recommender_settings, regional_regulation_disclaimer_spec, source_facebook_post_id, source_instagram_media_id, status, template_url, template_url_spec, thumbnail_id, thumbnail_url, title, url_tags, use_page_actor_override, video_id
        thumbnail_height: Optional.
        thumbnail_width: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if thumbnail_height is not None:
        params["thumbnail_height"] = thumbnail_height
    if thumbnail_width is not None:
        params["thumbnail_width"] = thumbnail_width
    result = await get_client().get(f"{ad_creative_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_creative(
    ad_creative_id: str,
    account_id: Optional[str] = None,
    adlabels: Optional[str] = None,
    name: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """POST /#update on AdCreative.

    Args:
        ad_creative_id: The ID of the AdCreative object.
        account_id: Optional.
        adlabels: Optional.
        name: Optional.
        status: Optional.
    """
    params = {}
    if account_id is not None:
        params["account_id"] = account_id
    if adlabels is not None:
        params["adlabels"] = adlabels
    if name is not None:
        params["name"] = name
    if status is not None:
        params["status"] = status
    result = await get_client().post(f"{ad_creative_id}", data=params)
    return json.dumps(result, indent=2)


AD_VIDEO_FIELDS = [
    "ad_breaks",
    "admin_creator",
    "audio_isrc",
    "backdated_time",
    "backdated_time_granularity",
    "boost_eligibility_info",
    "content_category",
    "content_tags",
    "copyright",
    "copyright_check_information",
    "copyright_monitoring_status",
    "created_time",
    "custom_labels",
    "description",
    "embed_html",
    "embeddable",
    "event",
    "expiration",
    "format",
    "from",
    "icon",
    "id",
    "is_crosspost_video",
    "is_crossposting_eligible",
    "is_episode",
    "is_instagram_eligible",
    "is_reference_only",
    "length",
    "live_audience_count",
    "live_status",
    "music_video_copyright",
    "permalink_url",
    "picture",
    "place",
    "post_id",
    "post_views",
    "premiere_living_room_status",
    "privacy",
    "published",
    "scheduled_publish_time",
    "season",
    "source",
    "spherical",
    "status",
    "title",
    "universal_video_id",
    "updated_time",
    "views"
]


async def get_ad_video_boost_ads_list(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /boost_ads_list on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/boost_ads_list", params=params)
    return json.dumps(result, indent=2)


async def get_ad_video_captions(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /captions on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/captions", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_captions(
    ad_video_id: str,
    captions_file: Optional[str] = None,
    default_locale: Optional[str] = None,
    locales_to_delete: Optional[str] = None,
) -> str:
    """POST /captions on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        captions_file: Optional.
        default_locale: Optional.
        locales_to_delete: Optional.
    """
    params = {}
    if captions_file is not None:
        params["captions_file"] = captions_file
    if default_locale is not None:
        params["default_locale"] = default_locale
    if locales_to_delete is not None:
        params["locales_to_delete"] = locales_to_delete
    result = await get_client().post(f"{ad_video_id}/captions", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_collaborators(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /collaborators on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/collaborators", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_collaborators(ad_video_id: str, target_id: str) -> str:
    """POST /collaborators on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        target_id: Required.
    """
    params = {}
    params["target_id"] = target_id
    result = await get_client().post(f"{ad_video_id}/collaborators", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_comments(
    ad_video_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
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
    result = await get_client().get(f"{ad_video_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_comments(
    ad_video_id: str,
    attachment_id: Optional[str] = None,
    attachment_share_url: Optional[str] = None,
    attachment_url: Optional[str] = None,
    comment_privacy_value: Optional[str] = None,
    facepile_mentioned_ids: Optional[str] = None,
    feedback_source: Optional[str] = None,
    is_offline: Optional[bool] = None,
    message: Optional[str] = None,
    nectar_module: Optional[str] = None,
    object_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    text: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /comments on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        attachment_id: Optional.
        attachment_share_url: Optional.
        attachment_url: Optional.
        comment_privacy_value: Optional. Values: DECLINED_BY_ADMIN_ASSISTANT, DEFAULT_PRIVACY, FRIENDS_AND_POST_OWNER, FRIENDS_ONLY, GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE, OWNER_OR_COMMENTER, PENDING_APPROVAL, REMOVED_BY_ADMIN_ASSISTANT, SIDE_CONVERSATION, SIDE_CONVERSATION_AND_POST_OWNER, SPOTLIGHT_TAB
        facepile_mentioned_ids: Optional.
        feedback_source: Optional.
        is_offline: Optional.
        message: Optional.
        nectar_module: Optional.
        object_id: Optional.
        parent_comment_id: Optional.
        text: Optional.
        tracking: Optional.
    """
    params = {}
    if attachment_id is not None:
        params["attachment_id"] = attachment_id
    if attachment_share_url is not None:
        params["attachment_share_url"] = attachment_share_url
    if attachment_url is not None:
        params["attachment_url"] = attachment_url
    if comment_privacy_value is not None:
        params["comment_privacy_value"] = comment_privacy_value
    if facepile_mentioned_ids is not None:
        params["facepile_mentioned_ids"] = facepile_mentioned_ids
    if feedback_source is not None:
        params["feedback_source"] = feedback_source
    if is_offline is not None:
        params["is_offline"] = is_offline
    if message is not None:
        params["message"] = message
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if object_id is not None:
        params["object_id"] = object_id
    if parent_comment_id is not None:
        params["parent_comment_id"] = parent_comment_id
    if text is not None:
        params["text"] = text
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().post(f"{ad_video_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_crosspost_shared_pages(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /crosspost_shared_pages on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/crosspost_shared_pages", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_gaming_clip_create(ad_video_id: str, duration_seconds: Optional[float] = None) -> str:
    """POST /gaming_clip_create on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        duration_seconds: Optional.
    """
    params = {}
    if duration_seconds is not None:
        params["duration_seconds"] = duration_seconds
    result = await get_client().post(f"{ad_video_id}/gaming_clip_create", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_likes(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_likes(
    ad_video_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    notify: Optional[bool] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        feedback_source: Optional.
        nectar_module: Optional.
        notify: Optional.
        tracking: Optional.
    """
    params = {}
    if feedback_source is not None:
        params["feedback_source"] = feedback_source
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if notify is not None:
        params["notify"] = notify
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().post(f"{ad_video_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_poll_settings(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /poll_settings on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/poll_settings", params=params)
    return json.dumps(result, indent=2)


async def get_ad_video_polls(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /polls on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/polls", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_polls(
    ad_video_id: str,
    options: str,
    question: str,
    close_after_voting: Optional[bool] = None,
    correct_option: Optional[int] = None,
    default_open: Optional[bool] = None,
    show_gradient: Optional[bool] = None,
    show_results: Optional[bool] = None,
) -> str:
    """POST /polls on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        close_after_voting: Optional.
        correct_option: Optional.
        default_open: Optional.
        options: Required.
        question: Required.
        show_gradient: Optional.
        show_results: Optional.
    """
    params = {}
    if close_after_voting is not None:
        params["close_after_voting"] = close_after_voting
    if correct_option is not None:
        params["correct_option"] = correct_option
    if default_open is not None:
        params["default_open"] = default_open
    params["options"] = options
    params["question"] = question
    if show_gradient is not None:
        params["show_gradient"] = show_gradient
    if show_results is not None:
        params["show_results"] = show_results
    result = await get_client().post(f"{ad_video_id}/polls", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_sponsor_tags(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /sponsor_tags on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/sponsor_tags", params=params)
    return json.dumps(result, indent=2)


async def get_ad_video_tags(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /tags on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/tags", params=params)
    return json.dumps(result, indent=2)


async def get_ad_video_thumbnails(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /thumbnails on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}/thumbnails", params=params)
    return json.dumps(result, indent=2)


async def create_ad_video_thumbnails(ad_video_id: str, source: str, is_preferred: Optional[bool] = None) -> str:
    """POST /thumbnails on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        is_preferred: Optional.
        source: Required.
    """
    params = {}
    if is_preferred is not None:
        params["is_preferred"] = is_preferred
    params["source"] = source
    result = await get_client().post(f"{ad_video_id}/thumbnails", data=params)
    return json.dumps(result, indent=2)


async def get_ad_video_video_insights(
    ad_video_id: str,
    fields: Optional[str] = None,
    metric: Optional[str] = None,
    period: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /video_insights on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return.
        metric: Optional.
        period: Optional. Values: day, days_28, lifetime, month, total_over_range, week
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if metric is not None:
        params["metric"] = metric
    if period is not None:
        params["period"] = period
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{ad_video_id}/video_insights", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_video(ad_video_id: str) -> str:
    """DELETE /#delete on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
    """
    params = {}
    result = await get_client().delete(f"{ad_video_id}")
    return json.dumps(result, indent=2)


async def get_ad_video(ad_video_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        fields: Comma-separated list of fields to return. Available: ad_breaks, admin_creator, audio_isrc, backdated_time, backdated_time_granularity, boost_eligibility_info, content_category, content_tags, copyright, copyright_check_information, copyright_monitoring_status, created_time, custom_labels, description, embed_html, embeddable, event, expiration, format, from, icon, id, is_crosspost_video, is_crossposting_eligible, is_episode, is_instagram_eligible, is_reference_only, length, live_audience_count, live_status, music_video_copyright, permalink_url, picture, place, post_id, post_views, premiere_living_room_status, privacy, published, scheduled_publish_time, season, source, spherical, status, title, universal_video_id, updated_time, views
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_video_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_video(
    ad_video_id: str,
    ad_breaks: Optional[str] = None,
    allow_bm_crossposting: Optional[bool] = None,
    allow_crossposting_for_pages: Optional[str] = None,
    backdated_time: Optional[str] = None,
    backdated_time_granularity: Optional[str] = None,
    call_to_action: Optional[str] = None,
    content_category: Optional[str] = None,
    content_tags: Optional[str] = None,
    custom_labels: Optional[str] = None,
    description: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    embeddable: Optional[bool] = None,
    expiration: Optional[str] = None,
    expire_now: Optional[bool] = None,
    increment_play_count: Optional[bool] = None,
    name: Optional[str] = None,
    preferred_thumbnail_id: Optional[str] = None,
    privacy: Optional[str] = None,
    publish_to_news_feed: Optional[bool] = None,
    publish_to_videos_tab: Optional[bool] = None,
    published: Optional[bool] = None,
    scheduled_publish_time: Optional[int] = None,
    social_actions: Optional[bool] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    tags: Optional[str] = None,
    target: Optional[str] = None,
    universal_video_id: Optional[str] = None,
) -> str:
    """POST /#update on AdVideo.

    Args:
        ad_video_id: The ID of the AdVideo object.
        ad_breaks: Optional.
        allow_bm_crossposting: Optional.
        allow_crossposting_for_pages: Optional.
        backdated_time: Optional.
        backdated_time_granularity: Optional.
        call_to_action: Optional.
        content_category: Optional.
        content_tags: Optional.
        custom_labels: Optional.
        description: Optional.
        direct_share_status: Optional.
        embeddable: Optional.
        expiration: Optional.
        expire_now: Optional.
        increment_play_count: Optional.
        name: Optional.
        preferred_thumbnail_id: Optional.
        privacy: Optional.
        publish_to_news_feed: Optional.
        publish_to_videos_tab: Optional.
        published: Optional.
        scheduled_publish_time: Optional.
        social_actions: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        tags: Optional.
        target: Optional.
        universal_video_id: Optional.
    """
    params = {}
    if ad_breaks is not None:
        params["ad_breaks"] = ad_breaks
    if allow_bm_crossposting is not None:
        params["allow_bm_crossposting"] = allow_bm_crossposting
    if allow_crossposting_for_pages is not None:
        params["allow_crossposting_for_pages"] = allow_crossposting_for_pages
    if backdated_time is not None:
        params["backdated_time"] = backdated_time
    if backdated_time_granularity is not None:
        params["backdated_time_granularity"] = backdated_time_granularity
    if call_to_action is not None:
        params["call_to_action"] = call_to_action
    if content_category is not None:
        params["content_category"] = content_category
    if content_tags is not None:
        params["content_tags"] = content_tags
    if custom_labels is not None:
        params["custom_labels"] = custom_labels
    if description is not None:
        params["description"] = description
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if embeddable is not None:
        params["embeddable"] = embeddable
    if expiration is not None:
        params["expiration"] = expiration
    if expire_now is not None:
        params["expire_now"] = expire_now
    if increment_play_count is not None:
        params["increment_play_count"] = increment_play_count
    if name is not None:
        params["name"] = name
    if preferred_thumbnail_id is not None:
        params["preferred_thumbnail_id"] = preferred_thumbnail_id
    if privacy is not None:
        params["privacy"] = privacy
    if publish_to_news_feed is not None:
        params["publish_to_news_feed"] = publish_to_news_feed
    if publish_to_videos_tab is not None:
        params["publish_to_videos_tab"] = publish_to_videos_tab
    if published is not None:
        params["published"] = published
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
    if social_actions is not None:
        params["social_actions"] = social_actions
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if tags is not None:
        params["tags"] = tags
    if target is not None:
        params["target"] = target
    if universal_video_id is not None:
        params["universal_video_id"] = universal_video_id
    result = await get_client().post(f"{ad_video_id}", data=params)
    return json.dumps(result, indent=2)


CANVAS_FIELDS = [
    "background_color",
    "body_elements",
    "business_id",
    "canvas_link",
    "collection_hero_image",
    "collection_hero_video",
    "collection_thumbnails",
    "dynamic_setting",
    "element_payload",
    "elements",
    "fb_body_elements",
    "hero_asset_facebook_post_id",
    "hero_asset_instagram_media_id",
    "id",
    "is_hidden",
    "is_published",
    "last_editor",
    "linked_documents",
    "name",
    "owner",
    "property_list",
    "source_template",
    "store_url",
    "style_list",
    "tags",
    "ui_property_list",
    "unused_body_elements",
    "update_time",
    "use_retailer_item_ids"
]


async def get_canvas_preview(canvas_id: str, fields: Optional[str] = None) -> str:
    """GET /preview on Canvas.

    Args:
        canvas_id: The ID of the Canvas object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{canvas_id}/preview", params=params)
    return json.dumps(result, indent=2)


async def get_canvas_previews(canvas_id: str, fields: Optional[str] = None, user_ids: Optional[str] = None) -> str:
    """GET /previews on Canvas.

    Args:
        canvas_id: The ID of the Canvas object.
        fields: Comma-separated list of fields to return.
        user_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if user_ids is not None:
        params["user_ids"] = user_ids
    result = await get_client().get(f"{canvas_id}/previews", params=params)
    return json.dumps(result, indent=2)


async def get_canvas(canvas_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Canvas.

    Args:
        canvas_id: The ID of the Canvas object.
        fields: Comma-separated list of fields to return. Available: background_color, body_elements, business_id, canvas_link, collection_hero_image, collection_hero_video, collection_thumbnails, dynamic_setting, element_payload, elements, fb_body_elements, hero_asset_facebook_post_id, hero_asset_instagram_media_id, id, is_hidden, is_published, last_editor, linked_documents, name, owner, property_list, source_template, store_url, style_list, tags, ui_property_list, unused_body_elements, update_time, use_retailer_item_ids
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{canvas_id}", params=params)
    return json.dumps(result, indent=2)


async def update_canvas(
    canvas_id: str,
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
    """POST /#update on Canvas.

    Args:
        canvas_id: The ID of the Canvas object.
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
    result = await get_client().post(f"{canvas_id}", data=params)
    return json.dumps(result, indent=2)

