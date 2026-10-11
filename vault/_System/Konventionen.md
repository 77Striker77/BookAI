---
tags: [system]
---

# Konventionen des Vaults (v2, 2026-10-11)

> **v2:** Fakten und Erleben getrennt, Feld `bereich:`, Personen und Gruppen, Besitz und
> Status als zwei Achsen, Cockpits je Bereich und Person. Grundlage: Umbauplan Phase 3
> (BookAI → TasteCompass_AI). Was v1 regelte, gilt weiter, wo hier nichts anderes steht.

Dieser Vault ist die **einzige Wahrheit** des Empfehlungssystems — ein normaler
Obsidian-Vault: atomare Notizen, YAML-Frontmatter, `[[Wikilinks]]`, Tags.
**Nie raten — immer hier lesen, bevor gesucht oder empfohlen wird.**

> ⚠️ **OBERSTE REGEL (siehe `CLAUDE.md`):** Der Vault ist die EINZIGE Quelle. Die
> `artifacts/*.html` sind nur **Projektionen** daraus — nur aus dem Vault erzeugt, nie
> umgekehrt. Enthält ein (auch veröffentlichtes) Artefakt mehr als der Vault, ist das ein
> Bug: **erst in den Vault backporten**, dann das Artefakt neu erzeugen. Publish nur mit
> committetem Vault-Stand (`bash scripts/vault-first.sh`).

## Struktur

```
vault/
├── Home.md                    Dashboard/MOC (Einstieg)
├── Profil/
│   ├── Profil.md              MOC "mein Geschmack": NUR kontextübergreifende Muster
│   ├── Kontexte/              ⭐ je Geschmacksraum (Genre-Cluster) eine Notiz mit
│   │   │                        EIGENEN Gewichten & Präferenzen (Fantasy ≠ Thriller!)
│   │   └── Kontexte.md        MOC + Zuordnungsregeln
│   ├── Gewichte.md            GLOBALE Default-Gewichte (Kontexte überschreiben sie)
│   ├── No-Gos.md              harte Ausschlüsse (global; Kontext-No-Gos in Kontext-Notiz)
│   └── Interviews/            je Interviewrunde eine datierte Notiz (Provenienz!)
├── Werke/
│   └── Buecher/               ⭐ FAKTEN je Werk (= Reihe/Universum/Standalone): Bände,
│                                Metadaten, Wertungen, Universum, DNA — einmal je Werk
├── Personen/
│   └── Lucas/
│       └── Erlebnisse/        ⭐ ERLEBEN je Werk und Person: Lesestand, Verdikt,
│                                Aspekt-Bewertungen, Spoiler-Grenze — „<Werk> – Lucas.md“
├── Bibliothek/
│   ├── Autoren/  Sprecher/    je Entität eine Notiz
│   ├── Figuren/              ⭐ je WERK ein Figurenverzeichnis „<Werk> – Figuren.md“
│   │                           (Personal + Kurzbeschreibung + Band der Ersteinführung).
│   │                           Deckt IMMER nur bis zum Lesestand ab — Figuren jenseits
│   │                           der Grenze werden gar nicht erst recherchiert (ihr Name
│   │                           allein ist ein Spoiler, s. Spoiler-Politik §4).
│   │                           Verlinkt aus der Werk-Notiz (Abschnitt „👥 Figuren“).
├── Merkmale/                  DNA-Atome: je Merkmal EINE Notiz, Status JE KONTEXT
│   ├── Genres/  Themen/  Ton/  Erzählstil/  Figuren/  Setting/
│   └── Handwerk/              ⭐ Ausführungsqualitäten: [[Aufgeblähter Mittelteil]],
│                                [[Starkes Finale]], [[Infodump-Weltenbau]] …
├── Empfehlungen/
│   ├── Warteliste.md
│   ├── Läufe/                 je Empfehlungslauf eine Notiz (Historie)
│   └── Kandidaten/            GEDÄCHTNIS: jeder je berührte Titel — mit Prognose je
│                                Aspekt + append-only Prüf-Historie + Wiedervorlage
└── _System/
    ├── Konventionen.md        dieses Dokument
    └── Templates/             Kopiervorlagen (9 Notiztypen)
```

## ⭐ Bewertungseinheit: das WERK, nicht der Einzelband

Der Nutzer bewertet **Reihen/Universen als Ganzes** — sein Empfinden bezieht sich fast
immer auf das komplette Werk (Nutzeraussage 16.07.2026). Deshalb:

