"""Auto-generated Meta Marketing API tools — whatsapp."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


WHATS_APP_BUSINESS_ACCOUNT_FIELDS = [
    "account_review_status",
    "analytics",
    "auth_international_rate_eligibility",
    "business_verification_status",
    "country",
    "creation_time",
    "currency",
    "health_status",
    "id",
    "is_enabled_for_insights",
    "is_shared_with_partners",
    "linked_commerce_account",
    "marketing_messages_lite_api_status",
    "marketing_messages_onboarding_status",
    "message_template_namespace",
    "name",
    "on_behalf_of_business_info",
    "owner_business",
    "owner_business_info",
    "ownership_type",
    "primary_business_location",
    "primary_funding_id",
    "purchase_order_number",
    "status",
    "timezone_id",
    "whatsapp_business_manager_messaging_limit"
]


async def delete_whats_app_business_account_assigned_users(whats_app_business_account_id: str, user: int) -> str:
    """DELETE /assigned_users on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{whats_app_business_account_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_assigned_users(whats_app_business_account_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{whats_app_business_account_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_assigned_users(whats_app_business_account_id: str, tasks: str, user: int) -> str:
    """POST /assigned_users on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        tasks: Required. Values: DEVELOP, MANAGE, MANAGE_EXTENSIONS, MANAGE_PHONE, MANAGE_PHONE_ASSETS, MANAGE_TEMPLATES, MESSAGING, VIEW_COST, VIEW_PHONE_ASSETS, VIEW_TEMPLATES
        user: Required.
    """
    params = {}
    params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"{whats_app_business_account_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_audiences(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /audiences on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/audiences", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_call_analytics(
    whats_app_business_account_id: str,
    end: int,
    granularity: str,
    start: int,
    fields: Optional[str] = None,
    country_codes: Optional[str] = None,
    dimensions: Optional[str] = None,
    directions: Optional[str] = None,
    metric_types: Optional[str] = None,
    phone_numbers: Optional[str] = None,
    tiers: Optional[str] = None,
) -> str:
    """GET /call_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        country_codes: Optional.
        dimensions: Optional. Values: COUNTRY, DIRECTION, PHONE, TIER, UNKNOWN
        directions: Optional. Values: BUSINESS_INITIATED, UNKNOWN, USER_INITIATED
        end: Required.
        granularity: Required. Values: DAILY, HALF_HOUR, MONTHLY
        metric_types: Optional. Values: AVERAGE_DURATION, COST, COUNT, UNKNOWN
        phone_numbers: Optional.
        start: Required.
        tiers: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if country_codes is not None:
        params["country_codes"] = country_codes
    if dimensions is not None:
        params["dimensions"] = dimensions
    if directions is not None:
        params["directions"] = directions
    params["end"] = end
    params["granularity"] = granularity
    if metric_types is not None:
        params["metric_types"] = metric_types
    if phone_numbers is not None:
        params["phone_numbers"] = phone_numbers
    params["start"] = start
    if tiers is not None:
        params["tiers"] = tiers
    result = await get_client().get(f"{whats_app_business_account_id}/call_analytics", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_conversation_analytics(
    whats_app_business_account_id: str,
    end: int,
    granularity: str,
    start: int,
    fields: Optional[str] = None,
    conversation_categories: Optional[str] = None,
    conversation_directions: Optional[str] = None,
    conversation_types: Optional[str] = None,
    country_codes: Optional[str] = None,
    dimensions: Optional[str] = None,
    metric_types: Optional[str] = None,
    phone_numbers: Optional[str] = None,
) -> str:
    """GET /conversation_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        conversation_categories: Optional. Values: AUTHENTICATION, AUTHENTICATION_INTERNATIONAL, MARKETING, MARKETING_LITE, SERVICE, UTILITY
        conversation_directions: Optional. Values: BUSINESS_INITIATED, UNKNOWN, USER_INITIATED
        conversation_types: Optional. Values: FREE_ENTRY_POINT, FREE_TIER, REGULAR, UNKNOWN
        country_codes: Optional.
        dimensions: Optional. Values: CONVERSATION_CATEGORY, CONVERSATION_DIRECTION, CONVERSATION_TYPE, COUNTRY, PHONE, UNKNOWN
        end: Required.
        granularity: Required. Values: DAILY, HALF_HOUR, MONTHLY
        metric_types: Optional. Values: CONVERSATION, COST, UNKNOWN
        phone_numbers: Optional.
        start: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if conversation_categories is not None:
        params["conversation_categories"] = conversation_categories
    if conversation_directions is not None:
        params["conversation_directions"] = conversation_directions
    if conversation_types is not None:
        params["conversation_types"] = conversation_types
    if country_codes is not None:
        params["country_codes"] = country_codes
    if dimensions is not None:
        params["dimensions"] = dimensions
    params["end"] = end
    params["granularity"] = granularity
    if metric_types is not None:
        params["metric_types"] = metric_types
    if phone_numbers is not None:
        params["phone_numbers"] = phone_numbers
    params["start"] = start
    result = await get_client().get(f"{whats_app_business_account_id}/conversation_analytics", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_dataset(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /dataset on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/dataset", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_dataset(whats_app_business_account_id: str, dataset_name: Optional[str] = None) -> str:
    """POST /dataset on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        dataset_name: Optional.
    """
    params = {}
    if dataset_name is not None:
        params["dataset_name"] = dataset_name
    result = await get_client().post(f"{whats_app_business_account_id}/dataset", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_degrees_of_freedom_spec(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /degrees_of_freedom_spec on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/degrees_of_freedom_spec", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_flows(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /flows on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/flows", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_flows(
    whats_app_business_account_id: str,
    categories: str,
    name: str,
    clone_flow_id: Optional[str] = None,
    endpoint_uri: Optional[str] = None,
    flow_json: Optional[str] = None,
    publish: Optional[bool] = None,
) -> str:
    """POST /flows on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        categories: Required. Values: APPOINTMENT_BOOKING, CONTACT_US, CUSTOMER_SUPPORT, LEAD_GENERATION, OTHER, SHOPPING, SIGN_IN, SIGN_UP, SURVEY
        clone_flow_id: Optional.
        endpoint_uri: Optional.
        flow_json: Optional.
        name: Required.
        publish: Optional.
    """
    params = {}
    params["categories"] = categories
    if clone_flow_id is not None:
        params["clone_flow_id"] = clone_flow_id
    if endpoint_uri is not None:
        params["endpoint_uri"] = endpoint_uri
    if flow_json is not None:
        params["flow_json"] = flow_json
    params["name"] = name
    if publish is not None:
        params["publish"] = publish
    result = await get_client().post(f"{whats_app_business_account_id}/flows", data=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_generate_payment_configuration_oauth_link(
    whats_app_business_account_id: str,
    configuration_name: str,
    redirect_url: Optional[str] = None,
) -> str:
    """POST /generate_payment_configuration_oauth_link on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        configuration_name: Required.
        redirect_url: Optional.
    """
    params = {}
    params["configuration_name"] = configuration_name
    if redirect_url is not None:
        params["redirect_url"] = redirect_url
    result = await get_client().post(f"{whats_app_business_account_id}/generate_payment_configuration_oauth_link", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_group_analytics(
    whats_app_business_account_id: str,
    end: str,
    group_ids: str,
    start: str,
    fields: Optional[str] = None,
    granularity: Optional[str] = None,
    metric_types: Optional[str] = None,
) -> str:
    """GET /group_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        end: Required.
        granularity: Optional. Values: DAILY
        group_ids: Required.
        metric_types: Optional. Values: CLICKS, COST, DELIVERED, PARTICIPANTS_JOINED, PARTICIPANTS_LEFT, READ, REPLIES, SENT
        start: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["end"] = end
    if granularity is not None:
        params["granularity"] = granularity
    params["group_ids"] = group_ids
    if metric_types is not None:
        params["metric_types"] = metric_types
    params["start"] = start
    result = await get_client().get(f"{whats_app_business_account_id}/group_analytics", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_marketing_campaigns(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /marketing_campaigns on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/marketing_campaigns", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_message_campaigns(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /message_campaigns on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/message_campaigns", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_message_samples(
    whats_app_business_account_id: str,
    type_: str,
    interactive: Optional[str] = None,
    text: Optional[str] = None,
) -> str:
    """POST /message_samples on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        interactive: Optional.
        text: Optional.
        type_: Required. Values: INTERACTIVE, TEXT
    """
    params = {}
    if interactive is not None:
        params["interactive"] = interactive
    if text is not None:
        params["text"] = text
    params["type"] = type_
    result = await get_client().post(f"{whats_app_business_account_id}/message_samples", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_message_template_previews(
    whats_app_business_account_id: str,
    category: str,
    fields: Optional[str] = None,
    add_security_recommendation: Optional[bool] = None,
    business_name: Optional[str] = None,
    button_types: Optional[str] = None,
    code_expiration_minutes: Optional[int] = None,
    languages: Optional[str] = None,
) -> str:
    """GET /message_template_previews on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        add_security_recommendation: Optional.
        business_name: Optional.
        button_types: Optional. Values: OTP
        category: Required. Values: AUTHENTICATION
        code_expiration_minutes: Optional.
        languages: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if add_security_recommendation is not None:
        params["add_security_recommendation"] = add_security_recommendation
    if business_name is not None:
        params["business_name"] = business_name
    if button_types is not None:
        params["button_types"] = button_types
    params["category"] = category
    if code_expiration_minutes is not None:
        params["code_expiration_minutes"] = code_expiration_minutes
    if languages is not None:
        params["languages"] = languages
    result = await get_client().get(f"{whats_app_business_account_id}/message_template_previews", params=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_account_message_templates(whats_app_business_account_id: str, name: str, hsm_id: Optional[str] = None) -> str:
    """DELETE /message_templates on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        hsm_id: Optional.
        name: Required.
    """
    params = {}
    if hsm_id is not None:
        params["hsm_id"] = hsm_id
    params["name"] = name
    result = await get_client().delete(f"{whats_app_business_account_id}/message_templates")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_message_templates(
    whats_app_business_account_id: str,
    fields: Optional[str] = None,
    category: Optional[str] = None,
    content: Optional[str] = None,
    language: Optional[str] = None,
    name: Optional[str] = None,
    name_or_content: Optional[str] = None,
    quality_score: Optional[str] = None,
    source: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """GET /message_templates on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        category: Optional. Values: AUTHENTICATION, MARKETING, UTILITY
        content: Optional.
        language: Optional.
        name: Optional.
        name_or_content: Optional.
        quality_score: Optional. Values: GREEN, RED, UNKNOWN, YELLOW
        source: Optional. Values: AUTO_GENERATED, MANUAL
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
    if quality_score is not None:
        params["quality_score"] = quality_score
    if source is not None:
        params["source"] = source
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{whats_app_business_account_id}/message_templates", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_message_templates(
    whats_app_business_account_id: str,
    category: str,
    language: str,
    name: str,
    allow_category_change: Optional[bool] = None,
    bid_spec: Optional[str] = None,
    components: Optional[str] = None,
    creative_sourcing_spec: Optional[str] = None,
    cta_url_link_tracking_opted_out: Optional[bool] = None,
    degrees_of_freedom_spec: Optional[str] = None,
    display_format: Optional[str] = None,
    library_template_body_inputs: Optional[str] = None,
    library_template_button_inputs: Optional[str] = None,
    library_template_name: Optional[str] = None,
    message_send_ttl_seconds: Optional[int] = None,
    parameter_format: Optional[str] = None,
    send_type: Optional[str] = None,
    sub_category: Optional[str] = None,
) -> str:
    """POST /message_templates on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        allow_category_change: Optional.
        bid_spec: Optional.
        category: Required. Values: AUTHENTICATION, MARKETING, UTILITY
        components: Optional.
        creative_sourcing_spec: Optional.
        cta_url_link_tracking_opted_out: Optional.
        degrees_of_freedom_spec: Optional.
        display_format: Optional. Values: ORDER_DETAILS
        language: Required.
        library_template_body_inputs: Optional.
        library_template_button_inputs: Optional.
        library_template_name: Optional.
        message_send_ttl_seconds: Optional.
        name: Required.
        parameter_format: Optional. Values: NAMED, POSITIONAL
        send_type: Optional. Values: CAMPAIGN, DIRECT
        sub_category: Optional. Values: ORDER_DETAILS, ORDER_STATUS, RICH_ORDER_STATUS
    """
    params = {}
    if allow_category_change is not None:
        params["allow_category_change"] = allow_category_change
    if bid_spec is not None:
        params["bid_spec"] = bid_spec
    params["category"] = category
    if components is not None:
        params["components"] = components
    if creative_sourcing_spec is not None:
        params["creative_sourcing_spec"] = creative_sourcing_spec
    if cta_url_link_tracking_opted_out is not None:
        params["cta_url_link_tracking_opted_out"] = cta_url_link_tracking_opted_out
    if degrees_of_freedom_spec is not None:
        params["degrees_of_freedom_spec"] = degrees_of_freedom_spec
    if display_format is not None:
        params["display_format"] = display_format
    params["language"] = language
    if library_template_body_inputs is not None:
        params["library_template_body_inputs"] = library_template_body_inputs
    if library_template_button_inputs is not None:
        params["library_template_button_inputs"] = library_template_button_inputs
    if library_template_name is not None:
        params["library_template_name"] = library_template_name
    if message_send_ttl_seconds is not None:
        params["message_send_ttl_seconds"] = message_send_ttl_seconds
    params["name"] = name
    if parameter_format is not None:
        params["parameter_format"] = parameter_format
    if send_type is not None:
        params["send_type"] = send_type
    if sub_category is not None:
        params["sub_category"] = sub_category
    result = await get_client().post(f"{whats_app_business_account_id}/message_templates", data=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_migrate_flows(
    whats_app_business_account_id: str,
    source_waba_id: str,
    source_flow_names: Optional[str] = None,
) -> str:
    """POST /migrate_flows on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        source_flow_names: Optional.
        source_waba_id: Required.
    """
    params = {}
    if source_flow_names is not None:
        params["source_flow_names"] = source_flow_names
    params["source_waba_id"] = source_waba_id
    result = await get_client().post(f"{whats_app_business_account_id}/migrate_flows", data=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_migrate_message_templates(
    whats_app_business_account_id: str,
    source_waba_id: str,
    count: Optional[int] = None,
    page_number: Optional[int] = None,
    template_ids: Optional[str] = None,
) -> str:
    """POST /migrate_message_templates on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        count: Optional.
        page_number: Optional.
        source_waba_id: Required.
        template_ids: Optional.
    """
    params = {}
    if count is not None:
        params["count"] = count
    if page_number is not None:
        params["page_number"] = page_number
    params["source_waba_id"] = source_waba_id
    if template_ids is not None:
        params["template_ids"] = template_ids
    result = await get_client().post(f"{whats_app_business_account_id}/migrate_message_templates", data=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_account_payment_configuration(whats_app_business_account_id: str, configuration_name: str) -> str:
    """DELETE /payment_configuration on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        configuration_name: Required.
    """
    params = {}
    params["configuration_name"] = configuration_name
    result = await get_client().delete(f"{whats_app_business_account_id}/payment_configuration")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_payment_configuration(
    whats_app_business_account_id: str,
    configuration_name: str,
    fields: Optional[str] = None,
) -> str:
    """GET /payment_configuration on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        configuration_name: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["configuration_name"] = configuration_name
    result = await get_client().get(f"{whats_app_business_account_id}/payment_configuration", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_payment_configuration(
    whats_app_business_account_id: str,
    configuration_name: str,
    data_endpoint_url: Optional[str] = None,
    merchant_category_code: Optional[str] = None,
    merchant_vpa: Optional[str] = None,
    provider_name: Optional[str] = None,
    purpose_code: Optional[str] = None,
    redirect_url: Optional[str] = None,
) -> str:
    """POST /payment_configuration on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        configuration_name: Required.
        data_endpoint_url: Optional.
        merchant_category_code: Optional.
        merchant_vpa: Optional.
        provider_name: Optional. Values: BILLDESK, PAYU, RAZORPAY, UPI_VPA, ZAAKPAY
        purpose_code: Optional.
        redirect_url: Optional.
    """
    params = {}
    params["configuration_name"] = configuration_name
    if data_endpoint_url is not None:
        params["data_endpoint_url"] = data_endpoint_url
    if merchant_category_code is not None:
        params["merchant_category_code"] = merchant_category_code
    if merchant_vpa is not None:
        params["merchant_vpa"] = merchant_vpa
    if provider_name is not None:
        params["provider_name"] = provider_name
    if purpose_code is not None:
        params["purpose_code"] = purpose_code
    if redirect_url is not None:
        params["redirect_url"] = redirect_url
    result = await get_client().post(f"{whats_app_business_account_id}/payment_configuration", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_payment_configurations(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /payment_configurations on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/payment_configurations", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_phone_numbers(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /phone_numbers on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/phone_numbers", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_phone_numbers(
    whats_app_business_account_id: str,
    cc: Optional[str] = None,
    migrate_phone_number: Optional[bool] = None,
    phone_number: Optional[str] = None,
    preverified_id: Optional[str] = None,
    verified_name: Optional[str] = None,
) -> str:
    """POST /phone_numbers on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        cc: Optional.
        migrate_phone_number: Optional.
        phone_number: Optional.
        preverified_id: Optional.
        verified_name: Optional.
    """
    params = {}
    if cc is not None:
        params["cc"] = cc
    if migrate_phone_number is not None:
        params["migrate_phone_number"] = migrate_phone_number
    if phone_number is not None:
        params["phone_number"] = phone_number
    if preverified_id is not None:
        params["preverified_id"] = preverified_id
    if verified_name is not None:
        params["verified_name"] = verified_name
    result = await get_client().post(f"{whats_app_business_account_id}/phone_numbers", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_pricing_analytics(
    whats_app_business_account_id: str,
    end: int,
    granularity: str,
    start: int,
    fields: Optional[str] = None,
    country_codes: Optional[str] = None,
    dimensions: Optional[str] = None,
    metric_types: Optional[str] = None,
    phone_numbers: Optional[str] = None,
    pricing_categories: Optional[str] = None,
    pricing_types: Optional[str] = None,
    tiers: Optional[str] = None,
) -> str:
    """GET /pricing_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        country_codes: Optional.
        dimensions: Optional. Values: COUNTRY, PHONE, PRICING_CATEGORY, PRICING_TYPE, TIER
        end: Required.
        granularity: Required. Values: DAILY, HALF_HOUR, MONTHLY
        metric_types: Optional. Values: COST, VOLUME
        phone_numbers: Optional.
        pricing_categories: Optional. Values: AUTHENTICATION, AUTHENTICATION_INTERNATIONAL, GROUP_MARKETING, GROUP_MARKETING_LITE, GROUP_SERVICE, GROUP_UTILITY, MARKETING, MARKETING_LITE, MARKETING_LITE_DYNAMIC, SERVICE, UTILITY
        pricing_types: Optional. Values: FREE_CUSTOMER_SERVICE, FREE_ENTRY_POINT, FREE_GROUP_CUSTOMER_SERVICE, REGULAR
        start: Required.
        tiers: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if country_codes is not None:
        params["country_codes"] = country_codes
    if dimensions is not None:
        params["dimensions"] = dimensions
    params["end"] = end
    params["granularity"] = granularity
    if metric_types is not None:
        params["metric_types"] = metric_types
    if phone_numbers is not None:
        params["phone_numbers"] = phone_numbers
    if pricing_categories is not None:
        params["pricing_categories"] = pricing_categories
    if pricing_types is not None:
        params["pricing_types"] = pricing_types
    params["start"] = start
    if tiers is not None:
        params["tiers"] = tiers
    result = await get_client().get(f"{whats_app_business_account_id}/pricing_analytics", params=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_account_product_catalogs(whats_app_business_account_id: str, catalog_id: str) -> str:
    """DELETE /product_catalogs on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        catalog_id: Required.
    """
    params = {}
    params["catalog_id"] = catalog_id
    result = await get_client().delete(f"{whats_app_business_account_id}/product_catalogs")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_product_catalogs(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /product_catalogs on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_product_catalogs(whats_app_business_account_id: str, catalog_id: str) -> str:
    """POST /product_catalogs on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        catalog_id: Required.
    """
    params = {}
    params["catalog_id"] = catalog_id
    result = await get_client().post(f"{whats_app_business_account_id}/product_catalogs", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_schedules(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /schedules on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/schedules", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_set_obo_mobility_intent(whats_app_business_account_id: str, solution_id: Optional[str] = None) -> str:
    """POST /set_obo_mobility_intent on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        solution_id: Optional.
    """
    params = {}
    if solution_id is not None:
        params["solution_id"] = solution_id
    result = await get_client().post(f"{whats_app_business_account_id}/set_obo_mobility_intent", data=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_set_solution_migration_intent(
    whats_app_business_account_id: str,
    app_id: Optional[str] = None,
    solution_id: Optional[str] = None,
) -> str:
    """POST /set_solution_migration_intent on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        app_id: Optional.
        solution_id: Optional.
    """
    params = {}
    if app_id is not None:
        params["app_id"] = app_id
    if solution_id is not None:
        params["solution_id"] = solution_id
    result = await get_client().post(f"{whats_app_business_account_id}/set_solution_migration_intent", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_solutions(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /solutions on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/solutions", params=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_account_subscribed_apps(whats_app_business_account_id: str) -> str:
    """DELETE /subscribed_apps on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
    """
    params = {}
    result = await get_client().delete(f"{whats_app_business_account_id}/subscribed_apps")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_subscribed_apps(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /subscribed_apps on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/subscribed_apps", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_subscribed_apps(
    whats_app_business_account_id: str,
    override_callback_uri: Optional[str] = None,
    verify_token: Optional[str] = None,
) -> str:
    """POST /subscribed_apps on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        override_callback_uri: Optional.
        verify_token: Optional.
    """
    params = {}
    if override_callback_uri is not None:
        params["override_callback_uri"] = override_callback_uri
    if verify_token is not None:
        params["verify_token"] = verify_token
    result = await get_client().post(f"{whats_app_business_account_id}/subscribed_apps", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_template_analytics(
    whats_app_business_account_id: str,
    end: str,
    granularity: str,
    start: str,
    template_ids: str,
    fields: Optional[str] = None,
    metric_types: Optional[str] = None,
    product_type: Optional[str] = None,
    use_waba_timezone: Optional[bool] = None,
) -> str:
    """GET /template_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        end: Required.
        granularity: Required. Values: DAILY
        metric_types: Optional. Values: APP_ACTIVATIONS, APP_ADD_TO_CART, APP_CHECKOUTS_INITIATED, APP_PURCHASES, APP_PURCHASES_CONVERSION_VALUE, CLICKED, COST, DELIVERED, READ, REPLIED, SENT, WEBSITE_ADD_TO_CART, WEBSITE_CHECKOUTS_INITIATED, WEBSITE_PURCHASES, WEBSITE_PURCHASES_CONVERSION_VALUE
        product_type: Optional. Values: CLOUD_API, MARKETING_MESSAGES_LITE_API
        start: Required.
        template_ids: Required.
        use_waba_timezone: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["end"] = end
    params["granularity"] = granularity
    if metric_types is not None:
        params["metric_types"] = metric_types
    if product_type is not None:
        params["product_type"] = product_type
    params["start"] = start
    params["template_ids"] = template_ids
    if use_waba_timezone is not None:
        params["use_waba_timezone"] = use_waba_timezone
    result = await get_client().get(f"{whats_app_business_account_id}/template_analytics", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_template_group_analytics(
    whats_app_business_account_id: str,
    end: str,
    granularity: str,
    start: str,
    template_group_ids: str,
    fields: Optional[str] = None,
    metric_types: Optional[str] = None,
    use_waba_timezone: Optional[bool] = None,
) -> str:
    """GET /template_group_analytics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        end: Required.
        granularity: Required. Values: DAILY
        metric_types: Optional. Values: APP_ACTIVATIONS, APP_ADD_TO_CART, APP_CHECKOUTS_INITIATED, APP_PURCHASES, APP_PURCHASES_CONVERSION_VALUE, CLICKED, COST, DELIVERED, READ, REPLIED, SENT, WEBSITE_ADD_TO_CART, WEBSITE_CHECKOUTS_INITIATED, WEBSITE_PURCHASES, WEBSITE_PURCHASES_CONVERSION_VALUE
        start: Required.
        template_group_ids: Required.
        use_waba_timezone: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["end"] = end
    params["granularity"] = granularity
    if metric_types is not None:
        params["metric_types"] = metric_types
    params["start"] = start
    params["template_group_ids"] = template_group_ids
    if use_waba_timezone is not None:
        params["use_waba_timezone"] = use_waba_timezone
    result = await get_client().get(f"{whats_app_business_account_id}/template_group_analytics", params=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_template_groups(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /template_groups on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}/template_groups", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_template_groups(
    whats_app_business_account_id: str,
    description: str,
    name: str,
    whatsapp_business_templates: str,
) -> str:
    """POST /template_groups on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        description: Required.
        name: Required.
        whatsapp_business_templates: Required.
    """
    params = {}
    params["description"] = description
    params["name"] = name
    params["whatsapp_business_templates"] = whatsapp_business_templates
    result = await get_client().post(f"{whats_app_business_account_id}/template_groups", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_template_performance_metrics(
    whats_app_business_account_id: str,
    fields: Optional[str] = None,
    name: Optional[str] = None,
    template_id: Optional[str] = None,
) -> str:
    """GET /template_performance_metrics on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        name: Optional.
        template_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if name is not None:
        params["name"] = name
    if template_id is not None:
        params["template_id"] = template_id
    result = await get_client().get(f"{whats_app_business_account_id}/template_performance_metrics", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_upsert_message_templates(
    whats_app_business_account_id: str,
    category: str,
    components: str,
    languages: str,
    name: str,
    message_send_ttl_seconds: Optional[int] = None,
) -> str:
    """POST /upsert_message_templates on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        category: Required. Values: AUTHENTICATION
        components: Required.
        languages: Required.
        message_send_ttl_seconds: Optional.
        name: Required.
    """
    params = {}
    params["category"] = category
    params["components"] = components
    params["languages"] = languages
    if message_send_ttl_seconds is not None:
        params["message_send_ttl_seconds"] = message_send_ttl_seconds
    params["name"] = name
    result = await get_client().post(f"{whats_app_business_account_id}/upsert_message_templates", data=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_account_welcome_message_sequences(whats_app_business_account_id: str, sequence_id: str) -> str:
    """DELETE /welcome_message_sequences on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        sequence_id: Required.
    """
    params = {}
    params["sequence_id"] = sequence_id
    result = await get_client().delete(f"{whats_app_business_account_id}/welcome_message_sequences")
    return json.dumps(result, indent=2)


async def get_whats_app_business_account_welcome_message_sequences(
    whats_app_business_account_id: str,
    fields: Optional[str] = None,
    app_id: Optional[str] = None,
    sequence_id: Optional[str] = None,
) -> str:
    """GET /welcome_message_sequences on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return.
        app_id: Optional.
        sequence_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if app_id is not None:
        params["app_id"] = app_id
    if sequence_id is not None:
        params["sequence_id"] = sequence_id
    result = await get_client().get(f"{whats_app_business_account_id}/welcome_message_sequences", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_account_welcome_message_sequences(
    whats_app_business_account_id: str,
    name: Optional[str] = None,
    sequence_id: Optional[str] = None,
    welcome_message_sequence: Optional[str] = None,
) -> str:
    """POST /welcome_message_sequences on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        name: Optional.
        sequence_id: Optional.
        welcome_message_sequence: Optional.
    """
    params = {}
    if name is not None:
        params["name"] = name
    if sequence_id is not None:
        params["sequence_id"] = sequence_id
    if welcome_message_sequence is not None:
        params["welcome_message_sequence"] = welcome_message_sequence
    result = await get_client().post(f"{whats_app_business_account_id}/welcome_message_sequences", data=params)
    return json.dumps(result, indent=2)


async def get_whats_app_business_account(whats_app_business_account_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        fields: Comma-separated list of fields to return. Available: account_review_status, analytics, auth_international_rate_eligibility, business_verification_status, country, creation_time, currency, health_status, id, is_enabled_for_insights, is_shared_with_partners, linked_commerce_account, marketing_messages_lite_api_status, marketing_messages_onboarding_status, message_template_namespace, name, on_behalf_of_business_info, owner_business, owner_business_info, ownership_type, primary_business_location, primary_funding_id, purchase_order_number, status, timezone_id, whatsapp_business_manager_messaging_limit
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_account_id}", params=params)
    return json.dumps(result, indent=2)


async def update_whats_app_business_account(
    whats_app_business_account_id: str,
    is_enabled_for_insights: Optional[bool] = None,
) -> str:
    """POST /#update on WhatsAppBusinessAccount.

    Args:
        whats_app_business_account_id: The ID of the WhatsAppBusinessAccount object.
        is_enabled_for_insights: Optional.
    """
    params = {}
    if is_enabled_for_insights is not None:
        params["is_enabled_for_insights"] = is_enabled_for_insights
    result = await get_client().post(f"{whats_app_business_account_id}", data=params)
    return json.dumps(result, indent=2)


WHATS_APP_BUSINESS_PRE_VERIFIED_PHONE_NUMBER_FIELDS = [
    "code_verification_status",
    "code_verification_time",
    "id",
    "owner_business",
    "phone_number",
    "verification_expiry_time"
]


async def get_whats_app_business_pre_verified_phone_number_partners(
    whats_app_business_pre_verified_phone_number_id: str,
    fields: Optional[str] = None,
) -> str:
    """GET /partners on WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whats_app_business_pre_verified_phone_number_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_pre_verified_phone_number_id}/partners", params=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_pre_verified_phone_number_request_code(
    whats_app_business_pre_verified_phone_number_id: str,
    code_method: str,
    language: str,
) -> str:
    """POST /request_code on WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whats_app_business_pre_verified_phone_number_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber object.
        code_method: Required. Values: SMS, VOICE
        language: Required.
    """
    params = {}
    params["code_method"] = code_method
    params["language"] = language
    result = await get_client().post(f"{whats_app_business_pre_verified_phone_number_id}/request_code", data=params)
    return json.dumps(result, indent=2)


async def create_whats_app_business_pre_verified_phone_number_verify_code(whats_app_business_pre_verified_phone_number_id: str, code: str) -> str:
    """POST /verify_code on WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whats_app_business_pre_verified_phone_number_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber object.
        code: Required.
    """
    params = {}
    params["code"] = code
    result = await get_client().post(f"{whats_app_business_pre_verified_phone_number_id}/verify_code", data=params)
    return json.dumps(result, indent=2)


async def delete_whats_app_business_pre_verified_phone_number(whats_app_business_pre_verified_phone_number_id: str) -> str:
    """DELETE /#delete on WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whats_app_business_pre_verified_phone_number_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber object.
    """
    params = {}
    result = await get_client().delete(f"{whats_app_business_pre_verified_phone_number_id}")
    return json.dumps(result, indent=2)


async def get_whats_app_business_pre_verified_phone_number(
    whats_app_business_pre_verified_phone_number_id: str,
    fields: Optional[str] = None,
) -> str:
    """GET /#get on WhatsAppBusinessPreVerifiedPhoneNumber.

    Args:
        whats_app_business_pre_verified_phone_number_id: The ID of the WhatsAppBusinessPreVerifiedPhoneNumber object.
        fields: Comma-separated list of fields to return. Available: code_verification_status, code_verification_time, id, owner_business, phone_number, verification_expiry_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_pre_verified_phone_number_id}", params=params)
    return json.dumps(result, indent=2)


WHATS_APP_BUSINESS_PROFILE_FIELDS = [
    "id",
    "name_verification",
    "whatsapp_business_api_data"
]


async def get_whats_app_business_profile(whats_app_business_profile_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on WhatsAppBusinessProfile.

    Args:
        whats_app_business_profile_id: The ID of the WhatsAppBusinessProfile object.
        fields: Comma-separated list of fields to return. Available: id, name_verification, whatsapp_business_api_data
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{whats_app_business_profile_id}", params=params)
    return json.dumps(result, indent=2)


async def update_whats_app_business_profile(whats_app_business_profile_id: str) -> str:
    """POST /#update on WhatsAppBusinessProfile.

    Args:
        whats_app_business_profile_id: The ID of the WhatsAppBusinessProfile object.
    """
    params = {}
    result = await get_client().post(f"{whats_app_business_profile_id}", data=params)
    return json.dumps(result, indent=2)

