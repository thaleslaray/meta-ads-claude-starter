# Meta Ads + Claude Code Starter

Boilerplate com **um único objetivo**: passar pelo Meta App Review e sair do tier Development (60 pts/h) pro Standard Access (9.000 pts/h, 150x mais quota).

**Resultado típico:** App Review aprovado em 2-72h na primeira tentativa.

## ⚠️ Sobre o dashboard

O dashboard incluso (Next.js + FastAPI) é **exclusivamente demo pro App Review** — você o deploya, grava o screencast nele, submete pro Meta. Depois de aprovado, **a operação real acontece via Claude Code + MCP `meta-ads-mcp`**, não pelo dashboard. Você pode até desligar o Vercel após aprovação se quiser.

A skill `meta-app-review-approval` é a fonte da verdade — ela contém todas as regras, templates de descrição, captions Netflix-style, e o blueprint do dashboard. Quem só ler a skill consegue replicar o processo inteiro mesmo sem clonar este repo.

## Quickstart (30min)

```bash
# 1. Clone
git clone https://github.com/thaleslaray/meta-ads-claude-starter
cd meta-ads-claude-starter

# 2. Setup interativo (pede tokens, gera .env)
./scripts/setup.sh

# 3. Deploy na Vercel
cd dashboard
vercel deploy --prod

# 4. Use via Claude Code
cd ..
claude  # Claude lê CLAUDE.md + .mcp.json + skills automaticamente
```

## O que vem dentro

| Componente | Pra quê |
|------------|---------|
| **Dashboard Next.js + FastAPI** | DEMO pro App Review (descartável após aprovação) |
| **Skill `meta-app-review-approval`** | Fonte da verdade: workflow completo + templates + captions |
| **Skill `meta-ads-compliance`** | Regras anti-ban + 5 regras de operação contínua |
| **Skill `meta-ads-warmup`** | Acumula API calls enquanto espera App Review |
| **MCP `meta-ads-mcp`** | Acesso direto à Marketing API via Claude (uso operacional) |
| **Templates** | Descrição do App Review + instruções pro analista |

## Documentação

| Doc | O que cobre |
|-----|-------------|
| [01-setup.md](./docs/01-setup.md) | Criar app Meta + tokens (15min) |
| [02-deploy.md](./docs/02-deploy.md) | Deploy na Vercel (15min) |
| [03-app-review.md](./docs/03-app-review.md) | Submeter App Review (1-3 dias) |
| [04-operacao.md](./docs/04-operacao.md) | Uso dia-a-dia + automações safe |
| [05-troubleshooting.md](./docs/05-troubleshooting.md) | Erros comuns + fixes |

## Pré-requisitos

- Conta Meta Business Manager **verificada**
- App criado em `developers.facebook.com`
- Node.js 20+
- Python 3.11+
- Conta Vercel (free tier funciona)
- Claude Code instalado (`claude` no terminal)

## Por que este repo existe

A Meta Marketing API tem uma armadilha: o tier inicial (Development Access) só dá 60 pontos/hora — esgota em segundos numa operação real. Pra ganhar Standard Access (9.000 pts/h) você precisa passar por App Review, que rejeita 90% dos apps na primeira tentativa.

Este starter encapsula a fórmula testada que aprovou em **2 horas na primeira tentativa**:
- Dashboard funcional como prova de uso real
- Auth via System User (não OAuth confuso)
- Audit log + HITL pra demonstrar boas práticas
- Templates de descrição + screencast com formato que Meta endossa

## Status

**v1.0.0** — Estável. Aprovado pelo Meta para a app `meta.escoladeautomacao.com.br` em 24/04/2026 (2h de análise, primeira tentativa).

## Contribuindo

PRs e issues bem-vindos em [GitHub Issues](https://github.com/thaleslaray/meta-ads-claude-starter/issues).

Antes de abrir issue de erro:
1. Veja [docs/05-troubleshooting.md](./docs/05-troubleshooting.md)
2. Procure issues fechados (talvez já foi resolvido)
3. **NUNCA** inclua tokens/secrets no issue

## Licença

MIT — ver [LICENSE](./LICENSE).

## Autor

Maintido por [Thales Laray](https://github.com/thaleslaray).
