---
name: book-reco-artifact
description: >
  Pflegt die ZWEI festen Artefakte des Buch-/Hörbuch-Systems: (1) "Meine Bibliothek" –
  Basis-Artefakt mit allen guten Büchern samt wichtigsten Infos/Metadaten, wird bei jeder
  neuen Titel-Analyse aktualisiert (gleiche URL); (2) "Empfehlungen" – wird bei jedem
  neuen Empfehlungslauf ÜBERSCHRIEBEN (gleiche URL), zeigt Kerndaten + ≥3 Empfehlungen
  mit %-Match-Balken und "Was passt / Was passt nicht". Nutze diesen Skill nach einer
  Titel-Analyse (→ Bibliothek updaten) oder am Ende eines Empfehlungslaufs (→ Empfehlungen
  überschreiben). NIEMALS zusätzliche neue Artefakte anlegen.
---

# Die zwei festen Artefakte

## ⚠️ OBERSTE REGEL zuerst — Vault → Artefakt, nie umgekehrt

Artefakte sind **reine Projektionen des Vaults** (`vault/`). Verbindlich (siehe `CLAUDE.md`):

1. **Nur aus dem Vault erzeugen.** Jede Zahl, jeder Titel, jeder Satz im Artefakt MUSS
   bereits im Vault stehen. Steht etwas nur „im Kopf" oder frisch recherchiert bereit →
   erst in den Vault schreiben, dann ins Artefakt.
2. **Nie Artefakt über Vault.** Enthält ein (auch veröffentlichtes) Artefakt Infos, die der
   Vault nicht hat → Bug: **erst in den Vault backporten**, dann das Artefakt neu erzeugen.
3. **Publish = Commit.** Reihenfolge IMMER: Vault schreiben → committen → Artefakt aus Vault
   erzeugen → publizieren → pushen. Vor Publish `bash scripts/vault-first.sh` laufen lassen;
   nie publizieren, solange Vault-Änderungen uncommittet sind (ephemerer Container → Verlust).
4. **Repo-Datei = Live-Version.** Nach dem Publish muss `artifacts/<name>.html` im Repo mit
   der veröffentlichten Fassung übereinstimmen und committet sein (sonst überschreibt ein
   späterer Publish die gute Live-Version mit altem Stand — Vorfall 2026-07-17).

# Es gibt genau zwei Artefakte

Es gibt **genau zwei** Artefakte — beide leben unter stabilen Dateipfaden im Repo und
werden **an Ort und Stelle aktualisiert**, nie neu erzeugt:

| # | Artefakt | Datei | Favicon | Wann aktualisieren |
|---|---|---|---|---|
| 1 | **Meine Bibliothek** (Basis) | `artifacts/bibliothek.html` | 📚 | nach jeder Titel-Analyse / Profil-Änderung |
| 2 | **Empfehlungen** | `artifacts/empfehlungen.html` | 🎯 | bei jedem Empfehlungslauf **komplett überschreiben** |

## URL-Stabilität (wichtig!)

- **Gleiche Session:** einfach die Datei editieren und mit dem Artifact-Tool unter
  demselben Pfad erneut publizieren → gleiche URL.
- **Neue Session:** die Artefakte existieren schon! Erst `Artifact(action:"list")`
  aufrufen, die URL von „Meine Bibliothek" bzw. „Empfehlungen" heraussuchen und beim
  Publish als `url:` mitgeben — sonst entsteht eine neue URL (verboten).
- Favicon und `<title>` **niemals ändern** (Wiedererkennung): „Meine Bibliothek" 📚,
  „Empfehlungen" 🎯.
- Beim Publish ein kurzes `label` setzen (z. B. `+titel-name` bzw. `lauf-2026-07-16`).

## Datenquellen (Vault — nie raten)

