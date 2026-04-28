"""Auto-generated Meta Marketing API tools — groups."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


GROUP_FIELDS = [
    "archived",
    "cover",
    "created_time",
    "description",
    "email",
    "icon",
    "id",
    "install",
    "link",
    "member_count",
    "member_request_count",
    "name",
    "parent",
    "permissions",
    "privacy",
    "purpose",
    "subdomain",
    "updated_time",
    "venue"
]


async def delete_group_admins(group_id: str, uid: int) -> str:
    """DELETE /admins on Group.

    Args:
        group_id: The ID of the Group object.
        uid: Required.
    """
    params = {}
    params["uid"] = uid
    result = await get_client().delete(f"{group_id}/admins")
    return json.dumps(result, indent=2)


async def create_group_admins(group_id: str, uid: int) -> str:
    """POST /admins on Group.

    Args:
        group_id: The ID of the Group object.
        uid: Required.
    """
    params = {}
    params["uid"] = uid
    result = await get_client().post(f"{group_id}/admins", data=params)
    return json.dumps(result, indent=2)


async def get_group_albums(group_id: str, fields: Optional[str] = None) -> str:
    """GET /albums on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/albums", params=params)
    return json.dumps(result, indent=2)


async def get_group_docs(group_id: str, fields: Optional[str] = None) -> str:
    """GET /docs on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/docs", params=params)
    return json.dumps(result, indent=2)


async def get_group_events(group_id: str, fields: Optional[str] = None) -> str:
    """GET /events on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/events", params=params)
    return json.dumps(result, indent=2)


