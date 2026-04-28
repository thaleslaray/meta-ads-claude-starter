"""Auto-generated Meta Marketing API tools — ad_studies."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_STUDY_FIELDS = [
    "business",
    "canceled_time",
    "client_business",
    "cooldown_start_time",
    "created_by",
    "created_time",
    "description",
    "end_time",
    "id",
    "measurement_contact",
    "name",
    "observation_end_time",
    "results_first_available_date",
    "sales_contact",
    "start_time",
    "type",
    "updated_by",
    "updated_time"
]


async def get_ad_study_cells(ad_study_id: str, fields: Optional[str] = None) -> str:
    """GET /cells on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_id}/cells", params=params)
    return json.dumps(result, indent=2)


async def create_ad_study_checkpoint(
    ad_study_id: str,
    checkpoint_data: str,
    checkpoint_name: str,
    component: str,
    instance_id: Optional[str] = None,
    run_id: Optional[str] = None,
) -> str:
    """POST /checkpoint on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        checkpoint_data: Required.
        checkpoint_name: Required.
        component: Required.
        instance_id: Optional.
        run_id: Optional.
    """
    params = {}
    params["checkpoint_data"] = checkpoint_data
    params["checkpoint_name"] = checkpoint_name
    params["component"] = component
    if instance_id is not None:
        params["instance_id"] = instance_id
    if run_id is not None:
        params["run_id"] = run_id
    result = await get_client().post(f"{ad_study_id}/checkpoint", data=params)
    return json.dumps(result, indent=2)


async def get_ad_study_instances(ad_study_id: str, fields: Optional[str] = None) -> str:
    """GET /instances on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_id}/instances", params=params)
    return json.dumps(result, indent=2)


async def create_ad_study_instances(ad_study_id: str, breakdown_key: str, run_id: Optional[str] = None) -> str:
    """POST /instances on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        breakdown_key: Required.
        run_id: Optional.
    """
    params = {}
    params["breakdown_key"] = breakdown_key
    if run_id is not None:
        params["run_id"] = run_id
    result = await get_client().post(f"{ad_study_id}/instances", data=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objectives(ad_study_id: str, fields: Optional[str] = None) -> str:
    """GET /objectives on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_id}/objectives", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_study(ad_study_id: str) -> str:
    """DELETE /#delete on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
    """
    params = {}
    result = await get_client().delete(f"{ad_study_id}")
    return json.dumps(result, indent=2)


