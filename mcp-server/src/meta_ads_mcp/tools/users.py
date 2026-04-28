"""Auto-generated Meta Marketing API tools — users."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


USER_FIELDS = [
    "about",
    "age_range",
    "birthday",
    "client_business_id",
    "community",
    "cover",
    "currency",
    "education",
    "email",
    "favorite_athletes",
    "favorite_teams",
    "first_name",
    "gender",
    "hometown",
    "id",
    "inspirational_people",
    "install_type",
    "installed",
    "is_guest_user",
    "is_work_account",
    "languages",
    "last_name",
    "link",
    "local_news_megaphone_dismiss_status",
    "local_news_subscription_status",
    "locale",
    "location",
    "meeting_for",
    "middle_name",
    "name",
    "name_format",
    "payment_pricepoints",
    "political",
    "profile_pic",
    "quotes",
    "relationship_status",
    "religion",
    "shared_login_upgrade_required_by",
    "short_name",
    "significant_other",
    "sports",
    "supports_donate_button_in_live_video",
    "third_party_id",
    "timezone",
    "token_for_business",
    "updated_time",
    "verified",
    "video_upload_limits",
    "website"
]


async def delete_user_access_tokens(user_id: str) -> str:
    """DELETE /access_tokens on User.

    Args:
        user_id: The ID of the User object.
    """
    params = {}
    result = await get_client().delete(f"{user_id}/access_tokens")
    return json.dumps(result, indent=2)


async def create_user_access_tokens(
    user_id: str,
    business_app: str,
    page_id: Optional[str] = None,
    scope: Optional[str] = None,
    set_token_expires_in_60_days: Optional[bool] = None,
) -> str:
    """POST /access_tokens on User.

    Args:
        user_id: The ID of the User object.
        business_app: Required.
        page_id: Optional.
        scope: Optional.
        set_token_expires_in_60_days: Optional.
    """
    params = {}
    params["business_app"] = business_app
    if page_id is not None:
        params["page_id"] = page_id
    if scope is not None:
        params["scope"] = scope
    if set_token_expires_in_60_days is not None:
        params["set_token_expires_in_60_days"] = set_token_expires_in_60_days
    result = await get_client().post(f"{user_id}/access_tokens", data=params)
    return json.dumps(result, indent=2)


async def get_user_accounts(
    user_id: str,
    fields: Optional[str] = None,
    ad_id: Optional[str] = None,
    is_place: Optional[bool] = None,
    is_promotable: Optional[bool] = None,
) -> str:
    """GET /accounts on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        ad_id: Optional.
        is_place: Optional.
        is_promotable: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_id is not None:
        params["ad_id"] = ad_id
    if is_place is not None:
        params["is_place"] = is_place
    if is_promotable is not None:
        params["is_promotable"] = is_promotable
    result = await get_client().get(f"{user_id}/accounts", params=params)
    return json.dumps(result, indent=2)


async def create_user_accounts(
    user_id: str,
    name: str,
    about: Optional[str] = None,
    address: Optional[str] = None,
    category: Optional[int] = None,
    category_enum: Optional[str] = None,
    category_list: Optional[str] = None,
    city_id: Optional[str] = None,
    coordinates: Optional[str] = None,
    cover_photo: Optional[str] = None,
    description: Optional[str] = None,
    ignore_coordinate_warnings: Optional[bool] = None,
    location: Optional[str] = None,
    phone: Optional[str] = None,
    picture: Optional[str] = None,
    website: Optional[str] = None,
    zip_: Optional[str] = None,
) -> str:
    """POST /accounts on User.

    Args:
        user_id: The ID of the User object.
        about: Optional.
        address: Optional.
        category: Optional.
        category_enum: Optional.
        category_list: Optional.
        city_id: Optional.
        coordinates: Optional.
        cover_photo: Optional.
        description: Optional.
        ignore_coordinate_warnings: Optional.
        location: Optional.
        name: Required.
        phone: Optional.
        picture: Optional.
        website: Optional.
        zip_: Optional.
    """
    params = {}
    if about is not None:
        params["about"] = about
    if address is not None:
        params["address"] = address
    if category is not None:
        params["category"] = category
    if category_enum is not None:
        params["category_enum"] = category_enum
    if category_list is not None:
        params["category_list"] = category_list
    if city_id is not None:
        params["city_id"] = city_id
    if coordinates is not None:
        params["coordinates"] = coordinates
    if cover_photo is not None:
        params["cover_photo"] = cover_photo
    if description is not None:
        params["description"] = description
    if ignore_coordinate_warnings is not None:
        params["ignore_coordinate_warnings"] = ignore_coordinate_warnings
    if location is not None:
        params["location"] = location
    params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if picture is not None:
        params["picture"] = picture
    if website is not None:
        params["website"] = website
    if zip_ is not None:
        params["zip"] = zip_
    result = await get_client().post(f"{user_id}/accounts", data=params)
    return json.dumps(result, indent=2)


