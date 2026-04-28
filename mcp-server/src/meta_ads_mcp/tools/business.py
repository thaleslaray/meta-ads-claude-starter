"""Auto-generated Meta Marketing API tools — business."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


BUSINESS_FIELDS = [
    "block_offline_analytics",
    "collaborative_ads_managed_partner_business_info",
    "collaborative_ads_managed_partner_eligibility",
    "collaborative_ads_partner_premium_options",
    "created_by",
    "created_time",
    "extended_updated_time",
    "id",
    "is_hidden",
    "link",
    "marketing_messages_onboarding_status",
    "name",
    "payment_account_id",
    "primary_page",
    "profile_picture_uri",
    "timezone_id",
    "two_factor_type",
    "updated_by",
    "updated_time",
    "user_access_expire_time",
    "verification_status",
    "vertical",
    "vertical_id",
    "whatsapp_business_manager_messaging_limit"
]


async def create_business_access_token(
    business_id: str,
    app_id: str,
    scope: str,
    fbe_external_business_id: Optional[str] = None,
    system_user_name: Optional[str] = None,
) -> str:
    """POST /access_token on Business.

    Args:
        business_id: The ID of the Business object.
        app_id: Required.
        fbe_external_business_id: Optional.
        scope: Required.
        system_user_name: Optional.
    """
    params = {}
    params["app_id"] = app_id
    if fbe_external_business_id is not None:
        params["fbe_external_business_id"] = fbe_external_business_id
    params["scope"] = scope
    if system_user_name is not None:
        params["system_user_name"] = system_user_name
    result = await get_client().post(f"{business_id}/access_token", data=params)
    return json.dumps(result, indent=2)


async def get_business_ad_account_infos(
    business_id: str,
    fields: Optional[str] = None,
    ad_account_id: Optional[str] = None,
    parent_advertiser_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> str:
    """GET /ad_account_infos on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        ad_account_id: Optional.
        parent_advertiser_id: Optional.
        user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_account_id is not None:
        params["ad_account_id"] = ad_account_id
    if parent_advertiser_id is not None:
        params["parent_advertiser_id"] = parent_advertiser_id
    if user_id is not None:
        params["user_id"] = user_id
    result = await get_client().get(f"{business_id}/ad_account_infos", params=params)
    return json.dumps(result, indent=2)


async def delete_business_ad_accounts(business_id: str, adaccount_id: str) -> str:
    """DELETE /ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        adaccount_id: Required.
    """
    params = {}
    params["adaccount_id"] = adaccount_id
    result = await get_client().delete(f"{business_id}/ad_accounts")
    return json.dumps(result, indent=2)


async def get_business_ad_custom_derived_metrics(
    business_id: str,
    fields: Optional[str] = None,
    adhoc_custom_metrics: Optional[str] = None,
    scope: Optional[str] = None,
) -> str:
    """GET /ad_custom_derived_metrics on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        adhoc_custom_metrics: Optional.
        scope: Optional. Values: ACCOUNT, BUSINESS, BUSINESS_ASSET_GROUP
    """
    params = {}
    params["fields"] = fields or "id,name"
    if adhoc_custom_metrics is not None:
        params["adhoc_custom_metrics"] = adhoc_custom_metrics
    if scope is not None:
        params["scope"] = scope
    result = await get_client().get(f"{business_id}/ad_custom_derived_metrics", params=params)
    return json.dumps(result, indent=2)


async def create_business_ad_review_requests(business_id: str, ad_account_ids: Optional[str] = None) -> str:
    """POST /ad_review_requests on Business.

    Args:
        business_id: The ID of the Business object.
        ad_account_ids: Optional.
    """
    params = {}
    if ad_account_ids is not None:
        params["ad_account_ids"] = ad_account_ids
    result = await get_client().post(f"{business_id}/ad_review_requests", data=params)
    return json.dumps(result, indent=2)


