"""Auto-generated Meta Marketing API tools — misc."""

import json
from typing import Optional

from meta_ads_mcp.client import get_client


URL_FIELDS = [
    "engagement",
    "id",
    "og_object",
    "ownership_permissions",
    "scopes"
]


async def get_url(url_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on URL.

    Args:
        url_id: The ID of the URL object.
        fields: Comma-separated list of fields to return. Available: engagement, id, og_object, ownership_permissions, scopes
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{url_id}", params=params)
    return json.dumps(result, indent=2)


async def update_url(
    url_id: str,
    blacklist: Optional[bool] = None,
    denylist: Optional[bool] = None,
    hmac: Optional[str] = None,
    locale: Optional[str] = None,
    scopes: Optional[str] = None,
    ts: Optional[str] = None,
) -> str:
    """POST /#update on URL.

    Args:
        url_id: The ID of the URL object.
        blacklist: Optional.
        denylist: Optional.
        hmac: Optional.
        locale: Optional.
        scopes: Optional.
        ts: Optional.
    """
    params = {}
    if blacklist is not None:
        params["blacklist"] = blacklist
    if denylist is not None:
        params["denylist"] = denylist
    if hmac is not None:
        params["hmac"] = hmac
    if locale is not None:
        params["locale"] = locale
    if scopes is not None:
        params["scopes"] = scopes
    if ts is not None:
        params["ts"] = ts
    result = await get_client().post(f"{url_id}", data=params)
    return json.dumps(result, indent=2)


PRIVATE_LIFT_STUDY_INSTANCE_FIELDS = [
    "breakdown_key",
    "created_time",
    "feature_list",
    "id",
    "issuer_certificate",
    "latest_status_update_time",
    "run_id",
    "server_hostnames",
    "server_ips",
    "status",
    "tier"
]


async def get_private_lift_study_instance(private_lift_study_instance_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on PrivateLiftStudyInstance.

    Args:
        private_lift_study_instance_id: The ID of the PrivateLiftStudyInstance object.
        fields: Comma-separated list of fields to return. Available: breakdown_key, created_time, feature_list, id, issuer_certificate, latest_status_update_time, run_id, server_hostnames, server_ips, status, tier
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{private_lift_study_instance_id}", params=params)
    return json.dumps(result, indent=2)


async def update_private_lift_study_instance(
    private_lift_study_instance_id: str,
    operation: Optional[str] = None,
    run_id: Optional[str] = None,
) -> str:
    """POST /#update on PrivateLiftStudyInstance.

    Args:
        private_lift_study_instance_id: The ID of the PrivateLiftStudyInstance object.
        operation: Optional.
        run_id: Optional.
    """
    params = {}
    if operation is not None:
        params["operation"] = operation
    if run_id is not None:
        params["run_id"] = run_id
    result = await get_client().post(f"{private_lift_study_instance_id}", data=params)
    return json.dumps(result, indent=2)


BIZ_INBOX_OFFSITE_EMAIL_ACCOUNT_FIELDS = [
    "email_address",
    "id"
]


async def get_biz_inbox_offsite_email_account_assigned_users(biz_inbox_offsite_email_account_id: str, fields: Optional[str] = None) -> str:
    """GET /assigned_users on BizInboxOffsiteEmailAccount.

    Args:
        biz_inbox_offsite_email_account_id: The ID of the BizInboxOffsiteEmailAccount object.
        fields: Comma-separated list of fields to return.
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{biz_inbox_offsite_email_account_id}/assigned_users", params=params)
    return json.dumps(result, indent=2)


async def get_biz_inbox_offsite_email_account(biz_inbox_offsite_email_account_id: str, fields: Optional[str] = None) -> str:
    """GET /#get on BizInboxOffsiteEmailAccount.

    Args:
        biz_inbox_offsite_email_account_id: The ID of the BizInboxOffsiteEmailAccount object.
        fields: Comma-separated list of fields to return. Available: email_address, id
    """
    params = {}
    params["fields"] = fields or "id,name"
    result = await get_client().get(f"{biz_inbox_offsite_email_account_id}", params=params)
    return json.dumps(result, indent=2)

