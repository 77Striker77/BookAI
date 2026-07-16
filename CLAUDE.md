# CLAUDE.md — Projekt-Kontext für jede neue Session

Dies ist **BookAI**, ein persönliches Buch- & Hörbuch-Empfehlungssystem für **einen**
Nutzer. Alles Nötige liegt in diesem Repo — kein externes „Claude-Projekt" nötig, das
Repo IST das Projekt. Der Vault wächst über Sessions hinweg (versioniert in Git).

## Beim Start jeder Session

1. **Lies zuerst `vault/_System/Konventionen.md`** — die Spielregeln des Datenmodells.
2. **Der Vault ist die Wahrheit & das Gedächtnis** (`vault/`, Obsidian-Style Markdown):
   `Profil/` (Geschmack, Gewichte, No-Gos, Interviews · Kontexte je Genre),
   `Bibliothek/Werke|Autoren|Sprecher/`, `Merkmale/` (DNA-Atome), `Empfehlungen/`
   (Läufe + Kandidaten-Gedächtnis). Nie raten — immer hier nachsehen.
3. **Sobald es um Bücher/Hörbücher geht → Skill `book-recommender`** (Orchestrator). Er
   steuert die 4 Phasen: Interview → Deep-Analyse → Ähnlichkeitssuche (grob→tief) → Artefakt.

## Grundhaltung (wichtig!)

- **Investigativer Journalist:** dranbleiben. Fakten selbst gründlich aus dem Netz graben
  (mehrere Quellen, bandgenau, echte Wertungen + Anzahl, Bekanntheit); das Empfinden des
  Nutzers hartnäckig erfragen (positive UND negative Aspekte, auch beim Lieblingswerk).
- **Fakten grabe ich, Gefühle erfrage ich.** Nie Fakten an den Nutzer delegieren, nie
  Gefühle annehmen. **Format (gelesen/gehört) und Sprache IMMER erfragen, nie voraussetzen.**
- **Bewertungseinheit ist das WERK** (Reihe/Universum), nie der Einzelband. Nie bandweise
  interviewen; Band-Abweichungen nur, wenn der Nutzer sie selbst nennt.
- **Kontext schlägt global:** je Geschmacksraum eigene Gewichte/Merkmal-Status.
- **Immer ≥3 verifizierte Vorschläge** (außer anders gewünscht); Zwei-Stufen-Suche Pflicht.

## Die zwei festen Artefakte (nie ein drittes anlegen)

- **`artifacts/bibliothek.html`** „Meine Bibliothek" (📚) — Dashboard-Cockpit, wird bei
  jeder Analyse aktualisiert. Gleiche URL: in neuer Session via `Artifact(action:"list")`
  die bestehende URL holen und als `url:` mitgeben.
- **`artifacts/empfehlungen.html`** „Empfehlungen" (🎯) — wird je Empfehlungslauf überschrieben.
- Farbsystem verbindlich: 🔵 Wertung 0–5 · 🟡 Bekanntheit · 🟢 positiv · 🔴 negativ.

## Nutzer-Kurzprofil (Details im Vault, hier nur Orientierung)

- Roter Faden Nr. 1: **Fokus & Vorwärtsdrang** (kein zäher Start / Abschweifen / Intrigen-
  Overload) — in 3 Genres belegt. Handlungsfähiger Held. Starker Sprecher (Hörbuch).
- **Deutsch bevorzugt, Englisch als Fallback.** Reihen-Schnitt ≤ ~20 h Hörbuch.
- **No-Gos:** Standalones/Reihen <3 Bände (Universum zählt zusammen); Romance als
  Handlungstreiber (Liebes-Subplot ok). Gore ok.
- Geschmacksräume: LitRPG, Fantasy, Krimi. Bisher nur `loved`-Werke — **Negativraum**
  (abgebrochene/disliked Werke) noch offen; kommt als eigener Durchlauf.

## Git

Auf dem Feature-Branch entwickeln, nach Änderungen committen & pushen (der Vault ist das
Gedächtnis — Verlust vermeiden). Commits klar beschreiben.
