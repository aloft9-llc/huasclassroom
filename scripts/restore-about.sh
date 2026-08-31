#!/usr/bin/env bash
# Restore About page from _unpublished/ into web/ (does not re-add nav links).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SRC="_unpublished/about"

if [ ! -f "$SRC/about.html" ] || [ ! -f "$SRC/about.css" ]; then
  echo "  Archive not found in $SRC/"
  exit 1
fi

cp "$SRC/about.html" web/about.html
cp "$SRC/about.css" web/assets/css/about.css

echo ""
echo "  Restored:"
echo "    web/about.html"
echo "    web/assets/css/about.css"
echo ""
echo "  Re-add “About Me” links in web/index.html (and lesson nav) if needed."
echo "  Preview:  npm run serve  →  http://localhost:3000/about.html"
echo "  Publish:  npm run publish"
echo ""
