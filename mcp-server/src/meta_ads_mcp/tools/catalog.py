"""Auto-generated Meta Marketing API tools — catalog."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


PRODUCT_CATALOG_FIELDS = [
    "ad_account_to_collaborative_ads_share_settings",
    "agency_collaborative_ads_share_settings",
    "business",
    "catalog_store",
    "commerce_merchant_settings",
    "creator_user",
    "da_display_settings",
    "default_image_url",
    "fallback_image_url",
    "feed_count",
    "id",
    "is_catalog_segment",
    "is_local_catalog",
    "name",
    "owner_business",
    "product_count",
    "store_catalog_settings",
    "user_access_expire_time",
    "vertical"
]


async def delete_product_catalog_agencies(product_catalog_id: str, business: str) -> str:
    """DELETE /agencies on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        business: Required.
    """
    params = {}
    params["business"] = business
    result = await get_client().delete(f"{product_catalog_id}/agencies")
    return json.dumps(result, indent=2)


async def get_product_catalog_agencies(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /agencies on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/agencies", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_agencies(
    product_catalog_id: str,
    business: str,
    enabled_collab_terms: Optional[str] = None,
    permitted_roles: Optional[str] = None,
    permitted_tasks: Optional[str] = None,
    skip_defaults: Optional[bool] = None,
    utm_settings: Optional[str] = None,
) -> str:
    """POST /agencies on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        business: Required.
        enabled_collab_terms: Optional. Values: ENFORCE_CREATE_NEW_AD_ACCOUNT, ENFORCE_SHARE_AD_PERFORMANCE_ACCESS
        permitted_roles: Optional. Values: ADMIN, ADVERTISER
        permitted_tasks: Optional. Values: AA_ANALYZE, ADVERTISE, MANAGE, MANAGE_AR
        skip_defaults: Optional.
        utm_settings: Optional.
    """
    params = {}
    params["business"] = business
    if enabled_collab_terms is not None:
        params["enabled_collab_terms"] = enabled_collab_terms
    if permitted_roles is not None:
        params["permitted_roles"] = permitted_roles
    if permitted_tasks is not None:
        params["permitted_tasks"] = permitted_tasks
    if skip_defaults is not None:
        params["skip_defaults"] = skip_defaults
    if utm_settings is not None:
        params["utm_settings"] = utm_settings
    result = await get_client().post(f"{product_catalog_id}/agencies", data=params)
    return json.dumps(result, indent=2)


async def delete_product_catalog_assigned_users(product_catalog_id: str, user: int) -> str:
    """DELETE /assigned_users on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        user: Required.
    """
    params = {}
    params["user"] = user
    result = await get_client().delete(f"{product_catalog_id}/assigned_users")
    return json.dumps(result, indent=2)


async def get_product_catalog_assigned_users(product_catalog_id: str, business: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        business: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["business"] = business
    result = await get_client().get(f"{product_catalog_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_assigned_users(product_catalog_id: str, tasks: str, user: int) -> str:
    """POST /assigned_users on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        tasks: Required. Values: AA_ANALYZE, ADVERTISE, MANAGE, MANAGE_AR
        user: Required.
    """
    params = {}
    params["tasks"] = tasks
    params["user"] = user
    result = await get_client().post(f"{product_catalog_id}/assigned_users", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_automotive_models(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /automotive_models on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/automotive_models", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_batch(
    product_catalog_id: str,
    requests: str,
    allow_upsert: Optional[bool] = None,
    fbe_external_business_id: Optional[str] = None,
    version: Optional[int] = None,
) -> str:
    """POST /batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_upsert: Optional.
        fbe_external_business_id: Optional.
        requests: Required.
        version: Optional.
    """
    params = {}
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    if fbe_external_business_id is not None:
        params["fbe_external_business_id"] = fbe_external_business_id
    params["requests"] = requests
    if version is not None:
        params["version"] = version
    result = await get_client().post(f"{product_catalog_id}/batch", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_catalog_store(product_catalog_id: str, page: str) -> str:
    """POST /catalog_store on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        page: Required.
    """
    params = {}
    params["page"] = page
    result = await get_client().post(f"{product_catalog_id}/catalog_store", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_categories(
    product_catalog_id: str,
    categorization_criteria: str,
    fields: Optional[str] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /categories on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        categorization_criteria: Required. Values: BRAND, CATEGORY, PRODUCT_TYPE
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["categorization_criteria"] = categorization_criteria
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/categories", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_categories(product_catalog_id: str, data: str) -> str:
    """POST /categories on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        data: Required.
    """
    params = {}
    params["data"] = data
    result = await get_client().post(f"{product_catalog_id}/categories", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_check_batch_request_status(
    product_catalog_id: str,
    handle: str,
    fields: Optional[str] = None,
    error_priority: Optional[str] = None,
    load_ids_of_invalid_requests: Optional[bool] = None,
) -> str:
    """GET /check_batch_request_status on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        error_priority: Optional. Values: HIGH, LOW, MEDIUM
        handle: Required.
        load_ids_of_invalid_requests: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if error_priority is not None:
        params["error_priority"] = error_priority
    params["handle"] = handle
    if load_ids_of_invalid_requests is not None:
        params["load_ids_of_invalid_requests"] = load_ids_of_invalid_requests
    result = await get_client().get(f"{product_catalog_id}/check_batch_request_status", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_check_marketplace_partner_deals_status(product_catalog_id: str, session_id: str, fields: Optional[str] = None) -> str:
    """GET /check_marketplace_partner_deals_status on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        session_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["session_id"] = session_id
    result = await get_client().get(f"{product_catalog_id}/check_marketplace_partner_deals_status", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_check_marketplace_partner_sellers_status(product_catalog_id: str, session_id: str, fields: Optional[str] = None) -> str:
    """GET /check_marketplace_partner_sellers_status on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        session_id: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["session_id"] = session_id
    result = await get_client().get(f"{product_catalog_id}/check_marketplace_partner_sellers_status", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_collaborative_ads_lsb_image_bank(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /collaborative_ads_lsb_image_bank on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/collaborative_ads_lsb_image_bank", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_collaborative_ads_share_settings(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /collaborative_ads_share_settings on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/collaborative_ads_share_settings", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_cpas_lsb_image_bank(
    product_catalog_id: str,
    backup_image_urls: str,
    ad_group_id: Optional[int] = None,
    agency_business_id: Optional[int] = None,
) -> str:
    """POST /cpas_lsb_image_bank on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        ad_group_id: Optional.
        agency_business_id: Optional.
        backup_image_urls: Required.
    """
    params = {}
    if ad_group_id is not None:
        params["ad_group_id"] = ad_group_id
    if agency_business_id is not None:
        params["agency_business_id"] = agency_business_id
    params["backup_image_urls"] = backup_image_urls
    result = await get_client().post(f"{product_catalog_id}/cpas_lsb_image_bank", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_creator_asset_creatives(
    product_catalog_id: str,
    fields: Optional[str] = None,
    moderation_status: Optional[str] = None,
) -> str:
    """GET /creator_asset_creatives on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        moderation_status: Optional. Values: ARCHIVED, ELIGIBLE, EXPIRED, INELIGIBLE, IN_REVIEW, PAUSED, UNKNOWN
    """
    params = {}
    params["fields"] = fields or "id,name"
    if moderation_status is not None:
        params["moderation_status"] = moderation_status
    result = await get_client().get(f"{product_catalog_id}/creator_asset_creatives", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_data_sources(
    product_catalog_id: str,
    fields: Optional[str] = None,
    ingestion_source_type: Optional[str] = None,
) -> str:
    """GET /data_sources on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        ingestion_source_type: Optional. Values: ALL, PRIMARY, SUPPLEMENTARY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ingestion_source_type is not None:
        params["ingestion_source_type"] = ingestion_source_type
    result = await get_client().get(f"{product_catalog_id}/data_sources", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_destinations(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /destinations on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/destinations", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_diagnostics(
    product_catalog_id: str,
    fields: Optional[str] = None,
    affected_channels: Optional[str] = None,
    affected_entities: Optional[str] = None,
    affected_features: Optional[str] = None,
    severities: Optional[str] = None,
    types: Optional[str] = None,
) -> str:
    """GET /diagnostics on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        affected_channels: Optional. Values: b2c_marketplace, c2c_marketplace, da, daily_deals, daily_deals_legacy, ig_product_tagging, marketplace, marketplace_ads_deprecated, marketplace_shops, mini_shops, offline_conversions, shops, universal_checkout, whatsapp
        affected_entities: Optional. Values: product_catalog, product_event, product_item, product_set
        affected_features: Optional. Values: augmented_reality, checkout
        severities: Optional. Values: MUST_FIX, OPPORTUNITY
        types: Optional. Values: AR_VISIBILITY_ISSUES, ATTRIBUTES_INVALID, ATTRIBUTES_MISSING, CATEGORY, CHECKOUT, DA_VISIBILITY_ISSUES, EVENT_SOURCE_ISSUES, IMAGE_QUALITY, LOW_QUALITY_TITLE_AND_DESCRIPTION, POLICY_VIOLATION, SHOPS_VISIBILITY_ISSUES
    """
    params = {}
    params["fields"] = fields or "id,name"
    if affected_channels is not None:
        params["affected_channels"] = affected_channels
    if affected_entities is not None:
        params["affected_entities"] = affected_entities
    if affected_features is not None:
        params["affected_features"] = affected_features
    if severities is not None:
        params["severities"] = severities
    if types is not None:
        params["types"] = types
    result = await get_client().get(f"{product_catalog_id}/diagnostics", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_event_stats(
    product_catalog_id: str,
    fields: Optional[str] = None,
    breakdowns: Optional[str] = None,
) -> str:
    """GET /event_stats on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        breakdowns: Optional. Values: DEVICE_TYPE
    """
    params = {}
    params["fields"] = fields or "id,name"
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    result = await get_client().get(f"{product_catalog_id}/event_stats", params=params)
    return json.dumps(result, indent=2)


async def delete_product_catalog_external_event_sources(product_catalog_id: str, external_event_sources: Optional[str] = None) -> str:
    """DELETE /external_event_sources on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        external_event_sources: Optional.
    """
    params = {}
    if external_event_sources is not None:
        params["external_event_sources"] = external_event_sources
    result = await get_client().delete(f"{product_catalog_id}/external_event_sources")
    return json.dumps(result, indent=2)


async def get_product_catalog_external_event_sources(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /external_event_sources on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/external_event_sources", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_external_event_sources(product_catalog_id: str, external_event_sources: Optional[str] = None) -> str:
    """POST /external_event_sources on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        external_event_sources: Optional.
    """
    params = {}
    if external_event_sources is not None:
        params["external_event_sources"] = external_event_sources
    result = await get_client().post(f"{product_catalog_id}/external_event_sources", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_flights(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /flights on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/flights", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_geolocated_items_batch(
    product_catalog_id: str,
    item_type: str,
    requests: str,
    allow_upsert: Optional[bool] = None,
) -> str:
    """POST /geolocated_items_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_upsert: Optional.
        item_type: Required.
        requests: Required.
    """
    params = {}
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    params["item_type"] = item_type
    params["requests"] = requests
    result = await get_client().post(f"{product_catalog_id}/geolocated_items_batch", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_home_listings(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /home_listings on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/home_listings", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_home_listings(
    product_catalog_id: str,
    address: str,
    availability: str,
    currency: str,
    home_listing_id: str,
    images: str,
    name: str,
    price: float,
    url: str,
    year_built: int,
    description: Optional[str] = None,
    listing_type: Optional[str] = None,
    num_baths: Optional[float] = None,
    num_beds: Optional[float] = None,
    num_units: Optional[float] = None,
    property_type: Optional[str] = None,
) -> str:
    """POST /home_listings on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        address: Required.
        availability: Required.
        currency: Required.
        description: Optional.
        home_listing_id: Required.
        images: Required.
        listing_type: Optional.
        name: Required.
        num_baths: Optional.
        num_beds: Optional.
        num_units: Optional.
        price: Required.
        property_type: Optional.
        url: Required.
        year_built: Required.
    """
    params = {}
    params["address"] = address
    params["availability"] = availability
    params["currency"] = currency
    if description is not None:
        params["description"] = description
    params["home_listing_id"] = home_listing_id
    params["images"] = images
    if listing_type is not None:
        params["listing_type"] = listing_type
    params["name"] = name
    if num_baths is not None:
        params["num_baths"] = num_baths
    if num_beds is not None:
        params["num_beds"] = num_beds
    if num_units is not None:
        params["num_units"] = num_units
    params["price"] = price
    if property_type is not None:
        params["property_type"] = property_type
    params["url"] = url
    params["year_built"] = year_built
    result = await get_client().post(f"{product_catalog_id}/home_listings", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_hotel_rooms_batch(product_catalog_id: str, handle: str, fields: Optional[str] = None) -> str:
    """GET /hotel_rooms_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        handle: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["handle"] = handle
    result = await get_client().get(f"{product_catalog_id}/hotel_rooms_batch", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_hotel_rooms_batch(
    product_catalog_id: str,
    standard: str,
    file: Optional[str] = None,
    password: Optional[str] = None,
    update_only: Optional[bool] = None,
    url: Optional[str] = None,
    username: Optional[str] = None,
) -> str:
    """POST /hotel_rooms_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        file: Optional.
        password: Optional.
        standard: Required. Values: google
        update_only: Optional.
        url: Optional.
        username: Optional.
    """
    params = {}
    if file is not None:
        params["file"] = file
    if password is not None:
        params["password"] = password
    params["standard"] = standard
    if update_only is not None:
        params["update_only"] = update_only
    if url is not None:
        params["url"] = url
    if username is not None:
        params["username"] = username
    result = await get_client().post(f"{product_catalog_id}/hotel_rooms_batch", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_hotels(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /hotels on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/hotels", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_hotels(
    product_catalog_id: str,
    address: str,
    description: str,
    images: str,
    name: str,
    url: str,
    applinks: Optional[str] = None,
    base_price: Optional[int] = None,
    brand: Optional[str] = None,
    currency: Optional[str] = None,
    guest_ratings: Optional[str] = None,
    hotel_id: Optional[str] = None,
    phone: Optional[str] = None,
    star_rating: Optional[float] = None,
) -> str:
    """POST /hotels on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        address: Required.
        applinks: Optional.
        base_price: Optional.
        brand: Optional.
        currency: Optional.
        description: Required.
        guest_ratings: Optional.
        hotel_id: Optional.
        images: Required.
        name: Required.
        phone: Optional.
        star_rating: Optional.
        url: Required.
    """
    params = {}
    params["address"] = address
    if applinks is not None:
        params["applinks"] = applinks
    if base_price is not None:
        params["base_price"] = base_price
    if brand is not None:
        params["brand"] = brand
    if currency is not None:
        params["currency"] = currency
    params["description"] = description
    if guest_ratings is not None:
        params["guest_ratings"] = guest_ratings
    if hotel_id is not None:
        params["hotel_id"] = hotel_id
    params["images"] = images
    params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if star_rating is not None:
        params["star_rating"] = star_rating
    params["url"] = url
    result = await get_client().post(f"{product_catalog_id}/hotels", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_items_batch(
    product_catalog_id: str,
    item_type: str,
    requests: str,
    allow_upsert: Optional[bool] = None,
    item_sub_type: Optional[str] = None,
    version: Optional[int] = None,
) -> str:
    """POST /items_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_upsert: Optional.
        item_sub_type: Optional. Values: APPLIANCES, BABY_FEEDING, BABY_TRANSPORT, BEAUTY, BEDDING, CAMERAS, CELL_PHONES_AND_SMART_WATCHES, CLEANING_SUPPLIES, CLOTHING, CLOTHING_ACCESSORIES, COMPUTERS_AND_TABLETS, DIAPERING_AND_POTTY_TRAINING, ELECTRONICS_ACCESSORIES, FURNITURE, HEALTH, HOME_GOODS, JEWELRY, NURSERY, PRINTERS_AND_SCANNERS, PROJECTORS, SHOES_AND_FOOTWEAR, SOFTWARE, TOYS, TVS_AND_MONITORS, VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES, WATCHES
        item_type: Required.
        requests: Required.
        version: Optional.
    """
    params = {}
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    if item_sub_type is not None:
        params["item_sub_type"] = item_sub_type
    params["item_type"] = item_type
    params["requests"] = requests
    if version is not None:
        params["version"] = version
    result = await get_client().post(f"{product_catalog_id}/items_batch", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_localized_items_batch(
    product_catalog_id: str,
    item_type: str,
    requests: str,
    allow_upsert: Optional[bool] = None,
    version: Optional[int] = None,
) -> str:
    """POST /localized_items_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_upsert: Optional.
        item_type: Required.
        requests: Required.
        version: Optional.
    """
    params = {}
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    params["item_type"] = item_type
    params["requests"] = requests
    if version is not None:
        params["version"] = version
    result = await get_client().post(f"{product_catalog_id}/localized_items_batch", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_marketplace_partner_deals_details(product_catalog_id: str, requests: str) -> str:
    """POST /marketplace_partner_deals_details on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        requests: Required.
    """
    params = {}
    params["requests"] = requests
    result = await get_client().post(f"{product_catalog_id}/marketplace_partner_deals_details", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_marketplace_partner_sellers_details(product_catalog_id: str, requests: str) -> str:
    """POST /marketplace_partner_sellers_details on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        requests: Required.
    """
    params = {}
    params["requests"] = requests
    result = await get_client().post(f"{product_catalog_id}/marketplace_partner_sellers_details", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_marketplace_partner_signals(
    product_catalog_id: str,
    event_name: str,
    event_time: str,
    user_data: str,
    event_source_url: Optional[str] = None,
    order_data: Optional[str] = None,
) -> str:
    """POST /marketplace_partner_signals on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        event_name: Required. Values: ADD_TO_CART, PURCHASE, TEST, VIEW_ITEM
        event_source_url: Optional.
        event_time: Required.
        order_data: Optional.
        user_data: Required.
    """
    params = {}
    params["event_name"] = event_name
    if event_source_url is not None:
        params["event_source_url"] = event_source_url
    params["event_time"] = event_time
    if order_data is not None:
        params["order_data"] = order_data
    params["user_data"] = user_data
    result = await get_client().post(f"{product_catalog_id}/marketplace_partner_signals", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_pricing_variables_batch(product_catalog_id: str, handle: str, fields: Optional[str] = None) -> str:
    """GET /pricing_variables_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        handle: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["handle"] = handle
    result = await get_client().get(f"{product_catalog_id}/pricing_variables_batch", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_pricing_variables_batch(
    product_catalog_id: str,
    standard: str,
    file: Optional[str] = None,
    password: Optional[str] = None,
    update_only: Optional[bool] = None,
    url: Optional[str] = None,
    username: Optional[str] = None,
) -> str:
    """POST /pricing_variables_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        file: Optional.
        password: Optional.
        standard: Required. Values: google
        update_only: Optional.
        url: Optional.
        username: Optional.
    """
    params = {}
    if file is not None:
        params["file"] = file
    if password is not None:
        params["password"] = password
    params["standard"] = standard
    if update_only is not None:
        params["update_only"] = update_only
    if url is not None:
        params["url"] = url
    if username is not None:
        params["username"] = username
    result = await get_client().post(f"{product_catalog_id}/pricing_variables_batch", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_product_feeds(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /product_feeds on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/product_feeds", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_product_feeds(
    product_catalog_id: str,
    country: Optional[str] = None,
    default_currency: Optional[str] = None,
    deletion_enabled: Optional[bool] = None,
    delimiter: Optional[str] = None,
    encoding: Optional[str] = None,
    feed_type: Optional[str] = None,
    file_name: Optional[str] = None,
    ingestion_source_type: Optional[str] = None,
    item_sub_type: Optional[str] = None,
    migrated_from_feed_id: Optional[str] = None,
    name: Optional[str] = None,
    override_type: Optional[str] = None,
    override_value: Optional[str] = None,
    primary_feed_ids: Optional[str] = None,
    quoted_fields_mode: Optional[str] = None,
    rules: Optional[str] = None,
    schedule: Optional[str] = None,
    selected_override_fields: Optional[str] = None,
    update_schedule: Optional[str] = None,
    use_case: Optional[str] = None,
) -> str:
    """POST /product_feeds on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        country: Optional.
        default_currency: Optional.
        deletion_enabled: Optional.
        delimiter: Optional. Values: AUTODETECT, BAR, COMMA, SEMICOLON, TAB, TILDE
        encoding: Optional. Values: AUTODETECT, LATIN1, UTF16BE, UTF16LE, UTF32BE, UTF32LE, UTF8
        feed_type: Optional. Values: AUTOMOTIVE_MODEL, COLLECTION, DESTINATION, FLIGHT, HOME_LISTING, HOTEL, HOTEL_ROOM, LOCAL_INVENTORY, MEDIA_TITLE, OFFER, PRODUCTS, PRODUCT_RATINGS_AND_REVIEWS, TRANSACTABLE_ITEMS, VEHICLES, VEHICLE_OFFER
        file_name: Optional.
        ingestion_source_type: Optional. Values: PRIMARY_FEED, SUPPLEMENTARY_FEED
        item_sub_type: Optional. Values: APPLIANCES, BABY_FEEDING, BABY_TRANSPORT, BEAUTY, BEDDING, CAMERAS, CELL_PHONES_AND_SMART_WATCHES, CLEANING_SUPPLIES, CLOTHING, CLOTHING_ACCESSORIES, COMPUTERS_AND_TABLETS, DIAPERING_AND_POTTY_TRAINING, ELECTRONICS_ACCESSORIES, FURNITURE, HEALTH, HOME_GOODS, JEWELRY, NURSERY, PRINTERS_AND_SCANNERS, PROJECTORS, SHOES_AND_FOOTWEAR, SOFTWARE, TOYS, TVS_AND_MONITORS, VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES, WATCHES
        migrated_from_feed_id: Optional.
        name: Optional.
        override_type: Optional. Values: BATCH_API_LANGUAGE_OR_COUNTRY, CATALOG_SEGMENT_CUSTOMIZE_DEFAULT, COUNTRY, LANGUAGE, LANGUAGE_AND_COUNTRY, LOCAL, SMART_PIXEL_LANGUAGE_OR_COUNTRY, VERSION
        override_value: Optional.
        primary_feed_ids: Optional.
        quoted_fields_mode: Optional. Values: autodetect, off, on
        rules: Optional.
        schedule: Optional.
        selected_override_fields: Optional.
        update_schedule: Optional.
        use_case: Optional. Values: CREATOR_ASSET
    """
    params = {}
    if country is not None:
        params["country"] = country
    if default_currency is not None:
        params["default_currency"] = default_currency
    if deletion_enabled is not None:
        params["deletion_enabled"] = deletion_enabled
    if delimiter is not None:
        params["delimiter"] = delimiter
    if encoding is not None:
        params["encoding"] = encoding
    if feed_type is not None:
        params["feed_type"] = feed_type
    if file_name is not None:
        params["file_name"] = file_name
    if ingestion_source_type is not None:
        params["ingestion_source_type"] = ingestion_source_type
    if item_sub_type is not None:
        params["item_sub_type"] = item_sub_type
    if migrated_from_feed_id is not None:
        params["migrated_from_feed_id"] = migrated_from_feed_id
    if name is not None:
        params["name"] = name
    if override_type is not None:
        params["override_type"] = override_type
    if override_value is not None:
        params["override_value"] = override_value
    if primary_feed_ids is not None:
        params["primary_feed_ids"] = primary_feed_ids
    if quoted_fields_mode is not None:
        params["quoted_fields_mode"] = quoted_fields_mode
    if rules is not None:
        params["rules"] = rules
    if schedule is not None:
        params["schedule"] = schedule
    if selected_override_fields is not None:
        params["selected_override_fields"] = selected_override_fields
    if update_schedule is not None:
        params["update_schedule"] = update_schedule
    if use_case is not None:
        params["use_case"] = use_case
    result = await get_client().post(f"{product_catalog_id}/product_feeds", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_product_groups(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /product_groups on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/product_groups", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_product_groups(
    product_catalog_id: str,
    retailer_id: Optional[str] = None,
    variants: Optional[str] = None,
) -> str:
    """POST /product_groups on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        retailer_id: Optional.
        variants: Optional.
    """
    params = {}
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    if variants is not None:
        params["variants"] = variants
    result = await get_client().post(f"{product_catalog_id}/product_groups", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_product_sets(
    product_catalog_id: str,
    fields: Optional[str] = None,
    ancestor_id: Optional[str] = None,
    has_children: Optional[bool] = None,
    parent_id: Optional[str] = None,
    retailer_id: Optional[str] = None,
) -> str:
    """GET /product_sets on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        ancestor_id: Optional.
        has_children: Optional.
        parent_id: Optional.
        retailer_id: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if ancestor_id is not None:
        params["ancestor_id"] = ancestor_id
    if has_children is not None:
        params["has_children"] = has_children
    if parent_id is not None:
        params["parent_id"] = parent_id
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    result = await get_client().get(f"{product_catalog_id}/product_sets", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_product_sets(
    product_catalog_id: str,
    name: str,
    filter_: Optional[str] = None,
    metadata: Optional[str] = None,
    ordering_info: Optional[str] = None,
    publish_to_shops: Optional[str] = None,
    retailer_id: Optional[str] = None,
) -> str:
    """POST /product_sets on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        filter_: Optional.
        metadata: Optional.
        name: Required.
        ordering_info: Optional.
        publish_to_shops: Optional.
        retailer_id: Optional.
    """
    params = {}
    if filter_ is not None:
        params["filter"] = filter_
    if metadata is not None:
        params["metadata"] = metadata
    params["name"] = name
    if ordering_info is not None:
        params["ordering_info"] = ordering_info
    if publish_to_shops is not None:
        params["publish_to_shops"] = publish_to_shops
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    result = await get_client().post(f"{product_catalog_id}/product_sets", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_product_sets_batch(product_catalog_id: str, handle: str, fields: Optional[str] = None) -> str:
    """GET /product_sets_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        handle: Required.
    """
    params = {}
    params["fields"] = fields or "id,name"
    params["handle"] = handle
    result = await get_client().get(f"{product_catalog_id}/product_sets_batch", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_products(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    error_priority: Optional[str] = None,
    error_type: Optional[str] = None,
    filter_: Optional[str] = None,
    return_only_approved_products: Optional[bool] = None,
) -> str:
    """GET /products on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        error_priority: Optional. Values: HIGH, LOW, MEDIUM
        error_type: Optional. Values: ADDRESS_BLOCKLISTED_IN_MARKET, AGGREGATED_LOCALIZATION_ISSUES, APP_HAS_NO_AEM_SETUP, AR_DELETED_DUE_TO_UPDATE, AR_POLICY_VIOLATED, AVAILABLE, BAD_QUALITY_IMAGE, BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK, BIZ_MSG_AI_AGENT_DISABLED_BY_USER, BIZ_MSG_GEN_AI_POLICY_VIOLATED, CANNOT_EDIT_SUBSCRIPTION_PRODUCTS, CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE, CHECKOUT_DISABLED_BY_USER, COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID, COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT, CRAWLED_AVAILABILITY_MISMATCH, DA_DISABLED_BY_USER, DA_POLICY_VIOLATION, DELETED_ITEM, DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT, DUPLICATE_IMAGES, DUPLICATE_TITLE_AND_DESCRIPTION, EMPTY_AVAILABILITY, EMPTY_CONDITION, EMPTY_DESCRIPTION, EMPTY_IMAGE_URL, EMPTY_PRICE, EMPTY_PRODUCT_URL, EMPTY_SELLER_DESCRIPTION, EMPTY_TITLE, EXTERNAL_MERCHANT_ID_MISMATCH, GENERIC_INVALID_FIELD, GROUPS_DISABLED_BY_USER, HIDDEN_UNTIL_PRODUCT_LAUNCH, ILLEGAL_PRODUCT_CATEGORY, IMAGE_FETCH_FAILED, IMAGE_FETCH_FAILED_BAD_GATEWAY, IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED, IMAGE_FETCH_FAILED_FORBIDDEN, IMAGE_FETCH_FAILED_LINK_BROKEN, IMAGE_FETCH_FAILED_TIMED_OUT, IMAGE_RESOLUTION_LOW, INACTIVE_SHOPIFY_PRODUCT, INVALID_COMMERCE_TAX_CATEGORY, INVALID_CONSOLIDATED_LOCALITY_INFORMATION, INVALID_CONTENT_ID, INVALID_DEALER_COMMUNICATION_PARAMETERS, INVALID_DMA_CODES, INVALID_FB_PAGE_ID, INVALID_IMAGES, INVALID_MONETIZER_RETURN_POLICY, INVALID_OFFER_DISCLAIMER_URL, INVALID_OFFER_END_DATE, INVALID_PRE_ORDER_PARAMS, INVALID_RANGE_FOR_AREA_SIZE, INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE, INVALID_RANGE_FOR_NUM_OF_BATHS, INVALID_RANGE_FOR_NUM_OF_BEDS, INVALID_RANGE_FOR_NUM_OF_ROOMS, INVALID_RANGE_FOR_PARKING_SPACES, INVALID_SHELTER_PAGE_ID, INVALID_SHIPPING_PROFILE_PARAMS, INVALID_SUBSCRIPTION_DISABLE_PARAMS, INVALID_SUBSCRIPTION_ENABLE_PARAMS, INVALID_SUBSCRIPTION_PARAMS, INVALID_TAX_EXTENSION_STATE, INVALID_VEHICLE_STATE, INVALID_VIRTUAL_TOUR_URL_DOMAIN, INVENTORY_ZERO_AVAILABILITY_IN_STOCK, IN_ANOTHER_PRODUCT_LAUNCH, ITEM_GROUP_NOT_SPECIFIED, ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP, ITEM_OVERRIDE_EMPTY_AVAILABILITY, ITEM_OVERRIDE_EMPTY_PRICE, ITEM_OVERRIDE_NOT_VISIBLE, ITEM_PRICE_NOT_POSITIVE, ITEM_STALE_OUT_OF_STOCK, MARKETPLACE_DISABLED_BY_USER, MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME, MARKETPLACE_PARTNER_CURRENCY_NOT_VALID, MARKETPLACE_PARTNER_DISTRIBUTION_DISABLED, MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG, MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_MISSING_LATLONG, MARKETPLACE_PARTNER_MISSING_SHIPPING_COST, MARKETPLACE_PARTNER_NOT_LOCAL_ITEM, MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM, MARKETPLACE_PARTNER_POLICY_VIOLATION, MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_SELLER_BANNED, MARKETPLACE_PARTNER_SELLER_NOT_VALID, MINI_SHOPS_DISABLED_BY_USER, MISSING_CHECKOUT, MISSING_CHECKOUT_CURRENCY, MISSING_COLOR, MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE, MISSING_EVENT, MISSING_INDIA_COMPLIANCE_FIELDS, MISSING_SHIPPING_PROFILE, MISSING_SIZE, MISSING_TAX_CATEGORY, NEGATIVE_COMMUNITY_FEEDBACK, NEGATIVE_PRICE, NOT_ENOUGH_IMAGES, NOT_ENOUGH_UNIQUE_PRODUCTS, NO_CONTENT_ID, OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH, PART_OF_PRODUCT_LAUNCH, PASSING_MULTIPLE_CONTENT_IDS, PRODUCT_DOMINANT_CURRENCY_MISMATCH, PRODUCT_EXPIRED, PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS, PRODUCT_ITEM_INVALID_PARTNER_TOKENS, PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP, PRODUCT_ITEM_NOT_VISIBLE, PRODUCT_NOT_APPROVED, PRODUCT_NOT_DOMINANT_CURRENCY, PRODUCT_OUT_OF_STOCK, PRODUCT_URL_EQUALS_DOMAIN, PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED, PROPERTY_PRICE_TOO_HIGH, PROPERTY_PRICE_TOO_LOW, PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY, PROPERTY_VALUE_CONTAINS_HTML_TAGS, PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK, PROPERTY_VALUE_FORMAT, PROPERTY_VALUE_MISSING, PROPERTY_VALUE_MISSING_WARNING, PROPERTY_VALUE_NON_POSITIVE, PROPERTY_VALUE_STRING_EXCEEDS_LENGTH, PROPERTY_VALUE_STRING_TOO_SHORT, PROPERTY_VALUE_UPPERCASE, PROPERTY_VALUE_UPPERCASE_WARNING, PURCHASE_RATE_BELOW_ADDTOCART, PURCHASE_RATE_BELOW_VIEWCONTENT, QUALITY_DUPLICATED_DESCRIPTION, QUALITY_ITEM_LINK_BROKEN, QUALITY_ITEM_LINK_REDIRECTING, RETAILER_ID_NOT_PROVIDED, RETAILER_ID_USED_BY_GROUP, SHOPIFY_INVALID_RETAILER_ID, SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE, SHOPS_POLICY_VIOLATION, SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED, TAX_CATEGORY_NOT_SUPPORTED_IN_UK, UNIQUE_PRODUCT_IDENTIFIER_MISSING, UNMATCHED_EVENTS, UNSUPPORTED_PRODUCT_CATEGORY, VARIANT_ATTRIBUTE_ISSUE, VIDEO_FETCH_FAILED, VIDEO_FETCH_FAILED_BAD_GATEWAY, VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED, VIDEO_FETCH_FAILED_FORBIDDEN, VIDEO_FETCH_FAILED_LINK_BROKEN, VIDEO_FETCH_FAILED_TIMED_OUT, VIDEO_ISSUE_GENERIC, VIDEO_NOT_DOWNLOADABLE, WHATSAPP_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION, WHATSAPP_POLICY_VIOLATION
        filter_: Optional.
        return_only_approved_products: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if error_priority is not None:
        params["error_priority"] = error_priority
    if error_type is not None:
        params["error_type"] = error_type
    if filter_ is not None:
        params["filter"] = filter_
    if return_only_approved_products is not None:
        params["return_only_approved_products"] = return_only_approved_products
    result = await get_client().get(f"{product_catalog_id}/products", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_products(
    product_catalog_id: str,
    currency: str,
    name: str,
    price: int,
    additional_image_urls: Optional[str] = None,
    additional_variant_attributes: Optional[str] = None,
    age_group: Optional[str] = None,
    allow_upsert: Optional[bool] = None,
    android_app_name: Optional[str] = None,
    android_class: Optional[str] = None,
    android_package: Optional[str] = None,
    android_url: Optional[str] = None,
    availability: Optional[str] = None,
    brand: Optional[str] = None,
    category: Optional[str] = None,
    category_specific_fields: Optional[str] = None,
    checkout_url: Optional[str] = None,
    color: Optional[str] = None,
    commerce_tax_category: Optional[str] = None,
    condition: Optional[str] = None,
    custom_data: Optional[str] = None,
    custom_label_0: Optional[str] = None,
    custom_label_1: Optional[str] = None,
    custom_label_2: Optional[str] = None,
    custom_label_3: Optional[str] = None,
    custom_label_4: Optional[str] = None,
    custom_number_0: Optional[int] = None,
    custom_number_1: Optional[int] = None,
    custom_number_2: Optional[int] = None,
    custom_number_3: Optional[int] = None,
    custom_number_4: Optional[int] = None,
    description: Optional[str] = None,
    expiration_date: Optional[str] = None,
    fb_product_category: Optional[str] = None,
    gender: Optional[str] = None,
    gtin: Optional[str] = None,
    image_url: Optional[str] = None,
    importer_address: Optional[str] = None,
    importer_name: Optional[str] = None,
    inventory: Optional[int] = None,
    ios_app_name: Optional[str] = None,
    ios_app_store_id: Optional[int] = None,
    ios_url: Optional[str] = None,
    ipad_app_name: Optional[str] = None,
    ipad_app_store_id: Optional[int] = None,
    ipad_url: Optional[str] = None,
    iphone_app_name: Optional[str] = None,
    iphone_app_store_id: Optional[int] = None,
    iphone_url: Optional[str] = None,
    launch_date: Optional[str] = None,
    live_special_price: Optional[str] = None,
    manufacturer_info: Optional[str] = None,
    manufacturer_part_number: Optional[str] = None,
    marked_for_product_launch: Optional[str] = None,
    material: Optional[str] = None,
    mobile_link: Optional[str] = None,
    ordering_index: Optional[int] = None,
    origin_country: Optional[str] = None,
    pattern: Optional[str] = None,
    product_priority_0: Optional[float] = None,
    product_priority_1: Optional[float] = None,
    product_priority_2: Optional[float] = None,
    product_priority_3: Optional[float] = None,
    product_priority_4: Optional[float] = None,
    product_type: Optional[str] = None,
    quantity_to_sell_on_facebook: Optional[int] = None,
    retailer_id: Optional[str] = None,
    retailer_product_group_id: Optional[str] = None,
    return_policy_days: Optional[int] = None,
    rich_text_description: Optional[str] = None,
    sale_price: Optional[int] = None,
    sale_price_end_date: Optional[str] = None,
    sale_price_start_date: Optional[str] = None,
    short_description: Optional[str] = None,
    size: Optional[str] = None,
    start_date: Optional[str] = None,
    url: Optional[str] = None,
    visibility: Optional[str] = None,
    wa_compliance_category: Optional[str] = None,
    windows_phone_app_id: Optional[str] = None,
    windows_phone_app_name: Optional[str] = None,
    windows_phone_url: Optional[str] = None,
) -> str:
    """POST /products on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        additional_image_urls: Optional.
        additional_variant_attributes: Optional.
        age_group: Optional. Values: adult, all ages, infant, kids, newborn, teen, toddler
        allow_upsert: Optional.
        android_app_name: Optional.
        android_class: Optional.
        android_package: Optional.
        android_url: Optional.
        availability: Optional. Values: available for order, discontinued, in stock, mark_as_sold, out of stock, pending, preorder
        brand: Optional.
        category: Optional.
        category_specific_fields: Optional.
        checkout_url: Optional.
        color: Optional.
        commerce_tax_category: Optional. Values: FB_ANIMAL, FB_ANIMAL_SUPP, FB_APRL, FB_APRL_ACCESSORIES, FB_APRL_ATHL_UNIF, FB_APRL_CASES, FB_APRL_CLOTHING, FB_APRL_COSTUME, FB_APRL_CSTM, FB_APRL_FORMAL, FB_APRL_HANDBAG, FB_APRL_JEWELRY, FB_APRL_SHOE, FB_APRL_SHOE_ACC, FB_APRL_SWIM, FB_APRL_SWIM_CHIL, FB_APRL_SWIM_CVR, FB_ARTS, FB_ARTS_HOBBY, FB_ARTS_PARTY, FB_ARTS_PARTY_GIFT_CARD, FB_ARTS_TICKET, FB_BABY, FB_BABY_BATH, FB_BABY_BLANKET, FB_BABY_DIAPER, FB_BABY_GIFT_SET, FB_BABY_HEALTH, FB_BABY_NURSING, FB_BABY_POTTY_TRN, FB_BABY_SAFE, FB_BABY_TOYS, FB_BABY_TRANSPORT, FB_BABY_TRANSPORT_ACC, FB_BAGS, FB_BAGS_BKPK, FB_BAGS_BOXES, FB_BAGS_BRFCS, FB_BAGS_CSMT_BAG, FB_BAGS_DFFL, FB_BAGS_DIPR, FB_BAGS_FNNY, FB_BAGS_GRMT, FB_BAGS_LUGG, FB_BAGS_LUG_ACC, FB_BAGS_MSGR, FB_BAGS_TOTE, FB_BAGS_TRN_CAS, FB_BLDG, FB_BLDG_ACC, FB_BLDG_CNSMB, FB_BLDG_FENCE, FB_BLDG_FUEL_TNK, FB_BLDG_HT_VNT, FB_BLDG_LOCK, FB_BLDG_MATRL, FB_BLDG_PLMB, FB_BLDG_PUMP, FB_BLDG_PWRS, FB_BLDG_STR_TANK, FB_BLDG_S_ENG, FB_BLDG_TL_ACC, FB_BLDG_TOOL, FB_BUSIND, FB_BUSIND_ADVERTISING, FB_BUSIND_AGRICULTURE, FB_BUSIND_AUTOMATION, FB_BUSIND_HEAVY_MACH, FB_BUSIND_LAB, FB_BUSIND_MEDICAL, FB_BUSIND_RETAIL, FB_BUSIND_SANITARY_CT, FB_BUSIND_SIGN, FB_BUSIND_STORAGE, FB_BUSIND_STORAGE_ACC, FB_BUSIND_WORK_GEAR, FB_CAMERA_ACC, FB_CAMERA_CAMERA, FB_CAMERA_OPTIC, FB_CAMERA_OPTICS, FB_CAMERA_PHOTO, FB_ELEC, FB_ELEC_ACC, FB_ELEC_ARCDADE, FB_ELEC_AUDIO, FB_ELEC_CIRCUIT, FB_ELEC_COMM, FB_ELEC_COMPUTER, FB_ELEC_GPS_ACC, FB_ELEC_GPS_NAV, FB_ELEC_GPS_TRK, FB_ELEC_MARINE, FB_ELEC_NETWORK, FB_ELEC_PART, FB_ELEC_PRINT, FB_ELEC_RADAR, FB_ELEC_SFTWR, FB_ELEC_SPEED_RDR, FB_ELEC_TELEVISION, FB_ELEC_TOLL, FB_ELEC_VIDEO, FB_ELEC_VID_GM_ACC, FB_ELEC_VID_GM_CNSL, FB_FOOD, FB_FURN, FB_FURN_BABY, FB_FURN_BENCH, FB_FURN_CART, FB_FURN_CHAIR, FB_FURN_CHAIR_ACC, FB_FURN_DIVIDE, FB_FURN_DIVIDE_ACC, FB_FURN_ENT_CTR, FB_FURN_FUTN, FB_FURN_FUTN_PAD, FB_FURN_OFFICE, FB_FURN_OFFICE_ACC, FB_FURN_OTTO, FB_FURN_OUTDOOR, FB_FURN_OUTDOOR_ACC, FB_FURN_SETS, FB_FURN_SHELVE_ACC, FB_FURN_SHLF, FB_FURN_SOFA, FB_FURN_SOFA_ACC, FB_FURN_STORAGE, FB_FURN_TABL, FB_FURN_TABL_ACC, FB_GENERIC_TAXABLE, FB_HLTH, FB_HLTH_HLTH, FB_HLTH_JWL_CR, FB_HLTH_LILP_BLM, FB_HLTH_LTN_SPF, FB_HLTH_PRSL_CR, FB_HLTH_SKN_CR, FB_HMGN, FB_HMGN_BATH, FB_HMGN_DCOR, FB_HMGN_EMGY, FB_HMGN_FPLC, FB_HMGN_FPLC_ACC, FB_HMGN_GS_SFT, FB_HMGN_HS_ACC, FB_HMGN_HS_APP, FB_HMGN_HS_SPL, FB_HMGN_KTCN, FB_HMGN_LAWN, FB_HMGN_LGHT, FB_HMGN_LINN, FB_HMGN_LT_ACC, FB_HMGN_OTDR, FB_HMGN_POOL, FB_HMGN_SCTY, FB_HMGN_SMK_ACC, FB_HMGN_UMBR, FB_HMGN_UMBR_ACC, FB_MDIA, FB_MDIA_BOOK, FB_MDIA_DVDS, FB_MDIA_MAG, FB_MDIA_MANL, FB_MDIA_MUSC, FB_MDIA_PRJ_PLN, FB_MDIA_SHT_MUS, FB_OFFC, FB_OFFC_BKAC, FB_OFFC_CRTS, FB_OFFC_DSKP, FB_OFFC_EQIP, FB_OFFC_FLNG, FB_OFFC_GNRL, FB_OFFC_INSTM, FB_OFFC_LP_DSK, FB_OFFC_MATS, FB_OFFC_NM_PLT, FB_OFFC_PPR_HNDL, FB_OFFC_PRSNT_SPL, FB_OFFC_SEALR, FB_OFFC_SHIP_SPL, FB_RLGN, FB_RLGN_CMNY, FB_RLGN_ITEM, FB_RLGN_WEDD, FB_SFTWR, FB_SFWR_CMPTR, FB_SFWR_DGTL_GD, FB_SFWR_GAME, FB_SHIPPING, FB_SPOR, FB_SPORT_ATHL, FB_SPORT_ATHL_CLTH, FB_SPORT_ATHL_SHOE, FB_SPORT_ATHL_SPRT, FB_SPORT_EXRCS, FB_SPORT_INDR_GM, FB_SPORT_OTDR_GM, FB_TOYS, FB_TOYS_EQIP, FB_TOYS_GAME, FB_TOYS_PZZL, FB_TOYS_TMRS, FB_TOYS_TOYS, FB_VEHI, FB_VEHI_PART
        condition: Optional. Values: cpo, new, open_box_new, refurbished, used, used_fair, used_good, used_like_new
        currency: Required.
        custom_data: Optional.
        custom_label_0: Optional.
        custom_label_1: Optional.
        custom_label_2: Optional.
        custom_label_3: Optional.
        custom_label_4: Optional.
        custom_number_0: Optional.
        custom_number_1: Optional.
        custom_number_2: Optional.
        custom_number_3: Optional.
        custom_number_4: Optional.
        description: Optional.
        expiration_date: Optional.
        fb_product_category: Optional.
        gender: Optional. Values: female, male, unisex
        gtin: Optional.
        image_url: Optional.
        importer_address: Optional.
        importer_name: Optional.
        inventory: Optional.
        ios_app_name: Optional.
        ios_app_store_id: Optional.
        ios_url: Optional.
        ipad_app_name: Optional.
        ipad_app_store_id: Optional.
        ipad_url: Optional.
        iphone_app_name: Optional.
        iphone_app_store_id: Optional.
        iphone_url: Optional.
        launch_date: Optional.
        live_special_price: Optional.
        manufacturer_info: Optional.
        manufacturer_part_number: Optional.
        marked_for_product_launch: Optional. Values: default, marked, not_marked
        material: Optional.
        mobile_link: Optional.
        name: Required.
        ordering_index: Optional.
        origin_country: Optional. Values: AC, AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW
        pattern: Optional.
        price: Required.
        product_priority_0: Optional.
        product_priority_1: Optional.
        product_priority_2: Optional.
        product_priority_3: Optional.
        product_priority_4: Optional.
        product_type: Optional.
        quantity_to_sell_on_facebook: Optional.
        retailer_id: Optional.
        retailer_product_group_id: Optional.
        return_policy_days: Optional.
        rich_text_description: Optional.
        sale_price: Optional.
        sale_price_end_date: Optional.
        sale_price_start_date: Optional.
        short_description: Optional.
        size: Optional.
        start_date: Optional.
        url: Optional.
        visibility: Optional. Values: published, staging
        wa_compliance_category: Optional. Values: COUNTRY_ORIGIN_EXEMPT, DEFAULT
        windows_phone_app_id: Optional.
        windows_phone_app_name: Optional.
        windows_phone_url: Optional.
    """
    params = {}
    if additional_image_urls is not None:
        params["additional_image_urls"] = additional_image_urls
    if additional_variant_attributes is not None:
        params["additional_variant_attributes"] = additional_variant_attributes
    if age_group is not None:
        params["age_group"] = age_group
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    if android_app_name is not None:
        params["android_app_name"] = android_app_name
    if android_class is not None:
        params["android_class"] = android_class
    if android_package is not None:
        params["android_package"] = android_package
    if android_url is not None:
        params["android_url"] = android_url
    if availability is not None:
        params["availability"] = availability
    if brand is not None:
        params["brand"] = brand
    if category is not None:
        params["category"] = category
    if category_specific_fields is not None:
        params["category_specific_fields"] = category_specific_fields
    if checkout_url is not None:
        params["checkout_url"] = checkout_url
    if color is not None:
        params["color"] = color
    if commerce_tax_category is not None:
        params["commerce_tax_category"] = commerce_tax_category
    if condition is not None:
        params["condition"] = condition
    params["currency"] = currency
    if custom_data is not None:
        params["custom_data"] = custom_data
    if custom_label_0 is not None:
        params["custom_label_0"] = custom_label_0
    if custom_label_1 is not None:
        params["custom_label_1"] = custom_label_1
    if custom_label_2 is not None:
        params["custom_label_2"] = custom_label_2
    if custom_label_3 is not None:
        params["custom_label_3"] = custom_label_3
    if custom_label_4 is not None:
        params["custom_label_4"] = custom_label_4
    if custom_number_0 is not None:
        params["custom_number_0"] = custom_number_0
    if custom_number_1 is not None:
        params["custom_number_1"] = custom_number_1
    if custom_number_2 is not None:
        params["custom_number_2"] = custom_number_2
    if custom_number_3 is not None:
        params["custom_number_3"] = custom_number_3
    if custom_number_4 is not None:
        params["custom_number_4"] = custom_number_4
    if description is not None:
        params["description"] = description
    if expiration_date is not None:
        params["expiration_date"] = expiration_date
    if fb_product_category is not None:
        params["fb_product_category"] = fb_product_category
    if gender is not None:
        params["gender"] = gender
    if gtin is not None:
        params["gtin"] = gtin
    if image_url is not None:
        params["image_url"] = image_url
    if importer_address is not None:
        params["importer_address"] = importer_address
    if importer_name is not None:
        params["importer_name"] = importer_name
    if inventory is not None:
        params["inventory"] = inventory
    if ios_app_name is not None:
        params["ios_app_name"] = ios_app_name
    if ios_app_store_id is not None:
        params["ios_app_store_id"] = ios_app_store_id
    if ios_url is not None:
        params["ios_url"] = ios_url
    if ipad_app_name is not None:
        params["ipad_app_name"] = ipad_app_name
    if ipad_app_store_id is not None:
        params["ipad_app_store_id"] = ipad_app_store_id
    if ipad_url is not None:
        params["ipad_url"] = ipad_url
    if iphone_app_name is not None:
        params["iphone_app_name"] = iphone_app_name
    if iphone_app_store_id is not None:
        params["iphone_app_store_id"] = iphone_app_store_id
    if iphone_url is not None:
        params["iphone_url"] = iphone_url
    if launch_date is not None:
        params["launch_date"] = launch_date
    if live_special_price is not None:
        params["live_special_price"] = live_special_price
    if manufacturer_info is not None:
        params["manufacturer_info"] = manufacturer_info
    if manufacturer_part_number is not None:
        params["manufacturer_part_number"] = manufacturer_part_number
    if marked_for_product_launch is not None:
        params["marked_for_product_launch"] = marked_for_product_launch
    if material is not None:
        params["material"] = material
    if mobile_link is not None:
        params["mobile_link"] = mobile_link
    params["name"] = name
    if ordering_index is not None:
        params["ordering_index"] = ordering_index
    if origin_country is not None:
        params["origin_country"] = origin_country
    if pattern is not None:
        params["pattern"] = pattern
    params["price"] = price
    if product_priority_0 is not None:
        params["product_priority_0"] = product_priority_0
    if product_priority_1 is not None:
        params["product_priority_1"] = product_priority_1
    if product_priority_2 is not None:
        params["product_priority_2"] = product_priority_2
    if product_priority_3 is not None:
        params["product_priority_3"] = product_priority_3
    if product_priority_4 is not None:
        params["product_priority_4"] = product_priority_4
    if product_type is not None:
        params["product_type"] = product_type
    if quantity_to_sell_on_facebook is not None:
        params["quantity_to_sell_on_facebook"] = quantity_to_sell_on_facebook
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    if retailer_product_group_id is not None:
        params["retailer_product_group_id"] = retailer_product_group_id
    if return_policy_days is not None:
        params["return_policy_days"] = return_policy_days
    if rich_text_description is not None:
        params["rich_text_description"] = rich_text_description
    if sale_price is not None:
        params["sale_price"] = sale_price
    if sale_price_end_date is not None:
        params["sale_price_end_date"] = sale_price_end_date
    if sale_price_start_date is not None:
        params["sale_price_start_date"] = sale_price_start_date
    if short_description is not None:
        params["short_description"] = short_description
    if size is not None:
        params["size"] = size
    if start_date is not None:
        params["start_date"] = start_date
    if url is not None:
        params["url"] = url
    if visibility is not None:
        params["visibility"] = visibility
    if wa_compliance_category is not None:
        params["wa_compliance_category"] = wa_compliance_category
    if windows_phone_app_id is not None:
        params["windows_phone_app_id"] = windows_phone_app_id
    if windows_phone_app_name is not None:
        params["windows_phone_app_name"] = windows_phone_app_name
    if windows_phone_url is not None:
        params["windows_phone_url"] = windows_phone_url
    result = await get_client().post(f"{product_catalog_id}/products", data=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_update_generated_image_config(product_catalog_id: str, data: str) -> str:
    """POST /update_generated_image_config on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        data: Required.
    """
    params = {}
    params["data"] = data
    result = await get_client().post(f"{product_catalog_id}/update_generated_image_config", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_vehicle_offers(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicle_offers on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/vehicle_offers", params=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_vehicles(
    product_catalog_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicles on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_catalog_id}/vehicles", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_vehicles(
    product_catalog_id: str,
    address: str,
    body_style: str,
    currency: str,
    description: str,
    exterior_color: str,
    images: str,
    make: str,
    mileage: str,
    model: str,
    price: int,
    state_of_vehicle: str,
    title: str,
    url: str,
    vehicle_id: str,
    vin: str,
    year: int,
    applinks: Optional[str] = None,
    availability: Optional[str] = None,
    condition: Optional[str] = None,
    date_first_on_lot: Optional[str] = None,
    dealer_id: Optional[str] = None,
    dealer_name: Optional[str] = None,
    dealer_phone: Optional[str] = None,
    drivetrain: Optional[str] = None,
    fb_page_id: Optional[str] = None,
    fuel_type: Optional[str] = None,
    interior_color: Optional[str] = None,
    transmission: Optional[str] = None,
    trim: Optional[str] = None,
    vehicle_type: Optional[str] = None,
) -> str:
    """POST /vehicles on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        address: Required.
        applinks: Optional.
        availability: Optional. Values: AVAILABLE, NOT_AVAILABLE, PENDING, UNKNOWN
        body_style: Required. Values: CONVERTIBLE, COUPE, CROSSOVER, ESTATE, GRANDTOURER, HATCHBACK, MINIBUS, MINIVAN, MPV, NONE, OTHER, PICKUP, ROADSTER, SALOON, SEDAN, SMALL_CAR, SPORTSCAR, SUPERCAR, SUPERMINI, SUV, TRUCK, VAN, WAGON
        condition: Optional. Values: EXCELLENT, FAIR, GOOD, NONE, OTHER, POOR, VERY_GOOD
        currency: Required.
        date_first_on_lot: Optional.
        dealer_id: Optional.
        dealer_name: Optional.
        dealer_phone: Optional.
        description: Required.
        drivetrain: Optional. Values: AWD, FOUR_WD, FWD, NONE, OTHER, RWD, TWO_WD
        exterior_color: Required.
        fb_page_id: Optional.
        fuel_type: Optional. Values: DIESEL, ELECTRIC, FLEX, GASOLINE, HYBRID, NONE, OTHER, PETROL, PLUGIN_HYBRID
        images: Required.
        interior_color: Optional.
        make: Required.
        mileage: Required.
        model: Required.
        price: Required.
        state_of_vehicle: Required. Values: CPO, NEW, USED
        title: Required.
        transmission: Optional. Values: AUTOMATIC, MANUAL, NONE, OTHER
        trim: Optional.
        url: Required.
        vehicle_id: Required.
        vehicle_type: Optional. Values: BOAT, CAR_TRUCK, COMMERCIAL, MOTORCYCLE, OTHER, POWERSPORT, RV_CAMPER, TRAILER
        vin: Required.
        year: Required.
    """
    params = {}
    params["address"] = address
    if applinks is not None:
        params["applinks"] = applinks
    if availability is not None:
        params["availability"] = availability
    params["body_style"] = body_style
    if condition is not None:
        params["condition"] = condition
    params["currency"] = currency
    if date_first_on_lot is not None:
        params["date_first_on_lot"] = date_first_on_lot
    if dealer_id is not None:
        params["dealer_id"] = dealer_id
    if dealer_name is not None:
        params["dealer_name"] = dealer_name
    if dealer_phone is not None:
        params["dealer_phone"] = dealer_phone
    params["description"] = description
    if drivetrain is not None:
        params["drivetrain"] = drivetrain
    params["exterior_color"] = exterior_color
    if fb_page_id is not None:
        params["fb_page_id"] = fb_page_id
    if fuel_type is not None:
        params["fuel_type"] = fuel_type
    params["images"] = images
    if interior_color is not None:
        params["interior_color"] = interior_color
    params["make"] = make
    params["mileage"] = mileage
    params["model"] = model
    params["price"] = price
    params["state_of_vehicle"] = state_of_vehicle
    params["title"] = title
    if transmission is not None:
        params["transmission"] = transmission
    if trim is not None:
        params["trim"] = trim
    params["url"] = url
    params["vehicle_id"] = vehicle_id
    if vehicle_type is not None:
        params["vehicle_type"] = vehicle_type
    params["vin"] = vin
    params["year"] = year
    result = await get_client().post(f"{product_catalog_id}/vehicles", data=params)
    return json.dumps(result, indent=2)


async def get_product_catalog_version_configs(product_catalog_id: str, fields: Optional[str] = None) -> str:
    """GET /version_configs on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_catalog_id}/version_configs", params=params)
    return json.dumps(result, indent=2)


async def create_product_catalog_version_items_batch(
    product_catalog_id: str,
    item_type: str,
    item_version: str,
    requests: str,
    allow_upsert: Optional[bool] = None,
    version: Optional[int] = None,
) -> str:
    """POST /version_items_batch on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_upsert: Optional.
        item_type: Required.
        item_version: Required.
        requests: Required.
        version: Optional.
    """
    params = {}
    if allow_upsert is not None:
        params["allow_upsert"] = allow_upsert
    params["item_type"] = item_type
    params["item_version"] = item_version
    params["requests"] = requests
    if version is not None:
        params["version"] = version
    result = await get_client().post(f"{product_catalog_id}/version_items_batch", data=params)
    return json.dumps(result, indent=2)


async def delete_product_catalog(
    product_catalog_id: str,
    allow_delete_catalog_with_live_product_set: Optional[bool] = None,
) -> str:
    """DELETE /#delete on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        allow_delete_catalog_with_live_product_set: Optional.
    """
    params = {}
    if allow_delete_catalog_with_live_product_set is not None:
        params["allow_delete_catalog_with_live_product_set"] = allow_delete_catalog_with_live_product_set
    result = await get_client().delete(f"{product_catalog_id}")
    return json.dumps(result, indent=2)


async def get_product_catalog(
    product_catalog_id: str,
    fields: Optional[str] = None,
    segment_use_cases: Optional[str] = None,
) -> str:
    """GET /#get on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        fields: Comma-separated list of fields to return. Available: ad_account_to_collaborative_ads_share_settings, agency_collaborative_ads_share_settings, business, catalog_store, commerce_merchant_settings, creator_user, da_display_settings, default_image_url, fallback_image_url, feed_count, id, is_catalog_segment, is_local_catalog, name, owner_business, product_count, store_catalog_settings, user_access_expire_time, vertical
        segment_use_cases: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if segment_use_cases is not None:
        params["segment_use_cases"] = segment_use_cases
    result = await get_client().get(f"{product_catalog_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_catalog(
    product_catalog_id: str,
    additional_vertical_option: Optional[str] = None,
    da_display_settings: Optional[str] = None,
    default_image_url: Optional[str] = None,
    destination_catalog_settings: Optional[str] = None,
    fallback_image_url: Optional[str] = None,
    flight_catalog_settings: Optional[str] = None,
    name: Optional[str] = None,
    partner_integration: Optional[str] = None,
    store_catalog_settings: Optional[str] = None,
) -> str:
    """POST /#update on ProductCatalog.

    Args:
        product_catalog_id: The ID of the ProductCatalog object.
        additional_vertical_option: Optional.
        da_display_settings: Optional.
        default_image_url: Optional.
        destination_catalog_settings: Optional.
        fallback_image_url: Optional.
        flight_catalog_settings: Optional.
        name: Optional.
        partner_integration: Optional.
        store_catalog_settings: Optional.
    """
    params = {}
    if additional_vertical_option is not None:
        params["additional_vertical_option"] = additional_vertical_option
    if da_display_settings is not None:
        params["da_display_settings"] = da_display_settings
    if default_image_url is not None:
        params["default_image_url"] = default_image_url
    if destination_catalog_settings is not None:
        params["destination_catalog_settings"] = destination_catalog_settings
    if fallback_image_url is not None:
        params["fallback_image_url"] = fallback_image_url
    if flight_catalog_settings is not None:
        params["flight_catalog_settings"] = flight_catalog_settings
    if name is not None:
        params["name"] = name
    if partner_integration is not None:
        params["partner_integration"] = partner_integration
    if store_catalog_settings is not None:
        params["store_catalog_settings"] = store_catalog_settings
    result = await get_client().post(f"{product_catalog_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_FEED_FIELDS = [
    "country",
    "created_time",
    "default_currency",
    "deletion_enabled",
    "delimiter",
    "encoding",
    "file_name",
    "id",
    "ingestion_source_type",
    "item_sub_type",
    "latest_upload",
    "migrated_from_feed_id",
    "name",
    "override_type",
    "primary_feeds",
    "product_count",
    "quoted_fields_mode",
    "schedule",
    "supplementary_feeds",
    "update_schedule"
]


async def get_product_feed_automotive_models(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /automotive_models on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/automotive_models", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_destinations(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /destinations on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/destinations", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_flights(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /flights on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/flights", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_home_listings(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /home_listings on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/home_listings", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_hotels(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /hotels on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/hotels", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_media_titles(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /media_titles on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/media_titles", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_products(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    error_priority: Optional[str] = None,
    error_type: Optional[str] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /products on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        error_priority: Optional. Values: HIGH, LOW, MEDIUM
        error_type: Optional. Values: ADDRESS_BLOCKLISTED_IN_MARKET, AGGREGATED_LOCALIZATION_ISSUES, APP_HAS_NO_AEM_SETUP, AR_DELETED_DUE_TO_UPDATE, AR_POLICY_VIOLATED, AVAILABLE, BAD_QUALITY_IMAGE, BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK, BIZ_MSG_AI_AGENT_DISABLED_BY_USER, BIZ_MSG_GEN_AI_POLICY_VIOLATED, CANNOT_EDIT_SUBSCRIPTION_PRODUCTS, CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE, CHECKOUT_DISABLED_BY_USER, COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID, COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT, CRAWLED_AVAILABILITY_MISMATCH, DA_DISABLED_BY_USER, DA_POLICY_VIOLATION, DELETED_ITEM, DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT, DUPLICATE_IMAGES, DUPLICATE_TITLE_AND_DESCRIPTION, EMPTY_AVAILABILITY, EMPTY_CONDITION, EMPTY_DESCRIPTION, EMPTY_IMAGE_URL, EMPTY_PRICE, EMPTY_PRODUCT_URL, EMPTY_SELLER_DESCRIPTION, EMPTY_TITLE, EXTERNAL_MERCHANT_ID_MISMATCH, GENERIC_INVALID_FIELD, GROUPS_DISABLED_BY_USER, HIDDEN_UNTIL_PRODUCT_LAUNCH, ILLEGAL_PRODUCT_CATEGORY, IMAGE_FETCH_FAILED, IMAGE_FETCH_FAILED_BAD_GATEWAY, IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED, IMAGE_FETCH_FAILED_FORBIDDEN, IMAGE_FETCH_FAILED_LINK_BROKEN, IMAGE_FETCH_FAILED_TIMED_OUT, IMAGE_RESOLUTION_LOW, INACTIVE_SHOPIFY_PRODUCT, INVALID_COMMERCE_TAX_CATEGORY, INVALID_CONSOLIDATED_LOCALITY_INFORMATION, INVALID_CONTENT_ID, INVALID_DEALER_COMMUNICATION_PARAMETERS, INVALID_DMA_CODES, INVALID_FB_PAGE_ID, INVALID_IMAGES, INVALID_MONETIZER_RETURN_POLICY, INVALID_OFFER_DISCLAIMER_URL, INVALID_OFFER_END_DATE, INVALID_PRE_ORDER_PARAMS, INVALID_RANGE_FOR_AREA_SIZE, INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE, INVALID_RANGE_FOR_NUM_OF_BATHS, INVALID_RANGE_FOR_NUM_OF_BEDS, INVALID_RANGE_FOR_NUM_OF_ROOMS, INVALID_RANGE_FOR_PARKING_SPACES, INVALID_SHELTER_PAGE_ID, INVALID_SHIPPING_PROFILE_PARAMS, INVALID_SUBSCRIPTION_DISABLE_PARAMS, INVALID_SUBSCRIPTION_ENABLE_PARAMS, INVALID_SUBSCRIPTION_PARAMS, INVALID_TAX_EXTENSION_STATE, INVALID_VEHICLE_STATE, INVALID_VIRTUAL_TOUR_URL_DOMAIN, INVENTORY_ZERO_AVAILABILITY_IN_STOCK, IN_ANOTHER_PRODUCT_LAUNCH, ITEM_GROUP_NOT_SPECIFIED, ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP, ITEM_OVERRIDE_EMPTY_AVAILABILITY, ITEM_OVERRIDE_EMPTY_PRICE, ITEM_OVERRIDE_NOT_VISIBLE, ITEM_PRICE_NOT_POSITIVE, ITEM_STALE_OUT_OF_STOCK, MARKETPLACE_DISABLED_BY_USER, MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME, MARKETPLACE_PARTNER_CURRENCY_NOT_VALID, MARKETPLACE_PARTNER_DISTRIBUTION_DISABLED, MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG, MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_MISSING_LATLONG, MARKETPLACE_PARTNER_MISSING_SHIPPING_COST, MARKETPLACE_PARTNER_NOT_LOCAL_ITEM, MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM, MARKETPLACE_PARTNER_POLICY_VIOLATION, MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_SELLER_BANNED, MARKETPLACE_PARTNER_SELLER_NOT_VALID, MINI_SHOPS_DISABLED_BY_USER, MISSING_CHECKOUT, MISSING_CHECKOUT_CURRENCY, MISSING_COLOR, MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE, MISSING_EVENT, MISSING_INDIA_COMPLIANCE_FIELDS, MISSING_SHIPPING_PROFILE, MISSING_SIZE, MISSING_TAX_CATEGORY, NEGATIVE_COMMUNITY_FEEDBACK, NEGATIVE_PRICE, NOT_ENOUGH_IMAGES, NOT_ENOUGH_UNIQUE_PRODUCTS, NO_CONTENT_ID, OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH, PART_OF_PRODUCT_LAUNCH, PASSING_MULTIPLE_CONTENT_IDS, PRODUCT_DOMINANT_CURRENCY_MISMATCH, PRODUCT_EXPIRED, PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS, PRODUCT_ITEM_INVALID_PARTNER_TOKENS, PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP, PRODUCT_ITEM_NOT_VISIBLE, PRODUCT_NOT_APPROVED, PRODUCT_NOT_DOMINANT_CURRENCY, PRODUCT_OUT_OF_STOCK, PRODUCT_URL_EQUALS_DOMAIN, PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED, PROPERTY_PRICE_TOO_HIGH, PROPERTY_PRICE_TOO_LOW, PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY, PROPERTY_VALUE_CONTAINS_HTML_TAGS, PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK, PROPERTY_VALUE_FORMAT, PROPERTY_VALUE_MISSING, PROPERTY_VALUE_MISSING_WARNING, PROPERTY_VALUE_NON_POSITIVE, PROPERTY_VALUE_STRING_EXCEEDS_LENGTH, PROPERTY_VALUE_STRING_TOO_SHORT, PROPERTY_VALUE_UPPERCASE, PROPERTY_VALUE_UPPERCASE_WARNING, PURCHASE_RATE_BELOW_ADDTOCART, PURCHASE_RATE_BELOW_VIEWCONTENT, QUALITY_DUPLICATED_DESCRIPTION, QUALITY_ITEM_LINK_BROKEN, QUALITY_ITEM_LINK_REDIRECTING, RETAILER_ID_NOT_PROVIDED, RETAILER_ID_USED_BY_GROUP, SHOPIFY_INVALID_RETAILER_ID, SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE, SHOPS_POLICY_VIOLATION, SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED, TAX_CATEGORY_NOT_SUPPORTED_IN_UK, UNIQUE_PRODUCT_IDENTIFIER_MISSING, UNMATCHED_EVENTS, UNSUPPORTED_PRODUCT_CATEGORY, VARIANT_ATTRIBUTE_ISSUE, VIDEO_FETCH_FAILED, VIDEO_FETCH_FAILED_BAD_GATEWAY, VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED, VIDEO_FETCH_FAILED_FORBIDDEN, VIDEO_FETCH_FAILED_LINK_BROKEN, VIDEO_FETCH_FAILED_TIMED_OUT, VIDEO_ISSUE_GENERIC, VIDEO_NOT_DOWNLOADABLE, WHATSAPP_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION, WHATSAPP_POLICY_VIOLATION
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if error_priority is not None:
        params["error_priority"] = error_priority
    if error_type is not None:
        params["error_type"] = error_type
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/products", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_rules(product_feed_id: str, fields: Optional[str] = None) -> str:
    """GET /rules on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_id}/rules", params=params)
    return json.dumps(result, indent=2)


async def create_product_feed_rules(
    product_feed_id: str,
    attribute: str,
    rule_type: str,
    params: Optional[str] = None,
) -> str:
    """POST /rules on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        attribute: Required.
        params: Optional.
        rule_type: Required. Values: fallback_rule, letter_case_rule, mapping_rule, regex_replace_rule, value_mapping_rule
    """
    params = {}
    params["attribute"] = attribute
    if params is not None:
        params["params"] = params
    params["rule_type"] = rule_type
    result = await get_client().post(f"{product_feed_id}/rules", data=params)
    return json.dumps(result, indent=2)


async def create_product_feed_supplementary_feed_assocs(product_feed_id: str, assoc_data: str) -> str:
    """POST /supplementary_feed_assocs on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        assoc_data: Required.
    """
    params = {}
    params["assoc_data"] = assoc_data
    result = await get_client().post(f"{product_feed_id}/supplementary_feed_assocs", data=params)
    return json.dumps(result, indent=2)


async def get_product_feed_upload_schedules(product_feed_id: str, fields: Optional[str] = None) -> str:
    """GET /upload_schedules on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_id}/upload_schedules", params=params)
    return json.dumps(result, indent=2)


async def create_product_feed_upload_schedules(product_feed_id: str, upload_schedule: Optional[str] = None) -> str:
    """POST /upload_schedules on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        upload_schedule: Optional.
    """
    params = {}
    if upload_schedule is not None:
        params["upload_schedule"] = upload_schedule
    result = await get_client().post(f"{product_feed_id}/upload_schedules", data=params)
    return json.dumps(result, indent=2)


async def get_product_feed_uploads(product_feed_id: str, fields: Optional[str] = None) -> str:
    """GET /uploads on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_id}/uploads", params=params)
    return json.dumps(result, indent=2)


async def create_product_feed_uploads(
    product_feed_id: str,
    fbe_external_business_id: Optional[str] = None,
    file: Optional[str] = None,
    password: Optional[str] = None,
    update_only: Optional[bool] = None,
    url: Optional[str] = None,
    username: Optional[str] = None,
) -> str:
    """POST /uploads on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fbe_external_business_id: Optional.
        file: Optional.
        password: Optional.
        update_only: Optional.
        url: Optional.
        username: Optional.
    """
    params = {}
    if fbe_external_business_id is not None:
        params["fbe_external_business_id"] = fbe_external_business_id
    if file is not None:
        params["file"] = file
    if password is not None:
        params["password"] = password
    if update_only is not None:
        params["update_only"] = update_only
    if url is not None:
        params["url"] = url
    if username is not None:
        params["username"] = username
    result = await get_client().post(f"{product_feed_id}/uploads", data=params)
    return json.dumps(result, indent=2)


async def get_product_feed_vehicle_offers(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicle_offers on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/vehicle_offers", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_vehicles(
    product_feed_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicles on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_feed_id}/vehicles", params=params)
    return json.dumps(result, indent=2)


async def delete_product_feed(product_feed_id: str) -> str:
    """DELETE /#delete on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
    """
    params = {}
    result = await get_client().delete(f"{product_feed_id}")
    return json.dumps(result, indent=2)


async def get_product_feed(product_feed_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        fields: Comma-separated list of fields to return. Available: country, created_time, default_currency, deletion_enabled, delimiter, encoding, file_name, id, ingestion_source_type, item_sub_type, latest_upload, migrated_from_feed_id, name, override_type, primary_feeds, product_count, quoted_fields_mode, schedule, supplementary_feeds, update_schedule
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_feed(
    product_feed_id: str,
    default_currency: Optional[str] = None,
    deletion_enabled: Optional[bool] = None,
    delimiter: Optional[str] = None,
    encoding: Optional[str] = None,
    migrated_from_feed_id: Optional[str] = None,
    name: Optional[str] = None,
    quoted_fields_mode: Optional[str] = None,
    schedule: Optional[str] = None,
    update_schedule: Optional[str] = None,
) -> str:
    """POST /#update on ProductFeed.

    Args:
        product_feed_id: The ID of the ProductFeed object.
        default_currency: Optional.
        deletion_enabled: Optional.
        delimiter: Optional.
        encoding: Optional.
        migrated_from_feed_id: Optional.
        name: Optional.
        quoted_fields_mode: Optional.
        schedule: Optional.
        update_schedule: Optional.
    """
    params = {}
    if default_currency is not None:
        params["default_currency"] = default_currency
    if deletion_enabled is not None:
        params["deletion_enabled"] = deletion_enabled
    if delimiter is not None:
        params["delimiter"] = delimiter
    if encoding is not None:
        params["encoding"] = encoding
    if migrated_from_feed_id is not None:
        params["migrated_from_feed_id"] = migrated_from_feed_id
    if name is not None:
        params["name"] = name
    if quoted_fields_mode is not None:
        params["quoted_fields_mode"] = quoted_fields_mode
    if schedule is not None:
        params["schedule"] = schedule
    if update_schedule is not None:
        params["update_schedule"] = update_schedule
    result = await get_client().post(f"{product_feed_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_SET_FIELDS = [
    "auto_creation_url",
    "filter",
    "id",
    "latest_metadata",
    "live_metadata",
    "name",
    "ordering_info",
    "product_catalog",
    "product_count",
    "retailer_id"
]


async def get_product_set_automotive_models(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /automotive_models on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/automotive_models", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_destinations(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /destinations on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/destinations", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_flights(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /flights on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/flights", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_home_listings(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /home_listings on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/home_listings", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_hotels(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /hotels on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/hotels", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_media_titles(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /media_titles on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/media_titles", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_products(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    error_priority: Optional[str] = None,
    error_type: Optional[str] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /products on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        error_priority: Optional. Values: HIGH, LOW, MEDIUM
        error_type: Optional. Values: ADDRESS_BLOCKLISTED_IN_MARKET, AGGREGATED_LOCALIZATION_ISSUES, APP_HAS_NO_AEM_SETUP, AR_DELETED_DUE_TO_UPDATE, AR_POLICY_VIOLATED, AVAILABLE, BAD_QUALITY_IMAGE, BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK, BIZ_MSG_AI_AGENT_DISABLED_BY_USER, BIZ_MSG_GEN_AI_POLICY_VIOLATED, CANNOT_EDIT_SUBSCRIPTION_PRODUCTS, CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE, CHECKOUT_DISABLED_BY_USER, COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID, COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT, CRAWLED_AVAILABILITY_MISMATCH, DA_DISABLED_BY_USER, DA_POLICY_VIOLATION, DELETED_ITEM, DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT, DUPLICATE_IMAGES, DUPLICATE_TITLE_AND_DESCRIPTION, EMPTY_AVAILABILITY, EMPTY_CONDITION, EMPTY_DESCRIPTION, EMPTY_IMAGE_URL, EMPTY_PRICE, EMPTY_PRODUCT_URL, EMPTY_SELLER_DESCRIPTION, EMPTY_TITLE, EXTERNAL_MERCHANT_ID_MISMATCH, GENERIC_INVALID_FIELD, GROUPS_DISABLED_BY_USER, HIDDEN_UNTIL_PRODUCT_LAUNCH, ILLEGAL_PRODUCT_CATEGORY, IMAGE_FETCH_FAILED, IMAGE_FETCH_FAILED_BAD_GATEWAY, IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED, IMAGE_FETCH_FAILED_FORBIDDEN, IMAGE_FETCH_FAILED_LINK_BROKEN, IMAGE_FETCH_FAILED_TIMED_OUT, IMAGE_RESOLUTION_LOW, INACTIVE_SHOPIFY_PRODUCT, INVALID_COMMERCE_TAX_CATEGORY, INVALID_CONSOLIDATED_LOCALITY_INFORMATION, INVALID_CONTENT_ID, INVALID_DEALER_COMMUNICATION_PARAMETERS, INVALID_DMA_CODES, INVALID_FB_PAGE_ID, INVALID_IMAGES, INVALID_MONETIZER_RETURN_POLICY, INVALID_OFFER_DISCLAIMER_URL, INVALID_OFFER_END_DATE, INVALID_PRE_ORDER_PARAMS, INVALID_RANGE_FOR_AREA_SIZE, INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE, INVALID_RANGE_FOR_NUM_OF_BATHS, INVALID_RANGE_FOR_NUM_OF_BEDS, INVALID_RANGE_FOR_NUM_OF_ROOMS, INVALID_RANGE_FOR_PARKING_SPACES, INVALID_SHELTER_PAGE_ID, INVALID_SHIPPING_PROFILE_PARAMS, INVALID_SUBSCRIPTION_DISABLE_PARAMS, INVALID_SUBSCRIPTION_ENABLE_PARAMS, INVALID_SUBSCRIPTION_PARAMS, INVALID_TAX_EXTENSION_STATE, INVALID_VEHICLE_STATE, INVALID_VIRTUAL_TOUR_URL_DOMAIN, INVENTORY_ZERO_AVAILABILITY_IN_STOCK, IN_ANOTHER_PRODUCT_LAUNCH, ITEM_GROUP_NOT_SPECIFIED, ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP, ITEM_OVERRIDE_EMPTY_AVAILABILITY, ITEM_OVERRIDE_EMPTY_PRICE, ITEM_OVERRIDE_NOT_VISIBLE, ITEM_PRICE_NOT_POSITIVE, ITEM_STALE_OUT_OF_STOCK, MARKETPLACE_DISABLED_BY_USER, MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME, MARKETPLACE_PARTNER_CURRENCY_NOT_VALID, MARKETPLACE_PARTNER_DISTRIBUTION_DISABLED, MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG, MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_MISSING_LATLONG, MARKETPLACE_PARTNER_MISSING_SHIPPING_COST, MARKETPLACE_PARTNER_NOT_LOCAL_ITEM, MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM, MARKETPLACE_PARTNER_POLICY_VIOLATION, MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED, MARKETPLACE_PARTNER_SELLER_BANNED, MARKETPLACE_PARTNER_SELLER_NOT_VALID, MINI_SHOPS_DISABLED_BY_USER, MISSING_CHECKOUT, MISSING_CHECKOUT_CURRENCY, MISSING_COLOR, MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE, MISSING_EVENT, MISSING_INDIA_COMPLIANCE_FIELDS, MISSING_SHIPPING_PROFILE, MISSING_SIZE, MISSING_TAX_CATEGORY, NEGATIVE_COMMUNITY_FEEDBACK, NEGATIVE_PRICE, NOT_ENOUGH_IMAGES, NOT_ENOUGH_UNIQUE_PRODUCTS, NO_CONTENT_ID, OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH, PART_OF_PRODUCT_LAUNCH, PASSING_MULTIPLE_CONTENT_IDS, PRODUCT_DOMINANT_CURRENCY_MISMATCH, PRODUCT_EXPIRED, PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS, PRODUCT_ITEM_INVALID_PARTNER_TOKENS, PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP, PRODUCT_ITEM_NOT_VISIBLE, PRODUCT_NOT_APPROVED, PRODUCT_NOT_DOMINANT_CURRENCY, PRODUCT_OUT_OF_STOCK, PRODUCT_URL_EQUALS_DOMAIN, PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED, PROPERTY_PRICE_TOO_HIGH, PROPERTY_PRICE_TOO_LOW, PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY, PROPERTY_VALUE_CONTAINS_HTML_TAGS, PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK, PROPERTY_VALUE_FORMAT, PROPERTY_VALUE_MISSING, PROPERTY_VALUE_MISSING_WARNING, PROPERTY_VALUE_NON_POSITIVE, PROPERTY_VALUE_STRING_EXCEEDS_LENGTH, PROPERTY_VALUE_STRING_TOO_SHORT, PROPERTY_VALUE_UPPERCASE, PROPERTY_VALUE_UPPERCASE_WARNING, PURCHASE_RATE_BELOW_ADDTOCART, PURCHASE_RATE_BELOW_VIEWCONTENT, QUALITY_DUPLICATED_DESCRIPTION, QUALITY_ITEM_LINK_BROKEN, QUALITY_ITEM_LINK_REDIRECTING, RETAILER_ID_NOT_PROVIDED, RETAILER_ID_USED_BY_GROUP, SHOPIFY_INVALID_RETAILER_ID, SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE, SHOPS_POLICY_VIOLATION, SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED, TAX_CATEGORY_NOT_SUPPORTED_IN_UK, UNIQUE_PRODUCT_IDENTIFIER_MISSING, UNMATCHED_EVENTS, UNSUPPORTED_PRODUCT_CATEGORY, VARIANT_ATTRIBUTE_ISSUE, VIDEO_FETCH_FAILED, VIDEO_FETCH_FAILED_BAD_GATEWAY, VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED, VIDEO_FETCH_FAILED_FORBIDDEN, VIDEO_FETCH_FAILED_LINK_BROKEN, VIDEO_FETCH_FAILED_TIMED_OUT, VIDEO_ISSUE_GENERIC, VIDEO_NOT_DOWNLOADABLE, WHATSAPP_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER, WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION, WHATSAPP_POLICY_VIOLATION
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if error_priority is not None:
        params["error_priority"] = error_priority
    if error_type is not None:
        params["error_type"] = error_type
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/products", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_vehicle_offers(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicle_offers on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/vehicle_offers", params=params)
    return json.dumps(result, indent=2)


async def get_product_set_vehicles(
    product_set_id: str,
    fields: Optional[str] = None,
    bulk_pagination: Optional[bool] = None,
    filter_: Optional[str] = None,
) -> str:
    """GET /vehicles on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return.
        bulk_pagination: Optional.
        filter_: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if bulk_pagination is not None:
        params["bulk_pagination"] = bulk_pagination
    if filter_ is not None:
        params["filter"] = filter_
    result = await get_client().get(f"{product_set_id}/vehicles", params=params)
    return json.dumps(result, indent=2)


async def delete_product_set(product_set_id: str, allow_live_product_set_deletion: Optional[bool] = None) -> str:
    """DELETE /#delete on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        allow_live_product_set_deletion: Optional.
    """
    params = {}
    if allow_live_product_set_deletion is not None:
        params["allow_live_product_set_deletion"] = allow_live_product_set_deletion
    result = await get_client().delete(f"{product_set_id}")
    return json.dumps(result, indent=2)


async def get_product_set(product_set_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        fields: Comma-separated list of fields to return. Available: auto_creation_url, filter, id, latest_metadata, live_metadata, name, ordering_info, product_catalog, product_count, retailer_id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_set_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_set(
    product_set_id: str,
    filter_: Optional[str] = None,
    metadata: Optional[str] = None,
    name: Optional[str] = None,
    ordering_info: Optional[str] = None,
    publish_to_shops: Optional[str] = None,
    retailer_id: Optional[str] = None,
) -> str:
    """POST /#update on ProductSet.

    Args:
        product_set_id: The ID of the ProductSet object.
        filter_: Optional.
        metadata: Optional.
        name: Optional.
        ordering_info: Optional.
        publish_to_shops: Optional.
        retailer_id: Optional.
    """
    params = {}
    if filter_ is not None:
        params["filter"] = filter_
    if metadata is not None:
        params["metadata"] = metadata
    if name is not None:
        params["name"] = name
    if ordering_info is not None:
        params["ordering_info"] = ordering_info
    if publish_to_shops is not None:
        params["publish_to_shops"] = publish_to_shops
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    result = await get_client().post(f"{product_set_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_ITEM_FIELDS = [
    "additional_image_cdn_urls",
    "additional_image_urls",
    "additional_variant_attributes",
    "age_group",
    "applinks",
    "availability",
    "brand",
    "bundle_items",
    "bundle_retailer_ids",
    "capabilities_disabled_by_user",
    "capability_to_review_status",
    "category",
    "category_specific_fields",
    "color",
    "commerce_insights",
    "condition",
    "currency",
    "custom_data",
    "custom_label_0",
    "custom_label_1",
    "custom_label_2",
    "custom_label_3",
    "custom_label_4",
    "custom_number_0",
    "custom_number_1",
    "custom_number_2",
    "custom_number_3",
    "custom_number_4",
    "description",
    "errors",
    "expiration_date",
    "fb_product_category",
    "gender",
    "generated_background_images",
    "generated_background_images_ad_usage",
    "gtin",
    "id",
    "image_cdn_urls",
    "image_fetch_status",
    "image_url",
    "images",
    "importer_address",
    "importer_name",
    "invalidation_errors",
    "inventory",
    "is_bundle_hero",
    "live_special_price",
    "manufacturer_info",
    "manufacturer_part_number",
    "marked_for_product_launch",
    "material",
    "mobile_link",
    "name",
    "ordering_index",
    "origin_country",
    "parent_product_id",
    "pattern",
    "post_conversion_signal_based_enforcement_appeal_eligibility",
    "price",
    "product_catalog",
    "product_feed",
    "product_group",
    "product_local_info",
    "product_relationship",
    "product_type",
    "quantity_to_sell_on_facebook",
    "retailer_id",
    "retailer_product_group_id",
    "review_rejection_reasons",
    "review_status",
    "rich_text_description",
    "sale_price",
    "sale_price_end_date",
    "sale_price_start_date",
    "shipping_weight_unit",
    "shipping_weight_value",
    "short_description",
    "size",
    "start_date",
    "status",
    "tags",
    "url",
    "vendor_id",
    "video_fetch_status",
    "videos",
    "visibility",
    "wa_compliance_category"
]


async def get_product_item_channels_to_integrity_status(product_item_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_item_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_product_item_override_details(
    product_item_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        fields: Comma-separated list of fields to return.
        keys: Optional.
        type_: Optional. Values: COUNTRY, LANGUAGE, LANGUAGE_AND_COUNTRY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if keys is not None:
        params["keys"] = keys
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{product_item_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_product_item_product_sets(product_item_id: str, fields: Optional[str] = None) -> str:
    """GET /product_sets on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_item_id}/product_sets", params=params)
    return json.dumps(result, indent=2)


async def get_product_item_videos_metadata(product_item_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_item_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def delete_product_item(product_item_id: str) -> str:
    """DELETE /#delete on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
    """
    params = {}
    result = await get_client().delete(f"{product_item_id}")
    return json.dumps(result, indent=2)


async def get_product_item(
    product_item_id: str,
    fields: Optional[str] = None,
    catalog_id: Optional[str] = None,
    image_height: Optional[int] = None,
    image_width: Optional[int] = None,
    override_country: Optional[str] = None,
    override_language: Optional[str] = None,
) -> str:
    """GET /#get on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        fields: Comma-separated list of fields to return. Available: additional_image_cdn_urls, additional_image_urls, additional_variant_attributes, age_group, applinks, availability, brand, bundle_items, bundle_retailer_ids, capabilities_disabled_by_user, capability_to_review_status, category, category_specific_fields, color, commerce_insights, condition, currency, custom_data, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, errors, expiration_date, fb_product_category, gender, generated_background_images, generated_background_images_ad_usage, gtin, id, image_cdn_urls, image_fetch_status, image_url, images, importer_address, importer_name, invalidation_errors, inventory, is_bundle_hero, live_special_price, manufacturer_info, manufacturer_part_number, marked_for_product_launch, material, mobile_link, name, ordering_index, origin_country, parent_product_id, pattern, post_conversion_signal_based_enforcement_appeal_eligibility, price, product_catalog, product_feed, product_group, product_local_info, product_relationship, product_type, quantity_to_sell_on_facebook, retailer_id, retailer_product_group_id, review_rejection_reasons, review_status, rich_text_description, sale_price, sale_price_end_date, sale_price_start_date, shipping_weight_unit, shipping_weight_value, short_description, size, start_date, status, tags, url, vendor_id, video_fetch_status, videos, visibility, wa_compliance_category
        catalog_id: Optional.
        image_height: Optional.
        image_width: Optional.
        override_country: Optional.
        override_language: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if catalog_id is not None:
        params["catalog_id"] = catalog_id
    if image_height is not None:
        params["image_height"] = image_height
    if image_width is not None:
        params["image_width"] = image_width
    if override_country is not None:
        params["override_country"] = override_country
    if override_language is not None:
        params["override_language"] = override_language
    result = await get_client().get(f"{product_item_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_item(
    product_item_id: str,
    additional_image_urls: Optional[str] = None,
    additional_variant_attributes: Optional[str] = None,
    age_group: Optional[str] = None,
    android_app_name: Optional[str] = None,
    android_class: Optional[str] = None,
    android_package: Optional[str] = None,
    android_url: Optional[str] = None,
    availability: Optional[str] = None,
    brand: Optional[str] = None,
    category: Optional[str] = None,
    category_specific_fields: Optional[str] = None,
    checkout_url: Optional[str] = None,
    color: Optional[str] = None,
    commerce_tax_category: Optional[str] = None,
    condition: Optional[str] = None,
    currency: Optional[str] = None,
    custom_data: Optional[str] = None,
    custom_label_0: Optional[str] = None,
    custom_label_1: Optional[str] = None,
    custom_label_2: Optional[str] = None,
    custom_label_3: Optional[str] = None,
    custom_label_4: Optional[str] = None,
    custom_number_0: Optional[int] = None,
    custom_number_1: Optional[int] = None,
    custom_number_2: Optional[int] = None,
    custom_number_3: Optional[int] = None,
    custom_number_4: Optional[int] = None,
    description: Optional[str] = None,
    expiration_date: Optional[str] = None,
    fb_product_category: Optional[str] = None,
    gender: Optional[str] = None,
    gtin: Optional[str] = None,
    image_url: Optional[str] = None,
    importer_address: Optional[str] = None,
    importer_name: Optional[str] = None,
    inventory: Optional[int] = None,
    ios_app_name: Optional[str] = None,
    ios_app_store_id: Optional[int] = None,
    ios_url: Optional[str] = None,
    ipad_app_name: Optional[str] = None,
    ipad_app_store_id: Optional[int] = None,
    ipad_url: Optional[str] = None,
    iphone_app_name: Optional[str] = None,
    iphone_app_store_id: Optional[int] = None,
    iphone_url: Optional[str] = None,
    launch_date: Optional[str] = None,
    live_special_price: Optional[str] = None,
    manufacturer_info: Optional[str] = None,
    manufacturer_part_number: Optional[str] = None,
    marked_for_product_launch: Optional[str] = None,
    material: Optional[str] = None,
    mobile_link: Optional[str] = None,
    name: Optional[str] = None,
    ordering_index: Optional[int] = None,
    origin_country: Optional[str] = None,
    pattern: Optional[str] = None,
    price: Optional[int] = None,
    product_priority_0: Optional[float] = None,
    product_priority_1: Optional[float] = None,
    product_priority_2: Optional[float] = None,
    product_priority_3: Optional[float] = None,
    product_priority_4: Optional[float] = None,
    product_type: Optional[str] = None,
    quantity_to_sell_on_facebook: Optional[int] = None,
    retailer_id: Optional[str] = None,
    return_policy_days: Optional[int] = None,
    rich_text_description: Optional[str] = None,
    sale_price: Optional[int] = None,
    sale_price_end_date: Optional[str] = None,
    sale_price_start_date: Optional[str] = None,
    short_description: Optional[str] = None,
    size: Optional[str] = None,
    start_date: Optional[str] = None,
    url: Optional[str] = None,
    visibility: Optional[str] = None,
    wa_compliance_category: Optional[str] = None,
    windows_phone_app_id: Optional[str] = None,
    windows_phone_app_name: Optional[str] = None,
    windows_phone_url: Optional[str] = None,
) -> str:
    """POST /#update on ProductItem.

    Args:
        product_item_id: The ID of the ProductItem object.
        additional_image_urls: Optional.
        additional_variant_attributes: Optional.
        age_group: Optional.
        android_app_name: Optional.
        android_class: Optional.
        android_package: Optional.
        android_url: Optional.
        availability: Optional.
        brand: Optional.
        category: Optional.
        category_specific_fields: Optional.
        checkout_url: Optional.
        color: Optional.
        commerce_tax_category: Optional.
        condition: Optional.
        currency: Optional.
        custom_data: Optional.
        custom_label_0: Optional.
        custom_label_1: Optional.
        custom_label_2: Optional.
        custom_label_3: Optional.
        custom_label_4: Optional.
        custom_number_0: Optional.
        custom_number_1: Optional.
        custom_number_2: Optional.
        custom_number_3: Optional.
        custom_number_4: Optional.
        description: Optional.
        expiration_date: Optional.
        fb_product_category: Optional.
        gender: Optional.
        gtin: Optional.
        image_url: Optional.
        importer_address: Optional.
        importer_name: Optional.
        inventory: Optional.
        ios_app_name: Optional.
        ios_app_store_id: Optional.
        ios_url: Optional.
        ipad_app_name: Optional.
        ipad_app_store_id: Optional.
        ipad_url: Optional.
        iphone_app_name: Optional.
        iphone_app_store_id: Optional.
        iphone_url: Optional.
        launch_date: Optional.
        live_special_price: Optional.
        manufacturer_info: Optional.
        manufacturer_part_number: Optional.
        marked_for_product_launch: Optional.
        material: Optional.
        mobile_link: Optional.
        name: Optional.
        ordering_index: Optional.
        origin_country: Optional.
        pattern: Optional.
        price: Optional.
        product_priority_0: Optional.
        product_priority_1: Optional.
        product_priority_2: Optional.
        product_priority_3: Optional.
        product_priority_4: Optional.
        product_type: Optional.
        quantity_to_sell_on_facebook: Optional.
        retailer_id: Optional.
        return_policy_days: Optional.
        rich_text_description: Optional.
        sale_price: Optional.
        sale_price_end_date: Optional.
        sale_price_start_date: Optional.
        short_description: Optional.
        size: Optional.
        start_date: Optional.
        url: Optional.
        visibility: Optional.
        wa_compliance_category: Optional.
        windows_phone_app_id: Optional.
        windows_phone_app_name: Optional.
        windows_phone_url: Optional.
    """
    params = {}
    if additional_image_urls is not None:
        params["additional_image_urls"] = additional_image_urls
    if additional_variant_attributes is not None:
        params["additional_variant_attributes"] = additional_variant_attributes
    if age_group is not None:
        params["age_group"] = age_group
    if android_app_name is not None:
        params["android_app_name"] = android_app_name
    if android_class is not None:
        params["android_class"] = android_class
    if android_package is not None:
        params["android_package"] = android_package
    if android_url is not None:
        params["android_url"] = android_url
    if availability is not None:
        params["availability"] = availability
    if brand is not None:
        params["brand"] = brand
    if category is not None:
        params["category"] = category
    if category_specific_fields is not None:
        params["category_specific_fields"] = category_specific_fields
    if checkout_url is not None:
        params["checkout_url"] = checkout_url
    if color is not None:
        params["color"] = color
    if commerce_tax_category is not None:
        params["commerce_tax_category"] = commerce_tax_category
    if condition is not None:
        params["condition"] = condition
    if currency is not None:
        params["currency"] = currency
    if custom_data is not None:
        params["custom_data"] = custom_data
    if custom_label_0 is not None:
        params["custom_label_0"] = custom_label_0
    if custom_label_1 is not None:
        params["custom_label_1"] = custom_label_1
    if custom_label_2 is not None:
        params["custom_label_2"] = custom_label_2
    if custom_label_3 is not None:
        params["custom_label_3"] = custom_label_3
    if custom_label_4 is not None:
        params["custom_label_4"] = custom_label_4
    if custom_number_0 is not None:
        params["custom_number_0"] = custom_number_0
    if custom_number_1 is not None:
        params["custom_number_1"] = custom_number_1
    if custom_number_2 is not None:
        params["custom_number_2"] = custom_number_2
    if custom_number_3 is not None:
        params["custom_number_3"] = custom_number_3
    if custom_number_4 is not None:
        params["custom_number_4"] = custom_number_4
    if description is not None:
        params["description"] = description
    if expiration_date is not None:
        params["expiration_date"] = expiration_date
    if fb_product_category is not None:
        params["fb_product_category"] = fb_product_category
    if gender is not None:
        params["gender"] = gender
    if gtin is not None:
        params["gtin"] = gtin
    if image_url is not None:
        params["image_url"] = image_url
    if importer_address is not None:
        params["importer_address"] = importer_address
    if importer_name is not None:
        params["importer_name"] = importer_name
    if inventory is not None:
        params["inventory"] = inventory
    if ios_app_name is not None:
        params["ios_app_name"] = ios_app_name
    if ios_app_store_id is not None:
        params["ios_app_store_id"] = ios_app_store_id
    if ios_url is not None:
        params["ios_url"] = ios_url
    if ipad_app_name is not None:
        params["ipad_app_name"] = ipad_app_name
    if ipad_app_store_id is not None:
        params["ipad_app_store_id"] = ipad_app_store_id
    if ipad_url is not None:
        params["ipad_url"] = ipad_url
    if iphone_app_name is not None:
        params["iphone_app_name"] = iphone_app_name
    if iphone_app_store_id is not None:
        params["iphone_app_store_id"] = iphone_app_store_id
    if iphone_url is not None:
        params["iphone_url"] = iphone_url
    if launch_date is not None:
        params["launch_date"] = launch_date
    if live_special_price is not None:
        params["live_special_price"] = live_special_price
    if manufacturer_info is not None:
        params["manufacturer_info"] = manufacturer_info
    if manufacturer_part_number is not None:
        params["manufacturer_part_number"] = manufacturer_part_number
    if marked_for_product_launch is not None:
        params["marked_for_product_launch"] = marked_for_product_launch
    if material is not None:
        params["material"] = material
    if mobile_link is not None:
        params["mobile_link"] = mobile_link
    if name is not None:
        params["name"] = name
    if ordering_index is not None:
        params["ordering_index"] = ordering_index
    if origin_country is not None:
        params["origin_country"] = origin_country
    if pattern is not None:
        params["pattern"] = pattern
    if price is not None:
        params["price"] = price
    if product_priority_0 is not None:
        params["product_priority_0"] = product_priority_0
    if product_priority_1 is not None:
        params["product_priority_1"] = product_priority_1
    if product_priority_2 is not None:
        params["product_priority_2"] = product_priority_2
    if product_priority_3 is not None:
        params["product_priority_3"] = product_priority_3
    if product_priority_4 is not None:
        params["product_priority_4"] = product_priority_4
    if product_type is not None:
        params["product_type"] = product_type
    if quantity_to_sell_on_facebook is not None:
        params["quantity_to_sell_on_facebook"] = quantity_to_sell_on_facebook
    if retailer_id is not None:
        params["retailer_id"] = retailer_id
    if return_policy_days is not None:
        params["return_policy_days"] = return_policy_days
    if rich_text_description is not None:
        params["rich_text_description"] = rich_text_description
    if sale_price is not None:
        params["sale_price"] = sale_price
    if sale_price_end_date is not None:
        params["sale_price_end_date"] = sale_price_end_date
    if sale_price_start_date is not None:
        params["sale_price_start_date"] = sale_price_start_date
    if short_description is not None:
        params["short_description"] = short_description
    if size is not None:
        params["size"] = size
    if start_date is not None:
        params["start_date"] = start_date
    if url is not None:
        params["url"] = url
    if visibility is not None:
        params["visibility"] = visibility
    if wa_compliance_category is not None:
        params["wa_compliance_category"] = wa_compliance_category
    if windows_phone_app_id is not None:
        params["windows_phone_app_id"] = windows_phone_app_id
    if windows_phone_app_name is not None:
        params["windows_phone_app_name"] = windows_phone_app_name
    if windows_phone_url is not None:
        params["windows_phone_url"] = windows_phone_url
    result = await get_client().post(f"{product_item_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_GROUP_FIELDS = [
    "id",
    "product_catalog",
    "retailer_id",
    "variants"
]


async def get_product_group_products(product_group_id: str, fields: Optional[str] = None) -> str:
    """GET /products on ProductGroup.

    Args:
        product_group_id: The ID of the ProductGroup object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_group_id}/products", params=params)
    return json.dumps(result, indent=2)


async def create_product_group_products(
    product_group_id: str,
    currency: str,
    image_url: str,
    name: str,
    price: int,
    retailer_id: str,
    additional_image_urls: Optional[str] = None,
    additional_variant_attributes: Optional[str] = None,
    age_group: Optional[str] = None,
    android_app_name: Optional[str] = None,
    android_class: Optional[str] = None,
    android_package: Optional[str] = None,
    android_url: Optional[str] = None,
    availability: Optional[str] = None,
    brand: Optional[str] = None,
    category: Optional[str] = None,
    checkout_url: Optional[str] = None,
    color: Optional[str] = None,
    commerce_tax_category: Optional[str] = None,
    condition: Optional[str] = None,
    custom_data: Optional[str] = None,
    custom_label_0: Optional[str] = None,
    custom_label_1: Optional[str] = None,
    custom_label_2: Optional[str] = None,
    custom_label_3: Optional[str] = None,
    custom_label_4: Optional[str] = None,
    custom_number_0: Optional[int] = None,
    custom_number_1: Optional[int] = None,
    custom_number_2: Optional[int] = None,
    custom_number_3: Optional[int] = None,
    custom_number_4: Optional[int] = None,
    description: Optional[str] = None,
    expiration_date: Optional[str] = None,
    fb_product_category: Optional[str] = None,
    gender: Optional[str] = None,
    gtin: Optional[str] = None,
    inventory: Optional[int] = None,
    ios_app_name: Optional[str] = None,
    ios_app_store_id: Optional[int] = None,
    ios_url: Optional[str] = None,
    ipad_app_name: Optional[str] = None,
    ipad_app_store_id: Optional[int] = None,
    ipad_url: Optional[str] = None,
    iphone_app_name: Optional[str] = None,
    iphone_app_store_id: Optional[int] = None,
    iphone_url: Optional[str] = None,
    launch_date: Optional[str] = None,
    live_special_price: Optional[str] = None,
    manufacturer_part_number: Optional[str] = None,
    marked_for_product_launch: Optional[str] = None,
    material: Optional[str] = None,
    mobile_link: Optional[str] = None,
    ordering_index: Optional[int] = None,
    pattern: Optional[str] = None,
    product_priority_0: Optional[float] = None,
    product_priority_1: Optional[float] = None,
    product_priority_2: Optional[float] = None,
    product_priority_3: Optional[float] = None,
    product_priority_4: Optional[float] = None,
    product_type: Optional[str] = None,
    quantity_to_sell_on_facebook: Optional[int] = None,
    return_policy_days: Optional[int] = None,
    rich_text_description: Optional[str] = None,
    sale_price: Optional[int] = None,
    sale_price_end_date: Optional[str] = None,
    sale_price_start_date: Optional[str] = None,
    short_description: Optional[str] = None,
    size: Optional[str] = None,
    start_date: Optional[str] = None,
    url: Optional[str] = None,
    visibility: Optional[str] = None,
    windows_phone_app_id: Optional[str] = None,
    windows_phone_app_name: Optional[str] = None,
    windows_phone_url: Optional[str] = None,
) -> str:
    """POST /products on ProductGroup.

    Args:
        product_group_id: The ID of the ProductGroup object.
        additional_image_urls: Optional.
        additional_variant_attributes: Optional.
        age_group: Optional. Values: adult, all ages, infant, kids, newborn, teen, toddler
        android_app_name: Optional.
        android_class: Optional.
        android_package: Optional.
        android_url: Optional.
        availability: Optional. Values: available for order, discontinued, in stock, mark_as_sold, out of stock, pending, preorder
        brand: Optional.
        category: Optional.
        checkout_url: Optional.
        color: Optional.
        commerce_tax_category: Optional. Values: FB_ANIMAL, FB_ANIMAL_SUPP, FB_APRL, FB_APRL_ACCESSORIES, FB_APRL_ATHL_UNIF, FB_APRL_CASES, FB_APRL_CLOTHING, FB_APRL_COSTUME, FB_APRL_CSTM, FB_APRL_FORMAL, FB_APRL_HANDBAG, FB_APRL_JEWELRY, FB_APRL_SHOE, FB_APRL_SHOE_ACC, FB_APRL_SWIM, FB_APRL_SWIM_CHIL, FB_APRL_SWIM_CVR, FB_ARTS, FB_ARTS_HOBBY, FB_ARTS_PARTY, FB_ARTS_PARTY_GIFT_CARD, FB_ARTS_TICKET, FB_BABY, FB_BABY_BATH, FB_BABY_BLANKET, FB_BABY_DIAPER, FB_BABY_GIFT_SET, FB_BABY_HEALTH, FB_BABY_NURSING, FB_BABY_POTTY_TRN, FB_BABY_SAFE, FB_BABY_TOYS, FB_BABY_TRANSPORT, FB_BABY_TRANSPORT_ACC, FB_BAGS, FB_BAGS_BKPK, FB_BAGS_BOXES, FB_BAGS_BRFCS, FB_BAGS_CSMT_BAG, FB_BAGS_DFFL, FB_BAGS_DIPR, FB_BAGS_FNNY, FB_BAGS_GRMT, FB_BAGS_LUGG, FB_BAGS_LUG_ACC, FB_BAGS_MSGR, FB_BAGS_TOTE, FB_BAGS_TRN_CAS, FB_BLDG, FB_BLDG_ACC, FB_BLDG_CNSMB, FB_BLDG_FENCE, FB_BLDG_FUEL_TNK, FB_BLDG_HT_VNT, FB_BLDG_LOCK, FB_BLDG_MATRL, FB_BLDG_PLMB, FB_BLDG_PUMP, FB_BLDG_PWRS, FB_BLDG_STR_TANK, FB_BLDG_S_ENG, FB_BLDG_TL_ACC, FB_BLDG_TOOL, FB_BUSIND, FB_BUSIND_ADVERTISING, FB_BUSIND_AGRICULTURE, FB_BUSIND_AUTOMATION, FB_BUSIND_HEAVY_MACH, FB_BUSIND_LAB, FB_BUSIND_MEDICAL, FB_BUSIND_RETAIL, FB_BUSIND_SANITARY_CT, FB_BUSIND_SIGN, FB_BUSIND_STORAGE, FB_BUSIND_STORAGE_ACC, FB_BUSIND_WORK_GEAR, FB_CAMERA_ACC, FB_CAMERA_CAMERA, FB_CAMERA_OPTIC, FB_CAMERA_OPTICS, FB_CAMERA_PHOTO, FB_ELEC, FB_ELEC_ACC, FB_ELEC_ARCDADE, FB_ELEC_AUDIO, FB_ELEC_CIRCUIT, FB_ELEC_COMM, FB_ELEC_COMPUTER, FB_ELEC_GPS_ACC, FB_ELEC_GPS_NAV, FB_ELEC_GPS_TRK, FB_ELEC_MARINE, FB_ELEC_NETWORK, FB_ELEC_PART, FB_ELEC_PRINT, FB_ELEC_RADAR, FB_ELEC_SFTWR, FB_ELEC_SPEED_RDR, FB_ELEC_TELEVISION, FB_ELEC_TOLL, FB_ELEC_VIDEO, FB_ELEC_VID_GM_ACC, FB_ELEC_VID_GM_CNSL, FB_FOOD, FB_FURN, FB_FURN_BABY, FB_FURN_BENCH, FB_FURN_CART, FB_FURN_CHAIR, FB_FURN_CHAIR_ACC, FB_FURN_DIVIDE, FB_FURN_DIVIDE_ACC, FB_FURN_ENT_CTR, FB_FURN_FUTN, FB_FURN_FUTN_PAD, FB_FURN_OFFICE, FB_FURN_OFFICE_ACC, FB_FURN_OTTO, FB_FURN_OUTDOOR, FB_FURN_OUTDOOR_ACC, FB_FURN_SETS, FB_FURN_SHELVE_ACC, FB_FURN_SHLF, FB_FURN_SOFA, FB_FURN_SOFA_ACC, FB_FURN_STORAGE, FB_FURN_TABL, FB_FURN_TABL_ACC, FB_GENERIC_TAXABLE, FB_HLTH, FB_HLTH_HLTH, FB_HLTH_JWL_CR, FB_HLTH_LILP_BLM, FB_HLTH_LTN_SPF, FB_HLTH_PRSL_CR, FB_HLTH_SKN_CR, FB_HMGN, FB_HMGN_BATH, FB_HMGN_DCOR, FB_HMGN_EMGY, FB_HMGN_FPLC, FB_HMGN_FPLC_ACC, FB_HMGN_GS_SFT, FB_HMGN_HS_ACC, FB_HMGN_HS_APP, FB_HMGN_HS_SPL, FB_HMGN_KTCN, FB_HMGN_LAWN, FB_HMGN_LGHT, FB_HMGN_LINN, FB_HMGN_LT_ACC, FB_HMGN_OTDR, FB_HMGN_POOL, FB_HMGN_SCTY, FB_HMGN_SMK_ACC, FB_HMGN_UMBR, FB_HMGN_UMBR_ACC, FB_MDIA, FB_MDIA_BOOK, FB_MDIA_DVDS, FB_MDIA_MAG, FB_MDIA_MANL, FB_MDIA_MUSC, FB_MDIA_PRJ_PLN, FB_MDIA_SHT_MUS, FB_OFFC, FB_OFFC_BKAC, FB_OFFC_CRTS, FB_OFFC_DSKP, FB_OFFC_EQIP, FB_OFFC_FLNG, FB_OFFC_GNRL, FB_OFFC_INSTM, FB_OFFC_LP_DSK, FB_OFFC_MATS, FB_OFFC_NM_PLT, FB_OFFC_PPR_HNDL, FB_OFFC_PRSNT_SPL, FB_OFFC_SEALR, FB_OFFC_SHIP_SPL, FB_RLGN, FB_RLGN_CMNY, FB_RLGN_ITEM, FB_RLGN_WEDD, FB_SFTWR, FB_SFWR_CMPTR, FB_SFWR_DGTL_GD, FB_SFWR_GAME, FB_SHIPPING, FB_SPOR, FB_SPORT_ATHL, FB_SPORT_ATHL_CLTH, FB_SPORT_ATHL_SHOE, FB_SPORT_ATHL_SPRT, FB_SPORT_EXRCS, FB_SPORT_INDR_GM, FB_SPORT_OTDR_GM, FB_TOYS, FB_TOYS_EQIP, FB_TOYS_GAME, FB_TOYS_PZZL, FB_TOYS_TMRS, FB_TOYS_TOYS, FB_VEHI, FB_VEHI_PART
        condition: Optional. Values: cpo, new, open_box_new, refurbished, used, used_fair, used_good, used_like_new
        currency: Required.
        custom_data: Optional.
        custom_label_0: Optional.
        custom_label_1: Optional.
        custom_label_2: Optional.
        custom_label_3: Optional.
        custom_label_4: Optional.
        custom_number_0: Optional.
        custom_number_1: Optional.
        custom_number_2: Optional.
        custom_number_3: Optional.
        custom_number_4: Optional.
        description: Optional.
        expiration_date: Optional.
        fb_product_category: Optional.
        gender: Optional. Values: female, male, unisex
        gtin: Optional.
        image_url: Required.
        inventory: Optional.
        ios_app_name: Optional.
        ios_app_store_id: Optional.
        ios_url: Optional.
        ipad_app_name: Optional.
        ipad_app_store_id: Optional.
        ipad_url: Optional.
        iphone_app_name: Optional.
        iphone_app_store_id: Optional.
        iphone_url: Optional.
        launch_date: Optional.
        live_special_price: Optional.
        manufacturer_part_number: Optional.
        marked_for_product_launch: Optional. Values: default, marked, not_marked
        material: Optional.
        mobile_link: Optional.
        name: Required.
        ordering_index: Optional.
        pattern: Optional.
        price: Required.
        product_priority_0: Optional.
        product_priority_1: Optional.
        product_priority_2: Optional.
        product_priority_3: Optional.
        product_priority_4: Optional.
        product_type: Optional.
        quantity_to_sell_on_facebook: Optional.
        retailer_id: Required.
        return_policy_days: Optional.
        rich_text_description: Optional.
        sale_price: Optional.
        sale_price_end_date: Optional.
        sale_price_start_date: Optional.
        short_description: Optional.
        size: Optional.
        start_date: Optional.
        url: Optional.
        visibility: Optional. Values: published, staging
        windows_phone_app_id: Optional.
        windows_phone_app_name: Optional.
        windows_phone_url: Optional.
    """
    params = {}
    if additional_image_urls is not None:
        params["additional_image_urls"] = additional_image_urls
    if additional_variant_attributes is not None:
        params["additional_variant_attributes"] = additional_variant_attributes
    if age_group is not None:
        params["age_group"] = age_group
    if android_app_name is not None:
        params["android_app_name"] = android_app_name
    if android_class is not None:
        params["android_class"] = android_class
    if android_package is not None:
        params["android_package"] = android_package
    if android_url is not None:
        params["android_url"] = android_url
    if availability is not None:
        params["availability"] = availability
    if brand is not None:
        params["brand"] = brand
    if category is not None:
        params["category"] = category
    if checkout_url is not None:
        params["checkout_url"] = checkout_url
    if color is not None:
        params["color"] = color
    if commerce_tax_category is not None:
        params["commerce_tax_category"] = commerce_tax_category
    if condition is not None:
        params["condition"] = condition
    params["currency"] = currency
    if custom_data is not None:
        params["custom_data"] = custom_data
    if custom_label_0 is not None:
        params["custom_label_0"] = custom_label_0
    if custom_label_1 is not None:
        params["custom_label_1"] = custom_label_1
    if custom_label_2 is not None:
        params["custom_label_2"] = custom_label_2
    if custom_label_3 is not None:
        params["custom_label_3"] = custom_label_3
    if custom_label_4 is not None:
        params["custom_label_4"] = custom_label_4
    if custom_number_0 is not None:
        params["custom_number_0"] = custom_number_0
    if custom_number_1 is not None:
        params["custom_number_1"] = custom_number_1
    if custom_number_2 is not None:
        params["custom_number_2"] = custom_number_2
    if custom_number_3 is not None:
        params["custom_number_3"] = custom_number_3
    if custom_number_4 is not None:
        params["custom_number_4"] = custom_number_4
    if description is not None:
        params["description"] = description
    if expiration_date is not None:
        params["expiration_date"] = expiration_date
    if fb_product_category is not None:
        params["fb_product_category"] = fb_product_category
    if gender is not None:
        params["gender"] = gender
    if gtin is not None:
        params["gtin"] = gtin
    params["image_url"] = image_url
    if inventory is not None:
        params["inventory"] = inventory
    if ios_app_name is not None:
        params["ios_app_name"] = ios_app_name
    if ios_app_store_id is not None:
        params["ios_app_store_id"] = ios_app_store_id
    if ios_url is not None:
        params["ios_url"] = ios_url
    if ipad_app_name is not None:
        params["ipad_app_name"] = ipad_app_name
    if ipad_app_store_id is not None:
        params["ipad_app_store_id"] = ipad_app_store_id
    if ipad_url is not None:
        params["ipad_url"] = ipad_url
    if iphone_app_name is not None:
        params["iphone_app_name"] = iphone_app_name
    if iphone_app_store_id is not None:
        params["iphone_app_store_id"] = iphone_app_store_id
    if iphone_url is not None:
        params["iphone_url"] = iphone_url
    if launch_date is not None:
        params["launch_date"] = launch_date
    if live_special_price is not None:
        params["live_special_price"] = live_special_price
    if manufacturer_part_number is not None:
        params["manufacturer_part_number"] = manufacturer_part_number
    if marked_for_product_launch is not None:
        params["marked_for_product_launch"] = marked_for_product_launch
    if material is not None:
        params["material"] = material
    if mobile_link is not None:
        params["mobile_link"] = mobile_link
    params["name"] = name
    if ordering_index is not None:
        params["ordering_index"] = ordering_index
    if pattern is not None:
        params["pattern"] = pattern
    params["price"] = price
    if product_priority_0 is not None:
        params["product_priority_0"] = product_priority_0
    if product_priority_1 is not None:
        params["product_priority_1"] = product_priority_1
    if product_priority_2 is not None:
        params["product_priority_2"] = product_priority_2
    if product_priority_3 is not None:
        params["product_priority_3"] = product_priority_3
    if product_priority_4 is not None:
        params["product_priority_4"] = product_priority_4
    if product_type is not None:
        params["product_type"] = product_type
    if quantity_to_sell_on_facebook is not None:
        params["quantity_to_sell_on_facebook"] = quantity_to_sell_on_facebook
    params["retailer_id"] = retailer_id
    if return_policy_days is not None:
        params["return_policy_days"] = return_policy_days
    if rich_text_description is not None:
        params["rich_text_description"] = rich_text_description
    if sale_price is not None:
        params["sale_price"] = sale_price
    if sale_price_end_date is not None:
        params["sale_price_end_date"] = sale_price_end_date
    if sale_price_start_date is not None:
        params["sale_price_start_date"] = sale_price_start_date
    if short_description is not None:
        params["short_description"] = short_description
    if size is not None:
        params["size"] = size
    if start_date is not None:
        params["start_date"] = start_date
    if url is not None:
        params["url"] = url
    if visibility is not None:
        params["visibility"] = visibility
    if windows_phone_app_id is not None:
        params["windows_phone_app_id"] = windows_phone_app_id
    if windows_phone_app_name is not None:
        params["windows_phone_app_name"] = windows_phone_app_name
    if windows_phone_url is not None:
        params["windows_phone_url"] = windows_phone_url
    result = await get_client().post(f"{product_group_id}/products", data=params)
    return json.dumps(result, indent=2)


async def delete_product_group(product_group_id: str, deletion_method: Optional[str] = None) -> str:
    """DELETE /#delete on ProductGroup.

    Args:
        product_group_id: The ID of the ProductGroup object.
        deletion_method: Optional.
    """
    params = {}
    if deletion_method is not None:
        params["deletion_method"] = deletion_method
    result = await get_client().delete(f"{product_group_id}")
    return json.dumps(result, indent=2)


async def get_product_group(product_group_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductGroup.

    Args:
        product_group_id: The ID of the ProductGroup object.
        fields: Comma-separated list of fields to return. Available: id, product_catalog, retailer_id, variants
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_group_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_group(
    product_group_id: str,
    default_product_id: Optional[str] = None,
    variants: Optional[str] = None,
) -> str:
    """POST /#update on ProductGroup.

    Args:
        product_group_id: The ID of the ProductGroup object.
        default_product_id: Optional.
        variants: Optional.
    """
    params = {}
    if default_product_id is not None:
        params["default_product_id"] = default_product_id
    if variants is not None:
        params["variants"] = variants
    result = await get_client().post(f"{product_group_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_FEED_RULE_FIELDS = [
    "attribute",
    "id",
    "params",
    "rule_type"
]


async def delete_product_feed_rule(product_feed_rule_id: str) -> str:
    """DELETE /#delete on ProductFeedRule.

    Args:
        product_feed_rule_id: The ID of the ProductFeedRule object.
    """
    params = {}
    result = await get_client().delete(f"{product_feed_rule_id}")
    return json.dumps(result, indent=2)


async def get_product_feed_rule(product_feed_rule_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductFeedRule.

    Args:
        product_feed_rule_id: The ID of the ProductFeedRule object.
        fields: Comma-separated list of fields to return. Available: attribute, id, params, rule_type
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_rule_id}", params=params)
    return json.dumps(result, indent=2)


async def update_product_feed_rule(product_feed_rule_id: str, params: str) -> str:
    """POST /#update on ProductFeedRule.

    Args:
        product_feed_rule_id: The ID of the ProductFeedRule object.
        params: Required.
    """
    params = {}
    params["params"] = params
    result = await get_client().post(f"{product_feed_rule_id}", data=params)
    return json.dumps(result, indent=2)


PRODUCT_FEED_UPLOAD_FIELDS = [
    "end_time",
    "error_count",
    "error_report",
    "filename",
    "id",
    "input_method",
    "num_deleted_items",
    "num_detected_items",
    "num_invalid_items",
    "num_persisted_items",
    "start_time",
    "url",
    "warning_count"
]


async def create_product_feed_upload_error_report(product_feed_upload_id: str) -> str:
    """POST /error_report on ProductFeedUpload.

    Args:
        product_feed_upload_id: The ID of the ProductFeedUpload object.
    """
    params = {}
    result = await get_client().post(f"{product_feed_upload_id}/error_report", data=params)
    return json.dumps(result, indent=2)


async def get_product_feed_upload_errors(
    product_feed_upload_id: str,
    fields: Optional[str] = None,
    error_priority: Optional[str] = None,
) -> str:
    """GET /errors on ProductFeedUpload.

    Args:
        product_feed_upload_id: The ID of the ProductFeedUpload object.
        fields: Comma-separated list of fields to return.
        error_priority: Optional. Values: HIGH, LOW, MEDIUM
    """
    params = {}
    params["fields"] = fields or "id,name"
    if error_priority is not None:
        params["error_priority"] = error_priority
    result = await get_client().get(f"{product_feed_upload_id}/errors", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_upload(product_feed_upload_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductFeedUpload.

    Args:
        product_feed_upload_id: The ID of the ProductFeedUpload object.
        fields: Comma-separated list of fields to return. Available: end_time, error_count, error_report, filename, id, input_method, num_deleted_items, num_detected_items, num_invalid_items, num_persisted_items, start_time, url, warning_count
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_upload_id}", params=params)
    return json.dumps(result, indent=2)


PRODUCT_FEED_UPLOAD_ERROR_FIELDS = [
    "affected_surfaces",
    "description",
    "error_type",
    "id",
    "severity",
    "summary",
    "total_count"
]


async def get_product_feed_upload_error_samples(product_feed_upload_error_id: str, fields: Optional[str] = None) -> str:
    """GET /samples on ProductFeedUploadError.

    Args:
        product_feed_upload_error_id: The ID of the ProductFeedUploadError object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_upload_error_id}/samples", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_upload_error_suggested_rules(product_feed_upload_error_id: str, fields: Optional[str] = None) -> str:
    """GET /suggested_rules on ProductFeedUploadError.

    Args:
        product_feed_upload_error_id: The ID of the ProductFeedUploadError object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_upload_error_id}/suggested_rules", params=params)
    return json.dumps(result, indent=2)


async def get_product_feed_upload_error(product_feed_upload_error_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on ProductFeedUploadError.

    Args:
        product_feed_upload_error_id: The ID of the ProductFeedUploadError object.
        fields: Comma-separated list of fields to return. Available: affected_surfaces, description, error_type, id, severity, summary, total_count
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{product_feed_upload_error_id}", params=params)
    return json.dumps(result, indent=2)


STORE_CATALOG_SETTINGS_FIELDS = [
    "id",
    "page"
]


async def delete_store_catalog_settings(store_catalog_settings_id: str) -> str:
    """DELETE /#delete on StoreCatalogSettings.

    Args:
        store_catalog_settings_id: The ID of the StoreCatalogSettings object.
    """
    params = {}
    result = await get_client().delete(f"{store_catalog_settings_id}")
    return json.dumps(result, indent=2)


async def get_store_catalog_settings(store_catalog_settings_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on StoreCatalogSettings.

    Args:
        store_catalog_settings_id: The ID of the StoreCatalogSettings object.
        fields: Comma-separated list of fields to return. Available: id, page
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{store_catalog_settings_id}", params=params)
    return json.dumps(result, indent=2)


OFFLINE_PRODUCT_ITEM_FIELDS = [
    "applinks",
    "brand",
    "category",
    "category_specific_fields",
    "currency",
    "description",
    "id",
    "image_fetch_status",
    "image_url",
    "images",
    "name",
    "offline_product_item_id",
    "price",
    "sanitized_images",
    "url",
    "visibility"
]


async def get_offline_product_item_channels_to_integrity_status(offline_product_item_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on OfflineProductItem.

    Args:
        offline_product_item_id: The ID of the OfflineProductItem object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_product_item_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_offline_product_item_override_details(
    offline_product_item_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on OfflineProductItem.

    Args:
        offline_product_item_id: The ID of the OfflineProductItem object.
        fields: Comma-separated list of fields to return.
        keys: Optional.
        type_: Optional. Values: COUNTRY, LANGUAGE, LANGUAGE_AND_COUNTRY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if keys is not None:
        params["keys"] = keys
    if type_ is not None:
        params["type"] = type_
    result = await get_client().get(f"{offline_product_item_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_offline_product_item(offline_product_item_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on OfflineProductItem.

    Args:
        offline_product_item_id: The ID of the OfflineProductItem object.
        fields: Comma-separated list of fields to return. Available: applinks, brand, category, category_specific_fields, currency, description, id, image_fetch_status, image_url, images, name, offline_product_item_id, price, sanitized_images, url, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{offline_product_item_id}", params=params)
    return json.dumps(result, indent=2)

