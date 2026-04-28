"""Auto-generated Meta Marketing API tools — ad_monetization."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_MONETIZATION_PROPERTY_FIELDS = [
    "owner_business"
]


async def get_ad_monetization_property_adnetworkanalytics(
    ad_monetization_property_id: str,
    metrics: str,
    fields: Optional[str] = None,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    should_include_until: Optional[bool] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """GET /adnetworkanalytics on AdMonetizationProperty.

    Args:
        ad_monetization_property_id: The ID of the AdMonetizationProperty object.
        fields: Comma-separated list of fields to return.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        should_include_until: Optional.
        since: Optional.
        until: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if should_include_until is not None:
        params["should_include_until"] = should_include_until
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().get(f"{ad_monetization_property_id}/adnetworkanalytics", params=params)
    return json.dumps(result, indent=2)


async def create_ad_monetization_property_adnetworkanalytics(
    ad_monetization_property_id: str,
    metrics: str,
    aggregation_period: Optional[str] = None,
    breakdowns: Optional[str] = None,
    filters: Optional[str] = None,
    limit: Optional[int] = None,
    ordering_column: Optional[str] = None,
    ordering_type: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> str:
    """POST /adnetworkanalytics on AdMonetizationProperty.

    Args:
        ad_monetization_property_id: The ID of the AdMonetizationProperty object.
        aggregation_period: Optional. Values: DAY, TOTAL
        breakdowns: Optional. Values: AD_SERVER_CAMPAIGN_ID, AD_SPACE, AGE, APP, CLICKED_VIEW_TAG, COUNTRY, DEAL, DEAL_AD, DEAL_PAGE, DELIVERY_METHOD, DISPLAY_FORMAT, FAIL_REASON, GENDER, INSTANT_ARTICLE_ID, INSTANT_ARTICLE_PAGE_ID, IS_DEAL_BACKFILL, PLACEMENT, PLACEMENT_NAME, PLATFORM, PROPERTY, SDK_VERSION
        filters: Optional.
        limit: Optional.
        metrics: Required. Values: FB_AD_NETWORK_BIDDING_BID_RATE, FB_AD_NETWORK_BIDDING_REQUEST, FB_AD_NETWORK_BIDDING_RESPONSE, FB_AD_NETWORK_BIDDING_REVENUE, FB_AD_NETWORK_BIDDING_WIN_RATE, FB_AD_NETWORK_CLICK, FB_AD_NETWORK_CPM, FB_AD_NETWORK_CTR, FB_AD_NETWORK_FILLED_REQUEST, FB_AD_NETWORK_FILL_RATE, FB_AD_NETWORK_IMP, FB_AD_NETWORK_IMPRESSION_RATE, FB_AD_NETWORK_REQUEST, FB_AD_NETWORK_REVENUE, FB_AD_NETWORK_SHOW_RATE, FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE, FB_AD_NETWORK_VIDEO_MRC, FB_AD_NETWORK_VIDEO_MRC_RATE, FB_AD_NETWORK_VIDEO_VIEW, FB_AD_NETWORK_VIDEO_VIEW_RATE
        ordering_column: Optional. Values: METRIC, TIME, VALUE
        ordering_type: Optional. Values: ASCENDING, DESCENDING
        since: Optional.
        until: Optional.
    """
    params = {}
    if aggregation_period is not None:
        params["aggregation_period"] = aggregation_period
    if breakdowns is not None:
        params["breakdowns"] = breakdowns
    if filters is not None:
        params["filters"] = filters
    if limit is not None:
        params["limit"] = limit
    params["metrics"] = metrics
    if ordering_column is not None:
        params["ordering_column"] = ordering_column
    if ordering_type is not None:
        params["ordering_type"] = ordering_type
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    result = await get_client().post(f"{ad_monetization_property_id}/adnetworkanalytics", data=params)
    return json.dumps(result, indent=2)


async def get_ad_monetization_property_adnetworkanalytics_results(
    ad_monetization_property_id: str,
    fields: Optional[str] = None,
    query_ids: Optional[str] = None,
) -> str:
    """GET /adnetworkanalytics_results on AdMonetizationProperty.

    Args:
        ad_monetization_property_id: The ID of the AdMonetizationProperty object.
        fields: Comma-separated list of fields to return.
        query_ids: Optional.
    """
    params = {}
    params["fields"] = fields or "id,name"
    if query_ids is not None:
        params["query_ids"] = query_ids
    result = await get_client().get(f"{ad_monetization_property_id}/adnetworkanalytics_results", params=params)
    return json.dumps(result, indent=2)


async def get_ad_monetization_property(ad_monetization_property_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdMonetizationProperty.

    Args:
        ad_monetization_property_id: The ID of the AdMonetizationProperty object.
        fields: Comma-separated list of fields to return. Available: owner_business
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_monetization_property_id}", params=params)
    return json.dumps(result, indent=2)


ADS_CONVERSION_GOAL_FIELDS = [
    "ad_account_id",
    "conversion_event_value_source",
    "description",
    "goal_creation_method",
    "id",
    "name",
    "performance_goal",
    "update_status"
]


async def get_ads_conversion_goal_conversion_events(ads_conversion_goal_id: str, fields: Optional[str] = None) -> str:
    """GET /conversion_events on AdsConversionGoal.

    Args:
        ads_conversion_goal_id: The ID of the AdsConversionGoal object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_conversion_goal_id}/conversion_events", params=params)
    return json.dumps(result, indent=2)


async def get_ads_conversion_goal(ads_conversion_goal_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdsConversionGoal.

    Args:
        ads_conversion_goal_id: The ID of the AdsConversionGoal object.
        fields: Comma-separated list of fields to return. Available: ad_account_id, conversion_event_value_source, description, goal_creation_method, id, name, performance_goal, update_status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_conversion_goal_id}", params=params)
    return json.dumps(result, indent=2)


ADS_VALUE_ADJUSTMENT_RULE_COLLECTION_FIELDS = [
    "id",
    "is_default_setting",
    "last_attach_time",
    "name",
    "product_type",
    "status"
]


async def create_ads_value_adjustment_rule_collection_delete_rule_set(ads_value_adjustment_rule_collection_id: str) -> str:
    """POST /delete_rule_set on AdsValueAdjustmentRuleCollection.

    Args:
        ads_value_adjustment_rule_collection_id: The ID of the AdsValueAdjustmentRuleCollection object.
    """
    params = {}
    result = await get_client().post(f"{ads_value_adjustment_rule_collection_id}/delete_rule_set", data=params)
    return json.dumps(result, indent=2)


async def get_ads_value_adjustment_rule_collection_rules(ads_value_adjustment_rule_collection_id: str, fields: Optional[str] = None) -> str:
    """GET /rules on AdsValueAdjustmentRuleCollection.

    Args:
        ads_value_adjustment_rule_collection_id: The ID of the AdsValueAdjustmentRuleCollection object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_value_adjustment_rule_collection_id}/rules", params=params)
    return json.dumps(result, indent=2)


async def get_ads_value_adjustment_rule_collection(ads_value_adjustment_rule_collection_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdsValueAdjustmentRuleCollection.

    Args:
        ads_value_adjustment_rule_collection_id: The ID of the AdsValueAdjustmentRuleCollection object.
        fields: Comma-separated list of fields to return. Available: id, is_default_setting, last_attach_time, name, product_type, status
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ads_value_adjustment_rule_collection_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ads_value_adjustment_rule_collection(
    ads_value_adjustment_rule_collection_id: str,
    name: str,
    rules: str,
    is_default_setting: Optional[bool] = None,
) -> str:
    """POST /#update on AdsValueAdjustmentRuleCollection.

    Args:
        ads_value_adjustment_rule_collection_id: The ID of the AdsValueAdjustmentRuleCollection object.
        is_default_setting: Optional.
        name: Required.
        rules: Required.
    """
    params = {}
    if is_default_setting is not None:
        params["is_default_setting"] = is_default_setting
    params["name"] = name
    params["rules"] = rules
    result = await get_client().post(f"{ads_value_adjustment_rule_collection_id}", data=params)
    return json.dumps(result, indent=2)