async def get_business_ad_studies(business_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_studies on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/ad_studies", params=params)
    return json.dumps(result, indent=2)


async def create_business_ad_studies(
    business_id: str,
    cells: str,
    end_time: int,
    name: str,
    start_time: int,
    client_business: Optional[str] = None,
    confidence_level: Optional[float] = None,
    cooldown_start_time: Optional[int] = None,
    description: Optional[str] = None,
    objectives: Optional[str] = None,
    observation_end_time: Optional[int] = None,
    type_: Optional[str] = None,
    viewers: Optional[str] = None,
) -> str:
    """POST /ad_studies on Business.

    Args:
        business_id: The ID of the Business object.
        cells: Required.
        client_business: Optional.
        confidence_level: Optional.
        cooldown_start_time: Optional.
        description: Optional.
        end_time: Required.
        name: Required.
        objectives: Optional.
        observation_end_time: Optional.
        start_time: Required.
        type_: Optional. Values: BACKEND_AB_TESTING, CONTINUOUS_LIFT_CONFIG, CREATIVE_SPEND_ENFORCEMENT, GEO_LIFT, LIFT, SPLIT_TEST
        viewers: Optional.
    """
    params = {}
    params["cells"] = cells
    if client_business is not None:
        params["client_business"] = client_business
    if confidence_level is not None:
        params["confidence_level"] = confidence_level
    if cooldown_start_time is not None:
        params["cooldown_start_time"] = cooldown_start_time
    if description is not None:
        params["description"] = description
    params["end_time"] = end_time
    params["name"] = name
    if objectives is not None:
        params["objectives"] = objectives
    if observation_end_time is not None:
        params["observation_end_time"] = observation_end_time
    params["start_time"] = start_time
    if type_ is not None:
        params["type"] = type_
    if viewers is not None:
        params["viewers"] = viewers
    result = await get_client().post(f"{business_id}/ad_studies", data=params)
    return json.dumps(result, indent=2)


async def create_business_adaccount(
    business_id: str,
    currency: str,
    end_advertiser: str,
    media_agency: str,
    name: str,
    partner: str,
    timezone_id: int,
    ad_account_created_from_bm_flag: Optional[bool] = None,
    funding_id: Optional[str] = None,
    invoice: Optional[bool] = None,
    invoice_group_id: Optional[str] = None,
    invoicing_emails: Optional[str] = None,
    io: Optional[bool] = None,
    po_number: Optional[str] = None,
) -> str:
    """POST /adaccount on Business.

    Args:
        business_id: The ID of the Business object.
        ad_account_created_from_bm_flag: Optional.
        currency: Required.
        end_advertiser: Required.
        funding_id: Optional.
        invoice: Optional.
        invoice_group_id: Optional.
        invoicing_emails: Optional.
        io: Optional.
        media_agency: Required.
        name: Required.
        partner: Required.
        po_number: Optional.
        timezone_id: Required.
    """
    params = {}
    if ad_account_created_from_bm_flag is not None:
        params["ad_account_created_from_bm_flag"] = ad_account_created_from_bm_flag
    params["currency"] = currency
    params["end_advertiser"] = end_advertiser
    if funding_id is not None:
        params["funding_id"] = funding_id
    if invoice is not None:
        params["invoice"] = invoice
    if invoice_group_id is not None:
        params["invoice_group_id"] = invoice_group_id
    if invoicing_emails is not None:
        params["invoicing_emails"] = invoicing_emails
    if io is not None:
        params["io"] = io
    params["media_agency"] = media_agency
    params["name"] = name
    params["partner"] = partner
    if po_number is not None:
        params["po_number"] = po_number
    params["timezone_id"] = timezone_id
    result = await get_client().post(f"{business_id}/adaccount", data=params)
    return json.dumps(result, indent=2)


async def create_business_add_phone_numbers(business_id: str, phone_number: str) -> str:
    """POST /add_phone_numbers on Business.

    Args:
        business_id: The ID of the Business object.
        phone_number: Required.
    """
    params = {}
    params["phone_number"] = phone_number
    result = await get_client().post(f"{business_id}/add_phone_numbers", data=params)
    return json.dumps(result, indent=2)


async def create_business_adnetwork_applications(business_id: str, name: str) -> str:
    """POST /adnetwork_applications on Business.

    Args:
        business_id: The ID of the Business object.
        name: Required.
    """
    params = {}
    params["name"] = name
    result = await get_client().post(f"{business_id}/adnetwork_applications", data=params)
    return json.dumps(result, indent=2)


async def get_business_adnetworkanalytics(
    business_id: str,
    metrics: str,
    fields: Optional[str] = None,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    should_include_until: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /adnetworkanalytics on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        should_include_until: Optional.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if should_include_until is not None:
        params["should_include_until"] = should_include_until
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{business_id}/adnetworkanalytics", params=params)
    return json.dumps(result, indent=2)


async def create_business_adnetworkanalytics(
    business_id: str,
    metrics: str,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """POST /adnetworkanalytics on Business.

    Args:
        business_id: The ID of the Business object.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        since: Optional.
        until: Optional.
    """
    params = {}
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().post(f"{business_id}/adnetworkanalytics", data=params)
    return json.dumps(result, indent=2)


async def get_business_adnetworkanalytics_results(business_id: str, fields: Optional[str] = None, query_ids: Optional[str] = None) -> str:
    """GET /adnetworkanalytics_results on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        query_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if query_ids is not None:
        params["query_ids"] = query_ids
    result = await get_client().get(f"{business_id}/adnetworkanalytics_results", params=params)
    return json.dumps(result, indent=2)


async def get_business_ads_dataset(
    business_id: str,
    fields: Optional[str] = None,
    id_filter: Optional[str] = None,
    name_filter: Optional[str] = None,
    sort_by: Optional[str] = None,
) -> str:
    """GET /ads_dataset on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        id_filter: Optional.
        name_filter: Optional.
        sort_by: Optional. Values: LAST_FIRED_TIME, NAME
    """
    params = {}
    params["fields"] = fields or "id,name"
    if id_filter is not None:
        params["id_filter"] = id_filter
    if name_filter is not None:
        params["name_filter"] = name_filter
    if sort_by is not None:
        params["sort_by"] = sort_by
    result = await get_client().get(f"{business_id}/ads_dataset", params=params)
    return json.dumps(result, indent=2)


async def create_business_ads_dataset(
    business_id: str,
    name: str,
    ad_account_id: Optional[str] = None,
    app_id: Optional[str] = None,
    is_crm: Optional[bool] = None,
) -> str:
    """POST /ads_dataset on Business.

    Args:
        business_id: The ID of the Business object.
        ad_account_id: Optional.
        app_id: Optional.
        is_crm: Optional.
        name: Required.
    """
    params = {}
    if ad_account_id is not None:
        params["ad_account_id"] = ad_account_id
    if app_id is not None:
        params["app_id"] = app_id
    if is_crm is not None:
        params["is_crm"] = is_crm
    params["name"] = name
    result = await get_client().post(f"{business_id}/ads_dataset", data=params)
    return json.dumps(result, indent=2)


async def get_business_ads_reporting_mmm_reports(business_id: str, fields: Optional[str] = None, filtering: Optional[str] = None) -> str:
    """GET /ads_reporting_mmm_reports on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        filtering: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if filtering is not None:
        params["filtering"] = filtering
    result = await get_client().get(f"{business_id}/ads_reporting_mmm_reports", params=params)
    return json.dumps(result, indent=2)


async def get_business_ads_reporting_mmm_schedulers(business_id: str, fields: Optional[str] = None) -> str:
    """GET /ads_reporting_mmm_schedulers on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/ads_reporting_mmm_schedulers", params=params)
    return json.dumps(result, indent=2)


async def get_business_adspixels(
    business_id: str,
    fields: Optional[str] = None,
    id_filter: Optional[str] = None,
    name_filter: Optional[str] = None,
    sort_by: Optional[str] = None,
) -> str:
    """GET /adspixels on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        id_filter: Optional.
        name_filter: Optional.
        sort_by: Optional. Values: LAST_FIRED_TIME, NAME
    """
    params = {}
    params["fields"] = fields or "id,name"
    if id_filter is not None:
        params["id_filter"] = id_filter
    if name_filter is not None:
        params["name_filter"] = name_filter
    if sort_by is not None:
        params["sort_by"] = sort_by
    result = await get_client().get(f"{business_id}/adspixels", params=params)
    return json.dumps(result, indent=2)


async def create_business_adspixels(business_id: str, name: str, is_crm: Optional[bool] = None) -> str:
    """POST /adspixels on Business.

    Args:
        business_id: The ID of the Business object.
        is_crm: Optional.
        name: Required.
    """
    params = {}
    if is_crm is not None:
        params["is_crm"] = is_crm
    params["name"] = name
    result = await get_client().post(f"{business_id}/adspixels", data=params)
    return json.dumps(result, indent=2)


async def delete_business_agencies(business_id: str, business: str) -> str:
    """DELETE /agencies on Business.

    Args:
        business_id: The ID of the Business object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{business_id}/agencies")
    return json.dumps(result, indent=2)


async def get_business_agencies(business_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def get_business_an_placements(business_id: str, fields: Optional[str] = None) -> str:
    """GET /an_placements on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/an_placements", params=params)
    return json.dumps(result, indent=2)


async def create_business_block_list_drafts(business_id: str, publisher_urls_file: str) -> str:
    """POST /block_list_drafts on Business.

    Args:
        business_id: The ID of the Business object.
        publisher_urls_file: Required.
    """
    params = {}
    params["publisher_urls_file"] = publisher_urls_file
    result = await get_client().post(f"{business_id}/block_list_drafts", data=params)
    return json.dumps(result, indent=2)


async def create_business_bm_review_requests(business_id: str, business_manager_ids: str) -> str:
    """POST /bm_review_requests on Business.

    Args:
        business_id: The ID of the Business object.
        business_manager_ids: Required.
    """
    params = {}
    params["business_manager_ids"] = business_manager_ids
    result = await get_client().post(f"{business_id}/bm_review_requests", data=params)
    return json.dumps(result, indent=2)


async def get_business_business_asset_groups(business_id: str, fields: Optional[str] = None) -> str:
    """GET /business_asset_groups on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/business_asset_groups", params=params)
    return json.dumps(result, indent=2)


async def get_business_business_invoices(
    business_id: str,
    fields: Optional[str] = None,
    end_date: Optional[str] = None,
    invoice_id: Optional[str] = None,
    issue_end_date: Optional[str] = None,
    issue_start_date: Optional[str] = None,
    root_id: Optional[int] = None,
    start_date: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /business_invoices on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        end_date: Optional.
        invoice_id: Optional.
        issue_end_date: Optional.
        issue_start_date: Optional.
        root_id: Optional.
        start_date: Optional.
        type_: Optional. Values: CM, DM, INV, PRO_FORMA
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_date is not None:
        params["end_date"] = end_date
    if invoice_id is not None:
        params["invoice_id"] = invoice_id
    if issue_end_date is not None:
        params["issue_end_date"] = issue_end_date
    if issue_start_date is not None:
        params["issue_start_date"] = issue_start_date
    if root_id is not None:
        params["root_id"] = root_id
    if start_date is not None:
        params["start_date"] = start_date
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{business_id}/business_invoices", params=params)
    return json.dumps(result, indent=2)


async def get_business_business_users(business_id: str, fields: Optional[str] = None) -> str:
    """GET /business_users on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/business_users", params=params)
    return json.dumps(result, indent=2)


async def create_business_business_users(
    business_id: str,
    email: str,
    invited_user_type: Optional[str] = None,
    role: Optional[str] = None,
    tasks: Optional[str] = None,
) -> str:
    """POST /business_users on Business.

    Args:
        business_id: The ID of the Business object.
        email: Required.
        invited_user_type: Optional. Values: FB, MWA
        role: Optional. Values: ADMIN, ADS_RIGHTS_REVIEWER, DEFAULT, DEVELOPER, EMPLOYEE, FINANCE_ANALYST, FINANCE_EDIT, FINANCE_EDITOR, FINANCE_VIEW, MANAGE, PARTNER_CENTER_ADMIN, PARTNER_CENTER_ANALYST, PARTNER_CENTER_EDUCATION, PARTNER_CENTER_MARKETING, PARTNER_CENTER_OPERATIONS
        tasks: Optional. Values: ADMIN, ADS_RIGHTS_REVIEWER, DEFAULT, DEVELOPER, EMPLOYEE, FINANCE_ANALYST, FINANCE_EDIT, FINANCE_EDITOR, FINANCE_VIEW, MANAGE, PARTNER_CENTER_ADMIN, PARTNER_CENTER_ANALYST, PARTNER_CENTER_EDUCATION, PARTNER_CENTER_MARKETING, PARTNER_CENTER_OPERATIONS
    """
    params = {}
    params["email"] = email
    if invited_user_type is not None:
        params["invited_user_type"] = invited_user_type
    if role is not None:
        params["role"] = role
    if tasks is not None:
        params["tasks"] = tasks
    result = await get_client().post(f"{business_id}/business_users", data=params)
    return json.dumps(result, indent=2)


async def get_business_businessprojects(business_id: str, fields: Optional[str] = None) -> str:
    """GET /businessprojects on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/businessprojects", params=params)
    return json.dumps(result, indent=2)


async def create_business_claim_custom_conversions(business_id: str, custom_conversion_id: str) -> str:
    """POST /claim_custom_conversions on Business.

    Args:
        business_id: The ID of the Business object.
        custom_conversion_id: Required.
    """
    params = {}
    params["custom_conversion_id"] = custom_conversion_id
    result = await get_client().post(f"{business_id}/claim_custom_conversions", data=params)
    return json.dumps(result, indent=2)


async def get_business_client_ad_accounts(
    business_id: str,
    fields: Optional[str] = None,
    search_query: Optional[str] = None,
) -> str:
    """GET /client_ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        search_query: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if search_query is not None:
        params["search_query"] = search_query
    result = await get_client().get(f"{business_id}/client_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_client_apps(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_apps on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_apps", params=params)
    return json.dumps(result, indent=2)


async def create_business_client_apps(business_id: str, app_id: str) -> str:
    """POST /client_apps on Business.

    Args:
        business_id: The ID of the Business object.
        app_id: Required.
    """
    params = {}
    params["app_id"] = app_id
    result = await get_client().post(f"{business_id}/client_apps", data=params)
    return json.dumps(result, indent=2)


async def get_business_client_instagram_assets(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_instagram_assets on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_instagram_assets", params=params)
    return json.dumps(result, indent=2)


async def get_business_client_offsite_signal_container_business_objects(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_offsite_signal_container_business_objects on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_offsite_signal_container_business_objects", params=params)
    return json.dumps(result, indent=2)


async def get_business_client_pages(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_pages on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_pages", params=params)
    return json.dumps(result, indent=2)


async def create_business_client_pages(business_id: str, page_id: int, permitted_tasks: Optional[str] = None) -> str:
    """POST /client_pages on Business.

    Args:
        business_id: The ID of the Business object.
        page_id: Required.
        permitted_tasks: Optional. Values: ADVERTISE, ANALYZE, CASHIER_ROLE, CREATE_CONTENT, GLOBAL_STRUCTURE_MANAGEMENT, MANAGE, MANAGE_JOBS, MANAGE_LEADS, MESSAGING, MODERATE, MODERATE_COMMUNITY, PAGES_MESSAGING, PAGES_MESSAGING_SUBSCRIPTIONS, PROFILE_PLUS_ADVERTISE, PROFILE_PLUS_ANALYZE, PROFILE_PLUS_CREATE_CONTENT, PROFILE_PLUS_FACEBOOK_ACCESS, PROFILE_PLUS_FULL_CONTROL, PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT, PROFILE_PLUS_MANAGE, PROFILE_PLUS_MANAGE_LEADS, PROFILE_PLUS_MESSAGING, PROFILE_PLUS_MODERATE, PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY, PROFILE_PLUS_REVENUE, READ_PAGE_MAILBOXES, VIEW_MONETIZATION_INSIGHTS
    """
    params = {}
    params["page_id"] = page_id
    if permitted_tasks is not None:
        params["permitted_tasks"] = permitted_tasks
    result = await get_client().post(f"{business_id}/client_pages", data=params)
    return json.dumps(result, indent=2)


async def get_business_client_pixels(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_pixels on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_pixels", params=params)
    return json.dumps(result, indent=2)


async def get_business_client_product_catalogs(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_product_catalogs on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_business_client_whatsapp_business_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /client_whatsapp_business_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/client_whatsapp_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def delete_business_clients(business_id: str, business: str) -> str:
    """DELETE /clients on Business.

    Args:
        business_id: The ID of the Business object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{business_id}/clients")
    return json.dumps(result, indent=2)


async def get_business_clients(business_id: str, fields: Optional[str] = None) -> str:
    """GET /clients on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/clients", params=params)
    return json.dumps(result, indent=2)


async def get_business_collaborative_ads_collaboration_requests(business_id: str, fields: Optional[str] = None, status: Optional[str] = None) -> str:
    """GET /collaborative_ads_collaboration_requests on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        status: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{business_id}/collaborative_ads_collaboration_requests", params=params)
    return json.dumps(result, indent=2)


async def create_business_collaborative_ads_collaboration_requests(
    business_id: str,
    brands: str,
    contact_email: str,
    contact_first_name: str,
    contact_last_name: str,
    receiver_business: str,
    requester_agency_or_brand: str,
    phone_number: Optional[str] = None,
    sender_client_business: Optional[str] = None,
) -> str:
    """POST /collaborative_ads_collaboration_requests on Business.

    Args:
        business_id: The ID of the Business object.
        brands: Required.
        contact_email: Required.
        contact_first_name: Required.
        contact_last_name: Required.
        phone_number: Optional.
        receiver_business: Required.
        requester_agency_or_brand: Required. Values: AGENCY, BRAND, MERCHANT
        sender_client_business: Optional.
    """
    params = {}
    params["brands"] = brands
    params["contact_email"] = contact_email
    params["contact_first_name"] = contact_first_name
    params["contact_last_name"] = contact_last_name
    if phone_number is not None:
        params["phone_number"] = phone_number
    params["receiver_business"] = receiver_business
    params["requester_agency_or_brand"] = requester_agency_or_brand
    if sender_client_business is not None:
        params["sender_client_business"] = sender_client_business
    result = await get_client().post(f"{business_id}/collaborative_ads_collaboration_requests", data=params)
    return json.dumps(result, indent=2)


async def get_business_collaborative_ads_suggested_partners(business_id: str, fields: Optional[str] = None) -> str:
    """GET /collaborative_ads_suggested_partners on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/collaborative_ads_suggested_partners", params=params)
    return json.dumps(result, indent=2)


async def get_business_commerce_merchant_settings(business_id: str, fields: Optional[str] = None) -> str:
    """GET /commerce_merchant_settings on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/commerce_merchant_settings", params=params)
    return json.dumps(result, indent=2)


async def get_business_cpas_business_setup_config(business_id: str, fields: Optional[str] = None) -> str:
    """GET /cpas_business_setup_config on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/cpas_business_setup_config", params=params)
    return json.dumps(result, indent=2)


async def create_business_cpas_business_setup_config(
    business_id: str,
    accepted_collab_ads_tos: Optional[bool] = None,
    ad_accounts: Optional[str] = None,
    business_capabilities_status: Optional[str] = None,
    capabilities_compliance_status: Optional[str] = None,
) -> str:
    """POST /cpas_business_setup_config on Business.

    Args:
        business_id: The ID of the Business object.
        accepted_collab_ads_tos: Optional.
        ad_accounts: Optional.
        business_capabilities_status: Optional.
        capabilities_compliance_status: Optional.
    """
    params = {}
    if accepted_collab_ads_tos is not None:
        params["accepted_collab_ads_tos"] = accepted_collab_ads_tos
    if ad_accounts is not None:
        params["ad_accounts"] = ad_accounts
    if business_capabilities_status is not None:
        params["business_capabilities_status"] = business_capabilities_status
    if capabilities_compliance_status is not None:
        params["capabilities_compliance_status"] = capabilities_compliance_status
    result = await get_client().post(f"{business_id}/cpas_business_setup_config", data=params)
    return json.dumps(result, indent=2)


async def get_business_cpas_merchant_config(business_id: str, fields: Optional[str] = None) -> str:
    """GET /cpas_merchant_config on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/cpas_merchant_config", params=params)
    return json.dumps(result, indent=2)


async def create_business_creative_folders(
    business_id: str,
    name: str,
    description: Optional[str] = None,
    parent_folder_id: Optional[str] = None,
) -> str:
    """POST /creative_folders on Business.

    Args:
        business_id: The ID of the Business object.
        description: Optional.
        name: Required.
        parent_folder_id: Optional.
    """
    params = {}
    if description is not None:
        params["description"] = description
    params["name"] = name
    if parent_folder_id is not None:
        params["parent_folder_id"] = parent_folder_id
    result = await get_client().post(f"{business_id}/creative_folders", data=params)
    return json.dumps(result, indent=2)


async def get_business_creditcards(business_id: str, fields: Optional[str] = None) -> str:
    """GET /creditcards on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/creditcards", params=params)
    return json.dumps(result, indent=2)


async def create_business_customconversions(
    business_id: str,
    custom_event_type: str,
    name: str,
    action_source_type: Optional[str] = None,
    advanced_rule: Optional[str] = None,
    default_conversion_value: Optional[float] = None,
    description: Optional[str] = None,
    event_source_id: Optional[str] = None,
    rule: Optional[str] = None,
) -> str:
    """POST /customconversions on Business.

    Args:
        business_id: The ID of the Business object.
        action_source_type: Optional. Values: app, business_messaging, chat, email, other, phone_call, physical_store, system_generated, website
        advanced_rule: Optional.
        custom_event_type: Required. Values: ADD_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, COMPLETE_REGISTRATION, CONTACT, CONTENT_VIEW, CUSTOMIZE_PRODUCT, DONATE, FACEBOOK_SELECTED, FIND_LOCATION, INITIATED_CHECKOUT, LEAD, LISTING_INTERACTION, OTHER, PURCHASE, SCHEDULE, SEARCH, START_TRIAL, SUBMIT_APPLICATION, SUBSCRIBE
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
    result = await get_client().post(f"{business_id}/customconversions", data=params)
    return json.dumps(result, indent=2)


async def get_business_event_source_groups(business_id: str, fields: Optional[str] = None) -> str:
    """GET /event_source_groups on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/event_source_groups", params=params)
    return json.dumps(result, indent=2)


async def create_business_event_source_groups(business_id: str, event_sources: str, name: str) -> str:
    """POST /event_source_groups on Business.

    Args:
        business_id: The ID of the Business object.
        event_sources: Required.
        name: Required.
    """
    params = {}
    params["event_sources"] = event_sources
    params["name"] = name
    result = await get_client().post(f"{business_id}/event_source_groups", data=params)
    return json.dumps(result, indent=2)


async def get_business_extendedcreditapplications(
    business_id: str,
    fields: Optional[str] = None,
    only_show_pending: Optional[bool] = None,
) -> str:
    """GET /extendedcreditapplications on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        only_show_pending: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if only_show_pending is not None:
        params["only_show_pending"] = only_show_pending
    result = await get_client().get(f"{business_id}/extendedcreditapplications", params=params)
    return json.dumps(result, indent=2)


async def get_business_extendedcredits(
    business_id: str,
    fields: Optional[str] = None,
    order_by_is_owned_credential: Optional[bool] = None,
) -> str:
    """GET /extendedcredits on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        order_by_is_owned_credential: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if order_by_is_owned_credential is not None:
        params["order_by_is_owned_credential"] = order_by_is_owned_credential
    result = await get_client().get(f"{business_id}/extendedcredits", params=params)
    return json.dumps(result, indent=2)


async def create_business_images(
    business_id: str,
    creative_folder_id: str,
    ad_placements_validation_only: Optional[bool] = None,
    bytes_: Optional[str] = None,
    name: Optional[str] = None,
    validation_ad_placements: Optional[str] = None,
) -> str:
    """POST /images on Business.

    Args:
        business_id: The ID of the Business object.
        ad_placements_validation_only: Optional.
        bytes_: Optional.
        creative_folder_id: Required.
        name: Optional.
        validation_ad_placements: Optional. Values: AUDIENCE_NETWORK_INSTREAM_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE, AUDIENCE_NETWORK_REWARDED_VIDEO, DESKTOP_FEED_STANDARD, FACEBOOK_STORY_MOBILE, FACEBOOK_STORY_STICKER_MOBILE, INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTANT_ARTICLE_STANDARD, INSTREAM_BANNER_DESKTOP, INSTREAM_BANNER_MOBILE, INSTREAM_VIDEO_DESKTOP, INSTREAM_VIDEO_IMAGE, INSTREAM_VIDEO_MOBILE, MESSENGER_MOBILE_INBOX_MEDIA, MESSENGER_MOBILE_STORY_MEDIA, MOBILE_FEED_STANDARD, MOBILE_FULLWIDTH, MOBILE_INTERSTITIAL, MOBILE_MEDIUM_RECTANGLE, MOBILE_NATIVE, RIGHT_COLUMN_STANDARD, SUGGESTED_VIDEO_MOBILE
    """
    params = {}
    if ad_placements_validation_only is not None:
        params["ad_placements_validation_only"] = ad_placements_validation_only
    if bytes_ is not None:
        params["bytes"] = bytes_
    params["creative_folder_id"] = creative_folder_id
    if name is not None:
        params["name"] = name
    if validation_ad_placements is not None:
        params["validation_ad_placements"] = validation_ad_placements
    result = await get_client().post(f"{business_id}/images", data=params)
    return json.dumps(result, indent=2)


async def get_business_initiated_audience_sharing_requests(
    business_id: str,
    fields: Optional[str] = None,
    recipient_id: Optional[str] = None,
    request_status: Optional[str] = None,
) -> str:
    """GET /initiated_audience_sharing_requests on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        recipient_id: Optional.
        request_status: Optional. Values: APPROVE, CANCELED, DECLINE, EXPIRED, IN_PROGRESS, MMA_DIRECT_ASSETS_APPROVED, MMA_DIRECT_ASSETS_DECLINED, MMA_DIRECT_ASSETS_EXPIRED, MMA_DIRECT_ASSETS_PENDING, PENDING, PENDING_EMAIL_VERIFICATION, PENDING_INTEGRITY_REVIEW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if recipient_id is not None:
        params["recipient_id"] = recipient_id
    if request_status is not None:
        params["request_status"] = request_status
    result = await get_client().get(f"{business_id}/initiated_audience_sharing_requests", params=params)
    return json.dumps(result, indent=2)


async def delete_business_instagram_accounts(business_id: str, instagram_account: str) -> str:
    """DELETE /instagram_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        instagram_account: Required.
    """
    params = {}
    params["instagram_account"] = instagram_account
    result = await get_client().delete(f"{business_id}/instagram_accounts")
    return json.dumps(result, indent=2)


async def get_business_instagram_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_instagram_business_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /instagram_business_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/instagram_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def delete_business_managed_businesses(business_id: str, existing_client_business_id: str) -> str:
    """DELETE /managed_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        existing_client_business_id: Required.
    """
    params = {}
    params["existing_client_business_id"] = existing_client_business_id
    result = await get_client().delete(f"{business_id}/managed_businesses")
    return json.dumps(result, indent=2)


async def create_business_managed_businesses(
    business_id: str,
    child_business_external_id: Optional[str] = None,
    existing_client_business_id: Optional[str] = None,
    name: Optional[str] = None,
    sales_rep_email: Optional[str] = None,
    survey_business_type: Optional[str] = None,
    survey_num_assets: Optional[int] = None,
    survey_num_people: Optional[int] = None,
    timezone_id: Optional[str] = None,
    vertical: Optional[str] = None,
) -> str:
    """POST /managed_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        child_business_external_id: Optional.
        existing_client_business_id: Optional.
        name: Optional.
        sales_rep_email: Optional.
        survey_business_type: Optional. Values: ADVERTISER, AGENCY, APP_DEVELOPER, PUBLISHER
        survey_num_assets: Optional.
        survey_num_people: Optional.
        timezone_id: Optional. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480
        vertical: Optional. Values: ADVERTISING, AUTOMOTIVE, CONSUMER_PACKAGED_GOODS, ECOMMERCE, EDUCATION, ENERGY_AND_UTILITIES, ENTERTAINMENT_AND_MEDIA, FINANCIAL_SERVICES, GAMING, GOVERNMENT_AND_POLITICS, HEALTH, LUXURY, MARKETING, NON_PROFIT, NOT_SET, ORGANIZATIONS_AND_ASSOCIATIONS, OTHER, PROFESSIONAL_SERVICES, RESTAURANT, RETAIL, TECHNOLOGY, TELECOM, TRAVEL
    """
    params = {}
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    if existing_client_business_id is not None:
        params["existing_client_business_id"] = existing_client_business_id
    if name is not None:
        params["name"] = name
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
    if vertical is not None:
        params["vertical"] = vertical
    result = await get_client().post(f"{business_id}/managed_businesses", data=params)
    return json.dumps(result, indent=2)


async def get_business_managed_partner_ads_funding_source_details(
    business_id: str,
    fields: Optional[str] = None,
    year_quarter: Optional[str] = None,
) -> str:
    """GET /managed_partner_ads_funding_source_details on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        year_quarter: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if year_quarter is not None:
        params["year_quarter"] = year_quarter
    result = await get_client().get(f"{business_id}/managed_partner_ads_funding_source_details", params=params)
    return json.dumps(result, indent=2)


async def create_business_managed_partner_business_setup(
    business_id: str,
    active_ad_account_id: Optional[str] = None,
    active_page_id: Optional[int] = None,
    partner_facebook_page_url: Optional[str] = None,
    partner_registration_countries: Optional[str] = None,
    seller_email_address: Optional[str] = None,
    seller_external_website_url: Optional[str] = None,
    template: Optional[str] = None,
) -> str:
    """POST /managed_partner_business_setup on Business.

    Args:
        business_id: The ID of the Business object.
        active_ad_account_id: Optional.
        active_page_id: Optional.
        partner_facebook_page_url: Optional.
        partner_registration_countries: Optional.
        seller_email_address: Optional.
        seller_external_website_url: Optional.
        template: Optional.
    """
    params = {}
    if active_ad_account_id is not None:
        params["active_ad_account_id"] = active_ad_account_id
    if active_page_id is not None:
        params["active_page_id"] = active_page_id
    if partner_facebook_page_url is not None:
        params["partner_facebook_page_url"] = partner_facebook_page_url
    if partner_registration_countries is not None:
        params["partner_registration_countries"] = partner_registration_countries
    if seller_email_address is not None:
        params["seller_email_address"] = seller_email_address
    if seller_external_website_url is not None:
        params["seller_external_website_url"] = seller_external_website_url
    if template is not None:
        params["template"] = template
    result = await get_client().post(f"{business_id}/managed_partner_business_setup", data=params)
    return json.dumps(result, indent=2)


async def delete_business_managed_partner_businesses(
    business_id: str,
    child_business_external_id: Optional[str] = None,
    child_business_id: Optional[str] = None,
) -> str:
    """DELETE /managed_partner_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        child_business_external_id: Optional.
        child_business_id: Optional.
    """
    params = {}
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    if child_business_id is not None:
        params["child_business_id"] = child_business_id
    result = await get_client().delete(f"{business_id}/managed_partner_businesses")
    return json.dumps(result, indent=2)


async def create_business_managed_partner_businesses(
    business_id: str,
    catalog_id: str,
    name: str,
    seller_external_website_url: str,
    seller_targeting_countries: str,
    vertical: str,
    ad_account_currency: Optional[str] = None,
    child_business_external_id: Optional[str] = None,
    credit_limit: Optional[int] = None,
    line_of_credit_id: Optional[str] = None,
    no_ad_account: Optional[bool] = None,
    page_name: Optional[str] = None,
    page_profile_image_url: Optional[str] = None,
    partition_type: Optional[str] = None,
    partner_facebook_page_url: Optional[str] = None,
    partner_registration_countries: Optional[str] = None,
    sales_rep_email: Optional[str] = None,
    skip_partner_page_creation: Optional[bool] = None,
    survey_business_type: Optional[str] = None,
    survey_num_assets: Optional[int] = None,
    survey_num_people: Optional[int] = None,
    timezone_id: Optional[str] = None,
) -> str:
    """POST /managed_partner_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        ad_account_currency: Optional.
        catalog_id: Required.
        child_business_external_id: Optional.
        credit_limit: Optional.
        line_of_credit_id: Optional.
        name: Required.
        no_ad_account: Optional.
        page_name: Optional.
        page_profile_image_url: Optional.
        partition_type: Optional. Values: AUTH, FIXED, FIXED_WITHOUT_PARTITION
        partner_facebook_page_url: Optional.
        partner_registration_countries: Optional.
        sales_rep_email: Optional.
        seller_external_website_url: Required.
        seller_targeting_countries: Required.
        skip_partner_page_creation: Optional.
        survey_business_type: Optional. Values: ADVERTISER, AGENCY, APP_DEVELOPER, PUBLISHER
        survey_num_assets: Optional.
        survey_num_people: Optional.
        timezone_id: Optional. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480
        vertical: Required. Values: ADVERTISING, AUTOMOTIVE, CONSUMER_PACKAGED_GOODS, ECOMMERCE, EDUCATION, ENERGY_AND_UTILITIES, ENTERTAINMENT_AND_MEDIA, FINANCIAL_SERVICES, GAMING, GOVERNMENT_AND_POLITICS, HEALTH, LUXURY, MARKETING, NON_PROFIT, NOT_SET, ORGANIZATIONS_AND_ASSOCIATIONS, OTHER, PROFESSIONAL_SERVICES, RESTAURANT, RETAIL, TECHNOLOGY, TELECOM, TRAVEL
    """
    params = {}
    if ad_account_currency is not None:
        params["ad_account_currency"] = ad_account_currency
    params["catalog_id"] = catalog_id
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    if credit_limit is not None:
        params["credit_limit"] = credit_limit
    if line_of_credit_id is not None:
        params["line_of_credit_id"] = line_of_credit_id
    params["name"] = name
    if no_ad_account is not None:
        params["no_ad_account"] = no_ad_account
    if page_name is not None:
        params["page_name"] = page_name
    if page_profile_image_url is not None:
        params["page_profile_image_url"] = page_profile_image_url
    if partition_type is not None:
        params["partition_type"] = partition_type
    if partner_facebook_page_url is not None:
        params["partner_facebook_page_url"] = partner_facebook_page_url
    if partner_registration_countries is not None:
        params["partner_registration_countries"] = partner_registration_countries
    if sales_rep_email is not None:
        params["sales_rep_email"] = sales_rep_email
    params["seller_external_website_url"] = seller_external_website_url
    params["seller_targeting_countries"] = seller_targeting_countries
    if skip_partner_page_creation is not None:
        params["skip_partner_page_creation"] = skip_partner_page_creation
    if survey_business_type is not None:
        params["survey_business_type"] = survey_business_type
    if survey_num_assets is not None:
        params["survey_num_assets"] = survey_num_assets
    if survey_num_people is not None:
        params["survey_num_people"] = survey_num_people
    if timezone_id is not None:
        params["timezone_id"] = timezone_id
    params["vertical"] = vertical
    result = await get_client().post(f"{business_id}/managed_partner_businesses", data=params)
    return json.dumps(result, indent=2)


async def create_business_onboard_partners_to_mm_lite(business_id: str, solution_id: Optional[str] = None) -> str:
    """POST /onboard_partners_to_mm_lite on Business.

    Args:
        business_id: The ID of the Business object.
        solution_id: Optional.
    """
    params = {}
    if solution_id is not None:
        params["solution_id"] = solution_id
    result = await get_client().post(f"{business_id}/onboard_partners_to_mm_lite", data=params)
    return json.dumps(result, indent=2)


async def get_business_openbridge_configurations(business_id: str, fields: Optional[str] = None) -> str:
    """GET /openbridge_configurations on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/openbridge_configurations", params=params)
    return json.dumps(result, indent=2)


async def create_business_openbridge_configurations(
    business_id: str,
    pixel_id: int,
    active: Optional[bool] = None,
    blocked_event_types: Optional[str] = None,
    blocked_websites: Optional[str] = None,
    cloud_provider: Optional[str] = None,
    cloud_region: Optional[str] = None,
    destination_id: Optional[str] = None,
    endpoint: Optional[str] = None,
    event_enrichment_state: Optional[str] = None,
    fallback_domain: Optional[str] = None,
    first_party_domain: Optional[str] = None,
    host_business_id: Optional[int] = None,
    instance_id: Optional[str] = None,
    instance_version: Optional[str] = None,
    is_sgw_instance: Optional[bool] = None,
    is_sgw_pixel_from_meta_pixel: Optional[bool] = None,
    partner_name: Optional[str] = None,
    sgw_account_id: Optional[str] = None,
    sgw_instance_url: Optional[str] = None,
    sgw_pixel_id: Optional[int] = None,
) -> str:
    """POST /openbridge_configurations on Business.

    Args:
        business_id: The ID of the Business object.
        active: Optional.
        blocked_event_types: Optional.
        blocked_websites: Optional.
        cloud_provider: Optional.
        cloud_region: Optional.
        destination_id: Optional.
        endpoint: Optional.
        event_enrichment_state: Optional. Values: NO, NOT_INITIALIZED, YES
        fallback_domain: Optional.
        first_party_domain: Optional.
        host_business_id: Optional.
        instance_id: Optional.
        instance_version: Optional.
        is_sgw_instance: Optional.
        is_sgw_pixel_from_meta_pixel: Optional.
        partner_name: Optional.
        pixel_id: Required.
        sgw_account_id: Optional.
        sgw_instance_url: Optional.
        sgw_pixel_id: Optional.
    """
    params = {}
    if active is not None:
        params["active"] = active
    if blocked_event_types is not None:
        params["blocked_event_types"] = blocked_event_types
    if blocked_websites is not None:
        params["blocked_websites"] = blocked_websites
    if cloud_provider is not None:
        params["cloud_provider"] = cloud_provider
    if cloud_region is not None:
        params["cloud_region"] = cloud_region
    if destination_id is not None:
        params["destination_id"] = destination_id
    if endpoint is not None:
        params["endpoint"] = endpoint
    if event_enrichment_state is not None:
        params["event_enrichment_state"] = event_enrichment_state
    if fallback_domain is not None:
        params["fallback_domain"] = fallback_domain
    if first_party_domain is not None:
        params["first_party_domain"] = first_party_domain
    if host_business_id is not None:
        params["host_business_id"] = host_business_id
    if instance_id is not None:
        params["instance_id"] = instance_id
    if instance_version is not None:
        params["instance_version"] = instance_version
    if is_sgw_instance is not None:
        params["is_sgw_instance"] = is_sgw_instance
    if is_sgw_pixel_from_meta_pixel is not None:
        params["is_sgw_pixel_from_meta_pixel"] = is_sgw_pixel_from_meta_pixel
    if partner_name is not None:
        params["partner_name"] = partner_name
    params["pixel_id"] = pixel_id
    if sgw_account_id is not None:
        params["sgw_account_id"] = sgw_account_id
    if sgw_instance_url is not None:
        params["sgw_instance_url"] = sgw_instance_url
    if sgw_pixel_id is not None:
        params["sgw_pixel_id"] = sgw_pixel_id
    result = await get_client().post(f"{business_id}/openbridge_configurations", data=params)
    return json.dumps(result, indent=2)


async def get_business_owned_ad_accounts(
    business_id: str,
    fields: Optional[str] = None,
    search_query: Optional[str] = None,
) -> str:
    """GET /owned_ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        search_query: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if search_query is not None:
        params["search_query"] = search_query
    result = await get_client().get(f"{business_id}/owned_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_business_owned_ad_accounts(business_id: str, adaccount_id: str) -> str:
    """POST /owned_ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        adaccount_id: Required.
    """
    params = {}
    params["adaccount_id"] = adaccount_id
    result = await get_client().post(f"{business_id}/owned_ad_accounts", data=params)
    return json.dumps(result, indent=2)


async def get_business_owned_apps(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_apps on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_apps", params=params)
    return json.dumps(result, indent=2)


async def create_business_owned_apps(business_id: str, app_id: str) -> str:
    """POST /owned_apps on Business.

    Args:
        business_id: The ID of the Business object.
        app_id: Required.
    """
    params = {}
    params["app_id"] = app_id
    result = await get_client().post(f"{business_id}/owned_apps", data=params)
    return json.dumps(result, indent=2)


async def delete_business_owned_businesses(business_id: str, client_id: str) -> str:
    """DELETE /owned_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        client_id: Required.
    """
    params = {}
    params["client_id"] = client_id
    result = await get_client().delete(f"{business_id}/owned_businesses")
    return json.dumps(result, indent=2)


async def get_business_owned_businesses(
    business_id: str,
    fields: Optional[str] = None,
    child_business_external_id: Optional[str] = None,
    client_user_id: Optional[int] = None,
) -> str:
    """GET /owned_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        child_business_external_id: Optional.
        client_user_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    if client_user_id is not None:
        params["client_user_id"] = client_user_id
    result = await get_client().get(f"{business_id}/owned_businesses", params=params)
    return json.dumps(result, indent=2)


async def create_business_owned_businesses(
    business_id: str,
    name: str,
    vertical: str,
    child_business_external_id: Optional[str] = None,
    page_permitted_tasks: Optional[str] = None,
    sales_rep_email: Optional[str] = None,
    shared_page_id: Optional[str] = None,
    should_generate_name: Optional[bool] = None,
    survey_business_type: Optional[str] = None,
    survey_num_assets: Optional[int] = None,
    survey_num_people: Optional[int] = None,
    timezone_id: Optional[str] = None,
) -> str:
    """POST /owned_businesses on Business.

    Args:
        business_id: The ID of the Business object.
        child_business_external_id: Optional.
        name: Required.
        page_permitted_tasks: Optional. Values: ADVERTISE, ANALYZE, CASHIER_ROLE, CREATE_CONTENT, GLOBAL_STRUCTURE_MANAGEMENT, MANAGE, MANAGE_JOBS, MANAGE_LEADS, MESSAGING, MODERATE, MODERATE_COMMUNITY, PAGES_MESSAGING, PAGES_MESSAGING_SUBSCRIPTIONS, PROFILE_PLUS_ADVERTISE, PROFILE_PLUS_ANALYZE, PROFILE_PLUS_CREATE_CONTENT, PROFILE_PLUS_FACEBOOK_ACCESS, PROFILE_PLUS_FULL_CONTROL, PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT, PROFILE_PLUS_MANAGE, PROFILE_PLUS_MANAGE_LEADS, PROFILE_PLUS_MESSAGING, PROFILE_PLUS_MODERATE, PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY, PROFILE_PLUS_REVENUE, READ_PAGE_MAILBOXES, VIEW_MONETIZATION_INSIGHTS
        sales_rep_email: Optional.
        shared_page_id: Optional.
        should_generate_name: Optional.
        survey_business_type: Optional. Values: ADVERTISER, AGENCY, APP_DEVELOPER, PUBLISHER
        survey_num_assets: Optional.
        survey_num_people: Optional.
        timezone_id: Optional. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480
        vertical: Required. Values: ADVERTISING, AUTOMOTIVE, CONSUMER_PACKAGED_GOODS, ECOMMERCE, EDUCATION, ENERGY_AND_UTILITIES, ENTERTAINMENT_AND_MEDIA, FINANCIAL_SERVICES, GAMING, GOVERNMENT_AND_POLITICS, HEALTH, LUXURY, MARKETING, NON_PROFIT, NOT_SET, ORGANIZATIONS_AND_ASSOCIATIONS, OTHER, PROFESSIONAL_SERVICES, RESTAURANT, RETAIL, TECHNOLOGY, TELECOM, TRAVEL
    """
    params = {}
    if child_business_external_id is not None:
        params["child_business_external_id"] = child_business_external_id
    params["name"] = name
    if page_permitted_tasks is not None:
        params["page_permitted_tasks"] = page_permitted_tasks
    if sales_rep_email is not None:
        params["sales_rep_email"] = sales_rep_email
    if shared_page_id is not None:
        params["shared_page_id"] = shared_page_id
    if should_generate_name is not None:
        params["should_generate_name"] = should_generate_name
    if survey_business_type is not None:
        params["survey_business_type"] = survey_business_type
    if survey_num_assets is not None:
        params["survey_num_assets"] = survey_num_assets
    if survey_num_people is not None:
        params["survey_num_people"] = survey_num_people
    if timezone_id is not None:
        params["timezone_id"] = timezone_id
    params["vertical"] = vertical
    result = await get_client().post(f"{business_id}/owned_businesses", data=params)
    return json.dumps(result, indent=2)


async def get_business_owned_instagram_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_instagram_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_owned_instagram_assets(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_instagram_assets on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_instagram_assets", params=params)
    return json.dumps(result, indent=2)


async def get_business_owned_offsite_signal_container_business_objects(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_offsite_signal_container_business_objects on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_offsite_signal_container_business_objects", params=params)
    return json.dumps(result, indent=2)


async def get_business_owned_pages(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_pages on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_pages", params=params)
    return json.dumps(result, indent=2)


async def create_business_owned_pages(
    business_id: str,
    page_id: int,
    code: Optional[str] = None,
    entry_point: Optional[str] = None,
) -> str:
    """POST /owned_pages on Business.

    Args:
        business_id: The ID of the Business object.
        code: Optional.
        entry_point: Optional.
        page_id: Required.
    """
    params = {}
    if code is not None:
        params["code"] = code
    if entry_point is not None:
        params["entry_point"] = entry_point
    params["page_id"] = page_id
    result = await get_client().post(f"{business_id}/owned_pages", data=params)
    return json.dumps(result, indent=2)


async def get_business_owned_pixels(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_pixels on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_pixels", params=params)
    return json.dumps(result, indent=2)


async def get_business_owned_product_catalogs(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_product_catalogs on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def create_business_owned_product_catalogs(
    business_id: str,
    name: str,
    additional_vertical_option: Optional[str] = None,
    business_metadata: Optional[str] = None,
    catalog_segment_filter: Optional[str] = None,
    catalog_segment_product_set_id: Optional[str] = None,
    da_display_settings: Optional[str] = None,
    destination_catalog_settings: Optional[str] = None,
    flight_catalog_settings: Optional[str] = None,
    parent_catalog_id: Optional[str] = None,
    partner_integration: Optional[str] = None,
    store_catalog_settings: Optional[str] = None,
    vertical: Optional[str] = None,
) -> str:
    """POST /owned_product_catalogs on Business.

    Args:
        business_id: The ID of the Business object.
        additional_vertical_option: Optional. Values: LOCAL_DA_CATALOG, LOCAL_PRODUCTS
        business_metadata: Optional.
        catalog_segment_filter: Optional.
        catalog_segment_product_set_id: Optional.
        da_display_settings: Optional.
        destination_catalog_settings: Optional.
        flight_catalog_settings: Optional.
        name: Required.
        parent_catalog_id: Optional.
        partner_integration: Optional.
        store_catalog_settings: Optional.
        vertical: Optional. Values: adoptable_pets, commerce, destinations, flights, generic, home_listings, hotels, local_service_businesses, offer_items, offline_commerce, transactable_items, vehicles
    """
    params = {}
    if additional_vertical_option is not None:
        params["additional_vertical_option"] = additional_vertical_option
    if business_metadata is not None:
        params["business_metadata"] = business_metadata
    if catalog_segment_filter is not None:
        params["catalog_segment_filter"] = catalog_segment_filter
    if catalog_segment_product_set_id is not None:
        params["catalog_segment_product_set_id"] = catalog_segment_product_set_id
    if da_display_settings is not None:
        params["da_display_settings"] = da_display_settings
    if destination_catalog_settings is not None:
        params["destination_catalog_settings"] = destination_catalog_settings
    if flight_catalog_settings is not None:
        params["flight_catalog_settings"] = flight_catalog_settings
    params["name"] = name
    if parent_catalog_id is not None:
        params["parent_catalog_id"] = parent_catalog_id
    if partner_integration is not None:
        params["partner_integration"] = partner_integration
    if store_catalog_settings is not None:
        params["store_catalog_settings"] = store_catalog_settings
    if vertical is not None:
        params["vertical"] = vertical
    result = await get_client().post(f"{business_id}/owned_product_catalogs", data=params)
    return json.dumps(result, indent=2)


async def get_business_owned_whatsapp_business_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /owned_whatsapp_business_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/owned_whatsapp_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def delete_business_pages(business_id: str, page_id: int) -> str:
    """DELETE /pages on Business.

    Args:
        business_id: The ID of the Business object.
        page_id: Required.
    """
    params = {}
    params["page_id"] = page_id
    result = await get_client().delete(f"{business_id}/pages")
    return json.dumps(result, indent=2)


async def get_business_partner_account_linking(business_id: str, fields: Optional[str] = None) -> str:
    """GET /partner_account_linking on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/partner_account_linking", params=params)
    return json.dumps(result, indent=2)


async def create_business_partner_premium_options(
    business_id: str,
    enable_basket_insight: bool,
    enable_extended_audience_retargeting: bool,
    partner_business_id: str,
    retailer_custom_audience_config: str,
    catalog_segment_id: Optional[str] = None,
    vendor_id: Optional[str] = None,
) -> str:
    """POST /partner_premium_options on Business.

    Args:
        business_id: The ID of the Business object.
        catalog_segment_id: Optional.
        enable_basket_insight: Required.
        enable_extended_audience_retargeting: Required.
        partner_business_id: Required.
        retailer_custom_audience_config: Required.
        vendor_id: Optional.
    """
    params = {}
    if catalog_segment_id is not None:
        params["catalog_segment_id"] = catalog_segment_id
    params["enable_basket_insight"] = enable_basket_insight
    params["enable_extended_audience_retargeting"] = enable_extended_audience_retargeting
    params["partner_business_id"] = partner_business_id
    params["retailer_custom_audience_config"] = retailer_custom_audience_config
    if vendor_id is not None:
        params["vendor_id"] = vendor_id
    result = await get_client().post(f"{business_id}/partner_premium_options", data=params)
    return json.dumps(result, indent=2)


async def get_business_passback_attribution_metadata_configs(business_id: str, fields: Optional[str] = None) -> str:
    """GET /passback_attribution_metadata_configs on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/passback_attribution_metadata_configs", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_client_ad_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_client_ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_client_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_client_apps(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_client_apps on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_client_apps", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_client_pages(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_client_pages on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_client_pages", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_owned_ad_accounts(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_owned_ad_accounts on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_owned_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_owned_pages(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_owned_pages on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_owned_pages", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_shared_offsite_signal_container_business_objects(business_id: str, fields: Optional[str] = None) -> str:
    """GET /pending_shared_offsite_signal_container_business_objects on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/pending_shared_offsite_signal_container_business_objects", params=params)
    return json.dumps(result, indent=2)


async def get_business_pending_users(business_id: str, fields: Optional[str] = None, email: Optional[str] = None) -> str:
    """GET /pending_users on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        email: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if email is not None:
        params["email"] = email
    result = await get_client().get(f"{business_id}/pending_users", params=params)
    return json.dumps(result, indent=2)


async def get_business_picture(
    business_id: str,
    fields: Optional[str] = None,
    height: Optional[int] = None,
    redirect: Optional[bool] = None,
    type_: Optional[str] = None,
    width: Optional[int] = None,
) -> str:
    """GET /picture on Business.

    Args:
        business_id: The ID of the Business object.
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
    result = await get_client().get(f"{business_id}/picture", params=params)
    return json.dumps(result, indent=2)


async def create_business_pixel_tos(business_id: str) -> str:
    """POST /pixel_tos on Business.

    Args:
        business_id: The ID of the Business object.
    """
    params = {}
    result = await get_client().post(f"{business_id}/pixel_tos", data=params)
    return json.dumps(result, indent=2)


async def get_business_preverified_numbers(
    business_id: str,
    fields: Optional[str] = None,
    code_verification_status: Optional[str] = None,
    phone_number: Optional[str] = None,
) -> str:
    """GET /preverified_numbers on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        code_verification_status: Optional. Values: EXPIRED, NOT_VERIFIED, VERIFIED
        phone_number: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if code_verification_status is not None:
        params["code_verification_status"] = code_verification_status
    if phone_number is not None:
        params["phone_number"] = phone_number
    result = await get_client().get(f"{business_id}/preverified_numbers", params=params)
    return json.dumps(result, indent=2)


async def get_business_received_audience_sharing_requests(
    business_id: str,
    fields: Optional[str] = None,
    initiator_id: Optional[str] = None,
    request_status: Optional[str] = None,
) -> str:
    """GET /received_audience_sharing_requests on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        initiator_id: Optional.
        request_status: Optional. Values: APPROVE, CANCELED, DECLINE, EXPIRED, IN_PROGRESS, MMA_DIRECT_ASSETS_APPROVED, MMA_DIRECT_ASSETS_DECLINED, MMA_DIRECT_ASSETS_EXPIRED, MMA_DIRECT_ASSETS_PENDING, PENDING, PENDING_EMAIL_VERIFICATION, PENDING_INTEGRITY_REVIEW
    """
    params = {}
    params["fields"] = fields or "id,name"
    if initiator_id is not None:
        params["initiator_id"] = initiator_id
    if request_status is not None:
        params["request_status"] = request_status
    result = await get_client().get(f"{business_id}/received_audience_sharing_requests", params=params)
    return json.dumps(result, indent=2)


async def get_business_reseller_guidances(business_id: str, fields: Optional[str] = None) -> str:
    """GET /reseller_guidances on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/reseller_guidances", params=params)
    return json.dumps(result, indent=2)


async def get_business_self_certified_whatsapp_business_submissions(
    business_id: str,
    fields: Optional[str] = None,
    end_business_id: Optional[str] = None,
) -> str:
    """GET /self_certified_whatsapp_business_submissions on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
        end_business_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_business_id is not None:
        params["end_business_id"] = end_business_id
    result = await get_client().get(f"{business_id}/self_certified_whatsapp_business_submissions", params=params)
    return json.dumps(result, indent=2)


async def create_business_self_certify_whatsapp_business(
    business_id: str,
    business_documents: str,
    end_business_id: str,
    average_monthly_revenue_spend_with_partner: Optional[str] = None,
    business_vertical: Optional[str] = None,
    end_business_address: Optional[str] = None,
    end_business_legal_name: Optional[str] = None,
    end_business_trade_names: Optional[str] = None,
    end_business_website: Optional[str] = None,
    num_billing_cycles_with_partner: Optional[int] = None,
) -> str:
    """POST /self_certify_whatsapp_business on Business.

    Args:
        business_id: The ID of the Business object.
        average_monthly_revenue_spend_with_partner: Optional.
        business_documents: Required.
        business_vertical: Optional. Values: ADULT_PRODUCTS_AND_SERVICES, ALCOHOL_AND_TOBACCO, AUTOMOTIVE_DEALERS, BODY_PARTS_FLUIDS, BUSINESS_AND_UTILITY, CONTENT_AND_APPS, CREATORS_AND_CELEBRITIES, DATING, DRUGS, ENDANGERED_SPECIES, FIREARMS, FRAUDULENT_MISLEADING_OFFENSIVE, GAMBLING, GROCERY_AND_CONVENIENCE_STORE, HAZARDOUS_GOODS_AND_MATERIALS, HOME, HOME_AND_AUTO_MANUFACTURING, LIFESTYLE, LIVE_NON_ENDANGERED_SPECIES, LOANS_DEBT_COLLECTION_BAIL_BONDS, LOCAL_EVENTS, MEDICAL_HEALTHCARE, MULTILEVEL_MARKETING, NON_PROFIT_AND_RELIGIOUS_ORGS, PROFESSIONAL, REAL_VIRTUAL_FAKE_CURRENCY, RESTAURANTS, RETAIL, TRANSPORTATION_AND_ACCOMMODATION
        end_business_address: Optional.
        end_business_id: Required.
        end_business_legal_name: Optional.
        end_business_trade_names: Optional.
        end_business_website: Optional.
        num_billing_cycles_with_partner: Optional.
    """
    params = {}
    if average_monthly_revenue_spend_with_partner is not None:
        params["average_monthly_revenue_spend_with_partner"] = average_monthly_revenue_spend_with_partner
    params["business_documents"] = business_documents
    if business_vertical is not None:
        params["business_vertical"] = business_vertical
    if end_business_address is not None:
        params["end_business_address"] = end_business_address
    params["end_business_id"] = end_business_id
    if end_business_legal_name is not None:
        params["end_business_legal_name"] = end_business_legal_name
    if end_business_trade_names is not None:
        params["end_business_trade_names"] = end_business_trade_names
    if end_business_website is not None:
        params["end_business_website"] = end_business_website
    if num_billing_cycles_with_partner is not None:
        params["num_billing_cycles_with_partner"] = num_billing_cycles_with_partner
    result = await get_client().post(f"{business_id}/self_certify_whatsapp_business", data=params)
    return json.dumps(result, indent=2)


async def create_business_setup_managed_partner_adaccounts(
    business_id: str,
    credit_line_id: str,
    marketplace_business_id: str,
    subvertical_v2: str,
    vendor_id: str,
    vertical_v2: str,
) -> str:
    """POST /setup_managed_partner_adaccounts on Business.

    Args:
        business_id: The ID of the Business object.
        credit_line_id: Required.
        marketplace_business_id: Required.
        subvertical_v2: Required. Values: ACCOUNTING_AND_TAX, ACTIVITIES_AND_LEISURE, AIR, APPAREL_AND_ACCESSORIES, ARTS_AND_HERITAGE_AND_EDUCATION, AR_OR_VR_GAMING, AUDIO_STREAMING, AUTO, AUTO_INSURANCE, AUTO_RENTAL, BABY, BALLOT_INITIATIVE_OR_REFERENDUM, BEAUTY, BEAUTY_AND_FASHION, BEER_AND_WINE_AND_LIQUOR_AND_MALT_BEVERAGES, BOOKSTORES, BROADCAST_TELEVISION, BUSINESS_CONSULTANTS, BUYING_AGENCY, CABLE_AND_SATELLITE, CABLE_TELEVISION, CALL_CENTER_AND_MESSAGING_SERVICES, CANDIDATE_OR_POLITICIAN, CAREER, CAREER_AND_TECH, CASUAL_DINING, CHRONIC_CONDITIONS_AND_MEDICAL_CAUSES, CIVIC_INFLUENCERS, CLINICAL_TRIALS, COFFEE, COMPUTER_AND_SOFTWARE_AND_HARDWARE, CONSOLE_AND_CROSS_PLATFORM_GAMING, CONSULTING, CONSUMER_ELECTRONICS, COUNSELING_AND_PSYCHOTHERAPY, CREATIVE_AGENCY, CREDIT_AND_FINANCING_AND_MORTAGES, CRUISES_AND_MARINE, CULTURE_AND_LIFESTYLE, DATA_ANALYTICS_AND_DATA_MANAGEMENT, DATING_AND_TECHNOLOGY_APPS, DEPARTMENT_STORE, DESKTOP_SOFTWARE, DIETING_AND_FITNESS_PROGRAMS, DIGITAL_NATIVE_EDUCATION_OR_TRAINING, DRINKING_PLACES, EDUCATION_RESOURCES, ED_TECH, ELEARNING_AND_MASSIVE_ONLINE_OPEN_COURSES, ELECTION_COMMISSION, ELECTRONICS_AND_APPLIANCES, ENGINEERING_AND_DESIGN, ENVIRONMENT_AND_ANIMAL_WELFARE, ESPORTS, EVENTS, FARMING_AND_RANCHING, FILE_STORAGE_AND_CLOUD_AND_DATA_SERVICES, FINANCE, FIN_TECH, FISHING_AND_HUNTING_AND_FORESTRY_AND_LOGGING, FITNESS, FOOD, FOOTWEAR, FOR_PROFIT_COLLEGES_AND_UNIVERSITIES, FULL_SERVICE_AGENCY, GOVERNMENT_CONTROLLED_ENTITY, GOVERNMENT_DEPARTMENT_OR_AGENCY, GOVERNMENT_OFFICIAL, GOVERNMENT_OWNED_MEDIA, GROCERY_AND_DRUG_AND_CONVENIENCE, HEAD_OF_STATE, HEALTH_INSURANCE, HEALTH_SYSTEMS_AND_PRACTITIONERS, HEALTH_TECH, HOME_AND_FURNITURE_AND_OFFICE, HOME_IMPROVEMENT, HOME_INSURANCE, HOME_TECH, HOTEL_AND_ACCOMODATION, HOUSEHOLD_GOODS_DURABLE, HOUSEHOLD_GOODS_NON_DURABLE, HR_AND_FINANCIAL_MANAGEMENT, HUMANITARIAN_OR_DISASTER_RELIEF, INDEPENDENT_EXPENDITURE_GROUP, INSURANCE_TECH, INTERNATIONAL_ORGANIZATON, INVESTMENT_BANK_AND_BROKERAGE, ISSUE_ADVOCACY, LEGAL, LIFE_INSURANCE, LOGISTICS_AND_TRANSPORTATION_AND_FLEET_MANAGEMENT, MANUFACTURING, MEDICAL_DEVICES_AND_SUPPLIES_AND_EQUIPMENT, MEDSPA_AND_ELECTIVE_SURGERIES_AND_ALTERNATIVE_MEDICINE, MINING_AND_QUARRYING, MOBILE_GAMING, MOVIES, MUSEUMS_AND_PARKS_AND_LIBRARIES, MUSIC, NETWORK_SECURITY_PRODUCTS, NEWS_AND_CURRENT_EVENTS, NON_PRESCRIPTION, NOT_FOR_PROFIT_COLLEGES_AND_UNIVERSITIES, OFFICE, OFFICE_OR_BUSINESS_SUPPLIES, OIL_AND_GAS_AND_CONSUMABLE_FUEL, ONLINE_ONLY_PUBLICATIONS, PACKAGE_OR_FREIGHT_DELIVERY, PARTY_INDEPENDENT_EXPENDITURE_GROUP_US, PAYMENT_PROCESSING_AND_GATEWAY_SOLUTIONS, PC_GAMING, PEOPLE, PERSONAL_CARE, PET, PHOTOGRAPHY_AND_FILMING_SERVICES, PIZZA, PLANNING_AGENCY, POLITICAL_PARTY_OR_COMMITTEE, PRESCRIPTION, PROFESSIONAL_ASSOCIATIONS, PROPERTY_AND_CASUALTY, QUICK_SERVICE, RADIO, RAILROADS, REAL_ESTATE, REAL_MONEY_GAMING, RECREATIONAL, RELIGIOUS, RESELLER, RESIDENTIAL_AND_LONG_TERM_CARE_FACILITIES_AND_OUTPATIENT_CARE_CENTERS, RETAIL_AND_CREDIT_UNION_AND_COMMERCIAL_BANK, RIDE_SHARING_OR_TAXI_SERVICES, SAFETY_SERVICES, SCHOLARLY, SCHOOL_AND_EARLY_CHILDREN_EDCATION, SOCIAL_MEDIA, SOFTWARE_AS_A_SERVICE, SPORTING, SPORTING_AND_OUTDOOR, SPORTS, SUPERSTORES, T1_AUTOMOTIVE_MANUFACTURER, T1_MOTORCYCLE, T2_DEALER_ASSOCIATIONS, T3_AUTO_AGENCY, T3_AUTO_RESELLERS, T3_DEALER_GROUPS, T3_FRANCHISE_DEALER, T3_INDEPENDENT_DEALER, T3_PARTS_AND_SERVICES, T3_PORTALS, TELECOMMUNICATIONS_EQUIPMENT_AND_ACCESSORIES, TELEPHONE_SERVICE_PROVIDERS_AND_CARRIERS, TICKETING, TOBACCO, TOURISM_AND_TRAVEL_SERVICES, TOURISM_BOARD, TOY_AND_HOBBY, TRADE_SCHOOL, TRAVEL_AGENCIES_AND_GUIDES_AND_OTAS, UTILITIES_AND_ENERGY_EQUIPMENT_AND_SERVICES, VETERINARY_CLINICS_AND_SERVICES, VIDEO_STREAMING, VIRTUAL_SERVICES, VITAMINS_OR_WELLNESS, WAREHOUSING_AND_STORAGE, WATER_AND_SOFT_DRINK_AND_BAVERAGE, WEBSITE_DESIGNERS_OR_GRAPHIC_DESIGNERS, WHOLESALE, WIRELESS_SERVICES
        vendor_id: Required.
        vertical_v2: Required. Values: ADVERTISING_AND_MARKETING, AGRICULTURE, AUTOMOTIVE, BANKING_AND_CREDIT_CARDS, BUSINESS_TO_BUSINESS, CONSUMER_PACKAGED_GOODS, ECOMMERCE, EDUCATION, ENERGY_AND_NATURAL_RESOURCES_AND_UTILITIES, ENTERTAINMENT_AND_MEDIA, GAMING, GOVERNMENT, HEALTHCARE_AND_PHARMACEUTICALS_AND_BIOTECH, INSURANCE, NON_PROFIT, ORGANIZATIONS_AND_ASSOCIATIONS, POLITICS, PROFESSIONAL_SERVICES, PUBLISHING, RESTAURANTS, RETAIL, TECHNOLOGY, TELECOM, TRAVEL
    """
    params = {}
    params["credit_line_id"] = credit_line_id
    params["marketplace_business_id"] = marketplace_business_id
    params["subvertical_v2"] = subvertical_v2
    params["vendor_id"] = vendor_id
    params["vertical_v2"] = vertical_v2
    result = await get_client().post(f"{business_id}/setup_managed_partner_adaccounts", data=params)
    return json.dumps(result, indent=2)


async def delete_business_share_preverified_numbers(business_id: str, partner_business_id: str, preverified_id: str) -> str:
    """DELETE /share_preverified_numbers on Business.

    Args:
        business_id: The ID of the Business object.
        partner_business_id: Required.
        preverified_id: Required.
    """
    params = {}
    params["partner_business_id"] = partner_business_id
    params["preverified_id"] = preverified_id
    result = await get_client().delete(f"{business_id}/share_preverified_numbers")
    return json.dumps(result, indent=2)


async def create_business_share_preverified_numbers(business_id: str, partner_business_id: str, preverified_id: str) -> str:
    """POST /share_preverified_numbers on Business.

    Args:
        business_id: The ID of the Business object.
        partner_business_id: Required.
        preverified_id: Required.
    """
    params = {}
    params["partner_business_id"] = partner_business_id
    params["preverified_id"] = preverified_id
    result = await get_client().post(f"{business_id}/share_preverified_numbers", data=params)
    return json.dumps(result, indent=2)


async def create_business_system_user_access_tokens(
    business_id: str,
    asset: Optional[str] = None,
    fetch_only: Optional[bool] = None,
    scope: Optional[str] = None,
    set_token_expires_in_60_days: Optional[bool] = None,
    system_user_id: Optional[int] = None,
) -> str:
    """POST /system_user_access_tokens on Business.

    Args:
        business_id: The ID of the Business object.
        asset: Optional.
        fetch_only: Optional.
        scope: Optional.
        set_token_expires_in_60_days: Optional.
        system_user_id: Optional.
    """
    params = {}
    if asset is not None:
        params["asset"] = asset
    if fetch_only is not None:
        params["fetch_only"] = fetch_only
    if scope is not None:
        params["scope"] = scope
    if set_token_expires_in_60_days is not None:
        params["set_token_expires_in_60_days"] = set_token_expires_in_60_days
    if system_user_id is not None:
        params["system_user_id"] = system_user_id
    result = await get_client().post(f"{business_id}/system_user_access_tokens", data=params)
    return json.dumps(result, indent=2)


async def get_business_system_users(business_id: str, fields: Optional[str] = None) -> str:
    """GET /system_users on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/system_users", params=params)
    return json.dumps(result, indent=2)


async def create_business_system_users(
    business_id: str,
    name: str,
    role: Optional[str] = None,
    system_user_id: Optional[int] = None,
) -> str:
    """POST /system_users on Business.

    Args:
        business_id: The ID of the Business object.
        name: Required.
        role: Optional. Values: ADMIN, ADS_RIGHTS_REVIEWER, DEFAULT, DEVELOPER, EMPLOYEE, FINANCE_ANALYST, FINANCE_EDIT, FINANCE_EDITOR, FINANCE_VIEW, MANAGE, PARTNER_CENTER_ADMIN, PARTNER_CENTER_ANALYST, PARTNER_CENTER_EDUCATION, PARTNER_CENTER_MARKETING, PARTNER_CENTER_OPERATIONS
        system_user_id: Optional.
    """
    params = {}
    params["name"] = name
    if role is not None:
        params["role"] = role
    if system_user_id is not None:
        params["system_user_id"] = system_user_id
    result = await get_client().post(f"{business_id}/system_users", data=params)
    return json.dumps(result, indent=2)


async def get_business_third_party_measurement_report_dataset(business_id: str, fields: Optional[str] = None) -> str:
    """GET /third_party_measurement_report_dataset on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}/third_party_measurement_report_dataset", params=params)
    return json.dumps(result, indent=2)


async def create_business_videos(
    business_id: str,
    creative_folder_id: str,
    ad_placements_validation_only: Optional[bool] = None,
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
    validation_ad_placements: Optional[str] = None,
    video_file_chunk: Optional[str] = None,
    video_id_original: Optional[str] = None,
    video_start_time_ms: Optional[int] = None,
    waterfall_id: Optional[str] = None,
) -> str:
    """POST /videos on Business.

    Args:
        business_id: The ID of the Business object.
        ad_placements_validation_only: Optional.
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
        creative_folder_id: Required.
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
        validation_ad_placements: Optional. Values: AUDIENCE_NETWORK_INSTREAM_VIDEO, AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE, AUDIENCE_NETWORK_REWARDED_VIDEO, DESKTOP_FEED_STANDARD, FACEBOOK_STORY_MOBILE, FACEBOOK_STORY_STICKER_MOBILE, INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTANT_ARTICLE_STANDARD, INSTREAM_BANNER_DESKTOP, INSTREAM_BANNER_MOBILE, INSTREAM_VIDEO_DESKTOP, INSTREAM_VIDEO_IMAGE, INSTREAM_VIDEO_MOBILE, MESSENGER_MOBILE_INBOX_MEDIA, MESSENGER_MOBILE_STORY_MEDIA, MOBILE_FEED_STANDARD, MOBILE_FULLWIDTH, MOBILE_INTERSTITIAL, MOBILE_MEDIUM_RECTANGLE, MOBILE_NATIVE, RIGHT_COLUMN_STANDARD, SUGGESTED_VIDEO_MOBILE
        video_file_chunk: Optional.
        video_id_original: Optional.
        video_start_time_ms: Optional.
        waterfall_id: Optional.
    """
    params = {}
    if ad_placements_validation_only is not None:
        params["ad_placements_validation_only"] = ad_placements_validation_only
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
    params["creative_folder_id"] = creative_folder_id
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
    if validation_ad_placements is not None:
        params["validation_ad_placements"] = validation_ad_placements
    if video_file_chunk is not None:
        params["video_file_chunk"] = video_file_chunk
    if video_id_original is not None:
        params["video_id_original"] = video_id_original
    if video_start_time_ms is not None:
        params["video_start_time_ms"] = video_start_time_ms
    if waterfall_id is not None:
        params["waterfall_id"] = waterfall_id
    result = await get_client().post(f"{business_id}/videos", data=params)
    return json.dumps(result, indent=2)


async def get_business(business_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Business.

    Args:
        business_id: The ID of the Business object.
        fields: Comma-separated list of fields to return. Available: block_offline_analytics, collaborative_ads_managed_partner_business_info, collaborative_ads_managed_partner_eligibility, collaborative_ads_partner_premium_options, created_by, created_time, extended_updated_time, id, is_hidden, link, marketing_messages_onboarding_status, name, payment_account_id, primary_page, profile_picture_uri, timezone_id, two_factor_type, updated_by, updated_time, user_access_expire_time, verification_status, vertical, vertical_id, whatsapp_business_manager_messaging_limit
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business(
    business_id: str,
    entry_point: Optional[str] = None,
    name: Optional[str] = None,
    primary_page: Optional[str] = None,
    timezone_id: Optional[int] = None,
    two_factor_type: Optional[str] = None,
    vertical: Optional[str] = None,
) -> str:
    """POST /#update on Business.

    Args:
        business_id: The ID of the Business object.
        entry_point: Optional.
        name: Optional.
        primary_page: Optional.
        timezone_id: Optional.
        two_factor_type: Optional.
        vertical: Optional.
    """
    params = {}
    if entry_point is not None:
        params["entry_point"] = entry_point
    if name is not None:
        params["name"] = name
    if primary_page is not None:
        params["primary_page"] = primary_page
    if timezone_id is not None:
        params["timezone_id"] = timezone_id
    if two_factor_type is not None:
        params["two_factor_type"] = two_factor_type
    if vertical is not None:
        params["vertical"] = vertical
    result = await get_client().post(f"{business_id}", data=params)
    return json.dumps(result, indent=2)


BUSINESS_USER_FIELDS = [
    "business",
    "business_role_request",
    "email",
    "finance_permission",
    "first_name",
    "id",
    "ip_permission",
    "last_name",
    "marked_for_removal",
    "name",
    "pending_email",
    "role",
    "tasks",
    "title",
    "two_fac_status"
]


async def get_business_user_assigned_ad_accounts(business_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_ad_accounts on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_user_id}/assigned_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_business_user_assigned_business_asset_groups(
    business_user_id: str,
    fields: Optional[str] = None,
    contained_asset_id: Optional[str] = None,
) -> str:
    """GET /assigned_business_asset_groups on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return.
        contained_asset_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if contained_asset_id is not None:
        params["contained_asset_id"] = contained_asset_id
    result = await get_client().get(f"{business_user_id}/assigned_business_asset_groups", params=params)
    return json.dumps(result, indent=2)


async def get_business_user_assigned_pages(business_user_id: str, fields: Optional[str] = None, pages: Optional[str] = None) -> str:
    """GET /assigned_pages on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return.
        pages: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if pages is not None:
        params["pages"] = pages
    result = await get_client().get(f"{business_user_id}/assigned_pages", params=params)
    return json.dumps(result, indent=2)


async def get_business_user_assigned_product_catalogs(business_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_product_catalogs on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_user_id}/assigned_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_business_user_assigned_whatsapp_business_accounts(business_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_whatsapp_business_accounts on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_user_id}/assigned_whatsapp_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def delete_business_user(business_user_id: str) -> str:
    """DELETE /#delete on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
    """
    params = {}
    result = await get_client().delete(f"{business_user_id}")
    return json.dumps(result, indent=2)


async def get_business_user(business_user_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        fields: Comma-separated list of fields to return. Available: business, business_role_request, email, finance_permission, first_name, id, ip_permission, last_name, marked_for_removal, name, pending_email, role, tasks, title, two_fac_status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_user_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business_user(
    business_user_id: str,
    clear_pending_email: Optional[bool] = None,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    pending_email: Optional[str] = None,
    role: Optional[str] = None,
    skip_verification_email: Optional[bool] = None,
    tasks: Optional[str] = None,
    title: Optional[str] = None,
) -> str:
    """POST /#update on BusinessUser.

    Args:
        business_user_id: The ID of the BusinessUser object.
        clear_pending_email: Optional.
        email: Optional.
        first_name: Optional.
        last_name: Optional.
        pending_email: Optional.
        role: Optional.
        skip_verification_email: Optional.
        tasks: Optional.
        title: Optional.
    """
    params = {}
    if clear_pending_email is not None:
        params["clear_pending_email"] = clear_pending_email
    if email is not None:
        params["email"] = email
    if first_name is not None:
        params["first_name"] = first_name
    if last_name is not None:
        params["last_name"] = last_name
    if pending_email is not None:
        params["pending_email"] = pending_email
    if role is not None:
        params["role"] = role
    if skip_verification_email is not None:
        params["skip_verification_email"] = skip_verification_email
    if tasks is not None:
        params["tasks"] = tasks
    if title is not None:
        params["title"] = title
    result = await get_client().post(f"{business_user_id}", data=params)
    return json.dumps(result, indent=2)


BUSINESS_ASSET_GROUP_FIELDS = [
    "id",
    "name",
    "owner_business"
]


async def delete_business_asset_group_assigned_users(business_asset_group_id: str, user: int) -> str:
    """DELETE /assigned_users on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{business_asset_group_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_business_asset_group_assigned_users(business_asset_group_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{business_asset_group_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_assigned_users(
    business_asset_group_id: str,
    user: int,
    adaccount_tasks: Optional[str] = None,
    offline_conversion_data_set_tasks: Optional[str] = None,
    page_tasks: Optional[str] = None,
    pixel_tasks: Optional[str] = None,
) -> str:
    """POST /assigned_users on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        adaccount_tasks: Optional. Values: AA_ANALYZE, ADVERTISE, ANALYZE, DRAFT, MANAGE
        offline_conversion_data_set_tasks: Optional. Values: AA_ANALYZE, ADVERTISE, MANAGE, UPLOAD, VIEW
        page_tasks: Optional. Values: ADVERTISE, ANALYZE, CASHIER_ROLE, CREATE_CONTENT, GLOBAL_STRUCTURE_MANAGEMENT, MANAGE, MANAGE_JOBS, MANAGE_LEADS, MESSAGING, MODERATE, MODERATE_COMMUNITY, PAGES_MESSAGING, PAGES_MESSAGING_SUBSCRIPTIONS, PROFILE_PLUS_ADVERTISE, PROFILE_PLUS_ANALYZE, PROFILE_PLUS_CREATE_CONTENT, PROFILE_PLUS_FACEBOOK_ACCESS, PROFILE_PLUS_FULL_CONTROL, PROFILE_PLUS_GLOBAL_STRUCTURE_MANAGEMENT, PROFILE_PLUS_MANAGE, PROFILE_PLUS_MANAGE_LEADS, PROFILE_PLUS_MESSAGING, PROFILE_PLUS_MODERATE, PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY, PROFILE_PLUS_REVENUE, READ_PAGE_MAILBOXES, VIEW_MONETIZATION_INSIGHTS
        pixel_tasks: Optional. Values: AA_ANALYZE, ADVERTISE, ANALYZE, EDIT, UPLOAD
        user: Required.
    """
    params = {}
    if adaccount_tasks is not None:
        params["adaccount_tasks"] = adaccount_tasks
    if offline_conversion_data_set_tasks is not None:
        params["offline_conversion_data_set_tasks"] = offline_conversion_data_set_tasks
    if page_tasks is not None:
        params["page_tasks"] = page_tasks
    if pixel_tasks is not None:
        params["pixel_tasks"] = pixel_tasks
    params["user"] = user
    result = await get_client().post(f"{business_asset_group_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_adaccounts(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_adaccounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_adaccounts")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_adaccounts(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_adaccounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_adaccounts", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_adaccounts(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_adaccounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_adaccounts", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_applications(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_applications on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_applications")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_applications(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_applications on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_applications", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_applications(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_applications on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_applications", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_custom_conversions(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_custom_conversions on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_custom_conversions")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_custom_conversions(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_custom_conversions on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_custom_conversions", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_custom_conversions(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_custom_conversions on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_custom_conversions", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_instagram_accounts(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_instagram_accounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_instagram_accounts")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_instagram_accounts(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_instagram_accounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_instagram_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_instagram_accounts(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_instagram_accounts on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_instagram_accounts", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_pages(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_pages on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_pages")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_pages(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_pages on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_pages", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_pages(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_pages on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_pages", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_pixels(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_pixels on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_pixels")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_pixels(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_pixels on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_pixels", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_pixels(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_pixels on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_pixels", data=params)
    return json.dumps(result, indent=2)


async def delete_business_asset_group_contained_product_catalogs(business_asset_group_id: str, asset_id: str) -> str:
    """DELETE /contained_product_catalogs on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().delete(f"{business_asset_group_id}/contained_product_catalogs")
    return json.dumps(result, indent=2)


async def get_business_asset_group_contained_product_catalogs(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /contained_product_catalogs on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}/contained_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def create_business_asset_group_contained_product_catalogs(business_asset_group_id: str, asset_id: str) -> str:
    """POST /contained_product_catalogs on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        asset_id: Required.
    """
    params = {}
    params["asset_id"] = asset_id
    result = await get_client().post(f"{business_asset_group_id}/contained_product_catalogs", data=params)
    return json.dumps(result, indent=2)


async def get_business_asset_group(business_asset_group_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        fields: Comma-separated list of fields to return. Available: id, name, owner_business
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_group_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business_asset_group(business_asset_group_id: str, name: Optional[str] = None) -> str:
    """POST /#update on BusinessAssetGroup.

    Args:
        business_asset_group_id: The ID of the BusinessAssetGroup object.
        name: Optional.
    """
    params = {}
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"{business_asset_group_id}", data=params)
    return json.dumps(result, indent=2)


SYSTEM_USER_FIELDS = [
    "created_by",
    "created_time",
    "finance_permission",
    "id",
    "ip_permission",
    "name"
]


async def get_system_user_assigned_ad_accounts(system_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_ad_accounts on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{system_user_id}/assigned_ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_system_user_assigned_business_asset_groups(
    system_user_id: str,
    fields: Optional[str] = None,
    contained_asset_id: Optional[str] = None,
) -> str:
    """GET /assigned_business_asset_groups on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return.
        contained_asset_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if contained_asset_id is not None:
        params["contained_asset_id"] = contained_asset_id
    result = await get_client().get(f"{system_user_id}/assigned_business_asset_groups", params=params)
    return json.dumps(result, indent=2)


async def get_system_user_assigned_pages(system_user_id: str, fields: Optional[str] = None, pages: Optional[str] = None) -> str:
    """GET /assigned_pages on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return.
        pages: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if pages is not None:
        params["pages"] = pages
    result = await get_client().get(f"{system_user_id}/assigned_pages", params=params)
    return json.dumps(result, indent=2)


async def get_system_user_assigned_product_catalogs(system_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_product_catalogs on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{system_user_id}/assigned_product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_system_user_assigned_whatsapp_business_accounts(system_user_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_whatsapp_business_accounts on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{system_user_id}/assigned_whatsapp_business_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_system_user(system_user_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on SystemUser.

    Args:
        system_user_id: The ID of the SystemUser object.
        fields: Comma-separated list of fields to return. Available: created_by, created_time, finance_permission, id, ip_permission, name
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{system_user_id}", params=params)
    return json.dumps(result, indent=2)


BUSINESS_ROLE_REQUEST_FIELDS = [
    "created_by",
    "created_time",
    "email",
    "expiration_time",
    "expiry_time",
    "finance_role",
    "id",
    "invite_link",
    "invited_user_type",
    "ip_role",
    "owner",
    "role",
    "status",
    "tasks",
    "updated_by",
    "updated_time"
]


async def delete_business_role_request(business_role_request_id: str) -> str:
    """DELETE /#delete on BusinessRoleRequest.

    Args:
        business_role_request_id: The ID of the BusinessRoleRequest object.
    """
    params = {}
    result = await get_client().delete(f"{business_role_request_id}")
    return json.dumps(result, indent=2)


async def get_business_role_request(business_role_request_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BusinessRoleRequest.

    Args:
        business_role_request_id: The ID of the BusinessRoleRequest object.
        fields: Comma-separated list of fields to return. Available: created_by, created_time, email, expiration_time, expiry_time, finance_role, id, invite_link, invited_user_type, ip_role, owner, role, status, tasks, updated_by, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_role_request_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business_role_request(
    business_role_request_id: str,
    role: Optional[str] = None,
    tasks: Optional[str] = None,
) -> str:
    """POST /#update on BusinessRoleRequest.

    Args:
        business_role_request_id: The ID of the BusinessRoleRequest object.
        role: Optional.
        tasks: Optional.
    """
    params = {}
    if role is not None:
        params["role"] = role
    if tasks is not None:
        params["tasks"] = tasks
    result = await get_client().post(f"{business_role_request_id}", data=params)
    return json.dumps(result, indent=2)


BUSINESS_AGREEMENT_FIELDS = [
    "id",
    "request_status"
]


async def get_business_agreement(business_agreement_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BusinessAgreement.

    Args:
        business_agreement_id: The ID of the BusinessAgreement object.
        fields: Comma-separated list of fields to return. Available: id, request_status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_agreement_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business_agreement(
    business_agreement_id: str,
    asset_id: Optional[int] = None,
    request_status: Optional[str] = None,
) -> str:
    """POST /#update on BusinessAgreement.

    Args:
        business_agreement_id: The ID of the BusinessAgreement object.
        asset_id: Optional.
        request_status: Optional.
    """
    params = {}
    if asset_id is not None:
        params["asset_id"] = asset_id
    if request_status is not None:
        params["request_status"] = request_status
    result = await get_client().post(f"{business_agreement_id}", data=params)
    return json.dumps(result, indent=2)


BUSINESS_ASSET_SHARING_AGREEMENT_FIELDS = [
    "id",
    "initiator",
    "recipient",
    "relationship_type",
    "request_status",
    "request_type"
]


async def get_business_asset_sharing_agreement(business_asset_sharing_agreement_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BusinessAssetSharingAgreement.

    Args:
        business_asset_sharing_agreement_id: The ID of the BusinessAssetSharingAgreement object.
        fields: Comma-separated list of fields to return. Available: id, initiator, recipient, relationship_type, request_status, request_type
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{business_asset_sharing_agreement_id}", params=params)
    return json.dumps(result, indent=2)


async def update_business_asset_sharing_agreement(business_asset_sharing_agreement_id: str, request_response: Optional[str] = None) -> str:
    """POST /#update on BusinessAssetSharingAgreement.

    Args:
        business_asset_sharing_agreement_id: The ID of the BusinessAssetSharingAgreement object.
        request_response: Optional.
    """
    params = {}
    if request_response is not None:
        params["request_response"] = request_response
    result = await get_client().post(f"{business_asset_sharing_agreement_id}", data=params)
    return json.dumps(result, indent=2)

