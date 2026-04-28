# Pesquisa: Como passar fácil no Meta App Review (Ads Management Standard Access)

**Gerado:** 2026-04-24
**Contexto:** Submissão de internal tool first-party (Escola de Automação) pra feature "Ads Management Standard Access"
**Status:** Pré-submissão; vídeo de 1min07s já gravado e legendado em inglês.

---

## Resumo Executivo

Submissão atual tem **alta chance de aprovar com 1-2 ajustes pequenos**. O risco principal é a ausência de caption explicando que auth é via System User token — o reviewer espera ver login OAuth e pode rejeitar com "unable to verify use case experience". Confiança ALTA (todos fatos-chave com ≥2 fontes Tier A/B).

---

## 🚨 Bloqueadores que precisam fix antes de submeter

### Fix 1 — Caption "System User auth" no início do vídeo

Reviewers em 2025-2026 rejeitam screencasts S2S sem login visível, **a menos que tenha overlay explícito**. Padrão aprovado:

> "This is an internal admin tool. Authentication to Meta is handled server-to-server via a System User access token (no end-user OAuth screen)."

3 fontes independentes confirmam: PostMoore case study, Reddit r/MetaAPIDevelopers (2025-2026), Stack Overflow Q 51351881 + Meta server-to-server sample submission.

### Fix 2 — Privacy Policy URL acessível

App Review rejeita instantaneamente se a URL der 404 ou for muito lenta. Verificar:
- Privacy Policy URL no app dashboard
- User Data Deletion URL (ou instruções)
- Ambos em domínio público, não localhost

3 fontes confirmam: Saurabh Dhar guide, Reddit r/facebook 1rux37s, PostMoore.

---

## Análise dos Sub-Tópicos

### Sub-tópico A — System User auth flow no screencast

**Achados:**
- Meta NÃO requer screencast pra apps server-to-server, mas a submissão UI força upload — então sobe um vídeo que **explica** o flow S2S, não que **mostra** OAuth.
- Padrão de caption aprovado: explicar nos primeiros 5-10s que auth acontece via System User no backend, sem login UI.
- Antes de cada ação que usa permission, repetir caption nomeando a permission ("This action uses ads_management via System User token").

**Fonte primária:** Meta server-to-server sample submission (referenciada em Stack Overflow 51351881 e em PDFs antigos da própria Meta).
**Fontes secundárias:** PostMoore 2026, Reddit r/MetaAPIDevelopers, Saurabh Dhar 2025.

### Sub-tópico B — First-party success cases

**Achados:**
- Casos públicos nomeados são raros, mas o padrão de aprovação first-party é consistente.
- PostMoore: aprovado depois de re-recording slow + per-permission annotations + remover API calls não usadas.
- Saurabh Dhar: portfolio inclui Marketing/Ads APIs aprovadas (não nomeia clientes).
- Threshold pra Standard Access: app deve apenas demonstrar uso correto. Threshold pra Advanced Access: 1500 calls + <10% erro em 30 dias.
- Timeline: 3-7 business days primeiro review; 2-5 dias por re-submit.
- Maioria precisa de 1 iteração.

**Diferença chave first-party vs SaaS:**
- First-party: foco em "own assets only" + dados não saem da org → caminho mais leve.
- SaaS: precisa explicar onboarding de 3rd parties + consent + separação de dados → review mais rigoroso.

### Sub-tópico C — Screencast policy 2025-2026

**Spec oficial:**
- Duração: NÃO publicada. Comunidade reporta 1-5min por permission group como faixa segura.
- Resolução: NÃO especificada. 720p/1080p MP4 H.264 é safe default.
- Audio narration: NÃO requerido. Captions/annotations recomendados (reviewers assistem mutado).
- Idioma: NÃO precisa ser inglês na UI; explicações em inglês recomendadas.
- O que mostrar: login (ou explicação S2S), permission grant, ação que usa permission, resultado visível.

**Mudanças 2025-2026 vs anos anteriores:**
- Mais ênfase em per-permission coverage.
- Mais ênfase em annotations/captions (reviewers assistem mutado).
- Stricter contra "generic screencast" — não pode ser vídeo reusado de outro app.
- Ongoing checks pós-aprovação (Meta pode pedir novos vídeos).

---

## Comparativo Aplicado à Submissão Atual

