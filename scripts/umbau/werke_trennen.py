#!/usr/bin/env python3
"""
werke_trennen.py — Phase 3 des Umbaus (2026-10-11): Werk-Notizen in Fakten und Erleben trennen.

  vault/Bibliothek/Werke/<Werk>.md
    → vault/Werke/Buecher/<Werk>.md                     Fakten (einmal je Werk)
    → vault/Personen/Lucas/Erlebnisse/<Werk> – Lucas.md  Erleben (je Person)

Getrennt wird abschnittsweise (Entscheidung Lucas 2026-10-11, Variante A):
  - Frontmatter: Schlüssel aus ERLEBNIS_KEYS wandern ins Erleben, der Rest bleibt.
  - Body: jeder ##-Abschnitt nach seiner Überschrift; einzelne ###-Abschnitte
    können ins Erleben umgeleitet werden. Gemischte Abschnitte gehen ganz ins Erleben.
  - Unbekannte Überschrift → Abbruch, nichts wird geschrieben.

Beweis: Jede Zeile der alten Notiz taucht in genau einer der beiden neuen Notizen
wieder auf (Zeilen-Multimenge alt == Fakten + Erleben, ohne die neu erzeugten Zeilen).

Aufruf:
  python scripts/umbau/werke_trennen.py              Probelauf, zeigt die Zuordnung
  python scripts/umbau/werke_trennen.py --schreiben  ausführen (git mv + schreiben)

Nur Standardbibliothek.
"""
import argparse
import collections
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
ALT = REPO / "vault" / "Bibliothek" / "Werke"
FAKTEN = REPO / "vault" / "Werke" / "Buecher"
PERSON = "Lucas"
ERLEBNIS = REPO / "vault" / "Personen" / PERSON / "Erlebnisse"

ERLEBNIS_KEYS = {
    "verdict", "verdict_status", "wiedervorlage", "format_erlebt", "sprache_erlebt",
    "bewertung", "sprecher_bewertung", "kontext", "tags",
    "spoiler_erlebt_bis", "spoiler_aktuell", "spoiler_gesamt", "spoiler_stand",
    "spoiler_sperrbegriffe", "spoiler_unerlebte_reihen",
}

H2_ERLEBNIS = ("Lesestand", "⭐ Bewertung", "⭐ Summe der Bewertungen", "Abweichungen",
               "Hörbuch-Erlebnis", "🎧 Hörbuch-Erlebnis", "DNA-Begründung",
               "🧮 Reihen-Gesamtbild", "Mein Kontrast")
H2_FAKTEN = ("Offene Fragen", "🗓️", "📚", "🗺️", "🗃️", "📇", "👥", "Hierarchie", "DNA (",
             "🔊", "🔀", "🧮 Community-Gesamtbild", "🎧 EMPFOHLENE")
H3_ERLEBNIS = ("Band-Unterschiede", "Auffällige Band-Unterschiede", "🙈 Spoiler-Regel")

F, E = "F", "E"


def zuordnung_h2(titel):
    if titel.startswith(H2_ERLEBNIS):
        return E
    if titel.startswith(H2_FAKTEN):
        return F
    return None


def trennen(pfad):
    zeilen = pfad.read_text(encoding="utf-8").split("\n")
    assert zeilen[0].strip() == "---", f"{pfad.name}: kein Frontmatter"
    ende = next(i for i in range(1, len(zeilen)) if zeilen[i].strip() == "---")
    fm, body = zeilen[1:ende], zeilen[ende + 1:]

    # --- Frontmatter: Kommentarzeilen hängen am folgenden, Fortsetzungen am vorigen Schlüssel
    fm_ziel, offen_kommentare, aktuell = [], [], F
    for z in fm:
        s = z.strip()
        if s.startswith("#"):
            offen_kommentare.append(z)
            continue
        if z and not z[0].isspace() and not s.startswith("-") and ":" in z:
            aktuell = E if z.split(":", 1)[0].strip() in ERLEBNIS_KEYS else F
        fm_ziel += [(k, aktuell) for k in offen_kommentare] + [(z, aktuell)]
        offen_kommentare = []
    fm_ziel += [(k, F) for k in offen_kommentare]

    # --- Body: Einleitung bis zum ersten ## bleibt Fakten
    body_ziel, fehler, protokoll = [], [], []
    h2, h3, im_code = F, None, False
    for z in body:
        if z.lstrip().startswith("```"):
            im_code = not im_code
        if not im_code and z.startswith("## "):
            t = z[3:].strip()
            h2, h3 = zuordnung_h2(t), None
            if h2 is None:
                fehler.append(f"unbekannte Überschrift: {z}")
                h2 = F
            protokoll.append((h2, z))
        elif not im_code and z.startswith("### "):
            h3 = E if z[4:].strip().startswith(H3_ERLEBNIS) else None
            if h3:
                protokoll.append((h3, z))
        elif not im_code and z.startswith("# "):
            h3 = None
        body_ziel.append((z, h3 or h2))

    return fm_ziel, body_ziel, fehler, protokoll


