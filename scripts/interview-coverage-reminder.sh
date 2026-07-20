#!/usr/bin/env bash
# ============================================================================
# Interview-Abdeckungs-Reminder (Stop-Hook) — eingeführt 2026-07-20.
# Stützt die PFLICHT-Abdeckungs-Matrix aus dem Skill 'book-taste-interview':
# jede Kern-Dimension muss POSITIV UND NEGATIV getrennt abgefragt sein.
#
# Der Hook kann den Dialog nicht mitlesen, prüft daher einen konkreten,
# überprüfbaren Stellvertreter: enthält die JÜNGSTE Interview-Notiz (die in
# dieser Session angefasst wurde) den Abschnitt "Abdeckungs-Matrix"? Der Skill
# verlangt, die AUSGEFÜLLTE Matrix ins Protokoll aufzunehmen. Fehlt sie in einer
# frischen Notiz -> Erinnerung (blockiert NICHT, analog Branch-Reminder).
# Gibt einen 'systemMessage' aus (für den Nutzer sichtbar), sonst nichts.
# ============================================================================
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root" 2>/dev/null || exit 0

# stdin (Hook-Payload) verwerfen
cat >/dev/null 2>&1 || true

dir="vault/Profil/Interviews"
[ -d "$dir" ] || exit 0

# Jüngste Interview-Notiz nach Änderungszeit finden (portabel: mtime via stat).
newest=""
newest_mtime=0
while IFS= read -r -d '' f; do
  m="$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null || echo 0)"
  if [ "${m:-0}" -gt "$newest_mtime" ]; then
    newest_mtime="$m"; newest="$f"
  fi
done < <(find "$dir" -type f -name '*.md' -print0 2>/dev/null)

[ -z "$newest" ] && exit 0

# Nur reagieren, wenn die Notiz in dieser Session frisch ist (<= 6 h alt) —
# sonst ist es eine Altnotiz und kein aktuelles Interview.
now="$(date +%s 2>/dev/null || echo 0)"
age=$(( now - newest_mtime ))
[ "$age" -gt 21600 ] && exit 0
[ "$age" -lt 0 ] && exit 0

# Enthält die Notiz die (ausgefüllte) Abdeckungs-Matrix? Dann ist alles gut.
if grep -qi "Abdeckungs-Matrix" "$newest" 2>/dev/null; then
  exit 0
fi

base="$(basename "$newest")"
msg="🎤 Interview-Skill: In der frischen Notiz '$base' fehlt die Abdeckungs-Matrix. Skill-Pflicht: jede Kern-Dimension (Held/Welt/Plot/Tempo/Ton/Sprecher) POSITIV UND NEGATIV getrennt abfragen und die ausgefuellte Matrix ins Protokoll aufnehmen, bevor an book-deep-analysis uebergeben wird."
# msg enthaelt keine JSON-Sonderzeichen (keine Doublequotes/Backslashes) -> direkt einbetten
printf '{"systemMessage": "%s"}\n' "$msg"
exit 0
