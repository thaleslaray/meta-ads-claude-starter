"""Auto-generated Meta Marketing API tools — instagram."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


IG_USER_FIELDS = [
    "biography",
    "business_discovery",
    "followers_count",
    "follows_count",
    "has_profile_pic",
    "id",
    "ig_id",
    "is_published",
    "legacy_instagram_user_id",
    "media_count",
    "mentioned_comment",
    "mentioned_media",
    "name",
    "owner_business",
    "profile_picture_url",
    "shopping_product_tag_eligibility",
    "shopping_review_status",
    "username",
    "website"
]


async def get_ig_user_agencies(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_authorized_adaccounts(ig_user_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /authorized_adaccounts on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{ig_user_id}/authorized_adaccounts", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_authorized_adaccounts(ig_user_id: str, account_id: str, business: str) -> str:
    """POST /authorized_adaccounts on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        account_id: Required.
        business: Required.
    """
    params = {}
    params["account_id"] = account_id
    params["business"] = business
    result = await get_client().post(f"{ig_user_id}/authorized_adaccounts", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_available_catalogs(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /available_catalogs on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/available_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_branded_content_ad_permissions(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /branded_content_ad_permissions on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/branded_content_ad_permissions", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_branded_content_ad_permissions(
    ig_user_id: str,
    creator_instagram_account: Optional[str] = None,
    creator_instagram_username: Optional[str] = None,
    revoke: Optional[bool] = None,
) -> str:
    """POST /branded_content_ad_permissions on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        creator_instagram_account: Optional.
        creator_instagram_username: Optional.
        revoke: Optional.
    """
    params = {}
    if creator_instagram_account is not None:
        params["creator_instagram_account"] = creator_instagram_account
    if creator_instagram_username is not None:
        params["creator_instagram_username"] = creator_instagram_username
    if revoke is not None:
        params["revoke"] = revoke
    result = await get_client().post(f"{ig_user_id}/branded_content_ad_permissions", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_branded_content_advertisable_medias(
    ig_user_id: str,
    fields: Optional[str] = None,
    ad_code: Optional[str] = None,
    creator_username: Optional[str] = None,
    media_relationship: Optional[str] = None,
    only_fetch_allowlisted: Optional[bool] = None,
    only_fetch_recommended_content: Optional[bool] = None,
    permalinks: Optional[str] = None,
) -> str:
    """GET /branded_content_advertisable_medias on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        ad_code: Optional.
        creator_username: Optional.
        media_relationship: Optional. Values: IS_TAGGED, OWNED
        only_fetch_allowlisted: Optional.
        only_fetch_recommended_content: Optional.
        permalinks: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_code is not None:
        params["ad_code"] = ad_code
    if creator_username is not None:
        params["creator_username"] = creator_username
    if media_relationship is not None:
        params["media_relationship"] = media_relationship
    if only_fetch_allowlisted is not None:
        params["only_fetch_allowlisted"] = only_fetch_allowlisted
    if only_fetch_recommended_content is not None:
        params["only_fetch_recommended_content"] = only_fetch_recommended_content
    if permalinks is not None:
        params["permalinks"] = permalinks
    result = await get_client().get(f"{ig_user_id}/branded_content_advertisable_medias", params=params)
    return json.dumps(result, indent=2)


async def delete_ig_user_branded_content_tag_approval(ig_user_id: str, user_ids: str) -> str:
    """DELETE /branded_content_tag_approval on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        user_ids: Required.
    """
    params = {}
    params["user_ids"] = user_ids
    result = await get_client().delete(f"{ig_user_id}/branded_content_tag_approval")
    return json.dumps(result, indent=2)


