# Namenskollisionen aufgelöst (2026-10-11)

Fünf Notiznamen existierten doppelt; `[[Name]]` war mehrdeutig. Jeder betroffene Link wurde
einzeln eingeordnet (Kontext der Zeile). Alle übrigen Links meinen bereits die Notiz, die den
Namen behält, und bleiben unverändert:

- `[[Der Donnerstagsmordclub]]`, `[[Die guten Jungs]]`, `[[Die bösen Jungs]]` → Werk (Fakten)
- `[[Vuldranni (iNcarn8)]]` → Werk-Verbund (Fakten)
- `[[LitRPG]]` → Kontext (`Profil/Kontexte/LitRPG.md`) — so lesen auch die `kontext:`-Felder

Abweichung vom ursprünglichen Vorschlag: Umbenannt wurde das **Genre-Merkmal** (9 Links), nicht
der Kontext (~60 Links + alle `kontext: "LitRPG"`-Felder + Skill-Pfad `Profil/Kontexte/<Raum>.md`).

| Wo | alt | neu |
| --- | --- | --- |
| Datei | `Empfehlungen/Kandidaten/Der Donnerstagsmordclub.md` | `Empfehlungen/Kandidaten/Der Donnerstagsmordclub (Kandidat).md` |
| Datei | `Empfehlungen/Kandidaten/Die guten Jungs.md` | `Empfehlungen/Kandidaten/Die guten Jungs (Kandidat).md` |
| Datei | `Empfehlungen/Kandidaten/Die bösen Jungs.md` | `Empfehlungen/Kandidaten/Die bösen Jungs (Kandidat).md` |
| Datei | `Bibliothek/Universen/Vuldranni (iNcarn8).md` | `Bibliothek/Universen/Vuldranni (Welt).md` |
| Datei | `Merkmale/Genres/LitRPG.md` | `Merkmale/Genres/LitRPG (Genre).md` |
| `Bibliothek/Universen/Vuldranni (Welt).md` Z. 2 | `name: "Vuldranni (iNcarn8)"` | `name: "Vuldranni (Welt)"` |
| `Bibliothek/Universen/Vuldranni (Welt).md` nach H1 | — | neuer Verweis auf den Werk-Verbund [[Vuldranni (iNcarn8)]] |
| `Bibliothek/Autoren/Eric Ugland.md` Z. 8 | `"[[Vuldranni (iNcarn8)]]"` | `"[[Vuldranni (Welt)]]"` |
| `Bibliothek/Autoren/Eric Ugland.md` Z. 36 | `**[[Vuldranni (iNcarn8)]]** — Spielwelt` | `**[[Vuldranni (Welt)|Vuldranni (iNcarn8)]]** — Spielwelt` |
| `Empfehlungen/Läufe/2026-07-17 Deutsche Bücher quer über alle Räume.md` Z. 32 | `| [[Die guten Jungs]] |` | `| [[Die guten Jungs (Kandidat)|Die guten Jungs]] |` |
| `Empfehlungen/Läufe/2026-07-17 Deutsche Bücher quer über alle Räume.md` Z. 67 | `| [[Der Donnerstagsmordclub]] |` | `| [[Der Donnerstagsmordclub (Kandidat)|Der Donnerstagsmordclub]] |` |
| `Empfehlungen/Warteliste.md` Z. 14 | `| [[Die guten Jungs]] |` | `| [[Die guten Jungs (Kandidat)|Die guten Jungs]] |` |
| `Werke/Buecher/Die bösen Jungs.md` Z. 61 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Die guten Jungs.md` Z. 61 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Dungeon Crawler Carl.md` Z. 56 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Dungeon Crawler Carl.md` Z. 126 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Survival Quest.md` Z. 60 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Survival Quest.md` Z. 168 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Vuldranni (iNcarn8).md` Z. 55 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Werke/Buecher/Vuldranni (iNcarn8).md` Z. 193 | `[[LitRPG]]` | `[[LitRPG (Genre)|LitRPG]]` |
| `Empfehlungen/Kandidaten/Die guten Jungs (Kandidat).md` Z. 32 | `genres: ["LitRPG", "GameLit", "Action-Komödie"]` | `genres: ["LitRPG (Genre)", "GameLit", "Action-Komödie"]` |
| `Empfehlungen/Kandidaten/He Who Fights With Monsters.md` Z. 18 | `genres: ["LitRPG", "Progression Fantasy", "Isekai"]` | `genres: ["LitRPG (Genre)", "Progression Fantasy", "Isekai"]` |
| `Empfehlungen/Kandidaten/The Primal Hunter.md` Z. 17 | `genres: ["LitRPG", "System-Apokalypse", "Progression Fantasy"]` | `genres: ["LitRPG (Genre)", "System-Apokalypse", "Progression Fantasy"]` |
| `Werke/Buecher/Die bösen Jungs.md` Z. 28 | `genres: [LitRPG, GameLit, Action-Komödie]` | `genres: ["LitRPG (Genre)", GameLit, Action-Komödie]` |
| `Werke/Buecher/Die guten Jungs.md` Z. 28 | `genres: [LitRPG, GameLit, Action-Komödie]` | `genres: ["LitRPG (Genre)", GameLit, Action-Komödie]` |
| `Werke/Buecher/Dungeon Crawler Carl.md` Z. 25 | `genres: [LitRPG, Science-Fantasy]` | `genres: ["LitRPG (Genre)", Science-Fantasy]` |
| `Werke/Buecher/Survival Quest.md` Z. 27 | `genres: [LitRPG]` | `genres: ["LitRPG (Genre)"]` |
| `Werke/Buecher/Vuldranni (iNcarn8).md` Z. 23 | `genres: [LitRPG, GameLit, Action-Komödie]` | `genres: ["LitRPG (Genre)", GameLit, Action-Komödie]` |
