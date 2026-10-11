#!/usr/bin/env bash
# ============================================================================
# Aktiviert die Branch-Politik (Regel des Nutzers, verschärft 2026-10-11: nur main).
#
#   Direkt auf main arbeiten. Erzwungener Seiten-Branch: in derselben Session auf main
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
chmod +x .githooks/pre-push .githooks/pre-commit 2>/dev/null || true

current="$(git branch --show-current 2>/dev/null || echo '?')"

echo "🌿 Branch-Politik aktiv: Es gibt nur main."
echo "   → Direkt auf main arbeiten. Erzwungener Seiten-Branch: noch in dieser Session nach main mergen und löschen."
if [ -n "$current" ] && [ "$current" != "main" ]; then
  echo "   Aktueller Branch: '$current' (Seiten-Branch) — am Ende nach 'main' mergen & löschen."
fi
