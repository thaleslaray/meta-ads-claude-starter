"""FastAPI entrypoint for Vercel Python serverless functions.

Handles all /api/* routes via FastAPI's routing. Vercel's @vercel/python
runtime auto-detects the ASGI `app` export and wraps it.

Note on state: each cold-start creates a fresh `_points_used` counter and
fresh audit log (written to /tmp which is per-invocation ephemeral on
Vercel). This is acceptable for an App Review demo — production data
lives in Meta's APIs, not in our function.
"""

import os
import sys

# Ensure bundled meta_ads_mcp package is importable
sys.path.insert(0, os.path.dirname(__file__))

# Force audit log to /tmp (Vercel's only writable directory)
os.environ.setdefault("META_ADS_AUDIT_DIR", "/tmp/audit_logs")

from fastapi import FastAPI, HTTPException, Query  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from meta_ads_mcp.audit import get_audit_log  # noqa: E402
from meta_ads_mcp.client import get_client  # noqa: E402

import json as _json

# Loaded from env vars so this template works for any business.
# META_AD_ACCOUNTS is a JSON array: [{"id": "act_xxx", "name": "...", "label": "..."}]
# META_BM_ID is the Business Manager numeric ID.
# ORG_NAME is your business name (shown in the dashboard UI).
ACCOUNTS = _json.loads(os.environ.get("META_AD_ACCOUNTS", "[]"))
BM_ID = os.environ.get("META_BM_ID", "")
ORG_NAME = os.environ.get("ORG_NAME", "Your Business")

if not ACCOUNTS:
    raise RuntimeError(
        "META_AD_ACCOUNTS env var is required. "
        'Format: \'[{"id":"act_xxx","name":"My Account","label":"Main"}]\''
    )

_points_used = 0
READ_COST = 1
WRITE_COST = 3

app = FastAPI(title="Meta Ads — Operations Dashboard (Vercel)")


@app.middleware("http")
async def add_no_store(request, call_next):
    response = await call_next(request)
    if request.url.path.startswith("/api/"):
        response.headers["Cache-Control"] = "no-store, must-revalidate"
    return response


def _reset_client_loop():
    client = get_client()
    if client._client is not None and not client._client.is_closed:
        client._client = None


# ──────────────────────────────────────────────────────────
# Endpoints
# ──────────────────────────────────────────────────────────

@app.get("/api/accounts")
def api_accounts():
    if not os.environ.get("META_ACCESS_TOKEN"):
        raise HTTPException(401, "META_ACCESS_TOKEN not set in server environment")
    return {"accounts": ACCOUNTS, "bm_id": BM_ID, "org_name": ORG_NAME}


@app.get("/api/quota")
def api_quota(account_id: str = Query(...)):
    client = get_client()
    summary = client.rate_limiter.get_usage_summary(account_id)
    usage = summary.get("account_usage", {})
    tier = usage.get("ads_api_access_tier", "development_access")
    max_pts = 9000 if tier == "standard_access" else 60
    header_pct = usage.get("acc_id_util_pct", 0)
    local_pct = min(100, _points_used * 100 / max_pts)
    used_pct = max(header_pct, local_pct)
    return {
        "tier": tier,
        "used_pct": round(used_pct, 1),
        "max_points": max_pts,
        "remaining_points": max(0, max_pts - int(max_pts * used_pct / 100)),
        "circuit_breaker": summary.get("circuit_breaker_open", False),
        "points_used": _points_used,
    }