- `vault/Profil/Profil.md` (Übergreifendes) + `Kontexte/*.md` (Gewichte & Top-Merkmale
  je Geschmacksraum) + `Gewichte.md` (Fallback) + `No-Gos.md`.
- `vault/Bibliothek/Werke/*.md` — Werke (Reihen!) inkl. **Aspekt-Bewertungen** (`bewertung:`).
- `vault/Empfehlungen/Läufe/` — die **neueste** Lauf-Notiz, plus die zugehörigen
  Kandidaten-Notizen (`vault/Empfehlungen/Kandidaten/`, dort liegen Scores, Prognosen
  je Aspekt, ✓/✗, Quellen) für Artefakt 2.

**Darstellungs-Konsequenzen:** In "Meine Bibliothek" die Bücher **nach Kontext
gruppieren** (je Gruppe eigener Kerndaten-Block mit den Kontext-Gewichten); je Buchkarte
die stärksten +/−-Aspekte zeigen (z. B. "✚ Rahmenerzählung · − Mittelteil zieht").
Im "Empfehlungen"-Artefakt den Kontext des Laufs nennen und je Empfehlung die
aspekt-basierten ✓/✗ aus der Prognose verwenden.

Vorher `dataviz`-Skill lesen (Farben/Balken/Dark-Mode), Vorlagen als Startpunkt nutzen:
`references/bibliothek-template.html` und `references/empfehlungen-template.html`.
Beide sind self-contained & theme-aware (CSP: keine externen Requests; Cover als
data:-URI einbetten oder 📖-Platzhalter lassen).

## 🎨 Farb-System (VERBINDLICH, konsistent — nie vermischen!)

Es gibt **zwei semantisch verschiedene Skalen** — jede hat GENAU eine Farbrolle:

| Bedeutung | Farbe | gilt für |
|---|---|---|
| **Community-Wertung 0–5 Sterne** (Qualität, Magnitude) | **Blau** (`--rating`) | Band-Wertungsbalken, Gewichte |
| **Bekanntheit/Reichweite** (WIE VIELE bewerten → Nische↔Phänomen) | **Gold** (`--fame`) | Fame-Meter (5 Stufen), Hype-Badges |
| **positiv** (mein `＋`-Aspekt / Community 👍) | **Grün** (`--pos`) | ＋-Zeilen, 👍, loved-Chips |
| **negativ** (mein `−`-Aspekt / Community 👎 / No-Go) | **Rot** (`--neg`) | −-Zeilen, 👎, No-Go-Chips |
| Struktur/Text | warme Neutraltöne | alles andere |

**Bekanntheit ≠ Qualität:** Gold misst NUR Reichweite (Stimmenzahl, Hype), nie ob es gut
ist. 5 Stufen: Geheimtipp <1k · Szene-bekannt 1k–10k · Etabliert 10k–100k · Bestseller
100k–1 Mio · Phänomen >1 Mio (aus `bekanntheit_stufe`/`hype` im Vault).

