#!/usr/bin/env bash
# ============================================================================
# Session-Ende-Reminder (Stop-Hook) — Branch-Politik vom 2026-07-20.
# Erinnert (blockiert NICHT), wenn gerade auf einem Seiten-Branch mit Commits
# gearbeitet wird, die noch nicht in 'main' gelandet sind: vor Session-Ende
# nach 'main' zusammenführen, dann den Seiten-Branch löschen.
# Gibt einen 'systemMessage' aus (für den Nutzer sichtbar), sonst nichts.
# ============================================================================
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root" 2>/dev/null || exit 0

# stdin (Hook-Payload) verwerfen
cat >/dev/null 2>&1 || true

current="$(git branch --show-current 2>/dev/null || echo '')"
[ -z "$current" ] && exit 0
[ "$current" = "main" ] && exit 0

# Basis zum Vergleich: 'origin/main' (Remote-Wahrheit) zuerst, sonst lokaler 'main'.
# Wichtig, weil der lokale 'main' im flüchtigen Container schnell veraltet und
# sonst Commits als "nicht gemergt" meldet, die remote längst in main liegen.
base=""
if git rev-parse --verify -q origin/main >/dev/null 2>&1; then
  base="origin/main"
elif git rev-parse --verify -q main >/dev/null 2>&1; then
  base="main"
fi

unmerged=0
if [ -n "$base" ]; then
  unmerged="$(git rev-list --count "${base}..HEAD" 2>/dev/null || echo 0)"
fi

# Auch uncommittete Änderungen zählen als "noch nicht gesichert"
dirty="$(git status --porcelain 2>/dev/null | head -c1)"

if [ "${unmerged:-0}" -gt 0 ] || [ -n "$dirty" ]; then
  msg="🌿 Branch-Politik: du bist auf Seiten-Branch '$current'"
  [ "${unmerged:-0}" -gt 0 ] && msg="$msg mit $unmerged Commit(s) noch nicht in main"
  [ -n "$dirty" ] && msg="$msg (+ uncommittete Änderungen)"
  msg="$msg. Vor Session-Ende alles nach main zusammenfuehren, dann diesen Branch loeschen: git branch -d $current und git push origin --delete $current"
  # msg enthaelt keine JSON-Sonderzeichen (keine Doublequotes/Backslashes) -> direkt einbetten
  printf '{"systemMessage": "%s"}\n' "$msg"
fi

exit 0
