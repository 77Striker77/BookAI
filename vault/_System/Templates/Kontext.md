---
name: ""               # z. B. Fantasy
aktualisiert:
uebergeordnet: ""      # falls Sub-Kontext (Split-Regel 2): erbt Nicht-Überschriebenes
buecher: 0             # Zähler analysierter Titel in diesem Kontext
# --- Gewichte NUR für diesen Kontext (überschreiben Gewichte.md; Summe ≈ 1.0) ---
gewichte:
  genres: 0.15
  themen: 0.25
  ton: 0.20
  erzaehlstil: 0.10
  tempo: 0.08
  komplexitaet: 0.07
  figuren: 0.10
  setting: 0.05
  handwerk: 0.00       # >0 setzen, sobald Handwerks-Muster in diesem Kontext belegt sind
# --- Präferenzen in diesem Kontext ---
tempo_pref: ""
komplexitaet_pref: ""
laenge_seiten: ""
laenge_stunden: ""
kontext_no_gos: []     # nur hier geltende Ausschlüsse
tags: [kontext]
---

# 🗂️ Kontext: ⟨Name⟩

## Charakter dieses Geschmacksraums

⟨2–3 Sätze: was ich HIER suche — und was hier anders ist als in anderen Kontexten.⟩

## Top-Merkmale in diesem Kontext

<!-- Nur die stärksten; vollständig via status_kontexte der Merkmal-Notizen -->
| Merkmal | Status hier | Evidenz |
| --- | --- | --- |
| [[⟨Merkmal⟩]] | loved | [[⟨Buch⟩]] +2, [[⟨Interview⟩]] |
| [[⟨Merkmal⟩]] | disliked | [[⟨Buch⟩]] −2 |

## Kombinationsregeln (Wechselwirkungen — schlagen Einzel-Status)

| Wenn … | dann … | Evidenz |
| --- | --- | --- |
| [[⟨Ich-Erzähler⟩]] MIT [[⟨Unzuverlässig⟩]] | +2 | [[⟨Buch⟩]], [[⟨Interview⟩]] |
| [[⟨Ich-Erzähler⟩]] OHNE [[⟨Unzuverlässig⟩]] | 0 | ⟨…⟩ |

## Bücher in diesem Kontext

*→ Backlinks; wichtigste hier gepinnt:*

| Titel | Verdikt |
| --- | --- |
| [[⟨…⟩]] | loved |

## Gewichts-Begründung & Änderungshistorie

| Datum | Änderung | Anlass/Evidenz |
| --- | --- | --- |
