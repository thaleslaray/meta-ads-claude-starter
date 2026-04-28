---
name: meta-ads-compliance
description: >
  Regras de compliance e prevenção de ban para operar Meta Ads via AI.
  DEVE ser carregada antes de qualquer interação com a Meta Marketing API,
  MCP meta-ads, ou Graph API de anúncios. Usar sempre que o usuário
  mencionar meta ads, facebook ads, campanha, anuncio, adset, ad set,
  budget, ROAS, CPA, criativos, público-alvo, pausar campanha, ativar
  campanha, insights de ads, performance de anúncios, desempenho,
  otimizar campanha, escalar, ou qualquer operação envolvendo contas
  de anúncio da Meta. Também usar quando o contexto envolver o MCP
  meta-ads-mcp ou tools como rate_limit_status, search_targeting,
  meta_api_call.
metadata:
  author: thaleslaray
  version: 2.1.0
---

# Meta Ads — Regras de Operação

## AVISO

Desde março/2026, a Meta bane permanentemente contas conectadas a AI agents que violam padrões da API. Sem apelação. Todas as regras abaixo existem pra evitar isso.

---

## ONBOARDING (primeira interação da sessão)

Na primeira vez que Meta Ads for mencionado na sessão:

1. Checar memória do projeto por conta Meta Ads salva
2. Se tem → confirmar. Se não → descobrir via `GET /me/adaccounts`
3. Checar consumo via `rate_limit_status(ad_account_id)`
4. Mostrar:

