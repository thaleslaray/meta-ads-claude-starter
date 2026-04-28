# Meta Ads + Claude Code Starter

Você está em um projeto cujo único objetivo é **passar pelo Meta App Review** e ganhar Standard Access (9.000 pts/h) pra Marketing API.

## ⚠️ Sobre o dashboard incluso

O dashboard (Next.js + FastAPI) é **EXCLUSIVAMENTE demo pro App Review**. Não é ferramenta operacional. Fluxo:

1. Aluno deploya o dashboard
2. Grava screencast nele (split-screen com Ads Manager nativo)
3. Submete pro Meta App Review
4. Após aprovação, dashboard pode ser desligado — operação real é via Claude Code + MCP

**Quando o usuário perguntar sobre uso operacional do dashboard, redirecione pro Claude Code + MCP.** Dashboard ≠ operação.

## Stack

- **Frontend:** Next.js 15 (App Router) + Tailwind CSS v4 + Recharts
- **Backend:** FastAPI (Python) deployado como Vercel Python Functions
- **Auth Meta:** System User token + appsecret_proof (HMAC-SHA256)
- **Skills carregadas:** `meta-ads-compliance`, `meta-ads-warmup`, `meta-app-review-approval`
- **MCP:** `meta-ads-mcp` configurado em `.mcp.json`

## Fluxo do projeto (do zero ao Standard Access)

```
FASE 1 — Setup (15min)
  └─ docs/01-setup.md — criar app Meta + tokens

FASE 2 — Deploy (15min)
  └─ docs/02-deploy.md — Vercel + custom domain (opcional)

FASE 3 — App Review (1-3 dias)
  └─ docs/03-app-review.md — usa skill meta-app-review-approval
  └─ Dashboard deployado serve como demo do reviewer

FASE 4 — Operação contínua (sempre)
  └─ docs/04-operacao.md — uso dia-a-dia com guard rails
```

## Convenções de código

### Backend (FastAPI)
- Toda chamada à Marketing API passa por `client.request()` (não axios direto), pra herdar rate limiter + audit log + appsecret_proof signing
- Writes (POST) sempre requerem `user_confirmed: true` no payload — HITL gate
- Audit log em JSONL append-only via `meta_ads_mcp.audit.get_audit_log()`
- Tier dev = 60 pts/h. Tier Standard = 9.000 pts/h. Em ambos, pausar polling quando BUC > 60%

### Frontend (Next.js)
- SWR pra cache de leituras com `cache: "no-store"` no fetcher (dashboard data muda com frequência)
- Optimistic UI nos writes via `useOptimisticCampaignUpdate` + `useRefreshAfterWrite`
- Captions Netflix-style (yellow + bottom) pra screencasts — ver `examples/captions-template.ass` se existir

## 5 regras anti-ban (NUNCA violar)

A skill `meta-ads-compliance` tem detalhes, mas resumindo:

1. **Polling ≥ 5 minutos** — nunca tight loop
2. **Writes só em horário comercial** (8h-20h horário local)
3. **HITL obrigatório em:** criar/publicar criativo, +20% budget, cross-account rebalance, criar campanha
4. **Pausar polling em 60% BUC** (já implementado no rate limiter)
5. **Audit log append-only** (já implementado)

Quando o usuário pedir uma automação que viole qualquer dessas regras, **recuse e ofereça alternativa safe**.

## Comandos úteis

| O que fazer | Comando |
|-------------|---------|
| Configurar tokens iniciais | `./scripts/setup.sh` |
| Verificar tier Meta após App Review | `./scripts/verify-tier.sh act_xxx https://meta.dominio.com` |
| Acumular calls (warm-up enquanto espera App Review) | `python scripts/warmup.py --depth standard --save` |
| Deploy dashboard | `cd dashboard && vercel deploy --prod` |
| Burn captions em screencast | `~/.claude/skills/meta-app-review-approval/scripts/burn-captions.sh input.mp4 captions.ass output.mp4` |

## Quando o usuário pedir ajuda

- **"como começar?"** → docs/01-setup.md
- **"como deploy?"** → docs/02-deploy.md
- **"vou submeter App Review"** → skill `meta-app-review-approval` + docs/03-app-review.md
- **"como automatizar X?"** → skill `meta-ads-compliance` (regras anti-ban) + docs/04-operacao.md
- **"deu erro"** → docs/05-troubleshooting.md
- **"como funciona Y?"** → este CLAUDE.md + ler arquivo relevante

## Variáveis de ambiente essenciais

Definir em `.env` (local) e no Vercel dashboard (produção):

```
META_ACCESS_TOKEN=         # System User token, nunca commitar
META_APP_SECRET=           # App secret, nunca commitar
META_BM_ID=                # Numeric Business Manager ID
META_AD_ACCOUNTS=          # JSON array: [{"id":"act_xxx","name":"...","label":"..."}]
ORG_NAME=                  # Nome do business (aparece no dashboard)
```

## Branding

Repo maintido por **Thales Laray**. Issues e PRs bem-vindos em `github.com/thaleslaray/meta-ads-claude-starter`.

## Licença

MIT — qualquer um pode usar, modificar, distribuir.
