# CLAUDE.md — Projekt-Kontext für jede neue Session

Dies ist **BookAI**, ein persönliches Buch- & Hörbuch-Empfehlungssystem für **einen**
Nutzer. Alles Nötige liegt in diesem Repo — kein externes „Claude-Projekt" nötig, das
Repo IST das Projekt. Der Vault wächst über Sessions hinweg (versioniert in Git).

## ⚠️ OBERSTE REGEL — Vault ist die einzige Quelle, Artefakte sind nur Projektionen

Diese Regel steht über allem anderen:

1. **Der Vault (`vault/` im Repo) ist die EINZIGE Wahrheit & Datenquelle.** Jede Analyse,
   jede Empfehlung, jedes Interview, jede Zahl lebt zuerst und maßgeblich im Vault.
2. **Artefakte (`artifacts/*.html`) sind NUR Abbildungen/Projektionen des Vaults.** Sie
   werden ausschließlich AUS dem Vault erzeugt. Ein Artefakt darf **niemals** eine
   Information enthalten, die nicht im Vault steht.
3. **Nie Artefakt über Vault.** Weicht ein (auch veröffentlichtes) Artefakt vom Vault ab
   oder enthält es mehr, ist das ein **Bug**: die Info wird SOFORT in den Vault
   zurückgespiegelt (Backport) — der Vault gewinnt immer, nie umgekehrt.
4. **Publish = Commit.** Ein Artefakt darf erst (re)publiziert werden, wenn der
   zugrunde liegende Vault-Stand committet ist. Artefakt-Update und Vault-Commit gehören
   in denselben Arbeitsschritt (Reihenfolge: Vault schreiben → committen → Artefakt aus
   Vault erzeugen → pushen). Nie ein Artefakt aktualisieren und den Vault „später".
5. **Startprüfung (jede Session, sobald Artefakte im Spiel sind):** Prüfe, ob die
   Live-Artefakte Infos zeigen, die der Vault nicht hat. Wenn ja → erst backporten, dann
   weiterarbeiten. Hilfsskript: `scripts/vault-first.sh` (zeigt uncommittete Vault-/
   Artefakt-Änderungen).

> **Warum diese Regel (Vorfall 2026-07-17):** Eine frühere Session hatte drei Werke
> ([[Riyria]], [[Survival Quest]], [[Scholomance]]) und einen geschärften roten Faden nur
> ins veröffentlichte Bibliotheks-Artefakt geschrieben, aber den Vault nie committet. Der
> ephemere Container wurde recycelt → die Vault-Daten waren weg, nur das Artefakt überlebte.
> Folge: eine Session ohne dieses Wissen empfahl ein bereits als „okay" bewertetes Werk.
> Das darf nie wieder passieren.

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
- **🗺️ Universum & Reihenfolge sind Pflichtrecherche.** Bei JEDEM Werk/Kandidaten klären:
  Welche Reihe ist das? Spielen andere Reihen in derselben Welt? Wie hängen sie zusammen,
  und in welcher **Lese-/Hör-Reihenfolge** (muss man etwas zuerst lesen/hören)? Immer im
  Vault festhalten (`universum:` + `verwandte_reihen:` + Abschnitt „Universum & Reihen-
  Landkarte"). Zählt auch für die Reihen-Pflicht ≥3 Bände (Universum zählt zusammen).
- **⭐ Autoren-Dossier ist Pflichtrecherche.** Wer ist der Autor: Herkunft (Land/Region),
  Werdegang, Bekanntheit/Reichweite (mit Belegen), welche Universen/Reihen. In der
  Autoren-Notiz pflegen. Details, Details, Details — investigativ bis ins Kleinste.
- **Bewertungseinheit ist das WERK** (Reihe/Universum), nie der Einzelband. Nie bandweise
  interviewen; Band-Abweichungen nur, wenn der Nutzer sie selbst nennt.
- **Kontext schlägt global:** je Geschmacksraum eigene Gewichte/Merkmal-Status.
- **Immer ≥3 verifizierte Vorschläge** (außer anders gewünscht); Zwei-Stufen-Suche Pflicht.

## Die zwei festen Artefakte (nie ein drittes anlegen)

**Beides sind reine Projektionen des Vaults (s. OBERSTE REGEL) — Inhalte immer aus
`vault/` erzeugen, nie umgekehrt; vor Publish committen.**

- **`artifacts/bibliothek.html`** „Meine Bibliothek" (📚) — Dashboard-Cockpit, wird bei
  jeder Analyse aus dem Vault neu erzeugt. Gleiche URL: in neuer Session via
  `Artifact(action:"list")` die bestehende URL holen und als `url:` mitgeben.
- **`artifacts/empfehlungen.html`** „Empfehlungen" (🎯) — wird je Empfehlungslauf aus dem
  Vault überschrieben.
- Die Repo-Dateien `artifacts/*.html` müssen mit der veröffentlichten Version übereinstimmen
  (sonst überschreibt ein späterer Publish die gute Live-Version mit einem alten Stand).
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

**Verbindlich (s. OBERSTE REGEL):** Vault-Änderungen und das daraus erzeugte Artefakt
gehören in **denselben** Commit-/Push-Schritt. Nie ein Artefakt publizieren, solange der
Vault-Stand uncommittet ist — der ephemere Container kann uncommittete Arbeit vernichten,
während das veröffentlichte Artefakt überlebt (genau so entstand der Vorfall 2026-07-17).
Vor Publish/Commit prüfen: `bash scripts/vault-first.sh`.
