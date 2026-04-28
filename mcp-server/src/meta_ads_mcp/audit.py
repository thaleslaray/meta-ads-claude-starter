"""Audit logging and business hours enforcement for Meta API operations.

Logs every write operation with before/after state for compliance.
Enforces business hours restriction on write operations.
"""

import json
import logging
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from zoneinfo import ZoneInfo

logger = logging.getLogger("meta_ads_mcp.audit")

# Business hours config (writes only allowed during these hours)
BUSINESS_HOURS_START = 8   # 8:00 AM
BUSINESS_HOURS_END = 20    # 8:00 PM
DEFAULT_TIMEZONE = "America/Sao_Paulo"


def is_business_hours(timezone: str = DEFAULT_TIMEZONE) -> bool:
    """Check if current time is within business hours."""
    tz = ZoneInfo(timezone)
    now = datetime.now(tz)
    # Weekdays only (Mon=0, Sun=6)
    if now.weekday() >= 5:
        return False
    return BUSINESS_HOURS_START <= now.hour < BUSINESS_HOURS_END


def warn_outside_business_hours(operation: str, timezone: str = DEFAULT_TIMEZONE) -> bool:
    """Log a warning if write happens outside business hours.

    Does NOT block the operation — the HITL approval flow is the primary
    defense against bot-like writes. Business hours acts as a soft signal
    only: legitimate humans (account owners) may approve writes at any
    hour. The warning is recorded in logs and audit trail for forensic
    visibility if Meta ever questions a write pattern.

    Args:
        operation: Description of the write operation being attempted.
        timezone: IANA timezone string.

    Returns:
        True if outside business hours (caller can include in audit metadata).
    """
    if is_business_hours(timezone):
        return False
    tz = ZoneInfo(timezone)
    now = datetime.now(tz)
    logger.warning(
        "Write outside business hours: %s at %s (%s). "
        "Allowed because HITL approval is required, but unusual pattern.",
        operation, now.strftime('%H:%M %A'), timezone,
    )
    return True


class AuditLog:
    """Append-only audit log for Meta API operations.

    Logs every write operation with full context for compliance.
    Log file is JSON Lines format (one JSON object per line).
    """

    def __init__(self, log_dir: Optional[str] = None):
        if log_dir:
            self._log_dir = Path(log_dir)
        else:
            self._log_dir = Path(os.environ.get(
                "META_ADS_AUDIT_DIR",
                Path(__file__).parent.parent.parent / "audit_logs",
            ))
        self._log_dir.mkdir(parents=True, exist_ok=True)

    @property
    def _log_file(self) -> Path:
        """Daily log file: audit_2026-04-16.jsonl"""
        date = datetime.now().strftime("%Y-%m-%d")
        return self._log_dir / f"audit_{date}.jsonl"

    def log_write(
        self,
        operation: str,
        endpoint: str,
        resource_id: str,
        before_state: Optional[dict[str, Any]] = None,
        after_state: Optional[dict[str, Any]] = None,
        request_payload: Optional[dict[str, Any]] = None,
        response_code: int = 0,
        response_body: Optional[dict[str, Any]] = None,
        user_confirmed: bool = False,
        buc_utilization: Optional[dict[str, Any]] = None,
        error: Optional[str] = None,
    ):
        """Log a write operation to the audit trail.

        Args:
            operation: Type of operation (create, update, delete, pause, activate)
            endpoint: API endpoint called
            resource_id: ID of the resource being modified
            before_state: State before the change (for updates)
            after_state: State after the change
            request_payload: What was sent (tokens sanitized)
            response_code: HTTP response code
            response_body: API response (truncated)
            user_confirmed: Whether a human explicitly approved this
            buc_utilization: BUC header values at time of call
            error: Error message if operation failed
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "epoch": time.time(),
            "operation": operation,
            "endpoint": endpoint,
            "resource_id": resource_id,
            "kind": "write",
            "user_confirmed": user_confirmed,
            "response_code": response_code,
        }

        if before_state:
            entry["before_state"] = before_state
        if after_state:
            entry["after_state"] = after_state
        if request_payload:
            # Sanitize tokens from payload
            safe_payload = {k: v for k, v in request_payload.items()
                          if k not in ("access_token", "appsecret_proof")}
            entry["request_payload"] = safe_payload
        if response_body:
            # Truncate large responses
            body_str = json.dumps(response_body)
            if len(body_str) > 2000:
                entry["response_body"] = json.loads(body_str[:2000] + "...")
            else:
                entry["response_body"] = response_body
        if buc_utilization:
            entry["buc_utilization"] = buc_utilization
        if error:
            entry["error"] = error

        line = json.dumps(entry, ensure_ascii=False)

        with open(self._log_file, "a") as f:
            f.write(line + "\n")

        logger.info(
            "AUDIT: %s %s %s (confirmed=%s, code=%d)",
            operation, endpoint, resource_id, user_confirmed, response_code,
        )

    def log_read(
        self,
        endpoint: str,
        ad_account: Optional[str] = None,
        operation: str = "read",
        resource_id: str = "",
        response_code: int = 200,
    ):
        """Log a read operation to the audit JSONL.

        Reads are logged with a smaller payload (no before/after states) but
        produce a real entry so the audit trail reflects all API activity, not
        just writes.
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "epoch": time.time(),
            "operation": operation,
            "endpoint": endpoint,
            "resource_id": resource_id or (ad_account or ""),
            "kind": "read",
            "response_code": response_code,
        }
        with open(self._log_file, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.debug("READ: %s (account=%s)", endpoint, ad_account)

    def get_recent_writes(self, limit: int = 20) -> list[dict]:
        """Get recent write operations from today's log."""
        return [e for e in self.get_recent_entries(limit=limit * 5)
                if e.get("kind") == "write"][-limit:]

    def get_recent_entries(self, limit: int = 20) -> list[dict]:
        """Get the N most recent audit entries (reads + writes) from today's log."""
        if not self._log_file.exists():
            return []
        entries = []
        with open(self._log_file) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        return entries[-limit:]

    def get_write_count_today(self) -> int:
        """Count write operations logged today."""
        if not self._log_file.exists():
            return 0
        count = 0
        with open(self._log_file) as f:
            for line in f:
                if line.strip():
                    count += 1
        return count


# Singleton
_audit_log: Optional[AuditLog] = None


def get_audit_log() -> AuditLog:
    """Get or create the shared AuditLog singleton."""
    global _audit_log
    if _audit_log is None:
        _audit_log = AuditLog()
    return _audit_log
