# 04 — Operação dia-a-dia (pós-aprovação)

Após App Review aprovado, **o dashboard cumpriu sua função e pode ser desligado**. A operação real acontece via Claude Code + MCP `meta-ads-mcp`.

## Setup mínimo pra operação

```bash
cd meta-ads-claude-starter
claude  # Claude Code lê CLAUDE.md + .mcp.json + skills automaticamente
```

Claude entra com:
- ✅ MCP `meta-ads` conectado (acesso direto à Marketing API)
- ✅ Skill `meta-ads-compliance` ativa (regras anti-ban aplicadas em toda interação)
- ✅ Contexto do projeto via CLAUDE.md

## Como mexer nas contas

| Ação | Como fazer |
|------|------------|
| Ver insights | "puxa insights dos últimos 7 dias da conta principal" |
| Listar campanhas | "lista campanhas ativas com spend > R$ 100" |
| Pausar campanha | "pausa a campanha X com aprovação" (Claude pede confirmação) |
| Update budget | "muda o budget da campanha Y pra R$ 500/dia" (Claude pede confirmação) |
| Análise ad-hoc | "compara CTR das 3 contas no último mês" |

## Para uso visual / não-técnico

Se você quer interface gráfica em vez de Claude Code, opções:

1. **Meta Ads Manager nativo** (https://business.facebook.com) — sempre funciona, é o padrão
2. **Reativar o dashboard** — manter Vercel ligado, ele continua funcional
3. **Build outro dashboard** — copy/paste do código vendored neste repo

Mas se você só vai usar Claude Code, **pode desligar o Vercel após aprovação** e economizar.

## 5 regras anti-ban (skill `meta-ads-compliance` aplica automaticamente)

1. **Polling ≥ 5 minutos** — nunca query em loop apertado
2. **Writes só em horário comercial** (8h-20h horário local)
3. **HITL obrigatório em:** criar/publicar criativo, +20% budget, cross-account rebalance, criar campanha
4. **Pausar polling em 60% BUC** (já implementado no rate limiter do MCP)
5. **Audit log append-only** (já implementado)

## Quando o tier voltar pra dev

Se o tier voltar pra `development_access` por qualquer motivo (ex: app teve problema, suspended, etc.), a skill `meta-ads-compliance` flagra automaticamente e sugere abrir App Review de novo via skill `meta-app-review-approval`.

## Próximo passo

→ [05-troubleshooting.md](./05-troubleshooting.md) — Quando der erro
