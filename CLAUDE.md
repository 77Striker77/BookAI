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

## ⭐ OBERSTES ZIEL (schlägt alles andere)

**„Meine Bibliothek" soll von JEDEM Werk so viele Daten wie irgend möglich enthalten und
die Meinung des Nutzers bis ins Letzte ausquetschen — damit spätere Suchen so präzise wie
möglich werden.** Daraus folgt kompromisslos:

- **BEI DER INFORMATIONSBESCHAFFUNG WIRD NIE ABGEKÜRZT.** Nicht bei geliebten, nicht bei
  „okay"-, nicht bei abgelehnten Werken. Der Verdikt bestimmt NIE die Recherchetiefe.
- **Metadaten sind Pflicht und detailgenau zu dokumentieren** — bandgenau: Titel (DE/EN/
  Original), alle Release-Daten (Buch UND Hörbuch, DE UND EN), ISBN je Ausgabe, Seitenzahl,
  Hördauer je Band, Verlag/Label, Sprecher, echte Wertungen MIT Anzahl je Band/Quelle,
  Bekanntheit. Fehlt trotz gründlicher Suche etwas → als „Offene Frage" markieren, NIE
  stillschweigend weglassen, mit „—" glätten oder zusammenfassen.
- **Meinung maximal ausquetschen:** Positiv UND negativ, getrennt gefragt, bis das Bild
  wirklich rund ist (siehe `book-taste-interview`). Lieber eine Runde zu viel als zu wenig.
- **Messlatte = die detailliertesten bestehenden Werk-Notizen.** Eine neue Notiz ist erst
  fertig, wenn sie mindestens deren Detailgrad erreicht.

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
  jeder Analyse aktualisiert. **Zweck: maximale Datendichte je Werk sichtbar machen**
  (Metadaten bandgenau, Wertungen je Band, Empfinden +/−). Gleiche URL: in neuer Session
  via `Artifact(action:"list")` die bestehende URL holen und als `url:` mitgeben.
- **`artifacts/empfehlungen.html`** „Empfehlungen" (🎯) — wird je Empfehlungslauf überschrieben.
- Farbsystem verbindlich: 🔵 Wertung 0–5 · 🟡 Bekanntheit · 🟢 positiv · 🔴 negativ.

## Nutzer-Kurzprofil (Details im Vault, hier nur Orientierung)

- Roter Faden Nr. 1: **Fokus & Vorwärtsdrang** (kein zäher Start / Abschweifen / Intrigen-
  Overload) — in 3 Genres belegt. Handlungsfähiger Held. Starker Sprecher (Hörbuch).
- **Deutsch bevorzugt, Englisch als Fallback.** Reihen-Schnitt ≤ ~20 h Hörbuch.
- **No-Gos:** Standalones/Reihen <3 Bände (Universum zählt zusammen); Romance als
  Handlungstreiber (Liebes-Subplot ok). Gore ok.
- Geschmacksräume: LitRPG, Fantasy, Krimi. Graubereich-Durchlauf gestartet: erstes
  `mixed`/„okay"-Werk erfasst ([[Survival Quest]]); weitere „okay"-/abgebrochene Werke
  folgen (schärfen die Ausschlüsse).

## Git

Auf dem Feature-Branch entwickeln, nach Änderungen committen & pushen (der Vault ist das
Gedächtnis — Verlust vermeiden). Commits klar beschreiben.
