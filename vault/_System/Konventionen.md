---
tags: [system]
---

# Konventionen des Vaults

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
├── Bibliothek/
│   ├── Werke/                 erlebte WERKE (= Reihe/Universum/Standalone) — mit
│   │                            ASPEKT-BEWERTUNGEN + Lesestand (siehe unten)
│   ├── Autoren/  Sprecher/    je Entität eine Notiz
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

- Eine Notiz in `Bibliothek/Werke/` = ein Werk (Reihe, Universum oder Standalone-
  Universum). Aspekt-Bewertungen, DNA und Verdikt gelten fürs Werk gesamt.
- **Lesestand als Tabelle in der Werk-Notiz** (welche Bände gehört/gelesen, was offen,
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
                                                          (→ Notiz wandert nach
                                                           Bibliothek/Werke/, Stub bleibt)
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
- `verdict`: loved | liked | mixed | disliked (Zusammenfassung der Aspekt-Bewertungen).
- **Keine erfundenen Werte**; `quellen:` pflegen; Unsicheres unter "Offene Fragen".
- Nach Änderungen: [[Home]] "Zuletzt", betroffene Kontext-/Merkmal-Notizen, [[Profil]].

## Wer liest/schreibt was

| Konsument | liest | schreibt |
|---|---|---|
| book-taste-interview | Profil/, Kontexte/, Merkmale/ | Interviews/, Kandidaten (erwaehnt) |
| book-deep-analysis | Interviews, Bibliothek/, Merkmale/ | Bücher (Aspekt-Bewertungen!), Merkmale/**, Entitäten, Kontexte/, Profil/ |
| book-similarity-search | Kontexte/, Merkmale/, Bücher/, **Kandidaten/** | Läufe/, **Kandidaten/** (Prognose + Historie) |
| book-reco-artifact | Kontexte/, Bücher/, neuester Lauf + Kandidaten | artifacts/*.html |