async def get_group_feed(
    group_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    q: Optional[str] = None,
    show_expired: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /feed on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
        include_hidden: Optional.
        q: Optional.
        show_expired: Optional.
        since: Optional.
        until: Optional.
        with_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_hidden is not None:
        params["include_hidden"] = include_hidden
    if q is not None:
        params["q"] = q
    if show_expired is not None:
        params["show_expired"] = show_expired
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    if with_ is not None:
        params["with"] = with_
    result = await get_client().get(f"{group_id}/feed", params=params)
    return json.dumps(result, indent=2)


async def create_group_feed(
    group_id: str,
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
    """POST /feed on Group.

    Args:
        group_id: The ID of the Group object.
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
    result = await get_client().post(f"{group_id}/feed", data=params)
    return json.dumps(result, indent=2)


async def get_group_files(group_id: str, fields: Optional[str] = None) -> str:
    """GET /files on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/files", params=params)
    return json.dumps(result, indent=2)


async def get_group_groups(group_id: str, fields: Optional[str] = None) -> str:
    """GET /groups on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/groups", params=params)
    return json.dumps(result, indent=2)


async def create_group_groups(
    group_id: str,
    name: str,
    admin: Optional[int] = None,
    description: Optional[str] = None,
    group_icon_id: Optional[str] = None,
    group_type: Optional[str] = None,
    join_setting: Optional[str] = None,
    parent_id: Optional[str] = None,
    post_permissions: Optional[str] = None,
    post_requires_admin_approval: Optional[bool] = None,
    privacy: Optional[str] = None,
    ref: Optional[str] = None,
) -> str:
    """POST /groups on Group.

    Args:
        group_id: The ID of the Group object.
        admin: Optional.
        description: Optional.
        group_icon_id: Optional.
        group_type: Optional. Values: CASUAL, COWORKERS, CUSTOM, FOR_SALE, FOR_WORK, GAME, HEALTH_SUPPORT, JOBS, LEARNING, NONE, PARENTING, STREAMER, WORK_ANNOUNCEMENT, WORK_DEMO_GROUP, WORK_DISCUSSION, WORK_EPHEMERAL, WORK_FEEDBACK, WORK_FOR_SALE, WORK_GARDEN, WORK_INTEGRITY, WORK_LEARNING, WORK_MENTORSHIP, WORK_MULTI_COMPANY, WORK_RECRUITING, WORK_SOCIAL, WORK_STAGES, WORK_TEAM, WORK_TEAMWORK
        join_setting: Optional. Values: ADMIN_ONLY, ANYONE, NONE
        name: Required.
        parent_id: Optional.
        post_permissions: Optional. Values: ADMIN_ONLY, ANYONE, NONE
        post_requires_admin_approval: Optional.
        privacy: Optional.
        ref: Optional.
    """
    params = {}
    if admin is not None:
        params["admin"] = admin
    if description is not None:
        params["description"] = description
    if group_icon_id is not None:
        params["group_icon_id"] = group_icon_id
    if group_type is not None:
        params["group_type"] = group_type
    if join_setting is not None:
        params["join_setting"] = join_setting
    params["name"] = name
    if parent_id is not None:
        params["parent_id"] = parent_id
    if post_permissions is not None:
        params["post_permissions"] = post_permissions
    if post_requires_admin_approval is not None:
        params["post_requires_admin_approval"] = post_requires_admin_approval
    if privacy is not None:
        params["privacy"] = privacy
    if ref is not None:
        params["ref"] = ref
    result = await get_client().post(f"{group_id}/groups", data=params)
    return json.dumps(result, indent=2)


async def get_group_live_videos(
    group_id: str,
    fields: Optional[str] = None,
    broadcast_status: Optional[str] = None,
    source: Optional[str] = None,
) -> str:
    """GET /live_videos on Group.

    Args:
        group_id: The ID of the Group object.
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
    result = await get_client().get(f"{group_id}/live_videos", params=params)
    return json.dumps(result, indent=2)


async def create_group_live_videos(
    group_id: str,
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
    """POST /live_videos on Group.

    Args:
        group_id: The ID of the Group object.
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
    result = await get_client().post(f"{group_id}/live_videos", data=params)
    return json.dumps(result, indent=2)


async def delete_group_members(group_id: str, email: Optional[str] = None, member: Optional[int] = None) -> str:
    """DELETE /members on Group.

    Args:
        group_id: The ID of the Group object.
        email: Optional.
        member: Optional.
    """
    params = {}
    if email is not None:
        params["email"] = email
    if member is not None:
        params["member"] = member
    result = await get_client().delete(f"{group_id}/members")
    return json.dumps(result, indent=2)


async def create_group_members(
    group_id: str,
    email: Optional[str] = None,
    from_: Optional[int] = None,
    member: Optional[int] = None,
    rate: Optional[int] = None,
    source: Optional[str] = None,
) -> str:
    """POST /members on Group.

    Args:
        group_id: The ID of the Group object.
        email: Optional.
        from_: Optional.
        member: Optional.
        rate: Optional.
        source: Optional.
    """
    params = {}
    if email is not None:
        params["email"] = email
    if from_ is not None:
        params["from"] = from_
    if member is not None:
        params["member"] = member
    if rate is not None:
        params["rate"] = rate
    if source is not None:
        params["source"] = source
    result = await get_client().post(f"{group_id}/members", data=params)
    return json.dumps(result, indent=2)


async def get_group_opted_in_members(group_id: str, fields: Optional[str] = None) -> str:
    """GET /opted_in_members on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{group_id}/opted_in_members", params=params)
    return json.dumps(result, indent=2)


async def create_group_photos(
    group_id: str,
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
    """POST /photos on Group.

    Args:
        group_id: The ID of the Group object.
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
    result = await get_client().post(f"{group_id}/photos", data=params)
    return json.dumps(result, indent=2)


async def get_group_picture(
    group_id: str,
    fields: Optional[str] = None,
    height: Optional[int] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /picture on Group.

    Args:
        group_id: The ID of the Group object.
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
    result = await get_client().get(f"{group_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def get_group_videos(group_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /videos on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: tagged, uploaded
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{group_id}/videos", params=params)
    return json.dumps(result, indent=2)


async def create_group_videos(
    group_id: str,
    application_id: Optional[str] = None,
    asked_fun_fact_prompt_id: Optional[int] = None,
    audio_story_wave_animation_handle: Optional[str] = None,
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
    is_explicit_share: Optional[bool] = None,
    is_group_linking_post: Optional[bool] = None,
    is_partnership_ad: Optional[bool] = None,
    is_voice_clip: Optional[bool] = None,
    location_source_id: Optional[str] = None,
    manual_privacy: Optional[bool] = None,
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
    referenced_sticker_id: Optional[str] = None,
    replace_video_id: Optional[str] = None,
    scheduled_publish_time: Optional[int] = None,
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
    """POST /videos on Group.

    Args:
        group_id: The ID of the Group object.
        application_id: Optional.
        asked_fun_fact_prompt_id: Optional.
        audio_story_wave_animation_handle: Optional.
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
        is_explicit_share: Optional.
        is_group_linking_post: Optional.
        is_partnership_ad: Optional.
        is_voice_clip: Optional.
        location_source_id: Optional.
        manual_privacy: Optional.
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
        referenced_sticker_id: Optional.
        replace_video_id: Optional.
        scheduled_publish_time: Optional.
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
    if referenced_sticker_id is not None:
        params["referenced_sticker_id"] = referenced_sticker_id
    if replace_video_id is not None:
        params["replace_video_id"] = replace_video_id
    if scheduled_publish_time is not None:
        params["scheduled_publish_time"] = scheduled_publish_time
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
    result = await get_client().post(f"{group_id}/videos", data=params)
    return json.dumps(result, indent=2)


async def get_group(group_id: str, fields: Optional[str] = None, icon_size: Optional[str] = None) -> str:
    """GET /#get on Group.

    Args:
        group_id: The ID of the Group object.
        fields: Comma-separated list of fields to return. Available: archived, cover, created_time, description, email, icon, id, install, link, member_count, member_request_count, name, parent, permissions, privacy, purpose, subdomain, updated_time, venue
        icon_size: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if icon_size is not None:
        params["icon_size"] = icon_size
    result = await get_client().get(f"{group_id}", params=params)
    return json.dumps(result, indent=2)


async def update_group(
    group_id: str,
    cover: Optional[str] = None,
    cover_url: Optional[str] = None,
    description: Optional[str] = None,
    focus_x: Optional[float] = None,
    focus_y: Optional[float] = None,
    group_icon: Optional[str] = None,
    is_official_group: Optional[bool] = None,
    join_setting: Optional[str] = None,
    name: Optional[str] = None,
    no_feed_story: Optional[bool] = None,
    offset_y: Optional[int] = None,
    post_permissions: Optional[str] = None,
    post_requires_admin_approval: Optional[bool] = None,
    privacy: Optional[str] = None,
    purpose: Optional[str] = None,
    update_view_time: Optional[bool] = None,
) -> str:
    """POST /#update on Group.

    Args:
        group_id: The ID of the Group object.
        cover: Optional.
        cover_url: Optional.
        description: Optional.
        focus_x: Optional.
        focus_y: Optional.
        group_icon: Optional.
        is_official_group: Optional.
        join_setting: Optional.
        name: Optional.
        no_feed_story: Optional.
        offset_y: Optional.
        post_permissions: Optional.
        post_requires_admin_approval: Optional.
        privacy: Optional.
        purpose: Optional.
        update_view_time: Optional.
    """
    params = {}
    if cover is not None:
        params["cover"] = cover
    if cover_url is not None:
        params["cover_url"] = cover_url
    if description is not None:
        params["description"] = description
    if focus_x is not None:
        params["focus_x"] = focus_x
    if focus_y is not None:
        params["focus_y"] = focus_y
    if group_icon is not None:
        params["group_icon"] = group_icon
    if is_official_group is not None:
        params["is_official_group"] = is_official_group
    if join_setting is not None:
        params["join_setting"] = join_setting
    if name is not None:
        params["name"] = name
    if no_feed_story is not None:
        params["no_feed_story"] = no_feed_story
    if offset_y is not None:
        params["offset_y"] = offset_y
    if post_permissions is not None:
        params["post_permissions"] = post_permissions
    if post_requires_admin_approval is not None:
        params["post_requires_admin_approval"] = post_requires_admin_approval
    if privacy is not None:
        params["privacy"] = privacy
    if purpose is not None:
        params["purpose"] = purpose
    if update_view_time is not None:
        params["update_view_time"] = update_view_time
    result = await get_client().post(f"{group_id}", data=params)
    return json.dumps(result, indent=2)

