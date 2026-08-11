---
tags: [system, spoiler]
gilt_ab: 2026-08-11
---

# Spoiler-Politik — was darf in einer Ausgabe stehen?

> **Nutzer-Regel (2026-08-11):** „In Artefakten oder Ausgaben dürfen nie Spoiler von
> Dingen sein, die ich noch nicht gelesen oder gehört habe. Wenn ich es habe, dürfen die
> Inhalte gerne etwas detaillierter drinstehen."

Diese Notiz ist die **einzige Quelle** der Spoiler-Regeln (OBERSTE REGEL: Vault gewinnt).
Der Linter `scripts/spoiler_check.py`, der Agent `spoiler-guard` und alle Skills lesen
von hier. Wer die Regeln ändern will, ändert **diese Notiz** — nicht den Code.

## 0. Geltungsbereich — was ist eine „Ausgabe"?

**Alles, was der Nutzer zu sehen bekommt**, ist eine Ausgabe und unterliegt der Politik:

| Ausgabe | Gate |
| --- | --- |
| `artifacts/bibliothek.html`, `artifacts/empfehlungen.html` | **hart** — kein Publish mit Verstoß |
| Chat-Antworten (auch Zwischenstände, Listen, Tabellen) | **hart** |
| Rückgaben von Subagenten (`book-scout` etc.) | **hart** |
| Vault-Notizen (`vault/**`) | **weich** — Details erlaubt, aber nur in einem `🔒 SPOILER`-Block (s. §5) |

Der Vault ist ein **Arbeitsspeicher**, kein Lesestoff — er darf mehr wissen als er zeigt.
Aber auch er versteckt Spoilriges hinter einem eingeklappten Block, weil der Nutzer ihn in
Obsidian öffnet.

## 1. Die Grenze: der Lesestand, bandgenau

Jede Werk-Notiz trägt im Frontmatter die maschinenlesbare Grenze:

```yaml
spoiler_erlebt_bis: 5      # letzter VOLLSTÄNDIG gelesener/gehörter Band (0 = keiner)
spoiler_aktuell: 6         # Band, der GERADE läuft (0 = keiner) — gilt als NICHT erlebt
spoiler_gesamt: 16         # erschienene Bände (Kontrollwert)
spoiler_stand: "2026-08-11"  # wann bestätigt
spoiler_sperrbegriffe: []  # harte Tabu-Begriffe (s. §4)
spoiler_aliase: []         # weitere Schreibweisen des Werktitels
```

**Der laufende Band zählt nicht als erlebt.** Wer bei Bd. 6 auf Minute 3 steht, hat Bd. 6
nicht erlebt. Deshalb ist `spoiler_aktuell` immer jenseits der Grenze.

### Freigabestufen (leiten sich automatisch ab)

| Stufe | Wann | Was erlaubt ist |
| --- | --- | --- |
| **`voll`** | `erlebt_bis` ≥ `gesamt` und nichts läuft | Alles. Details, Wendungen, Figurenschicksale, Enden — der Nutzer kennt sie. |
| **`bis_band_N`** | Teilweise erlebt | Details **nur bis einschließlich Band N**. Alles ab N+1: nur Neutralzone (§2). |
| **`blurb`** | `erlebt_bis` = 0, oder Werk gar nicht in der Bibliothek | **Klappentext-Ebene.** Gilt für JEDEN Empfehlungskandidaten — per Definition ungelesen. |

**Fail-closed:** Fehlt die Angabe, ist sie widersprüchlich oder ist das Werk unbekannt →
`blurb`. Nie „im Zweifel etwas mehr". Im Zweifel weniger.

## 2. Neutralzone — was NIE ein Spoiler ist

Diese Dinge dürfen immer und in voller Detailtiefe raus, für jedes Werk, jeden Band,
auch für nie angefasste Kandidaten. **Das oberste Ziel (maximale Datendichte) bleibt damit
vollständig erfüllt** — die Spoiler-Politik beschneidet Metadaten nicht um ein Byte:

- Titel (DE/EN/Original), Reihen-/Universumszugehörigkeit, Band-Nummern, Reihenfolge
- Alle Erscheinungsdaten (Buch/Hörbuch, DE/EN), ISBN, Seitenzahl, Hördauer, Verlag/Label
- Autor, Übersetzer, Sprecher, Solo/Voll-Cast, ungekürzt
- Wertungen mit Anzahl je Band/Quelle, Bekanntheit, Hype, Verkaufszahlen
- Genre, Ton, Tempo, Komplexität, Erzählperspektive, Setting-Typ
- Ausgangslage/Prämisse **von Band 1** (was auf dem Buchrücken steht)
- Struktur-/Handwerksurteile ohne Inhalt: „Mittelteil zieht", „Tempo zieht ab der Hälfte an",
  „Bd. 7 wird für Leerlauf kritisiert", „starkes Finale" (ohne zu sagen, WAS im Finale passiert)
- Lese-/Hörreihenfolge-Empfehlungen und Abhängigkeiten

**Grenzfall Reihenfolge-Begründung** (Regel aus der Parallel-Session 2026-08-11): **Dass**
ein Band zwei Stränge zusammenführt, ist Reihenfolge-Information und darf stehen — sonst
wäre die Reihenfolge-Regel nicht begründbar. **Wie** das geschieht, bleibt draußen. Im
Zweifel: die Reihenfolge-Wirkung nennen, nicht die Handlung.

