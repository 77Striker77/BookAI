# 📚 BookAI — Buch- & Hörbuch-Empfehlungssystem

Ein persönlicher Kurator für **Bücher und Hörbücher**, gebaut als Set aus einem Agent und
mehreren Skills für Claude Code. Statt oberflächlicher „Wer das mochte…"-Listen versteht es
erst deinen Geschmack im Detail und liefert dann **verifizierte** Empfehlungen mit
transparenter Begründung.

## So funktioniert's — die 4 Phasen

```
1) INTERVIEW    Du nennst Titel, die du mochtest → gezielte Fragen, WAS genau dir gefiel
2) DEEP-ANALYSE Titel werden gründlich untersucht: alle Metadaten + „Buch-DNA"
3) SUCHE        Ähnliche Titel: erst grob sieben (passt der Rahmen?), dann tief verifizieren
4) ARTEFAKT     Visualisierung: Kerndaten + Empfehlungen mit %-Match-Balken & Begründung
```

Kernprinzipien:
- **„Kenne deine Daten."** Bevor gesucht wird, muss die Buch-DNA der Referenztitel vorliegen.
- **Immer ≥ 3 Vorschläge** — außer du forderst ausdrücklich etwas anderes (das hat Vorrang).
- **Zwei Stufen, streng verifiziert.** Was die Tiefenprüfung nicht besteht, wird verworfen.
- **Buch und Hörbuch** — bei Hörbüchern zählen Sprecher, Performance und Hördauer mit.
- **Keine erfundenen Metadaten.** Alles aus Quellen (Open Library, Google Books, Web).

## Loslegen

Sag einfach, was du mochtest — z. B.:

> „Ich habe *Der Name des Windes* als Hörbuch geliebt. Empfiehl mir 3 ähnliche Hörbücher."

Der Orchestrator-Skill (`book-recommender`) übernimmt: er interviewt dich, analysiert den
Titel, sucht & verifiziert und baut am Ende ein Artefakt. Weitere Beispiele:

- „Analysiere meinen Geschmack anhand dieser 3 Bücher: …"
- „Suche etwas wie *X*, aber weniger düster."
- „Was soll ich als Nächstes lesen?" (nutzt dein gespeichertes Profil)

## Aufbau

```
.claude/
├── agents/
│   └── book-scout.md              Read-only Rechercheur (Kandidaten-Fan-out)
└── skills/
    ├── book-recommender/          Orchestrator (Einstiegspunkt, steuert die 4 Phasen)
    ├── book-taste-interview/      Phase 1 — Geschmacks-Interview
    ├── book-deep-analysis/        Phase 2 — Metadaten + Buch-DNA  (+ references/)
    ├── book-similarity-search/    Phase 3 — Suche grob → tief + Scoring
    └── book-reco-artifact/        Phase 4 — Visualisierung  (+ HTML-Vorlage)

taste-profile/                     Persistenter Datenspeicher (dein Geschmack)
├── SCHEMA.md                      Datenschema (Kerndaten, Titel-DNA, Empfehlungen)
├── profile.json                  DEIN aggregiertes Profil  (aus profile.example.json)
├── titles/                       je analysiertem Titel eine JSON
└── recommendations/              je Empfehlungslauf eine JSON
```

## Datenquellen

- **[Open Library](https://openlibrary.org/developers/api)** — frei, ohne Key: Genres/
  Subjects, ISBN, Jahr, Seiten, Cover. Primäre Metadatenquelle.
- **[Google Books](https://developers.google.com/books)** — Beschreibungen, Kategorien.
- **Web-Suche/-Fetch** — Ton, Themen, Rezensionen, und bei Hörbüchern Sprecher/Hördauer.

Details & Endpoints: `.claude/skills/book-deep-analysis/references/metadata-sources.md`.

## Scoring in Kürze

Jede Empfehlung wird pro Dimension (Genre, Themen, Ton, Erzählstil, Tempo, Komplexität,
Figuren, Setting) mit 0–100 bewertet. Der **Gesamt-Match %** ist die mit deinen
persönlichen `weights` gewichtete Summe. Bestätigt wird nur, was ≥ 65 % erreicht, kein
No-Go verletzt und in keiner dir wichtigen Dimension durchfällt.

---

Das Profil wächst mit jeder Analyse — je mehr Titel du einbringst, desto schärfer die
Empfehlungen.
