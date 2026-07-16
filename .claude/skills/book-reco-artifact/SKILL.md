---
name: book-reco-artifact
description: >
  Visualisiert Empfehlungslauf als Artefakt. Nutze diesen Skill am Ende eines Buch-/
  Hörbuch-Empfehlungslaufs, um Ergebnisse als HTML-Artefakt darzustellen: oben die
  Basis/Kerndaten (was wir über den Geschmack wissen), darunter die Empfehlungen (≥3),
  jede mit Gesamt-Match als Prozentbalken, Dimensions-Balken und Klartext "Was passt /
  Was passt nicht". Baut auf taste-profile/profile.json und dem recommendations-JSON auf.
---

# Empfehlungs-Artefakt (Visualisierung)

Am Ende jedes Empfehlungslaufs baust du ein **HTML-Artefakt**, das den ganzen
Denkprozess sichtbar macht. Es beantwortet auf einen Blick: *Was ist unsere Basis?* und
*Was wird empfohlen, wie gut passt es, und warum (nicht)?*

## Vorbereitung
1. Lies `.claude/skills/dataviz/SKILL.md` **bevor** du Farben/Balken gestaltest
   (Farbsystem, Kontrast, Light/Dark). Die Balkenfarben unten sind Platzhalter.
2. Lade die Daten:
   - **Kerndaten:** `taste-profile/profile.json` (Dimensionen, Gewichte, No-Gos).
   - **Empfehlungen:** das aktuelle `taste-profile/recommendations/<datum>-<thema>.json`.
3. Verwende die Vorlage `references/artifact-template.html` als Startpunkt und fülle sie
   mit echten Daten. Sie ist self-contained, theme-aware und ohne externe Requests –
   passend für das Artifact-Tool (CSP-konform).

## Aufbau des Artefakts (Pflichtabschnitte)

### A) Kopf
Titel des Laufs + die Anfrage ("Ähnlich zu *X*, als Hörbuch, deutsch") + Datum.

### B) Basis / Kerndaten
Kompakte Darstellung dessen, was den Geschmack ausmacht:
- Die wichtigsten `loved`-Merkmale je Dimension (Chips/Tags).
- Die **Gewichte** als kleine Balken/Legende (zeigt, was zählt: z. B. Themen 25 %).
- No-Gos deutlich markiert (rot/durchgestrichen).
- 1–2 Sätze "roter Faden" des Geschmacks.
Dieser Block macht transparent, wogegen gematcht wurde.

### C) Empfehlungen (≥3, sortiert nach Match)
Pro Empfehlung eine Karte mit:
- **Cover** (Open-Library-Cover-URL, falls vorhanden), Titel, Autor, Jahr, Format/Reihe.
  Bei Hörbuch: Sprecher + Hördauer.
- **Gesamt-Match als großer Prozentbalken** (z. B. `82 %`), Farbe nach Höhe
  (hoch=grün-ish, mittel=amber, niedrig=rot – gemäß dataviz).
- **Dimensions-Balken:** je Dimension ein kleiner Balken 0–100 mit Label. So sieht der
  Nutzer, *wo* es passt und *wo nicht*.
- **Was passt** (grün, ✓-Liste) und **Was passt nicht** (amber/rot, ✗-Liste) in Klartext.
- Quellen-Hinweis (dezent).

### D) Verworfen (optional, einklappbar)
Kurz die stärksten verworfenen Kandidaten + Grund ("Ton zu leicht – widerspricht 'düster'").
Zeigt, dass ehrlich gesiebt wurde.

## Regeln
- **Jeder Prozentwert muss aus dem recommendations-JSON stammen** – nichts fürs schöne
  Bild erfinden. Balkenlänge = Score.
- Mindestens 3 Empfehlungskarten (oder die vom Nutzer geforderte Anzahl).
- Deutsch beschriftet. Zahlen mit `%`. Responsive, Light+Dark, horizontal-scroll für
  breite Elemente vermeiden.
- Setze einen sinnvollen `<title>` und (beim Publish) ein Buch-Favicon (📚).

## Publizieren
Schreibe die gefüllte HTML nach z. B. `scratchpad/reco-<datum>.html` und publiziere sie
mit dem **Artifact**-Tool (`favicon: "📚"`, sprechende `description`). Danach dem Nutzer
1–2 Sätze Zusammenfassung + Hinweis, dass das Profil mit jeder Analyse schärfer wird.