- Eine Notiz in `Werke/Buecher/` = ein Werk (Reihe, Universum oder Standalone-
  Universum); dazu je Person eine Erlebnis-Notiz. Aspekt-Bewertungen, DNA und Verdikt
  gelten fürs Werk gesamt.
- **Lesestand als Tabelle in der Erlebnis-Notiz** (welche Bände gehört/gelesen, was offen,
  worauf gewartet wird) — kein separater Reihen-Ordner mehr.
- **NIE bandweise interviewen oder bewerten lassen.** Abweichungen einzelner Bände
  („Bd. 4 war zäh") nur erfassen, wenn der Nutzer sie VON SICH AUS nennt → Tabelle
  „Abweichungen einzelner Bände".
- Kandidaten sind ebenfalls **Werke** (die Reihe wird empfohlen, nicht Band 3).
- Bücher im selben Universum zählen als EIN Werk-Verbund (wichtig für die
  Reihen-Pflicht ≥3 Bände aus [[No-Gos]]).

### Werk-Verbund (mehrere Reihen in einem Universum) — Richtung: von unten nach oben!

Hat ein Universum mehrere Reihen mit je eigenem Flair (Beispiel: „Die Streitenden
Götter" = Sturmfels-Akademie + Prinz von Staub und Schatten):

- **Jede Reihe steht FÜR SICH** (`werk_typ: reihe`, Feld `universum:`): eigenständiges,
  voll bewertetes Werk mit eigenen Aspekten, eigenem Verdikt, eigenem Lesestand. Damit
  die Notiz allein lesbar ist, führt sie geteilte Aspekte als **geerbte Zeilen** auf
  (gekennzeichnet „geerbt aus [[Universum]]" — Pflege nur an der Quelle!).
- **Die Overall-Notiz ist der Elternknoten** (`werk_typ: universum`) und die **SUMME der
  untergeordneten Reihen**: sie steht in der Hierarchie OBEN und aggregiert (a) das
  Geteilte (Stil, Welt, Sprecher, gemeinsame Aspekte) UND (b) rollt die je eigenen
  Aspekte jeder Reihe auf ("eingebracht von [[Reihe X]]") zu einem Gesamtbild samt
  eigenem Schluss. Wird eine untergeordnete Reihe neu bewertet/ergänzt, MUSS die
  Overall-Summe nachgezogen werden. Reihen-Pflicht (≥3 Bände) wird hier geprüft.
- **Hierarchie/Darstellung — Overall oben, Reihen darunter eingerückt:**
  ```
  Die Streitenden Götter (Overall)
   ├─→ Sturmfels-Akademie (eigenständige Reihe)
   └─→ Der Prinz von Staub und Schatten (eigenständige Reihe)
  ```
  Im Artefakt: **zuerst die Overall-Karte (Kopf), dann darunter die Reihen-Karten**
  (eingerückt/als Kinder). Jede Reihe bleibt inhaltlich für sich voll bewertet.
- Matching: Reihen-Aspekte + geerbte Overall-Aspekte zusammen.

## 🔒 Spoilerfreiheit (Nutzerregel 2026-08-11)

> „wichtig ist auch im artefakt sollen keine inhaltlichen **spoiler** sein zu den teilen die
> ich noch nicht gelesen oder gehört habe!“

Verbindliche Ausformulierung: [[Spoiler-Politik]] (Wortlisten: [[Spoiler-Lexikon]]).
Gilt für **jede Ausgabe** — Artefakt, Chat-Antwort, Subagenten-Rückgabe. Der **Vault darf
mehr enthalten** (Arbeitsmaterial), versteckt Spoiliges aber im eingeklappten
`> [!warning]- 🔒 SPOILER`-Block. Maßgeblich ist der **Lesestand** des jeweiligen Werks.

| jenseits des Lesestands | erlaubt? |
| --- | --- |
| Titel (DE/EN), Bandnummer, Jahr, Hördauer, Sprecher, Verlag, ISBN | ✅ |
| Verfügbarkeit, Position in einer Lese-/Hörreihenfolge | ✅ |
| Wertungen, Stimmenzahl, Bekanntheit | ✅ |
| **Handlung, Wendungen, Figuren-Entwicklung, Orte, Ausgang eines Bandes** | ❌ |
| Community-Kritik, die Inhalte verrät (etwa: wer in Band Y ausscheidet) | ❌ |
| Community-Kritik ohne Inhalt („Bd. 7 hat Leerlauf“) | ✅ |

**Grenzfall Reihenfolge-Begründung:** Dass ein Band zwei Stränge zusammenführt, ist
**Reihenfolge-Information** und darf stehen — sonst wäre die Regel nicht begründbar. **Wie**
das geschieht, bleibt draußen. Im Zweifel: die Reihenfolge-Wirkung nennen, nicht die Handlung.

### Die Grenze maschinenlesbar (Pflichtfelder je Erlebnis-Notiz; `spoiler_aliase` in der Fakten-Notiz)

```yaml
spoiler_erlebt_bis: 5        # letzter VOLLSTÄNDIG erlebter Band (0 = keiner)
spoiler_aktuell: 6           # laufender Band — zählt als NICHT erlebt
spoiler_gesamt: 16           # erschienene Bände
spoiler_stand: "JJJJ-MM-TT"
spoiler_sperrbegriffe: []    # NUR neutrale Begriffe jenseits der Grenze, NIE das Ereignis
spoiler_aliase: []           # weitere Schreibweisen des Werktitels
spoiler_unerlebte_reihen: [] # Reihen im selben Universum, die NIE erlebt wurden
```

- **Frontmatter und die Lesestand-Tabelle im Body müssen übereinstimmen** — beide pflegen.
- Erscheint ein neuer Band, wächst `spoiler_gesamt`; ein `voll`-Werk rutscht dadurch
  automatisch auf `bis_band_N` zurück. Das ist gewollt.
- Handlungsdetails jenseits der Grenze gehören in der Notiz in einen eingeklappten Callout:
  `> [!warning]- 🔒 SPOILER — ab Bd. 7 (mein Stand: Bd. 5)`.
- Kontrolle: `python3 scripts/spoiler_check.py --grenzen`.
- Der **laufende Band zählt als NICHT erlebt**; unbekanntes Werk = ungelesen (fail-closed).
- Prüfen: `bash scripts/spoiler-gate.sh` (deterministisch) **und** Agent `spoiler-guard`
  (semantisch). Beides ist Pflicht vor jedem Artefakt-Publish.

## ⭐ Fakten und Erleben (v2) — was es einmal gibt und was je Person

„Fakten grabe ich, Gefühle erfrage ich“ ist ab v2 die Datenstruktur. Jedes erlebte Werk hat
**zwei** Notizen:

| | Fakten-Notiz | Erlebnis-Notiz |
| --- | --- | --- |
| Ort | `Werke/<Bereich>/<Werk>.md` | `Personen/<Person>/Erlebnisse/<Werk> – <Person>.md` |
| gibt es | einmal je Werk | einmal je Werk **und** Person |
| Frontmatter | Titel, Bände, Daten, ISBN, Hördauer, Sprecher, Wertungen, Bekanntheit, DNA, `spoiler_aliase`, `erlebnisse:` | `werk:`, `person:`, `kontext:`, `verdict:`, `format_erlebt:`, `sprache_erlebt:`, `bewertung:`, Spoiler-Grenze |
| Body | Universum, Bände, Metadaten, Community-Lob/-Kritik, Releases, DNA, Offene Fragen | Lesestand, Bewertung je Aspekt, Abweichungen, Hörbuch-Erlebnis, DNA-Begründung, Reihen-Gesamtbild |
| Vorlage | `Templates/Werk.md` | `Templates/Erlebnis.md` |

- **Links:** `[[Werk]]` zeigt immer auf die Fakten-Notiz. Die Erlebnis-Notiz verlinkt per
  `werk:` zurück, die Fakten-Notiz führt ihre Erlebnisse in `erlebnisse:`.
- **Gemischte Abschnitte** (Fakt und Empfinden in einem Absatz) gehören ins Erleben. Die
  Migration 2026-10-11 hat abschnittsweise getrennt (`scripts/umbau/werke_trennen.py`);
  gemischte Abschnitte werden bei Bedarf nachgeschärft, spätestens wenn eine zweite
  Person dasselbe Werk erlebt.
- Spoiler-Grenzen sind **je Person**: `scripts/spoiler_check.py` liest
  `Personen/<Person>/Erlebnisse/` (Person über `KURATOR_PERSON`, Standard `Lucas`).

## Bereich (v2)

Jede Werk- und Erlebnis-Notiz trägt `bereich:` — `buch` | `brettspiel` | `videospiel`
(weitere erst, wenn das erste Werk da ist). Je Bereich ein Unterordner in `Werke/`.
Bereichseigene Merkmale (z. B. Spielerzahl, Mechanik) fließen **nie** in das Matching
eines anderen Bereichs ein; übertragen wird nur über bereichsübergreifende Merkmale
(Ton, Themen, Figuren, Handwerk).

### Bereiche nicht vermischen — Geschmack wird je Bereich belegt (Nutzerregel 2026-10-11)

> „du musst aufpassen, die Medien auch nicht zu stark zu vermischen. Nur weil ich z. B.
> Magie-Bücher gerne höre, spiele ich dadurch nicht automatisch gerne Magie-Spiele.“

- **Merkmal-Notiz = gemeinsames Vokabular, nicht gemeinsamer Geschmack.** `bereiche:` sagt
  nur, wo ein Merkmal **vorkommen kann** (`[alle]` oder z. B. `[buch]`) — nie, ob es gefällt.
- **Jeder Kontext gehört zu genau einem Bereich** (`bereich:` in der Kontext-Notiz).
  `status_kontexte` und `status_global` gelten damit nur im Bereich, in dem sie belegt
  wurden — heute nur Bücher. Bekommt ein zweiter Bereich Wertungen, wird `status_global`
  zur Map je Bereich (`{buch: liked, videospiel: …}`), nicht überschrieben.
- **Keine automatische Übertragung.** Eine Wertung aus Büchern ist bei Spielen weder Bonus
  noch Malus. Der Geschmack in einem neuen Bereich wird dort eigens erfragt und belegt.
- **Erlaubt ist nur die Frage:** Ein Buch-Muster darf im Interview eines anderen Bereichs als
  **Frage** auftauchen („Magst du Magie auch in Spielen?“). Als Prognose bei einem Kandidaten
  höchstens mit Konfidenz `niedrig` und sichtbar als „aus Büchern vermutet“ — eine
  Empfehlung darf nie darauf ruhen.
- Offen für Phase 5: Die Merkmal-Status sind heute Lucas’ Geschmack; mit einer zweiten
  Person werden sie je Person geführt (s. „Personen und Gruppen“).

## Besitz und Status — zwei Achsen (v2)

In der Erlebnis-Notiz, unabhängig voneinander:

- `besitz:` `hat` | `wunsch` | `geliehen` | `verkauft` | leer (unbekannt)
- `status:` `geplant` | `laeuft` | `durch` | `abgebrochen` | leer (unbekannt)

Ein geliehenes Buch kann `durch` sein, ein Wunschtitel ist nicht im Besitz. **Nie
erfinden:** Für die 15 migrierten Werke sind beide Felder noch nicht erfragt.

## Personen und Gruppen — Geschmack bleibt getrennt (v2, Nutzerregel 2026-10-11)

> „du musst darauf auch aufpassen, dass wenn eine andere Person einen ganz anderen Geschmack
> hat, sie nicht plötzlich Dinge von mir empfohlen bekommt, nur weil sie vermeintlich nahe
> zu erreichen sind“

- Für Person X zählen **nur** X’ Erlebnisse, Profil, Kontexte und No-Gos. Erlebnisse anderer
  Personen sind **keine Evidenz, keine Kandidatenquelle und kein Bonus** beim Matching —
  auch nicht, wenn das Werk schon im Vault oder im Regal steht. Verfügbarkeit ist keine Passung.
- Das **Kandidaten-Gedächtnis gilt je Person**: Was eine Person verworfen hat, ist für eine
  andere nicht verworfen.
- **Gruppen** (z. B. „Wir zwei“) sind eigene Einträge unter `Personen/` mit eigenen
  Erlebnissen; für sie gelten die No-Gos **aller** Mitglieder zusammen.
- Ist unklar, für wen eine Empfehlung gedacht ist → fragen.

## Cockpits (v2, Nutzerentscheidung 2026-10-11)

Artefakte sind weiter reine Projektionen des Vaults. Aufteilung:

- je **Person** (und Gruppe) ein **Start-Cockpit**, das auf ihre Bereichs-Cockpits verlinkt
- je **Bereich und Person** eine **Bibliothek** (heute: Bücher · Lucas = `artifacts/bibliothek.html`)
- je **Person** (und Gruppe) ein **Empfehlungs-Cockpit**: „für mich“ → bei der Person,
  „für uns“ → bei der Gruppe (heute: Lucas = `artifacts/empfehlungen.html`)

Neue Cockpits entstehen erst, wenn es für sie Daten gibt — nicht auf Vorrat.

## Format (gelesen/gehört) — die Basis ist immer das Buch, der Sprecher ist Bonus

Regel (Nutzeraussage 2026-07-20): **Das Werk/Buch ist immer die Basis.** Ob der Nutzer
es **gelesen** (`format_erlebt: buch`) oder **gehört** (`format_erlebt: hoerbuch`, = Hörbuch
komplett durch) hat, ändert **nichts am inhaltlichen Matching** — die Ähnlichkeitssuche
läuft rein über die Werk-/Buch-DNA. Ein Kandidat wird nicht besser/schlechter, weil er
als Hörbuch vorliegt.

- **Format immer erfragen, nie annehmen** (pro Werk individuell; der Nutzer ist überwiegend
  Hörer, aber nicht immer). `format_erlebt` sauber setzen, damit gelesen/gehört
  unterscheidbar bleibt.
- **Der Sprecher ist eine ZUSÄTZLICHE Dimension — ausschließlich bei `hoerbuch`.** Nur
  dann nach ihm fragen (Stimme, Tempo, Betonung, Solo/Cast) und als eigene Aspekt-Zeile
  bewerten. Bei `buch` (gelesen) gibt es **keinen** Sprecher-Aspekt — Feld `sprecher: ""`.
- **Nutzen in Empfehlungen:** Ein **starker Sprecher wird als Plus aktiv hervorgehoben**
  (z. B. „…gelesen von einem Top-Sprecher wie [[…]]"). Er verschiebt nicht das
  inhaltliche Match, sondern ist ein zusätzliches Verkaufsargument obendrauf. Das stützt
  den roten Faden „starker Sprecher (Hörbuch)".

## Negativraum: disliked/abgebrochene Werke = eigener Durchlauf

Bislang enthält die Bibliothek nur `loved`-Werke. **Was der Nutzer NICHT mochte oder
abgebrochen hat, ist für gutes Matching genauso wertvoll** (Anti-Muster). Solche Werke
werden über denselben Workflow erfasst (Interview → Analyse), Verdikt `disliked`/`mixed`;
ihre Negativ-Aspekte (−2/−1) schärfen die weichen Ausschlüsse. Der Nutzer bringt sie
bewusst als eigenen Durchlauf ein — nicht drängen, aber die Lücke kennen und bei
Gelegenheit einladen.

## Kontexte (Geschmacksräume) — Geschmack ist nicht global

Was in Fantasy geliebt wird, kann im Thriller egal oder störend sein. Deshalb:

- Ein **Kontext** = grober Geschmacksraum (z. B. `Fantasy`, `Thriller/Krimi`, `SciFi`,
  `Sachbuch`). Notiz unter `Profil/Kontexte/` (Template `Kontext.md`), angelegt, sobald
  das erste Buch dieses Raums analysiert wird — nicht auf Vorrat.
- Jede Kontext-Notiz trägt: eigene `gewichte:` (überschreiben [[Gewichte]]), eigene
  Top-loved/disliked-Merkmale, Längen-/Tempo-Präferenz, ggf. Kontext-No-Gos.
- Jedes Buch und jeder Kandidat bekommt `kontext:` im Frontmatter (über seine Genres
  zugeordnet; Zuordnungsregeln in `Kontexte/Kontexte.md`). Grenzfälle: der dominante Raum.
- **Matching läuft immer im Kontext des Kandidaten**: dessen Gewichte + Merkmal-Status
  in DIESEM Kontext. Existiert (noch) kein Kontext → globale Defaults.
- [[Profil]] selbst hält nur noch das Kontextübergreifende: rote Fäden, die überall
  gelten, globale No-Gos, Format-/Sprachpräferenzen.

## Aspekt-Bewertungen — ein Buch ist kein Monolith

`verdict: loved` ist nur die Zusammenfassung. Die eigentliche Währung ist die
**Bewertung je Aspekt** in jeder Buch-Notiz:

| Skala | Bedeutung |
|---|---|
| +2 | herausragend, trägt das Buch für mich |
| +1 | gefiel |
| 0 | neutral / egal |
| −1 | störte |
| −2 | hat es mir fast/ganz verdorben |

- Jede Zeile: **Aspekt als `[[Merkmal-Link]]`** + Wertung + Warum + möglichst Beleg/Zitat.
- Auch geliebte Bücher haben negative Zeilen ("Mittelteil zieht: −1") — und die zählen
  beim Matching: ein Kandidat, der für [[Aufgeblähter Mittelteil]] bekannt ist, wird
  abgestraft, selbst wenn er sonst der Referenz ähnelt.
- Wiederkehrende Kritikpunkte über mehrere Bücher → als Merkmal-Notiz anlegen (oft in
  `Merkmale/Handwerk/`) und in der Kontext-/Profil-Notiz als Muster vermerken.
- Frontmatter spiegelt die Tabelle maschinenlesbar: `bewertung: [{aspekt, wert}, …]`.

## Merkmal-Status je Kontext

Merkmal-Notizen haben `status_global` UND `status_kontexte` (Map). Beispiel
[[Explizite Gewalt]]: Thriller `neutral`, Fantasy `disliked`. Evidenz (welches
Buch/Interview) steht in der Merkmal-Notiz; Backlinks zeigen alle Träger.

## Die Gedächtnis-Regel

**Jeder Titel, der je auftaucht, bekommt eine Kandidaten-Notiz** — erwähnt, grob
gesichtet, tief geprüft, empfohlen. Ohne Ausnahme. Zusätzlich gilt:

```
erwaehnt → gesichtet → geprueft-verworfen | empfohlen → warteliste → gelesen
                                                          (→ Fakten nach Werke/<Bereich>/,
                                                           Erleben nach Personen/<P>/Erlebnisse/,
                                                           Stub bleibt)
```

- **Prüf-Historie ist append-only:** jede Prüfung wird als neue Zeile angehängt
  (Datum, Lauf, Status, Score, Grund) — nie alte Einträge überschreiben. So sieht man,
  DASS und WARUM ein Titel schon 2× verworfen wurde.
- **Prognose je Aspekt** statt Pauschalurteil: erwartete Wertung pro Merkmal mit Beleg
  (Rezensionszitat, Quelle). Das macht Verwerfen/Bestätigen nachprüfbar.
- **Wiedervorlage-Trigger:** wenn ein Verwerfen an EINER Präferenz hing ("Tempo zu
  langsam"), notieren: "neu prüfen, falls sich ⟨Präferenz⟩ ändert". Ändert sich das
  Profil an dieser Stelle → Kandidat automatisch wieder in den Pool.
- Vor jeder Suche zuerst `Kandidaten/` sichten (Frontmatter genügt); Verworfenes nie
  erneut vorschlagen (außer Wiedervorlage-Trigger greift oder Nutzer bittet darum).
  Skip-Liste an den book-scout Agent geben.

## Granularität auf Abruf — Split-Regeln (WICHTIG)

**Keine leeren Strukturen auf Vorrat.** Die Struktur wird feiner, wo die Evidenz es
verlangt — nach diesen Regeln:

1. **Merkmal-Split:** Bewertet der Nutzer dasselbe Merkmal im selben Kontext
   **widersprüchlich** (≥2 Datenpunkte, z. B. [[Melancholisch]] einmal +2, einmal −1),
   ist das Merkmal zu grob → in Varianten spalten (z. B. [[Elegisch]] vs.
   [[Deprimierend]]). Die Eltern-Notiz bleibt als Hub (`varianten:`), die Kinder tragen
   `uebergeordnet:`. Alte Bewertungszeilen auf die passende Variante umziehen
   (Interview klärt, welche gemeint war). Nie spekulativ spalten — nur bei belegtem
   Widerspruch.
2. **Kontext-Split (Sub-Kontexte):** Laufen innerhalb eines Kontexts Gewichte oder
   Merkmal-Status systematisch auseinander (z. B. Grimdark-Titel folgen anderem Muster
   als High-Fantasy-Titel), Sub-Kontext anlegen (`uebergeordnet:` in der
   Kontext-Notiz). Sub-Kontext erbt alles Nicht-Überschriebene vom Eltern-Kontext.
3. **Kombinationsregeln (Wechselwirkungen):** Vorlieben sind oft bedingt —
   "[[Ich-Erzähler]] nur gut MIT [[Unzuverlässig]]", "[[Explizite Gewalt]] okay, außer
   kombiniert mit [[Tierleid]]". Solche Regeln leben in der Kontext-Notiz (Abschnitt
   "Kombinationsregeln", Wenn/Dann/Evidenz) und schlagen beim Matching die
   Einzel-Status der beteiligten Merkmale.
4. **Konfidenz:** Prognose-Zeilen bei Kandidaten tragen eine Konfidenz
   (hoch/mittel/niedrig — wie belastbar ist der Beleg?). Eine Empfehlung darf nicht
   allein auf niedrig-konfidenten Prognosen ruhen; im Zweifel weiter recherchieren
   oder transparent als Unsicherheit ausweisen.

## Verlinkungsregeln (das macht den Graphen)

- **Merkmale immer als Links, nie als tote Strings** — in Büchern UND Kandidaten
  (Bewertungs-/Prognose-Tabellen). Frontmatter zusätzlich als Klartext-Arrays.
- Fehlende Merkmal-/Autor-/Reihen-/Sprecher-/Kontext-Notizen anlegen (Templates),
  mit eigener Definition ("wie ICH das meine") und Evidenz-Links.
- Backlinks beantworten: "alle Träger von [[Verlust]]", "alles von [[Stefan Kaminski]]",
  "alle Bücher im Kontext [[Fantasy]]".

## Allgemeine Konventionen

- Dateiname = natürlicher Titel/Name; Kollision → `Titel (Autor).md`.
- Frontmatter = maschinenlesbar. Body = Bedeutung (Prosa, Begründung, Zitate, Links).
- Templates aus `_System/Templates/` kopieren, nicht verändern.
- `verdict`: loved | liked | mixed | disliked | **offen** (Zusammenfassung der Aspekt-Bewertungen).
  `offen` = **Bewertung bewusst ausgesetzt**, weil die Grundlage nicht reicht (Nutzer sagt selbst,
  er könne noch nichts sagen). Nicht dasselbe wie „noch nicht erfasst": `offen` ist eine
  bewusste Entscheidung und braucht `verdict_status:` (Begründung + Zitat + Datum) sowie
  `wiedervorlage:` (wann nachgefragt wird). **Nie** aus Bequemlichkeit statt eines echten
  Verdikts setzen — und **nie** eine vorläufige Zahl erfinden, wo der Nutzer schweigt.
- ⭐ **Rangfolge der Erscheinungsdaten (Nutzerregel 2026-08-11).** Wenn ein Datum *das* Datum
  eines Werks sein soll — Kopfzeile, Regal-Etikett, Uebersicht — gilt:
  1. **BUCH schlaegt HOERBUCH.** Das Hoerbuchdatum ist ein Detail und gehoert in die Bandliste,
     nie in die Kopfzeile. Zitat: *„Hoerbuch-Release ist zwar interessant, aber nur ein Detail,
     der Buchrelease ist wichtiger."*
  2. **DEUTSCH schlaegt INTERNATIONAL** — aber nur, wenn es die deutsche **Buch**ausgabe
     wirklich gibt.
  3. Gibt es keine deutsche Buchausgabe, steht das internationale Datum da, **sichtbar als
     solches markiert** (🌍) statt stillschweigend geglaettet. Passt zur Regel „nie glaetten".
  Quelle bleibt `erscheinungsdatum_bd1` / `letztes_datum` der Werk-Notiz.
- **Keine erfundenen Werte**; `quellen:` pflegen; Unsicheres unter "Offene Fragen".
- Nach Änderungen: [[Home]] "Zuletzt", betroffene Kontext-/Merkmal-Notizen, [[Profil]].

## Wer liest/schreibt was

| Konsument | liest | schreibt |
|---|---|---|
| book-taste-interview | Profil/, Kontexte/, Merkmale/ | Interviews/, Kandidaten (erwaehnt) |
| book-deep-analysis | Interviews, Werke/, Erlebnisse/, Bibliothek/, Merkmale/ | Werke/Buecher/ (Fakten), Erlebnisse/ (Aspekt-Bewertungen!), Merkmale/**, Entitäten, Kontexte/, Profil/ |
| book-similarity-search | Kontexte/, Merkmale/, Werke/, Erlebnisse/, **Kandidaten/** | Läufe/, **Kandidaten/** (Prognose + Historie) |
| book-reco-artifact | Kontexte/, Werke/, Erlebnisse/, neuester Lauf + Kandidaten | artifacts/*.html |
