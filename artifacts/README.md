# Die 2 festen Artefakte

Hier leben die HTML-Dateien der beiden einzigen Artefakte des Systems — **stabile
Pfade**, damit sie immer unter derselben URL republisht werden:

| Datei | Artefakt | Favicon | Verhalten |
|---|---|---|---|
| `bibliothek.html` | Meine Bibliothek (Basis: alle guten Bücher + Kerndaten) | 📚 | wird bei jeder Titel-Analyse aktualisiert |
| `empfehlungen.html` | Empfehlungen (letzter Lauf, %-Balken) | 🎯 | wird je Empfehlungslauf komplett überschrieben |

Regeln (Details: `.claude/skills/book-reco-artifact/SKILL.md`):
- **Nie neue Artefakte anlegen.** Nur diese beiden Dateien editieren + republishen.
- In neuer Session: erst `Artifact(action:"list")`, URL heraussuchen und als `url:`
  mitgeben — sonst entsteht ungewollt eine neue URL.
- `<title>` und Favicon nie ändern (Wiedererkennung).
- Vorlagen: `.claude/skills/book-reco-artifact/references/*-template.html`.
