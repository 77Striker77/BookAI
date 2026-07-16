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
- **Kontext schlägt global.** Je Geschmacksraum (Fantasy, Thriller, …) eigene Gewichte
  und Merkmal-Status — was in einem Genre geliebt wird, kann im anderen stören.
- **Ein Buch ist kein Monolith.** Bewertet wird je Aspekt (−2..+2 mit Beleg); auch die
  Schwächen geliebter Bücher fließen ins Matching ein.
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

vault/                             Datenquelle: Obsidian-Vault, atomar & verlinkt
├── Home.md                        Dashboard/MOC (Einstieg)
├── Profil/
│   ├── Profil.md                  NUR kontextübergreifende Muster
│   ├── Kontexte/                  ⭐ je Geschmacksraum (Fantasy, Thriller, …) eigene
│   │                                Gewichte & Präferenzen — Kontext schlägt global
│   ├── Gewichte.md (Fallback) · No-Gos.md
│   └── Interviews/                je Interviewrunde eine Notiz (Provenienz!)
├── Bibliothek/
│   ├── Bücher/                    ⭐ je Titel: Bewertung JE ASPEKT (−2..+2 + Beleg) —
│   │                                auch geliebte Bücher haben negative Zeilen
│   ├── Autoren/  Reihen/  Sprecher/   je Entität eine Notiz (Kandidatenquellen!)
├── Merkmale/                      DNA-Atome: je Merkmal EINE Notiz, Status JE KONTEXT
│   ├── Genres|Themen|Ton|Erzählstil|Figuren|Setting/
│   └── Handwerk/                  ⭐ Ausführungsqualität: Pacing, Finale, Infodumps …
├── Empfehlungen/
│   ├── Warteliste.md              bestätigt, noch nicht gelesen/gehört
│   ├── Läufe/                     je Empfehlungslauf eine Notiz (Historie)
│   └── Kandidaten/                ⭐ GEDÄCHTNIS: jeder je berührte Titel — Prognose je
│                                     Aspekt (belegt) + append-only Prüf-Historie +
│                                     Wiedervorlage-Trigger
└── _System/                       Konventionen.md + Templates/ (9 Notiztypen)

artifacts/                         die 2 festen HTML-Artefakte (stabile Pfade & URLs)
├── bibliothek.html                📚 Meine Bibliothek (Basis)
└── empfehlungen.html              🎯 Empfehlungen (wird überschrieben)
```

Der `vault/`-Ordner ist ein normaler Obsidian-Vault — direkt in Obsidian öffnen,
stöbern, selbst Notizen ergänzen. Die Links sind die Intelligenz: Backlinks einer
Merkmal-Notiz zeigen alle Bücher/Kandidaten, die es tragen; das Kandidaten-Gedächtnis
verhindert, dass je ein Titel doppelt geprüft oder Verworfenes erneut vorgeschlagen wird.

## Datenquellen

- **[Open Library](https://openlibrary.org/developers/api)** — frei, ohne Key: Genres/
  Subjects, ISBN, Jahr, Seiten, Cover. Primäre Metadatenquelle.
- **[Google Books](https://developers.google.com/books)** — Beschreibungen, Kategorien.
- **Web-Suche/-Fetch** — Ton, Themen, Rezensionen, und bei Hörbüchern Sprecher/Hördauer.

Details & Endpoints: `.claude/skills/book-deep-analysis/references/metadata-sources.md`.

## Scoring in Kürze

Je Kandidat zuerst eine **Prognose je Aspekt** (erwartete Wertung −2..+2 pro Merkmal,
belegt mit Rezensionen/Quellen, abgeglichen mit deinen Aspekt-Bewertungen der
Referenzbücher). Daraus je Dimension (Genre, Themen, Ton, Erzählstil, Tempo,
Komplexität, Figuren, Setting, Handwerk) ein Score 0–100. Der **Gesamt-Match %** ist
die gewichtete Summe mit den Gewichten des jeweiligen **Kontexts**
(`vault/Profil/Kontexte/`, Fallback `Gewichte.md`). Bestätigt wird nur, was ≥ 65 %
erreicht, kein No-Go verletzt und in keiner dir wichtigen Dimension durchfällt.
Jede Prüfung landet append-only in der Historie der Kandidaten-Notiz.

---

Das Profil wächst mit jeder Analyse — je mehr Titel du einbringst, desto schärfer die
Empfehlungen.
