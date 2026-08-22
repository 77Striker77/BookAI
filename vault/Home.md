---
tags: [moc, home]
---

# 🏠 Home — Buch- & Hörbuch-Vault

> Einstiegspunkt. Jedes Konzept ist eine atomare Notiz; die Links/Backlinks sind die
> eigentliche Intelligenz dieses Vaults. Konventionen: [[Konventionen]].

## Mein Geschmack

- [[Profil]] — der rote Faden (MOC über alle Dimensionen)
- [[Gewichte]] — was zählt wie stark im Match-Score (mit Begründung)
- [[No-Gos]] — harte Ausschlüsse
- `Profil/Interviews/` — jede Interviewrunde eine Notiz (Provenienz aller Aussagen)

## Bibliothek (erlebte Werke)

- `Bibliothek/Werke/` — voll analysierte WERKE (Reihe/Universum als Bewertungseinheit)
- `Bibliothek/Autoren/` · `Bibliothek/Sprecher/`

## Merkmale (die DNA-Atome)

- `Merkmale/Genres|Themen|Ton|Erzählstil|Figuren|Setting/` — je Merkmal EINE Notiz.
  Backlinks einer Merkmal-Notiz = alle Bücher/Kandidaten, die es tragen.

## Empfehlungen & Gedächtnis

- [[Warteliste]] — bestätigte, noch nicht gelesene/gehörte Empfehlungen
- `Empfehlungen/Läufe/` — jeder Empfehlungslauf eine Notiz (Historie)
- `Empfehlungen/Kandidaten/` — **GEDÄCHTNIS: jeder je erwähnte oder gesichtete Titel**,
  auch grob Aussortiertes, mit Status + Grund. Nie zweimal prüfen, nie Verworfenes
  erneut vorschlagen.

## 🔒 Spoilerfreiheit

- [[Spoiler-Politik]] — was in einer Ausgabe stehen darf (Neutralzone vs. Verbotszone)
- [[Spoiler-Lexikon]] — die Wortlisten des Linters (hier tunen, nicht im Code)
- Grenzen sehen: `python3 scripts/spoiler_check.py --grenzen`
- Vor jedem Publish: `bash scripts/spoiler-gate.sh` + Agent `spoiler-guard`

## Zuletzt

