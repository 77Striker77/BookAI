#!/usr/bin/env python3
"""
verbleib_pruefen.py — Nachweis zur Zeile-für-Zeile-Bereinigung (Phase 3, 2026-10-11).

Vergleicht Fakten- und Erlebnis-Notiz eines Werks mit einem früheren Commit und prüft:
  1. Jede alte Zeile (nicht leer), die in KEINER der beiden neuen Notizen mehr wörtlich
     vorkommt, muss im Protokoll scripts/umbau/protokoll/<Werk>.md stehen — erste
     Tabellenspalte als „F 12“, „E 30–34“, „F 84–92“ usw. (Zeilennummern = alter Stand).
  2. Beide Frontmatter sind gültiges YAML (wenn PyYAML vorhanden ist).
  3. Jede Markdown-Tabelle hat in Kopf- und Trennzeile gleich viele Spalten.

Aufruf:
  python scripts/umbau/verbleib_pruefen.py "<Werk>" <alter-commit>
Exit 0 = alles belegt, 1 = Lücken.
"""
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]


def pfade(werk):
    return (f"vault/Werke/Buecher/{werk}.md", f"vault/Personen/Lucas/Erlebnisse/{werk} – Lucas.md")


def alt(rev, pfad):
    r = subprocess.run(["git", "show", f"{rev}:{pfad}"], cwd=REPO, capture_output=True)
    if r.returncode:
        sys.exit(f"git show {rev}:{pfad} fehlgeschlagen")
    return r.stdout.decode("utf-8").replace("\r\n", "\n").split("\n")


def protokoll_zeilen(werk):
    p = REPO / "scripts" / "umbau" / "protokoll" / f"{werk}.md"
    if not p.exists():
        return None
    gedeckt = {"F": set(), "E": set()}
    for z in p.read_text(encoding="utf-8").split("\n"):
        if not z.startswith("|"):
            continue
        erste = z.strip("|").split("|")[0]
        for seite, a, b in re.findall(r"\b([FE])\s*(\d+)(?:\s*[–-]\s*(\d+))?", erste):
            a = int(a); b = int(b) if b else a
            gedeckt[seite].update(range(a, b + 1))
    return gedeckt


def tabellen_ok(text, name):
    fehler = []
    zeilen = text.split("\n")
    for i in range(1, len(zeilen)):
        if re.match(r"^\s*\|(\s*:?-{3,}:?\s*\|)+\s*$", zeilen[i]) and zeilen[i - 1].lstrip().startswith("|"):
            k = zeilen[i - 1].strip().strip("|").count("|") + 1
            t = zeilen[i].strip().strip("|").count("|") + 1
            if k != t:
                fehler.append(f"{name} Z. {i}: Tabellenkopf {k} Spalten, Trennzeile {t}")
    return fehler


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    werk, rev = sys.argv[1], sys.argv[2]
    pf, pe = pfade(werk)
    neu_f = (REPO / pf).read_text(encoding="utf-8")
    neu_e = (REPO / pe).read_text(encoding="utf-8")
    neu = set(neu_f.split("\n")) | set(neu_e.split("\n"))
    gedeckt = protokoll_zeilen(werk)
    probleme = []
    if gedeckt is None:
        probleme.append(f"Protokoll scripts/umbau/protokoll/{werk}.md fehlt")
        gedeckt = {"F": set(), "E": set()}
    geaendert = 0
    for seite, pfad in (("F", pf), ("E", pe)):
        for nr, z in enumerate(alt(rev, pfad), 1):
            if z.strip() and z not in neu:
                geaendert += 1
                if nr not in gedeckt[seite]:
                    probleme.append(f"{seite} {nr} nicht im Protokoll: {z[:110]}")
    try:
        import yaml
        for name, t in (("F", neu_f), ("E", neu_e)):
            try:
                yaml.safe_load(t[3:t.find("\n---", 3)])
            except Exception as ex:
                probleme.append(f"{name}: Frontmatter kein gültiges YAML ({str(ex).splitlines()[0]})")
    except ImportError:
        print("   (PyYAML fehlt — YAML nicht geprüft)")
    probleme += tabellen_ok(neu_f, "F") + tabellen_ok(neu_e, "E")
    print(f"■ {werk}: {geaendert} alte Zeilen geändert/verschoben", end="")
    if probleme:
        print(f" — ❌ {len(probleme)} Problem(e)")
        for p in probleme:
            print(f"   - {p}")
        return 1
    print(" — ✅ alle im Protokoll belegt, YAML und Tabellen ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
