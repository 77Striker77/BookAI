#!/usr/bin/env bash
# ============================================================================
# spoiler-gate.sh — das Gate von Hand: prüft ALLES, was rausgeht.
#
#   bash scripts/spoiler-gate.sh                 # Artefakte + Vault
#   bash scripts/spoiler-gate.sh <datei> …       # gezielt
#
# Pflichtschritt vor jedem Artefakt-Publish (zusammen mit scripts/vault-first.sh).
# Deckt die DETERMINISTISCHE Hälfte ab — die semantische macht der Agent
# 'spoiler-guard'. Beide sind Pflicht; dieses Skript erinnert daran.
#
# Exit 0 = sauber · 1 = Warnungen · 2 = VERSTOSS (nicht publizieren!)
# ============================================================================
set -uo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

echo "🔒 SPOILER-GATE — Grenzen aus dem Vault, Regeln aus _System/Spoiler-Politik.md"
echo

schlimmster=0
merke() { [ "$1" -gt "$schlimmster" ] && schlimmster="$1"; return 0; }

if [ "$#" -gt 0 ]; then
  python3 scripts/spoiler_check.py --gate "$@"; merke $?
else
  echo "▸ Artefakte (harte Ausgabe — hier blockt ein Verstoß den Publish)"
  shopt -s nullglob
  artefakte=(artifacts/*.html)
  if [ "${#artefakte[@]}" -gt 0 ]; then
    python3 scripts/spoiler_check.py --gate "${artefakte[@]}"; merke $?
  else
    echo "  (keine Artefakte gefunden)"
  fi
  echo
  echo "▸ Vault (Details erlaubt, aber nur im 🔒-Block)"
  vaultdateien=(vault/Bibliothek/Werke/*.md vault/Empfehlungen/Kandidaten/*.md
                vault/Empfehlungen/Läufe/*.md vault/Profil/Interviews/*.md)
  if [ "${#vaultdateien[@]}" -gt 0 ]; then
    python3 scripts/spoiler_check.py --quiet --herkunft vault "${vaultdateien[@]}"; merke $?
    [ "$?" -eq 0 ] && echo "  ✅ sauber"
  fi
fi

echo
echo "──────────────────────────────────────────────────────────────"
case "$schlimmster" in
  0) echo "✅ Deterministisch sauber."
     echo "   Fehlt noch die SEMANTISCHE Hälfte: Agent 'spoiler-guard' laufen lassen"
     echo "   (Paraphrasen und Andeutungen sieht keine Wortliste)." ;;
  1) echo "⚠️  Warnungen offen — vom 'spoiler-guard' beurteilen lassen, bevor publiziert wird." ;;
  *) echo "⛔ VERSTOSS — nicht publizieren. Handlung raus, Metadaten bleiben (Politik §2/§3)."
     echo "   Statt zu glätten: '🔒 Details zu Bd. X+ zurückgehalten' (§7)." ;;
esac
exit "$schlimmster"
