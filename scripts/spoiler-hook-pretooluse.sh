#!/usr/bin/env bash
# ============================================================================
# PreToolUse-Hook — das harte Tor (eingeführt 2026-08-11).
#
# Greift bei:
#   Artifact           -> prüft die Datei, die publiziert werden soll  (VERSTOSS = deny)
#   Write/Edit/MultiEdit -> prüft den Inhalt, der geschrieben werden soll
#
# Härte nach Ziel:
#   artifacts/**            hart  — VERSTOSS blockt (das ist die veröffentlichte Ausgabe)
#   vault/**                weich — Details erlaubt, aber nur im 🔒-Block (nur Hinweis)
#   sonstiges               weich — Hinweis
#
# Regeln/Grenzen kommen aus dem Vault (vault/_System/Spoiler-Politik.md).
# Der Hook darf NIE die Arbeit sprengen: jeder unerwartete Fehler => exit 0.
# ============================================================================
set -uo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root" 2>/dev/null || exit 0

payload="$(cat 2>/dev/null || true)"
[ -z "$payload" ] && exit 0
. "$repo_root/scripts/python-finden.sh"; [ -n "$PY" ] || exit 0

# JSON über Python statt jq (2026-10-11: unter Windows fehlt jq, der Hook schwieg dann)
feld() { printf '%s' "$payload" | $PY scripts/hook_json.py feld "$@" 2>/dev/null; }
tool="$(feld tool_name)"
pfad="$(feld tool_input.file_path tool_input.path)"

# Zu prüfenden Text einsammeln: bei Write der neue Inhalt, bei Edit die Ersetzung,
# bei Artifact die Datei auf der Platte.
inhalt=""
case "$tool" in
  Write)
    inhalt="$(feld tool_input.content)" ;;
  Edit)
    inhalt="$(feld tool_input.new_string)" ;;
  MultiEdit)
    inhalt="$(feld 'tool_input.edits[].new_string')" ;;
  Artifact)
    aktion="$(feld tool_input.action --standard publish)"
    [ "$aktion" = "list" ] && exit 0
    [ -f "$pfad" ] || exit 0
    inhalt="$(cat "$pfad" 2>/dev/null || true)" ;;
  *) exit 0 ;;
esac
[ -z "${inhalt//[[:space:]]/}" ] && exit 0

# Herkunft (bestimmt die Härte der Regeln) aus dem Zielpfad ableiten
rel="${pfad#$repo_root/}"
case "$rel" in
  *empfehlungen*|*Kandidaten*) herkunft="empfehlung" ;;
  artifacts/*|*/artifacts/*)   herkunft="artefakt" ;;
  vault/*|*/vault/*)           herkunft="vault" ;;
  *)                           herkunft="unbekannt" ;;
esac
[ "$tool" = "Artifact" ] && [ "$herkunft" = "unbekannt" ] && herkunft="artefakt"

bericht="$(printf '%s' "$inhalt" \
  | $PY scripts/spoiler_check.py --stdin --herkunft "$herkunft" --quiet 2>/dev/null)"
code=$?

# Hart blocken nur, wo eine echte Ausgabe entsteht
hart=0
case "$herkunft" in artefakt|empfehlung) hart=1 ;; esac
[ "$tool" = "Artifact" ] && hart=1

if [ "$code" -eq 2 ] && [ "$hart" -eq 1 ]; then
  grund="$(printf '🔒 SPOILER-GATE: blockiert.\n\n%s\n\nRegeln: vault/_System/Spoiler-Politik.md (§2 Neutralzone, §3 Verbotszone, §7 Zurückhalten statt Glätten).\nHandlung raus, Metadaten bleiben drin. Danach `spoiler-guard` laufen lassen und erneut versuchen.' "$bericht")"
  printf '%s' "$grund" | $PY scripts/hook_json.py ausgabe deny
  exit 0
fi

if [ "$code" -ne 0 ]; then
  hinweis="$(printf '🔒 Spoiler-Check (%s, nicht blockierend):\n%s' "$herkunft" "$bericht")"
  printf '%s' "$hinweis" | $PY scripts/hook_json.py ausgabe hinweis
fi
exit 0
