# Bereinigung Fakten/Erleben — Arbeitsanweisung (Phase 3, 2026-10-11)

Gilt für jedes Werkpaar nach der abschnittsweisen Trennung vom 2026-10-11.
Musterwerk: **Survival Quest** — vor dem Start lesen:
`vault/Werke/Buecher/Survival Quest.md`, `vault/Personen/Lucas/Erlebnisse/Survival Quest – Lucas.md`,
`scripts/umbau/protokoll/Survival Quest.md`. Vorlagen: `vault/_System/Templates/Werk.md`,
`vault/_System/Templates/Erlebnis.md`. Regeln: `vault/_System/Konventionen.md` (v2).

## Die Prüffrage

Für jede Zeile der Fakten-Notiz (F): **Wäre sie für eine andere Person genauso wahr?**
Nein → sie gehört in die Erlebnis-Notiz (E). Für jede Zeile in E: Ist sie reiner Fakt ohne
Bezug zu Lucas? → nach F.

## Was in F nicht stehen darf

- Lesestand (auch als Tabellenspalte „Lesestand“/„mein Stand“/„Status“), Verdikt, Kontext
  (`**Kontext:**` → in F `**Genre:**`), Format/Sprache „vom Nutzer gehört/gelesen“
- No-Go-Prüfungen („Reihen-Pflicht erfüllt“, „unter der 20-h-Grenze des Nutzers“)
- Wertungs-Vorzeichen (+), (−), (+2), „verletzt“, „deckt mein Empfinden/meine Kritik“
- Zitate, Urteile, Wünsche, Fragen an Lucas, Interview-Verweise (`Quelle Interview:` → E)
- **DNA ohne Beleg:** Ein Merkmal in der Fakten-DNA (Frontmatter `themen/ton/erzaehlstil/
  figuren/setting/handwerk`, `tempo`, `komplexitaet` und Abschnitt „DNA“) bleibt nur, wenn
  die Community-Rezensionen/Recherche **in F** es belegen — dann Quelle in Klammern dazu.
  Sonst raus aus F. Steht das Merkmal als Wertung in E (`bewertung:`/Tabelle), geht nichts
  verloren. Steht es dort NICHT, als „**Offen (DNA-Beleg):** …“ wörtlich unter F „Offene
  Fragen“ aufnehmen.
- Ein Merkmal, das laut Lucas' Wertung gerade **fehlt** („fehlt hier“, „verletzt“), darf nie
  als Eigenschaft in F stehen.

### Was als Beleg zählt (einheitlich festgelegt nach Runde 1, 2026-10-11)

| zählt | zählt nicht |
| --- | --- |
| Stelle in den Community-/Recherche-Abschnitten von F, die das Merkmal **inhaltlich direkt** aussagt — wörtliches Zitat oder als Community-Konsens gekennzeichnete Zusammenfassung („wiederkehrend: …“) | Kritik, die etwas anderes aussagt (z. B. „wenige lange Actionszenen“ für Eskalations-Setpieces) |
| **Einzelstimme**, wenn wörtlich zitiert — dann „(Einzelstimme)“ dazuschreiben | Zielgruppen-Vergleiche („für Nerds, was Ready Player One für Gamer ist“) |
| Genre-/Titel-/Prämissen-Angabe, **wenn sie das Merkmal selbst ausspricht** (Genre „Cosy Crime“ → Cosy-Wohlfühlatmosphäre; Prämisse „rechtmäßiger Erbe“ → Verlorenes Erbe) | Ableitungen, die mehr behaupten als die Quelle (Prämisse nennt den Erben, aber nicht als Hauptfigur) |
| | Formulierungen aus Lucas' Interview, auch wenn sie neutral klingen („Heist-Struktur“, „Sog-Phasen“) |

Reicht der Beleg nicht → **„Offen (DNA-Beleg):“** in F „Offene Fragen“, nicht still löschen.
Beleg in Klammern immer angeben: `(Community: „…“)`, `(Einzelstimme: „…“)`, `(Genre)`, `(Prämisse)`.

Fakten nie an Lucas delegieren: „Wer liest Bd. 3?“ ist eine Recherche-Lücke in F, keine Frage an ihn.

## Was in E nicht stehen soll

- Reine Community-Zahlen/-Befunde, Produktionsdaten, Gesamt-Hördauern, „Objektiv
  (Rezensionskonsens)…“ → nach F (DNA bzw. Community-Abschnitte). In E bleibt nur der
  **Abgleich** („deckt sich mit meinem …“), Zahlen höchstens als Bezug im Satz.
- Hördauern in der Lesestand-Tabelle → nur „gehört (dt.)“; Dauern stehen in F.

## Harte Regeln

