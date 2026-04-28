"""Auto-generated Meta Marketing API tools — media."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


MEDIA_TITLE_FIELDS = [
    "applinks",
    "category_specific_fields",
    "content_category",
    "currency",
    "description",
    "fb_page_alias",
    "fb_page_id",
    "genres",
    "id",
    "image_fetch_status",
    "images",
    "kg_fb_id",
    "media_title_id",
    "price",
    "sanitized_images",
    "title",
    "title_display_name",
    "unit_price",
    "url",
    "visibility",
    "wiki_data_item"
]


async def get_media_title_channels_to_integrity_status(media_title_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{media_title_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_media_title_override_details(
    media_title_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
        fields: Comma-separated list of fields to return.
        keys: Optional.
        type_: Optional. Values: COUNTRY, LANGUAGE, LANGUAGE_AND_COUNTRY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if keys is not None:
        params["keys"] = keys
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{media_title_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_media_title_videos_metadata(media_title_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{media_title_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def delete_media_title(media_title_id: str) -> str:
    """DELETE /#delete on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
    """
    params = {}
    result = await get_client().delete(f"{media_title_id}")
    return json.dumps(result, indent=2)


async def get_media_title(media_title_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
        fields: Comma-separated list of fields to return. Available: applinks, category_specific_fields, content_category, currency, description, fb_page_alias, fb_page_id, genres, id, image_fetch_status, images, kg_fb_id, media_title_id, price, sanitized_images, title, title_display_name, unit_price, url, visibility, wiki_data_item
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{media_title_id}", params=params)
    return json.dumps(result, indent=2)


async def update_media_title(
    media_title_id: str,
    applinks: Optional[str] = None,
    content_category: Optional[str] = None,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    fb_page_id: Optional[str] = None,
    genres: Optional[str] = None,
    images: Optional[str] = None,
    kg_fb_id: Optional[str] = None,
    price: Optional[int] = None,
    title: Optional[str] = None,
    title_display_name: Optional[str] = None,
    url: Optional[str] = None,
) -> str:
    """POST /#update on MediaTitle.

    Args:
        media_title_id: The ID of the MediaTitle object.
        applinks: Optional.
        content_category: Optional.
        currency: Optional.
        description: Optional.
        fb_page_id: Optional.
        genres: Optional.
        images: Optional.
        kg_fb_id: Optional.
        price: Optional.
        title: Optional.
        title_display_name: Optional.
        url: Optional.
    """
    params = {}
    if applinks is not None:
        params["applinks"] = applinks
    if content_category is not None:
        params["content_category"] = content_category
    if currency is not None:
        params["currency"] = currency
    if description is not None:
        params["description"] = description
    if fb_page_id is not None:
        params["fb_page_id"] = fb_page_id
    if genres is not None:
        params["genres"] = genres
    if images is not None:
        params["images"] = images
    if kg_fb_id is not None:
        params["kg_fb_id"] = kg_fb_id
    if price is not None:
        params["price"] = price
    if title is not None:
        params["title"] = title
    if title_display_name is not None:
        params["title_display_name"] = title_display_name
    if url is not None:
        params["url"] = url
    result = await get_client().post(f"{media_title_id}", data=params)
    return json.dumps(result, indent=2)


MEDIA_FINGERPRINT_FIELDS = [
    "duration_in_sec",
    "fingerprint_content_type",
    "fingerprint_type",
    "id",
    "metadata",
    "title",
    "universal_content_id"
]


async def get_media_fingerprint(media_fingerprint_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on MediaFingerprint.

    Args:
        media_fingerprint_id: The ID of the MediaFingerprint object.
        fields: Comma-separated list of fields to return. Available: duration_in_sec, fingerprint_content_type, fingerprint_type, id, metadata, title, universal_content_id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{media_fingerprint_id}", params=params)
    return json.dumps(result, indent=2)


async def update_media_fingerprint(
    media_fingerprint_id: str,
    metadata: Optional[str] = None,
    source: Optional[str] = None,
    title: Optional[str] = None,
    universal_content_id: Optional[str] = None,
) -> str:
    """POST /#update on MediaFingerprint.

    Args:
        media_fingerprint_id: The ID of the MediaFingerprint object.
        metadata: Optional.
        source: Optional.
        title: Optional.
        universal_content_id: Optional.
    """
    params = {}
    if metadata is not None:
        params["metadata"] = metadata
    if source is not None:
        params["source"] = source
    if title is not None:
        params["title"] = title
    if universal_content_id is not None:
        params["universal_content_id"] = universal_content_id
    result = await get_client().post(f"{media_fingerprint_id}", data=params)
    return json.dumps(result, indent=2)


VIDEO_LIST_FIELDS = [
    "creation_time",
    "description",
    "id",
    "last_modified",
    "owner",
    "season_number",
    "thumbnail",
    "title",
    "videos_count"
]


async def get_video_list_videos(video_list_id: str, fields: Optional[str] = None) -> str:
    """GET /videos on VideoList.

    Args:
        video_list_id: The ID of the VideoList object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_list_id}/videos", params=params)
    return json.dumps(result, indent=2)


