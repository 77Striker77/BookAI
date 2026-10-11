#!/usr/bin/env python3
"""
vault_pruefen.py — Prüfnetz für den Vault (eingeführt 2026-10-11, Phase 1 des Umbaus).

Zweck: Beim Umbau und im Alltag darf keine Notiz und kein Link verloren gehen.
Das Skript vergleicht den aktuellen Vault mit der gespeicherten Zählung in
scripts/vault-zaehlung.json und meldet:

  FEHLER   (Exit 1, Commit wird vom pre-commit-Hook gestoppt)
    - Notiz ohne oder mit offenem Frontmatter (--- … ---)
    - weniger Notizen als in der Zählung
    - Wikilinks um mehr als 1 % weniger als in der Zählung
    - mehr tote Links als in der Zählung
  WARNUNG  (Exit 0)
    - Wikilinks leicht weniger (≤ 1 %), z. B. weil ein Satz umgeschrieben wurde

Tote Links gibt es in zwei Sorten:
  umbrochen — der Linkname enthält einen Zeilenumbruch; Obsidian löst das nicht auf
  fehlt     — keine Notiz mit diesem Namen
Notizen unter vault/_System/ (Templates, Beispiele in den Konventionen) zählen
bei den toten Links nicht mit — dort sind Platzhalter gewollt.

Aufruf:
  python scripts/vault_pruefen.py            prüfen
  python scripts/vault_pruefen.py --liste    zusätzlich jeden toten Link mit Fundstelle
  python scripts/vault_pruefen.py --setzen   Zählung bewusst neu setzen (z. B. nach
                                             gewolltem Löschen) — im Commit begründen

Nur Standardbibliothek.
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
VAULT = REPO / "vault"
ZAEHLUNG = REPO / "scripts" / "vault-zaehlung.json"
AUSNAHME = VAULT / "_System"

LINK = re.compile(r"\[\[([^\]\|#]*)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
TOLERANZ_LINKS = 0.01


def frontmatter_ok(text):
    if not text.startswith("---"):
        return "kein Frontmatter"
    if re.search(r"\n---[ \t]*\r?(\n|$)", text[3:]) is None:
        return "Frontmatter nicht geschlossen"
    return None


def lesen():
    notizen = sorted(VAULT.rglob("*.md"))
    namen = {p.stem.lower() for p in notizen}
    dateien = {p.name.lower() for p in VAULT.rglob("*") if p.is_file()}

    fehler_fm, tote, ordner = [], [], {}
    links_gesamt = 0
    for p in notizen:
        rel = p.relative_to(VAULT)
        schluessel = "/".join(rel.parts[:2]) if len(rel.parts) > 2 else (rel.parts[0] if len(rel.parts) > 1 else ".")
        ordner[schluessel] = ordner.get(schluessel, 0) + 1

        text = p.read_text(encoding="utf-8")
        grund = frontmatter_ok(text)
        if grund:
            fehler_fm.append((rel.as_posix(), grund))

        zaehlt_tot = AUSNAHME not in p.parents
        for m in LINK.finditer(text):
            ziel = m.group(1).strip()
            if not ziel:
                continue
            links_gesamt += 1
            if not zaehlt_tot:
                continue
            if "\n" in ziel:
                tote.append((rel.as_posix(), ziel, "umbrochen"))
                continue
            basis = ziel.split("/")[-1].lower()
            if basis not in namen and basis not in dateien:
                tote.append((rel.as_posix(), ziel, "fehlt"))

    return {
        "notizen": len(notizen),
        "wikilinks": links_gesamt,
        "tote_links": len(tote),
        "ordner": dict(sorted(ordner.items())),
    }, fehler_fm, tote


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Prüfnetz für den Vault")
    ap.add_argument("--liste", action="store_true", help="tote Links einzeln ausgeben")
    ap.add_argument("--setzen", action="store_true", help="Zählung neu setzen")
    args = ap.parse_args()

    ist, fehler_fm, tote = lesen()
    soll = json.loads(ZAEHLUNG.read_text(encoding="utf-8")) if ZAEHLUNG.exists() else None

    print("📋 VAULT-PRÜFUNG")
    print(f"   Notizen {ist['notizen']} · Wikilinks {ist['wikilinks']} · tote Links {ist['tote_links']}"
          + (f"  (Zählung: {soll['notizen']} · {soll['wikilinks']} · {soll['tote_links']})" if soll else ""))

    fehler, warnungen = [], []
    for datei, grund in fehler_fm:
        fehler.append(f"{datei}: {grund}")

    if args.setzen:
        if fehler:
            print("\n❌ Zählung NICHT gesetzt — erst diese Fehler beheben:")
            for f in fehler:
                print(f"   - {f}")
            return 1
        ist["stand"] = datetime.date.today().isoformat()
        ZAEHLUNG.write_text(json.dumps(ist, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n✅ Zählung gesetzt: {ZAEHLUNG.relative_to(REPO).as_posix()}")
        return 0

    if soll is None:
        fehler.append("scripts/vault-zaehlung.json fehlt — einmal mit --setzen anlegen")
    else:
        if ist["notizen"] < soll["notizen"]:
            fehler.append(f"{soll['notizen'] - ist['notizen']} Notiz(en) weniger als in der Zählung")
        if ist["wikilinks"] < soll["wikilinks"]:
            weniger = soll["wikilinks"] - ist["wikilinks"]
            text = f"{weniger} Wikilink(s) weniger als in der Zählung"
            (fehler if weniger > soll["wikilinks"] * TOLERANZ_LINKS else warnungen).append(text)
        if ist["tote_links"] > soll["tote_links"]:
            fehler.append(f"{ist['tote_links'] - soll['tote_links']} toter Link/tote Links mehr als in der Zählung"
                          " (--liste zeigt alle)")
        for k in sorted(set(soll.get("ordner", {})) | set(ist["ordner"])):
            a, b = soll.get("ordner", {}).get(k, 0), ist["ordner"].get(k, 0)
            if a != b:
                print(f"   ↳ {k}: {a} → {b}")

    if args.liste and tote:
        print("\nTote Links (außerhalb _System):")
        for datei, ziel, art in tote:
            print(f"   [{art:9}] {datei}: [[{ziel.replace(chr(10), '⏎')}]]")

    for w in warnungen:
        print(f"⚠️  {w}")
    if fehler:
        print("\n❌ Vault-Prüfung fehlgeschlagen:")
        for f in fehler:
            print(f"   - {f}")
        print("\n   Gewollt (z. B. Notiz bewusst gelöscht)? → python scripts/vault_pruefen.py --setzen"
              "\n   und den Grund in die Commit-Nachricht schreiben.")
        return 1
    print("✅ Vault-Prüfung bestanden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
