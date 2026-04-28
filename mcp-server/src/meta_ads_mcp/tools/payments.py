"""Auto-generated Meta Marketing API tools — payments."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


PAYMENT_ENGINE_PAYMENT_FIELDS = [
    "actions",
    "application",
    "country",
    "created_time",
    "disputes",
    "fraud_status",
    "fulfillment_status",
    "id",
    "is_from_ad",
    "is_from_page_post",
    "items",
    "payout_foreign_exchange_rate",
    "phone_support_eligible",
    "platform",
    "refundable_amount",
    "request_id",
    "tax",
    "tax_country",
    "test",
    "user"
]


async def create_payment_engine_payment_dispute(payment_engine_payment_id: str, reason: str) -> str:
    """POST /dispute on PaymentEnginePayment.

    Args:
        payment_engine_payment_id: The ID of the PaymentEnginePayment object.
        reason: Required. Values: BANNED_USER, DENIED_REFUND, GRANTED_REPLACEMENT_ITEM
    """
    params = {}
    params["reason"] = reason
    result = await get_client().post(f"{payment_engine_payment_id}/dispute", data=params)
    return json.dumps(result, indent=2)


async def create_payment_engine_payment_refunds(
    payment_engine_payment_id: str,
    amount: float,
    currency: str,
    reason: Optional[str] = None,
) -> str:
    """POST /refunds on PaymentEnginePayment.

    Args:
        payment_engine_payment_id: The ID of the PaymentEnginePayment object.
        amount: Required.
        currency: Required.
        reason: Optional. Values: CUSTOMER_SERVICE, FRIENDLY_FRAUD, MALICIOUS_FRAUD
    """
    params = {}
    params["amount"] = amount
    params["currency"] = currency
    if reason is not None:
        params["reason"] = reason
    result = await get_client().post(f"{payment_engine_payment_id}/refunds", data=params)
    return json.dumps(result, indent=2)


async def get_payment_engine_payment(payment_engine_payment_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on PaymentEnginePayment.

    Args:
        payment_engine_payment_id: The ID of the PaymentEnginePayment object.
        fields: Comma-separated list of fields to return. Available: actions, application, country, created_time, disputes, fraud_status, fulfillment_status, id, is_from_ad, is_from_page_post, items, payout_foreign_exchange_rate, phone_support_eligible, platform, refundable_amount, request_id, tax, tax_country, test, user
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{payment_engine_payment_id}", params=params)
    return json.dumps(result, indent=2)


OMEGA_CUSTOMER_TRX_FIELDS = [
    "ad_account_ids",
    "advertiser_name",
    "amount",
    "amount_due",
    "billed_amount_details",
    "billing_period",
    "cdn_download_uri",
    "currency",
    "download_uri",
    "due_date",
    "entity",
    "id",
    "invoice_date",
    "invoice_id",
    "invoice_type",
    "liability_type",
    "payment_status",
    "payment_term",
    "type"
]


async def get_omega_customer_trx_campaigns(omega_customer_trx_id: str, fields: Optional[str] = None) -> str:
    """GET /campaigns on OmegaCustomerTrx.

    Args:
        omega_customer_trx_id: The ID of the OmegaCustomerTrx object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{omega_customer_trx_id}/campaigns", params=params)
    return json.dumps(result, indent=2)


async def get_omega_customer_trx(omega_customer_trx_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OmegaCustomerTrx.

    Args:
        omega_customer_trx_id: The ID of the OmegaCustomerTrx object.
        fields: Comma-separated list of fields to return. Available: ad_account_ids, advertiser_name, amount, amount_due, billed_amount_details, billing_period, cdn_download_uri, currency, download_uri, due_date, entity, id, invoice_date, invoice_id, invoice_type, liability_type, payment_status, payment_term, type
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{omega_customer_trx_id}", params=params)
    return json.dumps(result, indent=2)