| Aspecto | Tua submissão | Padrão "approved" | Risco |
|---------|---------------|-------------------|-------|
| Actor declarado | "Escola de Automação operates 3 owned accounts" | ✅ Match | OK |
| Use case explícito | Lista 5 ações concretas | ✅ Match | OK |
| First-party vs SaaS | "We are not building a third-party product" | ✅ Match | OK |
| Login/OAuth visível | ❌ Vídeo já começa logado | ⚠️ Reviewer espera login OU caption | **ALTO** |
| Caption System User | ❌ Captions atuais não mencionam | ✅ Reddit/PostMoore recomendam | **ALTO** |
| Real-data proof | ✅ Mostra Ads Manager refletindo write | ✅ Match | OK |
| Privacy Policy URL | Não verificado | Obrigatório, não pode 404 | **MÉDIO** |
| 1500 calls + <10% erro | Tier dev tem 60pts/h | NÃO é requisito pra Standard, só Advanced | **BAIXO** |
| English UI | ✅ Dashboard em inglês | ✅ Match | OK |
| Length 2-5min | 1min07s | ⚠️ Curto mas focado | **BAIXO** |

---

## Mito Desconsiderado

**"Precisa de 1500 chamadas + <10% erro"** — Esse é requisito pra **Advanced Access**, NÃO pra **Standard Access**. Standard Access só precisa que o app demonstre uso correto.

**Fontes:**
- Meta developer thread #691016324664624 (Primer rejected explicitly mentions "Ads API Standard Access" — but the criteria URL points to /authorization which lists 1500 calls under Advanced).
- Meta docs `/marketing-api/get-started/authorization`.
- LinkedIn Minhaj Ahmed (citing 1500/15days/<10%).

---

## Status dos Fatos-Chave

| Fato | Fontes | Verificado? |
|------|--------|-------------|
| System User aceito sem login OAuth com caption | Meta S2S sample + Stack Overflow 51351881 + PostMoore + Reddit r/MetaAPIDevelopers | ✅ confirmado (4 fontes) |
| 1500 calls + <10% erro é Advanced, não Standard | Meta docs official + LinkedIn Minhaj | ✅ confirmado (2 fontes) |
| Privacy Policy URL é hard blocker | Saurabh Dhar + Reddit guide 1rux37s + PostMoore | ✅ confirmado (3 fontes) |
| Vídeo 1-5min é faixa segura | Meta docs (sem limite oficial) + PostMoore + Reddit | ✅ confirmado |

---

## Fontes Avaliadas (CRAAP)

### Tier A (80-100)
- **Meta Screen Recordings doc** — 90 — `developers.facebook.com/docs/app-review/submission-guide/screen-recordings/`
- **Meta developer community thread #691016324664624** (Primer rejection) — 88 — texto literal de rejeição
- **Meta Ads Management Standard Access feature doc** — 92

### Tier B (60-79)
- **PostMoore "Why Meta App Review Keeps Disapproving"** — 78 — `postmoo.re/blogs/meta-app-review-disapproved-how-to-get-approved`
- **Saurabh Dhar Meta Approval Guide** — 70 — `saurabhdhar.com/blog/meta-app-approval-guide` — Purpose=vender consultoria, rebaixado
- **Reddit r/facebook 1rux37s** — 75 — community consensus
- **Reddit r/MetaAPIDevelopers** — 72 — discussions 2025-2026
- **Stack Overflow Q 51351881** — 68 — referencia Meta sample submission verbatim

### Tier C/D (descartados)
- LinkedIn posts genéricos sobre Facebook Ads — Purpose=lead gen, sem fact-check

---

## Recomendação Final

**Aprovar com 1 retake do vídeo + verificação de Privacy Policy URL.** Custo: ~30 minutos. Economiza 2-3 rounds de rejeição (cada round = 3-7 dias).

### Próximos passos
1. Editar `meta-captions.ass`: trocar primeiras 2 captions por overlays explicando System User auth.
2. Re-encodar vídeo via ffmpeg.
3. Verificar que Privacy Policy URL no app dashboard responde 200 OK.
4. Submeter com a descrição já redigida (cobre os 4 pontos críticos: actor, scope, permissions, data boundaries).

### Se rejeitar mesmo assim
- Re-ler nota de rejeição literalmente — Meta dá pista clara.
- Comum: re-record com permission overlays MAIS explícitos.
- Se não funcionar em 3 tentativas: considerar consultor (Saurabh Dhar) — ~$300-500.
