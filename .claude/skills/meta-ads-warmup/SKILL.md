---
name: meta-ads-warmup
description: >
  Acumula chamadas de API para desbloquear Advanced Access na Meta.
  TEMPORÁRIA — descarte após conseguir Advanced Access.
  Usar quando o usuário mencionar warmup, health report, advanced access,
  desbloquear meta, 1500 calls, rodar warmup, subir de tier,
  development access, standard access, pontos da meta, 60 pts,
  9000 pts, ou quiser aumentar o limite de chamadas da API.
metadata:
  author: thaleslaray
  version: 1.1.0
---

# Meta Ads Warmup — Desbloqueio de Advanced Access

Skill temporária para acumular as 1.500 chamadas necessárias para
desbloquear o Advanced Access (9.000 pts/hora vs 60 pts/hora atual).

## O que é Advanced Access

A Meta limita apps novos a 60 pontos por hora (cada consulta gasta 1,
cada alteração gasta 3). Um AI agent esgota isso em segundos. O Advanced
Access sobe pra 9.000 pontos — suficiente pra qualquer uso normal.

Pra desbloquear, a Meta exige 1.500 chamadas bem-sucedidas em 15 dias
com menos de 10% de erro. O dashboard que mostra o progresso é bugado
(bugs oficiais 856507118038187, 2153428708045063).

## Como rodar

Quando o usuário pedir pra rodar o warmup ou health report:

1. Navegar até o diretório do projeto meta-ads-mcp
2. Verificar que `META_ACCESS_TOKEN` e `META_APP_SECRET` estão configurados
3. Executar o health report no nível desejado:

```bash
# Report rápido (~30 chamadas, ~2 min)
uv run python scripts/warmup.py --depth quick --save

# Report padrão (~100 chamadas, ~5 min) — recomendado pra uso diário
uv run python scripts/warmup.py --depth standard --save

# Report completo (~200 chamadas, ~15 min)
uv run python scripts/warmup.py --depth deep --save

# Checar status do tier atual
uv run python scripts/warmup.py --status
```

4. Após rodar, reportar ao usuário:
   - Quantas chamadas foram feitas (total e por tipo BUC)
   - Taxa de erro
   - Quantas chamadas `ads_management` (as que provavelmente contam)

## Agendamento diário

Se o usuário quiser agendar pra rodar todo dia automaticamente, configurar
o cron local com `crontab -e`. O horário recomendado é 9h (horário de SP).

## Se o botão não destravar

O dashboard da Meta é bugado e o contador pode não refletir as chamadas reais.

1. No Graph API Explorer, trocar o app no dropdown pro app do usuário (não usar o app "Graph API Explorer")
2. Gerar token com ads_management e ads_read
3. Fazer algumas chamadas: `/act_xxx/campaigns`, `/act_xxx/adsets`, `/act_xxx/ads`
4. Com a sessão ativa, abrir a página de App Review do app
5. Esperar 24h — o dashboard tem delay
6. Se nada mudar em 2 semanas → abrir bug report

## Quando descartar esta skill

Quando o header `X-Business-Use-Case-Usage` retornar
`ads_api_access_tier: "standard_access"`, a skill cumpriu seu papel.
O usuário pode deletar a pasta da skill.
