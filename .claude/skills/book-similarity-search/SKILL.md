---
name: book-similarity-search
description: >
  Zweistufige Suche nach ähnlichen Büchern/Hörbüchern auf Basis der Buch-DNA und des
  Geschmacksprofils. Nutze diesen Skill, wenn der Nutzer Empfehlungen will ("suche
  ähnliche zu X", "was soll ich als Nächstes lesen/hören"). Stufe 1: grobes Sieben – passt
  ein Kandidat überhaupt in den Rahmen? Stufe 2: tiefe Verifikation – jeder Kandidat wird
  gegen die Dimensionen geprüft und bestätigt ODER verworfen. Prüft ZUERST das
  Kandidaten-Gedächtnis im Vault (Verworfenes nie erneut vorschlagen, Bekanntes nie
  doppelt recherchieren) und schreibt für JEDEN berührten Titel eine Kandidaten-Notiz.
  Liefert immer mindestens 3 verifizierte Vorschläge mit Match-Score je Dimension.
  Kann den book-scout Agent zur Kandidatenfindung fan-outen.
---

# Ähnlichkeitssuche (grob → tief)

Ziel: **verifizierte** Empfehlungen, nicht plausibel klingende Listen. Jeder Vorschlag
muss zwei Siebe passieren. Was durchfällt, wird verworfen – nicht durchgewunken.

## Voraussetzung: "Kenne deine Daten"
Bevor du startest, MUSS vorliegen:
- **Der Kontext der Suche** (Geschmacksraum, z. B. Fantasy — aus Referenztitel/Anfrage):
  `vault/Profil/Kontexte/<Raum>.md` liefert die geltenden **Gewichte & Präferenzen**;
  Fallback `vault/Profil/Gewichte.md`. Dazu `Profil.md` (Übergreifendes) + `No-Gos.md`
  (global + `kontext_no_gos` der Kontext-Notiz).
- Die Referenztitel mit ihren **Aspekt-Bewertungen** (`vault/Bibliothek/Bücher/`,
  Tabelle "Bewertung je Aspekt") — auch die NEGATIVEN Zeilen geliebter Bücher!
- Relevante Merkmal-Notizen unter `vault/Merkmale/` (Status IM KONTEXT via
  `status_kontexte`; Kontext schlägt global).
- **Das Gedächtnis:** `vault/Empfehlungen/Kandidaten/` — Frontmatter aller Notizen
  sichten. `geprueft-verworfen` nie erneut vorschlagen — AUSSER der
  `wiedervorlage:`-Trigger greift (die zugrunde liegende Präferenz hat sich geändert)
  oder der Nutzer bittet um Neubewertung; dann regulär neu durch Stufe 2, mit neuer
  Historie-Zeile. Für Bekanntes vorhandene Metadaten/Prognosen wiederverwenden.
Fehlt die DNA eines genannten Referenztitels → erst `book-deep-analysis` dafür laufen lassen.

Kläre außerdem: **Format** (Buch/Hörbuch/beides), **Sprache**, gewünschte **Anzahl**
(Default ≥3), und ob es eng am Referenztitel oder breiter am Gesamtprofil orientiert sein soll.

## Stufe 1 — Grobes Sieben (Rahmen)

Erzeuge einen **breiten Kandidatenpool** (10–25 Titel). Quellen kombinieren:
- Open-Library-`subjects` der Referenztitel als Sucheinstieg (gleiche Subjects/Autoren-Umfeld).
- Web-Suche "Bücher wie X", "if you liked X", Genre-/Themenlisten, Award-Listen.
- Bei Hörbüchern zusätzlich nach Format/Sprecher-Ökosystem suchen.
- Für Breite/Parallelität optional den **book-scout** Agent fan-outen (siehe unten).

Zusätzliche billige Quellen aus dem Vault: Autoren-Notizen ("Weitere Werke"),
Sprecher-Notizen ("Weitere Einlesungen"), Reihen-Notizen (nächster Band!), sowie
Backlinks der loved-Merkmal-Notizen.

**Grobfilter (schnell, nur Rahmen):** Ein Kandidat bleibt drin, wenn er grob passt bei:
Genre-Nähe, Sprache/Verfügbarkeit im gewünschten Format, kein hartes **No-Go** aus dem
Profil, ungefähr passende Länge/Ton. Zu weit weg → sofort raus. Ziel: 8–15 plausible Kandidaten.

**📝 Gedächtnis-Pflicht Stufe 1:** JEDER gesichtete Titel — auch die sofort
Aussortierten — bekommt eine Notiz `vault/Empfehlungen/Kandidaten/<Titel>.md`
(Template `Kandidat.md`) mit `kontext:`, `status: gesichtet`, allen gefundenen
Metadaten UND einer neuen Zeile in der **Prüf-Historie** (append-only: Datum, Lauf,
Stufe, Status, Grund). Bestehende Notizen: nur Frontmatter-Spiegel + neue
Historie-Zeile — nie alte Einträge überschreiben, Wissen bleibt.

> Sei hier tolerant: Stufe 1 soll nicht perfekt sein, nur den offensichtlichen Müll
> aussieben. Die echte Entscheidung fällt in Stufe 2.

## Stufe 2 — Tiefe Verifikation (bestätigen oder verwerfen)

Für **jeden** übrig gebliebenen Kandidaten:
1. **Metadaten holen** (wie in `book-deep-analysis`, Kurzform): Genre, Themen, Ton,
   Erzählstil, Tempo, Setting, Länge; bei Hörbuch Sprecher/Dauer. Quellen notieren.
2. **Prognose je Aspekt, dann Dimension scoren** (0–100 je Dimension) — im KONTEXT:
   a) Baue die **Prognose-Tabelle** der Kandidaten-Notiz: je relevantem Merkmal die
      erwartete Nutzer-Wertung (−2..+2) MIT Beleg (Rezensionszitat + Quelle), abgeglichen
      mit den Aspekt-Bewertungen der Referenzbücher ("Nutzer strafte [[Aufgeblähter
      Mittelteil]] bei X mit −1 ab; 3 Rezensionen nennen Längen → erwartet −1").
   b) Aggregiere die Aspekt-Prognosen zur Dimensions-Punktzahl. Merkmal-Status gilt
      IM Kontext (`status_kontexte`), nicht global:
   - 90–100 = trifft loved-Merkmale des Kontexts genau, keine negativen Prognosen.
   - 60–89 = passt gut, kleine Abweichung.
   - 30–59 = neutral/teils, oder positive und negative Prognosen mischen sich.
   - 0–29 = widerspricht dem Geschmack im Kontext.
   - disliked-Merkmal/No-Go (global ODER Kontext) → harte Abwertung, ggf. Ausschluss.
   - `handwerk` als eigene Dimension scoren, wenn der Kontext sie gewichtet.
