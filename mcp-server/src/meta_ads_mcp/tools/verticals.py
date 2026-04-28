"""Auto-generated Meta Marketing API tools — verticals."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


HOTEL_FIELDS = [
    "address",
    "applinks",
    "brand",
    "category",
    "category_specific_fields",
    "currency",
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
    "guest_ratings",
    "hotel_id",
    "id",
    "image_fetch_status",
    "images",
    "lowest_base_price",
    "loyalty_program",
    "margin_level",
    "name",
    "phone",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sale_price",
    "sanitized_images",
    "star_rating",
    "tags",
    "unit_price",
    "url",
    "visibility"
]


async def get_hotel_channels_to_integrity_status(hotel_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_hotel_hotel_rooms(hotel_id: str, fields: Optional[str] = None) -> str:
    """GET /hotel_rooms on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_id}/hotel_rooms", params=params)
    return json.dumps(result, indent=2)


async def get_hotel_override_details(
    hotel_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
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
    result = await get_client().get(f"{hotel_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_hotel_videos_metadata(hotel_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def delete_hotel(hotel_id: str) -> str:
    """DELETE /#delete on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
    """
    params = {}
    result = await get_client().delete(f"{hotel_id}")
    return json.dumps(result, indent=2)


async def get_hotel(hotel_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
        fields: Comma-separated list of fields to return. Available: address, applinks, brand, category, category_specific_fields, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, guest_ratings, hotel_id, id, image_fetch_status, images, lowest_base_price, loyalty_program, margin_level, name, phone, product_priority_0, product_priority_1, product_priority_2, product_priority_3, product_priority_4, sale_price, sanitized_images, star_rating, tags, unit_price, url, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_id}", params=params)
    return json.dumps(result, indent=2)


async def update_hotel(
    hotel_id: str,
    address: Optional[str] = None,
    applinks: Optional[str] = None,
    base_price: Optional[int] = None,
    brand: Optional[str] = None,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    guest_ratings: Optional[str] = None,
    images: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    star_rating: Optional[float] = None,
    url: Optional[str] = None,
) -> str:
    """POST /#update on Hotel.

    Args:
        hotel_id: The ID of the Hotel object.
        address: Optional.
        applinks: Optional.
        base_price: Optional.
        brand: Optional.
        currency: Optional.
        description: Optional.
        guest_ratings: Optional.
        images: Optional.
        name: Optional.
        phone: Optional.
        star_rating: Optional.
        url: Optional.
    """
    params = {}
    if address is not None:
        params["address"] = address
    if applinks is not None:
        params["applinks"] = applinks
    if base_price is not None:
        params["base_price"] = base_price
    if brand is not None:
        params["brand"] = brand
    if currency is not None:
        params["currency"] = currency
    if description is not None:
        params["description"] = description
    if guest_ratings is not None:
        params["guest_ratings"] = guest_ratings
    if images is not None:
        params["images"] = images
    if name is not None:
        params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if star_rating is not None:
        params["star_rating"] = star_rating
    if url is not None:
        params["url"] = url
    result = await get_client().post(f"{hotel_id}", data=params)
    return json.dumps(result, indent=2)


HOTEL_ROOM_FIELDS = [
    "applinks",
    "base_price",
    "currency",
    "description",
    "id",
    "images",
    "margin_level",
    "name",
    "room_id",
    "sale_price",
    "url"
]


async def get_hotel_room_pricing_variables(hotel_room_id: str, fields: Optional[str] = None) -> str:
    """GET /pricing_variables on HotelRoom.

    Args:
        hotel_room_id: The ID of the HotelRoom object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_room_id}/pricing_variables", params=params)
    return json.dumps(result, indent=2)


async def get_hotel_room(hotel_room_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on HotelRoom.

    Args:
        hotel_room_id: The ID of the HotelRoom object.
        fields: Comma-separated list of fields to return. Available: applinks, base_price, currency, description, id, images, margin_level, name, room_id, sale_price, url
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{hotel_room_id}", params=params)
    return json.dumps(result, indent=2)


FLIGHT_FIELDS = [
    "applinks",
    "category_specific_fields",
    "currency",
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
    "destination_airport",
    "destination_city",
    "flight_id",
    "id",
    "image_fetch_status",
    "images",
    "oneway_currency",
    "oneway_price",
    "origin_airport",
    "origin_city",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sanitized_images",
    "tags",
    "unit_price",
    "url",
    "visibility"
]


async def get_flight_channels_to_integrity_status(flight_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on Flight.

    Args:
        flight_id: The ID of the Flight object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{flight_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_flight_override_details(
    flight_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on Flight.

    Args:
        flight_id: The ID of the Flight object.
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
    result = await get_client().get(f"{flight_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_flight_videos_metadata(flight_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on Flight.

    Args:
        flight_id: The ID of the Flight object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{flight_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def get_flight(flight_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Flight.

    Args:
        flight_id: The ID of the Flight object.
        fields: Comma-separated list of fields to return. Available: applinks, category_specific_fields, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, destination_airport, destination_city, flight_id, id, image_fetch_status, images, oneway_currency, oneway_price, origin_airport, origin_city, price, product_priority_0, product_priority_1, product_priority_2, product_priority_3, product_priority_4, sanitized_images, tags, unit_price, url, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{flight_id}", params=params)
    return json.dumps(result, indent=2)


async def update_flight(
    flight_id: str,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    destination_airport: Optional[str] = None,
    destination_city: Optional[str] = None,
    images: Optional[str] = None,
    origin_airport: Optional[str] = None,
    origin_city: Optional[str] = None,
    price: Optional[int] = None,
    url: Optional[str] = None,
) -> str:
    """POST /#update on Flight.

    Args:
        flight_id: The ID of the Flight object.
        currency: Optional.
        description: Optional.
        destination_airport: Optional.
        destination_city: Optional.
        images: Optional.
        origin_airport: Optional.
        origin_city: Optional.
        price: Optional.
        url: Optional.
    """
    params = {}
    if currency is not None:
        params["currency"] = currency
    if description is not None:
        params["description"] = description
    if destination_airport is not None:
        params["destination_airport"] = destination_airport
    if destination_city is not None:
        params["destination_city"] = destination_city
    if images is not None:
        params["images"] = images
    if origin_airport is not None:
        params["origin_airport"] = origin_airport
    if origin_city is not None:
        params["origin_city"] = origin_city
    if price is not None:
        params["price"] = price
    if url is not None:
        params["url"] = url
    result = await get_client().post(f"{flight_id}", data=params)
    return json.dumps(result, indent=2)


DESTINATION_FIELDS = [
    "address",
    "applinks",
    "category_specific_fields",
    "currency",
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
    "destination_id",
    "id",
    "image_fetch_status",
    "images",
    "name",
    "price",
    "price_change",
    "sanitized_images",
    "tags",
    "types",
    "unit_price",
    "url",
    "visibility"
]


async def get_destination_channels_to_integrity_status(destination_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on Destination.

    Args:
        destination_id: The ID of the Destination object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{destination_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_destination_override_details(
    destination_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on Destination.

    Args:
        destination_id: The ID of the Destination object.
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
    result = await get_client().get(f"{destination_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_destination_videos_metadata(destination_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on Destination.

    Args:
        destination_id: The ID of the Destination object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{destination_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def get_destination(destination_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Destination.

    Args:
        destination_id: The ID of the Destination object.
        fields: Comma-separated list of fields to return. Available: address, applinks, category_specific_fields, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, destination_id, id, image_fetch_status, images, name, price, price_change, sanitized_images, tags, types, unit_price, url, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{destination_id}", params=params)
    return json.dumps(result, indent=2)


VEHICLE_FIELDS = [
    "address",
    "applinks",
    "availability",
    "availability_circle_radius",
    "availability_circle_radius_unit",
    "body_style",
    "category_specific_fields",
    "condition",
    "currency",
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
    "date_first_on_lot",
    "dealer_communication_channel",
    "dealer_email",
    "dealer_id",
    "dealer_name",
    "dealer_phone",
    "dealer_privacy_policy_url",
    "description",
    "drivetrain",
    "exterior_color",
    "fb_page_id",
    "features",
    "fuel_type",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "legal_disclosure_impressum_url",
    "make",
    "mileage",
    "model",
    "previous_currency",
    "previous_price",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sale_currency",
    "sale_price",
    "sanitized_images",
    "state_of_vehicle",
    "tags",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "vehicle_id",
    "vehicle_registration_plate",
    "vehicle_specifications",
    "vehicle_type",
    "vin",
    "visibility",
    "year"
]


async def get_vehicle_channels_to_integrity_status(vehicle_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle_override_details(
    vehicle_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle object.
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
    result = await get_client().get(f"{vehicle_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle_videos_metadata(vehicle_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle(vehicle_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle object.
        fields: Comma-separated list of fields to return. Available: address, applinks, availability, availability_circle_radius, availability_circle_radius_unit, body_style, category_specific_fields, condition, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, date_first_on_lot, dealer_communication_channel, dealer_email, dealer_id, dealer_name, dealer_phone, dealer_privacy_policy_url, description, drivetrain, exterior_color, fb_page_id, features, fuel_type, id, image_fetch_status, images, interior_color, legal_disclosure_impressum_url, make, mileage, model, previous_currency, previous_price, price, product_priority_0, product_priority_1, product_priority_2, product_priority_3, product_priority_4, sale_currency, sale_price, sanitized_images, state_of_vehicle, tags, title, transmission, trim, unit_price, url, vehicle_id, vehicle_registration_plate, vehicle_specifications, vehicle_type, vin, visibility, year
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_id}", params=params)
    return json.dumps(result, indent=2)


async def update_vehicle(
    vehicle_id: str,
    address: Optional[str] = None,
    applinks: Optional[str] = None,
    availability: Optional[str] = None,
    body_style: Optional[str] = None,
    condition: Optional[str] = None,
    currency: Optional[str] = None,
    date_first_on_lot: Optional[str] = None,
    dealer_id: Optional[str] = None,
    dealer_name: Optional[str] = None,
    dealer_phone: Optional[str] = None,
    description: Optional[str] = None,
    drivetrain: Optional[str] = None,
    exterior_color: Optional[str] = None,
    fb_page_id: Optional[str] = None,
    fuel_type: Optional[str] = None,
    images: Optional[str] = None,
    interior_color: Optional[str] = None,
    make: Optional[str] = None,
    mileage: Optional[str] = None,
    model: Optional[str] = None,
    price: Optional[int] = None,
    state_of_vehicle: Optional[str] = None,
    title: Optional[str] = None,
    transmission: Optional[str] = None,
    trim: Optional[str] = None,
    url: Optional[str] = None,
    vehicle_type: Optional[str] = None,
    vin: Optional[str] = None,
    year: Optional[int] = None,
) -> str:
    """POST /#update on Vehicle.

    Args:
        vehicle_id: The ID of the Vehicle object.
        address: Optional.
        applinks: Optional.
        availability: Optional.
        body_style: Optional.
        condition: Optional.
        currency: Optional.
        date_first_on_lot: Optional.
        dealer_id: Optional.
        dealer_name: Optional.
        dealer_phone: Optional.
        description: Optional.
        drivetrain: Optional.
        exterior_color: Optional.
        fb_page_id: Optional.
        fuel_type: Optional.
        images: Optional.
        interior_color: Optional.
        make: Optional.
        mileage: Optional.
        model: Optional.
        price: Optional.
        state_of_vehicle: Optional.
        title: Optional.
        transmission: Optional.
        trim: Optional.
        url: Optional.
        vehicle_type: Optional.
        vin: Optional.
        year: Optional.
    """
    params = {}
    if address is not None:
        params["address"] = address
    if applinks is not None:
        params["applinks"] = applinks
    if availability is not None:
        params["availability"] = availability
    if body_style is not None:
        params["body_style"] = body_style
    if condition is not None:
        params["condition"] = condition
    if currency is not None:
        params["currency"] = currency
    if date_first_on_lot is not None:
        params["date_first_on_lot"] = date_first_on_lot
    if dealer_id is not None:
        params["dealer_id"] = dealer_id
    if dealer_name is not None:
        params["dealer_name"] = dealer_name
    if dealer_phone is not None:
        params["dealer_phone"] = dealer_phone
    if description is not None:
        params["description"] = description
    if drivetrain is not None:
        params["drivetrain"] = drivetrain
    if exterior_color is not None:
        params["exterior_color"] = exterior_color
    if fb_page_id is not None:
        params["fb_page_id"] = fb_page_id
    if fuel_type is not None:
        params["fuel_type"] = fuel_type
    if images is not None:
        params["images"] = images
    if interior_color is not None:
        params["interior_color"] = interior_color
    if make is not None:
        params["make"] = make
    if mileage is not None:
        params["mileage"] = mileage
    if model is not None:
        params["model"] = model
    if price is not None:
        params["price"] = price
    if state_of_vehicle is not None:
        params["state_of_vehicle"] = state_of_vehicle
    if title is not None:
        params["title"] = title
    if transmission is not None:
        params["transmission"] = transmission
    if trim is not None:
        params["trim"] = trim
    if url is not None:
        params["url"] = url
    if vehicle_type is not None:
        params["vehicle_type"] = vehicle_type
    if vin is not None:
        params["vin"] = vin
    if year is not None:
        params["year"] = year
    result = await get_client().post(f"{vehicle_id}", data=params)
    return json.dumps(result, indent=2)


VEHICLE_OFFER_FIELDS = [
    "amount_currency",
    "amount_percentage",
    "amount_price",
    "amount_qualifier",
    "applinks",
    "availability",
    "body_style",
    "cashback_currency",
    "cashback_price",
    "category_specific_fields",
    "currency",
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
    "dma_codes",
    "downpayment_currency",
    "downpayment_price",
    "downpayment_qualifier",
    "drivetrain",
    "end_date",
    "end_time",
    "exterior_color",
    "fuel_type",
    "generation",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "interior_upholstery",
    "make",
    "model",
    "offer_description",
    "offer_disclaimer",
    "offer_type",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sanitized_images",
    "start_date",
    "start_time",
    "tags",
    "term_length",
    "term_qualifier",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "vehicle_offer_id",
    "visibility",
    "year"
]


async def get_vehicle_offer_channels_to_integrity_status(vehicle_offer_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on VehicleOffer.

    Args:
        vehicle_offer_id: The ID of the VehicleOffer object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_offer_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle_offer_override_details(
    vehicle_offer_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on VehicleOffer.

    Args:
        vehicle_offer_id: The ID of the VehicleOffer object.
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
    result = await get_client().get(f"{vehicle_offer_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle_offer_videos_metadata(vehicle_offer_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on VehicleOffer.

    Args:
        vehicle_offer_id: The ID of the VehicleOffer object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_offer_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def get_vehicle_offer(vehicle_offer_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on VehicleOffer.

    Args:
        vehicle_offer_id: The ID of the VehicleOffer object.
        fields: Comma-separated list of fields to return. Available: amount_currency, amount_percentage, amount_price, amount_qualifier, applinks, availability, body_style, cashback_currency, cashback_price, category_specific_fields, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, dma_codes, downpayment_currency, downpayment_price, downpayment_qualifier, drivetrain, end_date, end_time, exterior_color, fuel_type, generation, id, image_fetch_status, images, interior_color, interior_upholstery, make, model, offer_description, offer_disclaimer, offer_type, price, product_priority_0, product_priority_1, product_priority_2, product_priority_3, product_priority_4, sanitized_images, start_date, start_time, tags, term_length, term_qualifier, title, transmission, trim, unit_price, url, vehicle_offer_id, visibility, year
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{vehicle_offer_id}", params=params)
    return json.dumps(result, indent=2)


AUTOMOTIVE_MODEL_FIELDS = [
    "applinks",
    "automotive_model_id",
    "availability",
    "body_style",
    "category_specific_fields",
    "currency",
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
    "drivetrain",
    "exterior_color",
    "finance_description",
    "finance_type",
    "fuel_type",
    "generation",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "interior_upholstery",
    "make",
    "model",
    "price",
    "sanitized_images",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "visibility",
    "year"
]


async def get_automotive_model_channels_to_integrity_status(automotive_model_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on AutomotiveModel.

    Args:
        automotive_model_id: The ID of the AutomotiveModel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{automotive_model_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_automotive_model_override_details(
    automotive_model_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on AutomotiveModel.

    Args:
        automotive_model_id: The ID of the AutomotiveModel object.
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
    result = await get_client().get(f"{automotive_model_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_automotive_model_videos_metadata(automotive_model_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on AutomotiveModel.

    Args:
        automotive_model_id: The ID of the AutomotiveModel object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{automotive_model_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def get_automotive_model(automotive_model_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AutomotiveModel.

    Args:
        automotive_model_id: The ID of the AutomotiveModel object.
        fields: Comma-separated list of fields to return. Available: applinks, automotive_model_id, availability, body_style, category_specific_fields, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, drivetrain, exterior_color, finance_description, finance_type, fuel_type, generation, id, image_fetch_status, images, interior_color, interior_upholstery, make, model, price, sanitized_images, title, transmission, trim, unit_price, url, visibility, year
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{automotive_model_id}", params=params)
    return json.dumps(result, indent=2)


HOME_LISTING_FIELDS = [
    "ac_type",
    "additional_fees_description",
    "address",
    "agent_company",
    "agent_email",
    "agent_fb_page_id",
    "agent_name",
    "agent_phone",
    "applinks",
    "area_size",
    "area_unit",
    "availability",
    "category_specific_fields",
    "co_2_emission_rating_eu",
    "currency",
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
    "days_on_market",
    "description",
    "energy_rating_eu",
    "furnish_type",
    "group_id",
    "heating_type",
    "home_listing_id",
    "id",
    "image_fetch_status",
    "images",
    "laundry_type",
    "listing_type",
    "max_currency",
    "max_price",
    "min_currency",
    "min_price",
    "name",
    "num_baths",
    "num_beds",
    "num_rooms",
    "num_units",
    "parking_type",
    "partner_verification",
    "pet_policy",
    "price",
    "property_type",
    "sanitized_images",
    "securitydeposit_currency",
    "securitydeposit_price",
    "tags",
    "unit_price",
    "url",
    "visibility",
    "year_built"
]


async def get_home_listing_channels_to_integrity_status(home_listing_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{home_listing_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_home_listing_override_details(
    home_listing_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
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
    result = await get_client().get(f"{home_listing_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_home_listing_videos_metadata(home_listing_id: str, fields: Optional[str] = None) -> str:
    """GET /videos_metadata on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{home_listing_id}/videos_metadata", params=params)
    return json.dumps(result, indent=2)


async def delete_home_listing(home_listing_id: str) -> str:
    """DELETE /#delete on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
    """
    params = {}
    result = await get_client().delete(f"{home_listing_id}")
    return json.dumps(result, indent=2)


async def get_home_listing(home_listing_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
        fields: Comma-separated list of fields to return. Available: ac_type, additional_fees_description, address, agent_company, agent_email, agent_fb_page_id, agent_name, agent_phone, applinks, area_size, area_unit, availability, category_specific_fields, co_2_emission_rating_eu, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, days_on_market, description, energy_rating_eu, furnish_type, group_id, heating_type, home_listing_id, id, image_fetch_status, images, laundry_type, listing_type, max_currency, max_price, min_currency, min_price, name, num_baths, num_beds, num_rooms, num_units, parking_type, partner_verification, pet_policy, price, property_type, sanitized_images, securitydeposit_currency, securitydeposit_price, tags, unit_price, url, visibility, year_built
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{home_listing_id}", params=params)
    return json.dumps(result, indent=2)


async def update_home_listing(
    home_listing_id: str,
    address: Optional[str] = None,
    availability: Optional[str] = None,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    images: Optional[str] = None,
    listing_type: Optional[str] = None,
    name: Optional[str] = None,
    num_baths: Optional[float] = None,
    num_beds: Optional[float] = None,
    num_units: Optional[float] = None,
    price: Optional[float] = None,
    property_type: Optional[str] = None,
    url: Optional[str] = None,
    year_built: Optional[int] = None,
) -> str:
    """POST /#update on HomeListing.

    Args:
        home_listing_id: The ID of the HomeListing object.
        address: Optional.
        availability: Optional.
        currency: Optional.
        description: Optional.
        images: Optional.
        listing_type: Optional.
        name: Optional.
        num_baths: Optional.
        num_beds: Optional.
        num_units: Optional.
        price: Optional.
        property_type: Optional.
        url: Optional.
        year_built: Optional.
    """
    params = {}
    if address is not None:
        params["address"] = address
    if availability is not None:
        params["availability"] = availability
    if currency is not None:
        params["currency"] = currency
    if description is not None:
        params["description"] = description
    if images is not None:
        params["images"] = images
    if listing_type is not None:
        params["listing_type"] = listing_type
    if name is not None:
        params["name"] = name
    if num_baths is not None:
        params["num_baths"] = num_baths
    if num_beds is not None:
        params["num_beds"] = num_beds
    if num_units is not None:
        params["num_units"] = num_units
    if price is not None:
        params["price"] = price
    if property_type is not None:
        params["property_type"] = property_type
    if url is not None:
        params["url"] = url
    if year_built is not None:
        params["year_built"] = year_built
    result = await get_client().post(f"{home_listing_id}", data=params)
    return json.dumps(result, indent=2)


HIGH_DEMAND_PERIOD_FIELDS = [
    "ad_object_id",
    "budget_value",
    "budget_value_type",
    "id",
    "recurrence_type",
    "time_end",
    "time_start",
    "weekly_schedule"
]


async def delete_high_demand_period(high_demand_period_id: str) -> str:
    """DELETE /#delete on HighDemandPeriod.

    Args:
        high_demand_period_id: The ID of the HighDemandPeriod object.
    """
    params = {}
    result = await get_client().delete(f"{high_demand_period_id}")
    return json.dumps(result, indent=2)


async def get_high_demand_period(high_demand_period_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on HighDemandPeriod.

    Args:
        high_demand_period_id: The ID of the HighDemandPeriod object.
        fields: Comma-separated list of fields to return. Available: ad_object_id, budget_value, budget_value_type, id, recurrence_type, time_end, time_start, weekly_schedule
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{high_demand_period_id}", params=params)
    return json.dumps(result, indent=2)


async def update_high_demand_period(
    high_demand_period_id: str,
    budget_value: Optional[int] = None,
    budget_value_type: Optional[str] = None,
    time_end: Optional[int] = None,
    time_start: Optional[int] = None,
) -> str:
    """POST /#update on HighDemandPeriod.

    Args:
        high_demand_period_id: The ID of the HighDemandPeriod object.
        budget_value: Optional.
        budget_value_type: Optional.
        time_end: Optional.
        time_start: Optional.
    """
    params = {}
    if budget_value is not None:
        params["budget_value"] = budget_value
    if budget_value_type is not None:
        params["budget_value_type"] = budget_value_type
    if time_end is not None:
        params["time_end"] = time_end
    if time_start is not None:
        params["time_start"] = time_start
    result = await get_client().post(f"{high_demand_period_id}", data=params)
    return json.dumps(result, indent=2)


TRANSACTABLE_ITEM_FIELDS = [
    "action_title",
    "applinks",
    "category_specific_fields",
    "currency",
    "description",
    "duration_time",
    "duration_type",
    "id",
    "image_fetch_status",
    "images",
    "order_index",
    "price",
    "price_type",
    "sanitized_images",
    "session_type",
    "time_padding_after_end",
    "title",
    "transactable_item_id",
    "url",
    "visibility"
]


async def get_transactable_item_channels_to_integrity_status(transactable_item_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on TransactableItem.

    Args:
        transactable_item_id: The ID of the TransactableItem object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{transactable_item_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_transactable_item_override_details(
    transactable_item_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on TransactableItem.

    Args:
        transactable_item_id: The ID of the TransactableItem object.
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
    result = await get_client().get(f"{transactable_item_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_transactable_item(transactable_item_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on TransactableItem.

    Args:
        transactable_item_id: The ID of the TransactableItem object.
        fields: Comma-separated list of fields to return. Available: action_title, applinks, category_specific_fields, currency, description, duration_time, duration_type, id, image_fetch_status, images, order_index, price, price_type, sanitized_images, session_type, time_padding_after_end, title, transactable_item_id, url, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{transactable_item_id}", params=params)
    return json.dumps(result, indent=2)


LOCAL_SERVICE_BUSINESS_FIELDS = [
    "address",
    "applinks",
    "availability",
    "brand",
    "category",
    "category_specific_fields",
    "condition",
    "cuisine_type",
    "currency",
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
    "expiration_date",
    "gtin",
    "id",
    "image_fetch_status",
    "images",
    "local_info",
    "local_service_business_id",
    "main_local_info",
    "phone",
    "price",
    "price_range",
    "retailer_category",
    "sanitized_images",
    "size",
    "tags",
    "title",
    "unit_price",
    "url",
    "vendor_id",
    "visibility"
]


async def get_local_service_business_channels_to_integrity_status(local_service_business_id: str, fields: Optional[str] = None) -> str:
    """GET /channels_to_integrity_status on LocalServiceBusiness.

    Args:
        local_service_business_id: The ID of the LocalServiceBusiness object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{local_service_business_id}/channels_to_integrity_status", params=params)
    return json.dumps(result, indent=2)


async def get_local_service_business_override_details(
    local_service_business_id: str,
    fields: Optional[str] = None,
    keys: Optional[str] = None,
    type_: Optional[str] = None,
) -> str:
    """GET /override_details on LocalServiceBusiness.

    Args:
        local_service_business_id: The ID of the LocalServiceBusiness object.
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
    result = await get_client().get(f"{local_service_business_id}/override_details", params=params)
    return json.dumps(result, indent=2)


async def get_local_service_business(local_service_business_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on LocalServiceBusiness.

    Args:
        local_service_business_id: The ID of the LocalServiceBusiness object.
        fields: Comma-separated list of fields to return. Available: address, applinks, availability, brand, category, category_specific_fields, condition, cuisine_type, currency, custom_label_0, custom_label_1, custom_label_2, custom_label_3, custom_label_4, custom_number_0, custom_number_1, custom_number_2, custom_number_3, custom_number_4, description, expiration_date, gtin, id, image_fetch_status, images, local_info, local_service_business_id, main_local_info, phone, price, price_range, retailer_category, sanitized_images, size, tags, title, unit_price, url, vendor_id, visibility
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{local_service_business_id}", params=params)
    return json.dumps(result, indent=2)

