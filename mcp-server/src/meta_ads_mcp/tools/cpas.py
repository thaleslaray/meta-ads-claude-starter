"""Auto-generated Meta Marketing API tools — cpas."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


CPAS_BUSINESS_SETUP_CONFIG_FIELDS = [
    "accepted_collab_ads_tos",
    "business",
    "business_capabilities_status",
    "capabilities_compliance_status",
    "id"
]


async def get_cpas_business_setup_config_ad_accounts(cpas_business_setup_config_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_accounts on CPASBusinessSetupConfig.

    Args:
        cpas_business_setup_config_id: The ID of the CPASBusinessSetupConfig object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{cpas_business_setup_config_id}/ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def get_cpas_business_setup_config(cpas_business_setup_config_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on CPASBusinessSetupConfig.

    Args:
        cpas_business_setup_config_id: The ID of the CPASBusinessSetupConfig object.
        fields: Comma-separated list of fields to return. Available: accepted_collab_ads_tos, business, business_capabilities_status, capabilities_compliance_status, id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{cpas_business_setup_config_id}", params=params)
    return json.dumps(result, indent=2)


CPAS_LSB_IMAGE_BANK_FIELDS = [
    "ad_group_id",
    "catalog_segment_proxy_id",
    "id"
]


async def get_cpas_lsb_image_bank_backup_images(cpas_lsb_image_bank_id: str, fields: Optional[str] = None) -> str:
    """GET /backup_images on CPASLsbImageBank.

    Args:
        cpas_lsb_image_bank_id: The ID of the CPASLsbImageBank object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{cpas_lsb_image_bank_id}/backup_images", params=params)
    return json.dumps(result, indent=2)


async def get_cpas_lsb_image_bank(cpas_lsb_image_bank_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on CPASLsbImageBank.

    Args:
        cpas_lsb_image_bank_id: The ID of the CPASLsbImageBank object.
        fields: Comma-separated list of fields to return. Available: ad_group_id, catalog_segment_proxy_id, id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{cpas_lsb_image_bank_id}", params=params)
    return json.dumps(result, indent=2)


async def update_cpas_lsb_image_bank(cpas_lsb_image_bank_id: str, backup_image_urls: str) -> str:
    """POST /#update on CPASLsbImageBank.

    Args:
        cpas_lsb_image_bank_id: The ID of the CPASLsbImageBank object.
        backup_image_urls: Required.
    """
    params = {}
    params["backup_image_urls"] = backup_image_urls
    result = await get_client().post(f"{cpas_lsb_image_bank_id}", data=params)
    return json.dumps(result, indent=2)

