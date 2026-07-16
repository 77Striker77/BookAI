# Datenschema – Geschmacksprofil (Kerndaten)

Dieses Verzeichnis ist der persistente Datenspeicher des Buch-/Hörbuch-Empfehlungssystems.
Alle Analysen und Empfehlungen bauen auf diesen Daten auf. **Nie raten – immer hier
nachschauen, bevor eine Suche oder Empfehlung startet.**

## Verzeichnisaufbau

```
taste-profile/
├── SCHEMA.md              ← dieses Dokument (Referenz)
├── profile.json           ← DEIN aggregiertes Geschmacksprofil (die Kerndaten)
├── profile.example.json   ← Beispiel/Vorlage
├── titles/                ← je analysiertem Titel eine JSON-Datei
│   └── <slug>.json
└── recommendations/       ← gespeicherte Empfehlungs-Läufe
    └── <datum>-<thema>.json
```

## 1. `profile.json` – Aggregiertes Geschmacksprofil

Das ist die verdichtete Wahrheit über den Geschmack des Nutzers, gewonnen aus allen
analysierten Titeln + Interview-Antworten. Struktur:

```json
{
  "updated": "2026-07-16",
  "language_pref": ["de", "en"],
  "format_pref": { "buch": true, "hoerbuch": true, "notes": "Hörbuch bevorzugt für lange Pendelstrecken" },

  "dimensions": {
    "genres":        { "loved": ["Dark Fantasy", "Literary SciFi"], "liked": ["Thriller"], "disliked": ["Cozy Romance"] },
    "themen":        { "loved": ["Moralische Grauzonen", "Verlust", "Machtmissbrauch"], "disliked": ["reine Wohlfühl-Handlung"] },
    "ton_stimmung":  { "loved": ["düster", "melancholisch", "bitter-humorvoll"], "disliked": ["kitschig"] },
    "erzaehlstil":   { "loved": ["unzuverlässiger Erzähler", "Multi-POV"], "disliked": ["allwissend distanziert"] },
    "tempo":         { "pref": "slow-burn mit Eskalation", "disliked": ["durchgehend hektisch"] },
    "komplexitaet":  { "pref": "hoch – verschachtelte Plots, Ambiguität" },
    "figuren":       { "loved": ["moralisch ambivalente Antihelden", "starke Nebenfiguren"], "pref": "character-driven" },
    "setting":       { "loved": ["dekadente Imperien", "kalte Nordwelten"], "disliked": [] },
    "laenge":        { "pref_pages": "400-700", "pref_hours": "12-25" },
    "emotion":       { "seeks": ["Sog", "Beklemmung", "Katharsis"] }
  },

  "hoerbuch": {
    "sprecher_loved": ["David Nathan"],
    "performance_pref": "voller Cast bevorzugt, aber starker Solo-Sprecher okay",
    "no_gos": ["monotone KI-Stimmen", "zu schnelles Tempo"]
  },

  "no_gos": ["Tierquälerei explizit", "Cliffhanger ohne Auflösung"],
  "weights": {
    "genres": 0.15, "themen": 0.25, "ton_stimmung": 0.20, "erzaehlstil": 0.10,
    "tempo": 0.08, "komplexitaet": 0.07, "figuren": 0.10, "setting": 0.05
  }
}
```

`weights` bestimmt, wie stark jede Dimension in den Gesamt-Match-Score (%) einfließt.
Summe ≈ 1.0. Wird während der Interviews justiert, wenn klar wird, was dem Nutzer
besonders wichtig ist.

## 2. `titles/<slug>.json` – Einzeltitel-Analyse

Für jeden vom Nutzer genannten (und geliebten/gehassten) Titel. `slug` = kebab-case
aus Titel, z. B. `der-name-des-windes.json`.

```json
{
  "title": "Der Name des Windes",
  "author": "Patrick Rothfuss",
  "year": 2007,
  "series": "Königsmörder-Chronik #1",
  "format_experienced": "hoerbuch",
  "narrator": "Stefan Kaminski",
  "verdict": "loved",           // loved | liked | mixed | disliked
  "isbn": "9783608938142",
  "sources": ["openlibrary:/works/OL...W", "google_books:...", "web:..."],

  "metadata": {
    "genres": ["Fantasy", "Coming-of-Age"],
    "subjects": ["magic school", "framed narrative", "music"],
    "page_count": 880,
    "audio_hours": 28.5,
    "language": "de",
    "ratings": { "goodreads": 4.5, "amazon": 4.6 }
  },

  "analysis": {
    "was_gefiel": ["Rahmenerzählung", "lyrische Sprache", "kompetenter Held mit Fehlern"],
    "was_stoerte": ["langsames Mittelteil"],
    "dna": {
      "genres": ["Fantasy"],
      "themen": ["Ruhm vs. Wahrheit", "Verlust", "Wissensdurst"],
      "ton_stimmung": ["melancholisch", "nostalgisch"],
      "erzaehlstil": ["Ich-Erzähler", "Rahmenerzählung", "unzuverlässig"],
      "tempo": "slow-burn",
      "komplexitaet": "hoch",
      "figuren": ["begabter Antiheld", "starke Frauenfiguren"],
      "setting": ["Fantasy-Universität", "mittelalterlich"]
    }
  },
  "user_quotes": ["Ich mochte, wie er sich selbst romantisiert erzählt"]
}
```

`analysis.dna` ist der wichtigste Teil: die extrahierte "Buch-DNA", auf die
Ähnlichkeitssuchen matchen.

## 3. `recommendations/<datum>-<thema>.json` – Empfehlungs-Läufe

Gespeichertes Ergebnis eines Suchlaufs, damit Empfehlungen nachvollziehbar und
Artefakte reproduzierbar sind. Enthält Referenztitel, Kandidaten mit Scores je
Dimension, Match-Gesamt-% und Begründung (was passt / was nicht). Struktur siehe
`book-similarity-search` Skill.

## Konventionen

- **Immer zuerst laden**, bevor gesucht wird. Fehlt `profile.json`, erst Interview + Analyse.
- Slugs kebab-case, klein, ohne Umlaute-Sonderfälle (ä→ae, ö→oe, ü→ue, ß→ss).
- Jede Zahl (Score, %) muss aus konkreten Daten ableitbar sein – keine erfundenen Metadaten.
- Quellen (`sources`) immer mitschreiben für spätere Verifikation.