3. **Gesamt-Match-% berechnen** = gewichtete Summe der Dimensions-Scores mit den
   Gewichten des **Kontexts** (`gewichte:` der Kontext-Notiz; Fallback
   `vault/Profil/Gewichte.md`). Formel:
   `match = Σ(score_dim × weight_dim) / Σ(weight_dim)`  (nur berücksichtigte Dimensionen).
4. **Verdikt:**
   - **Bestätigt** wenn Gesamt-Match ≥ 65 UND kein No-Go verletzt UND keine für den
     Nutzer *kritische* Dimension (hohes Gewicht) unter ~40 liegt.
   - Sonst **verworfen** – mit Grund (welche Dimension warum durchfiel).

**📝 Gedächtnis-Pflicht Stufe 2:** Kandidaten-Notiz jedes tief geprüften Titels
aktualisieren: Prognose-Tabelle (je Aspekt, mit Belegen), neue **Historie-Zeile**
(append-only), `status` + `overall` + `scores` als Frontmatter-Spiegel des jüngsten
Stands, Verdikt-Begründung ✓/✗, alle Rohdaten/Quellen in "Notizen & Rohdaten".
**Bei Verwerfen an EINER Präferenz** (z. B. nur Tempo): `wiedervorlage:` setzen
("neu prüfen, falls Tempo-Präferenz sich lockert"). DNA-Merkmale als `[[Links]]` —
so tauchen Kandidaten in den Backlinks der Merkmal-Notizen auf.

Sei in Stufe 2 **streng**: lieber einen plausibel klingenden Titel verwerfen, als den
Nutzer mit einem enttäuschenden Vorschlag zu verlieren.

## Mindestmenge absichern
Ziel sind **≥3 bestätigte** Vorschläge (oder die vom Nutzer geforderte Anzahl).
- Bleiben nach Stufe 2 weniger als 3 übrig → **zurück zu Stufe 1**, Pool erweitern
  (andere Subjects, benachbarte Autoren, andere Suchwinkel), erneut verifizieren.
- Niemals die Mindestmenge erreichen, indem du die Schwelle senkst oder Schwaches
  durchwinkst. Lieber transparent: "3 starke gefunden; ein 4. mit Einschränkungen."
- Sortiere bestätigte Kandidaten nach Gesamt-Match absteigend.

## Ergebnis persistieren (Vault)
Schreibe die Lauf-Notiz `vault/Empfehlungen/Läufe/<JJJJ-MM-TT> <Thema>.md`
(Template `vault/_System/Templates/Lauf.md`):
- Frontmatter: Datum, Anfrage, Referenzen als `[[Wikilinks]]`, Format, benutzte
  Gewichte, Poolgrößen (Stufe 1 / Stufe 2).
- Tabellen: Empfohlen (mit Match-%), tief geprüft & verworfen (mit Grund), nur
  gesichtet — alles als Links auf die Kandidaten-Notizen (dort liegen die Details).
- Kommt eine Empfehlung auf die Leseliste des Nutzers → `vault/Empfehlungen/Warteliste.md`
  ergänzen und Kandidaten-Status auf `warteliste`.
- `vault/Home.md` → "Zuletzt" ergänzen.

Die Historie bleibt so im Vault erhalten. Danach **book-reco-artifact** (Phase 4)
aufrufen: es überschreibt das feste Artefakt „Empfehlungen" mit diesem neuesten Lauf
(gleiche URL, nie ein neues Artefakt).

## Optional: Fan-out mit dem book-scout Agent
Für breite oder parallele Recherche kann der **book-scout** Agent mehrfach gestartet
werden (je ein Suchwinkel: nach Subjects / nach Themen / nach Autoren-Umfeld / Award-Listen).
**Gib ihm die Liste bereits bekannter Titel mit** (aus `Empfehlungen/Kandidaten/` +
Bibliothek), damit er sie überspringt. Er liefert je einen strukturierten
Kandidaten-Batch zurück. Danach dedupliziert du, schreibst die Kandidaten-Notizen
(Gedächtnis-Pflicht!) und führst Stufe 2 zentral durch. Nutze das bei
"gründlich"/"viele Optionen"; für schnelle Anfragen reicht die Inline-Suche.
