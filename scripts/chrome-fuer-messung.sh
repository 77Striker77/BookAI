#!/usr/bin/env bash
# chrome-fuer-messung.sh — Browser-Wrapper für die Design-Werkstatt (Design_AI).
#
# Warum es das gibt: Die BookAI-Sessions laufen in einem Container **als root**.
# Chromium verweigert dort den Start ohne `--no-sandbox` — und zwar still: die
# Skripte von `design:artefakt-werkstatt` bekommen einfach leere Ausgaben und
# melden dann „Seite lädt möglicherweise gar nicht", „Breitenmatrix UNGEPRUEFT"
# und „kein Debug-Port". Das sind KEINE Artefakt-Fehler, sondern eine
# Umgebungsfalle. Dieser Wrapper schaltet sie aus.
#
# Benutzung:
#   export BROWSER_BIN="$CLAUDE_PROJECT_DIR/scripts/chrome-fuer-messung.sh"
#   bash <artefakt-werkstatt>/scripts/mess.sh artifacts/bibliothek.html
#
# Ein anderer Browser lässt sich über CHROME_ECHT vorgeben.
set -u

kandidaten=(
  "${CHROME_ECHT:-}"
  /opt/pw-browsers/chromium-1194/chrome-linux/chrome
  /opt/pw-browsers/chromium/chrome-linux/chrome
  /usr/bin/chromium
  /usr/bin/chromium-browser
  /usr/bin/google-chrome
)

# Playwright-Installationen tragen eine Build-Nummer im Pfad — mit einsammeln,
# damit ein Update des Images den Wrapper nicht bricht.
for treffer in /opt/pw-browsers/chromium-*/chrome-linux/chrome; do
  [ -x "$treffer" ] && kandidaten+=("$treffer")
done

browser=""
for k in "${kandidaten[@]}"; do
  if [ -n "$k" ] && [ -x "$k" ]; then browser="$k"; break; fi
done

if [ -z "$browser" ]; then
  echo "chrome-fuer-messung: kein Chromium gefunden (CHROME_ECHT setzen)" >&2
  exit 3
fi

# --no-sandbox: Pflicht als root · --disable-dev-shm-usage: /dev/shm ist im
# Container knapp · dbus-Rauschen wird nicht unterdrückt, es ist harmlos.
exec "$browser" --no-sandbox --disable-dev-shm-usage "$@"
