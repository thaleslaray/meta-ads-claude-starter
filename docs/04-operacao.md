# 04 — Operação dia-a-dia

Como usar o repo no dia-a-dia depois de aprovado em Standard Access.

## Modo de uso recomendado

```bash
cd meta-ads-claude-starter
claude  # Claude Code lê CLAUDE.md + .mcp.json + skills automaticamente
```

Claude entra com:
- ✅ MCP `meta-ads` conectado (acesso direto à API)
- ✅ Skill `meta-ads-compliance` ativa (regras anti-ban)
- ✅ Skill `meta-app-review-approval` carregada se você falar de App Review
- ✅ Contexto do projeto via CLAUDE.md

## 3 caminhos pra mexer nas contas

| Caminho | Quando usar |
|---------|-------------|
| **Meta Ads Manager nativo** | Mudanças complexas, criar campanhas do zero, criativos novos |
| **Dashboard interno** (URL Vercel) | Pause/activate, update budget, ver insights consolidados, audit trail |
| **Claude Code com MCP** | Análises ad-hoc, scripts, automações via prompt |

## 5 regras anti-ban (NUNCA violar)

A skill `meta-ads-compliance` aplica automaticamente, mas vale memorizar:

1. **Polling ≥ 5 minutos** — nunca query em loop apertado
2. **Writes só em horário comercial** (8h-20h horário local)
3. **HITL obrigatório em:** criar/publicar criativo, +20% budget, cross-account rebalance, criar campanha
4. **Pausar polling em 60% BUC** (já implementado no rate limiter)
5. **Audit log append-only** (já implementado)

## Automações safe (verde)

Pode rodar sem stress:

- ✅ Auto-refresh dashboards (5-15min)
- ✅ Day-parting (pause à noite, retoma de manhã)
- ✅ Auto-pause underperformers (CPA > X com cooldown 6h + min spend)
- ✅ Slack alerts em performance changes
- ✅ Relatórios diários automatizados
- ✅ AI agent 24/7 propondo via Slack (HITL no write)

## Automações com cuidado (amarelo)

Implementar com guard rails extras:

- ⚠️ Auto-scale +X% — use cap +15% max 1x/dia, horário comercial
- ⚠️ Bulk creative upload — HITL obrigatório no conteúdo
- ⚠️ Cross-account rebalance — HITL obrigatório

## NÃO fazer (vermelho)

- ❌ Polling sub-minuto
- ❌ Auto-publish criativo sem human review
- ❌ Mudanças fora horário comercial em alta velocidade
- ❌ Retry storm em erro 613/429 (sempre exponential backoff)

## Comandos úteis

| Tarefa | Comando |
|--------|---------|
| Verificar tier atual | `./scripts/verify-tier.sh act_xxx https://meta.dominio.com.br` |
| Listar campanhas via API | Pedir ao Claude: "lista todas as campanhas ativas da conta principal" |
| Pausar campanha | "pausa a campanha X com aprovação humana" |
| Update budget | "muda o budget da campanha Y pra R$ 500/dia, com confirmação" |
| Insights da semana | "puxa insights dos últimos 7 dias agrupado por campanha" |

## Quando o tier voltar pra dev

Se o tier voltar pra `development_access` por qualquer motivo (ex: app teve problema), a skill `meta-ads-compliance` flagra automaticamente e sugere abrir App Review de novo via skill `meta-app-review-approval`.

## Próximo passo

→ [05-troubleshooting.md](./05-troubleshooting.md) — Quando der erro
