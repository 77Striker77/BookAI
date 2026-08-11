#!/usr/bin/env bash
# ============================================================================
# spoiler-selftest.sh — prüft den Spoiler-Linter gegen tests/spoiler/faelle/.
#
# Jeder Fall trägt einen Kopf:
#     # erwartung: verstoss | warnung | sauber
#     # herkunft:  artefakt | empfehlung | kandidat | chat | subagent | vault
#     # vault:     echt | fixture      (fixture = tests/spoiler/fixture)
#     # was:       wozu der Fall da ist
#
# Zweck: Positivfälle (muss greifen) UND Negativfälle (darf NICHT greifen) —
# ein Spoiler-Checker, der Fehlalarme produziert, wird ignoriert und ist damit
# schlimmer als keiner. Jede neue Regel im Lexikon braucht beide Sorten.
#
# Exit 0 = alle Fälle wie erwartet · Exit 1 = mindestens ein Fall weicht ab.
# ============================================================================
set -uo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

faelle_dir="tests/spoiler/faelle"
[ -d "$faelle_dir" ] || { echo "Keine Testfälle unter $faelle_dir"; exit 1; }

gesamt=0; ok=0; fehler=0
falsch_negativ=0   # Spoiler durchgerutscht (gefährlich)
falsch_positiv=0   # Fehlalarm (macht das Gate unbrauchbar)

kopf() { grep -m1 "^# $1:" "$2" 2>/dev/null | sed "s/^# $1:[[:space:]]*//" | tr -d '\r'; }

echo "🔒 SPOILER-SELBSTTEST"
echo

for f in "$faelle_dir"/*.txt; do
  [ -e "$f" ] || continue
  gesamt=$((gesamt+1))
  erwartung="$(kopf erwartung "$f")"; erwartung="${erwartung:-sauber}"
  herkunft="$(kopf herkunft "$f")";   herkunft="${herkunft:-artefakt}"
  vault="$(kopf vault "$f")";         vault="${vault:-echt}"
  was="$(kopf was "$f")"

  root_arg=()
  [ "$vault" = "fixture" ] && root_arg=(--root "$repo_root/tests/spoiler/fixture")

  # Kopfzeilen entfernen, Rest prüfen
  grep -v '^# \(erwartung\|herkunft\|vault\|was\):' "$f" \
    | python3 scripts/spoiler_check.py --stdin --herkunft "$herkunft" \
        --quiet "${root_arg[@]}" >/tmp/spoiler-selftest.out 2>&1
  code=$?

  case "$code" in
    0) ist="sauber" ;;
    1) ist="warnung" ;;
    2) ist="verstoss" ;;
    *) ist="FEHLER($code)" ;;
  esac

  if [ "$ist" = "$erwartung" ]; then
    ok=$((ok+1))
    printf '  ✅ %-46s %s\n' "$(basename "$f")" "$erwartung"
  else
    fehler=$((fehler+1))
    # Härte vergleichen: erwartet streng, bekommen lasch = falsch negativ
    rang() { case "$1" in sauber) echo 0;; warnung) echo 1;; verstoss) echo 2;; *) echo 9;; esac; }
    if [ "$(rang "$ist")" -lt "$(rang "$erwartung")" ]; then
      falsch_negativ=$((falsch_negativ+1)); art="DURCHGERUTSCHT"
    else
      falsch_positiv=$((falsch_positiv+1)); art="FEHLALARM"
    fi
    printf '  ❌ %-46s erwartet=%-8s ist=%-8s  [%s]\n' \
      "$(basename "$f")" "$erwartung" "$ist" "$art"
    [ -n "$was" ] && printf '       Fall: %s\n' "$was"
    sed 's/^/       │ /' /tmp/spoiler-selftest.out | head -12
  fi
done
rm -f /tmp/spoiler-selftest.out

echo
echo "──────────────────────────────────────────────────────────────"
printf 'Fälle: %d · bestanden: %d · abweichend: %d\n' "$gesamt" "$ok" "$fehler"
if [ "$fehler" -gt 0 ]; then
  printf '   ⛔ durchgerutschte Spoiler: %d   (Regel fehlt oder ist zu lasch)\n' "$falsch_negativ"
  printf '   ⚠️  Fehlalarme:              %d   (Lexikon/Whitelist nachschärfen)\n' "$falsch_positiv"
  echo "   → Wortlisten liegen in vault/_System/Spoiler-Lexikon.md (nicht im Code!)."
  exit 1
fi
echo "✅ Alle Fälle wie erwartet."
exit 0
