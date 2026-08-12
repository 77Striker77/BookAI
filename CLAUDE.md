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

## 🔒 SPOILER-REGEL (Nutzer-Regel 2026-08-11, gilt für JEDE Ausgabe)

**In Artefakten und Ausgaben darf nie etwas stehen, das der Nutzer noch nicht gelesen oder
gehört hat. Was er erlebt hat, darf gerne detaillierter drinstehen.**

- Regeln: `vault/_System/Spoiler-Politik.md` · Wortlisten: `vault/_System/Spoiler-Lexikon.md`
  · Skill: **`spoiler-check`** · Agent: **`spoiler-guard`**
- Grenze = bandgenauer Lesestand im Frontmatter jeder Werk-Notiz
  (`spoiler_erlebt_bis`, `spoiler_aktuell`, `spoiler_gesamt`, `spoiler_sperrbegriffe`).
  Abrufen: `python3 scripts/spoiler_check.py --grenzen`.
- **Der laufende Band zählt als NICHT erlebt. Unbekanntes Werk = ungelesen (fail-closed).**
  Empfehlungskandidaten sind per Definition ungelesen → nur Klappentext-Ebene.
- **Kein Widerspruch zum obersten Ziel:** Metadaten (Titel, Daten, ISBN, Seiten, Hördauer,
  Sprecher, Wertungen, Bekanntheit, Ton/Tempo) sind NIE ein Spoiler — die maximale
  Datendichte bleibt vollständig erhalten. Zurückgehalten wird **nur Handlung**.
- **Nie stillschweigend glätten** — stattdessen sichtbar: „🔒 Details zu Bd. X+
  zurückgehalten (dein Stand: Bd. Y)."
