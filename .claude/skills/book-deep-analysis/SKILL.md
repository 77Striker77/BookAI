---
name: book-deep-analysis
description: >
  Tiefenanalyse einzelner Buch-/Hörbuchtitel. Nutze diesen Skill, um vom Nutzer genannte
  Titel gründlich zu untersuchen: alle Metadaten sammeln (Genre, Themen, Jahr, ISBN,
  Seiten/Hördauer, Sprecher, Bewertungen) UND die "Buch-DNA" extrahieren – was den Titel
  ausmacht und was der Nutzer daran mochte. Schreibt Ergebnisse nach taste-profile/ und
  aktualisiert das aggregierte Geschmacksprofil. Voraussetzung, bevor nach Ähnlichem
  gesucht wird ("kenne deine Daten").
---

# Deep-Analyse einzelner Titel

Bevor du irgendetwas empfiehlst, musst du die Referenztitel **wirklich verstehen** –
objektiv (Metadaten) und subjektiv (warum der Nutzer sie mochte). Das Ergebnis ist die
**Buch-DNA**, gegen die später gematcht wird.

## Ablauf pro Titel

### 1. Identität eindeutig klären
Titel + Autor + ggf. Reihe/Band + Ausgabe/Sprache. Bei Mehrdeutigkeit (gleiche Titel)
mit dem Nutzer abklären, welche Ausgabe/welcher Autor gemeint ist.

### 2. Metadaten sammeln (mehrere Quellen, keine Erfindung)
Siehe `references/metadata-sources.md` für konkrete Endpoints. Reihenfolge:
1. **Open Library** (frei, ohne Key) – Genres/Subjects, Jahr, ISBN, Cover, Seiten.
2. **Google Books** – Beschreibung, Kategorien, Seitenzahl, teils Bewertungen.
3. **Web-Suche/-Fetch** – für Themen, Ton, Rezensionen, Goodreads-Rating, und bei
   **Hörbüchern**: Sprecher/Narrator, Hördauer (Stunden), Voll-Cast vs. Solo, Verlag.

Erfasse mindestens: `genres`, `subjects/themen`, `year`, `series`, `isbn`, `page_count`,
`audio_hours` (bei Hörbuch), `narrator`, `language`, `ratings`. Notiere die `sources`.

### 3. Buch-DNA extrahieren (das Herzstück)
Verdichte Metadaten + Rezensionen + Interview-Antworten zu diesen Dimensionen (identisch
zu `taste-profile/SCHEMA.md`):

| Dimension     | Frage |
|---------------|-------|
| genres        | Welche Genres/Subgenres? |
| themen        | Welche Motive/Konflikte/Ideen trägt das Buch? |
| ton_stimmung  | Düster, warm, ironisch, episch, melancholisch…? |
| erzaehlstil   | POV, unzuverlässig, Rahmen, Prosa-Dichte, Struktur? |
| tempo         | Slow-burn ↔ Vollgas; gleichmäßig ↔ eskalierend? |
| komplexitaet  | Verschachtelung, Ambiguität, Anspruch? |
| figuren       | Figurentypen; character- ↔ plot-driven? |
| setting       | Ort/Zeit/Welt; Kulisse ↔ tragend? |

Trenne dabei sauber:
- **Was macht das Buch objektiv aus** (gilt für alle Leser).
- **Was der Nutzer konkret daran mochte** (`was_gefiel`) und was ihn störte (`was_stoerte`) –
  aus dem Interview. Das gewichtet später die DNA.

### 4. Persistieren
Schreibe `taste-profile/titles/<slug>.json` nach dem Schema. Aktualisiere danach
`taste-profile/profile.json`:
- Ergänze wiederkehrende Muster unter `dimensions.*.loved/liked/disliked`.
- Wenn eine Dimension über mehrere Lieblingsbücher konstant auftaucht, erhöhe ihr
  `weight` (und normalisiere die Summe ~1.0). Beispiel: Nutzer liebt bei allen Titeln
  "unzuverlässige Erzähler" → `erzaehlstil` höher gewichten.
- `updated`-Datum setzen (heutiges Datum aus dem Kontext).

### 5. Muster-Zusammenfassung an den Nutzer
Nach der Analyse: fasse in 3–6 Sätzen zusammen, was du jetzt über seinen Geschmack weißt.
Bei mehreren Titeln: nenne die **roten Fäden** ("In allen drei Titeln: moralisch
ambivalente Hauptfiguren + düsterer Ton + langsamer Aufbau"). Das ist die Basis, die im
Artefakt als "Kerndaten" erscheint.

## Qualitätsregeln
- Mindestens 2 unabhängige Quellen für harte Fakten (Jahr, Autor, ISBN).
- Unsichere Angaben markieren (`"year": "~2011?"`), nie glätten.
- Bei Reihen: kläre, ob der ganze Zyklus oder nur ein Band gemeint ist.
- Hörbuch ≠ Buch: derselbe Titel kann als Hörbuch anders wirken (Sprecher!). Beides
  getrennt vermerken, wenn relevant.
