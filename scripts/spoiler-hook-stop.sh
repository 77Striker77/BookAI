#!/usr/bin/env bash
# ============================================================================
# Stop-/SubagentStop-Hook — das Netz unter der Ausgabe (eingeführt 2026-08-11).
#
# Prüft zwei Dinge, bevor die Antwort stehen bleibt:
#   1. die ANTWORT selbst (Chat ist auch eine Ausgabe!)
#   2. die Artefakte auf der Platte — und ob sie seit ihrer letzten Änderung
#      überhaupt durchs Gate gelaufen sind (.claude/state/spoiler-gate.json)
#
# VERSTOSS  -> exit 2: Claude darf nicht stoppen, muss bereinigen.
# WARNUNG   -> systemMessage (sichtbarer Hinweis, kein Block).
# Jeder unerwartete Fehler => exit 0 (der Hook darf nie die Arbeit sprengen).
# ============================================================================
set -uo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root" 2>/dev/null || exit 0

payload="$(cat 2>/dev/null || true)"
command -v python3 >/dev/null 2>&1 || exit 0
have_jq=0; command -v jq >/dev/null 2>&1 && have_jq=1

ereignis="stop"
antwort=""
if [ "$have_jq" -eq 1 ] && [ -n "$payload" ]; then
  ereignis="$(jq -r '.hook_event_name // "Stop"' <<<"$payload" 2>/dev/null)"
  # Feldname je nach Ereignis/Version unterschiedlich -> defensiv mehrere probieren
  antwort="$(jq -r '
      .last_assistant_message // .last_message // .response //
      .agent_output // .result // .output // ""' <<<"$payload" 2>/dev/null)"
fi

meldungen=""
blocken=0

pruefe() {   # $1 = Text, $2 = Herkunft, $3 = Bezeichnung
  local text="$1" herkunft="$2" name="$3" out code
  [ -z "${text//[[:space:]]/}" ] && return 0
  out="$(printf '%s' "$text" \
        | python3 scripts/spoiler_check.py --stdin --herkunft "$herkunft" --quiet 2>/dev/null)"
  code=$?
  [ "$code" -eq 0 ] && return 0
  meldungen="${meldungen}
── ${name} ──
${out}"
  [ "$code" -eq 2 ] && blocken=1
  return 0
}

# --- 1. die Antwort selbst ---------------------------------------------------
if [ "$ereignis" = "SubagentStop" ]; then
  pruefe "$antwort" "subagent" "Rückgabe des Subagenten"
else
  pruefe "$antwort" "chat" "Antwort im Chat"
fi

# --- 2. Artefakte + Gate-Nachweis -------------------------------------------
if [ "$ereignis" != "SubagentStop" ]; then
  for f in artifacts/*.html; do
    [ -e "$f" ] || continue
    out="$(python3 scripts/spoiler_check.py --quiet --gate "$f" 2>/dev/null)"; code=$?
    if [ "$code" -ne 0 ]; then
      meldungen="${meldungen}
── ${f} ──
${out}"
      [ "$code" -eq 2 ] && blocken=1
    fi
  done
fi

[ -z "${meldungen//[[:space:]]/}" ] && exit 0

if [ "$blocken" -eq 1 ]; then
  {
    echo "🔒 SPOILER-GATE: Diese Ausgabe verrät etwas, das der Nutzer noch nicht gelesen/gehört hat."
    echo "$meldungen"
    echo
    echo "Zu tun (Reihenfolge):"
    echo "  1. Handlung entfernen — Metadaten NICHT anfassen (Politik §2)."
    echo "  2. Statt zu glätten: '🔒 Details zu Bd. X+ zurückgehalten' schreiben (§7)."
    echo "  3. Bei Unsicherheit den Agenten 'spoiler-guard' laufen lassen."
    echo "  4. Erneut prüfen: bash scripts/spoiler-gate.sh"
    echo "Regeln: vault/_System/Spoiler-Politik.md · Grenzen: python3 scripts/spoiler_check.py --grenzen"
  } >&2
  exit 2
fi

if [ "$have_jq" -eq 1 ]; then
  kurz="$(printf '%s' "$meldungen" | tr '\n' ' ' | cut -c1-600)"
  jq -n --arg m "🔒 Spoiler-Check: Warnung(en) offen — bitte vom 'spoiler-guard' beurteilen lassen. $kurz" \
    '{systemMessage: $m}'
fi
exit 0