1. **Nichts verlieren.** Jede Information steht danach in F oder E. Wörtlich verschieben,
   wo es geht. Löschen nur, wenn dieselbe Information nachweislich schon dasteht — im
   Protokoll die Fundstelle nennen.
2. **Nie raten, nie Gefühle zuschreiben.** Eine Aussage über Lucas' Empfinden, die weder in
   E belegt noch im verlinkten Interview (`vault/Profil/Interviews/`) steht → nicht
   behaupten, sondern als Frage unter „## Offene Fragen an Lucas“ in E.
3. **Widersprüche nicht glätten.** Zwei verschiedene Zahlen/Daten → beide stehen lassen
   und unter „Offene Fragen“ (F für Fakten, E für Fragen an Lucas) vermerken. Nur
   auflösen, wenn die Notiz selbst die Bestätigung enthält (wie bei Survival Quest
   `letztes_datum`).
4. **Spoiler-Felder** (`spoiler_*`) inhaltlich nicht ändern. Spoiler-Callouts
   (`> [!warning]- 🔒 SPOILER`) unverändert mitnehmen.
5. **Nur die eigenen Dateien anfassen:** die F- und E-Notiz der zugewiesenen Werke und
   `scripts/umbau/protokoll/<Werk>.md`. Keine anderen Notizen, keine Umbenennungen,
   keine neuen Notizen, keine Links auf nicht existierende Notizen. Nicht committen.
6. **Verweise reparieren:** „s. u.“, „siehe Bewertung“, „(siehe Offene Fragen)“ usw., deren
   Ziel jetzt in der anderen Notiz liegt → auf `[[Werk]]` bzw. `[[Werk – Lucas]]`
   umbiegen. „geerbt aus [[Universum]]“ / „Eingebracht von [[Reihe]]“ zeigen auf
   **Wertungen** → `[[Universum – Lucas]]` / `[[Reihe – Lucas]]`.

## Struktur nach der Bereinigung (wie Musterwerk)

- **F:** H1, Erleben-Link (`> 👤 …`), Kurzbeschreibung, `**Genre:** … · **Autor:** … ·
  **Sprecher (dt.):** …`, Universum, Bände (Tabelle ohne Lesestand-Spalte), ggf.
  `**Hördauer gesamt (dt.):**`, Community lobt/kritisiert, „### Auffällige
  Band-Unterschiede (Community)“ falls vorhanden, Metadaten, Releases, DNA (mit Hinweis
  „Nur belegte Merkmale …“), „## 🧮 Community-Gesamtbild“, Offene Fragen (nur
  Recherche-Lücken).
- **E:** Frontmatter mit `besitz: ""` und `status:` (nur `durch`, wenn der Lesestand alle
  erschienenen Bände als erlebt zeigt; `laeuft`, wenn ein Band läuft; `abgebrochen` nur,
  wenn ausdrücklich so notiert; sonst leer + Kommentar), `tags: [erlebnis, <format>,
  <verdict>]` (Genre-Tags → F-Tags). Body: H1, Einleitungssatz, `**Kontext:** [[…]] ·
  **Quellen:** [[Interview …]]`, persönliches Blockzitat, Lesestand, Bewertung je Aspekt,
  Abweichungen, „## Band-Unterschiede: Community-Kurve vs. mein Empfinden“ (H2, nicht H3
  vor dem ersten H2), DNA-Begründung, Hörbuch-Erlebnis, Reihen-Gesamtbild,
  „## Offene Fragen an Lucas“ (mindestens Besitz).
- `bewertung:` in E muss mit der Bewertungstabelle übereinstimmen (gleiche Aspekte, gleiche
  Werte). Abweichungen → nicht raten, unter Offene Fragen vermerken.
- F-Tags: `[werk, buch, <werk_typ>, <genre-tags>]`.

## Protokoll `scripts/umbau/protokoll/<Werk>.md`

Format wie im Musterwerk: Tabelle `| alt | Inhalt (gekürzt) | Verbleib | Grund |`. Erste
Spalte **immer** mit Zeilennummern des Ausgangsstands, z. B. `F 58–59`, `E 27`. Jede alte
Zeile, die nicht mehr wörtlich vorkommt, muss abgedeckt sein. Danach Abschnitt „Neu
hinzugekommen“.

## Nachweis (Pflicht, bevor du fertig meldest)

```bash
. scripts/python-finden.sh
$PY scripts/umbau/verbleib_pruefen.py "<Werk>" <Ausgangs-Commit>   # muss ✅ zeigen
$PY scripts/vault_pruefen.py                                       # muss bestanden sein
$PY scripts/spoiler_check.py --quiet --herkunft vault "<F-Pfad>" "<E-Pfad>"   # rc 0
$PY scripts/spoiler_check.py --grenzen                             # Stufe des Werks unverändert
```
