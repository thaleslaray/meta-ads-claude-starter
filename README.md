# Meta Ads + Claude Code Starter

> Boilerplate testado pra passar pelo Meta App Review na primeira tentativa e ganhar **Standard Access** (9.000 chamadas/h em vez de 60).

[![v1.0.1](https://img.shields.io/badge/version-1.0.1-blue)](https://github.com/thaleslaray/meta-ads-claude-starter/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---

## ⚠️ ANTES DE COMEÇAR: você precisa MESMO disso?

**90% das pessoas que pensam que precisam deste repo, na verdade não precisam.** Vamos descobrir se você é dos 10%.

### Pergunta única: você quer LER ou ESCREVER?

| O que você quer fazer | Exemplos | Solução |
|----------------------|----------|---------|
| **Só LER** dados das suas campanhas | "Quanto gastei essa semana?", "Qual campanha tem o melhor ROAS?", "Mostra meu CTR comparado com o mês passado" | 🟢 **Use Windsor.ai** (5min, sem App Review) — [pula pra explicação ↓](#-caso-1--você-só-quer-ler-dados) |
| **ESCREVER** mudanças nas campanhas | "Pausa essa campanha", "Aumenta o budget pra R$ 500", "Cria uma campanha nova" | 🔴 **Use este repo** (precisa de App Review) — [pula pra explicação ↓](#-caso-2--você-quer-escrever-precisa-deste-repo) |
| **Ambos** | Algumas leituras + algumas escritas | 🔴 Use este repo (cobre os 2 casos) |

> **Por que essa diferença existe?** A Meta cobra do seu app uma "moeda" chamada *pontos*. Cada **leitura** custa 1 ponto, cada **escrita** custa 3 pontos. No tier inicial (chamado *Development Access*) você tem só **60 pontos por hora** — esgota em segundos. O **Windsor.ai já passou pelo App Review** deles, então você usa a quota DELES (que é gigante). Mas eles só permitem leitura. Pra escrever, você precisa do SEU próprio app aprovado pela Meta.

---

## 🟢 CASO 1 — Você só quer LER dados

**Boa notícia:** você não precisa deste repo. Você não precisa criar app na Meta. Você não precisa passar por App Review. Tudo isso é dor de cabeça desnecessária pra você.

### O que usar: Windsor.ai + Claude

[Windsor.ai](https://windsor.ai) é uma empresa que conecta com Meta Ads (e Google Ads, TikTok, etc.) e te dá acesso aos dados via uma API que **já passou pelo App Review da Meta** — você herda a aprovação deles.

Eles têm um **MCP oficial integrado ao Claude.ai**, então é só:

1. **Cria conta gratuita** em https://windsor.ai (3 min)
2. **Conecta sua conta Meta Ads** clicando em "Add Connector → Facebook Ads" (1 min, faz o OAuth)
3. **Vai pro Claude.ai** (não Claude Code, é a versão web/app)
4. **Conecta o Windsor.ai** em Settings → Connectors → Windsor.ai
5. **Pergunta o que quiser:**
   - "Quanto gastei em Meta Ads essa semana?"
   - "Compara o CTR das minhas 3 contas"
   - "Quais campanhas têm CPA > R$ 50?"

**Pronto.** Você tá fazendo análise de Meta Ads via Claude sem ter mexido em nenhuma linha de código. Custo: zero (free tier do Windsor cobre uso pessoal).

> 💡 **Quando o Windsor não basta?** Quando você quer **mudar** alguma coisa (pausar campanha, mudar budget). Nesse caso volta aqui em cima e segue o **Caso 2**.

---

## 🔴 CASO 2 — Você quer ESCREVER (precisa deste repo)

Se você confirmou que precisa fazer mudanças nas campanhas via API (não só ler), então segue. Esta é a parte difícil — vou te guiar passo a passo.

### A história do problema

A Meta tem dois "tiers" de acesso pra Marketing API:

| Tier | Quota | Quem tem |
|------|-------|----------|
| **Development Access** (padrão) | 60 chamadas/h | Todo app novo começa aqui |
| **Standard Access** (precisa aprovação) | 9.000 chamadas/h | Apps que passaram pelo App Review |

60 chamadas por hora **esgota em segundos** quando você tá automatizando. É como se você tivesse um carro com tanque de 1 litro de combustível.

Pra ganhar Standard Access (150x mais quota), você precisa **convencer um humano da Meta** que seu app é legítimo e bem feito. Esse processo é o **Meta App Review**.

### Por que App Review é difícil

Meta recebe **milhares de submissões por dia**. O reviewer dá ~5 minutos pra cada app. Se em 5 minutos ele não entende o que você faz, **rejeita sem ler direito**.

Os 90% que são rejeitados na primeira tentativa caem porque:
- Descrição confusa ou genérica ("nosso app otimiza ads") — reviewer não entende o que é específico
- Vídeo demo mal feito (sem captions, fora de foco, mostrando coisa errada)
- Forms mal preenchidos ("none of the above" em campos que pedem maturidade de compliance)
- URL de privacidade quebrada (404)
- Tentativas óbvias de "burlar o sistema" (auto-publicar criativos sem revisão humana)

### O que este repo entrega

A **fórmula testada que aprovou em 2 horas na primeira tentativa** quando submetemos pra app `meta.escoladeautomacao.com.br` em abril/2026.

Encapsulada em:
1. **Dashboard pronto** — você não precisa construir UI nenhuma. Só configura 5 variáveis e deploya. Esse dashboard é o "objeto" que o reviewer vai analisar no vídeo.
2. **Skills do Claude Code** — quando você abre o projeto no Claude Code, ele já carrega 3 skills (`meta-ads-compliance`, `meta-ads-warmup`, `meta-app-review-approval`) que te guiam em cada passo.
3. **Templates** — descrição, instruções pro analista, captions Netflix-style do vídeo, todos prontos pra adaptar.
4. **Documentação detalhada** — 5 docs cobrindo setup → deploy → app review → operação → troubleshooting.

### Resultado típico (com este repo)

| Métrica | Sem este repo | Com este repo |
|---------|---------------|---------------|
| Tentativas até aprovação | 3-10 | 1 |
| Tempo total | 2-8 semanas | 2h-3 dias |
| Tempo seu (de trabalho ativo) | 10-20h | 30 min |

---

## ✅ Pré-requisitos (caso 2)

Antes de clonar o repo, garanta que tem TUDO isso. Se faltar 1, não adianta começar:

### Coisas da Meta

- [ ] **Conta no Business Manager** — https://business.facebook.com
- [ ] **Business Manager VERIFICADO** (selo verde nas Settings → Business Info)
  - **O que é:** Meta confirma que você é uma empresa real (CNPJ + endereço + telefone)
  - **Como fazer:** Business Settings → Security Center → Business Verification → segue o passo-a-passo (precisa de comprovante de empresa, ex: contrato social)
  - **Por que importa:** **App Review é AUTOMATICAMENTE rejeitado** se o BM não tá verificado, antes mesmo de um humano olhar
- [ ] **App criado** em https://developers.facebook.com/apps com use case "Other → Empresa"
- [ ] **Marketing API** adicionado como produto no app
- [ ] **Privacy Policy URL pública** configurada no app
  - **O que é:** uma página tipo `seusite.com/privacidade` explicando como você trata dados
  - **Onde por:** App Settings → Basic → Privacy Policy URL
  - **Pode usar:** se você já tem site institucional com política de privacidade, usa essa URL. Se não tem, gera uma rápida no Termly.io ou similar.

### Tokens (você vai colar isso no setup do repo)

Anote esses 3 valores:

| Onde achar | O que copiar | Parece com |
|------------|--------------|------------|
| Business Settings → Users → System Users → "Generate New Token" | `META_ACCESS_TOKEN` | `EAAXxxxxxxxxxxxxxxxxxxxxxx...` (200+ caracteres) |
| App Settings → Basic → App Secret (clica "Show", coloca senha do FB) | `META_APP_SECRET` | `abc123def456...` (32 caracteres) |
| Business Settings → Business Info → "ID da empresa" | `META_BM_ID` | `1234567890` (numérico) |

> ⚠️ **MUITO IMPORTANTE sobre o token:** ao gerar o System User token, marque essas 3 permissões: `ads_management`, `ads_read`, `business_management`. E define a expiração como "Never" (System User tokens não expiram, é normal).

### Stack local

- [ ] **Node.js 20+** — testa: `node --version` (se não tem, baixa em https://nodejs.org)
- [ ] **Python 3.11+** — testa: `python3 --version` (Mac já vem, Windows baixa em https://python.org)
- [ ] **Git** — testa: `git --version`
- [ ] **Claude Code** — testa: `claude --version` (instala em https://docs.anthropic.com/claude-code)
- [ ] **Conta Vercel** (gratuita) + CLI: `npm install -g vercel`

---

## 🔄 Como funciona (visão geral)

```
┌─────────────────────────────────────────────────────────────┐
│  FASE 1: SETUP (15min)                                      │
│  Clone repo + tokens + .env                                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 2: DEPLOY (15min)                                     │
│  Vercel deploy → URL pública pra reviewer testar            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 3: APP REVIEW (2h-3 dias)                             │
│  Gravar screencast no dashboard + form + submit             │
│  Skill `meta-app-review-approval` te guia passo-a-passo     │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  FASE 4: APROVADO! Standard Access ativo (9.000/h)          │
│  Operação contínua via Claude Code + MCP                    │
│  Dashboard pode ser desligado (cumpriu seu papel)           │
└─────────────────────────────────────────────────────────────┘
```

### ⚠️ MUITO IMPORTANTE: O dashboard é DEMO, não ferramenta de uso diário

O dashboard incluso (Next.js + FastAPI) tem **um único propósito**: ser a prova visual de funcionamento que você grava no vídeo pro Meta App Review.

**Após aprovado:**
- ✅ Você pode **desligar o Vercel** (economia de recursos)
- ✅ Sua operação real do dia-a-dia vira via **Claude Code + MCP `meta-ads-mcp`**, não pelo dashboard
- ✅ Se quiser manter o dashboard pra acessar via celular sem terminal, tudo bem — mas não é necessário

Pensa assim: o dashboard é o **portfolio que você mostra pro empregador na entrevista**. Depois de contratado, você não usa o portfolio mais — usa as ferramentas reais do trabalho.

---

## 🚀 Quickstart 30 minutos (passo-a-passo)

### Passo 1 — Clone o repo (1min)

Abre o terminal:

```bash
git clone https://github.com/thaleslaray/meta-ads-claude-starter
cd meta-ads-claude-starter
```

### Passo 2 — Liste suas ad accounts (5min)

Antes de rodar o setup, você precisa saber os IDs das contas que vai gerenciar.

1. Abre https://developers.facebook.com/tools/explorer/
2. Seleciona seu app no dropdown do canto direito
3. Cola no campo de query: `me/adaccounts?fields=id,name`
4. **Importante:** clica em "Get Token" → "Get User Access Token" e seleciona as permissions `ads_read` e `ads_management`. (Esse token é só pra fazer essa consulta agora, NÃO é o token do passo 3.)
5. Clica **Submit**

Você vai ver lista tipo:

```json
{
  "data": [
    {"id": "act_487731909607599", "name": "Conta Principal"},
    {"id": "act_708497467651098", "name": "Conta Teste"}
  ]
}
```

Anota os IDs (formato `act_xxxxxxxxx`) — você vai colar no próximo passo.

### Passo 3 — Setup interativo (5min)

```bash
./scripts/setup.sh
```

O script vai te perguntar uma coisa por vez. Cola cada valor:

```
META_ACCESS_TOKEN (System User token): EAAxxx...
META_APP_SECRET: abc123...
META_BM_ID (numeric Business Manager ID): 1234567890
ORG_NAME (your business name): Minha Empresa LTDA

Add ad account? (y/N) y
  Account ID (act_xxx): act_487731909607599
  Account name: Conta Principal
  Short label: Main

Add ad account? (y/N) y
  Account ID (act_xxx): act_708497467651098
  Account name: Conta Teste
  Short label: Test

Add ad account? (y/N) n

✓ .env written (2 accounts configured)
```

Ele cria o arquivo `.env` na raiz. **Esse arquivo tem segredos, NUNCA commita no git** (já tá no `.gitignore`).

### Passo 4 — Teste local (5min)

Pra confirmar que tudo funciona antes de subir pra Vercel:

```bash
cd dashboard
npm install              # baixa dependências do Next.js (~30s)
pip install -r requirements.txt  # baixa dependências do Python (~10s)
```

Abre **2 abas** do terminal:

**Aba 1 — backend Python:**
```bash
cd dashboard/api
uvicorn index:app --reload --port 8000
```

**Aba 2 — frontend Next.js:**
```bash
cd dashboard
npm run dev
```

Abre http://localhost:3000 no navegador. **Você deve ver:**
- ✅ Suas contas no dropdown do header
- ✅ Insights (se as contas têm gastos recentes)
- ✅ Lista de campanhas

Se NÃO funcionar, lê [docs/05-troubleshooting.md](./docs/05-troubleshooting.md). Erros mais comuns:
- "META_AD_ACCOUNTS env var is required" → o `.env` tá errado
- "Invalid OAuth access token" → token errado ou expirado
- "Invalid appsecret_proof" → App Secret tem espaço no final

### Passo 5 — Deploy Vercel (5min)

Vamos colocar isso no ar pra Meta poder acessar:

```bash
cd dashboard
vercel login    # primeira vez: vai abrir navegador pra fazer login
vercel link     # primeira vez: aceita criar projeto novo
```

Agora adiciona cada variável de ambiente (uma por uma):

```bash
vercel env add META_ACCESS_TOKEN production
# cola o token quando pedir, enter

vercel env add META_APP_SECRET production
# cola o secret, enter

vercel env add META_BM_ID production
# cola o BM ID, enter

vercel env add META_AD_ACCOUNTS production
# cola o JSON inteiro, enter
# (pega do seu .env, é o valor de META_AD_ACCOUNTS)

vercel env add ORG_NAME production
# cola o nome, enter
```

Agora deploy:

```bash
vercel --prod
```

No final aparece a URL: `https://meta-ads-dashboard-xxxx.vercel.app`. **Abre essa URL no navegador e confirma que funciona em produção.**

> 💡 **Opcional mas recomendado:** configurar custom domain pra ficar tipo `meta.suaempresa.com.br`. Vai em Vercel Dashboard → Settings → Domains → Add. **Vantagem:** parece mais profissional pro reviewer.

### Passo 6 — App Review (15min de trabalho + 2h-3 dias de espera)

Aqui é onde a mágica acontece. Volta pra raiz do repo e abre Claude Code:

```bash
cd ..  # volta pra raiz
claude
```

Quando o Claude abrir, ele já vem **pré-carregado** com:
- ✅ MCP `meta-ads-mcp` conectado (acesso direto à Marketing API)
- ✅ Skills `meta-ads-compliance`, `meta-ads-warmup`, `meta-app-review-approval`
- ✅ Contexto do projeto via `CLAUDE.md`

Então você simplesmente diz pra ele:

> "Vou submeter o Meta App Review pedindo Ads Management Standard Access. Me guia passo a passo."

E ele vai te guiar:
1. **Pré-flight check** — verifica se BM tá verificado, app tá Live, Privacy Policy responde 200
2. **Gravar screencast** — split-screen com seu dashboard à esquerda + Meta Ads Manager nativo à direita (mostra que muda em tempo real)
3. **Adicionar captions Netflix-style** com `ffmpeg` (script vem pronto)
4. **Preencher o form** em developers.facebook.com — descrição em 5 seções, instruções analista, todos os campos do "Tratamento de dados"
5. **Submeter**

Tempo de resposta da Meta: **2 horas a 3 dias**. Email vai chegar no email da conta dev.

### Passo 7 — Verificar aprovação 🎉

Quando receber o email "Your App Review results are ready":

```bash
./scripts/verify-tier.sh act_seu_id https://seu-dominio.vercel.app
```

Resposta esperada:

```
✓ APPROVED — tier is standard_access (9000 pts/h, was 60)
```

**Você acabou de ganhar 150x mais quota.** 🚀

---

## 📦 O que vem dentro

```
meta-ads-claude-starter/
├── README.md                          ← este arquivo
├── CLAUDE.md                          ← instruções pro Claude Code (auto-carregado)
├── LICENSE                            ← MIT
├── .gitignore
│
├── .env.example                       ← template das env vars
├── .mcp.json                          ← config do MCP meta-ads-mcp
│
├── .claude/skills/                    ← 3 skills auto-carregadas pelo Claude
│   ├── meta-ads-compliance/           ← regras anti-ban (sempre ativa)
│   ├── meta-ads-warmup/               ← acumula calls enquanto espera review
│   └── meta-app-review-approval/      ← workflow completo de aprovação
│
├── dashboard/                         ← Next.js + FastAPI (DEMO pra App Review)
│   ├── api/
│   │   ├── index.py                   ← endpoints FastAPI
│   │   └── meta_ads_mcp/              ← package vendored com client + audit + rate limiter
│   ├── app/                           ← Next.js App Router pages
│   ├── components/                    ← componentes UI
│   ├── lib/                           ← hooks SWR + helpers
│   └── vercel.json                    ← config Vercel Python Functions
│
├── docs/                              ← documentação detalhada
│   ├── 01-setup.md                    ← criar app Meta + tokens
│   ├── 02-deploy.md                   ← deploy Vercel
│   ├── 03-app-review.md               ← submeter App Review
│   ├── 04-operacao.md                 ← uso pós-aprovação
│   └── 05-troubleshooting.md          ← erros comuns
│
├── scripts/
│   ├── setup.sh                       ← wizard interativo de setup
│   ├── verify-tier.sh                 ← checa tier após aprovação
│   └── warmup.py                      ← acumula API calls
│
└── examples/
    ├── descricao-app-review.txt       ← template em pt-BR pra colar no form
    └── instrucoes-analista.txt        ← template em pt-BR
```

---

## ❓ FAQ

### Eu sou leigo total, dá pra fazer mesmo?

Dá. Você precisa saber:
- Abrir terminal e copiar comandos (não precisa entender o que cada comando faz)
- Cadastrar coisas em sites (Meta, Vercel, GitHub)
- Ler instruções com calma

Você NÃO precisa saber:
- Programar
- Como funciona Next.js, FastAPI, Vercel internamente
- Inglês fluente (a doc é toda pt-BR)

Se travar, lê o [docs/05-troubleshooting.md](./docs/05-troubleshooting.md) ou abre Issue no GitHub.

### Quanto tempo dura todo o processo?

| Fase | Tempo seu | Tempo Meta |
|------|-----------|------------|
| Setup local | 30min | — |
| Submeter App Review | 15min | 2h-3 dias |
| **Total** | **~45min** | **2h-3 dias** |

### Quanto custa?

| Serviço | Custo |
|---------|-------|
| Meta API (Standard Access) | R$ 0 |
| Vercel (free tier) | R$ 0 |
| GitHub | R$ 0 |
| Claude Code | depende do seu plano (Pro a partir de $20/mês) |
| **Total** | **~R$ 100/mês (só Claude Code)** |

### O dashboard precisa ficar rodando pra sempre?

**Não.** Ele é só demo pra App Review. Após aprovado, pode desligar o Vercel sem problema. Operação real é via Claude Code + MCP.

### O que acontece se eu não passar no primeiro App Review?

Meta manda email com nota específica do que faltou. As mais comuns:
- **"Unable to verify use case experience"** → vídeo não mostrava bem o System User auth → re-grava com caption explícita
- **"Privacy policy URL not accessible"** → URL deu 404 → corrige no app dashboard
- **"Permissions don't match demonstrated use"** → você pediu ads_management mas só mostrou leitura no vídeo → re-grava mostrando uma escrita

Re-submit é rápido (3-5 dias). A skill `meta-app-review-approval` tem `references/myths.md` cobrindo todos os casos.

### Posso usar pra atender clientes externos?

Não com este repo. **Standard Access é só pra contas próprias.** Se você quer atender clientes externos, precisa de **Advanced Access** (processo bem mais complexo, precisa demonstrar OAuth de cliente, etc.).

A skill `meta-app-review-approval` tem uma seção "Quando precisar do próximo tier" explicando essa diferença.

### Posso usar com Python? Node? Outras stacks?

A stack do dashboard incluso é Next.js + FastAPI, mas o **conceito vale pra qualquer stack**. A skill `meta-app-review-approval` tem o blueprint do que o demo precisa mostrar — você pode reimplementar em Django, Rails, Vue, qualquer coisa.

### Funciona fora do Brasil?

Sim. O repo tá em pt-BR mas o código é universal. Templates em `examples/` estão em pt-BR mas você pode traduzir. App Review form pode ser preenchido em pt-BR ou inglês.

### E se eu só quiser ler dados, tem como evitar tudo isso?

**Sim, leia [a seção do topo deste README](#%EF%B8%8F-antes-de-começar-você-precisa-mesmo-disso).** Spoiler: usa Windsor.ai + Claude.ai e resolve em 5min.

---

## 🆘 Suporte

### Travou? Antes de pedir ajuda:

1. **Lê [docs/05-troubleshooting.md](./docs/05-troubleshooting.md)** — cobre 80% dos erros
2. **Procura em [GitHub Issues](https://github.com/thaleslaray/meta-ads-claude-starter/issues)** (talvez já foi reportado)
3. **Tenta reproduzir com env limpa** (às vezes é cache local)

### Ainda travou? Abre um Issue

Vai em https://github.com/thaleslaray/meta-ads-claude-starter/issues/new

**Inclui:**
- Comando exato que rodou
- Erro completo (não corta)
- Output de `vercel logs --since 30m` se for problema de deploy
- Versão dos pré-requisitos: `node --version`, `python3 --version`, `vercel --version`

**NÃO inclui:**
- ❌ `META_ACCESS_TOKEN`
- ❌ `META_APP_SECRET`
- ❌ Qualquer secret

---

## 📜 Licença

MIT — qualquer um pode usar, modificar, distribuir, vender. Ver [LICENSE](./LICENSE).

## 👤 Autor

Maintido por [Thales Laray](https://github.com/thaleslaray).

---

## ⭐ Gostou?

Se este repo te economizou tempo:
- ⭐ Star no GitHub (ajuda outros a encontrar)
- 🔄 Compartilha com quem tá penando no App Review
- 💬 Conta no Issues como foi sua experiência (positiva ou negativa, ambas ajudam a melhorar)
