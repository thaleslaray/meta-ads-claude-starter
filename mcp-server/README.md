# meta-ads-mcp

Meta Graph API v25.0 MCP server with FastMCP Code Mode — 1,265 tools auto-generated from Meta's official SDK specs.

> **WARNING: Connecting AI agents to Meta ad accounts can result in permanent account bans with no appeal process. This is actively happening as of March 2026. Read the [Safety](#safety) section before using.**

## What is this?

An MCP server that exposes the **entire Meta Graph API** as tools, auto-generated from the [facebook-business-sdk-codegen](https://github.com/facebook/facebook-business-sdk-codegen) spec files. FastMCP Code Mode collapses all 1,265 tools into 3 meta-tools (`search`, `get_schema`, `execute`) so the agent can discover and use any endpoint without being overwhelmed.

## Safety

### The Risk

Since March 2026, Meta is **permanently banning** ad accounts connected to AI agents via MCP. Dozens of confirmed cases across Reddit, LinkedIn, and X. Bans are:

- **Permanent** — no reinstatement
- **Automated** — Meta's abuse detection flags non-human API patterns
- **No appeal** — automated "review unsuccessful" response
- **Cascading** — can disable your personal Facebook profile and Business Manager

### What Triggers Bans

| Trigger | Risk Level |
|---------|-----------|
| Using personal access tokens from cloud IPs | CRITICAL |
| Apps without App Review (dev mode in production) | CRITICAL |
| Burst API call patterns (no delay between requests) | HIGH |
| 24/7 non-human activity patterns | HIGH |
| Write operations (create/update/delete ads) via AI | HIGH |
| Browser automation instead of official API | CRITICAL |

### Built-in Protections

This server includes compliance hardening to minimize (not eliminate) risk:

- **Read-only by default** — write tools require `META_ADS_WRITE_MODE=true`
- **Proactive rate limiting** — monitors all 4 Meta response headers, throttles at 75%, pauses at 90%
- **Circuit breaker** — abuse detection errors (613/0, 613/1996) block ALL requests immediately
- **Input validation** — catches bad parameters before sending (user errors reduce your rate limit quota)
- **ETag caching** — avoids re-fetching unchanged data
- **Custom User-Agent** — identifies as `meta-ads-mcp/0.1.0`
- **Exponential backoff with jitter** — respects `estimated_time_to_regain_access` from headers

### Required Setup (Do NOT Skip)

1. **Create a Meta App** at [developers.facebook.com](https://developers.facebook.com)
2. **Pass App Review** for `ads_read` (and `ads_management` if needed)
3. **Create a System User** in Business Manager (tokens never expire, safer than personal tokens)
4. **Get Advanced Access** — requires 1,500+ API calls in 15 days with <15% error rate. Without this, you get only 60 points/hour (burns in seconds).
5. **Set `META_APP_SECRET`** — enables `appsecret_proof` (HMAC-SHA256 signature on every request)

### Recommended Architecture

The safest pattern is **never let AI write directly to Meta**:

```
Meta API → ETL to your database → AI analyzes offline → Human applies changes in Ads Manager
```

If you must use write operations, enable human-in-the-loop:

```
AI recommends changes → Human reviews → Human applies via META_ADS_WRITE_MODE=true
```

## Setup

```bash
# Install
pip install -e ".[dev]"

# Required
export META_ACCESS_TOKEN="your_system_user_token"

# Strongly recommended
export META_APP_SECRET="your_app_secret"

# Optional: enable write operations (create/update/delete)
# export META_ADS_WRITE_MODE=true

# Run
meta-ads-mcp
```

## Usage with Claude Code

Add to your `.mcp.json`:

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "meta-ads-mcp",
      "env": {
        "META_ACCESS_TOKEN": "your_system_user_token",
        "META_APP_SECRET": "your_app_secret"
      }
    }
  }
}
```

## Architecture

```
facebook-business-sdk-codegen specs (951 JSON files)
    | generator.py parses 119 specs with APIs
Python async tool functions (35 modules, 1,265 tools)
    | server.py registers (filters write tools unless META_ADS_WRITE_MODE=true)
FastMCP server
    | CodeMode transform
3 meta-tools (search, get_schema, execute)
    | agent uses
Claude / any MCP client
```

### Compliance Stack

```
Request flow:
  1. Input validation (validation.py) — catch bad params before sending
  2. Rate limiter (rate_limiter.py) — proactive throttling from response headers
  3. Circuit breaker — abuse detection kills all requests
  4. HTTP client (client.py) — retries with backoff + jitter
  5. ETag cache — If-None-Match for unchanged data

