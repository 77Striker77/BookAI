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
│   ├── Profil.md              MOC "mein Geschmack" + skalare Präferenzen (Frontmatter)
│   ├── Gewichte.md            Match-Gewichte (Frontmatter) + Begründung (Body)
│   ├── No-Gos.md              harte Ausschlüsse, je mit Herkunft
│   └── Interviews/            je Interviewrunde eine datierte Notiz (Provenienz!)
├── Bibliothek/
│   ├── Bücher/                voll analysierte, ERLEBTE Titel (Buch-DNA)
│   ├── Autoren/  Reihen/  Sprecher/     je Entität eine Notiz
├── Merkmale/                  ⭐ DNA-Atome: je Merkmal EINE Notiz
│   ├── Genres/  Themen/  Ton/  Erzählstil/  Figuren/  Setting/
├── Empfehlungen/
│   ├── Warteliste.md          bestätigt, aber noch nicht gelesen/gehört
│   ├── Läufe/                 je Empfehlungslauf eine Notiz (Historie)
│   └── Kandidaten/            ⭐ GEDÄCHTNIS: jeder je berührte Titel
└── _System/
    ├── Konventionen.md        dieses Dokument
    └── Templates/             Kopiervorlagen für jeden Notiztyp
```

## Die Gedächtnis-Regel (wichtigste Regel)

**Jeder Titel, der je auftaucht, bekommt eine Notiz** — egal ob nur im Gespräch erwähnt,
in Stufe 1 grob gesichtet, in Stufe 2 verworfen oder empfohlen. Ohne Ausnahme.

Status-Lebenszyklus (`status:` im Frontmatter der Kandidaten-Notiz):

```
erwaehnt ──────────► (im Gespräch genannt, nicht weiter verfolgt)
gesichtet ─────────► (Stufe 1: grob geprüft; Kurzgrund, warum raus/nicht weiterverfolgt)
geprueft-verworfen ► (Stufe 2: tief geprüft & abgelehnt; Scores + Gründe PFLICHT)
empfohlen ─────────► (Stufe 2 bestanden, im Lauf ausgesprochen)
warteliste ────────► (Nutzer will es lesen/hören → auch in [[Warteliste]] eintragen)
gelesen ───────────► Notiz wandert nach Bibliothek/Bücher/ (volle Analyse),
                     Kandidaten-Notiz wird durch Verweis-Stub ersetzt
```

Konsequenzen:
- **Vor jeder Suche zuerst `Empfehlungen/Kandidaten/` lesen** (Frontmatter genügt):
  Verworfenes nie erneut vorschlagen (außer der Nutzer bittet um Neubewertung),
  Gesichtetes nicht doppelt recherchieren — vorhandene Metadaten wiederverwenden.
- Auch dem book-scout Agent die Liste bekannter Titel mitgeben ("überspringen").

## Verlinkungsregeln (das macht den Graphen)

- **Merkmale immer als Links, nie als tote Strings.** In Buch-/Kandidaten-Notizen:
  `ton: "[[Melancholisch]], [[Nostalgisch]]"` im Body-Abschnitt "DNA"; im Frontmatter
  zusätzlich als Klartext-Array für maschinelles Lesen (`ton: [Melancholisch, Nostalgisch]`).
- Existiert die Merkmal-Notiz noch nicht → **anlegen** (Template `Merkmal.md`), mit
  eigener Definition ("wie ICH das meine") und `status: loved|liked|neutral|disliked`.
- Autoren, Reihen, Sprecher ebenso verlinken (`[[Patrick Rothfuss]]`) und bei Bedarf anlegen.
- Backlinks beantworten dann: "alle Bücher mit [[Verlust]]", "alles von [[Stefan Kaminski]]".
- Matching Stufe 2 wird dadurch konkret: Welche loved-Merkmal-Notizen verlinkt der
  Kandidat, welche disliked? (Plus Gewichte aus [[Gewichte]].)

## Allgemeine Konventionen

- Dateiname = natürlicher Titel/Name: `Der Name des Windes.md`, `Patrick Rothfuss.md`.
  Bei Kollision Klammerzusatz: `Titel (Autor).md`.
- Frontmatter = maschinenlesbar (Metadaten, Status, Scores). Body = Bedeutung
  (Prosa, Begründungen, Zitate, Links).
- Templates aus `_System/Templates/` kopieren, nicht verändern.
- `verdict`: loved | liked | mixed | disliked. Tags klein: #loved, #hoerbuch, #buch.
- **Keine erfundenen Werte.** Fehlendes leer lassen + unter "Offene Fragen" notieren.
  `quellen:` immer pflegen.
- Nach jeder Änderung: [[Home]] "Zuletzt" kurz ergänzen; nach Analysen [[Profil]] und
  betroffene Merkmal-Notizen fortschreiben.

## Wer liest/schreibt was

| Konsument | liest | schreibt |
|---|---|---|
| book-taste-interview | Profil/, Merkmale/ | Profil/Interviews/<Datum>.md |
| book-deep-analysis | Interviews, Bibliothek/, Merkmale/ | Bibliothek/** , Merkmale/**, Profil/ |
| book-similarity-search | Profil/, Bibliothek/, Merkmale/, **Kandidaten/** | Empfehlungen/Läufe/, **Kandidaten/** |
| book-reco-artifact | Profil/, Bibliothek/, neuester Lauf | artifacts/*.html |
