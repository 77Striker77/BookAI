#!/usr/bin/env bash
# ============================================================================
# Schaltet die Ein-Branch-Verriegelung scharf.
# Muss pro Klon/Session einmal laufen (git-Hook-Pfad lebt in .git/config und
# wird NICHT mitcommittet; der Web-Container ist flüchtig).
# Wird idealerweise per SessionStart-Hook automatisch aufgerufen.
# ============================================================================
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

git config core.hooksPath .githooks
chmod +x .githooks/pre-push 2>/dev/null || true

echo "🔒 Ein-Branch-Verriegelung aktiv: Pushes nur auf 'claude/books-library-feedback-rhkjwj'."
