"""Auto-generated Meta Marketing API tools — audiences."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


CUSTOM_AUDIENCE_FIELDS = [
    "account_id",
    "approximate_count_lower_bound",
    "approximate_count_upper_bound",
    "customer_file_source",
    "data_source",
    "data_source_types",
    "datafile_custom_audience_uploading_status",
    "delete_time",
    "delivery_status",
    "description",
    "excluded_custom_audiences",
    "external_event_source",
    "fields_violating_integrity_policy",
    "household_audience",
    "id",
    "included_custom_audiences",
    "is_eligible_for_sac_campaigns",
    "is_household",
    "is_snapshot",
    "is_value_based",
    "lookalike_audience_ids",
    "lookalike_spec",
    "name",
    "operation_status",
    "opt_out_link",
    "owner_business",
    "page_deletion_marked_delete_time",
    "permission_for_actions",
    "pixel_id",
    "regulated_audience_spec",
    "retention_days",
    "rev_share_policy_id",
    "rule",
    "rule_aggregation",
    "rule_v2",
    "seed_audience",
    "sharing_status",
    "subtype",
    "time_content_updated",
    "time_created",
    "time_updated"
]


async def delete_custom_audience_adaccounts(custom_audience_id: str, adaccounts: Optional[str] = None) -> str:
    """DELETE /adaccounts on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        adaccounts: Optional.
    """
    params = {}
    if adaccounts is not None:
        params["adaccounts"] = adaccounts
    result = await get_client().delete(f"{custom_audience_id}/adaccounts")
    return json.dumps(result, indent=2)


async def get_custom_audience_adaccounts(
    custom_audience_id: str,
    fields: Optional[str] = None,
    permissions: Optional[str] = None,
) -> str:
    """GET /adaccounts on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
        permissions: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if permissions is not None:
        params["permissions"] = permissions
    result = await get_client().get(f"{custom_audience_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def create_custom_audience_adaccounts(
    custom_audience_id: str,
    adaccounts: Optional[str] = None,
    permissions: Optional[str] = None,
    relationship_type: Optional[str] = None,
    replace: Optional[bool] = None,
) -> str:
    """POST /adaccounts on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        adaccounts: Optional.
        permissions: Optional.
        relationship_type: Optional.
        replace: Optional.
    """
    params = {}
    if adaccounts is not None:
        params["adaccounts"] = adaccounts
    if permissions is not None:
        params["permissions"] = permissions
    if relationship_type is not None:
        params["relationship_type"] = relationship_type
    if replace is not None:
        params["replace"] = replace
    result = await get_client().post(f"{custom_audience_id}/adaccounts", data=params)
    return json.dumps(result, indent=2)


async def get_custom_audience_ads(
    custom_audience_id: str,
    fields: Optional[str] = None,
    effective_status: Optional[str] = None,
    status: Optional[str] = None,
) -> str:
    """GET /ads on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
        effective_status: Optional.
        status: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if effective_status is not None:
        params["effective_status"] = effective_status
    if status is not None:
        params["status"] = status
    result = await get_client().get(f"{custom_audience_id}/ads", params=params)
    return json.dumps(result, indent=2)


async def get_custom_audience_health(
    custom_audience_id: str,
    fields: Optional[str] = None,
    calculated_date: Optional[str] = None,
    processed_date: Optional[str] = None,
    value_aggregation_duration: Optional[int] = None,
    value_country: Optional[str] = None,
    value_currency: Optional[str] = None,
    value_version: Optional[int] = None,
) -> str:
    """GET /health on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
        calculated_date: Optional.
        processed_date: Optional.
        value_aggregation_duration: Optional.
        value_country: Optional.
        value_currency: Optional.
        value_version: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if calculated_date is not None:
        params["calculated_date"] = calculated_date
    if processed_date is not None:
        params["processed_date"] = processed_date
    if value_aggregation_duration is not None:
        params["value_aggregation_duration"] = value_aggregation_duration
    if value_country is not None:
        params["value_country"] = value_country
    if value_currency is not None:
        params["value_currency"] = value_currency
    if value_version is not None:
        params["value_version"] = value_version
    result = await get_client().get(f"{custom_audience_id}/health", params=params)
    return json.dumps(result, indent=2)


