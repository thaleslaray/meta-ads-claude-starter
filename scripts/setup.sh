#!/usr/bin/env bash
# Interactive setup wizard. Asks for tokens + ad accounts and writes .env.
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
echo "Get these from:"
echo "  - System User token: business.facebook.com → System Users → Generate Token"
echo "  - App Secret: developers.facebook.com → Your App → Settings → Basic"
echo "  - Business Manager ID: business.facebook.com → Settings → Business Info"
echo ""

read -r -p "META_ACCESS_TOKEN (System User token): " META_ACCESS_TOKEN
read -r -p "META_APP_SECRET: " META_APP_SECRET
read -r -p "META_BM_ID (numeric Business Manager ID): " META_BM_ID
read -r -p "ORG_NAME (your business name): " ORG_NAME

echo ""
echo "Now we need your ad accounts. You'll add them one at a time."
echo "Account IDs look like 'act_487731909607599'."
echo ""

ACCOUNTS_JSON="["
COUNT=0
while true; do
  read -r -p "Add ad account? (y/N) " add
  if [ "$add" != "y" ] && [ "$add" != "Y" ]; then
    break
  fi
  read -r -p "  Account ID (act_xxx): " ACC_ID
  read -r -p "  Account name (e.g. 'Main Brand Account'): " ACC_NAME
  read -r -p "  Short label (e.g. 'Main'): " ACC_LABEL

  if [ $COUNT -gt 0 ]; then
    ACCOUNTS_JSON+=","
  fi
  ACCOUNTS_JSON+="{\"id\":\"$ACC_ID\",\"name\":\"$ACC_NAME\",\"label\":\"$ACC_LABEL\"}"
  COUNT=$((COUNT + 1))
done
ACCOUNTS_JSON+="]"

if [ $COUNT -eq 0 ]; then
  echo "Error: at least one ad account is required." >&2
  exit 1
fi

# Write .env (no trailing newlines on values)
{
  printf "META_ACCESS_TOKEN=%s\n" "$META_ACCESS_TOKEN"
  printf "META_APP_SECRET=%s\n" "$META_APP_SECRET"
  printf "META_BM_ID=%s\n" "$META_BM_ID"
  printf "META_AD_ACCOUNTS=%s\n" "$ACCOUNTS_JSON"
  printf "ORG_NAME=%s\n" "$ORG_NAME"
} > "$ENV_FILE"

chmod 600 "$ENV_FILE"

echo ""
echo "✓ .env written ($COUNT accounts configured)"
echo ""
echo "Next: ./scripts/verify-tier.sh ${ACC_ID:-act_xxx} http://localhost:3000"
echo "  (after starting dashboard locally with 'cd dashboard && npm run dev')"
