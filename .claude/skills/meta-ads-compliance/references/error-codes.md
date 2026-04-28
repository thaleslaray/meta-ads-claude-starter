# Meta API Error Codes — Complete Reference

## Circuit Breaker (STOP ALL REQUESTS)

| Code | Subcode | Meaning | Action |
|------|---------|---------|--------|
| 613 | 0 (null) | Abuse prevention | Circuit breaker 5min, stop everything |
| 613 | 1996 | Behavioral anomaly | Circuit breaker 5min, reduce volume permanently |

**613/1996 detects:**
- Sudden volume spikes (10 calls/hr → 10,000)
- Pattern changes after deployment
- Volume inconsistent with app's user base
- Systematic graph traversal (account → campaigns → adsets → ads → insights)
- Fix: gradual ramp-up over days, not just backoff

---

## Retryable Rate Limits (Backoff + Retry)

| Code | Subcode | Meaning | Action |
|------|---------|---------|--------|
| 4 | — | App rate limit | Backoff, check X-App-Usage |
| 4 | 1504022 | Ads Insights platform throttle | Backoff, reduce query complexity |
| 4 | 1504039 | Ads Insights platform throttle | Backoff, reduce query complexity |
| 17 | — | User rate limit | Backoff |
| 17 | 2446079 | Ads API token rate limit | Backoff, check access tier |
| 17 | 1885172 | Account spend limit (10/day) | Stop spend changes for today |
| 32 | — | Pages API rate limit | Backoff |
| 613 | 1487742 | Too many calls from ad account | Backoff, check BUC headers |
| 613 | 5044001 | QPS mutation limit (100/s) | Spread mutations over time |
| 613 | 1487632 | Ad set budget limit (4/hr) | Wait 1 hour for that ad set |
| 613 | 1487225 | Ad creation limit | Based on daily spend |

## BUC (Business Use Case) Rate Limits

| Code | Subcode | BUC Type | Action |
|------|---------|----------|--------|
| 80000 | 2446079 | Ads Insights | Use estimated_time_to_regain_access |
| 80001 | — | Pages | Backoff |
| 80002 | — | Instagram | Backoff |
| 80003 | 2446079 | Custom Audience | Backoff |
| 80004 | 2446079 | Ads Management | Backoff |
| 80005 | — | LeadGen | Backoff |
| 80006 | — | Messenger | Backoff |
| 80008 | — | WhatsApp Business | Backoff |
| 80009 | — | Catalog Management | Backoff |
| 80014 | — | Catalog Batch | Backoff |

## Non-Retryable (Fix the Problem)

| Code | Meaning | Action |
|------|---------|--------|
| 190 | Token expired/invalidated | Generate new token, DO NOT retry |
| 10 | Permission denied | Check token scopes |
| 100 | Invalid parameter | Fix the request parameters |
| 200 | Permission denied (specific) | Check access level |