- Erwähnt der Nutzer seinen Fortschritt („bin bei Band 3", „Teil 2 durch", „abgebrochen"),
  **sofort** die Grenze in der Werk-Notiz nachziehen — sonst arbeitet alles falsch weiter.
- Prüfen: `bash scripts/spoiler-gate.sh` (deterministisch) **und** Agent `spoiler-guard`
  (semantisch). Beides ist Pflicht vor jedem Artefakt-Publish. Selbsttest der Regeln:
  `bash scripts/spoiler-selftest.sh`.
- Automatische Sicherungen (Hooks, `.claude/settings.json`): SessionStart kippt die Grenzen
  in den Kontext; PreToolUse blockt Artefakt-Publish/Schreiben mit Verstoß; Stop prüft die
  Chat-Antwort und die Artefakte; SubagentStop prüft Subagenten-Rückgaben. **Die Hooks sind
  das Netz, nicht die Methode** — aktiv prüfen, nicht aufs Auffangen verlassen.

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

## 🎨 Gestaltung — die Design-Werkstatt (Plugin `design@design-ai`)

Alles Optische an den beiden Artefakten läuft über die Werkstatt aus dem Repo
**[Design_AI](https://github.com/77Striker77/Design_AI)**. Sie ist in
`.claude/settings.json` **projektgebunden** aktiviert (`extraKnownMarketplaces` +
`enabledPlugins`) — bewusst nicht auf Benutzer-Ebene, weil die BookAI-Sessions in
**ephemeren Containern** laufen und eine Benutzer-Installation dort nicht überlebt.

| Aufgabe | Weg |
| --- | --- |
| Richtung, Farbsystem, Skalen, Theming, a11y | `design:frontend-handwerk` |
| HTML-Artefakt bauen, prüfen, veröffentlichen | `design:artefakt-werkstatt` |
| Visueller Baustein (Hintergrund, Animation, Glow) | `design:artefakt-bausteine` — **zuerst dort nachsehen** |
| Bestehendes Artefakt begutachten lassen | Agent `design:design-gutachter` |

**Reihenfolge: Richtung → Ausführung → Messen.** Keine Farbe ohne Messung mit
`kontrast.mjs` gegen den echten Grund, je Theme einzeln. Am Ende sagen, was **nicht**
geprüft wurde.

### Pflicht nach jeder Änderung an `artifacts/*.html`

```bash
export BROWSER_BIN="$CLAUDE_PROJECT_DIR/scripts/chrome-fuer-messung.sh"
bash <artefakt-werkstatt>/scripts/scan.sh artifacts/bibliothek.html   # statisch
bash <artefakt-werkstatt>/scripts/mess.sh artifacts/bibliothek.html   # Browser
```

`<artefakt-werkstatt>` = `${CLAUDE_PLUGIN_ROOT}/.claude/skills/artefakt-werkstatt`.
**Die erzeugten PNGs ansehen, nicht nur die Checkzeilen lesen.**

> ⚠️ **Container-Falle (gelöst am 2026-08-11):** Die Session läuft als **root**, Chromium
> startet dort ohne `--no-sandbox` nicht — und zwar **still**. `mess.sh` meldete dann
> „Seite lädt möglicherweise gar nicht", „Breitenmatrix UNGEPRUEFT" und „kein Debug-Port".
> Das waren **keine** Artefakt-Fehler, sondern die Umgebung. Deshalb gibt es
> `scripts/chrome-fuer-messung.sh` — immer über `BROWSER_BIN` einhängen, nie Chromium
> direkt. Kommen diese drei Meldungen wieder, ist der Wrapper nicht gesetzt.

### 🧱 Informations-Architektur der Artefakte (Nutzerregel 2026-08-11)

> „das ist immer noch zu viel Input pro angezeigte Seite … baue es übersichtlicher
> **ohne weniger Info zu zeigen**"

**Nie Information streichen, um Platz zu schaffen — staffeln.** Genau **ein Muster je Ebene**
(gemischte Muster zwingen den Nutzer, drei Bedienmodelle zu lernen):

| Ebene | Inhalt | Muster |
| --- | --- | --- |
| 1 | Ansichten **und** alle Werke | **Schiene links** (`.rail`) — zeigt ALLE Ziele gleichzeitig |
| 2 | Abschnitte einer Ansicht | Reiter (`.tabsec`), genau einer sichtbar |
| 3 | Detail je Werk | `<details class="dt">` — nativ, tastaturfest, druckt aufgeklappt |

> 🧭 **Warum Schiene statt Topnav (Nutzer 2026-08-11: „deine Navigation ist immer noch
> scheiße"):** Es liefen **fünf** Mechanismen nebeneinander — Topnav, Reiter, `<details>`,
> Fußnav und Sekundärnav. Recherche (NN/g zu Tab-Grenzen; Linear/Stripe/Grafana): sobald die
> Ziele nicht mehr in ~5 Reiter passen, ist die **Seitenleiste** das skalierende Muster, weil
> sie alle Ziele auf einmal zeigt. Hier wiegt das doppelt — das iframe wächst auf Inhaltshöhe,
> `sticky` wird nie aktiv, also muss die Navigation **im Fluss** stehen statt zu kleben.
> Fußnav und untere Sekundärnav sind damit **ersatzlos entfallen**. Schmal (≤900 px) wird die
> Schiene zu einer Chip-Reihe; die Werkliste blendet dort aus, dort führt der Index.

**Werke = Index + Detailseiten.** `#werke` ist eine Zeile je Werk (Titel · Verdikt · Raum ·
Bände · ⌀ · Bekanntheit · Format); jedes Werk hat eine eigene Ansicht `#w-<slug>`. Neue Werke
brauchen **eine Indexzeile + eine `<div class="view" id="v-w-…">`** — der Router liest die
Ansichten aus dem DOM, es gibt keine Liste zum Nachpflegen.

**Richtwert: keine Ansicht über ~2,5 Bildschirme** (900 px). Nach dem Umbau messen:

```bash
# Höhe der aktiven Ansicht je Hash, 1180 px und 420 px
```

**Was NIE eingeklappt wird:** der aktuelle Lesestand, die harte Reihenfolge-Regel, alle
⚠️-Warnungen und die Konfidenz-/Quellenangaben. Eine versteckte Warnung ist keine Warnung.

**Nicht wieder einbauen** (waren belegte Fehler, s. Gutachten 2026-08-11): `<button>` ohne
`href` im Menü (der Klick-Handler steigt aus → Menüpunkt tut nichts) · Hover-Dropdowns in
einer `sticky` Nav ohne `max-height` (schnitt Einträge dauerhaft ab) · feste
`scroll-margin-top`-Werte (→ `var(--nav-h)` benutzen) · Fließtext ohne `max-width`
(lief auf 111–137 Zeichen statt 65–75) · **einen Ansichtsnamen im Router hart hineinschreiben**
(s. u.).

> 🩹 **Belegter Totalausfall 2026-08-11 — leere Seite durch einen Router-Fallback.**
> Der Router hatte `"uebersicht"` als Rückfallwert (`show()`, `route()`), die Startansicht
> hieß nach der Englisch-Umstellung aber `v-home`. Folge: bei **leerem Hash** — also beim
> ganz normalen ersten Aufruf — fand `show()` keine passende Ansicht, blendete **alle** aus
> und die Seite war **komplett leer**. Weder `scan.sh` noch `mess.sh` schlugen an: „VIEWS
> gefunden=19 leer=0" prüft die Ansichten einzeln, nicht ob überhaupt eine sichtbar ist.
> **Regel:** Der Rückfall wird aus dem DOM abgeleitet (`document.querySelector(".view.on")`,
> sonst die erste Ansicht) — **nie** ein Name im Code. **Prüfung:** nach jeder Änderung an
> Router oder Ansichts-IDs die Datei mit **leerem Hash** laden und zählen, wie viele
> `.view.on` es gibt (muss genau 1 sein). Die Render-PNGs zeigten die leere Seite sofort —
> genau deshalb steht in dieser Datei „**die PNGs ansehen, nicht nur die Checkzeilen lesen**".

> 🩹 **Belegter Ausfall 2026-08-11 (b) — eine Klassenkollision malte weiße Kästen.**
> Die Schritte der neuen Hörspur hießen `.st` — genauso wie die Status-Pillen der Bandlisten
> (`.st.done { background: var(--card) }`). Jeder Schritt bekam dadurch einen weißen Kasten
> untergeschoben, obwohl die eigene Regel gar keinen Hintergrund setzt. Im Browser gemessen:
> `.st` hatte `background: rgb(255,255,255)`. **Regel:** neue Komponenten bekommen einen
> eigenen Namensraum (hier `.hs`), und vor jeder neuen Klasse einmal `grep 'class="<name>'`
> und `grep '\.<name>'` über die Datei.

> 🩹 **Belegter Ausfall 2026-08-11 (c) — totes Skript zeigte auf entferntes Markup.**
> Beim Ersetzen der Topnav durch die Schiene blieb `document.querySelector(".nav").offsetHeight`
> stehen. Der TypeError flog **vor** `route()` — dadurch landete **jeder** Hash auf der
> Startseite, weil nur noch das im Markup gesetzte `.view.on` übrig blieb. `#werke`, `#upnext`,
> `#geschmack`, jede Werkseite: alle zeigten Home. **Regel:** Wer Markup entfernt, sucht
> vorher, wer im Skript darauf zeigt. **Prüfung:** nach jedem Umbau jeden Hash einmal laden und
> die aktive Ansicht vergleichen — ein Fehler im Skript sieht sonst aus wie ein Routing, das
> „halt immer Home nimmt".

> ⚠️ **`mess.sh` prüft Text erst ab 3:1 — nicht ab 4,5:1.** Der Bereich dazwischen läuft
> **grün** durch. Nach jeder Farbänderung zusätzlich `kontrast.mjs` gegen die echten Gründe
> laufen lassen, **je Theme einzeln**. Genau dort lagen im hellen Theme sechs Verstöße
> (u. a. `--muted` 3,18:1), die die Werkstatt nicht gemeldet hat. Für Text auf Soft-Flächen
> gibt es deshalb die dunkleren Varianten `--pos-ink` / `--neg-ink` / `--fame-ink` /
> `--rating-ink`; `--pos`/`--neg`/`--fame` bleiben **Flächenfarben**.

### Mess-Marker in den Artefakten

`artifacts/bibliothek.html` trägt im `<style>` die Werkstatt-Marker `@artefakt`,
`@grund-hell`, `@grund-dunkel`, `@serien-hell`, `@serien-dunkel`. **Werden `--bg`/`--panel`
oder die Serienfarben geändert, müssen die Marker mitgezogen werden** — sonst misst
`mess.sh` gegen den falschen Grund und meldet trotzdem grün.

### 🎛️ Gestalterische Richtung: „Neon-Nachtregal" (Stand 2026-08-11)

Die Richtung wurde in dieser Reihenfolge vom Nutzer gesetzt — jeder Schritt hat den
vorigen korrigiert, die Historie steht hier, damit niemand rueckwaerts laeuft:

1. „zu ungrafisch … Startseite muss mehr hermachen, kein 0815-Text" → Daten als Grafik.
2. „cozy Buchladen-Vibes … in Untermenues alle Infos preisgeben, auf den ersten Blick
   nicht mit Text erschlagen" → Regal, Cover, Aufklappen.
3. **„der Background-Braunton gefaellt mir gar nicht. nichts Braunes bitte."**
4. **„gruen ist auch nicht der perfekte Hintergrund, evtl. was schwarz mit Neon oder so
   und evtl. animiert? wie beim Designer?"**

**Aktuell gilt: nachtschwarz mit Neon, EINE Bildwelt.** Die Seite ist dunkel, egal was das
System sagt; die drei Theme-Bloecke tragen dieselben Werte (der Umschalter bleibt
deklariert, weil `scan.sh` das prueft — er aendert nur nichts mehr).

- **Grund `#06080c` · Tafel `#0d1119` · Karte `#121722`.** ⛔ **Kein Braun, kein Creme,
  kein Gruen als Grund.**
- **Neon-Akzente, Bedeutung bleibt verbindlich:** 🔵 Wertung `#4dd2ff` · 🟡 Bekanntheit
  `#ffc94d` · 🟢 positiv `#3ff08a` · 🔴 negativ `#ff6b85`. Alle gegen alle drei Gruende
  gemessen, 5,6:1 bis 13,4:1.
- **Bewegter Hintergrund:** 26 Lichtbahnen, geerntet aus
  `design:artefakt-bausteine/background-beams`. Kern des Bausteins: **die Bewegung sitzt im
  Verlauf, nicht im Pfad** — vier `<animate>` je Bahn auf `x1/y1/x2/y2` mit
  `gradientUnits="userSpaceOnUse"` (mit Bounding-Box leuchtet jede Bahn die meiste Zeit
  ausserhalb des Bildes). Ruhewert ist eine zufaellige Phase, damit bei
  `prefers-reduced-motion` ein **Standbild** bleibt statt eines leeren Rechtecks.
  Gemessen: 104 `<animate>` normal, 0 bei reduzierter Bewegung.
- **Lampenring** um die laufenden Buecher aus `border-beam-panel` (Kegelverlauf, zwei
  Masken, unscharfer Zwilling als Schein).
- **Das Regal** ist ein Moebel: Korpus, Seitenwangen, Rueckwand, drei Faecher mit
  Deckenverschattung; die Brettkante ist eine **Neonroehre**. Buchhoehe = Bandzahl,
  Etiketten haengen unter dem Brett (helle Praegung auf dunkler Rueckwand).
- **Cover:** 1–4 Embleme je Einband, Groesse nach Anzahl (1 → 2,9em … 4 → 1,5em).
  Reihen desselben Universums fuehren **dasselbe erste Emblem** (Vuldranni 🗺️,
  Streitende Goetter ⚡) — Zusammengehoerigkeit ohne Titel lesen zu muessen.
- **Keine Floskel-Ueberschrift.** Die Startseite beginnt mit dem, was gerade laeuft.

> 🩹 **Belegter Fehler 2026-08-11 (d) — eine Sammelregel riss zwei Ebenen aus der Verankerung.**
> `.page > * { position: relative }` galt auch fuer die neue Bahnen-Ebene (`fixed`) und die
> Sprungmarke (`absolute`). Beide wurden dadurch normale Bloecke im Fluss: **600 px Leerraum
> ueber der Kopfleiste und eine dauerhaft sichtbare Sprungmarke.** Die Regel regelt jetzt nur
> noch den Stapel (`:not(.beams):not(.skip)`). **Regel:** Sammelregeln auf `> *` nie
> `position` setzen lassen, wenn im Container etwas fixed oder absolut liegt.

### Was das Farbsystem angeht

Das verbindliche Farbsystem der Artefakte (🔵 Wertung · 🟡 Bekanntheit · 🟢 positiv ·
🔴 negativ) steht **über** ästhetischen Vorschlägen der Werkstatt: Bedeutung schlägt Optik.
Die Werkstatt liefert die **Messung** dazu, nicht die Bedeutung.

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
