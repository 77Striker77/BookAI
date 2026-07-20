#!/usr/bin/env bash
# ============================================================================
# Aktiviert die Branch-Politik (Regel des Nutzers, aktualisiert 2026-07-20).
#
#   Seiten-Branches sind ERLAUBT. Aber vor Session-Ende muss ALLES auf 'main'
#   landen — danach kann der Seiten-Branch gefahrlos gelöscht werden.
#
# Muss pro Klon/Session einmal laufen (git-Hook-Pfad lebt in .git/config und
# wird NICHT mitcommittet; der Web-Container ist flüchtig).
# Wird per SessionStart-Hook automatisch aufgerufen.
# ============================================================================
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

git config core.hooksPath .githooks
chmod +x .githooks/pre-push 2>/dev/null || true

current="$(git branch --show-current 2>/dev/null || echo '?')"

echo "🌿 Branch-Politik aktiv: Seiten-Branches erlaubt."
echo "   → Vor Session-Ende ALLES auf 'main' zusammenführen, dann Seiten-Branch löschen."
if [ -n "$current" ] && [ "$current" != "main" ]; then
  echo "   Aktueller Branch: '$current' (Seiten-Branch) — am Ende nach 'main' mergen & löschen."
fi
