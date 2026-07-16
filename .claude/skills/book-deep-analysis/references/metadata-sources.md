# Metadaten-Quellen & Endpoints

Konkrete, frei nutzbare Quellen für Buch-/Hörbuch-Metadaten. Immer mit `WebFetch`/`WebSearch`
abrufen. **Considerate use:** Ergebnisse cachen (im Titel-JSON speichern), nicht spammen,
sinnvollen Kontext im Prompt mitgeben.

## 1. Open Library (frei, ohne API-Key) — primäre Metadatenquelle

Basis: `https://openlibrary.org`

- **Suche:**
  `https://openlibrary.org/search.json?q=TITEL+AUTOR&fields=title,author_name,first_publish_year,subject,isbn,key,edition_count,number_of_pages_median,ratings_average&limit=5`
  Liefert `docs[]` mit Titel, Autor, Erstveröffentlichung, **subjects** (Themen/Genres),
  ISBNs, Werk-Key, Seitenzahl-Median, Ø-Rating.

- **Werk-Details (Themen, Beschreibung):**
  `https://openlibrary.org/works/OL...W.json` → `subjects`, `description`.

- **ISBN → Edition:**
  `https://openlibrary.org/isbn/{isbn}.json`

- **Autor:**
  `https://openlibrary.org/authors/OL...A.json`

- **Cover (fürs Artefakt):**
  `https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg` (auch `-L.jpg`; oder `/b/id/{cover_id}-M.jpg`)

Stärken: strukturierte `subjects` (ideal für grobes Sieben), stabil, keine Limits-Hürden.
Schwächen: bei sehr neuen/Nischentiteln lückenhaft; Ton/Stimmung fehlt → per Web ergänzen.

## 2. Google Books (Beschreibungen, Kategorien)

- **Suche:**
  `https://www.googleapis.com/books/v1/volumes?q=intitle:TITEL+inauthor:AUTOR&maxResults=5`
  (öffentliche Daten meist ohne Key; bei Rate-Limit/Fehler auf Open Library + Web ausweichen).
  Nützliche Felder in `items[].volumeInfo`: `description`, `categories`, `pageCount`,
  `publishedDate`, `averageRating`, `industryIdentifiers` (ISBN).

Stärken: gute Klappentexte/Beschreibung (Basis für Themen & Ton). Schwächen: Kategorien grob.

## 3. Web-Suche/-Fetch — Ton, Themen, Rezensionen, Hörbuch-Daten

Für alles, was Struktur-APIs nicht liefern:
- **Themen & Ton:** Suche nach `"BUCHTITEL" themes tone review` bzw. `Rezension Themen Stil`.
- **Bewertungen:** Goodreads-Rating, Amazon-Sterne (per Suche, nicht scrapen was gesperrt ist).
- **Vergleichstitel:** `"books similar to BUCHTITEL"` / `"Bücher wie BUCHTITEL"` als
  zusätzliche Kandidatenquelle (aber immer eigenständig verifizieren!).

### Hörbuch-spezifisch
Struktur-APIs kennen Hörbuchdaten kaum. Per Web ermitteln:
- **Sprecher/Narrator:** `"HÖRBUCH" Sprecher gelesen von` / `narrated by`.
- **Hördauer (Stunden), ungekürzt/gekürzt, Voll-Cast vs. Solo, Hörbuchverlag.**
- Quellen: Audible-Produktseiten (Suche), Verlagsseiten (z. B. Hörverlag, Argon),
  Bibliothekskataloge. Audible hat keine offene API → über Suchergebnisse arbeiten.

## Priorität & Verifikation

1. Harte Fakten (Autor, Jahr, ISBN, Seiten): Open Library **und** Google Books abgleichen.
2. Weiche Merkmale (Themen, Ton): Google-Books-Beschreibung + ≥1 Rezension.
3. Hörbuch-Merkmale: ≥1 Händler-/Verlagsquelle.
4. Widersprüche nicht glätten → im JSON als unsicher markieren und Quelle notieren.

**Nie eine Zahl oder ein Genre erfinden.** Fehlt eine Angabe, bleibt sie leer/`null` mit Notiz.
