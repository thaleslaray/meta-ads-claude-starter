"""Auto-generated Meta Marketing API tools — content."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


POST_FIELDS = [
    "actions",
    "admin_creator",
    "allowed_advertising_objectives",
    "application",
    "backdated_time",
    "call_to_action",
    "can_reply_privately",
    "caption",
    "child_attachments",
    "comments_mirroring_domain",
    "coordinates",
    "created_time",
    "description",
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
    "link",
    "message",
    "message_tags",
    "multi_share_end_card",
    "multi_share_optimized",
    "name",
    "object_id",
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
    "source",
    "status_type",
    "story",
    "story_tags",
    "subscribed",
    "target",
    "targeting",
    "timeline_visibility",
    "type",
    "updated_time",
    "via",
    "video_buying_eligibility",
    "width"
]


async def get_post_attachments(post_id: str, fields: Optional[str] = None) -> str:
    """GET /attachments on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{post_id}/attachments", params=params)
    return json.dumps(result, indent=2)


async def get_post_comments(
    post_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on Post.

    Args:
        post_id: The ID of the Post object.
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
    result = await get_client().get(f"{post_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_post_comments(
    post_id: str,
    attachment_id: Optional[str] = None,
    attachment_share_url: Optional[str] = None,
    attachment_url: Optional[str] = None,
    comment: Optional[str] = None,
    comment_privacy_value: Optional[str] = None,
    feedback_source: Optional[str] = None,
    message: Optional[str] = None,
    nectar_module: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /comments on Post.

    Args:
        post_id: The ID of the Post object.
        attachment_id: Optional.
        attachment_share_url: Optional.
        attachment_url: Optional.
        comment: Optional.
        comment_privacy_value: Optional. Values: DECLINED_BY_ADMIN_ASSISTANT, DEFAULT_PRIVACY, FRIENDS_AND_POST_OWNER, FRIENDS_ONLY, GRAPHQL_MULTIPLE_VALUE_HACK_DO_NOT_USE, OWNER_OR_COMMENTER, PENDING_APPROVAL, REMOVED_BY_ADMIN_ASSISTANT, SIDE_CONVERSATION, SIDE_CONVERSATION_AND_POST_OWNER, SPOTLIGHT_TAB
        feedback_source: Optional.
        message: Optional.
        nectar_module: Optional.
        parent_comment_id: Optional.
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
    result = await get_client().post(f"{post_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_post_dynamic_posts(post_id: str, fields: Optional[str] = None) -> str:
    """GET /dynamic_posts on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{post_id}/dynamic_posts", params=params)
    return json.dumps(result, indent=2)


async def get_post_insights(
    post_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    metric: Optional[str] = None,
    period: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on Post.

    Args:
        post_id: The ID of the Post object.
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
    result = await get_client().get(f"{post_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def delete_post_likes(
    post_id: str,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """DELETE /likes on Post.

    Args:
        post_id: The ID of the Post object.
        nectar_module: Optional.
        tracking: Optional.
    """
    params = {}
    if nectar_module is not None:
        params["nectar_module"] = nectar_module
    if tracking is not None:
        params["tracking"] = tracking
    result = await get_client().delete(f"{post_id}/likes")
    return json.dumps(result, indent=2)


async def create_post_likes(
    post_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on Post.

    Args:
        post_id: The ID of the Post object.
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
    result = await get_client().post(f"{post_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_post_reactions(post_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /reactions on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: ANGRY, CARE, FIRE, HAHA, HUNDRED, LIKE, LOVE, NONE, PRIDE, SAD, THANKFUL, WOW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{post_id}/reactions", params=params)
    return json.dumps(result, indent=2)


async def get_post_sharedposts(post_id: str, fields: Optional[str] = None) -> str:
    """GET /sharedposts on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{post_id}/sharedposts", params=params)
    return json.dumps(result, indent=2)


async def get_post_sponsor_tags(post_id: str, fields: Optional[str] = None) -> str:
    """GET /sponsor_tags on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{post_id}/sponsor_tags", params=params)
    return json.dumps(result, indent=2)


async def get_post_to(post_id: str, fields: Optional[str] = None) -> str:
    """GET /to on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{post_id}/to", params=params)
    return json.dumps(result, indent=2)


async def delete_post(post_id: str) -> str:
    """DELETE /#delete on Post.

    Args:
        post_id: The ID of the Post object.
    """
    params = {}
    result = await get_client().delete(f"{post_id}")
    return json.dumps(result, indent=2)


async def get_post(
    post_id: str,
    fields: Optional[str] = None,
    primary_fb_page_id: Optional[str] = None,
    primary_ig_user_id: Optional[str] = None,
) -> str:
    """GET /#get on Post.

    Args:
        post_id: The ID of the Post object.
        fields: Comma-separated list of fields to return. Available: actions, admin_creator, allowed_advertising_objectives, application, backdated_time, call_to_action, can_reply_privately, caption, child_attachments, comments_mirroring_domain, coordinates, created_time, description, event, expanded_height, expanded_width, feed_targeting, from, full_picture, height, icon, id, instagram_eligibility, is_app_share, is_eligible_for_promotion, is_expired, is_hidden, is_inline_created, is_instagram_eligible, is_popular, is_published, is_spherical, link, message, message_tags, multi_share_end_card, multi_share_optimized, name, object_id, parent_id, permalink_url, picture, place, privacy, promotable_id, promotion_status, properties, scheduled_publish_time, shares, source, status_type, story, story_tags, subscribed, target, targeting, timeline_visibility, type, updated_time, via, video_buying_eligibility, width
        primary_fb_page_id: Optional.
        primary_ig_user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if primary_fb_page_id is not None:
        params["primary_fb_page_id"] = primary_fb_page_id
    if primary_ig_user_id is not None:
        params["primary_ig_user_id"] = primary_ig_user_id
    result = await get_client().get(f"{post_id}", params=params)
    return json.dumps(result, indent=2)


async def update_post(
    post_id: str,
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
    """POST /#update on Post.

    Args:
        post_id: The ID of the Post object.
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
    result = await get_client().post(f"{post_id}", data=params)
    return json.dumps(result, indent=2)


COMMENT_FIELDS = [
    "admin_creator",
    "application",
    "attachment",
    "can_comment",
    "can_hide",
    "can_like",
    "can_remove",
    "can_reply_privately",
    "comment_count",
    "created_time",
    "from",
    "id",
    "is_hidden",
    "is_private",
    "like_count",
    "live_broadcast_timestamp",
    "message",
    "message_tags",
    "object",
    "parent",
    "permalink_url",
    "private_reply_conversation",
    "user_likes"
]


async def get_comment_comments(
    comment_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on Comment.

    Args:
        comment_id: The ID of the Comment object.
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
    result = await get_client().get(f"{comment_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_comment_comments(
    comment_id: str,
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
    """POST /comments on Comment.

    Args:
        comment_id: The ID of the Comment object.
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
    result = await get_client().post(f"{comment_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def delete_comment_likes(
    comment_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """DELETE /likes on Comment.

    Args:
        comment_id: The ID of the Comment object.
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
    result = await get_client().delete(f"{comment_id}/likes")
    return json.dumps(result, indent=2)


async def get_comment_likes(comment_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on Comment.

    Args:
        comment_id: The ID of the Comment object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{comment_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def create_comment_likes(
    comment_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on Comment.

    Args:
        comment_id: The ID of the Comment object.
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
    result = await get_client().post(f"{comment_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_comment_reactions(comment_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /reactions on Comment.

    Args:
        comment_id: The ID of the Comment object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: ANGRY, CARE, FIRE, HAHA, HUNDRED, LIKE, LOVE, NONE, PRIDE, SAD, THANKFUL, WOW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{comment_id}/reactions", params=params)
    return json.dumps(result, indent=2)


async def delete_comment(comment_id: str) -> str:
    """DELETE /#delete on Comment.

    Args:
        comment_id: The ID of the Comment object.
    """
    params = {}
    result = await get_client().delete(f"{comment_id}")
    return json.dumps(result, indent=2)


async def get_comment(comment_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Comment.

    Args:
        comment_id: The ID of the Comment object.
        fields: Comma-separated list of fields to return. Available: admin_creator, application, attachment, can_comment, can_hide, can_like, can_remove, can_reply_privately, comment_count, created_time, from, id, is_hidden, is_private, like_count, live_broadcast_timestamp, message, message_tags, object, parent, permalink_url, private_reply_conversation, user_likes
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{comment_id}", params=params)
    return json.dumps(result, indent=2)


async def update_comment(
    comment_id: str,
    attachment_id: Optional[str] = None,
    attachment_share_url: Optional[str] = None,
    attachment_url: Optional[str] = None,
    is_hidden: Optional[bool] = None,
    message: Optional[str] = None,
) -> str:
    """POST /#update on Comment.

    Args:
        comment_id: The ID of the Comment object.
        attachment_id: Optional.
        attachment_share_url: Optional.
        attachment_url: Optional.
        is_hidden: Optional.
        message: Optional.
    """
    params = {}
    if attachment_id is not None:
        params["attachment_id"] = attachment_id
    if attachment_share_url is not None:
        params["attachment_share_url"] = attachment_share_url
    if attachment_url is not None:
        params["attachment_url"] = attachment_url
    if is_hidden is not None:
        params["is_hidden"] = is_hidden
    if message is not None:
        params["message"] = message
    result = await get_client().post(f"{comment_id}", data=params)
    return json.dumps(result, indent=2)


PHOTO_FIELDS = [
    "album",
    "alt_text",
    "alt_text_custom",
    "backdated_time",
    "backdated_time_granularity",
    "can_backdate",
    "can_delete",
    "can_tag",
    "created_time",
    "event",
    "from",
    "height",
    "icon",
    "id",
    "images",
    "link",
    "name",
    "name_tags",
    "page_story_id",
    "picture",
    "place",
    "position",
    "source",
    "target",
    "updated_time",
    "webp_images",
    "width"
]


async def get_photo_comments(
    photo_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on Photo.

    Args:
        photo_id: The ID of the Photo object.
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
    result = await get_client().get(f"{photo_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_photo_comments(
    photo_id: str,
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
    """POST /comments on Photo.

    Args:
        photo_id: The ID of the Photo object.
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
    result = await get_client().post(f"{photo_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_photo_insights(
    photo_id: str,
    fields: Optional[str] = None,
    date_preset: Optional[str] = None,
    metric: Optional[str] = None,
    period: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on Photo.

    Args:
        photo_id: The ID of the Photo object.
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
    result = await get_client().get(f"{photo_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_photo_likes(photo_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on Photo.

    Args:
        photo_id: The ID of the Photo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{photo_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def create_photo_likes(
    photo_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    notify: Optional[bool] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on Photo.

    Args:
        photo_id: The ID of the Photo object.
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
    result = await get_client().post(f"{photo_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_photo_sponsor_tags(photo_id: str, fields: Optional[str] = None) -> str:
    """GET /sponsor_tags on Photo.

    Args:
        photo_id: The ID of the Photo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{photo_id}/sponsor_tags", params=params)
    return json.dumps(result, indent=2)


async def delete_photo(photo_id: str) -> str:
    """DELETE /#delete on Photo.

    Args:
        photo_id: The ID of the Photo object.
    """
    params = {}
    result = await get_client().delete(f"{photo_id}")
    return json.dumps(result, indent=2)


async def get_photo(photo_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Photo.

    Args:
        photo_id: The ID of the Photo object.
        fields: Comma-separated list of fields to return. Available: album, alt_text, alt_text_custom, backdated_time, backdated_time_granularity, can_backdate, can_delete, can_tag, created_time, event, from, height, icon, id, images, link, name, name_tags, page_story_id, picture, place, position, source, target, updated_time, webp_images, width
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{photo_id}", params=params)
    return json.dumps(result, indent=2)


ALBUM_FIELDS = [
    "backdated_time",
    "backdated_time_granularity",
    "can_backdate",
    "can_upload",
    "count",
    "cover_photo",
    "created_time",
    "description",
    "edit_link",
    "event",
    "from",
    "id",
    "is_user_facing",
    "link",
    "location",
    "modified_major",
    "name",
    "photo_count",
    "place",
    "privacy",
    "type",
    "updated_time",
    "video_count"
]


async def get_album_comments(
    album_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on Album.

    Args:
        album_id: The ID of the Album object.
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
    result = await get_client().get(f"{album_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_album_comments(
    album_id: str,
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
    """POST /comments on Album.

    Args:
        album_id: The ID of the Album object.
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
    result = await get_client().post(f"{album_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_album_likes(album_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on Album.

    Args:
        album_id: The ID of the Album object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{album_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def create_album_likes(
    album_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    notify: Optional[bool] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on Album.

    Args:
        album_id: The ID of the Album object.
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
    result = await get_client().post(f"{album_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_album_photos(album_id: str, fields: Optional[str] = None) -> str:
    """GET /photos on Album.

    Args:
        album_id: The ID of the Album object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{album_id}/photos", params=params)
    return json.dumps(result, indent=2)


async def create_album_photos(
    album_id: str,
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
    manual_privacy: Optional[bool] = None,
    message: Optional[str] = None,
    name: Optional[str] = None,
    no_story: Optional[bool] = None,
    offline_id: Optional[int] = None,
    og_action_type_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_set_profile_badge: Optional[bool] = None,
    og_suggestion_mechanism: Optional[str] = None,
    place: Optional[str] = None,
    privacy: Optional[str] = None,
    profile_id: Optional[int] = None,
    provenance_info: Optional[str] = None,
    proxied_app_id: Optional[str] = None,
    published: Optional[bool] = None,
    qn: Optional[str] = None,
    spherical_metadata: Optional[str] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    tags: Optional[str] = None,
    target_id: Optional[int] = None,
    targeting: Optional[str] = None,
    time_since_original_post: Optional[int] = None,
    uid: Optional[int] = None,
    unpublished_content_type: Optional[str] = None,
    url: Optional[str] = None,
    user_selected_tags: Optional[bool] = None,
    vault_image_id: Optional[str] = None,
) -> str:
    """POST /photos on Album.

    Args:
        album_id: The ID of the Album object.
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
        manual_privacy: Optional.
        message: Optional.
        name: Optional.
        no_story: Optional.
        offline_id: Optional.
        og_action_type_id: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_set_profile_badge: Optional.
        og_suggestion_mechanism: Optional.
        place: Optional.
        privacy: Optional.
        profile_id: Optional.
        provenance_info: Optional.
        proxied_app_id: Optional.
        published: Optional.
        qn: Optional.
        spherical_metadata: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        tags: Optional.
        target_id: Optional.
        targeting: Optional.
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
    if manual_privacy is not None:
        params["manual_privacy"] = manual_privacy
    if message is not None:
        params["message"] = message
    if name is not None:
        params["name"] = name
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
    result = await get_client().post(f"{album_id}/photos", data=params)
    return json.dumps(result, indent=2)


async def get_album_picture(
    album_id: str,
    fields: Optional[str] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /picture on Album.

    Args:
        album_id: The ID of the Album object.
        fields: Comma-separated list of fields to return.
        redirect: Optional.
        type_: Optional. Values: album, small, thumbnail
    """
    params = {}
    params["fields"] = fields or "id,name"
    if redirect is not None:
        params["redirect"] = redirect
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{album_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def get_album(album_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Album.

    Args:
        album_id: The ID of the Album object.
        fields: Comma-separated list of fields to return. Available: backdated_time, backdated_time_granularity, can_backdate, can_upload, count, cover_photo, created_time, description, edit_link, event, from, id, is_user_facing, link, location, modified_major, name, photo_count, place, privacy, type, updated_time, video_count
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{album_id}", params=params)
    return json.dumps(result, indent=2)


LIVE_VIDEO_FIELDS = [
    "ad_break_config",
    "ad_break_failure_reason",
    "broadcast_start_time",
    "copyright",
    "creation_time",
    "dash_ingest_url",
    "dash_preview_url",
    "description",
    "embed_html",
    "from",
    "id",
    "ingest_streams",
    "is_manual_mode",
    "is_reference_only",
    "live_views",
    "permalink_url",
    "planned_start_time",
    "recommended_encoder_settings",
    "seconds_left",
    "secure_stream_url",
    "status",
    "stream_url",
    "targeting",
    "title",
    "total_views",
    "video"
]


async def get_live_video_blocked_users(live_video_id: str, fields: Optional[str] = None, uid: Optional[str] = None) -> str:
    """GET /blocked_users on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
        uid: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if uid is not None:
        params["uid"] = uid
    result = await get_client().get(f"{live_video_id}/blocked_users", params=params)
    return json.dumps(result, indent=2)


async def get_live_video_comments(
    live_video_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
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
    result = await get_client().get(f"{live_video_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def get_live_video_crosspost_shared_pages(live_video_id: str, fields: Optional[str] = None) -> str:
    """GET /crosspost_shared_pages on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{live_video_id}/crosspost_shared_pages", params=params)
    return json.dumps(result, indent=2)


async def get_live_video_crossposted_broadcasts(live_video_id: str, fields: Optional[str] = None) -> str:
    """GET /crossposted_broadcasts on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{live_video_id}/crossposted_broadcasts", params=params)
    return json.dumps(result, indent=2)


async def get_live_video_errors(live_video_id: str, fields: Optional[str] = None) -> str:
    """GET /errors on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{live_video_id}/errors", params=params)
    return json.dumps(result, indent=2)


async def create_live_video_input_streams(live_video_id: str) -> str:
    """POST /input_streams on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
    """
    params = {}
    result = await get_client().post(f"{live_video_id}/input_streams", data=params)
    return json.dumps(result, indent=2)


async def get_live_video_polls(live_video_id: str, fields: Optional[str] = None) -> str:
    """GET /polls on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{live_video_id}/polls", params=params)
    return json.dumps(result, indent=2)


async def create_live_video_polls(
    live_video_id: str,
    options: str,
    question: str,
    close_after_voting: Optional[bool] = None,
    correct_option: Optional[int] = None,
    default_open: Optional[bool] = None,
    show_gradient: Optional[bool] = None,
    show_results: Optional[bool] = None,
) -> str:
    """POST /polls on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
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
    result = await get_client().post(f"{live_video_id}/polls", data=params)
    return json.dumps(result, indent=2)


async def get_live_video_reactions(live_video_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /reactions on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: ANGRY, CARE, FIRE, HAHA, HUNDRED, LIKE, LOVE, NONE, PRIDE, SAD, THANKFUL, WOW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{live_video_id}/reactions", params=params)
    return json.dumps(result, indent=2)


async def delete_live_video(live_video_id: str) -> str:
    """DELETE /#delete on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
    """
    params = {}
    result = await get_client().delete(f"{live_video_id}")
    return json.dumps(result, indent=2)


async def get_live_video(
    live_video_id: str,
    fields: Optional[str] = None,
    target_token: Optional[str] = None,
) -> str:
    """GET /#get on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        fields: Comma-separated list of fields to return. Available: ad_break_config, ad_break_failure_reason, broadcast_start_time, copyright, creation_time, dash_ingest_url, dash_preview_url, description, embed_html, from, id, ingest_streams, is_manual_mode, is_reference_only, live_views, permalink_url, planned_start_time, recommended_encoder_settings, seconds_left, secure_stream_url, status, stream_url, targeting, title, total_views, video
        target_token: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if target_token is not None:
        params["target_token"] = target_token
    result = await get_client().get(f"{live_video_id}", params=params)
    return json.dumps(result, indent=2)


async def update_live_video(
    live_video_id: str,
    allow_bm_crossposting: Optional[bool] = None,
    content_tags: Optional[str] = None,
    cross_share_to_group_ids: Optional[str] = None,
    crossposting_actions: Optional[str] = None,
    custom_labels: Optional[str] = None,
    description: Optional[str] = None,
    direct_share_status: Optional[int] = None,
    embeddable: Optional[bool] = None,
    end_live_video: Optional[bool] = None,
    event_params: Optional[str] = None,
    is_audio_only: Optional[bool] = None,
    is_manual_mode: Optional[bool] = None,
    live_comment_moderation_setting: Optional[str] = None,
    master_ingest_stream_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    persistent_stream_key_status: Optional[str] = None,
    place: Optional[str] = None,
    planned_start_time: Optional[str] = None,
    privacy: Optional[str] = None,
    published: Optional[bool] = None,
    schedule_custom_profile_image: Optional[str] = None,
    schedule_feed_background_image: Optional[str] = None,
    sponsor_id: Optional[str] = None,
    sponsor_relationship: Optional[int] = None,
    status: Optional[str] = None,
    stream_type: Optional[str] = None,
    tags: Optional[str] = None,
    targeting: Optional[str] = None,
    title: Optional[str] = None,
) -> str:
    """POST /#update on LiveVideo.

    Args:
        live_video_id: The ID of the LiveVideo object.
        allow_bm_crossposting: Optional.
        content_tags: Optional.
        cross_share_to_group_ids: Optional.
        crossposting_actions: Optional.
        custom_labels: Optional.
        description: Optional.
        direct_share_status: Optional.
        embeddable: Optional.
        end_live_video: Optional.
        event_params: Optional.
        is_audio_only: Optional.
        is_manual_mode: Optional.
        live_comment_moderation_setting: Optional.
        master_ingest_stream_id: Optional.
        og_icon_id: Optional.
        og_phrase: Optional.
        persistent_stream_key_status: Optional.
        place: Optional.
        planned_start_time: Optional.
        privacy: Optional.
        published: Optional.
        schedule_custom_profile_image: Optional.
        schedule_feed_background_image: Optional.
        sponsor_id: Optional.
        sponsor_relationship: Optional.
        status: Optional.
        stream_type: Optional.
        tags: Optional.
        targeting: Optional.
        title: Optional.
    """
    params = {}
    if allow_bm_crossposting is not None:
        params["allow_bm_crossposting"] = allow_bm_crossposting
    if content_tags is not None:
        params["content_tags"] = content_tags
    if cross_share_to_group_ids is not None:
        params["cross_share_to_group_ids"] = cross_share_to_group_ids
    if crossposting_actions is not None:
        params["crossposting_actions"] = crossposting_actions
    if custom_labels is not None:
        params["custom_labels"] = custom_labels
    if description is not None:
        params["description"] = description
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
    if embeddable is not None:
        params["embeddable"] = embeddable
    if end_live_video is not None:
        params["end_live_video"] = end_live_video
    if event_params is not None:
        params["event_params"] = event_params
    if is_audio_only is not None:
        params["is_audio_only"] = is_audio_only
    if is_manual_mode is not None:
        params["is_manual_mode"] = is_manual_mode
    if live_comment_moderation_setting is not None:
        params["live_comment_moderation_setting"] = live_comment_moderation_setting
    if master_ingest_stream_id is not None:
        params["master_ingest_stream_id"] = master_ingest_stream_id
    if og_icon_id is not None:
        params["og_icon_id"] = og_icon_id
    if og_phrase is not None:
        params["og_phrase"] = og_phrase
    if persistent_stream_key_status is not None:
        params["persistent_stream_key_status"] = persistent_stream_key_status
    if place is not None:
        params["place"] = place
    if planned_start_time is not None:
        params["planned_start_time"] = planned_start_time
    if privacy is not None:
        params["privacy"] = privacy
    if published is not None:
        params["published"] = published
    if schedule_custom_profile_image is not None:
        params["schedule_custom_profile_image"] = schedule_custom_profile_image
    if schedule_feed_background_image is not None:
        params["schedule_feed_background_image"] = schedule_feed_background_image
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
    if sponsor_relationship is not None:
        params["sponsor_relationship"] = sponsor_relationship
    if status is not None:
        params["status"] = status
    if stream_type is not None:
        params["stream_type"] = stream_type
    if tags is not None:
        params["tags"] = tags
    if targeting is not None:
        params["targeting"] = targeting
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{live_video_id}", data=params)
    return json.dumps(result, indent=2)


EVENT_FIELDS = [
    "attending_count",
    "can_guests_invite",
    "category",
    "cover",
    "created_time",
    "declined_count",
    "description",
    "discount_code_enabled",
    "end_time",
    "event_times",
    "guest_list_enabled",
    "id",
    "interested_count",
    "is_canceled",
    "is_draft",
    "is_online",
    "is_page_owned",
    "maybe_count",
    "name",
    "noreply_count",
    "online_event_format",
    "online_event_third_party_url",
    "owner",
    "parent_group",
    "place",
    "registration_setting",
    "scheduled_publish_time",
    "start_time",
    "ticket_setting",
    "ticket_uri",
    "ticket_uri_start_sales_time",
    "ticketing_privacy_uri",
    "ticketing_terms_uri",
    "timezone",
    "type",
    "updated_time"
]


async def get_event_comments(event_id: str, fields: Optional[str] = None) -> str:
    """GET /comments on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def get_event_feed(event_id: str, fields: Optional[str] = None) -> str:
    """GET /feed on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/feed", params=params)
    return json.dumps(result, indent=2)


async def get_event_live_videos(event_id: str, fields: Optional[str] = None) -> str:
    """GET /live_videos on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/live_videos", params=params)
    return json.dumps(result, indent=2)


async def create_event_live_videos(
    event_id: str,
    content_tags: Optional[str] = None,
    description: Optional[str] = None,
    enable_backup_ingest: Optional[bool] = None,
    encoding_settings: Optional[str] = None,
    event_params: Optional[str] = None,
    fisheye_video_cropped: Optional[bool] = None,
    front_z_rotation: Optional[float] = None,
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
    title: Optional[str] = None,
) -> str:
    """POST /live_videos on Event.

    Args:
        event_id: The ID of the Event object.
        content_tags: Optional.
        description: Optional.
        enable_backup_ingest: Optional.
        encoding_settings: Optional.
        event_params: Optional.
        fisheye_video_cropped: Optional.
        front_z_rotation: Optional.
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
        title: Optional.
    """
    params = {}
    if content_tags is not None:
        params["content_tags"] = content_tags
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
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{event_id}/live_videos", data=params)
    return json.dumps(result, indent=2)


async def get_event_photos(event_id: str, fields: Optional[str] = None) -> str:
    """GET /photos on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/photos", params=params)
    return json.dumps(result, indent=2)


async def get_event_picture(event_id: str, fields: Optional[str] = None) -> str:
    """GET /picture on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def get_event_posts(event_id: str, fields: Optional[str] = None) -> str:
    """GET /posts on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/posts", params=params)
    return json.dumps(result, indent=2)


async def get_event_roles(event_id: str, fields: Optional[str] = None) -> str:
    """GET /roles on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/roles", params=params)
    return json.dumps(result, indent=2)


async def get_event_ticket_tiers(event_id: str, fields: Optional[str] = None) -> str:
    """GET /ticket_tiers on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/ticket_tiers", params=params)
    return json.dumps(result, indent=2)


async def get_event_videos(event_id: str, fields: Optional[str] = None) -> str:
    """GET /videos on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}/videos", params=params)
    return json.dumps(result, indent=2)


async def get_event(event_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Event.

    Args:
        event_id: The ID of the Event object.
        fields: Comma-separated list of fields to return. Available: attending_count, can_guests_invite, category, cover, created_time, declined_count, description, discount_code_enabled, end_time, event_times, guest_list_enabled, id, interested_count, is_canceled, is_draft, is_online, is_page_owned, maybe_count, name, noreply_count, online_event_format, online_event_third_party_url, owner, parent_group, place, registration_setting, scheduled_publish_time, start_time, ticket_setting, ticket_uri, ticket_uri_start_sales_time, ticketing_privacy_uri, ticketing_terms_uri, timezone, type, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{event_id}", params=params)
    return json.dumps(result, indent=2)


STORIES_FIELDS = [
    "creation_time",
    "media_id",
    "media_type",
    "post_id",
    "status",
    "url"
]


async def get_stories_insights(stories_id: str, fields: Optional[str] = None, metric: Optional[str] = None) -> str:
    """GET /insights on Stories.

    Args:
        stories_id: The ID of the Stories object.
        fields: Comma-separated list of fields to return.
        metric: Optional. Values: PAGES_FB_STORY_REPLIES, PAGES_FB_STORY_SHARES, PAGES_FB_STORY_STICKER_INTERACTIONS, PAGES_FB_STORY_THREAD_LIGHTWEIGHT_REACTIONS, PAGE_STORY_IMPRESSIONS_BY_STORY_ID, PAGE_STORY_IMPRESSIONS_BY_STORY_ID_UNIQUE, STORY_INTERACTION
    """
    params = {}
    params["fields"] = fields or "id,name"
    if metric is not None:
        params["metric"] = metric
    result = await get_client().get(f"{stories_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_stories(stories_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Stories.

    Args:
        stories_id: The ID of the Stories object.
        fields: Comma-separated list of fields to return. Available: creation_time, media_id, media_type, post_id, status, url
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{stories_id}", params=params)
    return json.dumps(result, indent=2)


LINK_FIELDS = [
    "caption",
    "created_time",
    "description",
    "from",
    "icon",
    "id",
    "link",
    "message",
    "multi_share_optimized",
    "name",
    "privacy",
    "via"
]


async def create_link_comments(
    link_id: str,
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
    """POST /comments on Link.

    Args:
        link_id: The ID of the Link object.
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
    result = await get_client().post(f"{link_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_link_likes(link_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on Link.

    Args:
        link_id: The ID of the Link object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{link_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def get_link(link_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Link.

    Args:
        link_id: The ID of the Link object.
        fields: Comma-separated list of fields to return. Available: caption, created_time, description, from, icon, id, link, message, multi_share_optimized, name, privacy, via
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{link_id}", params=params)
    return json.dumps(result, indent=2)


STATUS_FIELDS = [
    "event",
    "from",
    "id",
    "message",
    "place",
    "updated_time"
]


async def create_status_likes(
    status_id: str,
    feedback_source: Optional[str] = None,
    nectar_module: Optional[str] = None,
    notify: Optional[bool] = None,
    tracking: Optional[str] = None,
) -> str:
    """POST /likes on Status.

    Args:
        status_id: The ID of the Status object.
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
    result = await get_client().post(f"{status_id}/likes", data=params)
    return json.dumps(result, indent=2)


async def get_status(status_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Status.

    Args:
        status_id: The ID of the Status object.
        fields: Comma-separated list of fields to return. Available: event, from, id, message, place, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{status_id}", params=params)
    return json.dumps(result, indent=2)

