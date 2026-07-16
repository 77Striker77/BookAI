# 📚 BookAI — Buch- & Hörbuch-Empfehlungssystem

Ein persönlicher Kurator für **Bücher und Hörbücher**, gebaut als Set aus einem Agent und
mehreren Skills für Claude Code. Statt oberflächlicher „Wer das mochte…"-Listen versteht es
erst deinen Geschmack im Detail und liefert dann **verifizierte** Empfehlungen mit
transparenter Begründung.

## So funktioniert's — die 4 Phasen

```
1) INTERVIEW    Du nennst Titel, die du mochtest → gezielte Fragen, WAS genau dir gefiel
2) DEEP-ANALYSE Titel werden gründlich untersucht: alle Metadaten + „Buch-DNA"
                → ins Vault geschrieben + Artefakt „Meine Bibliothek" aktualisiert
3) SUCHE        Ähnliche Titel: erst grob sieben (passt der Rahmen?), dann tief verifizieren
4) ARTEFAKT     Artefakt „Empfehlungen" wird ÜBERSCHRIEBEN: Kerndaten + ≥3 Vorschläge
                mit %-Match-Balken & Begründung was passt / was nicht
```

## Die zwei festen Artefakte

| Artefakt | Inhalt | Verhalten |
|---|---|---|
| 📚 **Meine Bibliothek** | alle guten Bücher mit wichtigsten Infos & Metadaten + Geschmacks-Kerndaten | wird bei jeder Analyse **aktualisiert** (gleiche URL) |
| 🎯 **Empfehlungen** | der jeweils letzte Empfehlungslauf mit %-Balken | wird je Lauf **überschrieben** (gleiche URL) |

Es entstehen nie zusätzliche Artefakte; die Historie aller Läufe liegt im Vault.

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
    └── book-reco-artifact/        Phase 4 — die 2 festen Artefakte  (+ HTML-Vorlagen)

vault/                             Datenquelle: Obsidian-Style Vault (alles Markdown)
├── README.md                      Konventionen (Frontmatter, Wikilinks, Tags)
├── Profil.md                      DEIN aggregiertes Geschmacksprofil + Gewichte
├── Bücher/                        je analysiertem Titel eine Notiz (_TEMPLATE.md)
└── Empfehlungen/                  je Empfehlungslauf eine Notiz — die Historie

artifacts/                         die 2 festen HTML-Artefakte (stabile Pfade & URLs)
├── bibliothek.html                📚 Meine Bibliothek (Basis)
└── empfehlungen.html              🎯 Empfehlungen (wird überschrieben)
```

Der `vault/`-Ordner ist ein normaler Obsidian-Vault — du kannst ihn direkt in Obsidian
öffnen und darin stöbern oder selbst Notizen ergänzen.

## Datenquellen

- **[Open Library](https://openlibrary.org/developers/api)** — frei, ohne Key: Genres/
  Subjects, ISBN, Jahr, Seiten, Cover. Primäre Metadatenquelle.
- **[Google Books](https://developers.google.com/books)** — Beschreibungen, Kategorien.
- **Web-Suche/-Fetch** — Ton, Themen, Rezensionen, und bei Hörbüchern Sprecher/Hördauer.

Details & Endpoints: `.claude/skills/book-deep-analysis/references/metadata-sources.md`.

## Scoring in Kürze

Jede Empfehlung wird pro Dimension (Genre, Themen, Ton, Erzählstil, Tempo, Komplexität,
Figuren, Setting) mit 0–100 bewertet. Der **Gesamt-Match %** ist die mit deinen
persönlichen Gewichten (`gewicht_*` in `vault/Profil.md`) gewichtete Summe. Bestätigt
wird nur, was ≥ 65 % erreicht, kein No-Go verletzt und in keiner dir wichtigen Dimension
durchfällt.

---

Das Profil wächst mit jeder Analyse — je mehr Titel du einbringst, desto schärfer die
Empfehlungen.