Response headers monitored:
  - X-Business-Use-Case-Usage (BUC — per ad account)
  - X-Ad-Account-Usage (Marketing API utilization %)
  - X-App-Usage (platform-level)
  - X-FB-Ads-Insights-Throttle (insights-specific)

Error codes handled:
  - 4, 17, 32 — platform rate limits (retryable)
  - 613/0, 613/1996 — abuse detection (circuit breaker, NOT retryable)
  - 613/1487742, 613/5044001, 613/1487632 — specific limits (retryable)
  - 80000-80014 — BUC limits (retryable with header wait time)
```

## Rate Limits Quick Reference

| Tier | Ads Management | Ads Insights | Points |
|------|---------------|-------------|--------|
| Dev (Standard Access) | 300 + 40 * active_ads /hr | 600 + 400 * active_ads /hr | Read=1, Write=3 |
| Advanced Access | 100,000 + 40 * active_ads /hr | 190,000 + 400 * active_ads /hr | Read=1, Write=3 |

**QPS limit**: 100 mutations/second per app + ad account.

**User errors reduce your quota**: `- 0.001 * User_Errors` in the formula. Input validation prevents this.

## Advanced Features

### Batch API

Send up to 50 requests in a single HTTP call:

```python
results = await client.batch([
    {"method": "GET", "relative_url": "v25.0/act_123/campaigns?fields=name,status"},
    {"method": "GET", "relative_url": "v25.0/act_456/campaigns?fields=name,status"},
])
```

### Async Insights

For large datasets, uses POST → poll → GET pattern:

```python
# Automatically falls back to sync if the response is small
insights = await client.get_insights_async("act_123", params={
    "fields": "impressions,spend,cpc",
    "date_preset": "last_30d",
    "level": "campaign",
})
```

## Maintenance

### Updating specs (codegen)

When Meta updates their API:

```bash
bash scripts/update_and_regenerate.sh
```

This pulls latest specs from `facebook-business-sdk-codegen`, regenerates enums and all 35 tool modules.

### Updating FastMCP

```bash
pip install --upgrade "fastmcp[code-mode]"
python -m pytest tests/ -v
```

Breaking changes to watch: `CodeMode` and `MontySandboxProvider` imports (currently `fastmcp.experimental.transforms.code_mode`).

## Covered Endpoints

### Ads / Marketing (core)

| Module | Tools | Description |
|--------|-------|-------------|
| accounts | 113 | Account management, billing, users |
| campaigns | 12 | Campaign CRUD, status management |
| adsets | 16 | Ad set CRUD, targeting, budgets |
| ads | 11 | Ad CRUD, previews, leads |
| creatives | 31 | Creative CRUD, video, Instant Experiences |
| audiences | 15 | Custom/lookalike audience management |
| images | 1 | Ad image upload |
| rules | 6 | Automated rules |
| pixels | 46 | Tracking, conversions, event sources |
| ad_studies | 22 | A/B testing (lift studies) |
| ad_labels | 7 | Ad organization labels |
| ad_async | 8 | Async bulk operations, reports |
| ad_monetization | 10 | Monetization, conversion goals |

### Instagram

| Module | Tools | Description |
|--------|-------|-------------|
| instagram | 62 | Feed, stories, reels, insights, hashtags |
| instagram_only_api | 29 | Basic Display API |
| instagram_business | 16 | Business asset integration |

### Pages / Content

| Module | Tools | Description |
|--------|-------|-------------|
| pages | 154 | Facebook Pages management |
| content | 69 | Content CRUD |
| media | 23 | Media management, copyright |

### Business

| Module | Tools | Description |
|--------|-------|-------------|
| business | 161 | Business Manager |
| extended_credit | 17 | Credit lines, invoicing |

### Other

| Module | Tools | Description |
|--------|-------|-------------|
| catalog | 115 | Full catalog management |
| commerce | 30 | Orders, payouts, shop settings |
| lead_gen | 7 | Lead forms and individual leads |
| whatsapp | 57 | Templates, phone numbers, analytics, flows |
| verticals | 46 | Dynamic ads for verticals |
| messenger | 8 | Messenger integration |
| applications | 60 | Facebook Apps |
| users | 61 | Facebook Users |
| groups | 21 | Facebook Groups |
| publisher_block_lists | 9 | Brand safety |
| targeting | 3 | Interest/behavior/demographic search |
| generic | 1 | Raw API call to any endpoint |

**Total: 1,265 auto-generated + 4 manual = 1,269 tools → 3 meta-tools via Code Mode**

## v25.0 Breaking Changes

- Advantage+ shopping/app campaigns are blocked — use Advantage+ campaigns structure
- `metadata=1` query param is deprecated
- Async report error fields changed (error_code uint to int, new fields)

## License

MIT
