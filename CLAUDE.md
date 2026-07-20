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
  jeder Analyse **aus dem Vault neu erzeugt**. **Zweck: maximale Datendichte je Werk sichtbar
  machen** (Metadaten bandgenau, Wertungen je Band, Empfinden +/−). Gleiche URL: in neuer
  Session via `Artifact(action:"list")` die bestehende URL holen und als `url:` mitgeben.
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
- Geschmacksräume: LitRPG, Fantasy, Krimi. Graubereich-Durchlauf gestartet: erstes
  `mixed`/„okay"-Werk erfasst ([[Survival Quest]]); weitere „okay"-/abgebrochene Werke
  folgen (schärfen die Ausschlüsse).

## Git

Auf dem Feature-Branch entwickeln, nach Änderungen committen & pushen (der Vault ist das
Gedächtnis — Verlust vermeiden). Commits klar beschreiben.

**Branch-Politik (Nutzer-Regel, 2026-07-20):** Seiten-Branches **dürfen** entstehen
(z. B. je Arbeitspaket/Session). **Aber vor Session-Ende muss ALLES auf `main` landen**
— zusammenführen (mergen/pushen), damit kein Wissen auf einem vergessenen Seiten-Branch
versauert (passt zur „Vault ist das Gedächtnis"-Regel). Danach den Seiten-Branch löschen:
`git checkout main && git merge <branch> && git push origin main` → `git branch -d <branch>
&& git push origin --delete <branch>`. Darauf wird aktiv hingewiesen: SessionStart-Hook
(`scripts/branch-policy.sh`) + Stop-Hook (`scripts/session-end-branch-reminder.sh`) melden,
wenn noch etwas nicht in `main` ist. Der `pre-push`-Hook blockiert nicht mehr, erinnert nur.

**Verbindlich (s. OBERSTE REGEL):** Vault-Änderungen und das daraus erzeugte Artefakt
gehören in **denselben** Commit-/Push-Schritt. Nie ein Artefakt publizieren, solange der
Vault-Stand uncommittet ist — der ephemere Container kann uncommittete Arbeit vernichten,
während das veröffentlichte Artefakt überlebt (genau so entstand der Vorfall 2026-07-17).
Vor Publish/Commit prüfen: `bash scripts/vault-first.sh`.