@app.get("/api/account/{account_id}/campaigns")
async def api_account_campaigns(account_id: str, date_preset: str = "last_year"):
    global _points_used
    _reset_client_loop()
    client = get_client()

    camps = await client.request("GET", f"/{account_id}/campaigns",
        params={
            "fields": "id,name,status,objective,daily_budget,lifetime_budget,effective_status",
            "limit": 25,
        },
        audit_context={"operation": "list_campaigns", "resource_id": account_id},
    )
    _points_used += READ_COST
    campaigns = {c["id"]: c for c in camps.get("data", [])}

    try:
        ins = await client.request("GET", f"/{account_id}/insights",
            params={
                "fields": "campaign_id,spend,impressions,clicks,ctr,cpc",
                "date_preset": date_preset,
                "level": "campaign",
                "limit": 25,
            },
            audit_context={"operation": "read_campaign_insights", "resource_id": account_id},
        )
        _points_used += READ_COST
        for row in ins.get("data", []):
            cid = row.get("campaign_id")
            if cid in campaigns:
                campaigns[cid]["spend"] = float(row.get("spend", 0))
                campaigns[cid]["impressions"] = int(row.get("impressions", 0))
                campaigns[cid]["clicks"] = int(row.get("clicks", 0))
                campaigns[cid]["ctr"] = float(row.get("ctr", 0))
                campaigns[cid]["cpc"] = float(row.get("cpc", 0))
    except Exception:
        pass

    out = []
    for c in campaigns.values():
        out.append({
            "id": c.get("id"),
            "name": c.get("name") or "—",
            "status": c.get("status"),
            "effective_status": c.get("effective_status"),
            "objective": c.get("objective") or "—",
            "daily_budget": float(c.get("daily_budget", 0)) / 100 if c.get("daily_budget") else None,
            "lifetime_budget": float(c.get("lifetime_budget", 0)) / 100 if c.get("lifetime_budget") else None,
            "spend": c.get("spend", 0),
            "impressions": c.get("impressions", 0),
            "clicks": c.get("clicks", 0),
            "ctr": c.get("ctr", 0),
            "cpc": c.get("cpc", 0),
        })
    out.sort(key=lambda x: x.get("spend", 0), reverse=True)
    return {"campaigns": out}


class StatusUpdate(BaseModel):
    new_status: str
    user_confirmed: bool = False


@app.post("/api/campaign/{campaign_id}/status")
async def api_update_status(campaign_id: str, payload: StatusUpdate):
    global _points_used
    if not payload.user_confirmed:
        raise HTTPException(400, "user_confirmed must be true. HITL approval required.")
    if payload.new_status not in {"ACTIVE", "PAUSED"}:
        raise HTTPException(400, "new_status must be ACTIVE or PAUSED")

    _reset_client_loop()
    client = get_client()

    before = await client.request("GET", f"/{campaign_id}", params={"fields": "status,name"})
    _points_used += READ_COST

    await client.request("POST", f"/{campaign_id}",
        data={"status": payload.new_status},
        audit_context={
            "operation": "update_status",
            "before_state": {"status": before.get("status")},
            "after_state": {"status": payload.new_status},
            "user_confirmed": True,
        },
    )
    _points_used += WRITE_COST

    after = await client.request("GET", f"/{campaign_id}", params={
        "fields": "id,name,status,effective_status"
    })
    _points_used += READ_COST

    return {"ok": True, "campaign": after}


class BudgetUpdate(BaseModel):
    daily_budget_brl: float
    user_confirmed: bool = False


@app.post("/api/campaign/{campaign_id}/budget")
async def api_update_budget(campaign_id: str, payload: BudgetUpdate):
    global _points_used
    if not payload.user_confirmed:
        raise HTTPException(400, "user_confirmed must be true. HITL approval required.")
    if payload.daily_budget_brl < 1.0:
        raise HTTPException(400, "daily_budget must be >= R$ 1.00")

    _reset_client_loop()
    client = get_client()

    before = await client.request("GET", f"/{campaign_id}",
        params={"fields": "daily_budget,name,status"})
    _points_used += READ_COST
    before_brl = float(before.get("daily_budget", 0)) / 100 if before.get("daily_budget") else None

    new_cents = int(payload.daily_budget_brl * 100)
    try:
        await client.request("POST", f"/{campaign_id}",
            data={"daily_budget": str(new_cents)},
            audit_context={
                "operation": "update_budget",
                "before_state": {"daily_budget_brl": before_brl},
                "after_state": {"daily_budget_brl": payload.daily_budget_brl},
                "user_confirmed": True,
            },
        )
    except Exception as e:
        # Meta commonly rejects budget updates on ABO campaigns (budget lives
        # at the ad set level). Surface a friendly message.
        msg = str(e)[:200]
        if "adset" in msg.lower() or "budget" in msg.lower():
            raise HTTPException(
                422,
                "Meta rejected the update. This is usually because the campaign "
                "uses Ad Set Budget Optimization (budget lives on ad sets). "
                "Budget updates at the campaign level are only supported for "
                f"Campaign Budget Optimization (CBO) campaigns. Meta error: {msg}",
            )
        raise HTTPException(422, f"Meta rejected the update: {msg}")
    _points_used += WRITE_COST

    after = await client.request("GET", f"/{campaign_id}",
        params={"fields": "id,name,daily_budget,status"})
    _points_used += READ_COST

    return {"ok": True, "campaign": after}