def bauen(stem, fm_ziel, body_ziel):
    """Liefert (fakten, erleben) als Listen von (zeile, erzeugt?)."""
    erl_name = f"{stem} – {PERSON}"
    werk_typ = next((z.split(":", 1)[1].strip().strip('"') for z, _ in fm_ziel
                     if z.startswith("werk_typ:")), "werk")

    fak = [("---", True)]
    for z, ziel in fm_ziel:
        if ziel == F:
            fak.append((z, False))
            if z.startswith("titel:"):
                fak.append(('bereich: "buch"', True))
    fak += [(f"erlebnisse: [\"[[{erl_name}]]\"]", True),
            (f"tags: [werk, buch, {werk_typ}]", True), ("---", True)]

    h1_gesetzt = False
    for z, ziel in body_ziel:
        if ziel != F:
            continue
        fak.append((z, False))
        if not h1_gesetzt and z.startswith("# "):
            fak += [("", True),
                    (f"> 👤 **Erleben je Person:** [[{erl_name}]] — Lesestand, Bewertung, Verdikt.", True)]
            h1_gesetzt = True

    erl = [("---", True), (f'werk: "[[{stem}]]"', True), (f'person: "{PERSON}"', True),
           ('bereich: "buch"', True)]
    erl += [(z, False) for z, ziel in fm_ziel if ziel == E]
    erl += [("---", True), ("", True), (f"# {erl_name}", True), ("", True),
            (f"Mein Erleben von [[{stem}]]. Fakten, Bände und Metadaten stehen dort — "
             f"hier nur, was {PERSON} erlebt und empfunden hat.", True), ("", True)]
    erl += [(z, False) for z, ziel in body_ziel if ziel == E]
    return fak, erl


def beweis(pfad, fak, erl):
    alt = pfad.read_text(encoding="utf-8").split("\n")
    ende = next(i for i in range(1, len(alt)) if alt[i].strip() == "---")
    alt = alt[1:ende] + alt[ende + 1:]
    neu = [z for z, erzeugt in fak + erl if not erzeugt]
    a, n = collections.Counter(alt), collections.Counter(neu)
    return a - n, n - a


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--schreiben", action="store_true")
    args = ap.parse_args()

    werke = sorted(ALT.glob("*.md"))
    plan, alle_fehler = [], []
    for p in werke:
        fm_ziel, body_ziel, fehler, protokoll = trennen(p)
        fak, erl = bauen(p.stem, fm_ziel, body_ziel)
        fehlt, zuviel = beweis(p, fak, erl)
        n_f = sum(1 for _, e in fak if not e)
        n_e = sum(1 for _, e in erl if not e)
        print(f"\n■ {p.name}: {n_f} Zeilen Fakten · {n_e} Zeilen Erleben"
              f" · Beweis {'✅' if not fehlt and not zuviel else '❌'}")
        for ziel, z in protokoll:
            print(f"    {'Fakten ' if ziel == F else 'Erleben'}  {z}")
        fm_e = [z.split(':')[0] for z, ziel in fm_ziel if ziel == E and ':' in z and not z[0].isspace()
                and not z.strip().startswith(('#', '-'))]
        print(f"    Frontmatter → Erleben: {', '.join(fm_e)}")
        for f in fehler:
            alle_fehler.append(f"{p.name}: {f}")
        if fehlt or zuviel:
            alle_fehler.append(f"{p.name}: Beweis fehlgeschlagen (fehlt {sum(fehlt.values())}, "
                               f"zuviel {sum(zuviel.values())})")
        plan.append((p, fak, erl))

    print(f"\n{len(werke)} Werke geprüft.")
    if alle_fehler:
        print("❌ Abbruch, nichts geschrieben:")
        for f in alle_fehler:
            print(f"   - {f}")
        return 1
    if not args.schreiben:
        print("✅ Probelauf sauber. Ausführen mit --schreiben.")
        return 0

    FAKTEN.mkdir(parents=True, exist_ok=True)
    ERLEBNIS.mkdir(parents=True, exist_ok=True)
    for p, fak, erl in plan:
        ziel_f = FAKTEN / p.name
        ziel_e = ERLEBNIS / f"{p.stem} – {PERSON}.md"
        assert not ziel_f.exists() and not ziel_e.exists(), f"Ziel existiert schon: {p.name}"
        subprocess.run(["git", "mv", str(p), str(ziel_f)], cwd=REPO, check=True)
        ziel_f.write_text("\n".join(z for z, _ in fak), encoding="utf-8")
        ziel_e.write_text("\n".join(z for z, _ in erl).rstrip("\n") + "\n", encoding="utf-8")
    print(f"✅ {len(plan)} Werke getrennt → {FAKTEN.relative_to(REPO).as_posix()} + "
          f"{ERLEBNIS.relative_to(REPO).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
