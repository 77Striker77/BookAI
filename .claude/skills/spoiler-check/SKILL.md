---
name: spoiler-check
description: >
  Prüft eine Ausgabe auf Spoiler und hält sie spoilerfrei — für alles, was der Nutzer noch
  nicht gelesen/gehört hat. Nutze diesen Skill, BEVOR ein Artefakt publiziert, eine
  Empfehlung oder Analyse ausgegeben oder eine Werk-Notiz geschrieben wird; außerdem, wenn
  der Nutzer den Lesestand ändert ("bin jetzt bei Band 3", "hab Teil 2 durch", "hab X
  angefangen/abgebrochen") oder fragt, ob etwas spoilert. Führt den deterministischen
  Linter und den semantischen Agenten 'spoiler-guard' zusammen und pflegt die bandgenauen
  Grenzen im Vault.
---

# spoiler-check — Ausgaben spoilerfrei halten

Verbindliche Regeln: **`vault/_System/Spoiler-Politik.md`** (der Vault ist die Wahrheit,
auch für die Spoiler-Regeln). Dieser Skill führt sie aus, er erfindet sie nicht.

## Der Kerngedanke in drei Sätzen

1. Was der Nutzer **erlebt** hat, darf **detailliert** besprochen werden — ausdrücklich mehr
   als bisher.
2. Was er **nicht** erlebt hat, existiert in Ausgaben nur als **Neutralzone**: Metadaten,
   Prämisse von Bd. 1, Ton/Tempo, Wertungen, Handwerksurteile ohne Inhalt.
3. **Fail-closed:** unklar = nicht erlebt. Und **nie glätten** — Zurückgehaltenes wird als
   „🔒 Details zu Bd. X+ zurückgehalten" sichtbar gemacht.

Die Politik beschneidet **nur Handlung, nie Daten**. Das oberste Projektziel (maximale
Datendichte je Werk) bleibt unangetastet.

## A) Prüfen, bevor etwas rausgeht

```bash
python3 scripts/spoiler_check.py --grenzen           # wie weit bin ich in welchem Werk?
bash scripts/spoiler-gate.sh                         # Artefakte + Vault, deterministisch
python3 scripts/spoiler_check.py artifacts/empfehlungen.html   # gezielt
python3 scripts/spoiler_check.py --stdin --herkunft chat < entwurf.md
```

Danach **immer** den Agenten `spoiler-guard` auf denselben Text ansetzen. Beide Hälften
sind Pflicht:

| | fängt | ist blind für |
| --- | --- | --- |
| Linter (deterministisch) | Signalwörter, Bandbezüge, Sperrbegriffe | Paraphrasen, Andeutungen, Implikationen |
| `spoiler-guard` (semantisch) | Umschreibungen, Auslassungen, Vergleichs-Lecks | nichts systematisch — aber er ist nicht beweisbar vollständig |

Das ist kein Doppelaufwand, sondern der Kern des Entwurfs: Automatische Spoiler-Erkennung
liegt in der Forschung bei ~75–80 % Trefferquote (SpoilerNet, UCSD/Goodreads, ACL 2019).
Als **einziges** Gate wäre das viel zu schwach — deshalb harte Regeln + Urteil + Hooks.

**Urteil `blockieren` oder ein `VERSTOSS` → nicht publizieren.** Erst bereinigen.

## B) Bereinigen — was womit ersetzt wird

| Statt | Schreib |
| --- | --- |
| „In Bd. 6 verrät ⟨Figur⟩ die Gruppe." | „🔒 Handlungsdetails ab Bd. 6 zurückgehalten (dein Stand: Bd. 5)." |
| „Am Ende löst sich alles auf." | „Die Reihe ist abgeschlossen (6 Bände, ⌀ 4,5 · 120k Wertungen)." |
| „⟨Figur⟩ kommt später nicht mehr vor." | *(ersatzlos — schon die Aussage ist der Spoiler)* |
| Klappentext von Bd. 6 | Klappentext von Bd. 1 (bzw. des ersten ungelesenen Bandes) |

Metadaten dabei **nie** anfassen. Wer beim Bereinigen Zahlen verliert, hat es falsch gemacht.

## C) Lesestand ändern (der häufigste Auslöser)

Sagt der Nutzer etwas wie „bin jetzt bei Band 3", „Teil 2 durch", „hab X abgebrochen":

1. Betroffene Werk-Notiz öffnen (`vault/Bibliothek/Werke/⟨Werk⟩.md`).
2. Frontmatter setzen — **der laufende Band zählt NICHT als erlebt**:
   ```yaml
   spoiler_erlebt_bis: 2        # letzter VOLLSTÄNDIG erlebter Band
   spoiler_aktuell: 3           # läuft gerade (0 = keiner)
   spoiler_gesamt: 8            # erschienene Bände
   spoiler_stand: "2026-08-11"
   ```
3. Die Prosa-Tabelle „Lesestand" im Body **gleich mitziehen** (beide müssen übereinstimmen).
4. `python3 scripts/spoiler_check.py --grenzen` zur Kontrolle.
5. **Wichtig:** Grenze verschoben → alte Ausgaben können jetzt zu wenig zeigen. Bei der
   nächsten Artefakt-Erzeugung prüfen, ob bei neu freigegebenen Werken mehr Detail
   nachgetragen werden sollte (Politik §6 — mehr Detail ist erwünscht!).
6. Vault committen (Gedächtnis-Regel), dann erst Artefakte neu erzeugen.

Erscheint ein neuer Band, wächst `spoiler_gesamt` — dadurch rutscht ein `voll`-Werk
automatisch zurück auf `bis_band_N`. Das ist gewollt.

## D) Sperrbegriffe pflegen (bei tiefer Recherche)

Wenn `book-deep-analysis` oder `book-scout` ohnehin spätere Bände sichten und dabei Namen
aufschnappen, die erst dort auftauchen: als **neutrale Begriffe** in
`spoiler_sperrbegriffe` der Werk-Notiz eintragen.

> ⚠️ Die Liste selbst darf kein Spoiler sein: `["Nebelkrone"]` ja — `["Nebelkrone tötet
> ⟨Figur⟩ in Bd. 6"]` nein.

## E) Vault schreiben: der 🔒-Block

Muss eine Notiz etwas jenseits der Grenze festhalten (z. B. eine Rezensionswarnung zu
Bd. 7), kommt es in einen eingeklappten Callout — nie in den Fließtext:

```markdown
> [!warning]- 🔒 SPOILER — ab Bd. 7 (mein Stand: Bd. 5)
> ⟨Inhalt⟩
```

## F) Neutralzone ausweisen (gegen Fehlalarme)

Ist eine Stelle nachweislich Neutralzone (typisch: Klappentext/Prämisse von Bd. 1), wird sie
markiert statt das Lexikon aufzuweichen:

- HTML: `<p data-spoilerfrei="Klappentext Bd. 1">…</p>`
- Markdown: `<!-- spoilerfrei -->` bzw. `<!-- spoilerfrei:start -->` … `<!-- spoilerfrei:end -->`

Audit: `python3 scripts/spoiler_check.py --ausnahmen artifacts/*.html` listet **jede**
Ausnahme auf. Sperrbegriffe gelten trotz Marker weiter.

## G) Wenn der Linter irrt

- **Fehlalarm** → belegtes Muster in `vault/_System/Spoiler-Lexikon.md` unter
  `spoiler-phrasen-whitelist` bzw. `spoiler-titel-whitelist` eintragen.
- **Durchgerutscht** → neues Muster unter `spoiler-hart`/`spoiler-weich` ergänzen.
- **In beiden Fällen Pflicht:** Testfall in `tests/spoiler/faelle/` anlegen (Positiv- UND
  Negativfall) und `bash scripts/spoiler-selftest.sh` grün fahren. Ohne Testfall keine Regel
  — sonst driftet der Linter und wird ignoriert.

## Die Sicherungen laufen automatisch mit

| Hook | wirkt |
| --- | --- |
| `SessionStart` | kippt die Grenzen sofort in den Kontext |
| `PreToolUse` (Artifact/Write/Edit) | **blockt** einen Publish/Schreibvorgang mit Verstoß |
| `Stop` | prüft die Chat-Antwort + Artefakte; Verstoß = Antwort darf nicht stehen bleiben |
| `SubagentStop` | prüft die Rückgabe jedes Subagenten (z. B. `book-scout`) |

Die Hooks sind das Netz, nicht die Methode. Verlass dich nicht darauf, dass sie dich
auffangen — prüfe aktiv, bevor du ausgibst.
