"""Auto-generated Meta Marketing API tools — messenger."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


MESSENGER_ADS_PARTIAL_AUTOMATED_STEP_LIST_FIELDS = [
    "fblead_form",
    "first_step_id",
    "id",
    "page",
    "privacy_url",
    "reminder_text",
    "stop_question_message"
]


async def get_messenger_ads_partial_automated_step_list_steps(messenger_ads_partial_automated_step_list_id: str, fields: Optional[str] = None) -> str:
    """GET /steps on MessengerAdsPartialAutomatedStepList.

    Args:
        messenger_ads_partial_automated_step_list_id: The ID of the MessengerAdsPartialAutomatedStepList object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{messenger_ads_partial_automated_step_list_id}/steps", params=params)
    return json.dumps(result, indent=2)


async def get_messenger_ads_partial_automated_step_list(messenger_ads_partial_automated_step_list_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on MessengerAdsPartialAutomatedStepList.

    Args:
        messenger_ads_partial_automated_step_list_id: The ID of the MessengerAdsPartialAutomatedStepList object.
        fields: Comma-separated list of fields to return. Available: fblead_form, first_step_id, id, page, privacy_url, reminder_text, stop_question_message
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{messenger_ads_partial_automated_step_list_id}", params=params)
    return json.dumps(result, indent=2)


MESSENGER_BUSINESS_TEMPLATE_FIELDS = [
    "category",
    "components",
    "creation_time",
    "id",
    "language",
    "language_count",
    "last_updated_time",
    "library_template_name",
    "name",
    "rejected_reason",
    "rejection_reasons",
    "specific_rejection_reasons",
    "status"
]


async def get_messenger_business_template(messenger_business_template_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on MessengerBusinessTemplate.

    Args:
        messenger_business_template_id: The ID of the MessengerBusinessTemplate object.
        fields: Comma-separated list of fields to return. Available: category, components, creation_time, id, language, language_count, last_updated_time, library_template_name, name, rejected_reason, rejection_reasons, specific_rejection_reasons, status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{messenger_business_template_id}", params=params)
    return json.dumps(result, indent=2)


async def update_messenger_business_template(messenger_business_template_id: str, components: Optional[str] = None) -> str:
    """POST /#update on MessengerBusinessTemplate.

    Args:
        messenger_business_template_id: The ID of the MessengerBusinessTemplate object.
        components: Optional.
    """
    params = {}
    if components is not None:
        params["components"] = components
    result = await get_client().post(f"{messenger_business_template_id}", data=params)
    return json.dumps(result, indent=2)


PERSONA_FIELDS = [
    "id",
    "name",
    "profile_picture_url"
]


async def delete_persona(persona_id: str) -> str:
    """DELETE /#delete on Persona.

    Args:
        persona_id: The ID of the Persona object.
    """
    params = {}
    result = await get_client().delete(f"{persona_id}")
    return json.dumps(result, indent=2)


async def get_persona(persona_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Persona.

    Args:
        persona_id: The ID of the Persona object.
        fields: Comma-separated list of fields to return. Available: id, name, profile_picture_url
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{persona_id}", params=params)
    return json.dumps(result, indent=2)


UNIFIED_THREAD_FIELDS = [
    "can_reply",
    "folder",
    "former_participants",
    "id",
    "is_owner",
    "is_subscribed",
    "link",
    "linked_group",
    "message_count",
    "name",
    "participants",
    "scoped_thread_key",
    "senders",
    "snippet",
    "unread_count",
    "updated_time",
    "wallpaper"
]


async def get_unified_thread_messages(
    unified_thread_id: str,
    fields: Optional[str] = None,
    source: Optional[str] = None,
) -> str:
    """GET /messages on UnifiedThread.

    Args:
        unified_thread_id: The ID of the UnifiedThread object.
        fields: Comma-separated list of fields to return.
        source: Optional. Values: ALL, PARTICIPANTS
    """
    params = {}
    params["fields"] = fields or "id,name"
    if source is not None:
        params["source"] = source
    result = await get_client().get(f"{unified_thread_id}/messages", params=params)
    return json.dumps(result, indent=2)


async def get_unified_thread(unified_thread_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on UnifiedThread.

    Args:
        unified_thread_id: The ID of the UnifiedThread object.
        fields: Comma-separated list of fields to return. Available: can_reply, folder, former_participants, id, is_owner, is_subscribed, link, linked_group, message_count, name, participants, scoped_thread_key, senders, snippet, unread_count, updated_time, wallpaper
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{unified_thread_id}", params=params)
    return json.dumps(result, indent=2)

