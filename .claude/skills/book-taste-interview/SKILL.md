---
name: book-taste-interview
description: >
  Strukturiertes Geschmacks-Interview für Buch-/Hörbuch-Empfehlungen. Nutze diesen Skill,
  wenn der Nutzer einen oder mehrere Titel nennt, die er mochte (oder nicht mochte), und
  bevor eine Empfehlung erstellt wird. Zweck: herausfinden, WAS genau am Titel gefiel –
  nicht nur DASS er gefiel. Ergebnis fließt in die Buch-DNA und das Geschmacksprofil.
---

# Geschmacks-Interview

Ziel: Die genannten Titel sind nur der Startpunkt. Du musst herausfinden, **was** der
Nutzer daran mochte, um seinen wahren Geschmack zu erfassen. Zwei Leute lieben dasselbe
Buch aus komplett verschiedenen Gründen – der Grund entscheidet über gute Empfehlungen.

## Ablauf

> ⭐ **Bewertungseinheit ist das WERK** (Reihe/Universum als Ganzes): Der Nutzer
> bewertet Reihen komplett, nicht Band für Band. NIE bandweise abfragen ("wie fandest
> du Band 3?"). Erfasst wird das Gesamterlebnis + Lesestand; Band-Abweichungen nur,
> wenn er sie von sich aus nennt.

1. **Werk & Verdikt erfassen.** Für jedes genannte Werk: Buch oder Hörbuch? Geliebt,
   okay, oder abgelehnt? Autor/Sprecher, falls bekannt; Lesestand (wie weit?).

2. **Gezielt nachfragen** – nicht mit allen Fragen auf einmal erschlagen. Stelle 3–5
   fokussierte Fragen pro Titel/Runde, hake bei interessanten Antworten nach. Decke über
   die Runden diese Dimensionen ab:

   - **Emotion/Sog:** Was hat es mit dir gemacht? Beklemmung, Trost, Nervenkitzel, Staunen?
   - **Genre/Ton:** Mochtest du eher die düstere/leichte/humorvolle Färbung?
   - **Figuren:** Welche Figur ist hängen geblieben und warum? Antihelden? Weichzeichner?
   - **Handlung vs. Charaktere:** Ging es dir mehr um Plot-Twists oder um Innenleben?
   - **Erzählweise:** Ich-Erzähler? Mehrere Perspektiven? Unzuverlässig? Sprache/Stil?
   - **Tempo:** Slow-burn, der sich aufbaut, oder direkt Vollgas?
   - **Setting/Welt:** Hat dich die Welt gepackt oder war sie nur Kulisse?
   - **Konkrete Szene:** Gibt es eine Szene/Stelle, die du nie vergessen hast? (sehr aufschlussreich)
   - **Was hat gestört?** Auch beim Lieblingsbuch – wo hast du die Augen gerollt? Wie
     schlimm war es (hat genervt vs. fast verdorben)? → wird zur Aspekt-Wertung −1/−2.
   - **Kontext-Kontraste:** Gilt das auch in anderen Genres? ("Slow-burn liebst du in
     Fantasy – auch im Thriller?") → füllt `status_kontexte` der Merkmale.

3. **Bei Hörbüchern zusätzlich:**
   - Sprecher-Performance: Solo-Sprecher oder voller Cast? Stimme, Tempo, Betonung?
   - Hätte das Buch dir gedruckt genauso gefallen, oder machte es der Sprecher aus?
   - Länge/Format: gerne lang (>20 h) oder kompakt? Nebenbei-Hören oder volle Aufmerksamkeit?

4. **No-Gos abklären:** Gibt es Dinge, die dir ein Buch sofort verderben? (z. B. bestimmte
   Inhalte, Cliffhanger ohne Auflösung, bestimmte Erzählweisen).

5. **Format- & Sprachpräferenz:** Sollen Empfehlungen als Buch, Hörbuch oder beides sein?
   Deutsch, Englisch, egal?

## Gute-Fragen-Prinzipien

- **Warum-Fragen schlagen Was-Fragen.** "Was mochtest du?" → "Warum ist dir gerade *das*
  im Gedächtnis geblieben?"
- **Kontraste nutzen:** "Du mochtest A, aber nicht B – was ist der Unterschied für dich?"
- **Vage Antworten konkretisieren:** "spannend" → "spannend durch Rätsel, durch Gefahr,
  oder durch zwischenmenschliche Anspannung?"
- **Widersprüche auflösen = Split-Chance:** Bewertet der Nutzer dasselbe Merkmal mal
  positiv, mal negativ → herausarbeiten, worin der Unterschied liegt ("melancholisch
  mochtest du bei A, bei B nervte es — war A eher elegisch und B deprimierend?").
  Das liefert die Varianten für einen Merkmal-Split (Konventionen → Split-Regeln).
- **Bedingungen aufdecken:** "Magst du X immer, oder nur zusammen mit Y?" → wird zur
  Kombinationsregel in der Kontext-Notiz.
- **Nicht therapieren, sondern kalibrieren.** 2–4 Runden reichen meist.

## Persistieren: jede Runde eine Interview-Notiz

Schreibe die Runde als `vault/Profil/Interviews/<Datum> <Anlass>.md` (Template
`vault/_System/Templates/Interview.md`): Fragen & Antworten möglichst wörtlich,
Schlüssel-Zitate, Tabelle "Erkenntnis → eingeflossen in [[…]]". Diese Notizen sind die
**Provenienz** — jede spätere Profil-/Gewichts-/Merkmal-Aussage muss auf eine
Interview-Notiz zurückzeigen. Erwähnt der Nutzer nebenbei weitere Titel ("X fand ich
auch gut", "Y habe ich abgebrochen"), lege sofort Kandidaten-Notizen mit
`status: erwaehnt` an (Gedächtnis-Regel).

## Übergabe an die Analyse

Wörtliche Zitate des Nutzers sind Gold – sie zeigen, welche Sprache/Kategorien er selbst
nutzt. Übergib an **book-deep-analysis**, das diese Interview-Signale mit objektiven
Metadaten zur Buch-DNA verschmilzt und den Vault aktualisiert.

Wenn `vault/Profil/Profil.md` schon gefüllt ist: gleiche die neuen Antworten damit ab und weise
auf Muster oder Widersprüche hin ("Du sagst düster, aber deine Top-3 sind eher hoffnungsvoll –
was stimmt?").
