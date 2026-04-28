# Form Fields Reference

The Meta App Review submission has 4 phases. Recommended answers for each field, based on what passed review on the first try for an internal first-party tool.

## Phase 1 — Verificação (Verification)

Mostly auto-completed if Business Manager is verified. Nothing to fill manually here unless prompted for missing docs.

## Phase 2 — Configurações do app (App Settings)

Confirms the app's basic configuration. These come from App Dashboard → Settings → Basic.

| Field | What to use |
|-------|-------------|
| **Privacy Policy URL** | `https://YOUR-MARKETING-DOMAIN/privacy-or-terms-page/` — must respond 200 OK from a clean browser. Same parent domain as the business is fine even if app lives on a subdomain. |
| **User Data Deletion** | Same URL as Privacy Policy if the policy contains a deletion section. Otherwise: dedicated `/data-deletion` page or instructions text like `"Email contato@... to request deletion"`. |
| **Site URL** | The **business marketing site**, not the app dashboard. Reviewers use this to validate the entity exists. |
| **App Domains** | List domains used by the app (e.g., `meta.escoladeautomacao.com.br`). |
| **App Type** | Empresa (Business) — gives access to the right permission set. |
| **App Mode** | Live (not Development) — required for App Review. |

## Phase 3 — Uso permitido (Permitted Use)

Two sub-tabs: **Requests** (new permissions) and **Renewal** (annual re-confirmation of existing permissions).

For **Renewal** of basic auto-granted permissions (`public_profile`, `email`):

- ☑ "Certifico que todo e qualquer uso de **public_profile** está dentro do permitido"
- ☑ "Certifico que todo e qualquer uso de **email** está dentro do permitido"

These are auto-granted to every app and the checkbox just affirms intent. Even if your app uses System User and never sees end-user OAuth, it's safe to check — you're affirming "if I use it, I'll use it within scope".

## Phase 4 — Tratamento de dados (Data Handling)

The 5 questions under this phase. Recommended answers for an internal first-party tool:

### processor-0 — Has data processors?

> "Você tem operadores de dados ou provedores de serviços (incluindo as próprias empresas) que terão acesso aos Dados da Plataforma que você obtém da Meta?"

**Não** — internal tool, no third-party processors handling Meta data on your behalf.

(For SaaS: probably **Sim** if you use AWS/Vercel/etc. that handle the data — but check legal interpretation.)

### responsible-1 — Who is responsible?

> "Quem é a pessoa ou a entidade que será responsável por todos os Dados da Plataforma que a Meta compartilha com você?"

**Your business legal name** — match the privacy policy. E.g., "Escola de Automação e IA".

### responsible-2 — Country?

Country where the responsible entity is registered.

### requests-3 — Provided data to public authorities for national security in last 12 months?

> "Você forneceu dados pessoais ou informações pessoais de usuários a autoridades públicas em resposta a solicitações de segurança nacional nos últimos 12 meses?"

**Não** — unless you literally have, in which case answer truthfully.

### requests-4 — Which processes apply to public authority requests?

⚠️ **DO NOT mark "Nenhuma das opções acima"**. Even if you've never received such a request, marking "none" signals low compliance maturity to the reviewer.

Mark at least these 2:

- ☑ **Análise obrigatória sobre a legitimidade das solicitações**
- ☑ **Política de minimização de dados: a capacidade de divulgar o mínimo de informações conforme a necessidade**

These are LGPD/GDPR baseline practices that any responsible business follows by default. If your privacy policy mentions LGPD compliance, marking these is consistent.

Optional adds (mark if you actually do them):
- Disposições para contestar os pedidos considerados ilegais
- Registro dessas solicitações, incluindo as respostas, o raciocínio legal e as pessoas envolvidas

## Phase 5 — Instruções para o analista (Analyst Instructions)

The free-text textbox where you tell the reviewer how to test your app. Use the template in `assets/instructions-web-2-template.txt`.

Critical content:
- State the app is internal/first-party (so reviewer knows not to expect end-user OAuth flow)
- Mention the live app URL (separate from the Site URL on Settings)
- Explain auth model — System User token + appsecret_proof
- Reference the screencast and what it demonstrates
- List the ad account IDs covered

Optional fields you can leave blank for an internal tool:

- **accesscode-web-1** (test credentials for paywall) — N/A
- **accesscode-web-2** (cortesia codes for app store) — N/A
- **geo-web-5** (geographic restrictions) — N/A unless you actually geofence
- **documents-web-1** (supporting docs) — N/A, screencast is uploaded separately
