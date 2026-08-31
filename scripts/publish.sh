#!/usr/bin/env bash
# Commit all changes and push to main → triggers GitHub Pages deploy.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

MSG="${1:-}"

echo ""
echo "  Publish to GitHub Pages"
echo "  ────────────────────────"
echo ""
echo "  Preview first:  npm run serve  →  http://localhost:3000"
echo ""

if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "  No changes to publish."
  exit 0
fi

echo "  Changes to publish:"
git status --short
echo ""

if [ -z "$MSG" ]; then
  read -r -p "  Commit message [Site update]: " MSG
  MSG="${MSG:-Site update}"
fi

read -r -p "  Commit and push to main? [y/N] " CONFIRM
case "$CONFIRM" in
  y|Y|yes|Yes) ;;
  *) echo "  Cancelled."; exit 0 ;;
esac

git add -A
git commit -m "$MSG"
git push origin main

echo ""
echo "  Pushed to main. GitHub Actions will deploy in ~1 minute."
echo "  Live site: https://huasclassroom.com"
echo ""
