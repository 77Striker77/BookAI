---
aktualisiert:
gewicht_genres: 0.15
gewicht_themen: 0.25
gewicht_ton: 0.20
gewicht_erzaehlstil: 0.10
gewicht_tempo: 0.08
gewicht_komplexitaet: 0.07
gewicht_figuren: 0.10
gewicht_setting: 0.05
gewicht_handwerk: 0.00
tags: [profil, gewichte]
---

# ⚖️ Gewichte des Match-Scores — GLOBALE DEFAULTS

Formel: `match = Σ(score_dim × gewicht_dim) / Σ(gewicht_dim)` — Summe der Gewichte ≈ 1.0.

> **Kontext schlägt global:** hat der Kontext des Kandidaten (`Profil/Kontexte/<X>.md`)
> eigene `gewichte:`, gelten DIE. Diese Datei ist nur der Fallback für Kontexte ohne
> eigene Gewichte und für kontextlose Fälle. `handwerk` startet global bei 0.00 und
> wird erst gewichtet, wo Handwerks-Muster belegt sind (meist je Kontext).

## Begründung je Gewicht

*Jede Änderung braucht Evidenz aus [[Profil]] → "Muster & Beobachtungen" oder einem
Interview. Startwerte sind Defaults, noch unbegründet.*

| Dimension | Gewicht | Warum |
| --- | --- | --- |
| Themen | 0.25 | Default — noch keine Evidenz |
| Ton | 0.20 | Default |
| Genres | 0.15 | Default |
| Erzählstil | 0.10 | Default |
| Figuren | 0.10 | Default |
| Tempo | 0.08 | Default |
| Komplexität | 0.07 | Default |
| Setting | 0.05 | Default |

## Änderungshistorie

| Datum | Änderung | Anlass |
| --- | --- | --- |
