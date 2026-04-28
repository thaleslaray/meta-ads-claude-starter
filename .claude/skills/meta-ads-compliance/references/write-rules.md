# Write Operations — Detailed Rules

## Risk Classification

### LOW RISK — Simple confirmation
- Pause campaign/adset/ad
- Archive campaign
- Generate ad preview (`/generatepreviews` — read-only, 1pt)

### MEDIUM RISK — Confirmation + before/after log
- Change budget (daily or lifetime)
- Change bid strategy/amount
- Modify targeting
- Change schedule (start/end dates)
- Resume/activate paused campaign
- Change optimization goal

### HIGH RISK — Explicit confirmation + extended review
- Create new campaigns/adsets/ads
- Upload new creatives (triggers ad review)
- Bulk operations (multiple changes in one session)
- Delete anything (IRREVERSIBLE for campaigns)
- Copy campaigns

### NEVER AUTOMATE — Do NOT expose
- Account-level settings (spend limits, timezone)
- Payment methods
- User/permission management
- Business Manager configuration
- Custom Audiences from customer data (privacy/compliance)
- App settings or token management

## Hard Limits

| Operation | Limit | Error Code |
|-----------|-------|------------|
| Budget changes per adset | 4/hour | 613 (sub 1487632) |
| Account spend limit changes | 10/day | 17 (sub 1885172) |
| Ad creation | Based on daily spend | 613 (sub 1487225) |
| QPS mutations | 100/s per app+account | 613 (sub 5044001) |
| Write points | 3 points each (vs 1 for reads) | — |

## Human-in-the-Loop Flow

```
1. USER REQUEST
   "Pause campaign Desafio_0625"

2. AI FETCHES CURRENT STATE (GET — 1pt)
   GET /{campaign_id}?fields=id,name,status,effective_status,daily_budget
   → {status: "ACTIVE", daily_budget: "5000", ...}

3. AI SHOWS PREVIEW
   "Campaign: Desafio_0625 | Vendas | ABO | 1-10-1 | V10
    Current status: ACTIVE
    Daily budget: R$ 50.00
    Action: Will PAUSE this campaign.
    Confirm? (yes/no)"

4. USER CONFIRMS
   "yes"

5. AI EXECUTES (POST — 3pts)
   POST /{campaign_id} data={status: "PAUSED"}

6. AI LOGS (audit_logs/audit_YYYY-MM-DD.jsonl)
   {
     "timestamp": "2026-04-16T14:30:00",
     "operation": "pause",
     "endpoint": "{campaign_id}",
     "resource_id": "{campaign_id}",
     "before_state": {"status": "ACTIVE"},
     "after_state": {"status": "PAUSED"},
     "user_confirmed": true,
     "response_code": 200
   }

7. AI CONFIRMS TO USER
   "Campaign pausada. Status: ACTIVE → PAUSED.
    Logged at audit_logs/audit_2026-04-16.jsonl"
```

## Reversibility

| Operation | Reversible? | How |
|-----------|------------|-----|
| Pause | Yes | Set status=ACTIVE |
| Change budget | Yes | Set back to previous value (from audit log) |
| Archive | Yes | Set status=ACTIVE |
| Delete | **NO** | Permanent — CANNOT undo |
| Create | Partially | Can pause/archive but it exists |
| Creative changes | No | Old creative is replaced |
| Targeting changes | Partially | Can revert params from audit log |

## Meta's Preference

> "It is better to create a new ad than to change existing ones."
> — Meta Marketing API Best Practices

Changes that trigger ad review:
- Creative (image, video, text)
- Targeting
- Optimization goal

Changes that do NOT trigger review:
- Budget
- Schedule
- Bid amount
- Status (pause/activate)
