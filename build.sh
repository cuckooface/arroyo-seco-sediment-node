#!/usr/bin/env bash
# Rebuild deck/ASSN_Deck_Updated.pdf from deck/deck.html (1920x1080 pages).
set -euo pipefail
cd "$(dirname "$0")/deck"
for c in google-chrome google-chrome-stable chromium chromium-browser /opt/pw-browsers/chromium "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
  if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME="$c"; break; fi
done
: "${CHROME:?Chrome or Chromium not found}"
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --allow-file-access-from-files \
  --virtual-time-budget=15000 --print-to-pdf="$PWD/ASSN_Deck_Updated.pdf" "file://$PWD/deck.html"
echo "wrote deck/ASSN_Deck_Updated.pdf"
