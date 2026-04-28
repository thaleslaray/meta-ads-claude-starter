"""Auto-generated Meta Marketing API tools — lead_gen."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


LEADGEN_FORM_FIELDS = [
    "allow_organic_lead",
    "block_display_for_non_targeted_viewer",
    "context_card",
    "created_time",
    "creator",
    "expired_leads_count",
    "follow_up_action_text",
    "follow_up_action_url",
    "id",
    "is_optimized_for_quality",
    "leads_count",
    "legal_content",
    "locale",
    "name",
    "organic_leads_count",
    "page",
    "page_id",
    "privacy_policy_url",
    "question_page_custom_headline",
    "questions",
    "status",
    "thank_you_page",
    "tracking_parameters"
]


async def get_leadgen_form_leads(leadgen_form_id: str, fields: Optional[str] = None) -> str:
    """GET /leads on LeadgenForm.

    Args:
        leadgen_form_id: The ID of the LeadgenForm object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{leadgen_form_id}/leads", params=params)
    return json.dumps(result, indent=2)


async def get_leadgen_form_test_leads(leadgen_form_id: str, fields: Optional[str] = None) -> str:
    """GET /test_leads on LeadgenForm.

    Args:
        leadgen_form_id: The ID of the LeadgenForm object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{leadgen_form_id}/test_leads", params=params)
    return json.dumps(result, indent=2)


async def create_leadgen_form_test_leads(
    leadgen_form_id: str,
    custom_disclaimer_responses: Optional[str] = None,
    field_data: Optional[str] = None,
) -> str:
    """POST /test_leads on LeadgenForm.

    Args:
        leadgen_form_id: The ID of the LeadgenForm object.
        custom_disclaimer_responses: Optional.
        field_data: Optional.
    """
    params = {}
    if custom_disclaimer_responses is not None:
        params["custom_disclaimer_responses"] = custom_disclaimer_responses
    if field_data is not None:
        params["field_data"] = field_data
    result = await get_client().post(f"{leadgen_form_id}/test_leads", data=params)
    return json.dumps(result, indent=2)


async def get_leadgen_form(leadgen_form_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on LeadgenForm.

    Args:
        leadgen_form_id: The ID of the LeadgenForm object.
        fields: Comma-separated list of fields to return. Available: allow_organic_lead, block_display_for_non_targeted_viewer, context_card, created_time, creator, expired_leads_count, follow_up_action_text, follow_up_action_url, id, is_optimized_for_quality, leads_count, legal_content, locale, name, organic_leads_count, page, page_id, privacy_policy_url, question_page_custom_headline, questions, status, thank_you_page, tracking_parameters
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{leadgen_form_id}", params=params)
    return json.dumps(result, indent=2)


async def update_leadgen_form(leadgen_form_id: str, status: Optional[str] = None) -> str:
    """POST /#update on LeadgenForm.

    Args:
        leadgen_form_id: The ID of the LeadgenForm object.
        status: Optional.
    """
    params = {}
    if status is not None:
        params["status"] = status
    result = await get_client().post(f"{leadgen_form_id}", data=params)
    return json.dumps(result, indent=2)


LEAD_FIELDS = [
    "ad_id",
    "ad_name",
    "adset_id",
    "adset_name",
    "campaign_id",
    "campaign_name",
    "created_time",
    "custom_disclaimer_responses",
    "field_data",
    "form_id",
    "home_listing",
    "id",
    "is_organic",
    "partner_name",
    "platform",
    "post",
    "post_submission_check_result",
    "retailer_item_id",
    "vehicle"
]


async def delete_lead(lead_id: str) -> str:
    """DELETE /#delete on Lead.

    Args:
        lead_id: The ID of the Lead object.
    """
    params = {}
    result = await get_client().delete(f"{lead_id}")
    return json.dumps(result, indent=2)


async def get_lead(lead_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Lead.

    Args:
        lead_id: The ID of the Lead object.
        fields: Comma-separated list of fields to return. Available: ad_id, ad_name, adset_id, adset_name, campaign_id, campaign_name, created_time, custom_disclaimer_responses, field_data, form_id, home_listing, id, is_organic, partner_name, platform, post, post_submission_check_result, retailer_item_id, vehicle
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{lead_id}", params=params)
    return json.dumps(result, indent=2)

