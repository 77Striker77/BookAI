---
tags: [system]
---

# Konventionen des Vaults

Dieser Vault ist die **einzige Wahrheit** des Empfehlungssystems — ein normaler
Obsidian-Vault: atomare Notizen, YAML-Frontmatter, `[[Wikilinks]]`, Tags.
**Nie raten — immer hier lesen, bevor gesucht oder empfohlen wird.**

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
│   ├── Bücher/                erlebte Titel — mit ASPEKT-BEWERTUNGEN (siehe unten)
│   ├── Autoren/  Reihen/  Sprecher/     je Entität eine Notiz
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
                                                           Bibliothek/Bücher/, Stub bleibt)
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
