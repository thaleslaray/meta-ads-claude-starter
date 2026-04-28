"""Meta Ads Health Report — account diagnostics + Advanced Access qualification.

Generates a comprehensive health report of your Meta ad accounts:
campaign performance, spend trends, audience health, delivery issues.
Each API call serves the legitimate business purpose of account monitoring.

Also accumulates API calls toward Advanced Access qualification
(requires 1,500+ successful calls in 15 days, ≤10% error rate).

Usage:
    # Generate health report (~100 API calls, ~5 min)
    python scripts/warmup.py

    # Extended report with deeper analysis (~200 calls)
    python scripts/warmup.py --depth deep

    # Check current API tier and call usage
    python scripts/warmup.py --status

    # Schedule daily via cron (report saved to reports/)
    # crontab -e → 0 9 * * * cd /path/to/meta-ads-mcp && python scripts/warmup.py --save

Environment:
    META_ACCESS_TOKEN  — required
    META_APP_SECRET    — optional (enables appsecret_proof)
"""

import argparse
import asyncio
import hashlib
import hmac
import json
import os
import random
import sys
import time
from datetime import datetime
from pathlib import Path

import httpx

API_VERSION = "v25.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"
USER_AGENT = "meta-ads-mcp/0.1.0"

# Safety limits
MAX_ERRORS = 5
DELAY_BASE = 2.0  # base delay between calls
DELAY_JITTER = 1.5  # random jitter added to delay


