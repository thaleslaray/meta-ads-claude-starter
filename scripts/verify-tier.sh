#!/usr/bin/env bash
# Verify Meta API tier post-approval.
#
# Why this exists:
#   The /api/quota endpoint reads from the in-memory rate_limiter cache.
#   That cache is empty until at least 1 real Marketing API call has
#   been made — so right after approval, /api/quota will still report
#   "development_access" with max 60 pts, even though the upgrade is
#   already active. This script triggers a real read first, then queries
#   the quota, so you see the actual current tier.
#
# Usage:
#   ./verify-tier.sh <account_id> <api_base_url>
#
# Example:
#   ./verify-tier.sh act_487731909607599 https://meta.escoladeautomacao.com.br

set -euo pipefail

ACCOUNT="${1:?usage: verify-tier.sh <account_id> <api_base_url>}"
BASE="${2:?missing api base url, e.g. https://app.example.com}"

echo "1. Triggering real Marketing API read…"
curl -s "$BASE/api/account/$ACCOUNT/insights-with-delta?date_preset=today" \
  -o /tmp/_verify_insights.json -w "  HTTP: %{http_code}\n"

echo ""
echo "2. Reading current quota / tier…"
QUOTA="$(curl -s "$BASE/api/quota?account_id=$ACCOUNT")"
echo "  $QUOTA"

echo ""
TIER="$(echo "$QUOTA" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("tier","unknown"))')"
MAX_PTS="$(echo "$QUOTA" | python3 -c 'import sys,json; print(json.load(sys.stdin).get("max_points","unknown"))')"

case "$TIER" in
  standard_access)
    echo "✓ APPROVED — tier is standard_access ($MAX_PTS pts/h, was 60)"
    ;;
  development_access)
    echo "⚠ Still development_access. If approval came through within"
    echo "  the last hour, wait 5-10 minutes and re-run. Meta caches"
    echo "  the tier propagation."
    ;;
  *)
    echo "? Unexpected tier: $TIER"
    ;;
esac
