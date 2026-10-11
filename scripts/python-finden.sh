#!/usr/bin/env bash
# ============================================================================
# python-finden.sh — wird mit `. scripts/python-finden.sh` eingebunden und
# setzt $PY auf ein funktionierendes Python ≥ 3.8 (leer, wenn keines da ist).
#
# Warum (2026-10-11): Unter Windows ist `python3` meist nur der Platzhalter
# des Microsoft Store — `command -v python3` findet ihn, der Aufruf scheitert
# aber. Die Spoiler-Hooks liefen dort deshalb still ins Leere. Hier wird jeder
# Kandidat wirklich ausgeführt, statt nur gesucht.
#
# Aufruf danach unquotiert: `$PY scripts/spoiler_check.py …` (wegen "py -3").
# ============================================================================
PY=""
for _kandidat in python3 python "py -3"; do
  if $_kandidat -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" >/dev/null 2>&1; then
    PY="$_kandidat"
    break
  fi
done
unset _kandidat

# Windows-Python liest und schreibt sonst in cp1252 (Umlaute, Emojis, ⟨⟩).
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8