## 3. Verbotszone — was jenseits der Grenze NIE raus darf

- Ereignisse, Wendungen, Enthüllungen, Auflösungen (Wer ist der Täter, was ist das Geheimnis)
- Figurenschicksale: Tod, Verrat, Rückkehr, Identität, Beziehung, Fraktionswechsel, Aufstieg
- Wer in späteren Bänden überhaupt noch vorkommt (auch das ist eine Information!)
- Endzustände: „am Ende der Reihe ist X …", Zustand der Welt nach Band N
- Titel/Klappentext **späterer** Bände, soweit sie den Stand verraten. **Klappentext-Regel:**
  Der Klappentext von Band N spoilert Band N−1. Zusammengefasst werden darf höchstens der
  Klappentext des **ersten ungelesenen Bandes** (= `erlebt_bis` + 1), und auch der nur in
  seinem nicht-handlungsverratenden Teil.
- Zitate aus Rezensionen, die Handlung verraten — auch wenn die Quelle sie unmarkiert bringt

## 4. `spoiler_sperrbegriffe` — die harte Tabu-Liste je Werk

Begriffe, die **nur jenseits der Grenze** existieren: Namen von Figuren, Orten, Fraktionen,
Artefakten, die erst später auftauchen. Ihr bloßes Vorkommen in einer Ausgabe ist ein
harter Verstoß — auch ohne Kontext, denn schon der Name verrät („X taucht also später auf").

> ⚠️ **Die Liste selbst darf kein Spoiler sein.** Nur **neutrale Begriffe**, NIE das
> Ereignis dazu. Richtig: `["Gralsritter"]`. Falsch: `["Gralsritter töten Anna in Bd. 6"]`.
> Wer die Liste liest, darf nichts erfahren, was er nicht schon weiß.

Gepflegt wird sie von `book-deep-analysis`, wenn bei der Recherche ohnehin spätere Bände
gesichtet werden. Leer ist ein gültiger Zustand — die generischen Regeln greifen trotzdem.

## 5. Vault-Regel: der `🔒 SPOILER`-Block

Muss eine Werk-Notiz etwas festhalten, das jenseits der Grenze liegt (z. B. eine
Rezensionswarnung zu Bd. 7), kommt es in einen **eingeklappten Obsidian-Callout**:

```markdown
> [!warning]- 🔒 SPOILER — ab Bd. 7 (mein Stand: Bd. 5)
> ⟨Inhalt, der jenseits meiner Grenze liegt⟩
```

Das `-` hinter `[!warning]` klappt den Block in Obsidian **zu**. Der Nutzer entscheidet
selbst, ob er aufklappt. Der Linter verlangt genau das: harte Treffer in `vault/**` müssen
in so einem Block stehen, sonst Warnung.

## 6. Detailtiefe bei erlebten Werken — bewusst MEHR

Umgekehrt gilt die Regel auch nach oben: Was der Nutzer erlebt hat, darf **detaillierter**
beschrieben werden als bisher — konkrete Szenen, Figurenkonstellationen, warum genau ein
Moment traf. Das schärft das Matching. Ein `voll`-Werk (z. B. [[Survival Quest]],
[[Riyria]], [[Scholomance]], [[Alex Verus]]) darf ohne Rücksicht besprochen werden.

## 7. Wenn etwas nicht sagbar ist: markieren statt weglassen

Nie stillschweigend glätten (das verstößt gegen das oberste Ziel). Stattdessen sichtbar
machen, dass da etwas ist:

> „🔒 Details zu Bd. 3+ zurückgehalten (dein Stand: Bd. 2 läuft)."

So bleibt nachvollziehbar, dass Information existiert, ohne sie zu verraten.

## 8. Prüfkette (wer prüft wann)

```
Vault (Wahrheit: Lesestand + Sperrbegriffe)
   └─→ scripts/spoiler_check.py        deterministisch, hart, präzise
         ├─→ Hook PreToolUse  (Artifact/Write/Edit)  → blockt Publish/Schreiben
         ├─→ Hook PostToolUse (Write/Edit)           → meldet zurück
         ├─→ Hook Stop/SubagentStop                  → prüft Chat-Antwort + Artefakte
         └─→ Agent spoiler-guard                     → semantische Prüfung (Paraphrasen)
```

Deterministik fängt das Eindeutige, der Agent das Umschriebene. **Beide sind Pflicht,
bevor ein Artefakt publiziert wird** (`bash scripts/spoiler-gate.sh` macht beides sichtbar).

## 9. Selbsttest

`bash scripts/spoiler-selftest.sh` fährt die Fälle aus `tests/spoiler/faelle/` gegen den
Linter und meldet Treffer/Fehlalarme. Jede neue Regel bekommt dort einen Positiv- UND
einen Negativfall (sonst driftet der Linter in Fehlalarme ab und wird ignoriert).

## Offene Fragen

- `spoiler_sperrbegriffe` sind bei allen Werken noch leer — werden befüllt, sobald
  `book-deep-analysis` das nächste Mal spätere Bände sichtet.
- Bei [[Magic 2.0]] ist der Abbruch (Bd. 5–6 bewusst ungelesen) dauerhaft: Grenze bleibt
  Bd. 4, außer der Nutzer sagt etwas anderes.
