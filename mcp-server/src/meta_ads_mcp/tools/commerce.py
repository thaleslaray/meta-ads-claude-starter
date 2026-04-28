"""Auto-generated Meta Marketing API tools — commerce."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


COMMERCE_ORDER_FIELDS = [
    "buyer_details",
    "channel",
    "contains_bopis_items",
    "created",
    "estimated_payment_details",
    "id",
    "is_group_buy",
    "is_test_order",
    "last_updated",
    "merchant_order_id",
    "order_status",
    "pre_order_details",
    "selected_shipping_option",
    "ship_by_date",
    "shipping_address"
]


async def create_commerce_order_acknowledge_order(
    commerce_order_id: str,
    idempotency_key: str,
    merchant_order_reference: Optional[str] = None,
) -> str:
    """POST /acknowledge_order on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        idempotency_key: Required.
        merchant_order_reference: Optional.
    """
    params = {}
    params["idempotency_key"] = idempotency_key
    if merchant_order_reference is not None:
        params["merchant_order_reference"] = merchant_order_reference
    result = await get_client().post(f"{commerce_order_id}/acknowledge_order", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_cancellations(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /cancellations on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/cancellations", params=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_cancellations(
    commerce_order_id: str,
    idempotency_key: str,
    cancel_reason: Optional[str] = None,
    items: Optional[str] = None,
    restock_items: Optional[bool] = None,
) -> str:
    """POST /cancellations on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        cancel_reason: Optional.
        idempotency_key: Required.
        items: Optional.
        restock_items: Optional.
    """
    params = {}
    if cancel_reason is not None:
        params["cancel_reason"] = cancel_reason
    params["idempotency_key"] = idempotency_key
    if items is not None:
        params["items"] = items
    if restock_items is not None:
        params["restock_items"] = restock_items
    result = await get_client().post(f"{commerce_order_id}/cancellations", data=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_item_updates(commerce_order_id: str, items: str, merchant_order_reference: str) -> str:
    """POST /item_updates on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        items: Required.
        merchant_order_reference: Required.
    """
    params = {}
    params["items"] = items
    params["merchant_order_reference"] = merchant_order_reference
    result = await get_client().post(f"{commerce_order_id}/item_updates", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_items(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /items on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/items", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_payments(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /payments on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/payments", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_promotion_details(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /promotion_details on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/promotion_details", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_promotions(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /promotions on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/promotions", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_refunds(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /refunds on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/refunds", params=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_refunds(
    commerce_order_id: str,
    idempotency_key: str,
    reason_code: str,
    adjustment_amount: Optional[str] = None,
    deductions: Optional[str] = None,
    items: Optional[str] = None,
    reason_text: Optional[str] = None,
    return_id: Optional[str] = None,
    shipping: Optional[str] = None,
) -> str:
    """POST /refunds on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        adjustment_amount: Optional.
        deductions: Optional.
        idempotency_key: Required.
        items: Optional.
        reason_code: Required. Values: BUYERS_REMORSE, DAMAGED_GOODS, FACEBOOK_INITIATED, NOT_AS_DESCRIBED, QUALITY_ISSUE, REFUND_COMPROMISED, REFUND_FOR_RETURN, REFUND_REASON_OTHER, REFUND_SFI_FAKE, REFUND_SFI_REAL, WRONG_ITEM
        reason_text: Optional.
        return_id: Optional.
        shipping: Optional.
    """
    params = {}
    if adjustment_amount is not None:
        params["adjustment_amount"] = adjustment_amount
    if deductions is not None:
        params["deductions"] = deductions
    params["idempotency_key"] = idempotency_key
    if items is not None:
        params["items"] = items
    params["reason_code"] = reason_code
    if reason_text is not None:
        params["reason_text"] = reason_text
    if return_id is not None:
        params["return_id"] = return_id
    if shipping is not None:
        params["shipping"] = shipping
    result = await get_client().post(f"{commerce_order_id}/refunds", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_returns(
    commerce_order_id: str,
    fields: Optional[str] = None,
    merchant_return_id: Optional[str] = None,
    statuses: Optional[str] = None,
) -> str:
    """GET /returns on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
        merchant_return_id: Optional.
        statuses: Optional. Values: APPROVED, DISAPPROVED, MERCHANT_MARKED_COMPLETED, REFUNDED, REQUESTED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if merchant_return_id is not None:
        params["merchant_return_id"] = merchant_return_id
    if statuses is not None:
        params["statuses"] = statuses
    result = await get_client().get(f"{commerce_order_id}/returns", params=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_returns(
    commerce_order_id: str,
    items: str,
    merchant_return_id: Optional[str] = None,
    return_message: Optional[str] = None,
    update: Optional[str] = None,
) -> str:
    """POST /returns on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        items: Required.
        merchant_return_id: Optional.
        return_message: Optional.
        update: Optional.
    """
    params = {}
    params["items"] = items
    if merchant_return_id is not None:
        params["merchant_return_id"] = merchant_return_id
    if return_message is not None:
        params["return_message"] = return_message
    if update is not None:
        params["update"] = update
    result = await get_client().post(f"{commerce_order_id}/returns", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_shipments(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /shipments on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}/shipments", params=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_shipments(
    commerce_order_id: str,
    idempotency_key: str,
    external_redemption_link: Optional[str] = None,
    external_shipment_id: Optional[str] = None,
    fulfillment: Optional[str] = None,
    items: Optional[str] = None,
    merchant_order_reference: Optional[str] = None,
    shipment_origin_postal_code: Optional[str] = None,
    shipping_tax_details: Optional[str] = None,
    should_use_default_fulfillment_location: Optional[bool] = None,
    tracking_info: Optional[str] = None,
) -> str:
    """POST /shipments on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        external_redemption_link: Optional.
        external_shipment_id: Optional.
        fulfillment: Optional.
        idempotency_key: Required.
        items: Optional.
        merchant_order_reference: Optional.
        shipment_origin_postal_code: Optional.
        shipping_tax_details: Optional.
        should_use_default_fulfillment_location: Optional.
        tracking_info: Optional.
    """
    params = {}
    if external_redemption_link is not None:
        params["external_redemption_link"] = external_redemption_link
    if external_shipment_id is not None:
        params["external_shipment_id"] = external_shipment_id
    if fulfillment is not None:
        params["fulfillment"] = fulfillment
    params["idempotency_key"] = idempotency_key
    if items is not None:
        params["items"] = items
    if merchant_order_reference is not None:
        params["merchant_order_reference"] = merchant_order_reference
    if shipment_origin_postal_code is not None:
        params["shipment_origin_postal_code"] = shipment_origin_postal_code
    if shipping_tax_details is not None:
        params["shipping_tax_details"] = shipping_tax_details
    if should_use_default_fulfillment_location is not None:
        params["should_use_default_fulfillment_location"] = should_use_default_fulfillment_location
    if tracking_info is not None:
        params["tracking_info"] = tracking_info
    result = await get_client().post(f"{commerce_order_id}/shipments", data=params)
    return json.dumps(result, indent=2)


async def create_commerce_order_update_shipment(
    commerce_order_id: str,
    idempotency_key: str,
    tracking_info: str,
    external_shipment_id: Optional[str] = None,
    fulfillment_id: Optional[str] = None,
    shipment_id: Optional[str] = None,
) -> str:
    """POST /update_shipment on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        external_shipment_id: Optional.
        fulfillment_id: Optional.
        idempotency_key: Required.
        shipment_id: Optional.
        tracking_info: Required.
    """
    params = {}
    if external_shipment_id is not None:
        params["external_shipment_id"] = external_shipment_id
    if fulfillment_id is not None:
        params["fulfillment_id"] = fulfillment_id
    params["idempotency_key"] = idempotency_key
    if shipment_id is not None:
        params["shipment_id"] = shipment_id
    params["tracking_info"] = tracking_info
    result = await get_client().post(f"{commerce_order_id}/update_shipment", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_order(commerce_order_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on CommerceOrder.

    Args:
        commerce_order_id: The ID of the CommerceOrder object.
        fields: Comma-separated list of fields to return. Available: buyer_details, channel, contains_bopis_items, created, estimated_payment_details, id, is_group_buy, is_test_order, last_updated, merchant_order_id, order_status, pre_order_details, selected_shipping_option, ship_by_date, shipping_address
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_id}", params=params)
    return json.dumps(result, indent=2)


COMMERCE_MERCHANT_SETTINGS_FIELDS = [
    "checkout_config",
    "checkout_message",
    "contact_email",
    "cta",
    "display_name",
    "facebook_channel",
    "id",
    "instagram_channel",
    "korea_ftc_listing",
    "merchant_page",
    "merchant_status",
    "offsite_iab_checkout_enabled_countries",
    "payment_provider",
    "privacy_policy_localized",
    "return_policy_localized",
    "shops_ads_setup",
    "terms"
]


async def create_commerce_merchant_settings_acknowledge_orders(commerce_merchant_settings_id: str, idempotency_key: str, orders: str) -> str:
    """POST /acknowledge_orders on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        idempotency_key: Required.
        orders: Required.
    """
    params = {}
    params["idempotency_key"] = idempotency_key
    params["orders"] = orders
    result = await get_client().post(f"{commerce_merchant_settings_id}/acknowledge_orders", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_commerce_orders(
    commerce_merchant_settings_id: str,
    fields: Optional[str] = None,
    filters: Optional[str] = None,
    state: Optional[str] = None,
    updated_after: Optional[str] = None,
    updated_before: Optional[str] = None,
) -> str:
    """GET /commerce_orders on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
        filters: Optional. Values: HAS_CANCELLATIONS, HAS_FULFILLMENTS, HAS_REFUNDS, NO_CANCELLATIONS, NO_REFUNDS, NO_SHIPMENTS
        state: Optional. Values: COMPLETED, CREATED, FB_PROCESSING, IN_PROGRESS
        updated_after: Optional.
        updated_before: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if filters is not None:
        params["filters"] = filters
    if state is not None:
        params["state"] = state
    if updated_after is not None:
        params["updated_after"] = updated_after
    if updated_before is not None:
        params["updated_before"] = updated_before
    result = await get_client().get(f"{commerce_merchant_settings_id}/commerce_orders", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_commerce_payouts(
    commerce_merchant_settings_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /commerce_payouts on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{commerce_merchant_settings_id}/commerce_payouts", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_commerce_transactions(
    commerce_merchant_settings_id: str,
    fields: Optional[str] = None,
    end_time: Optional[str] = None,
    payout_reference_id: Optional[str] = None,
    start_time: Optional[str] = None,
) -> str:
    """GET /commerce_transactions on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
        end_time: Optional.
        payout_reference_id: Optional.
        start_time: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time is not None:
        params["end_time"] = end_time
    if payout_reference_id is not None:
        params["payout_reference_id"] = payout_reference_id
    if start_time is not None:
        params["start_time"] = start_time
    result = await get_client().get(f"{commerce_merchant_settings_id}/commerce_transactions", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_order_management_apps(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /order_management_apps on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}/order_management_apps", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_product_catalogs(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /product_catalogs on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}/product_catalogs", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_returns(
    commerce_merchant_settings_id: str,
    fields: Optional[str] = None,
    end_time_created: Optional[str] = None,
    merchant_return_id: Optional[str] = None,
    start_time_created: Optional[str] = None,
    statuses: Optional[str] = None,
) -> str:
    """GET /returns on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
        end_time_created: Optional.
        merchant_return_id: Optional.
        start_time_created: Optional.
        statuses: Optional. Values: APPROVED, DISAPPROVED, MERCHANT_MARKED_COMPLETED, REFUNDED, REQUESTED
    """
    params = {}
    params["fields"] = fields or "id,name"
    if end_time_created is not None:
        params["end_time_created"] = end_time_created
    if merchant_return_id is not None:
        params["merchant_return_id"] = merchant_return_id
    if start_time_created is not None:
        params["start_time_created"] = start_time_created
    if statuses is not None:
        params["statuses"] = statuses
    result = await get_client().get(f"{commerce_merchant_settings_id}/returns", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_setup_status(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /setup_status on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}/setup_status", params=params)
    return json.dumps(result, indent=2)


async def create_commerce_merchant_settings_shipping_profiles(
    commerce_merchant_settings_id: str,
    name: str,
    shipping_destinations: str,
    handling_time: Optional[str] = None,
    is_default: Optional[bool] = None,
    is_default_shipping_profile: Optional[bool] = None,
    reference_id: Optional[str] = None,
) -> str:
    """POST /shipping_profiles on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        handling_time: Optional.
        is_default: Optional.
        is_default_shipping_profile: Optional.
        name: Required.
        reference_id: Optional.
        shipping_destinations: Required.
    """
    params = {}
    if handling_time is not None:
        params["handling_time"] = handling_time
    if is_default is not None:
        params["is_default"] = is_default
    if is_default_shipping_profile is not None:
        params["is_default_shipping_profile"] = is_default_shipping_profile
    params["name"] = name
    if reference_id is not None:
        params["reference_id"] = reference_id
    params["shipping_destinations"] = shipping_destinations
    result = await get_client().post(f"{commerce_merchant_settings_id}/shipping_profiles", data=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_shops(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /shops on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}/shops", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings_tax_settings(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /tax_settings on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}/tax_settings", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_merchant_settings(commerce_merchant_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on CommerceMerchantSettings.

    Args:
        commerce_merchant_settings_id: The ID of the CommerceMerchantSettings object.
        fields: Comma-separated list of fields to return. Available: checkout_config, checkout_message, contact_email, cta, display_name, facebook_channel, id, instagram_channel, korea_ftc_listing, merchant_page, merchant_status, offsite_iab_checkout_enabled_countries, payment_provider, privacy_policy_localized, return_policy_localized, shops_ads_setup, terms
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_merchant_settings_id}", params=params)
    return json.dumps(result, indent=2)


COMMERCE_ORDER_TRANSACTION_DETAIL_FIELDS = [
    "merchant_order_id",
    "net_payment_amount",
    "order_created",
    "order_details",
    "order_id",
    "payout_reference_id",
    "postal_code",
    "processing_fee",
    "state",
    "tax_rate",
    "transaction_date",
    "transaction_type",
    "transfer_id"
]


async def get_commerce_order_transaction_detail_items(commerce_order_transaction_detail_id: str, fields: Optional[str] = None) -> str:
    """GET /items on CommerceOrderTransactionDetail.

    Args:
        commerce_order_transaction_detail_id: The ID of the CommerceOrderTransactionDetail object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_transaction_detail_id}/items", params=params)
    return json.dumps(result, indent=2)


async def get_commerce_order_transaction_detail_tax_details(commerce_order_transaction_detail_id: str, fields: Optional[str] = None) -> str:
    """GET /tax_details on CommerceOrderTransactionDetail.

    Args:
        commerce_order_transaction_detail_id: The ID of the CommerceOrderTransactionDetail object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{commerce_order_transaction_detail_id}/tax_details", params=params)
    return json.dumps(result, indent=2)

