---
name: book-deep-analysis
description: >
  Tiefenanalyse einzelner Buch-/Hörbuchtitel. Nutze diesen Skill, um vom Nutzer genannte
  Titel gründlich zu untersuchen: alle Metadaten sammeln (Genre, Themen, Jahr, ISBN,
  Seiten/Hördauer, Sprecher, Bewertungen) UND die "Buch-DNA" extrahieren – was den Titel
  ausmacht und was der Nutzer daran mochte. Schreibt Ergebnisse atomar in den
  Obsidian-Style Vault: Buch-Notiz + verlinkte Merkmal-/Autor-/Sprecher-/Reihen-Notizen
  + Profil-Update. Voraussetzung, bevor nach Ähnlichem gesucht wird ("kenne deine
  Daten"). Danach "Meine Bibliothek"-Artefakt updaten.
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

**Pflicht: bandgenaue Metadaten, BOTTOM-UP** (Abschnitte „Die Bände einzeln",
„Nächste Releases", „Reihen-Gesamtbild" aus `Werk.md`). Reihenfolge strikt:
**erst jeder Band einzeln, das Reihen-Fazit ist IMMER der letzte Schritt.**

Für **JEDEN Band** erfassen (Tabelle + Lob/Kritik):
- **Titel** (deutsch UND englisch, falls beide existieren).
- **Erscheinungsdatum getrennt 🇩🇪 Deutsch und 🇬🇧 Englisch** (Buch und Hörbuch) — Deutsch
  und Englisch sind die wichtigen Sprachen. Fehlt eine Sprache: „noch nicht auf DE/EN".
- **Echte Nutzerwertung mit ANZAHL** je Quelle (Goodreads/LovelyBooks/Amazon/Audible),
  z. B. „4,6/5 bei 45 000". **Buch- und Hörbuch-Wertungen zum Inhalt gemeinsam** nutzen;
  Sprecher-/Produktionskritik separat halten. Keine erfundenen Zahlen — sonst „—".
- **Echtes Lob und echte Kritik** aus Rezensionen (konkrete Stichpunkte, nicht abstrakt).
- **Band-Unterschiede** notieren, wenn Wertungen schwanken (z. B. schwächerer Auftakt).

**Nächste Releases & Planung:** wann kommt der nächste Band auf **Deutsch** bzw.
**Englisch** (Termin/Ankündigung); Bände erschienen vs. geplant; Status; angekündigte
Erweiterungen (Spin-offs, Musik-EPs, Verfilmung) — oder „nichts bekannt".

**Reihen-Gesamtbild ZULETZT:** erst wenn alle Bände erfasst sind, das Fazit ziehen
(⌀-Wertung, roter Faden von Lob/Kritik, Abgleich mit MEINEM Empfinden). Bei einem
Universum fließt dieses Reihen-Fazit dann in die Overall-Notiz ein (die Overall-Summe
ist der allerletzte Schritt).

### 3. Buch-DNA extrahieren (das Herzstück)
Verdichte Metadaten + Rezensionen + Interview-Antworten zu diesen Dimensionen (Felder
identisch zum Frontmatter in `vault/_System/Templates/Werk.md`):

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

Zusätzlich die Dimension **handwerk** (Ausführungsqualität): Pacing-Probleme, Stärke
des Finales, Infodumps, Dialogqualität … — wiederkehrende Kritikpunkte des Nutzers
leben als Merkmal-Notizen unter `Merkmale/Handwerk/`.

**Kontext zuordnen:** Bestimme den Geschmacksraum des Titels (`kontext:`, z. B.
Fantasy) nach den Regeln in `vault/Profil/Kontexte/Kontexte.md`. Existiert der Kontext
noch nicht → Kontext-Notiz anlegen (Template `Kontext.md`).

**⭐ Aspekt-Bewertungen (die eigentliche Währung):** Zerlege das Nutzer-Urteil in
einzelne Aspekte — Tabelle "Bewertung je Aspekt" in der Buch-Notiz: je Zeile
`[[Merkmal-Link]]` + Wertung **−2..+2** + Warum + Beleg (Nutzer-Zitat/Szene).
Auch geliebte Bücher haben negative Zeilen — genau die machen das Matching scharf.
`verdict` ist nur die begründete Summe. Trenne dabei sauber:
- **Was macht das Buch objektiv aus** (gilt für alle Leser) → DNA.
- **Wie bewertet der NUTZER jeden Aspekt** (aus dem Interview) → Bewertungstabelle.

### 4. Persistieren (Vault, atomar — das ist der Graph-Aufbau)
Templates aus `vault/_System/Templates/`, Konventionen aus `vault/_System/Konventionen.md`.

1. **Werk-Notiz:** `vault/Bibliothek/Werke/<Werktitel>.md` (Template `Werk.md`).
   ⭐ **Bewertungseinheit ist das WERK** (Reihe/Universum als Ganzes) — NIE bandweise
   interviewen/bewerten; Band-Abweichungen nur, wenn der Nutzer sie selbst nennt.
   Frontmatter = Metadaten + DNA + `kontext:` + `bewertung:` maschinenlesbar; Body =
   **Bewertungstabelle je Aspekt** (mit Belegen), **Lesestand-Tabelle** (welche Bände
   gehört/gelesen/wartend), DNA als `[[Links]]`, Begründungen.
   War das Werk vorher Kandidat → Kandidaten-Notiz auf `status: gelesen` (Historie-Zeile
   anhängen!) und durch Verweis-Stub ersetzen ("→ [[Werk]] in Bibliothek").
2. **Merkmal-Notizen:** für JEDES bewertete/DNA-Merkmal (inkl. Handwerk!) prüfen, ob
   die Notiz unter `vault/Merkmale/<Dimension>/` existiert — sonst anlegen (Template
   `Merkmal.md`, eigene Definition). **Status je Kontext** pflegen (`status_kontexte`
   + Tabelle "Wirkung nach Kontext" mit Evidenz), `status_global` nur wenn
   kontextübergreifend belegt.
3. **Kontext-Notiz aktualisieren** (`vault/Profil/Kontexte/<Raum>.md`): Bücherzähler,
   Top-Merkmale-Tabelle, ggf. Gewichte MIT Begründung in der Änderungshistorie
   (z. B. Handwerk > 0, sobald Handwerks-Muster belegt). Übersichtstabelle in
   `Kontexte.md` pflegen.
4. **Entitäts-Notizen:** Autor (`Bibliothek/Autoren/`) und Sprecher (`Sprecher/`)
   anlegen/fortschreiben — inkl. Abschnitt "Weitere Werke/Einlesungen" als spätere
   Kandidatenquelle. (Reihen-Infos/Lesestand leben IN der Werk-Notiz.)
5. **Profil aktualisieren:** `vault/Profil/Profil.md` NUR mit kontextübergreifend
   bestätigten Mustern (roter Faden, Tabelle "Analysierte Titel"). Kontextspezifisches
   gehört in die Kontext-Notiz. Neue harte Ausschlüsse → `No-Gos.md` mit Herkunft.
6. **Split-Check (Granularität auf Abruf,** Konventionen → Split-Regeln**):**
   - Widerspricht die neue Bewertung eines Merkmals einer früheren im selben Kontext
     (z. B. [[Melancholisch]] jetzt −1, vorher +2)? → Nachfrage beim Nutzer, worin der
     Unterschied liegt, dann Merkmal in **Varianten spalten** (Hub + `uebergeordnet:`),
     alte Bewertungszeilen umziehen.
   - Zeigt sich eine **Bedingung** ("nur gut, wenn…")? → als **Kombinationsregel** in
     die Kontext-Notiz (Wenn/Dann/Evidenz).
   - Folgen mehrere Titel eines Kontexts einem klar anderen Muster? → **Sub-Kontext**
     erwägen (mit dem Nutzer bestätigen).
7. **Wiedervorlagen prüfen:** Hat sich durch diese Analyse eine Präferenz geändert
   (Gewicht, Merkmal-Status, Split, neue Kombinationsregel), sichte
   `Empfehlungen/Kandidaten/` nach Notizen, deren `wiedervorlage:` darauf triggert →
   dem Nutzer als Re-Check-Kandidaten nennen.
8. **`vault/Home.md`** → "Zuletzt" ergänzen.

**Danach `book-reco-artifact` aufrufen**, um das Basis-Artefakt "Meine Bibliothek" zu
aktualisieren (gleiche URL, nie neues Artefakt).

### 5. Muster-Zusammenfassung an den Nutzer
Nach der Analyse: fasse in 3–6 Sätzen zusammen, was du jetzt über seinen Geschmack weißt.
Bei mehreren Titeln: nenne die **roten Fäden** ("In allen drei Titeln: moralisch
ambivalente Hauptfiguren + düsterer Ton + langsamer Aufbau"). Das ist die Basis, die im
Artefakt als "Kerndaten" erscheint.

## Qualitätsregeln
- Mindestens 2 unabhängige Quellen für harte Fakten (Jahr, Autor, ISBN).
- Unsichere Angaben markieren (`jahr: "~2011?"` + Notiz unter "Offene Fragen"), nie glätten.
- Bei Reihen: kläre, ob der ganze Zyklus oder nur ein Band gemeint ist.
- Hörbuch ≠ Buch: derselbe Titel kann als Hörbuch anders wirken (Sprecher!). Beides
  getrennt vermerken, wenn relevant.
