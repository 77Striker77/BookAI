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
