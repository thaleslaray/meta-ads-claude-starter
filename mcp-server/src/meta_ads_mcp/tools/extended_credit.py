"""Auto-generated Meta Marketing API tools — extended_credit."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


EXTENDED_CREDIT_FIELDS = [
    "allocated_amount",
    "balance",
    "credit_available",
    "credit_type",
    "id",
    "is_access_revoked",
    "is_automated_experience",
    "legal_entity_name",
    "liable_address",
    "liable_biz_name",
    "max_balance",
    "online_max_balance",
    "owner_business",
    "owner_business_name",
    "partition_from",
    "receiving_credit_allocation_config",
    "send_bill_to_address",
    "send_bill_to_biz_name",
    "sold_to_address"
]


async def get_extended_credit_extended_credit_invoice_groups(extended_credit_id: str, fields: Optional[str] = None) -> str:
    """GET /extended_credit_invoice_groups on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{extended_credit_id}/extended_credit_invoice_groups", params=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_extended_credit_invoice_groups(extended_credit_id: str, emails: str, name: str) -> str:
    """POST /extended_credit_invoice_groups on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        emails: Required.
        name: Required.
    """
    params = {}
    params["emails"] = emails
    params["name"] = name
    result = await get_client().post(f"{extended_credit_id}/extended_credit_invoice_groups", data=params)
    return json.dumps(result, indent=2)


async def get_extended_credit_owning_credit_allocation_configs(
    extended_credit_id: str,
    fields: Optional[str] = None,
    receiving_business_id: Optional[str] = None,
) -> str:
    """GET /owning_credit_allocation_configs on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        fields: Comma-separated list of fields to return.
        receiving_business_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if receiving_business_id is not None:
        params["receiving_business_id"] = receiving_business_id
    result = await get_client().get(f"{extended_credit_id}/owning_credit_allocation_configs", params=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_owning_credit_allocation_configs(
    extended_credit_id: str,
    receiving_business_id: str,
    amount: Optional[str] = None,
    liability_type: Optional[str] = None,
    partition_type: Optional[str] = None,
    send_bill_to: Optional[str] = None,
) -> str:
    """POST /owning_credit_allocation_configs on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        amount: Optional.
        liability_type: Optional. Values: , MSA, Normal, Sequential
        partition_type: Optional. Values: AUTH, FIXED, FIXED_WITHOUT_PARTITION
        receiving_business_id: Required.
        send_bill_to: Optional. Values: , Advertiser, Agency
    """
    params = {}
    if amount is not None:
        params["amount"] = amount
    if liability_type is not None:
        params["liability_type"] = liability_type
    if partition_type is not None:
        params["partition_type"] = partition_type
    params["receiving_business_id"] = receiving_business_id
    if send_bill_to is not None:
        params["send_bill_to"] = send_bill_to
    result = await get_client().post(f"{extended_credit_id}/owning_credit_allocation_configs", data=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_whatsapp_credit_attach(extended_credit_id: str, waba_currency: str, waba_id: str) -> str:
    """POST /whatsapp_credit_attach on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        waba_currency: Required.
        waba_id: Required.
    """
    params = {}
    params["waba_currency"] = waba_currency
    params["waba_id"] = waba_id
    result = await get_client().post(f"{extended_credit_id}/whatsapp_credit_attach", data=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_whatsapp_credit_sharing(extended_credit_id: str, receiving_business_id: str) -> str:
    """POST /whatsapp_credit_sharing on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        receiving_business_id: Required.
    """
    params = {}
    params["receiving_business_id"] = receiving_business_id
    result = await get_client().post(f"{extended_credit_id}/whatsapp_credit_sharing", data=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_whatsapp_credit_sharing_and_attach(extended_credit_id: str, waba_currency: str, waba_id: str) -> str:
    """POST /whatsapp_credit_sharing_and_attach on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        waba_currency: Required.
        waba_id: Required.
    """
    params = {}
    params["waba_currency"] = waba_currency
    params["waba_id"] = waba_id
    result = await get_client().post(f"{extended_credit_id}/whatsapp_credit_sharing_and_attach", data=params)
    return json.dumps(result, indent=2)


async def get_extended_credit(extended_credit_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ExtendedCredit.

    Args:
        extended_credit_id: The ID of the ExtendedCredit object.
        fields: Comma-separated list of fields to return. Available: allocated_amount, balance, credit_available, credit_type, id, is_access_revoked, is_automated_experience, legal_entity_name, liable_address, liable_biz_name, max_balance, online_max_balance, owner_business, owner_business_name, partition_from, receiving_credit_allocation_config, send_bill_to_address, send_bill_to_biz_name, sold_to_address
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{extended_credit_id}", params=params)
    return json.dumps(result, indent=2)


EXTENDED_CREDIT_INVOICE_GROUP_FIELDS = [
    "auto_enroll",
    "bill_to_address",
    "customer_po_number",
    "email",
    "emails",
    "id",
    "liable_address",
    "name",
    "sold_to_address"
]


async def delete_extended_credit_invoice_group_ad_accounts(extended_credit_invoice_group_id: str, ad_account_id: str) -> str:
    """DELETE /ad_accounts on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
        ad_account_id: Required.
    """
    params = {}
    params["ad_account_id"] = ad_account_id
    result = await get_client().delete(f"{extended_credit_invoice_group_id}/ad_accounts")
    return json.dumps(result, indent=2)


async def get_extended_credit_invoice_group_ad_accounts(extended_credit_invoice_group_id: str, fields: Optional[str] = None) -> str:
    """GET /ad_accounts on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{extended_credit_invoice_group_id}/ad_accounts", params=params)
    return json.dumps(result, indent=2)