async def get_ad_study(ad_study_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
        fields: Comma-separated list of fields to return. Available: business, canceled_time, client_business, cooldown_start_time, created_by, created_time, description, end_time, id, measurement_contact, name, observation_end_time, results_first_available_date, sales_contact, start_time, type, updated_by, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_study(
    ad_study_id: str,
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
    """POST /#update on AdStudy.

    Args:
        ad_study_id: The ID of the AdStudy object.
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
        type_: Optional.
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
    result = await get_client().post(f"{ad_study_id}", data=params)
    return json.dumps(result, indent=2)


AD_STUDY_OBJECTIVE_FIELDS = [
    "id",
    "is_primary",
    "last_updated_results",
    "name",
    "results",
    "type"
]


async def get_ad_study_objective_adspixels(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /adspixels on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/adspixels", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_applications(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /applications on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/applications", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_brand_requests(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /brand_requests on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/brand_requests", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_customconversions(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /customconversions on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/customconversions", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_offline_conversion_data_sets(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /offline_conversion_data_sets on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/offline_conversion_data_sets", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_partner_private_studies(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /partner_private_studies on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/partner_private_studies", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective_partnerstudies(ad_study_objective_id: str, fields: Optional[str] = None) -> str:
    """GET /partnerstudies on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_objective_id}/partnerstudies", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_objective(
    ad_study_objective_id: str,
    fields: Optional[str] = None,
    breakdowns: Optional[str] = None,
    ds: Optional[str] = None,
) -> str:
    """GET /#get on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        fields: Comma-separated list of fields to return. Available: id, is_primary, last_updated_results, name, results, type
        breakdowns: Optional.
        ds: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if ds is not None:
        params["ds"] = ds
    result = await get_client().get(f"{ad_study_objective_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_study_objective(
    ad_study_objective_id: str,
    adspixels: Optional[str] = None,
    applications: Optional[str] = None,
    customconversions: Optional[str] = None,
    is_primary: Optional[bool] = None,
    name: Optional[str] = None,
    offline_conversion_data_sets: Optional[str] = None,
    offsite_datasets: Optional[str] = None,
    product_catalogs: Optional[str] = None,
    product_sets: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """POST /#update on AdStudyObjective.

    Args:
        ad_study_objective_id: The ID of the AdStudyObjective object.
        adspixels: Optional.
        applications: Optional.
        customconversions: Optional.
        is_primary: Optional.
        name: Optional.
        offline_conversion_data_sets: Optional.
        offsite_datasets: Optional.
        product_catalogs: Optional.
        product_sets: Optional.
        type_: Optional.
    """
    params = {}
    if adspixels is not None:
        params["adspixels"] = adspixels
    if applications is not None:
        params["applications"] = applications
    if customconversions is not None:
        params["customconversions"] = customconversions
    if is_primary is not None:
        params["is_primary"] = is_primary
    if name is not None:
        params["name"] = name
    if offline_conversion_data_sets is not None:
        params["offline_conversion_data_sets"] = offline_conversion_data_sets
    if offsite_datasets is not None:
        params["offsite_datasets"] = offsite_datasets
    if product_catalogs is not None:
        params["product_catalogs"] = product_catalogs
    if product_sets is not None:
        params["product_sets"] = product_sets
    if type_ is not None:
        params["type"] = type_
    result = await get_client().post(f"{ad_study_objective_id}", data=params)
    return json.dumps(result, indent=2)


AD_STUDY_CELL_FIELDS = [
    "ad_entities_count",
    "control_percentage",
    "id",
    "name",
    "treatment_percentage"
]


async def get_ad_study_cell_adaccounts(ad_study_cell_id: str, fields: Optional[str] = None) -> str:
    """GET /adaccounts on AdStudyCell.

    Args:
        ad_study_cell_id: The ID of the AdStudyCell object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_cell_id}/adaccounts", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_cell_adsets(ad_study_cell_id: str, fields: Optional[str] = None) -> str:
    """GET /adsets on AdStudyCell.

    Args:
        ad_study_cell_id: The ID of the AdStudyCell object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_cell_id}/adsets", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_cell_campaigns(ad_study_cell_id: str, fields: Optional[str] = None) -> str:
    """GET /campaigns on AdStudyCell.

    Args:
        ad_study_cell_id: The ID of the AdStudyCell object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_cell_id}/campaigns", params=params)
    return json.dumps(result, indent=2)


async def get_ad_study_cell(ad_study_cell_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdStudyCell.

    Args:
        ad_study_cell_id: The ID of the AdStudyCell object.
        fields: Comma-separated list of fields to return. Available: ad_entities_count, control_percentage, id, name, treatment_percentage
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_study_cell_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_study_cell(
    ad_study_cell_id: str,
    adaccounts: Optional[str] = None,
    adsets: Optional[str] = None,
    campaigns: Optional[str] = None,
    creation_template: Optional[str] = None,
    description: Optional[str] = None,
    name: Optional[str] = None,
) -> str:
    """POST /#update on AdStudyCell.

    Args:
        ad_study_cell_id: The ID of the AdStudyCell object.
        adaccounts: Optional.
        adsets: Optional.
        campaigns: Optional.
        creation_template: Optional.
        description: Optional.
        name: Optional.
    """
    params = {}
    if adaccounts is not None:
        params["adaccounts"] = adaccounts
    if adsets is not None:
        params["adsets"] = adsets
    if campaigns is not None:
        params["campaigns"] = campaigns
    if creation_template is not None:
        params["creation_template"] = creation_template
    if description is not None:
        params["description"] = description
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"{ad_study_cell_id}", data=params)
    return json.dumps(result, indent=2)