async def get_video_list(video_list_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on VideoList.

    Args:
        video_list_id: The ID of the VideoList object.
        fields: Comma-separated list of fields to return. Available: creation_time, description, id, last_modified, owner, season_number, thumbnail, title, videos_count
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_list_id}", params=params)
    return json.dumps(result, indent=2)


VIDEO_POLL_FIELDS = [
    "close_after_voting",
    "default_open",
    "id",
    "question",
    "show_gradient",
    "show_results",
    "status"
]


async def get_video_poll_poll_options(video_poll_id: str, fields: Optional[str] = None) -> str:
    """GET /poll_options on VideoPoll.

    Args:
        video_poll_id: The ID of the VideoPoll object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_poll_id}/poll_options", params=params)
    return json.dumps(result, indent=2)


async def get_video_poll(video_poll_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on VideoPoll.

    Args:
        video_poll_id: The ID of the VideoPoll object.
        fields: Comma-separated list of fields to return. Available: close_after_voting, default_open, id, question, show_gradient, show_results, status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_poll_id}", params=params)
    return json.dumps(result, indent=2)


async def update_video_poll(
    video_poll_id: str,
    action: str,
    close_after_voting: Optional[bool] = None,
    default_open: Optional[bool] = None,
    show_gradient: Optional[bool] = None,
    show_results: Optional[bool] = None,
) -> str:
    """POST /#update on VideoPoll.

    Args:
        video_poll_id: The ID of the VideoPoll object.
        action: Required.
        close_after_voting: Optional.
        default_open: Optional.
        show_gradient: Optional.
        show_results: Optional.
    """
    params = {}
    params["action"] = action
    if close_after_voting is not None:
        params["close_after_voting"] = close_after_voting
    if default_open is not None:
        params["default_open"] = default_open
    if show_gradient is not None:
        params["show_gradient"] = show_gradient
    if show_results is not None:
        params["show_results"] = show_results
    result = await get_client().post(f"{video_poll_id}", data=params)
    return json.dumps(result, indent=2)


VIDEO_COPYRIGHT_FIELDS = [
    "content_category",
    "content_protect_protection_disabled_reason",
    "copyright_content_id",
    "creator",
    "disable_protection_by_content_protect_status",
    "excluded_ownership_segments",
    "id",
    "in_conflict",
    "monitoring_status",
    "monitoring_type",
    "ownership_countries",
    "reference_file",
    "reference_file_disabled",
    "reference_file_disabled_by_ops",
    "reference_owner_id",
    "rule_ids",
    "tags",
    "whitelisted_ids"
]


async def get_video_copyright_update_records(video_copyright_id: str, fields: Optional[str] = None) -> str:
    """GET /update_records on VideoCopyright.

    Args:
        video_copyright_id: The ID of the VideoCopyright object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_copyright_id}/update_records", params=params)
    return json.dumps(result, indent=2)