async def get_ig_user_branded_content_tag_approval(ig_user_id: str, user_ids: str, fields: Optional[str] = None) -> str:
    """GET /branded_content_tag_approval on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        user_ids: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["user_ids"] = user_ids
    result = await get_client().get(f"{ig_user_id}/branded_content_tag_approval", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_branded_content_tag_approval(ig_user_id: str, user_ids: str) -> str:
    """POST /branded_content_tag_approval on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        user_ids: Required.
    """
    params = {}
    params["user_ids"] = user_ids
    result = await get_client().post(f"{ig_user_id}/branded_content_tag_approval", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_catalog_product_search(
    ig_user_id: str,
    catalog_id: str,
    fields: Optional[str] = None,
    q: Optional[str] = None,
) -> str:
    """GET /catalog_product_search on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        catalog_id: Required.
        q: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["catalog_id"] = catalog_id
    if q is not None:
        params["q"] = q
    result = await get_client().get(f"{ig_user_id}/catalog_product_search", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_collaboration_invites(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /collaboration_invites on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/collaboration_invites", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_collaboration_invites(ig_user_id: str, accept: bool, media_id: str) -> str:
    """POST /collaboration_invites on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        accept: Required.
        media_id: Required.
    """
    params = {}
    params["accept"] = accept
    params["media_id"] = media_id
    result = await get_client().post(f"{ig_user_id}/collaboration_invites", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_connected_threads_user(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /connected_threads_user on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/connected_threads_user", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_content_publishing_limit(ig_user_id: str, fields: Optional[str] = None, since: Optional[str] = None) -> str:
    """GET /content_publishing_limit on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        since: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if since is not None:
        params["since"] = since
    result = await get_client().get(f"{ig_user_id}/content_publishing_limit", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_creator_marketplace_creators(
    ig_user_id: str,
    fields: Optional[str] = None,
    creator_age_bucket: Optional[str] = None,
    creator_countries: Optional[str] = None,
    creator_gender: Optional[str] = None,
    creator_interests: Optional[str] = None,
    creator_max_engaged_accounts: Optional[int] = None,
    creator_max_followers: Optional[int] = None,
    creator_min_engaged_accounts: Optional[int] = None,
    creator_min_followers: Optional[int] = None,
    has_public_contact_email: Optional[bool] = None,
    major_audience_age_bucket: Optional[str] = None,
    major_audience_countries: Optional[str] = None,
    major_audience_gender: Optional[str] = None,
    query: Optional[str] = None,
    reels_interaction_rate: Optional[str] = None,
    show_onboarded_creators_only: Optional[bool] = None,
    similar_to_creators: Optional[str] = None,
    username: Optional[str] = None,
) -> str:
    """GET /creator_marketplace_creators on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        creator_age_bucket: Optional.
        creator_countries: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        creator_gender: Optional. Values: custom, female, male, unknown
        creator_interests: Optional.
        creator_max_engaged_accounts: Optional.
        creator_max_followers: Optional.
        creator_min_engaged_accounts: Optional.
        creator_min_followers: Optional.
        has_public_contact_email: Optional.
        major_audience_age_bucket: Optional.
        major_audience_countries: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        major_audience_gender: Optional. Values: custom, female, male, unknown
        query: Optional.
        reels_interaction_rate: Optional.
        show_onboarded_creators_only: Optional.
        similar_to_creators: Optional.
        username: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if creator_age_bucket is not None:
        params["creator_age_bucket"] = creator_age_bucket
    if creator_countries is not None:
        params["creator_countries"] = creator_countries
    if creator_gender is not None:
        params["creator_gender"] = creator_gender
    if creator_interests is not None:
        params["creator_interests"] = creator_interests
    if creator_max_engaged_accounts is not None:
        params["creator_max_engaged_accounts"] = creator_max_engaged_accounts
    if creator_max_followers is not None:
        params["creator_max_followers"] = creator_max_followers
    if creator_min_engaged_accounts is not None:
        params["creator_min_engaged_accounts"] = creator_min_engaged_accounts
    if creator_min_followers is not None:
        params["creator_min_followers"] = creator_min_followers
    if has_public_contact_email is not None:
        params["has_public_contact_email"] = has_public_contact_email
    if major_audience_age_bucket is not None:
        params["major_audience_age_bucket"] = major_audience_age_bucket
    if major_audience_countries is not None:
        params["major_audience_countries"] = major_audience_countries
    if major_audience_gender is not None:
        params["major_audience_gender"] = major_audience_gender
    if query is not None:
        params["query"] = query
    if reels_interaction_rate is not None:
        params["reels_interaction_rate"] = reels_interaction_rate
    if show_onboarded_creators_only is not None:
        params["show_onboarded_creators_only"] = show_onboarded_creators_only
    if similar_to_creators is not None:
        params["similar_to_creators"] = similar_to_creators
    if username is not None:
        params["username"] = username
    result = await get_client().get(f"{ig_user_id}/creator_marketplace_creators", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_dataset(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /dataset on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/dataset", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_dataset(ig_user_id: str, dataset_name: Optional[str] = None) -> str:
    """POST /dataset on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        dataset_name: Optional.
    """
    params = {}
    if dataset_name is not None:
        params["dataset_name"] = dataset_name
    result = await get_client().post(f"{ig_user_id}/dataset", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_insights(
    ig_user_id: str,
    metric: str,
    period: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    metric_type: Optional[str] = None,
    since: Optional[str] = None,
    timeframe: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /insights on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
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
    result = await get_client().get(f"{ig_user_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_instagram_backed_threads_user(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_backed_threads_user on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/instagram_backed_threads_user", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_instagram_backed_threads_user(ig_user_id: str) -> str:
    """POST /instagram_backed_threads_user on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
    """
    params = {}
    result = await get_client().post(f"{ig_user_id}/instagram_backed_threads_user", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_live_media(
    ig_user_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /live_media on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
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
    result = await get_client().get(f"{ig_user_id}/live_media", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_media(
    ig_user_id: str,
    fields: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /media on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
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
    result = await get_client().get(f"{ig_user_id}/media", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_media(
    ig_user_id: str,
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
    """POST /media on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
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
    result = await get_client().post(f"{ig_user_id}/media", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_media_publish(ig_user_id: str, creation_id: int) -> str:
    """POST /media_publish on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        creation_id: Required.
    """
    params = {}
    params["creation_id"] = creation_id
    result = await get_client().post(f"{ig_user_id}/media_publish", data=params)
    return json.dumps(result, indent=2)


async def create_ig_user_mentions(ig_user_id: str, media_id: str, message: str, comment_id: Optional[str] = None) -> str:
    """POST /mentions on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        comment_id: Optional.
        media_id: Required.
        message: Required.
    """
    params = {}
    if comment_id is not None:
        params["comment_id"] = comment_id
    params["media_id"] = media_id
    params["message"] = message
    result = await get_client().post(f"{ig_user_id}/mentions", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_notification_message_tokens(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /notification_message_tokens on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/notification_message_tokens", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_product_appeal(ig_user_id: str, product_id: str, fields: Optional[str] = None) -> str:
    """GET /product_appeal on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
        product_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["product_id"] = product_id
    result = await get_client().get(f"{ig_user_id}/product_appeal", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_product_appeal(ig_user_id: str, appeal_reason: str, product_id: str) -> str:
    """POST /product_appeal on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        appeal_reason: Required.
        product_id: Required.
    """
    params = {}
    params["appeal_reason"] = appeal_reason
    params["product_id"] = product_id
    result = await get_client().post(f"{ig_user_id}/product_appeal", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_recently_searched_hashtags(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /recently_searched_hashtags on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/recently_searched_hashtags", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_scheduled_media(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /scheduled_media on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/scheduled_media", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_stories(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /stories on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/stories", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_tags(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /tags on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/tags", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user_upcoming_events(ig_user_id: str, fields: Optional[str] = None) -> str:
    """GET /upcoming_events on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_user_id}/upcoming_events", params=params)
    return json.dumps(result, indent=2)


async def create_ig_user_upcoming_events(
    ig_user_id: str,
    start_time: str,
    title: str,
    end_time: Optional[str] = None,
    notification_subtypes: Optional[str] = None,
) -> str:
    """POST /upcoming_events on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        end_time: Optional.
        notification_subtypes: Optional. Values: AFTER_EVENT_1DAY, AFTER_EVENT_2DAY, AFTER_EVENT_3DAY, AFTER_EVENT_4DAY, AFTER_EVENT_5DAY, AFTER_EVENT_6DAY, AFTER_EVENT_7DAY, BEFORE_EVENT_15MIN, BEFORE_EVENT_1DAY, BEFORE_EVENT_1HOUR, BEFORE_EVENT_2DAY, EVENT_START, RESCHEDULED
        start_time: Required.
        title: Required.
    """
    params = {}
    if end_time is not None:
        params["end_time"] = end_time
    if notification_subtypes is not None:
        params["notification_subtypes"] = notification_subtypes
    params["start_time"] = start_time
    params["title"] = title
    result = await get_client().post(f"{ig_user_id}/upcoming_events", data=params)
    return json.dumps(result, indent=2)


async def get_ig_user_welcome_message_flows(
    ig_user_id: str,
    fields: Optional[str] = None,
    app_id: Optional[str] = None,
    flow_id: Optional[str] = None,
) -> str:
    """GET /welcome_message_flows on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
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
    result = await get_client().get(f"{ig_user_id}/welcome_message_flows", params=params)
    return json.dumps(result, indent=2)


async def get_ig_user(ig_user_id: str, fields: Optional[str] = None, adgroup_id: Optional[str] = None) -> str:
    """GET /#get on IGUser.

    Args:
        ig_user_id: The ID of the IGUser object.
        fields: Comma-separated list of fields to return. Available: biography, business_discovery, followers_count, follows_count, has_profile_pic, id, ig_id, is_published, legacy_instagram_user_id, media_count, mentioned_comment, mentioned_media, name, owner_business, profile_picture_url, shopping_product_tag_eligibility, shopping_review_status, username, website
        adgroup_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if adgroup_id is not None:
        params["adgroup_id"] = adgroup_id
    result = await get_client().get(f"{ig_user_id}", params=params)
    return json.dumps(result, indent=2)


IG_MEDIA_FIELDS = [
    "alt_text",
    "boost_eligibility_info",
    "caption",
    "comments_count",
    "copyright_check_information",
    "has_poll",
    "has_slider",
    "id",
    "ig_id",
    "is_comment_enabled",
    "is_shared_to_feed",
    "legacy_instagram_media_id",
    "like_count",
    "media_product_type",
    "media_type",
    "media_url",
    "owner",
    "permalink",
    "shortcode",
    "thumbnail_url",
    "timestamp",
    "username",
    "video_title",
    "view_count"
]


async def get_ig_media_boost_ads_list(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /boost_ads_list on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/boost_ads_list", params=params)
    return json.dumps(result, indent=2)


async def get_ig_media_branded_content_partner_promote(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /branded_content_partner_promote on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/branded_content_partner_promote", params=params)
    return json.dumps(result, indent=2)


async def create_ig_media_branded_content_partner_promote(ig_media_id: str, permission: bool, sponsor_id: int) -> str:
    """POST /branded_content_partner_promote on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        permission: Required.
        sponsor_id: Required.
    """
    params = {}
    params["permission"] = permission
    params["sponsor_id"] = sponsor_id
    result = await get_client().post(f"{ig_media_id}/branded_content_partner_promote", data=params)
    return json.dumps(result, indent=2)


async def get_ig_media_children(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /children on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/children", params=params)
    return json.dumps(result, indent=2)


async def get_ig_media_collaborators(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /collaborators on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/collaborators", params=params)
    return json.dumps(result, indent=2)


async def get_ig_media_comments(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /comments on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/comments", params=params)
    return json.dumps(result, indent=2)


async def create_ig_media_comments(ig_media_id: str, ad_id: Optional[str] = None, message: Optional[str] = None) -> str:
    """POST /comments on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        ad_id: Optional.
        message: Optional.
    """
    params = {}
    if ad_id is not None:
        params["ad_id"] = ad_id
    if message is not None:
        params["message"] = message
    result = await get_client().post(f"{ig_media_id}/comments", data=params)
    return json.dumps(result, indent=2)


async def get_ig_media_insights(
    ig_media_id: str,
    metric: str,
    fields: Optional[str] = None,
    breakdown: Optional[str] = None,
    period: Optional[str] = None,
) -> str:
    """GET /insights on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
        breakdown: Optional. Values: action_type, follow_type, story_navigation_action_type, surface_type
        metric: Required. Values: clips_replays_count, comments, follows, ig_reels_aggregated_all_plays_count, ig_reels_avg_watch_time, ig_reels_video_view_total_time, impressions, likes, navigation, plays, profile_activity, profile_visits, reach, replies, saved, shares, total_interactions, video_views, views
        period: Optional. Values: day, days_28, lifetime, month, total_over_range, week
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdown is not None:
        params["breakdown"] = breakdown
    params["metric"] = metric
    if period is not None:
        params["period"] = period
    result = await get_client().get(f"{ig_media_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def delete_ig_media_partnership_ad_code(ig_media_id: str) -> str:
    """DELETE /partnership_ad_code on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
    """
    params = {}
    result = await get_client().delete(f"{ig_media_id}/partnership_ad_code")
    return json.dumps(result, indent=2)


async def create_ig_media_partnership_ad_code(ig_media_id: str) -> str:
    """POST /partnership_ad_code on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
    """
    params = {}
    result = await get_client().post(f"{ig_media_id}/partnership_ad_code", data=params)
    return json.dumps(result, indent=2)


async def get_ig_media_product_tags(ig_media_id: str, fields: Optional[str] = None) -> str:
    """GET /product_tags on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_media_id}/product_tags", params=params)
    return json.dumps(result, indent=2)


async def create_ig_media_product_tags(ig_media_id: str, updated_tags: str, child_index: Optional[int] = None) -> str:
    """POST /product_tags on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        child_index: Optional.
        updated_tags: Required.
    """
    params = {}
    if child_index is not None:
        params["child_index"] = child_index
    params["updated_tags"] = updated_tags
    result = await get_client().post(f"{ig_media_id}/product_tags", data=params)
    return json.dumps(result, indent=2)


async def delete_ig_media(ig_media_id: str) -> str:
    """DELETE /#delete on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
    """
    params = {}
    result = await get_client().delete(f"{ig_media_id}")
    return json.dumps(result, indent=2)


async def get_ig_media(
    ig_media_id: str,
    fields: Optional[str] = None,
    ad_account_id: Optional[int] = None,
    boostable_media_callsite: Optional[str] = None,
    business_id: Optional[str] = None,
    primary_fb_page_id: Optional[str] = None,
    primary_ig_user_id: Optional[str] = None,
    secondary_fb_page_id: Optional[str] = None,
    secondary_ig_user_id: Optional[str] = None,
) -> str:
    """GET /#get on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        fields: Comma-separated list of fields to return. Available: alt_text, boost_eligibility_info, caption, comments_count, copyright_check_information, has_poll, has_slider, id, ig_id, is_comment_enabled, is_shared_to_feed, legacy_instagram_media_id, like_count, media_product_type, media_type, media_url, owner, permalink, shortcode, thumbnail_url, timestamp, username, video_title, view_count
        ad_account_id: Optional.
        boostable_media_callsite: Optional.
        business_id: Optional.
        primary_fb_page_id: Optional.
        primary_ig_user_id: Optional.
        secondary_fb_page_id: Optional.
        secondary_ig_user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_account_id is not None:
        params["ad_account_id"] = ad_account_id
    if boostable_media_callsite is not None:
        params["boostable_media_callsite"] = boostable_media_callsite
    if business_id is not None:
        params["business_id"] = business_id
    if primary_fb_page_id is not None:
        params["primary_fb_page_id"] = primary_fb_page_id
    if primary_ig_user_id is not None:
        params["primary_ig_user_id"] = primary_ig_user_id
    if secondary_fb_page_id is not None:
        params["secondary_fb_page_id"] = secondary_fb_page_id
    if secondary_ig_user_id is not None:
        params["secondary_ig_user_id"] = secondary_ig_user_id
    result = await get_client().get(f"{ig_media_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ig_media(ig_media_id: str, comment_enabled: bool) -> str:
    """POST /#update on IGMedia.

    Args:
        ig_media_id: The ID of the IGMedia object.
        comment_enabled: Required.
    """
    params = {}
    params["comment_enabled"] = comment_enabled
    result = await get_client().post(f"{ig_media_id}", data=params)
    return json.dumps(result, indent=2)


IG_COMMENT_FIELDS = [
    "from",
    "hidden",
    "id",
    "legacy_instagram_comment_id",
    "like_count",
    "media",
    "parent_id",
    "text",
    "timestamp",
    "user",
    "username"
]


async def get_ig_comment_replies(ig_comment_id: str, fields: Optional[str] = None) -> str:
    """GET /replies on IGComment.

    Args:
        ig_comment_id: The ID of the IGComment object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_comment_id}/replies", params=params)
    return json.dumps(result, indent=2)


async def create_ig_comment_replies(ig_comment_id: str, message: Optional[str] = None) -> str:
    """POST /replies on IGComment.

    Args:
        ig_comment_id: The ID of the IGComment object.
        message: Optional.
    """
    params = {}
    if message is not None:
        params["message"] = message
    result = await get_client().post(f"{ig_comment_id}/replies", data=params)
    return json.dumps(result, indent=2)


async def delete_ig_comment(ig_comment_id: str, ad_id: Optional[str] = None) -> str:
    """DELETE /#delete on IGComment.

    Args:
        ig_comment_id: The ID of the IGComment object.
        ad_id: Optional.
    """
    params = {}
    if ad_id is not None:
        params["ad_id"] = ad_id
    result = await get_client().delete(f"{ig_comment_id}")
    return json.dumps(result, indent=2)


async def get_ig_comment(ig_comment_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on IGComment.

    Args:
        ig_comment_id: The ID of the IGComment object.
        fields: Comma-separated list of fields to return. Available: from, hidden, id, legacy_instagram_comment_id, like_count, media, parent_id, text, timestamp, user, username
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_comment_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ig_comment(ig_comment_id: str, hide: bool, ad_id: Optional[str] = None) -> str:
    """POST /#update on IGComment.

    Args:
        ig_comment_id: The ID of the IGComment object.
        ad_id: Optional.
        hide: Required.
    """
    params = {}
    if ad_id is not None:
        params["ad_id"] = ad_id
    params["hide"] = hide
    result = await get_client().post(f"{ig_comment_id}", data=params)
    return json.dumps(result, indent=2)


IG_UPCOMING_EVENT_FIELDS = [
    "end_time",
    "id",
    "notification_subtypes",
    "notification_target_time",
    "start_time",
    "title"
]


async def get_ig_upcoming_event(ig_upcoming_event_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on IGUpcomingEvent.

    Args:
        ig_upcoming_event_id: The ID of the IGUpcomingEvent object.
        fields: Comma-separated list of fields to return. Available: end_time, id, notification_subtypes, notification_target_time, start_time, title
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ig_upcoming_event_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ig_upcoming_event(
    ig_upcoming_event_id: str,
    start_time: str,
    title: str,
    end_time: Optional[str] = None,
    notification_subtypes: Optional[str] = None,
    notification_target_time: Optional[str] = None,
) -> str:
    """POST /#update on IGUpcomingEvent.

    Args:
        ig_upcoming_event_id: The ID of the IGUpcomingEvent object.
        end_time: Optional.
        notification_subtypes: Optional.
        notification_target_time: Optional.
        start_time: Required.
        title: Required.
    """
    params = {}
    if end_time is not None:
        params["end_time"] = end_time
    if notification_subtypes is not None:
        params["notification_subtypes"] = notification_subtypes
    if notification_target_time is not None:
        params["notification_target_time"] = notification_target_time
    params["start_time"] = start_time
    params["title"] = title
    result = await get_client().post(f"{ig_upcoming_event_id}", data=params)
    return json.dumps(result, indent=2)


SHADOW_IG_HASHTAG_FIELDS = [
    "id",
    "name"
]


async def get_shadow_ig_hashtag_recent_media(shadow_ig_hashtag_id: str, user_id: str, fields: Optional[str] = None) -> str:
    """GET /recent_media on ShadowIGHashtag.

    Args:
        shadow_ig_hashtag_id: The ID of the ShadowIGHashtag object.
        fields: Comma-separated list of fields to return.
        user_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["user_id"] = user_id
    result = await get_client().get(f"{shadow_ig_hashtag_id}/recent_media", params=params)
    return json.dumps(result, indent=2)


async def get_shadow_ig_hashtag_top_media(shadow_ig_hashtag_id: str, user_id: str, fields: Optional[str] = None) -> str:
    """GET /top_media on ShadowIGHashtag.

    Args:
        shadow_ig_hashtag_id: The ID of the ShadowIGHashtag object.
        fields: Comma-separated list of fields to return.
        user_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["user_id"] = user_id
    result = await get_client().get(f"{shadow_ig_hashtag_id}/top_media", params=params)
    return json.dumps(result, indent=2)


async def get_shadow_ig_hashtag(shadow_ig_hashtag_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ShadowIGHashtag.

    Args:
        shadow_ig_hashtag_id: The ID of the ShadowIGHashtag object.
        fields: Comma-separated list of fields to return. Available: id, name
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{shadow_ig_hashtag_id}", params=params)
    return json.dumps(result, indent=2)

