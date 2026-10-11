# Bereinigung Der Prinz von Staub und Schatten — Protokoll (2026-10-11)

Zeile-für-Zeile-Bereinigung nach `scripts/umbau/BEREINIGUNG.md`, Musterwerk Survival Quest.
F = `vault/Werke/Buecher/Der Prinz von Staub und Schatten.md`, E = `vault/Personen/Lucas/Erlebnisse/Der Prinz von Staub und Schatten – Lucas.md`.
Zeilennummern = Stand **vor** der Bereinigung (Commit 4b3270a). Verbund: [[Die Streitenden Götter]].

Prüffrage je Zeile: *Wäre sie für eine andere Person genauso wahr?* Fakten-DNA nur mit Beleg
aus den Community-Rezensionen/der Recherche in F.

Jede alte Zeile, die nicht mehr wörtlich vorkommt, steht hier mit ihrem Verbleib. Alle
übrigen Zeilen sind unverändert in derselben Notiz (wörtlich verschobene zusätzlich gelistet).

| alt | Inhalt (gekürzt) | Verbleib | Grund |
| --- | --- | --- | --- |
| F 24 | `themen` + Rätselhafte Herkunft | F: ohne Rätselhafte Herkunft (übrige drei durch die Prämisse F 50–54 belegt) · E `bewertung` +2 | Prämisse belegt Exil/Erbe/Verfolgung/„rätselhafte Gabe“, aber keine rätselhafte Herkunft — nur Interview |
| F 25 | `ton: [Geheimnisvoll-mysteriöse Aura]` | F: `[]` · E `bewertung` +2 und DNA-Begründung | nur Interview (Ton-Frage 2026-07-20), keine Rezension |
| F 26 | `erzaehlstil` „# per Empfinden noch nicht erfasst → Offene Fragen“ | F: „# noch nicht recherchiert → Offene Fragen“ + Eintrag in F Offene Fragen · E Offene Fragen an Lucas: „per Empfinden noch nicht erfasst (Interview 2026-07-20)“ | Perspektive ist Fakt (Recherche-Lücke), Empfinden ist Frage an Lucas; Verweis zeigte ins Leere |
| F 28 | `komplexitaet` dito | wie F 26 | dito |
| F 27 | `tempo` „ruhig-stetig (Nutzer: 'trägt, aber grenzwertig')“ | F: „ruhig-stetig (Rezensionen: „ruhig, aber durchgehend spannend“; Bd. 2 etwas geringere Sogwirkung)“ · Nutzerzitat in E (Verdikt-Herleitung E 73, DNA-Begründung) | Nutzerzitat; Beleg F 55 / F 101 |
| F 31 | `handwerk` Zäher Start, Konstanter Vorwärtsdrang, Intrigen-Overload | F: `[]` · alle drei in E `bewertung` (−1) | nur Interview; Vorwärtsdrang laut Wertung verletzt; Community F 101 nennt nur geringere Sogwirkung Bd. 2, F 93 sogar „schnell in der Geschichte“ |
| F 36 | `analysiert` „2026-07-16 (Nachinterview 2026-07-20: Ton/Aspekte ergänzt)“ | F: „2026-07-16 (Recherche-Nachtrag 2026-07-20)“ · E Quellen: „[[2026-07-20 Interview Prinz von Staub und Schatten]] (Nachinterview: Ton/Aspekte ergänzt …)“ | Interview-Verweis → E; Recherche 2026-07-20 belegt in F 70 |
| F 39 | `tags: [werk, buch, reihe]` | F: `+ fantasy` | Genre-Tag gehört zum Werk |
| E 27 | `tags: [werk, reihe, hoerbuch, loved, fantasy]` | E: `[erlebnis, hoerbuch, loved]` | Vorlage Erlebnis |
| E 9 | `sprecher_bewertung: 2 # Hörbuch-Bonus, Günter Merlau (Interview 2026-07-20)` | entfernt; dieselbe Information steht in E `bewertung` „Günter Merlau“, wert 2 (E 16) und in der Tabelle E 60 inkl. „(Interview 2026-07-20)“ | Duplikat. Es bleibt der `bewertung`-Eintrag: Konventionen „Sprecher … als eigene Aspekt-Zeile in der Erlebnis-Notiz“; `sprecher_bewertung` steht in keiner Vorlage und wird von keinem Skript gelesen (nur in `werke_trennen.py` als Feldname zum Trennen) |
| F 48 | „Reihen-Pflicht: 5 geplant + Verbund → erfüllt.“ | E Lesestand, wörtlich | Reihen-Pflicht ist Lucas' No-Go |
| F 57 | „**Kontext:** [[Fantasy]] · **Autor:** … · **Sprecher:** …“ | F: „**Genre:** Epic Fantasy · … · **Sprecher (dt.):** …“ · E: „**Kontext:** [[Fantasy]] · **Quellen:** …“ | Kontext ist persönlich |
| F 65–68 | Bandtabelle mit Spalte „Lesestand“ („gehört ✓“) | F: dieselbe Tabelle ohne die Spalte · E Lesestand (E 48, unverändert) | gehört in E |
| F 115 | DNA Themen inkl. Rätselhafte Herkunft | F: drei Themen je mit Prämissen-Beleg · Rätselhafte Herkunft in E (`bewertung` +2, Tabelle) | wie F 24 |
| F 116 | „**Ton:** [[Geheimnisvoll-mysteriöse Aura]] (… = der Sog)“ | E DNA-Begründung, wörtlich | Lucas' Lesart |
| F 117 | „**Figuren:** [[Wachsende Hauptfigur]] (Tarikh) · **Setting:** Wüstenreich Aun-Mal“ | F: dieselbe Zeile + Belege („starke Figurenentwicklung“, F 54; „dichte Wüsten-/Orient-Atmosphäre“, F 95) | Quelle ergänzt |
| F 118 | „**Sprecher (Hörbuch-Bonus):** [[Günter Merlau]] +2 …“ | E neu „## Hörbuch-Erlebnis“, wörtlich (Wertung auch E 60) | Wertung |
| F 119 | „**Handwerk (negativ):** … verletzt … „zu politisch"“ | E DNA-Begründung, wörtlich | Wertung |
| F 120 | „**Tempo:** ruhig-stetig, „trägt, aber grenzwertig"“ | E DNA-Begründung, wörtlich · F: Tempo mit Rezensionsbeleg | Nutzerzitat |
| F 121–123 | Matching-Regel „Die geheimnisvolle Macht des Helden MUSS zentral bleiben …“ | E DNA-Begründung, wörtlich | Lucas' Wunsch |
| F 127 | „~~Beide Bände wirklich schon durch?~~ ✓ bestätigt (Interview 2026-07-20) …“ | E Lesestand, wörtlich | Lesestand |
| F 134 | „Quelle Interview: [[2026-07-20 …]] (Erstanalyse: [[2026-07-16 …]])“ | E: „**Quellen:** [[2026-07-20 Interview Prinz von Staub und Schatten]] (Nachinterview: …; Erstanalyse: [[2026-07-16 Interview Streitende Götter]])“ | Interview-Verweis → E |
| E 34–42 | H3 „Band-Unterschiede“ vor dem ersten H2 | E: H2 „Band-Unterschiede: Community-Kurve vs. mein Empfinden“ nach der Bewertung, Text E 35–42 wörtlich · F neu „### Auffällige Band-Unterschiede (Community)“: „Auftakt (Heimkehr) stärker gelobt als Bd. 2 …“ | Struktur (Vorlage); Community-Befund ist Fakt |
| E 65–66 | „geerbt aus [[Die Streitenden Götter]] (dort pflegen)“ | „geerbt aus [[Die Streitenden Götter – Lucas]] (dort pflegen)“ | Verweis zeigt auf Wertungen (Regel 6) |
| E 77–80 | „Community-Wertung Bd. 1 hoch (Audible.de 4,9 · ~1.633 …), Bd. 2 noch dünn (~400). Tenor: …“ | F neu „## 🧮 Community-Gesamtbild“: E 77–79 wörtlich · E: „Community-Wertung und Tenor: s. [[Der Prinz von Staub und Schatten]] (Community-Gesamtbild) — Bd. 1 hoch bewertet, …“; E 80 wörtlich | Zahlen stehen in F (F 17–18, F 67–68, F 93–101); in E nur Bezug |
| E 82–83 | „Vergleich zu Sturmfels: siehe dort (…)“ | „Vergleich zu Sturmfels: siehe [[Sturmfels-Akademie – Lucas]] (…)“ | Ziel explizit (Regel 6) |