async def get_custom_audience_salts(
    custom_audience_id: str,
    fields: Optional[str] = None,
    params: Optional[str] = None,
) -> str:
    """GET /salts on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
        params: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if params is not None:
        params["params"] = params
    result = await get_client().get(f"{custom_audience_id}/salts", params=params)
    return json.dumps(result, indent=2)


async def create_custom_audience_salts(custom_audience_id: str, salt: str, valid_from: str, valid_to: str) -> str:
    """POST /salts on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        salt: Required.
        valid_from: Required.
        valid_to: Required.
    """
    params = {}
    params["salt"] = salt
    params["valid_from"] = valid_from
    params["valid_to"] = valid_to
    result = await get_client().post(f"{custom_audience_id}/salts", data=params)
    return json.dumps(result, indent=2)


async def get_custom_audience_sessions(
    custom_audience_id: str,
    fields: Optional[str] = None,
    session_id: Optional[int] = None,
) -> str:
    """GET /sessions on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
        session_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if session_id is not None:
        params["session_id"] = session_id
    result = await get_client().get(f"{custom_audience_id}/sessions", params=params)
    return json.dumps(result, indent=2)


async def get_custom_audience_shared_account_info(custom_audience_id: str, fields: Optional[str] = None) -> str:
    """GET /shared_account_info on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{custom_audience_id}/shared_account_info", params=params)
    return json.dumps(result, indent=2)


async def delete_custom_audience_users(
    custom_audience_id: str,
    namespace: Optional[str] = None,
    payload: Optional[str] = None,
    session: Optional[str] = None,
) -> str:
    """DELETE /users on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        namespace: Optional.
        payload: Optional.
        session: Optional.
    """
    params = {}
    if namespace is not None:
        params["namespace"] = namespace
    if payload is not None:
        params["payload"] = payload
    if session is not None:
        params["session"] = session
    result = await get_client().delete(f"{custom_audience_id}/users")
    return json.dumps(result, indent=2)


async def create_custom_audience_users(
    custom_audience_id: str,
    namespace: Optional[str] = None,
    payload: Optional[str] = None,
    session: Optional[str] = None,
) -> str:
    """POST /users on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        namespace: Optional.
        payload: Optional.
        session: Optional.
    """
    params = {}
    if namespace is not None:
        params["namespace"] = namespace
    if payload is not None:
        params["payload"] = payload
    if session is not None:
        params["session"] = session
    result = await get_client().post(f"{custom_audience_id}/users", data=params)
    return json.dumps(result, indent=2)


async def create_custom_audience_usersreplace(
    custom_audience_id: str,
    payload: str,
    session: str,
    namespace: Optional[str] = None,
) -> str:
    """POST /usersreplace on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        namespace: Optional.
        payload: Required.
        session: Required.
    """
    params = {}
    if namespace is not None:
        params["namespace"] = namespace
    params["payload"] = payload
    params["session"] = session
    result = await get_client().post(f"{custom_audience_id}/usersreplace", data=params)
    return json.dumps(result, indent=2)


async def delete_custom_audience(custom_audience_id: str) -> str:
    """DELETE /#delete on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
    """
    params = {}
    result = await get_client().delete(f"{custom_audience_id}")
    return json.dumps(result, indent=2)


async def get_custom_audience(
    custom_audience_id: str,
    fields: Optional[str] = None,
    ad_account_id: Optional[str] = None,
    special_ad_categories: Optional[str] = None,
    special_ad_category_countries: Optional[str] = None,
    target_countries: Optional[str] = None,
) -> str:
    """GET /#get on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        fields: Comma-separated list of fields to return. Available: account_id, approximate_count_lower_bound, approximate_count_upper_bound, customer_file_source, data_source, data_source_types, datafile_custom_audience_uploading_status, delete_time, delivery_status, description, excluded_custom_audiences, external_event_source, fields_violating_integrity_policy, household_audience, id, included_custom_audiences, is_eligible_for_sac_campaigns, is_household, is_snapshot, is_value_based, lookalike_audience_ids, lookalike_spec, name, operation_status, opt_out_link, owner_business, page_deletion_marked_delete_time, permission_for_actions, pixel_id, regulated_audience_spec, retention_days, rev_share_policy_id, rule, rule_aggregation, rule_v2, seed_audience, sharing_status, subtype, time_content_updated, time_created, time_updated
        ad_account_id: Optional.
        special_ad_categories: Optional.
        special_ad_category_countries: Optional.
        target_countries: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ad_account_id is not None:
        params["ad_account_id"] = ad_account_id
    if special_ad_categories is not None:
        params["special_ad_categories"] = special_ad_categories
    if special_ad_category_countries is not None:
        params["special_ad_category_countries"] = special_ad_category_countries
    if target_countries is not None:
        params["target_countries"] = target_countries
    result = await get_client().get(f"{custom_audience_id}", params=params)
    return json.dumps(result, indent=2)


