---
name: meta-app-review-approval
description: Use whenever the user is preparing or submitting a Meta App Review for Marketing API features (Ads Management Standard Access, ads_read, ads_management, business_management, Page-related permissions). Trigger phrases include "App Review", "Standard Access", "Advanced Access", "Marketing API permission", "screencast pra Meta", "submeter pro Meta", "rejeitado pelo Meta", "ads_management", "ads_read", "BM verification" — even if the user doesn't say those exact terms but is clearly working on getting permissions approved on developers.facebook.com. Captures the full approval recipe (description, screencast specs, form answers, post-approval verification) from a real first-try approval that took 2 hours.
---

# Meta App Review — Approval Recipe

This skill captures the recipe that got `Ads Management Standard Access` approved on the **first attempt in ~2 hours** for an internal first-party tool. Use it whenever you're preparing or submitting for App Review.

## What this skill is for

Meta App Review is the gate to production access for Marketing API and Page-related permissions. Most apps get rejected 3-10 times before approval because the description, screencast, and form answers don't align with what reviewers actually look for. This skill encodes the alignment formula.

**Scope:** built specifically around Ads Management Standard Access for **first-party / internal tools** (companies managing their own ad accounts). Most of it transfers to other Marketing API features and SaaS apps too — but where SaaS differs, it's flagged inline.

## The 8 things that decide your approval

1. **Description** must hit 5 specific sections in the right order.
2. **Screencast** must show System User auth explicitly OR include OAuth login.
3. **Privacy Policy URL** must respond 200 OK on a public domain (doesn't need to be on the app's own domain).
4. **Form answers** ("Tratamento de dados") must reflect basic LGPD/GDPR maturity, not "none of the above".
5. **Site URL** in basic settings should point to your business marketing site, not to the app dashboard.
6. **Instructions for analyst** must explain the auth model and reproduce what's in the screencast.
7. **Description text and screencast must match step-by-step.** Mismatch is the #1 rejection reason.
8. **Standard Access ≠ Advanced Access.** Standard has no minimum-call requirement; the "1500 calls + <10% error in 30 days" rule applies only to Advanced.

If those 8 are right, approval comes fast. The rest of this skill is the concrete how-to.

## Phase 0 — Build a demo dashboard (the "what to show" blueprint)

The screencast (Phase 3) needs to demonstrate real Marketing API integration. Most apps are rejected because they show only a marketing site or a static UI — Meta needs to see actual writes happening through the API.

**You need a demo dashboard.** It can be:
- The starter at https://github.com/thaleslaray/meta-ads-claude-starter (clone, configure 5 env vars, deploy in 30min)
- Something you build yourself (use the blueprint below)

After approval, this dashboard is **disposable** — operation happens via Claude Code + MCP, not the dashboard. Don't over-engineer it.

### Minimum demo requirements (the dashboard MUST have)

For the screencast to satisfy reviewers, the dashboard needs to demonstrate:

1. **Read** — list real campaigns from at least one of your own ad accounts
2. **Write 1 — pause/activate** — toggle status of a campaign with HITL approval (confirmation panel before the API call)
3. **Write 2 — update budget** — change daily budget of a campaign with HITL approval
4. **Audit log visible** — show a log of API calls (operation, resource_id, before/after, timestamp)
5. **Auth model visible** — either OAuth flow OR a settings/info page showing System User configuration

### Implementation pattern (any stack)

Backend (the "how"):
- Authenticate to Marketing API server-to-server with System User token + appsecret_proof (HMAC-SHA256)
- Wrap every API call in a function that: (a) checks rate limit, (b) appends to audit log, (c) signs with appsecret_proof
- Writes require an explicit `user_confirmed: true` parameter — refuse if not set

Frontend (the "what user sees"):
- List of campaigns (table with name, status, budget, spend)
- Drawer/modal with "Propose change" → "Confirm" → "Approve & Execute" sequence (this is the HITL flow)
- Activity/Audit page showing recent operations
- Settings page showing tier (development_access vs standard_access), Business Manager ID, ad accounts under management

### Reference implementation