## Neu hinzugekommen

| Wo | Was | Grundlage |
| --- | --- | --- |
| F Frontmatter | `verwandte_reihen: ["Sturmfels-Akademie"]` | Hierarchie in [[Die Streitenden Götter]] |
| F | „## 🗺️ Universum & Reihenfolge“ (Epos-Bd. 6 ff., Sturmfels = Epos-Bd. 1–5, Abhängigkeit nicht recherchiert) | Spalte „# (Epos)“; „Fortsetzung des Epos“ in der Sturmfels-Notiz |
| F | „**Hördauer gesamt (dt.):** ~37 h 11 (2.231 min) · Schnitt ~18:36“ | 1104 + 1127 min aus F 67–68 |
| F DNA | Hinweis „Nur belegte Merkmale …“, Quellen je Merkmal, Tempo-Zeile | Vorlage Werk.md |
| F Offene Fragen | Erzählstil (Perspektive) und Komplexität nicht recherchiert | F 26/F 28 verwiesen auf Offene Fragen, dort stand nichts |
| E Frontmatter | `besitz: ""`, `status: "durch"` | Status nach BEREINIGUNG.md: alle erschienenen Bände (2/2) erlebt, bestätigt im Interview 2026-07-20; Reihe läuft weiter (Kommentar) |
| E | `**Kontext:** … · **Quellen:** …` | aus F 57 / F 134 |
| E Bewertung | Hinweis „Geerbte Zeilen stehen bewusst nicht in `bewertung:`“ | Konventionen „Pflege nur an der Quelle“ |
| E | „## DNA-Begründung“, „## Hörbuch-Erlebnis“ | nur aus F verschobene Zeilen |
| E | „## Offene Fragen an Lucas“: Besitz; Erzählstil/Komplexität per Empfinden | nie raten; Interview 2026-07-20 „Offen geblieben“ |

