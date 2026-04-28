"""Auto-generated Meta Marketing API tools — ad_async."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


AD_ASYNC_REQUEST_FIELDS = [
    "async_request_set",
    "created_time",
    "id",
    "input",
    "result",
    "scope_object_id",
    "status",
    "type",
    "updated_time"
]


async def delete_ad_async_request(ad_async_request_id: str) -> str:
    """DELETE /#delete on AdAsyncRequest.

    Args:
        ad_async_request_id: The ID of the AdAsyncRequest object.
    """
    params = {}
    result = await get_client().delete(f"{ad_async_request_id}")
    return json.dumps(result, indent=2)


async def get_ad_async_request(ad_async_request_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdAsyncRequest.

    Args:
        ad_async_request_id: The ID of the AdAsyncRequest object.
        fields: Comma-separated list of fields to return. Available: async_request_set, created_time, id, input, result, scope_object_id, status, type, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_async_request_id}", params=params)
    return json.dumps(result, indent=2)


AD_ASYNC_REQUEST_SET_FIELDS = [
    "canceled_count",
    "created_time",
    "error_count",
    "id",
    "in_progress_count",
    "initial_count",
    "is_completed",
    "name",
    "notification_mode",
    "notification_result",
    "notification_status",
    "notification_uri",
    "owner_id",
    "success_count",
    "total_count",
    "updated_time"
]


async def get_ad_async_request_set_requests(
    ad_async_request_set_id: str,
    fields: Optional[str] = None,
    statuses: Optional[str] = None,
) -> str:
    """GET /requests on AdAsyncRequestSet.

    Args:
        ad_async_request_set_id: The ID of the AdAsyncRequestSet object.
        fields: Comma-separated list of fields to return.
        statuses: Optional. Values: CANCELED, CANCELED_DEPENDENCY, ERROR, ERROR_CONFLICTS, ERROR_DEPENDENCY, INITIAL, IN_PROGRESS, PENDING_DEPENDENCY, PROCESS_BY_AD_ASYNC_ENGINE, PROCESS_BY_EVENT_PROCESSOR, SUCCESS, USER_CANCELED, USER_CANCELED_DEPENDENCY
    """
    params = {}
    params["fields"] = fields or "id,name"
    if statuses is not None:
        params["statuses"] = statuses
    result = await get_client().get(f"{ad_async_request_set_id}/requests", params=params)
    return json.dumps(result, indent=2)


async def delete_ad_async_request_set(ad_async_request_set_id: str) -> str:
    """DELETE /#delete on AdAsyncRequestSet.

    Args:
        ad_async_request_set_id: The ID of the AdAsyncRequestSet object.
    """
    params = {}
    result = await get_client().delete(f"{ad_async_request_set_id}")
    return json.dumps(result, indent=2)


async def get_ad_async_request_set(ad_async_request_set_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdAsyncRequestSet.

    Args:
        ad_async_request_set_id: The ID of the AdAsyncRequestSet object.
        fields: Comma-separated list of fields to return. Available: canceled_count, created_time, error_count, id, in_progress_count, initial_count, is_completed, name, notification_mode, notification_result, notification_status, notification_uri, owner_id, success_count, total_count, updated_time
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_async_request_set_id}", params=params)
    return json.dumps(result, indent=2)


async def update_ad_async_request_set(
    ad_async_request_set_id: str,
    name: Optional[str] = None,
    notification_mode: Optional[str] = None,
    notification_uri: Optional[str] = None,
) -> str:
    """POST /#update on AdAsyncRequestSet.

    Args:
        ad_async_request_set_id: The ID of the AdAsyncRequestSet object.
        name: Optional.
        notification_mode: Optional.
        notification_uri: Optional.
    """
    params = {}
    if name is not None:
        params["name"] = name
    if notification_mode is not None:
        params["notification_mode"] = notification_mode
    if notification_uri is not None:
        params["notification_uri"] = notification_uri
    result = await get_client().post(f"{ad_async_request_set_id}", data=params)
    return json.dumps(result, indent=2)


AD_REPORT_RUN_FIELDS = [
    "account_id",
    "async_percent_completion",
    "async_report_url",
    "async_status",
    "date_start",
    "date_stop",
    "emails",
    "error_code",
    "friendly_name",
    "id",
    "is_async_export",
    "is_bookmarked",
    "is_running",
    "schedule_id",
    "time_completed",
    "time_ref"
]


async def get_ad_report_run_insights(ad_report_run_id: str, fields: Optional[str] = None) -> str:
    """GET /insights on AdReportRun.

    Args:
        ad_report_run_id: The ID of the AdReportRun object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_report_run_id}/insights", params=params)
    return json.dumps(result, indent=2)


async def get_ad_report_run(ad_report_run_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on AdReportRun.

    Args:
        ad_report_run_id: The ID of the AdReportRun object.
        fields: Comma-separated list of fields to return. Available: account_id, async_percent_completion, async_report_url, async_status, date_start, date_stop, emails, error_code, friendly_name, id, is_async_export, is_bookmarked, is_running, schedule_id, time_completed, time_ref
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{ad_report_run_id}", params=params)
    return json.dumps(result, indent=2)