The starter repo has a working version in Next.js 15 + FastAPI deployed on Vercel. Files to look at:
- `dashboard/api/index.py` — backend with all 5 features
- `dashboard/components/campaigns/CampaignDrawer.tsx` — HITL flow pattern
- `dashboard/app/settings/page.tsx` — settings page exposing System User config

### What the dashboard does NOT need

- Beautiful design (functional > pretty)
- All Marketing API endpoints (just the ones tied to the requested permission)
- Production-grade error handling (it's a demo)
- Multi-tenant support (first-party use only)
- Any real users (the dashboard runs on your own accounts)

## Phase 1 — Pre-flight check (5 min)

Before you write a single line, verify these are true:

- [ ] Business Manager is verified on Meta (green check in BM settings).
- [ ] App is in "Live" mode (not "Development") — required for App Review.
- [ ] App is configured with the right "Use Case" (e.g., "Other → Empresa") so the right permission set appears.
- [ ] Privacy Policy URL is set in App Settings → Basic and returns HTTP 200.
- [ ] User Data Deletion URL or Instructions field is filled (can be the same Privacy URL if it has a deletion section).
- [ ] System User token (if applicable) signs with `appsecret_proof` (HMAC-SHA256). Plain tokens get auto-flagged.

If any of those is `false`, fix first. App Review will reject without a single human looking at the screencast.

## Phase 2 — Write the description (15 min)

Use the 5-section formula in `assets/description-template.txt`. Read it now, then adapt to the user's specifics.

The 5 sections, in order:

1. **Actor + first-party declaration** — who you are, which ad accounts you manage, explicit "we are NOT a third-party SaaS" if you're internal.
2. **Authentication model** — System User token + appsecret_proof, or OAuth flow. State this BEFORE describing what the app does.
3. **What the app does** — numbered list (3-7 items) of concrete features tied to the requested permission.
4. **Why Standard Access is required** — quota math: dev tier 60 pts/h is exhausted in seconds at scale; Standard 9000 pts/h is the minimum.
5. **Compliance & safety** — bullet list: auth method, audit log, rate limiter, HITL approval gates, HTTPS-only.

Each sentence in the description must correspond to something the reviewer will see in the screencast. Mismatch = rejection.

## Phase 3 — Build the screencast (30-60 min)

Specs that work in 2026:

- **Length:** 1-5 minutes. No hard limit, but focused beats long.
- **Resolution:** 720p+. 4K works too.
- **Captions:** Netflix-style (yellow text, bottom, black outline). See `scripts/burn-captions.sh`.
- **Language:** English UI + English captions. UI in another language is OK if you flag it in the form, but English avoids translation ambiguity.
- **Audio narration:** optional. Reviewers often watch muted — captions matter more.

What the screencast must show, in order:

1. **System User caption first 4 seconds** if you don't have OAuth. Without this overlay, reviewers reject with "unable to verify use case experience". Example caption: `"Internal dashboard — auth via server-side System User token (no end-user OAuth)"`.
2. **Real campaign data** — real names, real budgets, real status. No "Demo Client 1" placeholders.
3. **Each requested permission demonstrated explicitly.** Caption naming the permission at the moment of use: `"Backend calls Marketing API with System User token + ads_management"`.
4. **Result visible.** Show Meta's native Ads Manager (split-screen recommended) reflecting the write in real time. This is the proof that the API integration is real.
5. **Optional but high-signal:** audit log screen + settings screen with App ID/BM/tier visible. Shows compliance maturity.

The ffmpeg recipe for burning Netflix-style captions on a 4K screen recording is in `scripts/burn-captions.sh`. The `.ass` template (with PlayResY=2160 so font sizes scale correctly on 4K) is in `assets/captions-template.ass`.

## Phase 4 — Fill the form (10 min)

The submission form has multiple steps. The right answers are non-obvious for some. See `references/form-fields.md` for every field with the recommended answer and reasoning.

Highlights:

- **Site URL**: keep your **business marketing site** here, not the app dashboard. The marketing site validates the entity exists. The dashboard URL goes inside the "Instructions for analyst" textbox.
- **Tratamento de dados → "Quais processos aplica a solicitações de autoridades públicas"**: never mark "Nenhuma das opções acima". Mark at least "Análise obrigatória sobre legitimidade" + "Política de minimização de dados". These are LGPD baseline; marking "none" signals immaturity.
- **Privacy Policy URL**: same business entity is OK across subdomains/related domains. `www.company.com/privacy` works fine for an app deployed at `app.company.com`.
- **Instructions for analyst** template: see `assets/instructions-web-2-template.txt`. Must explicitly explain System User auth (matching the screencast captions) and list the ad account IDs.

## Phase 5 — Submit and verify (post-approval)

Once approved (email subject: "Your App Review results are ready"), tier upgrade is immediate but the dashboard's quota cache only refreshes on next real API call.

To verify the upgrade actually happened:

```bash
bash scripts/verify-tier.sh <account_id> <api_base_url>
```

This makes a real read call, then queries the quota endpoint, and confirms `ads_api_access_tier: "standard_access"` in the response. See `scripts/verify-tier.sh` for details.

**If the tier still shows `development_access` after a real call**, the upgrade hasn't propagated yet — wait 5-10 minutes and retry. If it persists past 1 hour, contact Meta support via the developer dashboard.

## Phase 6 — Take down the demo URL (security hygiene)

**Critical:** the demo dashboard deployed for App Review (e.g. on Vercel) exposes **read AND write** endpoints with your real Meta credentials. Reviewer needed it to verify the use case — but once approved, leaving it public is a footgun:

- Anyone who guesses the URL can call `/api/campaign/{id}/budget` or `/api/campaign/{id}/status` with no auth on top of the public route.
- The HITL flow is enforced by Claude Code (the operator), not by the HTTP layer — direct HTTP calls bypass it.
- Audit log + rate limiter still apply, but the worst case is real money spent / campaigns paused on real ads.

**Operational use of the MCP does NOT need this URL.** The MCP runs locally inside Claude Code with the same credentials — the dashboard was a one-time demo artifact for the reviewer.

After approval (email confirmed + `verify-tier.sh` shows `standard_access`):

```bash
# 1. Remove the custom domain alias (URL stops resolving)
vercel alias rm meta.your-domain.com --yes

# 2. Delete the project entirely (also kills the *.vercel.app fallback URL)
vercel project rm meta-ads-dashboard
```

If you keep the project for any reason, at minimum: rotate the Vercel env vars (`META_ACCESS_TOKEN`, `META_APP_SECRET`) and put the deployment behind Vercel's password protection / SSO.

## Common pitfalls (the ones that wasted us hours)

- **Vídeo sem caption explicando System User** → "unable to verify use case experience". This is the #1 rejection mode for S2S apps.
- **Privacy Policy URL retornando 404** → instant reject without human review.
- **"None of the above" no form de tratamento de dados** → reviewer reads as low compliance maturity, asks for clarification (delays approval).
- **Confundir Standard vs Advanced Access** → tentar acumular 1500 calls antes de submeter Standard (não precisa). Detalhe completo em `references/myths.md`.
- **Site URL = dashboard URL** → reviewer não consegue validar a entidade business. Use o site institucional.

## When the user asks "como tá minha submissão?" or similar

Don't guess. The Meta dashboard is authoritative. Either:
1. Open https://developers.facebook.com/apps/<APP_ID>/app-review/submissions/ via browser automation if available.
2. Check Gmail for emails from `noreply@developers.facebook.com` with subjects "Your App Review results are ready" or "Sua análise do app está pronta".
3. Ask the user for a screenshot.

## What to do if rejected

Meta's rejection notes are usually specific. Read the literal text in the email or the dashboard, then:

- **"Unable to verify use case experience"** → re-record screencast with more explicit captions per permission. Add the System User overlay if missing.
- **"Privacy policy URL not accessible"** → check the URL responds 200 from a clean browser. Update if needed.
- **"Permissions requested don't match demonstrated use"** → narrow the permission list OR expand the screencast to demonstrate every requested permission.
- **"Insufficient API integration"** → this is the Advanced Access criterion. Confirm you're submitting for Standard, not Advanced.

Re-submit is fast (3-5 days vs 3-7 for first review). Keep going.

## Quando precisar do próximo tier (Advanced Access)

Depois de aprovado em Standard, o próximo gate só faz sentido se o app virar **third-party** — atender contas de outras empresas, não as próprias.

### Tiers da Marketing API

| Tier | Quota | Quem precisa |
|------|-------|--------------|
| Development | 60 pts/h | Default ao criar app, só testes |
| **Standard** | 9.000 pts/h | First-party: gerenciar contas próprias do business |
| **Advanced** | Sem cap prático | Third-party: SaaS/agência atendendo contas de clientes externos |

### Critérios pra Advanced

1. Standard Access aprovado primeiro (pré-requisito)
2. **1.500+ chamadas Marketing API bem-sucedidas nos últimos 30 dias**
3. **Taxa de erro <10%** no mesmo período
4. App configurado pra OAuth (clientes externos autorizam suas próprias BMs)
5. Privacy policy menciona explicitamente uso third-party de dados

### Sinais de que NÃO precisa de Advanced

- Você gerencia só suas próprias contas (first-party stays first-party)
- Time interno tem N pessoas — 9.000 pts/h cobre fácil
- Sem planos de virar SaaS/agência

Pra esses casos, Standard é o final da linha. Pode arquivar a busca por Advanced.

### Como pedir Advanced

Mesmo fluxo desta skill (descrição + screencast + form), mas com diferenças:
- Descrição precisa explicar o modelo third-party (clientes conectam suas próprias contas)
- Screencast precisa mostrar **fluxo OAuth real** (não dá pra usar System User caption como atalho)
- Justificativa de quota deve mostrar volume de calls atual vs necessário
- Privacy policy precisa cobrir tratamento de dados de clientes terceiros, não só dados internos

Se chegar nesse ponto, refaz com este skill mas com foco em third-party — a fórmula muda.

## 5 regras anti-ban (válidas ANTES e DEPOIS da aprovação)

A skill `meta-ads-compliance` tem detalhes completos, mas pra garantir que esta skill é auto-suficiente, as 5 regras estão aqui também:

1. **Polling ≥ 5 minutos** — nunca tight loop. Meta's próprio ad-rules engine roda a cada 30-60min. Auto-refresh de dashboard: mínimo 5min.
2. **Writes só em horário comercial** (8h-20h horário local). Mudanças às 3am = sinal de bot.
3. **HITL obrigatório em 4 ações:** criar/publicar criativo, +20% budget, cross-account budget rebalance, criar campanha.
4. **Pausar polling em 60% BUC.** Header `X-Business-Use-Case-Usage` deve ser inspecionado em toda response.
5. **Audit log append-only.** Toda operação loga: timestamp, operation, resource_id, before_state, after_state, user_confirmed.

**Por que importam pro App Review:** o screencast precisa demonstrar o flow HITL e o audit log. Sem essas 2 evidências, reviewer rejeita com "unable to verify use case".

**Por que importam DEPOIS da aprovação:** se você violar essas regras com app aprovado, Meta pode revogar o tier ou banir o app. O ban-wave de 2025-2026 atingiu apps que não seguiram essas regras.

## Skills relacionadas

- **`meta-ads-compliance`** — Regras de compliance e prevenção de ban durante operação contínua com Meta Ads (rate limits, error codes, business hours). Use **depois** de aprovado pra rodar com segurança no novo tier. Esta skill aqui é o gate de aprovação; aquela é a operação pós-aprovação.

## Reference material

- `references/form-fields.md` — every field in the submission form with the right answer and why
- `references/myths.md` — common misconceptions (1500 calls, OAuth required, etc.)
- `references/research-2026-04.md` — the full research that informed this skill (Reddit guides, PostMoore case study, Saurabh Dhar, Meta docs)
- `assets/description-template.txt` — the 5-section description ready to adapt
- `assets/instructions-web-2-template.txt` — the analyst-instructions textbox template
- `assets/captions-template.ass` — Netflix-style caption file with PlayResY=2160 for 4K video
- `scripts/burn-captions.sh` — ffmpeg one-liner to burn captions onto a 4K screen recording
- `scripts/verify-tier.sh` — post-approval tier verification
