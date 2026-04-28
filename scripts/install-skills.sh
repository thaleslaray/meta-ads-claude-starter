#!/usr/bin/env bash
# Fallback installer for the 3 skills.
# Use this ONLY if Claude Code is not auto-discovering the skills
# from the project's .claude/skills/ folder.
#
# This copies the skills to ~/.claude/skills/ (global) so they're
# available system-wide.
#
# Run from repo root: ./scripts/install-skills.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$REPO_ROOT/.claude/skills"
DST="$HOME/.claude/skills"

if [ ! -d "$SRC" ]; then
  echo "Error: $SRC not found. Run from a fresh clone of the repo." >&2
  exit 1
fi

mkdir -p "$DST"

echo ""
echo "Installing skills to $DST"
echo "================================"
echo ""

for skill in meta-ads-compliance meta-ads-warmup meta-app-review-approval; do
  if [ -d "$DST/$skill" ]; then
    read -r -p "  $skill já existe em $DST. Sobrescrever? (y/N) " ans
    if [ "$ans" != "y" ] && [ "$ans" != "Y" ]; then
      echo "  ⏭  $skill skipped"
      continue
    fi
    rm -rf "$DST/$skill"
  fi
  cp -R "$SRC/$skill" "$DST/"
  echo "  ✓ $skill installed"
done

echo ""
echo "✅ Skills instaladas. Agora elas funcionam em qualquer projeto,"
echo "   não só neste repo."
echo ""
echo "Pra confirmar: abre 'claude' em qualquer pasta e digita '/'"
echo "— você deve ver as 3 skills no menu."