async def get_video_copyright(video_copyright_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on VideoCopyright.

    Args:
        video_copyright_id: The ID of the VideoCopyright object.
        fields: Comma-separated list of fields to return. Available: content_category, content_protect_protection_disabled_reason, copyright_content_id, creator, disable_protection_by_content_protect_status, excluded_ownership_segments, id, in_conflict, monitoring_status, monitoring_type, ownership_countries, reference_file, reference_file_disabled, reference_file_disabled_by_ops, reference_owner_id, rule_ids, tags, whitelisted_ids
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{video_copyright_id}", params=params)
    return json.dumps(result, indent=2)


async def update_video_copyright(
    video_copyright_id: str,
    append_excluded_ownership_segments: Optional[bool] = None,
    attribution_id: Optional[str] = None,
    content_category: Optional[str] = None,
    excluded_ownership_countries: Optional[str] = None,
    excluded_ownership_segments: Optional[str] = None,
    is_reference_disabled: Optional[bool] = None,
    monitoring_type: Optional[str] = None,
    ownership_countries: Optional[str] = None,
    rule_id: Optional[str] = None,
    whitelisted_ids: Optional[str] = None,
    whitelisted_ig_user_ids: Optional[str] = None,
) -> str:
    """POST /#update on VideoCopyright.

    Args:
        video_copyright_id: The ID of the VideoCopyright object.
        append_excluded_ownership_segments: Optional.
        attribution_id: Optional.
        content_category: Optional.
        excluded_ownership_countries: Optional.
        excluded_ownership_segments: Optional.
        is_reference_disabled: Optional.
        monitoring_type: Optional.
        ownership_countries: Optional.
        rule_id: Optional.
        whitelisted_ids: Optional.
        whitelisted_ig_user_ids: Optional.
    """
    params = {}
    if append_excluded_ownership_segments is not None:
        params["append_excluded_ownership_segments"] = append_excluded_ownership_segments
    if attribution_id is not None:
        params["attribution_id"] = attribution_id
    if content_category is not None:
        params["content_category"] = content_category
    if excluded_ownership_countries is not None:
        params["excluded_ownership_countries"] = excluded_ownership_countries
    if excluded_ownership_segments is not None:
        params["excluded_ownership_segments"] = excluded_ownership_segments
    if is_reference_disabled is not None:
        params["is_reference_disabled"] = is_reference_disabled
    if monitoring_type is not None:
        params["monitoring_type"] = monitoring_type
    if ownership_countries is not None:
        params["ownership_countries"] = ownership_countries
    if rule_id is not None:
        params["rule_id"] = rule_id
    if whitelisted_ids is not None:
        params["whitelisted_ids"] = whitelisted_ids
    if whitelisted_ig_user_ids is not None:
        params["whitelisted_ig_user_ids"] = whitelisted_ig_user_ids
    result = await get_client().post(f"{video_copyright_id}", data=params)
    return json.dumps(result, indent=2)


AUDIO_COPYRIGHT_FIELDS = [
    "creation_time",
    "displayed_matches_count",
    "id",
    "in_conflict",
    "isrc",
    "match_rule",
    "ownership_countries",
    "ownership_details",
    "reference_file_status",
    "ridge_monitoring_status",
    "tags",
    "update_time",
    "whitelisted_fb_users",
    "whitelisted_ig_users"
]


async def get_audio_copyright_update_records(audio_copyright_id: str, fields: Optional[str] = None) -> str:
    """GET /update_records on AudioCopyright.

    Args:
        audio_copyright_id: The ID of the AudioCopyright object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{audio_copyright_id}/update_records", params=params)
    return json.dumps(result, indent=2)


async def get_audio_copyright(audio_copyright_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AudioCopyright.

    Args:
        audio_copyright_id: The ID of the AudioCopyright object.
        fields: Comma-separated list of fields to return. Available: creation_time, displayed_matches_count, id, in_conflict, isrc, match_rule, ownership_countries, ownership_details, reference_file_status, ridge_monitoring_status, tags, update_time, whitelisted_fb_users, whitelisted_ig_users
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{audio_copyright_id}", params=params)
    return json.dumps(result, indent=2)


IMAGE_COPYRIGHT_FIELDS = [
    "artist",
    "copyright_monitoring_status",
    "creation_time",
    "creator",
    "custom_id",
    "description",
    "filename",
    "id",
    "image",
    "matches_count",
    "original_content_creation_date",
    "ownership_countries",
    "tags",
    "title",
    "update_time"
]


async def get_image_copyright(image_copyright_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ImageCopyright.

    Args:
        image_copyright_id: The ID of the ImageCopyright object.
        fields: Comma-separated list of fields to return. Available: artist, copyright_monitoring_status, creation_time, creator, custom_id, description, filename, id, image, matches_count, original_content_creation_date, ownership_countries, tags, title, update_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{image_copyright_id}", params=params)
    return json.dumps(result, indent=2)


async def update_image_copyright(
    image_copyright_id: str,
    artist: Optional[str] = None,
    creator: Optional[str] = None,
    custom_id: Optional[str] = None,
    description: Optional[str] = None,
    geo_ownership: Optional[str] = None,
    original_content_creation_date: Optional[int] = None,
    title: Optional[str] = None,
) -> str:
    """POST /#update on ImageCopyright.

    Args:
        image_copyright_id: The ID of the ImageCopyright object.
        artist: Optional.
        creator: Optional.
        custom_id: Optional.
        description: Optional.
        geo_ownership: Optional.
        original_content_creation_date: Optional.
        title: Optional.
    """
    params = {}
    if artist is not None:
        params["artist"] = artist
    if creator is not None:
        params["creator"] = creator
    if custom_id is not None:
        params["custom_id"] = custom_id
    if description is not None:
        params["description"] = description
    if geo_ownership is not None:
        params["geo_ownership"] = geo_ownership
    if original_content_creation_date is not None:
        params["original_content_creation_date"] = original_content_creation_date
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{image_copyright_id}", data=params)
    return json.dumps(result, indent=2)


RTB_DYNAMIC_POST_FIELDS = [
    "child_attachments",
    "created",
    "description",
    "id",
    "image_url",
    "link",
    "message",
    "owner_id",
    "place_id",
    "product_id",
    "title"
]


async def get_rtb_dynamic_post_comments(
    rtb_dynamic_post_id: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
    live_filter: Optional[str] = None,
    order: Optional[str] = None,
    since: Optional[str] = None,
) -> str:
    """GET /comments on RTBDynamicPost.

    Args:
        rtb_dynamic_post_id: The ID of the RTBDynamicPost object.
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
    result = await get_client().get(f"{rtb_dynamic_post_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def get_rtb_dynamic_post_likes(rtb_dynamic_post_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on RTBDynamicPost.

    Args:
        rtb_dynamic_post_id: The ID of the RTBDynamicPost object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{rtb_dynamic_post_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def get_rtb_dynamic_post(rtb_dynamic_post_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on RTBDynamicPost.

    Args:
        rtb_dynamic_post_id: The ID of the RTBDynamicPost object.
        fields: Comma-separated list of fields to return. Available: child_attachments, created, description, id, image_url, link, message, owner_id, place_id, product_id, title
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{rtb_dynamic_post_id}", params=params)
    return json.dumps(result, indent=2)