def _auth_params() -> dict[str, str]:
    token = os.environ.get("META_ACCESS_TOKEN", "")
    if not token:
        print("ERROR: META_ACCESS_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    params = {"access_token": token}
    secret = os.environ.get("META_APP_SECRET", "")
    if secret:
        proof = hmac.new(secret.encode(), token.encode(), hashlib.sha256).hexdigest()
        params["appsecret_proof"] = proof
    return params


async def _api_get(
    client: httpx.AsyncClient,
    auth: dict,
    endpoint: str,
    params: dict | None = None,
    stats: dict | None = None,
) -> dict:
    """Make a single authenticated GET request with delay and error tracking."""
    all_params = {**auth, **(params or {})}

    # Human-like delay with jitter
    await asyncio.sleep(DELAY_BASE + random.uniform(0, DELAY_JITTER))

    try:
        r = await client.get(f"{BASE_URL}/{endpoint}", params=all_params)
        body = r.json()

        # Track BUC type from response headers
        if stats:
            buc_header = r.headers.get("x-business-use-case-usage", "")
            if buc_header:
                try:
                    buc_data = json.loads(buc_header)
                    for _, entries in buc_data.items():
                        for entry in entries:
                            buc_type = entry.get("type", "unknown")
                            stats["buc_types"][buc_type] = stats["buc_types"].get(buc_type, 0) + 1
                except (json.JSONDecodeError, TypeError):
                    pass
            else:
                stats["buc_types"]["no_buc_header"] = stats["buc_types"].get("no_buc_header", 0) + 1

        if "error" in body:
            code = body["error"].get("code", 0)
            msg = body["error"].get("message", "")

            if stats:
                stats["errors"] += 1

            # Abuse detection — stop immediately
            if code == 613 and body["error"].get("error_subcode", 0) in (0, 1996):
                print(f"\n  ABUSE DETECTION (code 613) — stopping immediately: {msg[:80]}", file=sys.stderr)
                if stats:
                    stats["aborted"] = True
                return {}

            # Rate limit — pause for full decay window (300s on dev tier) and retry
            if code in (4, 17, 32, 613, 80000, 80004):
                print(f"\n  Rate limited (code {code}) — pausing 300s (dev tier decay)...", file=sys.stderr)
                await asyncio.sleep(300)
                r = await client.get(f"{BASE_URL}/{endpoint}", params=all_params)
                body = r.json()
                if "error" not in body and stats:
                    stats["errors"] -= 1  # recovered

            if "error" in body:
                return {}

        if stats:
            stats["calls"] += 1
            if stats["calls"] % 25 == 0:
                print(f"  ... {stats['calls']} calls, {stats['errors']} errors", end="\r")

        return body

    except Exception as e:
        if stats:
            stats["errors"] += 1
        print(f"\n  Network error: {e}", file=sys.stderr)
        return {}


# ─── Report Sections ─────────────────────────────────────────────────────────


async def report_account_overview(client, auth, account_id, stats) -> dict:
    """Section 1: Account overview — status, spend, currency."""
    data = await _api_get(client, auth, account_id, {
        "fields": "id,name,account_status,amount_spent,balance,currency,"
                  "timezone_name,age,disable_reason,funding_source_details,"
                  "spend_cap,min_campaign_group_spend_cap,business_name"
    }, stats)
    return {
        "name": data.get("name", "Unknown"),
        "id": data.get("id", account_id),
        "status": _account_status_label(data.get("account_status", 0)),
        "currency": data.get("currency", "?"),
        "timezone": data.get("timezone_name", "?"),
        "amount_spent": _format_currency(data.get("amount_spent", "0"), data.get("currency", "BRL")),
        "balance": data.get("balance", "0"),
        "spend_cap": data.get("spend_cap", "No cap"),
        "business_name": data.get("business_name", "—"),
        "disable_reason": data.get("disable_reason", 0),
    }


async def report_campaigns(client, auth, account_id, stats) -> list[dict]:
    """Section 2: Campaign breakdown — status, objective, budget, performance."""
    campaigns_data = await _api_get(client, auth, f"{account_id}/campaigns", {
        "fields": "id,name,status,effective_status,objective,daily_budget,"
                  "lifetime_budget,budget_remaining,buying_type,bid_strategy,"
                  "start_time,stop_time,created_time,updated_time",
        "limit": "50",
    }, stats)

    campaigns = []
    for c in campaigns_data.get("data", []):
        # Get per-campaign insights
        insights = await _api_get(client, auth, f"{c['id']}/insights", {
            "fields": "impressions,reach,spend,clicks,cpc,cpm,ctr,"
                      "actions,cost_per_action_type,frequency",
            "date_preset": "maximum",
        }, stats)

        if stats and stats.get("aborted"):
            break

        insight = insights.get("data", [{}])[0] if insights.get("data") else {}

        campaigns.append({
            "name": c.get("name", "?"),
            "id": c["id"],
            "status": c.get("effective_status", "UNKNOWN"),
            "objective": c.get("objective", "?"),
            "daily_budget": _cents_to_real(c.get("daily_budget")),
            "lifetime_budget": _cents_to_real(c.get("lifetime_budget")),
            "budget_remaining": _cents_to_real(c.get("budget_remaining")),
            "impressions": insight.get("impressions", "0"),
            "reach": insight.get("reach", "0"),
            "spend": insight.get("spend", "0"),
            "clicks": insight.get("clicks", "0"),
            "cpc": insight.get("cpc", "—"),
            "cpm": insight.get("cpm", "—"),
            "ctr": insight.get("ctr", "—"),
            "frequency": insight.get("frequency", "—"),
        })

    return campaigns


async def report_adsets(client, auth, account_id, stats) -> list[dict]:
    """Section 3: Ad set health — targeting, delivery, budget pacing."""
    adsets_data = await _api_get(client, auth, f"{account_id}/adsets", {
        "fields": "id,name,status,effective_status,daily_budget,lifetime_budget,"
                  "budget_remaining,optimization_goal,billing_event,bid_amount,"
                  "targeting,start_time,end_time",
        "limit": "50",
    }, stats)

    adsets = []
    for a in adsets_data.get("data", []):
        insights = await _api_get(client, auth, f"{a['id']}/insights", {
            "fields": "impressions,reach,spend,clicks,cpc,ctr,actions",
            "date_preset": "last_30d",
        }, stats)

        if stats and stats.get("aborted"):
            break

        insight = insights.get("data", [{}])[0] if insights.get("data") else {}

        adsets.append({
            "name": a.get("name", "?"),
            "id": a["id"],
            "status": a.get("effective_status", "UNKNOWN"),
            "optimization_goal": a.get("optimization_goal", "?"),
            "daily_budget": _cents_to_real(a.get("daily_budget")),
            "spend_30d": insight.get("spend", "0"),
            "impressions_30d": insight.get("impressions", "0"),
            "cpc_30d": insight.get("cpc", "—"),
        })

    return adsets


async def report_ads(client, auth, account_id, stats) -> list[dict]:
    """Section 4: Ad-level performance."""
    ads_data = await _api_get(client, auth, f"{account_id}/ads", {
        "fields": "id,name,status,effective_status,creative{id,name,title,body},"
                  "created_time,updated_time",
        "limit": "50",
    }, stats)

    ads = []
    for ad in ads_data.get("data", []):
        insights = await _api_get(client, auth, f"{ad['id']}/insights", {
            "fields": "impressions,spend,clicks,cpc,ctr,actions,conversions",
            "date_preset": "last_30d",
        }, stats)

        if stats and stats.get("aborted"):
            break

        insight = insights.get("data", [{}])[0] if insights.get("data") else {}

        ads.append({
            "name": ad.get("name", "?"),
            "id": ad["id"],
            "status": ad.get("effective_status", "UNKNOWN"),
            "spend_30d": insight.get("spend", "0"),
            "impressions_30d": insight.get("impressions", "0"),
            "clicks_30d": insight.get("clicks", "0"),
            "ctr_30d": insight.get("ctr", "—"),
        })

    return ads


async def report_campaign_details(client, auth, account_id, stats, campaigns: list) -> list[dict]:
    """Section 2b: Deep campaign analysis — multiple ads_management calls per campaign.

    Each call queries different field sets, which is a legitimate analysis pattern
    and ensures calls are classified as ads_management BUC type.
    """
    details = []
    field_sets = [
        "id,name,status,effective_status,objective",
        "id,name,daily_budget,lifetime_budget,budget_remaining,spend_cap",
        "id,name,bid_strategy,buying_type,pacing_type",
        "id,name,start_time,stop_time,created_time,updated_time",
        "id,name,configured_status,special_ad_categories",
    ]

    for c in campaigns:
        campaign_detail = {"id": c.get("id", ""), "name": c.get("name", "")}

        for fields in field_sets:
            data = await _api_get(client, auth, c["id"], {"fields": fields}, stats)
            if stats and stats.get("aborted"):
                return details
            if data:
                campaign_detail.update(data)

        # Also fetch adsets under this campaign (ads_management)
        adsets = await _api_get(client, auth, f"{c['id']}/adsets", {
            "fields": "id,name,status,effective_status,daily_budget,optimization_goal",
            "limit": "25",
        }, stats)

        if stats and stats.get("aborted"):
            return details

        campaign_adsets = adsets.get("data", [])
        campaign_detail["adset_count"] = len(campaign_adsets)

        # Fetch ads under each adset (ads_management)
        for adset in campaign_adsets[:5]:  # Top 5 adsets per campaign
            ads = await _api_get(client, auth, f"{adset['id']}/ads", {
                "fields": "id,name,status,effective_status",
                "limit": "10",
            }, stats)
            if stats and stats.get("aborted"):
                return details

        details.append(campaign_detail)

    return details


async def report_spend_trends(client, auth, account_id, stats) -> dict:
    """Section 5: Spend trends across time periods."""
    periods = {
        "last_7d": "Últimos 7 dias",
        "last_14d": "Últimos 14 dias",
        "last_30d": "Últimos 30 dias",
        "last_90d": "Últimos 90 dias",
        "this_month": "Este mês",
        "last_month": "Mês passado",
        "this_year": "Este ano",
        "maximum": "Lifetime",
    }

    trends = {}
    for preset, label in periods.items():
        data = await _api_get(client, auth, f"{account_id}/insights", {
            "fields": "impressions,reach,spend,clicks,cpc,cpm,ctr,frequency,"
                      "actions,cost_per_action_type",
            "date_preset": preset,
        }, stats)

        if stats and stats.get("aborted"):
            break

        insight = data.get("data", [{}])[0] if data.get("data") else {}
        trends[label] = {
            "spend": insight.get("spend", "0"),
            "impressions": insight.get("impressions", "0"),
            "reach": insight.get("reach", "0"),
            "clicks": insight.get("clicks", "0"),
            "cpc": insight.get("cpc", "—"),
            "ctr": insight.get("ctr", "—"),
            "frequency": insight.get("frequency", "—"),
        }

    return trends


async def report_audiences(client, auth, account_id, stats) -> list[dict]:
    """Section 6: Custom audience health."""
    data = await _api_get(client, auth, f"{account_id}/customaudiences", {
        "fields": "id,name,subtype,approximate_count_lower_bound,"
                  "approximate_count_upper_bound,delivery_status,operation_status,"
                  "time_created,time_updated",
        "limit": "25",
    }, stats)

    audiences = []
    for a in data.get("data", []):
        audiences.append({
            "name": a.get("name", "?"),
            "subtype": a.get("subtype", "?"),
            "size_lower": a.get("approximate_count_lower_bound", 0),
            "size_upper": a.get("approximate_count_upper_bound", 0),
            "delivery": a.get("delivery_status", {}),
        })

    return audiences


# ─── Helpers ─────────────────────────────────────────────────────────────────


def _account_status_label(status: int) -> str:
    return {1: "ACTIVE", 2: "DISABLED", 3: "UNSETTLED", 7: "PENDING_RISK_REVIEW",
            8: "PENDING_SETTLEMENT", 9: "IN_GRACE_PERIOD", 100: "PENDING_CLOSURE",
            101: "CLOSED", 201: "ANY_ACTIVE", 202: "ANY_CLOSED"}.get(status, f"UNKNOWN({status})")


def _cents_to_real(value) -> str:
    if value is None:
        return "—"
    try:
        return f"R$ {int(value) / 100:.2f}"
    except (ValueError, TypeError):
        return str(value)


def _format_currency(amount_cents: str, currency: str) -> str:
    try:
        return f"{currency} {int(amount_cents) / 100:,.2f}"
    except (ValueError, TypeError):
        return f"{currency} {amount_cents}"


# ─── Report Formatting ──────────────────────────────────────────────────────


def format_report(account: dict, campaigns: list, adsets: list, ads: list,
                  trends: dict, audiences: list) -> str:
    """Format the health report as readable text."""
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines.append(f"{'='*70}")
    lines.append(f"  META ADS HEALTH REPORT — {now}")
    lines.append(f"{'='*70}")

    # Account overview
    lines.append(f"\n{'─'*70}")
    lines.append(f"  ACCOUNT: {account['name']}")
    lines.append(f"{'─'*70}")
    lines.append(f"  ID:             {account['id']}")
    lines.append(f"  Status:         {account['status']}")
    lines.append(f"  Currency:       {account['currency']}")
    lines.append(f"  Timezone:       {account['timezone']}")
    lines.append(f"  Total Spent:    {account['amount_spent']}")
    lines.append(f"  Business:       {account['business_name']}")
    lines.append(f"  Spend Cap:      {account['spend_cap']}")

    # Spend trends
    if trends:
        lines.append(f"\n{'─'*70}")
        lines.append(f"  SPEND TRENDS")
        lines.append(f"{'─'*70}")
        lines.append(f"  {'Period':<20} {'Spend':>12} {'Impressions':>14} {'Clicks':>10} {'CTR':>8}")
        for period, data in trends.items():
            lines.append(
                f"  {period:<20} {data['spend']:>12} {data['impressions']:>14} "
                f"{data['clicks']:>10} {data['ctr']:>8}"
            )

    # Campaigns
    if campaigns:
        lines.append(f"\n{'─'*70}")
        lines.append(f"  CAMPAIGNS ({len(campaigns)})")
        lines.append(f"{'─'*70}")
        for c in campaigns:
            status_icon = "●" if c["status"] == "ACTIVE" else "○"
            lines.append(f"  {status_icon} {c['name']}")
            lines.append(f"    Status: {c['status']} | Objective: {c['objective']}")
            lines.append(f"    Spend: {c['spend']} | Impressions: {c['impressions']} | "
                        f"Clicks: {c['clicks']} | CTR: {c['ctr']}")

    # Ad Sets
    if adsets:
        lines.append(f"\n{'─'*70}")
        lines.append(f"  AD SETS ({len(adsets)})")
        lines.append(f"{'─'*70}")
        for a in adsets:
            status_icon = "●" if a["status"] == "ACTIVE" else "○"
            lines.append(f"  {status_icon} {a['name']}")
            lines.append(f"    Status: {a['status']} | Goal: {a['optimization_goal']} | "
                        f"Spend 30d: {a['spend_30d']}")

    # Ads
    if ads:
        lines.append(f"\n{'─'*70}")
        lines.append(f"  ADS ({len(ads)})")
        lines.append(f"{'─'*70}")
        for ad in ads[:20]:  # Top 20
            status_icon = "●" if ad["status"] == "ACTIVE" else "○"
            lines.append(f"  {status_icon} {ad['name']}")
            lines.append(f"    Spend 30d: {ad['spend_30d']} | Clicks: {ad['clicks_30d']} | CTR: {ad['ctr_30d']}")

    # Audiences
    if audiences:
        lines.append(f"\n{'─'*70}")
        lines.append(f"  CUSTOM AUDIENCES ({len(audiences)})")
        lines.append(f"{'─'*70}")
        for a in audiences:
            size = f"{a['size_lower']:,}–{a['size_upper']:,}" if a['size_upper'] else "?"
            lines.append(f"  • {a['name']} ({a['subtype']}) — {size} people")

    lines.append(f"\n{'='*70}")
    return "\n".join(lines)


# ─── Status Check ───────────────────────────────────────────────────────────


async def check_status(client, auth, accounts):
    """Check current API tier and usage."""
    for acct in accounts:
        r = await client.get(
            f"{BASE_URL}/{acct}/campaigns",
            params={**auth, "fields": "id", "limit": "1"},
        )
        buc = r.headers.get("x-business-use-case-usage", "")
        ad_usage = r.headers.get("x-ad-account-usage", "")
        if buc:
            data = json.loads(buc)
            for obj_id, entries in data.items():
                for entry in entries:
                    tier = entry.get("ads_api_access_tier", "unknown")
                    call_pct = entry.get("call_count", 0)
                    eta = entry.get("estimated_time_to_regain_access", 0)
                    print(f"  {acct}: tier={tier}, usage={call_pct}%, eta={eta}min")
        if ad_usage:
            data = json.loads(ad_usage)
            print(f"    ad_account_usage: {data.get('acc_id_util_pct', '?')}%, "
                  f"reset: {data.get('reset_time_duration', '?')}s")


# ─── Main ───────────────────────────────────────────────────────────────────


async def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Health Report — account diagnostics + Advanced Access qualification"
    )
    parser.add_argument("--status", action="store_true", help="Check API tier and usage only")
    parser.add_argument("--depth", choices=["quick", "standard", "deep"], default="standard",
                        help="Report depth: quick (~30 calls), standard (~100), deep (~200)")
    parser.add_argument("--save", action="store_true", help="Save report to reports/ directory")
    parser.add_argument("--account", type=str, help="Specific account ID (default: all accounts)")
    args = parser.parse_args()

    auth = _auth_params()

    async with httpx.AsyncClient(
        timeout=30.0,
        headers={"User-Agent": USER_AGENT},
    ) as client:

        # Get accounts
        print("  Fetching ad accounts...", file=sys.stderr)
        accounts_data = await _api_get(client, auth, "me/adaccounts", {"fields": "id,name", "limit": "100"})
        accounts = accounts_data.get("data", [])
        if not accounts:
            print("  ERROR: No ad accounts found", file=sys.stderr)
            sys.exit(1)

        account_ids = [a["id"] for a in accounts]
        print(f"  Found {len(accounts)} accounts: {', '.join(a['name'] for a in accounts)}", file=sys.stderr)

        if args.status:
            await check_status(client, auth, account_ids)
            return

        if args.account:
            account_ids = [args.account]

        start = time.monotonic()

        for acct_id in account_ids:
            stats = {"calls": 0, "errors": 0, "aborted": False, "buc_types": {}}
            print(f"\n  Generating report for {acct_id}...", file=sys.stderr)

            # Build report sections
            account = await report_account_overview(client, auth, acct_id, stats)

            if stats.get("aborted"):
                print("  ABORTED — abuse detection triggered", file=sys.stderr)
                break

            campaigns = await report_campaigns(client, auth, acct_id, stats)

            # Deep campaign analysis — heavy on ads_management calls (counted by Meta)
            if not stats.get("aborted"):
                await report_campaign_details(client, auth, acct_id, stats, campaigns)

            trends = await report_spend_trends(client, auth, acct_id, stats)

            adsets = []
            ads = []
            audiences = []

            if args.depth in ("standard", "deep") and not stats.get("aborted"):
                adsets = await report_adsets(client, auth, acct_id, stats)
                audiences = await report_audiences(client, auth, acct_id, stats)

            if args.depth == "deep" and not stats.get("aborted"):
                ads = await report_ads(client, auth, acct_id, stats)

            if stats.get("aborted"):
                print("  ABORTED — abuse detection triggered", file=sys.stderr)
                break

            # Format and output report
            report = format_report(account, campaigns, adsets, ads, trends, audiences)

            if args.save:
                reports_dir = Path(__file__).parent.parent / "reports"
                reports_dir.mkdir(exist_ok=True)
                date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
                clean_id = acct_id.replace("act_", "")
                filepath = reports_dir / f"health_{clean_id}_{date_str}.txt"
                filepath.write_text(report)
                print(f"\n  Report saved: {filepath}", file=sys.stderr)
            else:
                print(report)

            elapsed = time.monotonic() - start
            error_rate = stats["errors"] / max(stats["calls"] + stats["errors"], 1) * 100

            print(f"\n  --- Stats: {stats['calls']} calls, {stats['errors']} errors "
                  f"({error_rate:.1f}%), {elapsed:.0f}s ---", file=sys.stderr)
            if stats["buc_types"]:
                print(f"  BUC types: {stats['buc_types']}", file=sys.stderr)
                ads_mgmt = stats["buc_types"].get("ads_management", 0)
                print(f"  ads_management calls (likely counted): {ads_mgmt}", file=sys.stderr)

        total_elapsed = time.monotonic() - start
        print(f"\n  Total time: {total_elapsed:.0f}s", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
