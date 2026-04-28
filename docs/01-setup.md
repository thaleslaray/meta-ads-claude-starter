# 01 — Setup (15min)

Criar app Meta + tokens + configurar variáveis. Esse é o pré-requisito de tudo.

## 1. Criar app no Meta for Developers

1. Acesse https://developers.facebook.com/apps
2. Clique em **Create App**
3. Caso de uso: **Other → Empresa** (mostra as permissões certas)
4. Anote o **App ID** (numérico, ex: `344941004274813`)

## 2. Adicionar produto Marketing API

No painel do app:
1. **Add Product** → **Marketing API**
2. **Settings → Basic** do app:
   - **App Secret**: clique em "Show" e copie (precisa da senha do FB)
   - **Privacy Policy URL**: URL pública que responde 200 OK (pode ser do site marketing)
   - **App Domains**: domínio onde o dashboard vai rodar (ex: `meta.seudominio.com.br`)

## 3. Verificar Business Manager

No https://business.facebook.com:
1. Settings → Business Info
2. Anote o **Business ID** (numérico)
3. Confirme que o BM está **verified** (check verde)

Se não está verificado, faça verificação de business primeiro — sem isso o App Review é rejeitado.

## 4. Gerar System User token

No Business Settings:
1. **Users → System Users → Add**
   - Nome: "Meta Ads Dashboard"
   - Role: **Admin**
2. **Add Assets** ao System User:
   - Adicione o **app** que você criou (with Manage permission)
   - Adicione cada **ad account** que quer gerenciar (with Manage permission)
3. **Generate New Token**:
   - App: o app que você criou
   - Permissions: marque **`ads_management`** + **`ads_read`** + **`business_management`**
   - Token expiration: **Never** (System User tokens são longos por design)
4. Copie o token — você não vai poder ver de novo

## 5. Listar suas ad accounts

Via Graph API Explorer (https://developers.facebook.com/tools/explorer/):

```
GET /me/adaccounts?fields=id,name
```

Use o System User token. Anote os IDs de cada account que quer gerenciar (formato `act_xxxxxxxxxx`).

## 6. Preencher .env

```bash
cp .env.example .env
```

Edite `.env`:

```
META_ACCESS_TOKEN=EAAXxx...   # System User token do passo 4
META_APP_SECRET=abc123...     # App Secret do passo 2
META_BM_ID=1234567890         # Business ID do passo 3
META_AD_ACCOUNTS=[{"id":"act_xxx","name":"Conta Principal","label":"Main"},{"id":"act_yyy","name":"Conta Teste","label":"Test"}]
ORG_NAME=Sua Empresa
```

Ou rode o setup interativo que valida cada campo:

```bash
./scripts/setup.sh
```

## 7. Testar localmente

```bash
cd dashboard
npm install
pip install -r requirements.txt
npm run dev
# em outra aba:
cd dashboard/api && uvicorn index:app --reload --port 8000
```

Abra http://localhost:3000. Se aparecer suas contas, deu certo.

## Próximo passo

→ [02-deploy.md](./02-deploy.md) — Deploy na Vercel