- 2026-08-22 — 🐉 **[[Dark Lord Davi]] (Django Wexler) auf die [[Warteliste]]** — und damit die
  **erste vom Nutzer erteilte No-Go-Ausnahme**: Die Reihen-Pflicht ≥3 Bände ist keine Mauer,
  sondern ein Filter, den er bei starkem Ton-Match selbst öffnet (*„ne nimm es mit auf es sind
  nur 2 bücher"*). Arbeitsregel in [[No-Gos]] nachgezogen: Kandidaten, die **nur** an der
  Reihenlänge scheitern, werden künftig **mit Hinweis vorgelegt statt still verworfen**.
  Neue Autoren-Notiz [[Django Wexler]]. Offene Nachfrage fürs spätere Interview: stören ihn
  die Dauer-Sex-Kommentare, und empfindet er den Stationen-Aufbau als Längen?

- 2026-08-11 (R4) — 🎤 **Negativseite bei [[Die guten Jungs]] nachgeholt**, nachdem der
  Stop-Hook die fehlende Abdeckungs-Matrix gemeldet hatte. Sechs Felder einzeln geschlossen.
  Das bisherige Acht-mal-+2-Profil war ein **Erhebungsartefakt**. Drei Funde: ⭐ eine
  **Kombinationsregel** ([[Weltgeheimnisse & Entdeckung]] verlangt einen
  [[Wissbegieriger Selbermacher-Held]] — sonst Reibung am stärksten Plus), ⭐ die
  **Mechanik-Grenze** (Spielmechanik als Weltlogik ja, als vorgelesene Zahlenkolonne nein),
  ⭐ **Erzählwitz neutralisiert einen Systemfehler** ([[Regel-Inkonsistenz]] = 0 trotz
  fehlendem Inventar). Dazu: [[Konstanter Vorwärtsdrang]] +1 endlich belegt („Tempo war
  gut"), [[Tonwechsel Humor-Ernst]] +2 → +1 (Nutzer-Skala: DCC 9, hier 7–8),
  [[Magiesystem-Tiefe]] −1 als **zweiter** Beleg nach [[Riyria]] — ausdrücklich **kein**
  Ausschlusskriterium.

- 2026-08-11 — 🔒 **Spoiler-Schutz eingebaut** (Nutzer-Regel): keine Ausgabe verrät mehr
  etwas jenseits des bandgenauen Lesestands; erlebte Werke dürfen dafür **detaillierter**
  beschrieben werden. Neu: [[Spoiler-Politik]] + [[Spoiler-Lexikon]], `spoiler_*`-Felder in
  allen 15 Werk-Notizen, deterministischer Linter, Agent `spoiler-guard`, Skill
  `spoiler-check` und vier Hooks (SessionStart/PreToolUse/Stop/SubagentStop).
  Metadaten bleiben unangetastet — beschnitten wird ausschließlich Handlung.

- 2026-08-11 (Nachgang) — **Reihenfolgen als eigenes Thema:** neue MOC [[Reihenfolgen]] (alle Werke, 5 Reihenfolge-Typen, Verfügbarkeits-Engpässe). Dazu zwei **Korrekturen** aus der Verifikationsrunde: (1) ⚠️ **Weder [[Die guten Jungs]] noch [[Die bösen Jungs]] ist abgeschlossen** — Bd. 17 bzw. Bd. 12 sind für 2026 angekündigt (erster Stand war falsch); (2) die Crossover-Regel **BJ 11 vor GJ 15** ist jetzt **hart belegt** über die Erscheinungsdaten (21.04.2024 vs. 08.06.2024) plus Verlagstext plus Leser-Rezension. Verifikationsstand mit Konfidenz je Aussage steht in [[Vuldranni (iNcarn8)]]. Neue Nutzerregel in [[Konventionen]]: **Artefakte müssen spoilerfrei sein** — jenseits des Lesestands nur Metadaten, keine Handlung.
- 2026-08-11 — Werke 12+13 als **Verbund**: **[[Vuldranni (iNcarn8)]]** ([[Eric Ugland]]) mit
  [[Die guten Jungs]] (16 Bd.) + [[Die bösen Jungs]] (11 Bd.) — beide **liked (vorläufig)**,
  🎧 dt. Hörbuch. **Zweiter Werk-Verbund** nach [[Die Streitenden Götter]] — und der erste, in dem
  der Nutzer **mitten drin** ist (GJ 5/16 gehört, BJ 1/11 läuft). Kern des Auftrags: die
  **kombinierte Hörreihenfolge** über beide Reihen — recherchiert und vom Nutzer bestätigt:
  *GJ als Basis · Umstieg auf BJ 1 nach GJ 5 (Erscheinungschronologie) · harte Regel am Ende:
  **BJ 11 „2 Lügen, 2 Throne" VOR GJ 15 „Kampf um den Keramikthron"** (Crossover)*. 4 neue Merkmale:
  ⭐ [[Basisaufbau & Siedlungsentwicklung]] (+2, neuer Plus-Anker-Typ), [[Weltgeheimnisse &
  Entdeckung]], [[Monster-Vielfalt & Bestiarium]], [[Handfeste Kampf-Action]].
  **Zwei Kalibrierungen:** (1) ⭐ **die Politik-Schwelle ist erstmals benannt statt überschritten**
  — [[Intrigen-Overload ohne Progress]] steht hier auf **0** („noch in einem okey maße, mehr würde
  mich mehr nerven") → Politik als Würze = neutral, als Motor = Malus; (2)
  [[Über-crunchiges Zahlensystem]] bekommt eine **Intensitäts-Skala** (Beiwerk vs. Selbstzweck) +
  **Hörbuch-Verschärfung** (Statblöcke sind beim Hören nicht überspringbar).
  [[Stimmige Weltatmosphäre]] im Kontext [[LitRPG]] **liked → loved** (erster +2-Träger).
  **Erster Fall mit zwei Sprechern in EINEM Universum:** [[Robert Frank]] **+2** vs.
  [[Thomas Nicolai]] **−1** (direkter Vergleich des Nutzers). ⭐ **Erste Empfehlung des Systems,
  die tatsächlich gehört wird** — [[Die guten Jungs]] kam aus dem Lauf
  [[2026-07-17 Deutsche Bücher quer über alle Räume]] (86 %); Prognose-Nachkontrolle in der
  Kandidaten-Notiz: Ton/Held ✅, aber **vier Plus-Anker übersehen**.
  ⚠️ **Recherche-Einschränkung:** Audible.de, BücherTreff, Goodreads, Amazon und DNB waren
  Egress-geblockt (nur Websuche) → mehrere Bandtitel/Hördauern sind als **offene Fragen** markiert.
  Quelle: [[2026-08-11 Interview Die guten Jungs & Die bösen Jungs]].
- 2026-08-11 — Werk 11: **[[Der Donnerstagsmordclub]]** (Richard Osman, Cosy Crime, 5 Bände),
  **liked** — **2. Werk im Kontext [[Krimi]]** und **erstes `liked`** überhaupt (zwischen loved
  und mixed). Gehört dt., **[[Johannes Steck]]** + **[[Beate Himmelstoß]]** (Zwei-Stimmen-Lesung,
  Sprecher **0** — „solide, unauffällig"). **Die zentrale Erkenntnis schärft den stärksten roten
  Faden: Fokus ≠ Tempo.** Gemütlich ist okay ([[Cosy-Wohlfühlatmosphäre]] +2, alle vier
  Ton-Optionen), **Verdrängung** ist es nicht — neues Merkmal [[Persona-Strang verdrängt
  Haupthandlung]] (−2, „dafür lese ich keinen krimi!"; Demenz-Strang, **bandgenau als Bd. 4
  identifiziert**). Trotz Volltreffern bei Ton (+2), [[Unterschätztes Ermittler-Ensemble]] (+2),
  [[Cleverer Twist-Plot]] (+2) und perfekter formaler Passung nur `liked` — **erstes Werk, das
  an einem einzigen Faktor scheitert**. [[Locked-Room-Mystery]] von Bedingung zu **Bonus**
  relativiert. Krimi-Gewichte nachgezogen (figuren 0.05→0.12). Neuer Autor [[Richard Osman]]
  (**Phänomen** — 17+ Mio. Bücher, reichweitenstärkster Autor im Vault; Netflix 2025).
  **Community-Score-Warnung verschärft:** Bd. 4 ist der *bestbewertete* Band (4,46) — die
  Mehrheit feiert genau den Störfaktor. Quelle: [[2026-08-11 Interview Der Donnerstagsmordclub]].
- 2026-07-20 — Werk 10: **[[Magic 2.0]]** (Scott Meyer, Comedy-SciFi), **loved** (als leichte
  Kost) — **neuer Kontext [[Humor-Phantastik]]**, 2. gelesenes Werk (Buch, kein Sprecher). Trägt
  über [[Absurder Humor]] (+2, jetzt 2 Kontexte), [[Nerd-/Popkultur-Humor]] (+2) & [[Originelle
  Prämisse]] (+2, „Realität = editierbare Datei"). Held Martin = cleverer aktiver Nerd-Everyman.
  **Zwei Kalibrier-Erkenntnisse:** (1) **Deutsch-Präferenz drastisch geschärft** — Englisch-Müdigkeit
  stoppte die *geliebte* Reihe bei Bd. 4 (nicht Qualität) → Englisch = starker Malus, nicht bloß
  Fallback. (2) **OP-Held ist im Humor-Kontext KEIN Malus** (Kontext schlägt global, Gegenprobe zu
  Scholomance). 5 neue Merkmale, neuer Autor [[Scott Meyer]]. Quelle: [[2026-07-20 Interview Magic 2.0]].
- 2026-07-20 — Werk 9: **[[Haus Ashford]]** (Benedict Jacka, An Inheritance of Magic, Urban
  Fantasy, 3 Bände), **mixed / „okay"** — **Negativ-Gegenentwurf beim SELBEN Autor** wie das
  geliebte [[Alex Verus]]. Gehört dt., **[[Johannes Klaußner]]** (hier **+1**, bei Verus 0 →
  Diskrepanz notiert). Beweist: die **Ausführung** entscheidet loved↔okay, nicht Autor/Genre —
  dieselbe UF-Handschrift, aber Magie [[Gedämpfte umständliche Magie|„lasch"]]/[[Unbalanciertes
  Machtsystem|geld-gated]] statt wuchtig+balanciert, Aufstieg zäh ([[Rückgestaute Machtkurve]] +
  neu [[Bremsender Alltags-Ballast]]), Held teils passiv/klagend ([[Weinerlicher Held]]). **6 neue
  Merkmale**, davon 2 Plus-Anker: [[Limit-Break-Momente]] (+2, „sehr gut, nur zu selten" → schärft
  roten Faden 2b) und [[Wissbegieriger Selbermacher-Held]] (+2). Kandidat „An Inheritance of Magic"
  → gelesen (Stub). Quelle: [[2026-07-20 Interview Haus Ashford]].
- 2026-07-20 — Werk 8: **[[Alex Verus]]** (Benedict Jacka, Urban Fantasy, 12 Bände), **loved**
  — **2. loved-Werk in [[Fantasy]] & erster Positiv-Gegenentwurf** zu den 3 Fantasy-„okay"-Werken.
  Gehört dt., **[[Johannes Klaußner]]** (neutral, „kein Verstärker"). Löst Progression-/Magie-
  Faden POSITIV ein: Machtaufstieg (+2) + [[Wuchtig-spektakuläre Magie]] (+2, „fliegen die
  Fetzen", balanciert) + [[Verborgene Magie im Alltag]] (+2) + neuer Plus-Typ [[Moralisch
  ambivalenter Antiheld]] (+2). Neue Schwächen: [[Rückgestaute Machtkurve]] (Aufstieg zu
  backloaded), [[Zu passiver Held]], [[Setup ohne Payoff]], [[Regel-Inkonsistenz]],
  [[Intrigen-Overload ohne Progress]]. 6 neue Merkmale; Fantasy setting-Gewicht 0.08→0.12.
  [[Trocken-ironischer Humor]] jetzt 3 Werke. Autor-Kandidat: „An Inheritance of Magic".
  Quelle: [[2026-07-20 Interview Alex Verus]].
- 2026-07-20 — **Vault-Metadaten-Kur (alle 6 Bestandswerke):** dt. Hördauern/ISBNs/Daten,
  RU-Jahre, GR-Snapshots nachrecherchiert; Award-Korrekturen (Scholomance: Dragon Award
  Bd. 3 YA, kein Locus/Hugo-Finalist); Konsistenz-Fixes (Sturmfels „abgeschlossen",
  Cunninghams-Scheinfragen). Deutsch-Präferenz jetzt auch für Print bestätigt.
- 2026-07-17 — **Branch-Zusammenführung auf `main`:** die interview-basierten Vollversionen
  der 3 „okay"-Werke ([[Riyria]], [[Survival Quest]], [[Scholomance]], MIT Aspekt-Bewertungen)
  und der Empfehlungslauf beider Sessions in einem `main` vereint. Ersetzt die frühere, aus
  dem Artefakt rekonstruierte Fassung (s. [[Profil]] Sync-Vorfall).
- 2026-07-17 — **Erster Empfehlungslauf:** [[2026-07-17 Deutsche Bücher quer über alle Räume]].
  Drei book-scout-Agenten (LitRPG/Fantasy/Krimi) → 31 Kandidaten → **5 verifizierte
  Empfehlungen** auf Deutsch: [[Die guten Jungs]] · [[Das Geheimnis von Askir]] ·
  [[Susan Ryeland ermittelt (Magpie Murders)]] · [[Hawthorne ermittelt]] ·
  [[Die Gilde der schwarzen Magier]]. (Riyria zurückgezogen: bereits „okay".) Format pro
  Titel noch offen (Mistborn/Rabenschatten als Buch nachrückbereit).
- 2026-07-16 — Werk 7: [[Riyria]] (Michael J. Sullivan, Revelations, 6 Bände), **mixed /
  „okay"** — 3. Graubereich-Werk, 2. mixed in [[Fantasy]]. Hörbuch dt., **[[David Nathan]]**
  (loved, 4. „trägt"-Stimme). **Doppel-Referenz:** geliebt [[Ungleiches Duo]] (+2, Royce &
  Hadrian) + [[Geheimnisvolle Macht]] (+2); Anti-Muster [[Flache Machtprogression]] (−2,
  „kein Limit-Break" → deckt jetzt BEIDE Pole), [[Unbalanciertes Machtsystem]],
  [[Schwache Haupthandlung]], [[Dünnes Weltdetail]], [[Setup ohne Payoff]]. Neuer Faden:
  Magie-/Power-Fantasy-Lean. Community rated Finale am höchsten (4,57), mein Urteil gegen
  den Trend. Quelle: [[2026-07-16 Interview Riyria]].
- 2026-07-16 — Werk 6: [[Scholomance]] (Naomi Novik, Trilogie), **mixed / „okay"** —
  2. Graubereich-Werk, erstes mixed in [[Fantasy]]. Hörbuch dt., **[[Leonie Landa]]**
  (loved, „trägt"). **+** konsistente düstere Welt, durchdachte Regeln, Akademie-
  Gemeinschaft, Überlebens-Countdown, bissig-lockere El-Stimme. **−** [[Flache
  Machtprogression]] (−2, OP von Anfang), [[Zäher Start]], [[Überladenes Weltdetail]],
  [[Eindimensionale Gegenspieler]], [[Romance-Überhang]], [[Dauer-Zynismus]]. 7 neue
  Merkmale; neuer roter Faden „Progression/Aufstieg > OP-von-Anfang" (2 Kontexte).
  Quelle: [[2026-07-16 Interview Scholomance]].
- 2026-07-16 — Werk 5: [[Survival Quest]] (Vasily Mahanenko), **mixed / „okay"** — erstes
  bewusst als „okay" eingebrachtes Werk, **Start des Graubereich-Durchlaufs**. LitRPG,
  Hörbuch dt., [[Thomas Balou Martin]] (neutral). Anti-Referenz zu [[Dungeon Crawler Carl]]:
  Sidequest-Wildwuchs (−2), [[Setup ohne Payoff]] (−2), [[Überzogener Auserwählter]] (−2),
  über-crunchig, schwache Rahmenhandlung. 7 neue Negativ-Merkmale, [[Nebenquest-Wildwuchs]]
  jetzt `status_global: disliked`, 2 Kombinationsregeln in [[LitRPG]]. Community ~4,19 >
  mein Urteil → hohe Genre-Wertung ≠ Passung. Quelle: [[2026-07-16 Interview Survival Quest]].
- 2026-07-16 — Werk 4: [[Die mörderischen Cunninghams]] (Benjamin Stevenson), **loved, top**.
  Neuer Kontext [[Krimi]]. **Erstes GELESENES Werk** (Buch, dt.) — Format-Lektion: immer
  erfragen, nie annehmen. [[Konstanter Vorwärtsdrang]] jetzt in 3 Kontexten (+2).
  Bekanntheit: Bestseller (TV-Verfilmung). Community-⌀ ~3,8 < mein Urteil → Locked-Room-Faible.
  Agent-Haltung geschärft: investigativer Journalist (Fakten graben, Gefühle bohren).
- 2026-07-16 — Sturmfels-Tiefeninterview: Bd. 1 fast abgebrochen (zäher Start −2, Niri
  zu schwach −2, Fokusverlust −2), gerettet durch [[Starkes Finale]]. Neu:
  [[Zu lange schwacher Held]], [[Nebenquest-Wildwuchs]], [[Starkes Finale]] +
  Kombinationsregel. Roter Faden „Fokus/Vorwärtsdrang" jetzt 3× belegt; neue Achse
  Held-Handlungsfähigkeit. Overall-Summe & Fantasy-Gewichte nachgezogen.
- 2026-07-16 — Prinz-Tiefeninterview: Eigen-Aspekte erhoben ([[Geheimnisvolle Macht]] +2,
  [[Verlorenes Erbe & Thronanspruch]] +2, [[Rache & Verfolgungsdruck]] +2; −1 [[Zäher Start]]
  & Fokusverlust). **[[Konstanter Vorwärtsdrang]] jetzt kontextübergreifend (roter Faden).**
  Overall [[Die Streitenden Götter]] als Summe beider Reihen ausstaffiert.
- 2026-07-16 — Werke 2+3: [[Die Streitenden Götter]] (Verbund) mit [[Sturmfels-Akademie]]
  (loved) + [[Der Prinz von Staub und Schatten]] (loved). Kontext [[Fantasy]] angelegt,
  [[Günter Merlau]] loved.
- 2026-07-16 — Lesestand (in Werk-Notiz): DCC Bd. 2 am Hören; Bd. 3+ warten
  auf dt. Fassung. **Sprachfrage geklärt: Deutsch bevorzugt.**
- 2026-07-16 — Erstes Buch analysiert: [[Dungeon Crawler Carl]] (loved, Hörbuch dt.,
  [[Stefan Kaminski]]). Kontext [[LitRPG]] angelegt, 12 Merkmale, No-Gos erfasst
  (Reihen-Pflicht ≥3 Bände, Romantasy-Fokus). Quelle: [[2026-07-16 Erstinterview Dungeon Crawler Carl]]
