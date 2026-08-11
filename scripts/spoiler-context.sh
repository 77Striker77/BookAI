#!/usr/bin/env bash
# ============================================================================
# SessionStart-Hook — kippt die Spoiler-Grenzen sofort in den Kontext.
#
# Damit weiß jede Session ab Zeile 1, wie weit der Nutzer in welchem Werk ist —
# ohne dass jemand erst Dateien lesen muss. Das ist die billigste und wirksamste
# Schicht: Der Fehler passiert meist, weil die Grenze gar nicht präsent war.
# ============================================================================
set -uo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root" 2>/dev/null || exit 0
cat >/dev/null 2>&1 || true

command -v python3 >/dev/null 2>&1 || exit 0
command -v jq >/dev/null 2>&1 || exit 0

grenzen="$(python3 scripts/spoiler_check.py --grenzen 2>/dev/null)"
[ -z "$grenzen" ] && exit 0

kontext="$(cat <<EOF
🔒 SPOILER-POLITIK IST AKTIV (Regeln: vault/_System/Spoiler-Politik.md)

In JEDER Ausgabe (Artefakt, Chat-Antwort, Subagenten-Rückgabe) darf nichts stehen, was
der Nutzer noch nicht gelesen/gehört hat. Was er erlebt hat, darf ausdrücklich
DETAILLIERTER beschrieben werden. Metadaten (Titel, Daten, ISBN, Seiten, Hördauer,
Sprecher, Wertungen, Bekanntheit) sind NIE ein Spoiler — die volle Datendichte bleibt.
Der laufende Band gilt als NICHT erlebt. Unbekanntes Werk = ungelesen (fail-closed).
Nie stillschweigend glätten — stattdessen "🔒 Details zu Bd. X+ zurückgehalten" schreiben.

$grenzen

Prüfen: python3 scripts/spoiler_check.py <datei>  ·  vor Publish: bash scripts/spoiler-gate.sh
Semantisch prüfen lassen: Agent 'spoiler-guard' (Pflicht vor jedem Artefakt-Publish).
EOF
)"

jq -n --arg c "$kontext" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: $c
  }
}'
exit 0
