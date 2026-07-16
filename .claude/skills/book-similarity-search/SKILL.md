---
name: book-similarity-search
description: >
  Zweistufige Suche nach ähnlichen Büchern/Hörbüchern auf Basis der Buch-DNA und des
  Geschmacksprofils. Nutze diesen Skill, wenn der Nutzer Empfehlungen will ("suche
  ähnliche zu X", "was soll ich als Nächstes lesen/hören"). Stufe 1: grobes Sieben – passt
  ein Kandidat überhaupt in den Rahmen? Stufe 2: tiefe Verifikation – jeder Kandidat wird
  gegen die Dimensionen geprüft und bestätigt ODER verworfen. Liefert immer mindestens 3
  verifizierte Vorschläge mit Match-Score je Dimension. Kann den book-scout Agent zur
  Kandidatenfindung fan-outen.
---

# Ähnlichkeitssuche (grob → tief)

Ziel: **verifizierte** Empfehlungen, nicht plausibel klingende Listen. Jeder Vorschlag
muss zwei Siebe passieren. Was durchfällt, wird verworfen – nicht durchgewunken.

## Voraussetzung: "Kenne deine Daten"
Bevor du startest, MUSS vorliegen:
- `vault/Profil.md` (Kerndaten + `gewicht_*` im Frontmatter).
- Die Buch-DNA der Referenztitel (`vault/Bücher/<Titel>.md`, Frontmatter).
Fehlt die DNA eines genannten Referenztitels → erst `book-deep-analysis` dafür laufen lassen.

Kläre außerdem: **Format** (Buch/Hörbuch/beides), **Sprache**, gewünschte **Anzahl**
(Default ≥3), und ob es eng am Referenztitel oder breiter am Gesamtprofil orientiert sein soll.

## Stufe 1 — Grobes Sieben (Rahmen)

Erzeuge einen **breiten Kandidatenpool** (10–25 Titel). Quellen kombinieren:
- Open-Library-`subjects` der Referenztitel als Sucheinstieg (gleiche Subjects/Autoren-Umfeld).
- Web-Suche "Bücher wie X", "if you liked X", Genre-/Themenlisten, Award-Listen.
- Bei Hörbüchern zusätzlich nach Format/Sprecher-Ökosystem suchen.
- Für Breite/Parallelität optional den **book-scout** Agent fan-outen (siehe unten).

**Grobfilter (schnell, nur Rahmen):** Ein Kandidat bleibt drin, wenn er grob passt bei:
Genre-Nähe, Sprache/Verfügbarkeit im gewünschten Format, kein hartes **No-Go** aus dem
Profil, ungefähr passende Länge/Ton. Zu weit weg → sofort raus. Ziel: 8–15 plausible Kandidaten.

> Sei hier tolerant: Stufe 1 soll nicht perfekt sein, nur den offensichtlichen Müll
> aussieben. Die echte Entscheidung fällt in Stufe 2.

## Stufe 2 — Tiefe Verifikation (bestätigen oder verwerfen)

Für **jeden** übrig gebliebenen Kandidaten:
1. **Metadaten holen** (wie in `book-deep-analysis`, Kurzform): Genre, Themen, Ton,
   Erzählstil, Tempo, Setting, Länge; bei Hörbuch Sprecher/Dauer. Quellen notieren.
2. **Dimension für Dimension gegen das Profil scoren** (0–100 je Dimension):
   - 90–100 = trifft ein `loved`-Merkmal des Nutzers genau.
   - 60–89 = passt gut, kleine Abweichung.
   - 30–59 = neutral/teils.
   - 0–29 = widerspricht dem Geschmack.
   - Trifft ein `disliked`/No-Go → harte Abwertung, ggf. Ausschluss.
3. **Gesamt-Match-% berechnen** = gewichtete Summe der Dimensions-Scores mit den
   `gewicht_*`-Werten aus `vault/Profil.md`. Formel:
   `match = Σ(score_dim × weight_dim) / Σ(weight_dim)`  (nur berücksichtigte Dimensionen).
4. **Verdikt:**
   - **Bestätigt** wenn Gesamt-Match ≥ 65 UND kein No-Go verletzt UND keine für den
     Nutzer *kritische* Dimension (hohes Gewicht) unter ~40 liegt.
   - Sonst **verworfen** – mit Grund (welche Dimension warum durchfiel). Verworfene kurz
     festhalten (nützlich fürs Artefakt "warum nicht andere").

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
Schreibe eine neue Lauf-Notiz `vault/Empfehlungen/<JJJJ-MM-TT> <Thema>.md` — Kopie von
`vault/Empfehlungen/_TEMPLATE.md`:
- Frontmatter: Datum, Anfrage, Referenzen als `[[Wikilinks]]`, Format, benutzte Gewichte.
- Je bestätigter Empfehlung: YAML-Block mit allen Metadaten + `overall` + `scores` je
  Dimension, darunter Klartext **✓ Was passt** / **✗ Was passt nicht**, Quellen.
- Tabelle der **verworfenen** Kandidaten mit Grund (Dimension + Score).
- Notizen zum Lauf (Suchwinkel, Poolgrößen, Lücken).

Die Historie bleibt so im Vault erhalten. Danach **book-reco-artifact** (Phase 4)
aufrufen: es überschreibt das feste Artefakt „Empfehlungen" mit diesem neuesten Lauf
(gleiche URL, nie ein neues Artefakt).

## Optional: Fan-out mit dem book-scout Agent
Für breite oder parallele Recherche kann der **book-scout** Agent mehrfach gestartet
werden (je ein Suchwinkel: nach Subjects / nach Themen / nach Autoren-Umfeld / Award-Listen).
Er liefert je einen strukturierten Kandidaten-Batch zurück. Danach dedupliziert du und
führst Stufe 2 (Verifikation) zentral durch. Nutze das bei "gründlich"/"viele Optionen";
für schnelle Anfragen reicht die Inline-Suche.