## Runde 2 — Gegenprüfung + Beleg-Regel „Was als Beleg zählt“

| alt | Fund | Änderung |
| --- | --- | --- |
| F 29 | `figuren: [Wachsende Hauptfigur]` mit „Rezensionen: „starke Figurenentwicklung"“ — in F nur Zusammenfassung ohne Wortzitat, nicht auf Tarikh bezogen, Bd.-2-Kritik spricht eher dagegen | F: `figuren: []` + Kommentar; DNA-Zeile ohne Figuren; F Offene Fragen „Offen (DNA-Beleg): Wachsende Hauptfigur“ mit Grund; Wertung +1 bleibt in E |
| F 117 | Setting „(Community: „dichte Wüsten-/Orient-Atmosphäre")“ — Anführungszeichen um eine Zusammenfassung | „(Prämisse; Community-Lob: dichte Wüsten-/Orient-Atmosphäre)“ |
| F 24–25, F 31 | Runde 1 strich Rätselhafte Herkunft, Geheimnisvoll-mysteriöse Aura, Zäher Start, Intrigen-Overload still aus F. Neue Regel: unbelegt → „Offen (DNA-Beleg)“ | F Offene Fragen: vier „Offen (DNA-Beleg)“-Einträge mit Grund. Konstanter Vorwärtsdrang nicht aufgenommen: laut Wertung verletzt |
| — | Übrige DNA nach der Beleg-Regel | Geheimnisvolle Macht (Prämisse „rätselhafte Gabe“), Verlorenes Erbe (Prämisse: Exil, letzter Spross, Thron), Rache & Verfolgung (Prämisse: rachsüchtiges Adelshaus, Meuchler) → bleiben; Tempo: Wortzitat „ruhig, aber durchgehend spannend“ → bleibt |
