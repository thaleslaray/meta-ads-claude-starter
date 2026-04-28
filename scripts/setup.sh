#!/usr/bin/env bash
# Interactive setup wizard. Asks ONLY for what's needed for basic usage
# (Claude Code + 60 pts/h tier). Dashboard-related fields (BM_ID, AD_ACCOUNTS)
# are skipped — Claude will ask for them later if/when you decide to do
# the App Review.
#
# Run from repo root: ./scripts/setup.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$REPO_ROOT/.env"

if [ -f "$ENV_FILE" ]; then
  read -r -p ".env already exists. Overwrite? (y/N) " ans
  if [ "$ans" != "y" ] && [ "$ans" != "Y" ]; then
    echo "Aborted."
    exit 0
  fi
fi

echo ""
echo "Meta Ads + Claude Code — Setup Wizard"
echo "======================================"
echo ""
echo "Você só precisa de 2 coisas pra começar a usar Claude Code"
echo "com Meta Ads (60 pts/h). Pega ambos em business.facebook.com:"
echo ""
echo "  1. System User token: Configurações → Usuários → Usuários do Sistema"
echo "     → seu user → Gerar Novo Token"
echo "     (permissions: ads_management, ads_read, business_management)"
echo ""
echo "  2. App Secret: developers.facebook.com → seu app → Settings → Basic"
echo "     → App Secret → Show"
echo ""

read -r -p "META_ACCESS_TOKEN (System User token, começa com EAA...): " META_ACCESS_TOKEN
read -r -p "META_APP_SECRET (32 caracteres): " META_APP_SECRET
read -r -p "ORG_NAME (nome da sua empresa, aparece no dashboard se você fizer App Review): " ORG_NAME

# Write .env (no trailing newlines on values)
{
  printf "META_ACCESS_TOKEN=%s\n" "$META_ACCESS_TOKEN"
  printf "META_APP_SECRET=%s\n" "$META_APP_SECRET"
  printf "ORG_NAME=%s\n" "$ORG_NAME"
  printf "\n"
  printf "# Dashboard fields (preenchidos depois, se/quando fizer App Review):\n"
  printf "# META_BM_ID=1234567890\n"
  printf "# META_AD_ACCOUNTS=[{\"id\":\"act_xxx\",\"name\":\"Conta Principal\",\"label\":\"Main\"}]\n"
} > "$ENV_FILE"

chmod 600 "$ENV_FILE"

echo ""
echo "✅ .env criado!"
echo ""
echo "Próximo passo: roda 'claude' nesta pasta. Ele já vai estar"
echo "conectado nas suas contas Meta com guard rails anti-ban."
echo ""
echo "Tenta perguntar:"
echo "  • 'Lista minhas contas de anúncios'"
echo "  • 'Quanto gastei em Meta Ads essa semana?'"
echo "  • 'Mostra as 5 campanhas com pior CPA'"
echo ""
echo "Quando quiser evoluir pra Standard Access (9.000 pts/h),"
echo "fala pro Claude: 'Vou submeter Meta App Review'."
echo ""