**Eiserne Regeln:**
- **Rot bedeutet NIE eine Wertung** — nur „negativ / mag ich nicht". Eine 4,32/5 ist
  GUT → niemals rot; der relativ schwächste Band ist nur ein kürzerer **blauer** Balken
  (bester Band: ★, nicht farblich als „gut" umdeklarieren).
- **Wertungsbalken zeigen den Ausschnitt 4,0–5,0** (Achsen-Label + Hinweis Pflicht),
  damit man Unterschiede sieht — mit klarer Beschriftung „/5", sonst wird es als
  Prozent/1–10 fehlgelesen.
- **Grün/Rot immer mit Symbol** (＋/−, 👍/👎) — nie Farbe allein (Rot-Grün-Schwäche).
- Farb-Legende („Blau = Wertung 0–5 · Grün ＋ · Rot −") sichtbar einbauen.
- Palette per `dataviz`-Validator gegen beide Surfaces prüfen; Werte aus dem aktuellen
  `bibliothek.html` übernehmen (Tokens `--rating/--pos/--neg` + Dark-Mode-Stufen).

## Aufbau als Dashboard (Artefakt 1)

Kein langes Scroll-Dokument, sondern ein **Dashboard mit Sticky-Nav + Untermenü** und per
JS umschaltbaren Ansichten (Hash-Routing `#uebersicht/#werke/#bekanntheit/#releases/
#geschmack`; Werk-Anker `#dcc` etc. springen in die Werke-Ansicht):
- **Übersicht (Startseite):** Begrüßung, KPI-Kacheln, „Jetzt & als Nächstes" + roter
  Faden, **Bekanntheits-Ranking** (Gold-Meter), Mini-Werkkarten mit Cover.
- **Meine Werke:** volle Reihenkarten (Cover, Fame-Meter, Band-Wertungen, Empfinden,
  Community). Untermenü listet je Reihe einen Sprung-Link.
- **Bekanntheit:** 5-Stufen-Skala erklärt + alle Werke mit Meter + Hype.
- **Releases / Geschmack:** je eigene Ansicht.
Menü „Meine Werke ▾" ist ein Dropdown mit den einzelnen Reihen.

## Artefakt 1 — Meine Bibliothek (Basis)

Zeigt **alle guten Bücher** (verdict `loved` + `liked`; `mixed/disliked` nur in einer
kompakten, einklappbaren Sektion als Negativ-Kontrast). Inhalt:

1. **Kopf:** Titelzahl, Verteilung Buch/Hörbuch, Stand-Datum.
2. **Geschmacks-Kerndaten:** roter Faden (1–2 Sätze), wichtigste loved-Chips je
   Dimension, Gewichte als Mini-Balken, No-Gos rot markiert.
3. **Bücherkarten** (eine je Titel, loved zuerst): Cover/📖, Titel, Autor, Jahr, Reihe,
   Format-Badges (📖/🎧), bei Hörbuch Sprecher + Stunden, Verdikt-Badge, die wichtigsten
   DNA-Merkmale als Chips (Genres, Themen, Ton), 1 Zeile „warum geliebt", Rating falls belegt.
4. **Statistikleiste** (optional, wenn ≥5 Titel): häufigste Genres/Themen/Ton als Balken.

Nach jeder neuen Titel-Analyse: Karte ergänzen, Kerndaten-Block aktualisieren, republishen.

## Artefakt 2 — Empfehlungen (wird überschrieben)

Bei jedem Lauf wird `artifacts/empfehlungen.html` **komplett neu geschrieben** (alte
Empfehlungen fliegen raus — die Historie bleibt ja im Vault unter `vault/Empfehlungen/`).
Inhalt:

1. **Kopf:** Anfrage in einem Satz + Datum.
2. **Basis-Kurzblock:** gegen welche Kerndaten gematcht wurde (Kurzfassung + Verweis
   „vollständig in ‚Meine Bibliothek'").
3. **Empfehlungskarten (≥3, nach Match sortiert):** Cover/📖, Titel, Autor, Jahr, Format,
   Sprecher/Stunden bei Hörbuch, **großer Gesamt-Match-%-Balken**, Dimensions-Balken
   (0–100 je Dimension), **✓ Was passt** / **✗ Was passt nicht** in Klartext, Quellen dezent.
4. **Verworfen** (einklappbar): stärkste verworfene Kandidaten + Grund.

## Regeln

- Jeder %-Wert stammt aus der Lauf-Notiz im Vault — Balkenlänge = Score, nichts erfinden.
- Deutsch beschriftet, responsive, Light + Dark.
- **Keine dritten Artefakte.** Auch nicht „nur diesmal". Sonderwünsche (z. B. Vergleich)
  gehören als Sektion in eines der beiden.
- Nach dem Publish: 1–2 Sätze Zusammenfassung an den Nutzer + beide Links nennen, wenn
  beide aktualisiert wurden.
