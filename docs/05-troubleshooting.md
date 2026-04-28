# 05 — Troubleshooting

Erros comuns + fixes. Ordem aproximada: setup → deploy → app review → operação.

## Setup

### `META_AD_ACCOUNTS env var is required`

A variável não foi definida ou tem JSON inválido.

```bash
# Verifique:
echo $META_AD_ACCOUNTS

# Formato correto (sem espaço entre as chaves):
export META_AD_ACCOUNTS='[{"id":"act_xxx","name":"Main","label":"Principal"}]'
```

### `Invalid OAuth access token` ao fazer chamada

Token expirado ou de outro app. System User tokens NÃO expiram — se está expirado, é porque você usou um token de usuário comum por engano.

```bash
# Regenere via Business Settings → System Users → Generate New Token
# Selecione o app correto + permissions ads_management + ads_read
```

### `Invalid appsecret_proof`

App Secret tem espaço ou quebra de linha no final.

```bash
# Re-add sem newline:
printf "%s" "seu_app_secret_real" | vercel env add META_APP_SECRET production
vercel --prod  # redeploy pra pegar a env var nova
```

## Deploy

### Vercel mostra "Auth Required" em todas as páginas

Deployment Protection ativado. Desative em Settings → Deployment Protection → Disable.

### `/api/accounts` retorna 500

Provavelmente env vars faltando ou inválidas. Veja logs:

```bash
vercel logs --since 5m
```

### Dashboard carrega mas tabelas vazias

Sua System User não tem acesso às ad accounts listadas. Volta no Business Settings → System Users → adiciona as accounts ao System User com role Manage.

## App Review

### "Unable to verify use case experience"

#1 razão de rejeição. Solução: re-record com caption explícita de System User auth nos primeiros 4s do video.

```
"Internal dashboard — auth via server-side System User token (no end-user OAuth)"
```

### "Privacy policy URL not accessible"

URL retornou 404 ou demorou. Teste:

```bash
curl -I https://seu-dominio/privacy
# deve retornar HTTP/2 200
```

Se retorna 404, configure no app dashboard com URL real do site marketing (ex: `https://www.escoladeautomacao.com.br/termos-uso-privacidade/`).

### Tier ainda dev após aprovação

Cache do rate_limiter local. Faça 1 chamada real:

```bash
./scripts/verify-tier.sh act_xxx https://seu-dominio
```

Se persiste 1h+ após aprovação, abra ticket suporte Meta.

## Operação

### Erro 613 (Throttled)

Você passou o rate limit. O rate_limiter local já trata, mas se está vendo isso no console:

```
# 1. Pause polling daquela conta por 1h
# 2. Reduza frequência de queries
# 3. Use batch APIs em vez de N queries pequenas
```

### Erro 17 (User request limit reached)

Mesmo de cima, mas no nível user. Espera reset window (geralmente 1h).

### Erro 100 (Invalid parameter)

API call malformada. Veja `audit_logs/` pra payload completo da request que falhou.

### Erro 190 (Token invalid)

Token foi revogado ou expirado (raro com System User). Regenerar.

### Dashboard não atualiza após write

SWR cache. Refresh manual da página, ou aguarde 30s pro auto-revalidate.

### "Meta rejected the update" em budget change

Provável causa: campanha usa Ad Set Budget Optimization (ABO). Budget precisa ser ajustado no nível ad set, não campaign.

```bash
# Veja se a campanha tem daily_budget:
curl "https://seu-dominio/api/account/act_xxx/campaigns" | jq '.campaigns[] | select(.id=="ID") | .daily_budget'
# Se for null, é ABO — ajuste no Meta Ads Manager
```

## Suporte

Se nenhum desses fix resolveu:

1. Procure em [GitHub Issues](https://github.com/thaleslaray/meta-ads-claude-starter/issues) (talvez já foi reportado)
2. Abra novo Issue com:
   - Comando exato que rodou
   - Erro completo (não corte)
   - Output de `vercel logs --since 30m`
   - **NUNCA** inclua `META_ACCESS_TOKEN` ou `META_APP_SECRET` no Issue