async def update_custom_audience(
    custom_audience_id: str,
    allowed_domains: Optional[str] = None,
    claim_objective: Optional[str] = None,
    content_type: Optional[str] = None,
    countries: Optional[str] = None,
    customer_file_source: Optional[str] = None,
    description: Optional[str] = None,
    enable_fetch_or_create: Optional[bool] = None,
    event_source_group: Optional[str] = None,
    event_sources: Optional[str] = None,
    exclusions: Optional[str] = None,
    inclusionOperator: Optional[str] = None,
    inclusions: Optional[str] = None,
    lookalike_spec: Optional[str] = None,
    name: Optional[str] = None,
    opt_out_link: Optional[str] = None,
    parent_audience_id: Optional[int] = None,
    product_set_id: Optional[str] = None,
    retention_days: Optional[int] = None,
    rev_share_policy_id: Optional[int] = None,
    rule: Optional[str] = None,
    rule_aggregation: Optional[str] = None,
    tags: Optional[str] = None,
    use_in_campaigns: Optional[bool] = None,
) -> str:
    """POST /#update on CustomAudience.

    Args:
        custom_audience_id: The ID of the CustomAudience object.
        allowed_domains: Optional.
        claim_objective: Optional.
        content_type: Optional.
        countries: Optional.
        customer_file_source: Optional.
        description: Optional.
        enable_fetch_or_create: Optional.
        event_source_group: Optional.
        event_sources: Optional.
        exclusions: Optional.
        inclusionOperator: Optional.
        inclusions: Optional.
        lookalike_spec: Optional.
        name: Optional.
        opt_out_link: Optional.
        parent_audience_id: Optional.
        product_set_id: Optional.
        retention_days: Optional.
        rev_share_policy_id: Optional.
        rule: Optional.
        rule_aggregation: Optional.
        tags: Optional.
        use_in_campaigns: Optional.
    """
    params = {}
    if allowed_domains is not None:
        params["allowed_domains"] = allowed_domains
    if claim_objective is not None:
        params["claim_objective"] = claim_objective
    if content_type is not None:
        params["content_type"] = content_type
    if countries is not None:
        params["countries"] = countries
    if customer_file_source is not None:
        params["customer_file_source"] = customer_file_source
    if description is not None:
        params["description"] = description
    if enable_fetch_or_create is not None:
        params["enable_fetch_or_create"] = enable_fetch_or_create
    if event_source_group is not None:
        params["event_source_group"] = event_source_group
    if event_sources is not None:
        params["event_sources"] = event_sources
    if exclusions is not None:
        params["exclusions"] = exclusions
    if inclusionOperator is not None:
        params["inclusionOperator"] = inclusionOperator
    if inclusions is not None:
        params["inclusions"] = inclusions
    if lookalike_spec is not None:
        params["lookalike_spec"] = lookalike_spec
    if name is not None:
        params["name"] = name
    if opt_out_link is not None:
        params["opt_out_link"] = opt_out_link
    if parent_audience_id is not None:
        params["parent_audience_id"] = parent_audience_id
    if product_set_id is not None:
        params["product_set_id"] = product_set_id
    if retention_days is not None:
        params["retention_days"] = retention_days
    if rev_share_policy_id is not None:
        params["rev_share_policy_id"] = rev_share_policy_id
    if rule is not None:
        params["rule"] = rule
    if rule_aggregation is not None:
        params["rule_aggregation"] = rule_aggregation
    if tags is not None:
        params["tags"] = tags
    if use_in_campaigns is not None:
        params["use_in_campaigns"] = use_in_campaigns
    result = await get_client().post(f"{custom_audience_id}", data=params)
    return json.dumps(result, indent=2)