```
━━━ Meta Ads ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Conta:     [nome da conta]
  Seguranca: Tudo certo — compliance ativo
  Modo:      Somente leitura

  Consumo da API:
  ░░░░░░░░░░░░░░░░░░░░ 0%
  Pode fazer ~60 consultas e ~20 alteracoes nesta hora
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Usar linguagem leiga: "consultas" (não reads), "alteracoes" (não writes), "consumo" (não BUC).

---

## BARRA DE CONSUMO (durante o uso)

Após CADA chamada à API, mostrar:

```
Consumo: ████░░░░░░░░░░░░░░░░ 22% — 47 consultas restantes
```

Quando desacelerando (60%+):
```
Consumo: ████████████░░░░░░░░ 62% — Desacelerando para proteger a conta
```

Quando pausado (80%+):
```
Consumo: ████████████████░░░░ 83% — Pausado por seguranca (~3 min para liberar)
```

Após alteração:
```
Consumo: ████████░░░░░░░░░░░░ 38% (+1 alteracao) — 37 consultas | 12 alteracoes restantes
```

---

## NUNCA FAZER

1. **Nunca retentar após erro de abuso (613/0 ou 613/1996)** — retentar faz a Meta aumentar o tempo de bloqueio e pode escalar pra ban permanente
2. **Nunca continuar chamadas após atingir limite** — a Meta diz explicitamente que continuar AUMENTA o tempo de recuperação
3. **Nunca usar token pessoal** — tokens pessoais expiram em horas e amarram ao perfil pessoal do Facebook; se banir, perde o perfil inteiro
4. **Nunca deixar AI escrever sem aprovação humana** — todos os bans confirmados envolveram writes automáticos sem supervisão
5. **Nunca automatizar mudanças de budget em velocidade de máquina** — o sistema de detecção de fraude flagra edições rápidas como comportamento de bot
6. **Nunca usar automação de browser** — Playwright/Selenium triggera detecção de bot e viola os Platform Terms
7. **Nunca expor tokens em logs** — violação dos Platform Terms Section 6 e risco de roubo de credenciais
8. **Nunca criar e deletar campanhas rapidamente** — padrão clássico de fraude que o integrity system detecta
9. **Nunca fazer chamadas paralelas em múltiplas contas** — fan-out queima rate limit de todas as contas ao mesmo tempo
10. **Nunca operar sem appsecret_proof** — sem ele, qualquer pessoa com o token pode fazer chamadas se passando pelo app

---

## SEMPRE FAZER

1. **Usar System User tokens** — não expiram, são vinculados ao Business Manager (não ao perfil pessoal), e são o tipo recomendado pela Meta
2. **Monitorar headers de rate limit em toda resposta** — os 4 headers (X-Business-Use-Case-Usage, X-Ad-Account-Usage, X-App-Usage, X-FB-Ads-Insights-Throttle) dizem exatamente quanto da cota foi consumida
3. **Enviar appsecret_proof em toda request** — prova criptográfica de que a request veio do seu servidor, não de um token roubado
4. **Validar parâmetros antes de enviar** — erros HTTP 400 reduzem ativamente a cota de rate limit pela fórmula da Meta
5. **Usar backoff exponencial com jitter nos retries** — evita thundering herd (múltiplos retries simultâneos que pioram a situação)
6. **Logar toda operação de escrita com audit trail** — forensic trail protege em caso de apelação
7. **Processar contas sequencialmente** — uma de cada vez, nunca em paralelo, pra não parecer um scraper

---

## ALTERAÇÕES — Fluxo obrigatório

Toda alteração (criar, mudar, pausar, deletar) segue este fluxo:

```
1. PROPOR  → Mostrar o que vai mudar (estado atual vs proposto)
2. CONFIRMAR → Usuário aprova explicitamente
3. EXECUTAR → Enviar a chamada
4. REGISTRAR → Logar no audit trail
5. MOSTRAR  → Atualizar barra de consumo
```

Sem confirmação, NÃO executar. Isso é o que diferencia operadores que foram banidos (writes automáticos) dos que operam há 18 meses sem problemas (writes com aprovação humana).

### Classificação de risco

| Risco | Operações | Política |
|-------|-----------|----------|
| Baixo | Pausar, arquivar, gerar preview | Confirmação simples |
| Médio | Mudar budget, bid, targeting, ativar | Confirmação + log antes/depois |
| Alto | Criar ads/campanhas, upload criativos, deletar | Confirmação explícita + revisão |
| Proibido | Configurações de conta, pagamentos, permissões | NÃO expor |

### Limites

- Mudanças de budget: **4/hora por adset** — passar disso bloqueia mudanças naquele adset por 1 hora
- Mudanças de spend limit: **10/dia** — limite diário absoluto
- Alterações: **somente horário comercial** (seg-sex 8-20h) — operações fora desse horário são sinais de bot pra detecção de fraude

---

## ERROS — Referência rápida

### PARAR TUDO:
- `613/0` — Detecção de abuso
- `613/1996` — Anomalia comportamental

### ESPERAR E TENTAR DE NOVO:
- `4`, `17`, `32` — Rate limit
- `80000-80014` — Limites por tipo de uso

### NÃO TENTAR DE NOVO:
- `190` — Token expirado → gerar novo
- `100` — Parâmetro inválido → corrigir

Para tabela completa, ver `references/error-codes.md`.

---

## PADRÃO ZENTRIC (18 meses, 0 bans)

Modelo operacional comprovado por agência real (Zentric Digital) com 1.279 operações em 5 contas de clientes:

- Consultas são autônomas — AI lê livremente com rate limiting
- Alterações sempre com aprovação humana
- Polling máximo 1x/hora durante horário comercial
- Pausar em 60% de consumo
- Toda request logada

O rep da Meta confirmou diretamente pra eles:
> "A Meta não bane contas por usar AI. Bane contas cujo código viola rate limits, ignora sinais de integridade, ou quebra políticas de anúncios."

---

## 5 Regras Anti-Ban para Automação (Standard+ Access)

Quando o usuário pedir pra automatizar alguma operação Meta Ads (auto-pause, auto-scale, day-parting, polling, AI agent contínuo, dashboards real-time), **APLICAR essas 5 regras como guard rails obrigatórios**. Pesquisa multi-source confirma que apps que seguem isso passam ileso pelo ban-wave de 2025-2026.

### Regra 1 — Polling ≥ 5 minutos
Nunca tight loop (segundos ou poucos minutos). Meta's próprio ad-rules engine roda a cada 30-60min — copie a cadência. Auto-refresh dashboard: mínimo 5min, ideal 10-15min.

### Regra 2 — Writes só em horário comercial
8h-20h horário local. Mudanças de budget/status às 3am = sinal de bot. Day-parting (pause/resume agendado) é exceção OK porque é exatamente 2 writes/dia, padrão humano.

### Regra 3 — HITL obrigatório em 4 ações
- Criar/publicar criativo (conteúdo é #1 trigger de policy violation)
- Aumentar budget > 20% (Meta cap recomendado é +15% / 48h)
- Cross-account budget rebalance (move dinheiro entre BMs)
- Criar campanha nova

Auto-pause de underperformer e auto-scale conservador (+15% max 1x/dia) podem rodar sem HITL.

### Regra 4 — Pausar polling em 60% BUC
Inspecionar header `X-Business-Use-Case-Usage` em toda response. Se utilização > 60% em qualquer counter, pausar polling daquele account até o reset window. Nunca chegar perto de 80%, muito menos 100%.

### Regra 5 — Audit log append-only
Toda operação (read e write) loga: timestamp, operation, resource_id, before_state, after_state, user_confirmed. Se Meta perguntar, você prova uso legítimo — sem isso, ban appeal é impossível.

### Por que essas regras funcionam

O ban-wave 2025-2026 (casos Claude Code, Openclaw, Manus) atingiu apps com **combinação** de:
- Token mal configurado / app sem App Review
- Polling tight (queries em segundos)
- Budget changes 3am sem revisão
- Criativos AI publicados sem human review
- MCP unofficial / browser session token

Apps que seguem as 5 regras acima falham em **zero** desses triggers. Padrão Zentric Digital (5 contas, 1.279 ops/mês, 18 meses 0 bans) usa exatamente esse modelo.

### Anti-pattern explícito

Nunca propor ao usuário:
- ❌ Polling sub-minuto
- ❌ Auto-publish criativo sem human review
- ❌ Mudanças fora horário comercial em alta velocidade
- ❌ Retry storm em erro 613/429 (sempre exponential backoff)

---

## Skills relacionadas

- **`meta-app-review-approval`** — Para o gate único de aprovação no Meta App Review (Ads Management Standard Access e similares). Esta skill aqui cobre operação contínua; aquela cobre o processo de submissão pra ganhar acesso de produção.

  **GATILHO IMPORTANTE:** Se identificar que `ads_api_access_tier == "development_access"` ou `max_points == 60` no header `X-Business-Use-Case-Usage`, o app está no tier de desenvolvimento (60 pts/h). Isso esgota em segundos durante operação real. **Avise o usuário** que ele deve passar pelo App Review pra ganhar Standard Access (9.000 pts/h, 150x mais quota), e referencie a skill `meta-app-review-approval` que tem o workflow completo de aprovação na primeira tentativa (~2 horas de análise da Meta).
