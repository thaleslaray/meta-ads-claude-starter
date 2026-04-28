"""Auto-generated Meta Marketing API tools — fundraiser."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


FUNDRAISER_PERSON_TO_CHARITY_FIELDS = [
    "amount_raised",
    "charity_id",
    "currency",
    "description",
    "donations_count",
    "donors_count",
    "end_time",
    "external_amount_raised",
    "external_donations_count",
    "external_donors_count",
    "external_event_name",
    "external_event_start_time",
    "external_event_uri",
    "external_fundraiser_uri",
    "external_id",
    "goal_amount",
    "id",
    "internal_amount_raised",
    "internal_donations_count",
    "internal_donors_count",
    "name",
    "uri"
]


async def get_fundraiser_person_to_charity_donations(fundraiser_person_to_charity_id: str, fields: Optional[str] = None) -> str:
    """GET /donations on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{fundraiser_person_to_charity_id}/donations", params=params)
    return json.dumps(result, indent=2)


async def create_fundraiser_person_to_charity_end_fundraiser(fundraiser_person_to_charity_id: str) -> str:
    """POST /end_fundraiser on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
    """
    params = {}
    result = await get_client().post(f"{fundraiser_person_to_charity_id}/end_fundraiser", data=params)
    return json.dumps(result, indent=2)


async def get_fundraiser_person_to_charity_external_donations(fundraiser_person_to_charity_id: str, fields: Optional[str] = None) -> str:
    """GET /external_donations on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{fundraiser_person_to_charity_id}/external_donations", params=params)
    return json.dumps(result, indent=2)


async def create_fundraiser_person_to_charity_external_donations(
    fundraiser_person_to_charity_id: str,
    amount_received: int,
    currency: str,
    donation_id_hash: str,
    donation_time: int,
    donor_id_hash: str,
) -> str:
    """POST /external_donations on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
        amount_received: Required.
        currency: Required.
        donation_id_hash: Required.
        donation_time: Required.
        donor_id_hash: Required.
    """
    params = {}
    params["amount_received"] = amount_received
    params["currency"] = currency
    params["donation_id_hash"] = donation_id_hash
    params["donation_time"] = donation_time
    params["donor_id_hash"] = donor_id_hash
    result = await get_client().post(f"{fundraiser_person_to_charity_id}/external_donations", data=params)
    return json.dumps(result, indent=2)


async def get_fundraiser_person_to_charity(fundraiser_person_to_charity_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
        fields: Comma-separated list of fields to return. Available: amount_raised, charity_id, currency, description, donations_count, donors_count, end_time, external_amount_raised, external_donations_count, external_donors_count, external_event_name, external_event_start_time, external_event_uri, external_fundraiser_uri, external_id, goal_amount, id, internal_amount_raised, internal_donations_count, internal_donors_count, name, uri
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{fundraiser_person_to_charity_id}", params=params)
    return json.dumps(result, indent=2)


async def update_fundraiser_person_to_charity(
    fundraiser_person_to_charity_id: str,
    description: Optional[str] = None,
    end_time: Optional[str] = None,
    external_event_name: Optional[str] = None,
    external_event_start_time: Optional[str] = None,
    external_event_uri: Optional[str] = None,
    external_fundraiser_uri: Optional[str] = None,
    external_id: Optional[str] = None,
    goal_amount: Optional[int] = None,
    name: Optional[str] = None,
) -> str:
    """POST /#update on FundraiserPersonToCharity.

    Args:
        fundraiser_person_to_charity_id: The ID of the FundraiserPersonToCharity object.
        description: Optional.
        end_time: Optional.
        external_event_name: Optional.
        external_event_start_time: Optional.
        external_event_uri: Optional.
        external_fundraiser_uri: Optional.
        external_id: Optional.
        goal_amount: Optional.
        name: Optional.
    """
    params = {}
    if description is not None:
        params["description"] = description
    if end_time is not None:
        params["end_time"] = end_time
    if external_event_name is not None:
        params["external_event_name"] = external_event_name
    if external_event_start_time is not None:
        params["external_event_start_time"] = external_event_start_time
    if external_event_uri is not None:
        params["external_event_uri"] = external_event_uri
    if external_fundraiser_uri is not None:
        params["external_fundraiser_uri"] = external_fundraiser_uri
    if external_id is not None:
        params["external_id"] = external_id
    if goal_amount is not None:
        params["goal_amount"] = goal_amount
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"{fundraiser_person_to_charity_id}", data=params)
    return json.dumps(result, indent=2)

