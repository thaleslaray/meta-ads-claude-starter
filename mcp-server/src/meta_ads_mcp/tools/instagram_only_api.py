"""Auto-generated Meta Marketing API tools — instagram_only_api."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


IG_USER_FOR_IG_ONLY_API_FIELDS = [
    "account_type",
    "biography",
    "followers_count",
    "follows_count",
    "id",
    "media_count",
    "name",
    "profile_picture_url",
    "user_id",
    "username",
    "website"
]


async def get_ig_user_for_ig_only_api_business_messaging_feature_status(ig_user_for_ig_only_api_id: str, feature: str, fields: Optional[str] = None) -> str:
    """GET /business_messaging_feature_status on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
        feature: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["feature"] = feature
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/business_messaging_feature_status", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_content_publishing_limit(
    ig_user_for_ig_only_api_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /content_publishing_limit on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
        since: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if since is not None:
        params["since"] = since
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/content_publishing_limit", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_conversations(
    ig_user_for_ig_only_api_id: str,
    fields: Optional[str] = None,
    folder: Optional[str] = None,
    platform: Optional[str] = None,
    tags: Optional[str] = None,
    user_id: Optional[str] = None,
) -> str:
    """GET /conversations on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
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
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/conversations", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_insights(
    ig_user_for_ig_only_api_id: str,
    metric: str,
    period: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    metric_type: Optional[str] = None,
    since: Optional[str] = None,
    timeframe: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
        breakdown: Optional. Values: age, city, contact_button_type, country, follow_type, gender, media_product_type
        metric: Required. Values: accounts_engaged, comments, content_views, engaged_audience_demographics, follower_count, follower_demographics, follows_and_unfollows, likes, online_followers, profile_links_taps, profile_views, quotes, reach, reached_audience_demographics, replies, reposts, saves, shares, threads_clicks, threads_follower_demographics, threads_followers, threads_likes, threads_replies, threads_views, total_interactions, views, website_clicks
        metric_type: Optional. Values: default, time_series, total_value
        period: Required. Values: day, days_28, lifetime, month, total_over_range, week
        since: Optional.
        timeframe: Optional. Values: last_14_days, last_30_days, last_90_days, prev_month, this_month, this_week
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdown is not None:
        params["breakdown"] = breakdown
    params["metric"] = metric
    if metric_type is not None:
        params["metric_type"] = metric_type
    params["period"] = period
    if since is not None:
        params["since"] = since
    if timeframe is not None:
        params["timeframe"] = timeframe
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_live_media(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /live_media on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/live_media", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_media(
    ig_user_for_ig_only_api_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /media on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
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
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/media", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_media(
    ig_user_for_ig_only_api_id: str,
    alt_text: Optional[str] = None,
    audio_name: Optional[str] = None,
    caption: Optional[str] = None,
    children: Optional[str] = None,
    collaborators: Optional[str] = None,
    cover_url: Optional[str] = None,
    image_url: Optional[str] = None,
    is_carousel_item: Optional[bool] = None,
    location_id: Optional[str] = None,
    media_type: Optional[str] = None,
    product_tags: Optional[str] = None,
    share_to_feed: Optional[bool] = None,
    thumb_offset: Optional[str] = None,
    trial_params: Optional[str] = None,
    upload_type: Optional[str] = None,
    user_tags: Optional[str] = None,
    video_url: Optional[str] = None,
) -> str:
    """POST /media on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        alt_text: Optional.
        audio_name: Optional.
        caption: Optional.
        children: Optional.
        collaborators: Optional.
        cover_url: Optional.
        image_url: Optional.
        is_carousel_item: Optional.
        location_id: Optional.
        media_type: Optional.
        product_tags: Optional.
        share_to_feed: Optional.
        thumb_offset: Optional.
        trial_params: Optional.
        upload_type: Optional.
        user_tags: Optional.
        video_url: Optional.
    """
    params = {}
    if alt_text is not None:
        params["alt_text"] = alt_text
    if audio_name is not None:
        params["audio_name"] = audio_name
    if caption is not None:
        params["caption"] = caption
    if children is not None:
        params["children"] = children
    if collaborators is not None:
        params["collaborators"] = collaborators
    if cover_url is not None:
        params["cover_url"] = cover_url
    if image_url is not None:
        params["image_url"] = image_url
    if is_carousel_item is not None:
        params["is_carousel_item"] = is_carousel_item
    if location_id is not None:
        params["location_id"] = location_id
    if media_type is not None:
        params["media_type"] = media_type
    if product_tags is not None:
        params["product_tags"] = product_tags
    if share_to_feed is not None:
        params["share_to_feed"] = share_to_feed
    if thumb_offset is not None:
        params["thumb_offset"] = thumb_offset
    if trial_params is not None:
        params["trial_params"] = trial_params
    if upload_type is not None:
        params["upload_type"] = upload_type
    if user_tags is not None:
        params["user_tags"] = user_tags
    if video_url is not None:
        params["video_url"] = video_url
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/media", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_mediapublish(ig_user_for_ig_only_api_id: str, creation_id: int) -> str:
    """POST /mediapublish on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        creation_id: Required.
    """
    params = {}
    params["creation_id"] = creation_id
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/mediapublish", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_mentions(
    ig_user_for_ig_only_api_id: str,
    media_id: str,
    message: str,
    comment_id: Optional[str] = None,
) -> str:
    """POST /mentions on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        comment_id: Optional.
        media_id: Required.
        message: Required.
    """
    params = {}
    if comment_id is not None:
        params["comment_id"] = comment_id
    params["media_id"] = media_id
    params["message"] = message
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/mentions", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_messageattachments(ig_user_for_ig_only_api_id: str, message: str) -> str:
    """POST /messageattachments on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        message: Required.
    """
    params = {}
    params["message"] = message
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/messageattachments", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_messages(
    ig_user_for_ig_only_api_id: str,
    message: Optional[str] = None,
    messaging_type: Optional[str] = None,
    payload: Optional[str] = None,
    recipient: Optional[str] = None,
    sender_action: Optional[str] = None,
    tag: Optional[str] = None,
    thread_control: Optional[str] = None,
) -> str:
    """POST /messages on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        message: Optional.
        messaging_type: Optional. Values: MESSAGE_TAG, RESPONSE, UPDATE, UTILITY
        payload: Optional.
        recipient: Optional.
        sender_action: Optional. Values: MARK_SEEN, REACT, TYPING_OFF, TYPING_ON, UNREACT
        tag: Optional.
        thread_control: Optional.
    """
    params = {}
    if message is not None:
        params["message"] = message
    if messaging_type is not None:
        params["messaging_type"] = messaging_type
    if payload is not None:
        params["payload"] = payload
    if recipient is not None:
        params["recipient"] = recipient
    if sender_action is not None:
        params["sender_action"] = sender_action
    if tag is not None:
        params["tag"] = tag
    if thread_control is not None:
        params["thread_control"] = thread_control
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/messages", data=params)
    return json.dumps(result, indent=2)


async def delete_ig_user_for_ig_only_api_messenger_profile(ig_user_for_ig_only_api_id: str, fields: str) -> str:
    """DELETE /messenger_profile on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Required. Values: ACCOUNT_LINKING_URL, COMMANDS, DESCRIPTION, GET_STARTED, GREETING, HOME_URL, ICE_BREAKERS, PERSISTENT_MENU, PLATFORM, SUBJECT_TO_NEW_EU_PRIVACY_RULES, TITLE, WHITELISTED_DOMAINS
    """
    params = {}
    params["fields"] = fields
    result = await get_client().delete(f"{ig_user_for_ig_only_api_id}/messenger_profile")
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_messenger_profile(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /messenger_profile on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/messenger_profile", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_messenger_profile(
    ig_user_for_ig_only_api_id: str,
    ice_breakers: Optional[str] = None,
    persistent_menu: Optional[str] = None,
) -> str:
    """POST /messenger_profile on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        ice_breakers: Optional.
        persistent_menu: Optional.
    """
    params = {}
    if ice_breakers is not None:
        params["ice_breakers"] = ice_breakers
    if persistent_menu is not None:
        params["persistent_menu"] = persistent_menu
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/messenger_profile", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_stories(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /stories on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/stories", params=params)
    return json.dumps(result, indent=2)


async def delete_ig_user_for_ig_only_api_subscribed_apps(ig_user_for_ig_only_api_id: str) -> str:
    """DELETE /subscribed_apps on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
    """
    params = {}
    result = await get_client().delete(f"{ig_user_for_ig_only_api_id}/subscribed_apps")
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_subscribed_apps(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_apps on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/subscribed_apps", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_subscribed_apps(ig_user_for_ig_only_api_id: str, subscribed_fields: str) -> str:
    """POST /subscribed_apps on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        subscribed_fields: Required. Values: comment_poll_response, comments, creator_marketplace_invited_creator_onboarding, creator_marketplace_projects, delta, follow, live_comments, mentions, message_edit, message_reactions, messages, messaging_handover, messaging_optins, messaging_postbacks, messaging_referral, messaging_seen, onboarding_welcome_message_series, share_to_story, standby, story_insights, story_poll_response, story_reactions
    """
    params = {}
    params["subscribed_fields"] = subscribed_fields
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/subscribed_apps", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_tags(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /tags on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/tags", params=params)
    return json.dumps(result, indent=2)


async def delete_ig_user_for_ig_only_api_welcome_message_flows(ig_user_for_ig_only_api_id: str, flow_id: Optional[str] = None) -> str:
    """DELETE /welcome_message_flows on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        flow_id: Optional.
    """
    params = {}
    if flow_id is not None:
        params["flow_id"] = flow_id
    result = await get_client().delete(f"{ig_user_for_ig_only_api_id}/welcome_message_flows")
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api_welcome_message_flows(
    ig_user_for_ig_only_api_id: str,
    fields: Optional[str] = None,
    app_id: Optional[str] = None,
    flow_id: Optional[str] = None,
) -> str:
    """GET /welcome_message_flows on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
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
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}/welcome_message_flows", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_for_ig_only_api_welcome_message_flows(
    ig_user_for_ig_only_api_id: str,
    eligible_platforms: Optional[str] = None,
    flow_id: Optional[str] = None,
    name: Optional[str] = None,
    welcome_message_flow: Optional[str] = None,
) -> str:
    """POST /welcome_message_flows on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
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
    result = await get_client().post(f"{ig_user_for_ig_only_api_id}/welcome_message_flows", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_for_ig_only_api(ig_user_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on IGUserForIGOnlyAPI.

    Args:
        ig_user_for_ig_only_api_id: The ID of the IGUserForIGOnlyAPI object.
        fields: Comma-separated list of fields to return. Available: account_type, biography, followers_count, follows_count, id, media_count, name, profile_picture_url, user_id, username, website
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_for_ig_only_api_id}", params=params)
    return json.dumps(result, indent=2)


IG_MEDIA_FOR_IG_ONLY_API_FIELDS = [
    "alt_text",
    "caption",
    "comments_count",
    "id",
    "is_comment_enabled",
    "is_shared_to_feed",
    "like_count",
    "media_product_type",
    "media_type",
    "media_url",
    "owner",
    "permalink",
    "shortcode",
    "thumbnail_url",
    "timestamp",
    "username"
]


async def get_ig_media_for_ig_only_api_children(ig_media_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /children on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_for_ig_only_api_id}/children", params=params)
    return json.dumps(result, indent=2)


async def get_ig_media_for_ig_only_api_comments(ig_media_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /comments on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_for_ig_only_api_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_ig_media_for_ig_only_api_comments(ig_media_for_ig_only_api_id: str, message: Optional[str] = None) -> str:
    """POST /comments on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        message: Optional.
    """
    params = {}
    if message is not None:
        params["message"] = message
    result = await get_client().post(f"{ig_media_for_ig_only_api_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_ig_media_for_ig_only_api_insights(
    ig_media_for_ig_only_api_id: str,
    metric: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    period: Optional[str] = None,
) -> str:
    """GET /insights on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        fields: Comma-separated list of fields to return.
        breakdown: Optional. Values: action_type, follow_type, story_navigation_action_type, surface_type
        metric: Required. Values: clips_replays_count, comments, content_views, follows, ig_reels_aggregated_all_plays_count, ig_reels_avg_watch_time, ig_reels_video_view_total_time, impressions, likes, navigation, plays, profile_activity, profile_visits, quotes, reach, replies, reposts, saved, shares, thread_replies, thread_shares, threads_media_clicks, threads_views, total_interactions, views
        period: Optional. Values: day, days_28, lifetime, month, total_over_range, week
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdown is not None:
        params["breakdown"] = breakdown
    params["metric"] = metric
    if period is not None:
        params["period"] = period
    result = await get_client().get(f"{ig_media_for_ig_only_api_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_ig_media_for_ig_only_api(ig_media_for_ig_only_api_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        fields: Comma-separated list of fields to return. Available: alt_text, caption, comments_count, id, is_comment_enabled, is_shared_to_feed, like_count, media_product_type, media_type, media_url, owner, permalink, shortcode, thumbnail_url, timestamp, username
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_for_ig_only_api_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ig_media_for_ig_only_api(ig_media_for_ig_only_api_id: str, comment_enabled: bool) -> str:
    """POST /#update on IGMediaForIGOnlyAPI.

    Args:
        ig_media_for_ig_only_api_id: The ID of the IGMediaForIGOnlyAPI object.
        comment_enabled: Required.
    """
    params = {}
    params["comment_enabled"] = comment_enabled
    result = await get_client().post(f"{ig_media_for_ig_only_api_id}", data=params)
    return json.dumps(result, indent=2)

