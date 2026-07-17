#!/usr/bin/env bash
# vault-first.sh — Erinnerung & Guard für die OBERSTE REGEL (siehe CLAUDE.md):
#   Der Vault ist die EINZIGE Quelle. Artefakte sind nur Projektionen daraus.
#   Nie ein Artefakt publizieren/committen, solange Vault-Änderungen uncommittet sind.
#
# Aufruf: bash scripts/vault-first.sh   (vor jedem Artefakt-Publish und vor jedem Commit)
# Exit 0 = sauber (nichts Uncommittetes) · Exit 1 = es liegt Uncommittetes vor (bitte committen).

set -euo pipefail
root="$(git rev-parse --show-toplevel)"
cd "$root"

echo "🔒 VAULT-FIRST — Vault ist die einzige Wahrheit; Artefakte sind nur Projektionen."
echo

vault_changes="$(git status --porcelain -- vault 2>/dev/null || true)"
artifact_changes="$(git status --porcelain -- artifacts 2>/dev/null || true)"

status=0

if [ -n "$vault_changes" ]; then
  echo "⚠️  Uncommittete VAULT-Änderungen — VOR jedem Artefakt-Publish committen:"
  echo "$vault_changes"
  echo
  status=1
fi

if [ -n "$artifact_changes" ]; then
  echo "⚠️  Uncommittete ARTEFAKT-Änderungen — nur committen, wenn sie aus dem Vault erzeugt sind:"
  echo "$artifact_changes"
  echo
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "✅ Sauber: keine uncommitteten Vault-/Artefakt-Änderungen."
else
  echo "➡️  Reihenfolge: Vault schreiben → committen → Artefakt AUS dem Vault erzeugen → pushen."
  echo "➡️  Ein veröffentlichtes Artefakt darf NIE Infos enthalten, die nicht im Vault stehen."
fi

exit "$status"
