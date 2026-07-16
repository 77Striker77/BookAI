# 📔 Vault — die Datenquelle (Obsidian-Style)

Dieser Ordner ist die **einzige Wahrheit** des Empfehlungssystems. Alles Markdown mit
YAML-Frontmatter und `[[Wikilinks]]` — direkt als Obsidian-Vault öffenbar. **Nie raten —
immer hier lesen, bevor gesucht oder empfohlen wird.**

## Aufbau

```
vault/
├── README.md                  ← dieses Dokument (Konventionen)
├── Profil.md                  ← aggregiertes Geschmacksprofil (Kerndaten + Gewichte)
├── Bücher/                    ← je Titel eine Notiz: Metadaten (Frontmatter) + Analyse (Body)
│   ├── _TEMPLATE.md
│   └── <Titel>.md             z. B. "Der Name des Windes.md"
└── Empfehlungen/              ← je Empfehlungslauf eine Notiz (Historie bleibt erhalten)
    ├── _TEMPLATE.md
    └── <JJJJ-MM-TT> <Thema>.md
```

## Konventionen

- **Dateinamen = natürliche Titel** (Obsidian-Style): `Der Name des Windes.md`.
  Verlinken mit `[[Der Name des Windes]]`.
- **Frontmatter = maschinenlesbare Metadaten** (die "harten" Felder, gegen die gematcht
  wird). **Body = Analyse in Prosa** (was gefiel, Buch-DNA-Begründung, Zitate).
- Templates (`_TEMPLATE.md`) kopieren, nicht verändern.
- `verdict`: `loved | liked | mixed | disliked`.
- Tags: `#loved`, `#hoerbuch`, `#buch`, `#analysiert`, `#empfohlen`, `#verworfen`.
- Listen im Frontmatter als YAML-Arrays (`themen: [Verlust, Machtmissbrauch]`).
- **Keine erfundenen Werte.** Fehlt etwas → Feld leer lassen + im Body unter
  `## Offene Fragen` notieren. `quellen:` immer pflegen.
- Nach jeder Titel-Analyse: `Profil.md` aktualisieren (Muster ergänzen, ggf. Gewichte
  justieren, `aktualisiert:` setzen).

## Was liest wer?

| Konsument | liest | schreibt |
|---|---|---|
| book-taste-interview | Profil.md | Roh-Notizen → an Analyse |
| book-deep-analysis | Bücher/, Profil.md | Bücher/<Titel>.md, Profil.md |
| book-similarity-search | Profil.md, Bücher/ | Empfehlungen/<Datum Thema>.md |
| book-reco-artifact | Profil.md, Bücher/, neueste Empfehlung | artifacts/*.html |
