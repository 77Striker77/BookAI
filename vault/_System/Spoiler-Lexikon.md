---
tags: [system, spoiler]
---

# Spoiler-Lexikon — die Wortlisten des Linters

Datenquelle für `scripts/spoiler_check.py`. **Hier wird getunt, nicht im Code.** Der Linter
liest die Listen aus den Codeblöcken unten (eine Zeile = ein Eintrag, `#` = Kommentar).
Groß-/Kleinschreibung egal. Einträge sind **Regex** — für normale Wörter reicht der reine
Text, `\b`-Grenzen setzt der Linter selbst.

Fehlt diese Notiz, benutzt der Linter eingebaute Standardlisten (fail-safe).

## `hart` — verrät fast immer Handlung

Ein Treffer + Werk jenseits der Grenze = **Verstoß** (blockt Publish).

```spoiler-hart
# --- Figurenschicksal ---
stirbt
starb
sterben wird
tötet
getötet
ermordet
bringt \w+ um
überlebt nicht
überlebt (den|die|das)
opfert sich
opfertod
fällt im kampf
tod (von|des|der)
# --- Ausscheiden/Abwesenheit (Paraphrasen ohne Todeswort) ---
scheidet aus
scheidet in .{0,20}(bd|band)\.? ?\d
ist ab (bd|band)\.? ?\d+ nicht mehr
kommt (ab|in) (bd|band)\.? ?\d+ nicht mehr
taucht (ab|in) (bd|band)\.? ?\d+ nicht mehr auf
verlässt die (gruppe|truppe|reihe|crew)
ist nicht mehr (dabei|teil der)
verabschiedet sich aus der (reihe|handlung)
# --- Verrat & Identität ---
verrät
verrat (von|des|der|an)
verräter
doppelagent
entpuppt sich
stellt sich (als|heraus)
in wahrheit (ist|war)
wahre identität
echte identität
ist in wirklichkeit
gibt sich als
# --- Enthüllung & Auflösung ---
der (mörder|täter) ist
mörder ist
täter ist
stellt sich als täter
enthüllt (dass|sich)
enthüllung
offenbart (dass|sich)
es zeigt sich, dass
löst den fall
auflösung (des|der) (fall|krimi)
plot.?twist
schlusstwist
# --- Struktur-Verrat ---
am ende (des buches|des bandes|der reihe|von band)
im finale (stirbt|kommt es|wird|passiert|offenbart)
das ende (verrät|zeigt|bringt)
endet damit, dass
cliffhanger:.{0,40}(stirbt|verrät|entpuppt)
# --- Beziehung / Statuswechsel ---
wird (zum|zur) (verräter|könig|königin|dunkel)
kehrt (als|zurück als)
ist (der|die) (vater|mutter|sohn|tochter|bruder|schwester) von
# --- Englisch (Quellen sind oft EN) ---
dies in (book|volume)
is killed
gets killed
betrays
turns out to be
is revealed (to be|as)
the (killer|murderer|culprit) is
secretly (is|was)
comes back as
sacrifices (himself|herself|themselves)
```

## `weich` — verdächtig, braucht Urteil

Ein Treffer = **Warnung** (kein Block, aber der `spoiler-guard` schaut drauf).

```spoiler-weich
finale
das ende
schluss der reihe
im letzten band
höhepunkt der handlung
auflösung
wendepunkt
rückkehr (von|des|der)
verlust (von|des|der)
zeitsprung
wiedergeburt
neue fraktion
verbündet sich mit
trennt sich von
schwangerschaft
geheimnis (um|von|des|der)
prophezeiung erfüllt
```

## `titel-whitelist` — nie als Spoiler werten

Werk-, Band- und Reihentitel sind **Neutralzone** (§2 der Politik), auch wenn sie
Spoiler-Wörter enthalten („Wer stirbt, braucht festes Schuhwerk" ist ein Buchtitel, kein
Spoiler). Titel aus den Band-Tabellen des Vaults erkennt der Linter automatisch; alles
darüber hinaus kommt hier rein.

```spoiler-titel-whitelist
# Reihen-/Bandtitel, die Spoiler-Wörter enthalten (nur Titel, keine Sätze!)
Vier Enthauptungen und ein Todesfall
Wer stirbt, braucht festes Schuhwerk
Irgendwen haben wir doch alle auf dem Gewissen
Everyone in My Family Has Killed Someone
Jeder im Zug ist verdächtig
Everyone on This Train Is a Suspect
Der Donnerstagsmordclub
The Thursday Murder Club
Die mörderischen Cunninghams
Der Mann, der zweimal starb
The Man Who Died Twice
Die Gilde der schwarzen Magier
Das Lied des Blutes
The Butcher's Masquerade
This Inevitable Ruin
A Parade of Horribles
The Gate of the Feral Gods
Killing Them Awfully
Of Slicing Men
Nacht der Unholde
Die Freischaufler
Ein Teufel stirbt immer zuletzt
```

## Ausnahme-Marker im Text (stärker als jede Wortliste)

Ein Block, der ausdrücklich Neutralzone ist (typisch: **Klappentext/Prämisse von Band 1**),
wird direkt im Dokument markiert — das ist präziser als eine Wortliste und **prüfbar**
(`python3 scripts/spoiler_check.py --ausnahmen …` listet jede einzelne Ausnahme auf):

| Format | Marker |
| --- | --- |
| HTML | `<p data-spoilerfrei="Klappentext Bd. 1">…</p>` oder `class="… spoilerfrei"` |
| Markdown | `<!-- spoilerfrei -->` (die Zeile) bzw. `<!-- spoilerfrei:start -->` … `<!-- spoilerfrei:end -->` |

⚠️ Der Marker schaltet nur die **Wortlisten** ab. `spoiler_sperrbegriffe` (§4 der Politik)
gelten weiter — ein Figurenname aus Bd. 6 ist auch im Klappentext ein Leck. Wer den Marker
setzt, muss die Stelle vorher gegen §2 geprüft haben; Missbrauch fällt im Audit auf.

## `phrasen-whitelist` — stehende Wendungen des Systems

Formulierungen, die im Vault/Artefakt regelmäßig vorkommen und garantiert harmlos sind.
Hier NUR eintragen, was nachweislich ein Fehlalarm war — nicht auf Verdacht (sonst
verwässert die Regel).

```spoiler-phrasen-whitelist
# --- belegte Fehlalarme aus dem Lauf 2026-08-11 (Artefakt-Prüfung) ---
stirbt fast
stirbt und wacht
stirbt, wacht
entpuppt sich als Talent
# --- System-Vokabular ---
Reihen-Pflicht
Finale (Bd
(Finale)
Finale ausstehend
Finale angekündigt
das Finale ist noch nicht erschienen
starkes Finale
Starkes Finale
Aufgeblähter Mittelteil
Emotionale Sucker-Punches
kein Termin
Auflösung der offenen Fragen steht noch aus
```

## Pflegehinweis

Neue Regel? → Erst hier eintragen, dann **beide** Testfälle in `tests/spoiler/faelle/`
anlegen (einen der greifen muss, einen der NICHT greifen darf), dann
`bash scripts/spoiler-selftest.sh`. Ohne Testfall keine Regel.