_DATE_PREVIOUS = {
    "today": "yesterday",
    "yesterday": "last_7d",
    "last_7d": "last_14d",
    "last_30d": "last_90d",
    "last_90d": "last_year",
    "this_year": "last_year",
    "last_year": "maximum",
    "maximum": "maximum",
}


async def _fetch_insights_summary(client, account_id: str, date_preset: str):
    try:
        res = await client.request("GET", f"/{account_id}/insights",
            params={
                "fields": "spend,impressions,clicks,ctr,cpc,reach,frequency",
                "date_preset": date_preset,
                "level": "account",
            },
            audit_context={"operation": "read_account_insights_summary", "resource_id": account_id},
        )
        rows = res.get("data", [])
        if not rows:
            return {"empty": True, "date_preset": date_preset}
        d = rows[0]
        return {
            "empty": False,
            "date_preset": date_preset,
            "spend": float(d.get("spend", 0)),
            "impressions": int(d.get("impressions", 0)),
            "clicks": int(d.get("clicks", 0)),
            "ctr": float(d.get("ctr", 0)),
            "cpc": float(d.get("cpc", 0)),
            "reach": int(d.get("reach", 0)),
            "frequency": float(d.get("frequency", 0)),
        }
    except Exception as e:
        return {"empty": True, "error": str(e)[:200], "date_preset": date_preset}


async def _fetch_insights_daily(client, account_id: str, date_preset: str):
    try:
        res = await client.request("GET", f"/{account_id}/insights",
            params={
                "fields": "spend,date_start",
                "date_preset": date_preset,
                "level": "account",
                "time_increment": 1,
                "limit": 500,
            },
            audit_context={"operation": "read_insights_daily", "resource_id": account_id},
        )
        return [
            {"date": r.get("date_start"), "spend": float(r.get("spend", 0))}
            for r in res.get("data", [])
        ]
    except Exception:
        return []


def _delta_pct(curr, prev):
    if curr is None or prev is None or prev == 0:
        return None
    return round(((curr - prev) / prev) * 100, 1)


@app.get("/api/account/{account_id}/insights-with-delta")
async def api_insights_with_delta(account_id: str, date_preset: str = "last_year"):
    global _points_used
    _reset_client_loop()
    client = get_client()

    current = await _fetch_insights_summary(client, account_id, date_preset)
    _points_used += READ_COST

    prev_preset = _DATE_PREVIOUS.get(date_preset, "maximum")
    previous = await _fetch_insights_summary(client, account_id, prev_preset)
    _points_used += READ_COST

    time_series = await _fetch_insights_daily(client, account_id, date_preset)
    _points_used += READ_COST

    fields = ("spend", "impressions", "clicks", "ctr", "cpc", "reach")
    delta_pct = {}
    for f in fields:
        c = current.get(f) if not current.get("empty") else None
        p = previous.get(f) if not previous.get("empty") else None
        d = _delta_pct(c, p)
        if d is not None:
            delta_pct[f] = d

    return {
        "current": current,
        "previous": previous,
        "delta_pct": delta_pct,
        "time_series": time_series,
    }


@app.get("/api/audit")
def api_audit(limit: int = 20):
    audit = get_audit_log()
    entries = audit.get_recent_entries(limit=limit)
    return {"entries": list(reversed(entries))}