async def get_user_ad_studies(user_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_studies on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/ad_studies", params=params)
    return json.dumps(result, indent=2)


async def create_user_ad_studies(
    user_id: str,
    cells: Optional[str] = None,
    client_business: Optional[str] = None,
    confidence_level: Optional[float] = None,
    cooldown_start_time: Optional[int] = None,
    description: Optional[str] = None,
    end_time: Optional[int] = None,
    name: Optional[str] = None,
    objectives: Optional[str] = None,
    observation_end_time: Optional[int] = None,
    start_time: Optional[int] = None,
    type_: Optional[str] = None,
    viewers: Optional[str] = None,
) -> str:
    """POST /ad_studies on User.

    Args:
        user_id: The ID of the User object.
        cells: Optional.
        client_business: Optional.
        confidence_level: Optional.
        cooldown_start_time: Optional.
        description: Optional.
        end_time: Optional.
        name: Optional.
        objectives: Optional.
        observation_end_time: Optional.
        start_time: Optional.
        type_: Optional. Values: BACKEND_AB_TESTING, CONTINUOUS_LIFT_CONFIG, CREATIVE_SPEND_ENFORCEMENT, GEO_LIFT, LIFT, SPLIT_TEST
        viewers: Optional.
    """
    params = {}
    if cells is not None:
        params["cells"] = cells
    if client_business is not None:
        params["client_business"] = client_business
    if confidence_level is not None:
        params["confidence_level"] = confidence_level
    if cooldown_start_time is not None:
        params["cooldown_start_time"] = cooldown_start_time
    if description is not None:
        params["description"] = description
    if end_time is not None:
        params["end_time"] = end_time
    if name is not None:
        params["name"] = name
    if objectives is not None:
        params["objectives"] = objectives
    if observation_end_time is not None:
        params["observation_end_time"] = observation_end_time
    if start_time is not None:
        params["start_time"] = start_time
    if type_ is not None:
        params["type"] = type_
    if viewers is not None:
        params["viewers"] = viewers
    result = await get_client().post(f"{user_id}/ad_studies", data=params)
    return json.dumps(result, indent=2)


async def get_user_adaccounts(user_id: str, fields: Optional[str] = None) -> str:
    """GET /adaccounts on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_user_albums(user_id: str, fields: Optional[str] = None) -> str:
    """GET /albums on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/albums", params=params)
    return json.dumps(result, indent=2)


async def create_user_applications(user_id: str, business_app: int) -> str:
    """POST /applications on User.

    Args:
        user_id: The ID of the User object.
        business_app: Required.
    """
    params = {}
    params["business_app"] = business_app
    result = await get_client().post(f"{user_id}/applications", data=params)
    return json.dumps(result, indent=2)


async def get_user_apprequestformerrecipients(user_id: str, fields: Optional[str] = None) -> str:
    """GET /apprequestformerrecipients on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/apprequestformerrecipients", params=params)
    return json.dumps(result, indent=2)


async def get_user_apprequests(user_id: str, fields: Optional[str] = None) -> str:
    """GET /apprequests on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/apprequests", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_ad_accounts(user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_ad_accounts on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/assigned_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_applications(user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_applications on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/assigned_applications", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_business_asset_groups(
    user_id: str,
    fields: Optional[str] = None,
    contained_asset_id: Optional[str] = None,
) -> str:
    """GET /assigned_business_asset_groups on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        contained_asset_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if contained_asset_id is not None:
        params["contained_asset_id"] = contained_asset_id
    result = await get_client().get(f"{user_id}/assigned_business_asset_groups", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_pages(user_id: str, fields: Optional[str] = None, pages: Optional[str] = None) -> str:
    """GET /assigned_pages on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        pages: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if pages is not None:
        params["pages"] = pages
    result = await get_client().get(f"{user_id}/assigned_pages", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_product_catalogs(user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_product_catalogs on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/assigned_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_user_assigned_whatsapp_business_accounts(user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_whatsapp_business_accounts on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/assigned_whatsapp_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_user_business_users(user_id: str, fields: Optional[str] = None) -> str:
    """GET /business_users on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/business_users", params=params)
    return json.dumps(result, indent=2)


async def delete_user_businesses(user_id: str, business: Optional[str] = None) -> str:
    """DELETE /businesses on User.

    Args:
        user_id: The ID of the User object.
        business: Optional.
    """
    params = {}
    if business is not None:
        params["business"] = business
    result = await get_client().delete(f"{user_id}/businesses")
    return json.dumps(result, indent=2)


async def get_user_businesses(user_id: str, fields: Optional[str] = None) -> str:
    """GET /businesses on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/businesses", params=params)
    return json.dumps(result, indent=2)


async def create_user_businesses(
    user_id: str,
    name: str,
    vertical: str,
    child_business_external_id: Optional[str] = None,
    email: Optional[str] = None,
    primary_page: Optional[str] = None,
    sales_rep_email: Optional[str] = None,
    survey_business_type: Optional[str] = None,
    survey_num_assets: Optional[int] = None,
    survey_num_people: Optional[int] = None,
    timezone_id: Optional[str] = None,
) -> str:
    """POST /businesses on User.

    Args:
        user_id: The ID of the User object.
        child_business_external_id: Optional.
        email: Optional.
        name: Required.
        primary_page: Optional.
        sales_rep_email: Optional.
        survey_business_type: Optional. Values: ADVERTISER, AGENCY, APP_DEVELOPER, PUBLISHER
        survey_num_assets: Optional.
        survey_num_people: Optional.
        timezone_id: Optional. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480
        vertical: Required. Values: ADVERTISING, AUTOMOTIVE, CONSUMER_PACKAGED_GOODS, ECOMMERCE, EDUCATION, ENERGY_AND_UTILITIES, ENTERTAINMENT_AND_MEDIA, FINANCIAL_SERVICES, GAMING, GOVERNMENT_AND_POLITICS, HEALTH, LUXURY, MARKETING, NON_PROFIT, NOT_SET, ORGANIZATIONS_AND_ASSOCIATIONS, OTHER, PROFESSIONAL_SERVICES, RESTAURANT, RETAIL, TECHNOLOGY, TELECOM, TRAVEL
    """
    params = {}
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    if email is not None:
        params["email"] = email
    params["name"] = name
    if primary_page is not None:
        params["primary_page"] = primary_page
    if sales_rep_email is not None:
        params["sales_rep_email"] = sales_rep_email
    if survey_business_type is not None:
        params["survey_business_type"] = survey_business_type
    if survey_num_assets is not None:
        params["survey_num_assets"] = survey_num_assets
    if survey_num_people is not None:
        params["survey_num_people"] = survey_num_people
    if timezone_id is not None:
        params["timezone_id"] = timezone_id
    params["vertical"] = vertical
    result = await get_client().post(f"{user_id}/businesses", data=params)
    return json.dumps(result, indent=2)


async def get_user_conversations(
    user_id: str,
    fields: Optional[str] = None,
    folder: Optional[str] = None,
    platform: Optional[str] = None,
    tags: Optional[str] = None,
) -> str:
    """GET /conversations on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        folder: Optional.
        platform: Optional. Values: INSTAGRAM, MESSENGER
        tags: Optional.
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
    result = await get_client().get(f"{user_id}/conversations", params=params)
    return json.dumps(result, indent=2)


async def get_user_custom_labels(user_id: str, fields: Optional[str] = None) -> str:
    """GET /custom_labels on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/custom_labels", params=params)
    return json.dumps(result, indent=2)


async def get_user_events(
    user_id: str,
    fields: Optional[str] = None,
    include_canceled: Optional[bool] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /events on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        include_canceled: Optional.
        type_: Optional. Values: attending, created, declined, maybe, not_replied
    """
    params = {}
    params["fields"] = fields or "id,name"
    if include_canceled is not None:
        params["include_canceled"] = include_canceled
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{user_id}/events", params=params)
    return json.dumps(result, indent=2)


async def get_user_feed(
    user_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    q: Optional[str] = None,
    show_expired: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /feed on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().get(f"{user_id}/feed", params=params)
    return json.dumps(result, indent=2)


async def create_user_feed(
    user_id: str,
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
    """POST /feed on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().post(f"{user_id}/feed", data=params)
    return json.dumps(result, indent=2)


async def get_user_friends(user_id: str, fields: Optional[str] = None, uid: Optional[int] = None) -> str:
    """GET /friends on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        uid: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if uid is not None:
        params["uid"] = uid
    result = await get_client().get(f"{user_id}/friends", params=params)
    return json.dumps(result, indent=2)


async def get_user_fundraisers(user_id: str, fields: Optional[str] = None) -> str:
    """GET /fundraisers on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/fundraisers", params=params)
    return json.dumps(result, indent=2)


async def create_user_fundraisers(
    user_id: str,
    currency: str,
    description: str,
    end_time: str,
    external_id: str,
    fundraiser_type: str,
    goal_amount: int,
    name: str,
    charity_id: Optional[str] = None,
    cover_photo: Optional[str] = None,
    external_event_name: Optional[str] = None,
    external_event_start_time: Optional[str] = None,
    external_event_uri: Optional[str] = None,
    external_fundraiser_uri: Optional[str] = None,
    page_id: Optional[str] = None,
) -> str:
    """POST /fundraisers on User.

    Args:
        user_id: The ID of the User object.
        charity_id: Optional.
        cover_photo: Optional.
        currency: Required.
        description: Required.
        end_time: Required.
        external_event_name: Optional.
        external_event_start_time: Optional.
        external_event_uri: Optional.
        external_fundraiser_uri: Optional.
        external_id: Required.
        fundraiser_type: Required. Values: person_for_charity
        goal_amount: Required.
        name: Required.
        page_id: Optional.
    """
    params = {}
    if charity_id is not None:
        params["charity_id"] = charity_id
    if cover_photo is not None:
        params["cover_photo"] = cover_photo
    params["currency"] = currency
    params["description"] = description
    params["end_time"] = end_time
    if external_event_name is not None:
        params["external_event_name"] = external_event_name
    if external_event_start_time is not None:
        params["external_event_start_time"] = external_event_start_time
    if external_event_uri is not None:
        params["external_event_uri"] = external_event_uri
    if external_fundraiser_uri is not None:
        params["external_fundraiser_uri"] = external_fundraiser_uri
    params["external_id"] = external_id
    params["fundraiser_type"] = fundraiser_type
    params["goal_amount"] = goal_amount
    params["name"] = name
    if page_id is not None:
        params["page_id"] = page_id
    result = await get_client().post(f"{user_id}/fundraisers", data=params)
    return json.dumps(result, indent=2)


async def get_user_groups(
    user_id: str,
    fields: Optional[str] = None,
    admin_only: Optional[bool] = None,
    parent: Optional[str] = None,
) -> str:
    """GET /groups on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        admin_only: Optional.
        parent: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if admin_only is not None:
        params["admin_only"] = admin_only
    if parent is not None:
        params["parent"] = parent
    result = await get_client().get(f"{user_id}/groups", params=params)
    return json.dumps(result, indent=2)


async def get_user_ids_for_apps(user_id: str, fields: Optional[str] = None, app: Optional[int] = None) -> str:
    """GET /ids_for_apps on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        app: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app is not None:
        params["app"] = app
    result = await get_client().get(f"{user_id}/ids_for_apps", params=params)
    return json.dumps(result, indent=2)


async def get_user_ids_for_business(user_id: str, fields: Optional[str] = None, app: Optional[int] = None) -> str:
    """GET /ids_for_business on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        app: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app is not None:
        params["app"] = app
    result = await get_client().get(f"{user_id}/ids_for_business", params=params)
    return json.dumps(result, indent=2)


async def get_user_ids_for_pages(user_id: str, fields: Optional[str] = None, page: Optional[int] = None) -> str:
    """GET /ids_for_pages on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        page: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if page is not None:
        params["page"] = page
    result = await get_client().get(f"{user_id}/ids_for_pages", params=params)
    return json.dumps(result, indent=2)


async def get_user_likes(user_id: str, fields: Optional[str] = None, target_id: Optional[str] = None) -> str:
    """GET /likes on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        target_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if target_id is not None:
        params["target_id"] = target_id
    result = await get_client().get(f"{user_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def get_user_live_videos(
    user_id: str,
    fields: Optional[str] = None,
    broadcast_status: Optional[str] = None,
    source: Optional[str] = None,
) -> str:
    """GET /live_videos on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().get(f"{user_id}/live_videos", params=params)
    return json.dumps(result, indent=2)


async def create_user_live_videos(
    user_id: str,
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
    """POST /live_videos on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().post(f"{user_id}/live_videos", data=params)
    return json.dumps(result, indent=2)


async def create_user_messenger_desktop_performance_traces(user_id: str) -> str:
    """POST /messenger_desktop_performance_traces on User.

    Args:
        user_id: The ID of the User object.
    """
    params = {}
    result = await get_client().post(f"{user_id}/messenger_desktop_performance_traces", data=params)
    return json.dumps(result, indent=2)


async def create_user_messenger_kids_accounts_unread_badge(user_id: str, proxied_app_id: int) -> str:
    """POST /messenger_kids_accounts_unread_badge on User.

    Args:
        user_id: The ID of the User object.
        proxied_app_id: Required.
    """
    params = {}
    params["proxied_app_id"] = proxied_app_id
    result = await get_client().post(f"{user_id}/messenger_kids_accounts_unread_badge", data=params)
    return json.dumps(result, indent=2)


async def get_user_music(user_id: str, fields: Optional[str] = None, target_id: Optional[str] = None) -> str:
    """GET /music on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        target_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if target_id is not None:
        params["target_id"] = target_id
    result = await get_client().get(f"{user_id}/music", params=params)
    return json.dumps(result, indent=2)


async def create_user_notifications(
    user_id: str,
    bot_message_payload_elements: Optional[str] = None,
    filtering: Optional[str] = None,
    href: Optional[str] = None,
    label: Optional[str] = None,
    message: Optional[str] = None,
    notif_ids: Optional[str] = None,
    payload: Optional[str] = None,
    read: Optional[bool] = None,
    ref: Optional[str] = None,
    schedule_interval: Optional[int] = None,
    seen: Optional[bool] = None,
    template: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """POST /notifications on User.

    Args:
        user_id: The ID of the User object.
        bot_message_payload_elements: Optional.
        filtering: Optional. Values: ema, groups, groups_social
        href: Optional.
        label: Optional.
        message: Optional.
        notif_ids: Optional.
        payload: Optional.
        read: Optional.
        ref: Optional.
        schedule_interval: Optional.
        seen: Optional.
        template: Optional.
        type_: Optional. Values: content_update, generic
    """
    params = {}
    if bot_message_payload_elements is not None:
        params["bot_message_payload_elements"] = bot_message_payload_elements
    if filtering is not None:
        params["filtering"] = filtering
    if href is not None:
        params["href"] = href
    if label is not None:
        params["label"] = label
    if message is not None:
        params["message"] = message
    if notif_ids is not None:
        params["notif_ids"] = notif_ids
    if payload is not None:
        params["payload"] = payload
    if read is not None:
        params["read"] = read
    if ref is not None:
        params["ref"] = ref
    if schedule_interval is not None:
        params["schedule_interval"] = schedule_interval
    if seen is not None:
        params["seen"] = seen
    if template is not None:
        params["template"] = template
    if type_ is not None:
        params["type"] = type_
    result = await get_client().post(f"{user_id}/notifications", data=params)
    return json.dumps(result, indent=2)


async def get_user_payment_transactions(user_id: str, fields: Optional[str] = None) -> str:
    """GET /payment_transactions on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/payment_transactions", params=params)
    return json.dumps(result, indent=2)


async def delete_user_permissions(user_id: str, permission: Optional[str] = None) -> str:
    """DELETE /permissions on User.

    Args:
        user_id: The ID of the User object.
        permission: Optional.
    """
    params = {}
    if permission is not None:
        params["permission"] = permission
    result = await get_client().delete(f"{user_id}/permissions")
    return json.dumps(result, indent=2)


async def get_user_permissions(
    user_id: str,
    fields: Optional[str] = None,
    permission: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """GET /permissions on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        permission: Optional.
        status: Optional. Values: declined, expired, granted
    """
    params = {}
    params["fields"] = fields or "id,name"
    if permission is not None:
        params["permission"] = permission
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{user_id}/permissions", params=params)
    return json.dumps(result, indent=2)


async def get_user_personal_ad_accounts(user_id: str, fields: Optional[str] = None) -> str:
    """GET /personal_ad_accounts on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}/personal_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_user_photos(user_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /photos on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: tagged, uploaded
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{user_id}/photos", params=params)
    return json.dumps(result, indent=2)


async def create_user_photos(
    user_id: str,
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
    scheduled_publish_time: Optional[int] = None,
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
    """POST /photos on User.

    Args:
        user_id: The ID of the User object.
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
        scheduled_publish_time: Optional.
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
    result = await get_client().post(f"{user_id}/photos", data=params)
    return json.dumps(result, indent=2)


async def get_user_picture(
    user_id: str,
    fields: Optional[str] = None,
    height: Optional[int] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /picture on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().get(f"{user_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def get_user_posts(
    user_id: str,
    fields: Optional[str] = None,
    include_hidden: Optional[bool] = None,
    q: Optional[str] = None,
    show_expired: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    with_: Optional[str] = None,
) -> str:
    """GET /posts on User.

    Args:
        user_id: The ID of the User object.
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
    result = await get_client().get(f"{user_id}/posts", params=params)
    return json.dumps(result, indent=2)


async def get_user_rich_media_documents(user_id: str, fields: Optional[str] = None, query: Optional[str] = None) -> str:
    """GET /rich_media_documents on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        query: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if query is not None:
        params["query"] = query
    result = await get_client().get(f"{user_id}/rich_media_documents", params=params)
    return json.dumps(result, indent=2)


async def create_user_staging_resources(user_id: str, file: Optional[str] = None) -> str:
    """POST /staging_resources on User.

    Args:
        user_id: The ID of the User object.
        file: Optional.
    """
    params = {}
    if file is not None:
        params["file"] = file
    result = await get_client().post(f"{user_id}/staging_resources", data=params)
    return json.dumps(result, indent=2)


async def get_user_videos(user_id: str, fields: Optional[str] = None, type_: Optional[str] = None) -> str:
    """GET /videos on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return.
        type_: Optional. Values: TAGGED, UPLOADED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{user_id}/videos", params=params)
    return json.dumps(result, indent=2)


async def create_user_videos(
    user_id: str,
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
    direct_share_status: Optional[int] = None,
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
    no_story: Optional[bool] = None,
    og_action_type_id: Optional[str] = None,
    og_icon_id: Optional[str] = None,
    og_object_id: Optional[str] = None,
    og_phrase: Optional[str] = None,
    og_suggestion_mechanism: Optional[str] = None,
    original_fov: Optional[int] = None,
    original_projection_type: Optional[str] = None,
    partnership_ad_ad_code: Optional[str] = None,
    privacy: Optional[str] = None,
    publish_event_id: Optional[int] = None,
    referenced_sticker_id: Optional[str] = None,
    replace_video_id: Optional[str] = None,
    slideshow_spec: Optional[str] = None,
    source: Optional[str] = None,
    source_instagram_media_id: Optional[str] = None,
    spherical: Optional[bool] = None,
    sponsor_id: Optional[str] = None,
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
    """POST /videos on User.

    Args:
        user_id: The ID of the User object.
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
        direct_share_status: Optional.
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
        no_story: Optional.
        og_action_type_id: Optional.
        og_icon_id: Optional.
        og_object_id: Optional.
        og_phrase: Optional.
        og_suggestion_mechanism: Optional.
        original_fov: Optional.
        original_projection_type: Optional. Values: cubemap, equirectangular, half_equirectangular
        partnership_ad_ad_code: Optional.
        privacy: Optional.
        publish_event_id: Optional.
        referenced_sticker_id: Optional.
        replace_video_id: Optional.
        slideshow_spec: Optional.
        source: Optional.
        source_instagram_media_id: Optional.
        spherical: Optional.
        sponsor_id: Optional.
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
    if direct_share_status is not None:
        params["direct_share_status"] = direct_share_status
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
    if privacy is not None:
        params["privacy"] = privacy
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
    if sponsor_id is not None:
        params["sponsor_id"] = sponsor_id
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
    result = await get_client().post(f"{user_id}/videos", data=params)
    return json.dumps(result, indent=2)


async def delete_user(user_id: str) -> str:
    """DELETE /#delete on User.

    Args:
        user_id: The ID of the User object.
    """
    params = {}
    result = await get_client().delete(f"{user_id}")
    return json.dumps(result, indent=2)


async def get_user(user_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on User.

    Args:
        user_id: The ID of the User object.
        fields: Comma-separated list of fields to return. Available: about, age_range, birthday, client_business_id, community, cover, currency, education, email, favorite_athletes, favorite_teams, first_name, gender, hometown, id, inspirational_people, install_type, installed, is_guest_user, is_work_account, languages, last_name, link, local_news_megaphone_dismiss_status, local_news_subscription_status, locale, location, meeting_for, middle_name, name, name_format, payment_pricepoints, political, profile_pic, quotes, relationship_status, religion, shared_login_upgrade_required_by, short_name, significant_other, sports, supports_donate_button_in_live_video, third_party_id, timezone, token_for_business, updated_time, verified, video_upload_limits, website
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{user_id}", params=params)
    return json.dumps(result, indent=2)


async def update_user(
    user_id: str,
    emoji_color_pref: Optional[int] = None,
    firstname: Optional[str] = None,
    lastname: Optional[str] = None,
    local_news_megaphone_dismiss_status: Optional[str] = None,
    local_news_subscription_status: Optional[str] = None,
    name: Optional[str] = None,
    password: Optional[str] = None,
) -> str:
    """POST /#update on User.

    Args:
        user_id: The ID of the User object.
        emoji_color_pref: Optional.
        firstname: Optional.
        lastname: Optional.
        local_news_megaphone_dismiss_status: Optional.
        local_news_subscription_status: Optional.
        name: Optional.
        password: Optional.
    """
    params = {}
    if emoji_color_pref is not None:
        params["emoji_color_pref"] = emoji_color_pref
    if firstname is not None:
        params["firstname"] = firstname
    if lastname is not None:
        params["lastname"] = lastname
    if local_news_megaphone_dismiss_status is not None:
        params["local_news_megaphone_dismiss_status"] = local_news_megaphone_dismiss_status
    if local_news_subscription_status is not None:
        params["local_news_subscription_status"] = local_news_subscription_status
    if name is not None:
        params["name"] = name
    if password is not None:
        params["password"] = password
    result = await get_client().post(f"{user_id}", data=params)
    return json.dumps(result, indent=2)


PROFILE_FIELDS = [
    "can_post",
    "id",
    "link",
    "name",
    "pic",
    "pic_crop",
    "pic_large",
    "pic_small",
    "pic_square",
    "profile_type",
    "username"
]


async def get_profile_picture(
    profile_id: str,
    fields: Optional[str] = None,
    height: Optional[int] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /picture on Profile.

    Args:
        profile_id: The ID of the Profile object.
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
    result = await get_client().get(f"{profile_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def get_profile(profile_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Profile.

    Args:
        profile_id: The ID of the Profile object.
        fields: Comma-separated list of fields to return. Available: can_post, id, link, name, pic, pic_crop, pic_large, pic_small, pic_square, profile_type, username
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{profile_id}", params=params)
    return json.dumps(result, indent=2)


LIFE_EVENT_FIELDS = [
    "description",
    "end_time",
    "from",
    "id",
    "is_hidden",
    "start_time",
    "title",
    "updated_time"
]


async def get_life_event_likes(life_event_id: str, fields: Optional[str] = None) -> str:
    """GET /likes on LifeEvent.

    Args:
        life_event_id: The ID of the LifeEvent object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{life_event_id}/likes", params=params)
    return json.dumps(result, indent=2)


async def get_life_event(life_event_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on LifeEvent.

    Args:
        life_event_id: The ID of the LifeEvent object.
        fields: Comma-separated list of fields to return. Available: description, end_time, from, id, is_hidden, start_time, title, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{life_event_id}", params=params)
    return json.dumps(result, indent=2)


WORK_SKILL_FIELDS = [
    "id",
    "name"
]


async def get_work_skill_users(work_skill_id: str, fields: Optional[str] = None) -> str:
    """GET /users on WorkSkill.

    Args:
        work_skill_id: The ID of the WorkSkill object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{work_skill_id}/users", params=params)
    return json.dumps(result, indent=2)


async def get_work_skill(work_skill_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on WorkSkill.

    Args:
        work_skill_id: The ID of the WorkSkill object.
        fields: Comma-separated list of fields to return. Available: id, name
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{work_skill_id}", params=params)
    return json.dumps(result, indent=2)

