# 02 — Deploy na Vercel (15min)

Deploy do dashboard pra produção. Necessário pra App Review (Meta precisa de URL pública).

## Pré-requisitos

- `.env` configurado (ver [01-setup.md](./01-setup.md))
- Conta Vercel (free tier funciona)
- Vercel CLI: `npm install -g vercel`

## 1. Login na Vercel

```bash
cd dashboard
vercel login
```

## 2. Link do projeto

```bash
vercel link
# - Set up and deploy: Y
# - Scope: sua conta pessoal ou org
# - Link to existing project: N
# - Project name: meta-ads-dashboard
# - Directory: ./ (já está em dashboard/)
```

## 3. Configurar env vars no Vercel

Cada variável do `.env` local precisa ir pra Vercel:

```bash
vercel env add META_ACCESS_TOKEN production
# cola o token, enter
vercel env add META_APP_SECRET production
vercel env add META_BM_ID production
vercel env add META_AD_ACCOUNTS production
vercel env add ORG_NAME production
```

**Atenção:** ao adicionar `META_APP_SECRET`, garanta que **NÃO** tem espaço/quebra de linha no final. Use `printf` se necessário:

```bash
printf "%s" "abc123secretsemquebra" | vercel env add META_APP_SECRET production
```

## 4. Deploy

```bash
vercel --prod
```

Saída final dá uma URL `https://meta-ads-dashboard-xxx.vercel.app`. Abra e teste.

## 5. (Opcional) Custom domain

No dashboard Vercel → Settings → Domains:
1. Add `meta.seudominio.com.br`
2. Configure DNS conforme instruções (CNAME ou A record)
3. Aguarde SSL (automático)

URL recomendada: subdomínio do site marketing (ex: `meta.escoladeautomacao.com.br`). Mantém na mesma "marca" pra App Review aceitar Privacy Policy do domínio principal.

## 6. Smoke test

```bash
# Deve retornar 200 com lista de contas
curl https://seu-dominio/api/accounts
```

Resposta esperada:
```json
{"accounts":[{"id":"act_xxx",...}],"bm_id":"...","org_name":"Sua Empresa"}
```

## Troubleshooting

| Erro | Fix |
|------|-----|
| `META_AD_ACCOUNTS env var is required` | Adicionar a env var na Vercel + redeploy |
| `Invalid appsecret_proof` | App Secret tem espaço no final — re-add com `printf` |
| Vercel Auth bloqueando acesso | Settings → Deployment Protection → desativar |

## Próximo passo

→ [03-app-review.md](./03-app-review.md) — Submeter App Review
