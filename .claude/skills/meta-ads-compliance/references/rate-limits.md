# Meta API Rate Limits — Formulas and Headers

## Two Separate Systems

1. **Platform Rate Limits** — Graph API (app/user tokens)
2. **Business Use Case (BUC) Rate Limits** — Marketing API, Pages, Instagram

If both apply, **BUC takes precedence**. Marketing API has its own logic and does NOT count against Graph API.

## Development Tier (Standard Access)

| BUC Type | Formula (rolling 1 hour) |
|----------|-------------------------|
| Ads Management | `300 + 40 * Active_Ads` |
| Ads Insights | `600 + 400 * Active_Ads - 0.001 * User_Errors` |
| Custom Audience | `5,000 + 40 * Active_Custom_Audiences` (max 700K) |

**Score-based**: Max 60 points. Read = 1pt, Write = 3pts. Decay 300s, block 300s.

## Advanced Access (Standard Tier)

| BUC Type | Formula (rolling 1 hour) |
|----------|-------------------------|
| Ads Management | `100,000 + 40 * Active_Ads` |
| Ads Insights | `190,000 + 400 * Active_Ads - 0.001 * User_Errors` |
| Custom Audience | `190,000 + 40 * Active_Custom_Audiences` (max 700K) |

**Score-based**: Max 9,000 points. Read = 1pt, Write = 3pts. Decay 300s, block 60s.

## Specific Limits

| Limit | Value | Error Code |
|-------|-------|------------|
| QPS mutations | 100/s per app+account | 613 (sub 5044001) |
| Budget changes per adset | 4/hour | 613 (sub 1487632) |
| Account spend limit | 10/day | 17 (sub 1885172) |
| Ad creation | Based on daily spend | 613 (sub 1487225) |

## Response Headers to Monitor

### X-Business-Use-Case-Usage (MOST IMPORTANT)
```json
{
  "{business-object-id}": [{
    "type": "ads_management",
    "call_count": 95,
    "total_cputime": 20,
    "total_time": 20,
    "estimated_time_to_regain_access": 19,
    "ads_api_access_tier": "standard_access"
  }]
}
```

### X-Ad-Account-Usage
```json
{
  "acc_id_util_pct": 9.67,
  "reset_time_duration": 100,
  "ads_api_access_tier": "standard_access"
}
```

### X-App-Usage
```json
{ "call_count": 28, "total_time": 25, "total_cputime": 25 }
```

### X-FB-Ads-Insights-Throttle
```json
{ "app_id_util_pct": 100, "acc_id_util_pct": 10, "ads_api_access_tier": "standard_access" }
```

## Throttling Thresholds

| Threshold | Action |
|-----------|--------|
| 60% any metric | Pause account for this cycle (Zentric pattern) |
| 80% any metric | Hard pause, check estimated_time_to_regain_access |
| 100% | STOP — continuing increases recovery time |

## Key Rules

- **User errors reduce quota**: `-0.001 * User_Errors` in the formula
- **Multiple IDs = multiple calls**: `?ids=4,5,6` counts as 3 calls, not 1
- **Continuing after limit INCREASES recovery time** — Meta says this explicitly
- **estimated_time_to_regain_access** is in MINUTES, not seconds