async def create_extended_credit_invoice_group_ad_accounts(extended_credit_invoice_group_id: str, ad_account_id: str) -> str:
    """POST /ad_accounts on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
        ad_account_id: Required.
    """
    params = {}
    params["ad_account_id"] = ad_account_id
    result = await get_client().post(f"{extended_credit_invoice_group_id}/ad_accounts", data=params)
    return json.dumps(result, indent=2)


async def delete_extended_credit_invoice_group(extended_credit_invoice_group_id: str) -> str:
    """DELETE /#delete on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
    """
    params = {}
    result = await get_client().delete(f"{extended_credit_invoice_group_id}")
    return json.dumps(result, indent=2)


async def get_extended_credit_invoice_group(extended_credit_invoice_group_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
        fields: Comma-separated list of fields to return. Available: auto_enroll, bill_to_address, customer_po_number, email, emails, id, liable_address, name, sold_to_address
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{extended_credit_invoice_group_id}", params=params)
    return json.dumps(result, indent=2)


async def update_extended_credit_invoice_group(
    extended_credit_invoice_group_id: str,
    emails: Optional[str] = None,
    name: Optional[str] = None,
) -> str:
    """POST /#update on ExtendedCreditInvoiceGroup.

    Args:
        extended_credit_invoice_group_id: The ID of the ExtendedCreditInvoiceGroup object.
        emails: Optional.
        name: Optional.
    """
    params = {}
    if emails is not None:
        params["emails"] = emails
    if name is not None:
        params["name"] = name
    result = await get_client().post(f"{extended_credit_invoice_group_id}", data=params)
    return json.dumps(result, indent=2)


EXTENDED_CREDIT_ALLOCATION_CONFIG_FIELDS = [
    "currency_amount",
    "id",
    "liability_type",
    "owning_business",
    "owning_credential",
    "partition_type",
    "receiving_business",
    "receiving_credential",
    "request_status",
    "send_bill_to"
]


async def delete_extended_credit_allocation_config(extended_credit_allocation_config_id: str) -> str:
    """DELETE /#delete on ExtendedCreditAllocationConfig.

    Args:
        extended_credit_allocation_config_id: The ID of the ExtendedCreditAllocationConfig object.
    """
    params = {}
    result = await get_client().delete(f"{extended_credit_allocation_config_id}")
    return json.dumps(result, indent=2)


async def get_extended_credit_allocation_config(extended_credit_allocation_config_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ExtendedCreditAllocationConfig.

    Args:
        extended_credit_allocation_config_id: The ID of the ExtendedCreditAllocationConfig object.
        fields: Comma-separated list of fields to return. Available: currency_amount, id, liability_type, owning_business, owning_credential, partition_type, receiving_business, receiving_credential, request_status, send_bill_to
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{extended_credit_allocation_config_id}", params=params)
    return json.dumps(result, indent=2)


async def update_extended_credit_allocation_config(extended_credit_allocation_config_id: str, amount: Optional[str] = None) -> str:
    """POST /#update on ExtendedCreditAllocationConfig.

    Args:
        extended_credit_allocation_config_id: The ID of the ExtendedCreditAllocationConfig object.
        amount: Optional.
    """
    params = {}
    if amount is not None:
        params["amount"] = amount
    result = await get_client().post(f"{extended_credit_allocation_config_id}", data=params)
    return json.dumps(result, indent=2)

