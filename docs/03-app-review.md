# 03 — Submeter Meta App Review (1-3 dias)

Pra sair do tier Development (60 pts/h) e entrar no Standard (9.000 pts/h, 150x mais quota), você precisa passar pelo Meta App Review pedindo a feature **Ads Management Standard Access**.

A skill `meta-app-review-approval` carrega automaticamente quando você começar esse processo no Claude. Esse doc é o resumo executivo.

## Pré-flight checklist

- [ ] Setup feito (env vars OK)
- [ ] Dashboard deployado e respondendo 200
- [ ] Privacy Policy URL pública (no app dashboard)
- [ ] Business Manager **verified**
- [ ] App em modo **Live** (não Development)
- [ ] System User token + appsecret_proof OK

Se faltar qualquer um desses, App Review é rejeitado sem human review.

## 1. Gravar screencast (~30min)

O screencast é o que o reviewer vai analisar. Workflow:

1. **Setup gravação split-screen:** dashboard à esquerda, Meta Ads Manager nativo à direita
2. **Gravar 1-2min mostrando:**
   - Dashboard carregando dados reais
   - Você pausando/ativando uma campanha (HITL flow visível)
   - Você atualizando budget de uma campanha (HITL flow visível)
   - Meta Ads Manager refletindo as mudanças em tempo real (PROVA de que API tá real)
3. **Gravar em 720p+ MP4**, não precisa de audio

## 2. Adicionar captions Netflix-style

Use o template `.ass` da skill:

```bash
cp ~/.claude/skills/meta-app-review-approval/assets/captions-template.ass /tmp/captions.ass
# edite os textos pros seus momentos
~/.claude/skills/meta-app-review-approval/scripts/burn-captions.sh \
  meu-video.mp4 /tmp/captions.ass meu-video-captioned.mp4
```

Caption obrigatória nos primeiros 4s se você usa System User (sem OAuth visível):

> "Internal dashboard — auth via server-side System User token (no end-user OAuth)"

Sem essa caption, reviewer rejeita com "unable to verify use case experience".

## 3. Preencher form do App Review

Em https://developers.facebook.com/apps/SEU_APP_ID/app-review/submissions:

1. **Solicitar feature** → Ads Management Standard Access
2. **Descrição** → use template `examples/descricao-app-review.txt` (5 seções: actor, auth, what app does, why standard, compliance)
3. **Screencast** → upload do MP4 com captions
4. **Marcar checkbox** de uso permitido

## 4. Tratamento de dados (Phase 4 do form)

Respostas pra um internal first-party tool:

| Pergunta | Resposta |
|----------|----------|
| Operadores de dados terceiros? | Não |
| Entidade responsável | Sua razão social |
| País | Brasil |
| Compartilhou dados com autoridades? | Não |
| Processos pra solicitações de autoridades | **Marcar 2:** "Análise obrigatória de legitimidade" + "Política de minimização de dados". **NÃO marque "Nenhuma das opções acima"** |

## 5. Instruções pro analista

Use template `examples/instrucoes-analista.txt`. Mencione:
- App é internal first-party (only manages own accounts)
- Dashboard URL pública pra reviewer abrir
- Auth via System User (sem OAuth visível)
- Lista de ad account IDs cobertos
- Referência ao screencast

## 6. Submeter e esperar

- Tempo médio: **2 horas a 3 dias** (testado)
- Notificação chega no email da conta dev
- Status fica em `https://developers.facebook.com/apps/SEU_APP_ID/app-review/submissions`

## 7. Verificar tier após aprovação

```bash
./scripts/verify-tier.sh act_seu_id https://meta.seudominio.com.br
```

Resposta esperada:
```
✓ APPROVED — tier is standard_access (9000 pts/h, was 60)
```

Se ainda mostrar `development_access` 1h após aprovação, contate suporte Meta.

## Se rejeitar

Meta manda nota específica. Padrões comuns:

| Nota | Fix |
|------|-----|
| "Unable to verify use case experience" | Re-record com caption de System User mais explícita |
| "Privacy policy URL not accessible" | Verificar URL responde 200, fazer redeploy se preciso |
| "Permissions don't match demo" | Demonstrar EXATAMENTE as permissions pedidas no screencast |

Re-submit é rápido (3-5 dias). A skill `meta-app-review-approval` tem mais detalhes em `references/myths.md` e `references/form-fields.md`.

## Próximo passo

→ [04-operacao.md](./04-operacao.md) — Uso dia-a-dia com guard rails
