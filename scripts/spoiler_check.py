#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spoiler_check.py — deterministischer Spoiler-Linter für BookAI.

Regeln & Grenzen kommen AUSSCHLIESSLICH aus dem Vault (OBERSTE REGEL):
  vault/_System/Spoiler-Politik.md    die Regeln (menschenlesbar)
  vault/_System/Spoiler-Lexikon.md    die Wortlisten (maschinenlesbar, hier getunt)
  vault/Bibliothek/Werke/*.md         die Lesestand-Grenze je Werk (Frontmatter)

Aufruf:
    python3 scripts/spoiler_check.py artifacts/bibliothek.html
    python3 scripts/spoiler_check.py --stdin --herkunft chat < text.txt
    python3 scripts/spoiler_check.py --json --gate artifacts/*.html
    python3 scripts/spoiler_check.py --grenzen        # nur die Grenzen anzeigen

Exit-Codes:
    0 = sauber
    1 = Warnungen (menschliches/semantisches Urteil nötig)
    2 = VERSTOSS (hart — Publish/Ausgabe blockieren)
    3 = Aufruffehler

Kein Fremdpaket nötig (nur Standardbibliothek).
"""

from __future__ import annotations

import argparse
import hashlib
import html as htmllib
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field, asdict
from pathlib import Path

# --------------------------------------------------------------------------------------
# Fallback-Listen — greifen nur, wenn vault/_System/Spoiler-Lexikon.md fehlt (fail-safe).
# --------------------------------------------------------------------------------------
FALLBACK_HART = [
    r"stirbt", r"getötet", r"ermordet", r"überlebt nicht", r"opfert sich",
    r"tod (von|des|der)", r"verrät", r"verräter", r"entpuppt sich",
    r"stellt sich (als|heraus)", r"in wahrheit (ist|war)", r"wahre identität",
    r"der (mörder|täter) ist", r"plot.?twist", r"am ende (des buches|der reihe)",
    r"is killed", r"betrays", r"turns out to be", r"is revealed (to be|as)",
]
FALLBACK_WEICH = [r"finale", r"das ende", r"auflösung", r"wendepunkt", r"letzter band"]

# Bandreferenzen: "Bd. 5", "Band 5", "Buch 5", "Teil 5", "Bd 5-7", "books 3–4"
BAND_RE = re.compile(
    r"\b(?:bd\.?|band|bände|buch|bücher|teil|vol\.?|volume|book|books)\s*"
    r"(\d{1,2})(?:\s*(?:[-–—]|bis|to)\s*(\d{1,2}))?",
    re.IGNORECASE,
)
# Wo ein Werk erwähnt wird, ohne Zahl: "spätere Bände", "kommende Bände"
SPAETER_RE = re.compile(
    r"\b(spätere[nr]?\s+bänd|kommende[nr]?\s+bänd|folgebänd|later\s+book|subsequent\s+book)",
    re.IGNORECASE,
)

VERSTOSS, WARNUNG, OK = "VERSTOSS", "WARNUNG", "OK"


# --------------------------------------------------------------------------------------
# Datenmodell
# --------------------------------------------------------------------------------------
@dataclass
class Werk:
    titel: str
    datei: str
    erlebt_bis: int = 0
    aktuell: int = 0
    gesamt: int = 0
    stand: str = ""
    sperrbegriffe: list = field(default_factory=list)
    aliase: list = field(default_factory=list)
    universum: str = ""
    abgeschlossen: str = ""
    synthetisch: bool = False   # aus spoiler_unerlebte_reihen erzeugt (immer `blurb`)

    @property
    def stufe(self) -> str:
        """voll | bis_band_N | blurb — fail-closed bei fehlenden/kaputten Angaben."""
        if self.erlebt_bis <= 0:
            return "blurb"
        if self.gesamt and self.erlebt_bis >= self.gesamt and self.aktuell <= 0:
            return "voll"
        return f"bis_band_{self.erlebt_bis}"

    @property
    def voll(self) -> bool:
        return self.stufe == "voll"

    def namen(self) -> list:
        """Alle Schreibweisen, unter denen das Werk im Text auftauchen kann."""
        n = {self.titel, *self.aliase}
        # "Vuldranni (iNcarn8)" -> auch "Vuldranni" und "iNcarn8"
        m = re.match(r"^(.+?)\s*\((.+?)\)\s*$", self.titel)
        if m:
            n.update({m.group(1).strip(), m.group(2).strip()})
        # "Die Nebelgeborenen (Mistborn)" -> auch ohne Artikel
        for x in list(n):
            a = re.sub(r"^(die|der|das|the)\s+", "", x, flags=re.IGNORECASE).strip()
            if len(a) >= 4:
                n.add(a)
        return sorted({x for x in n if len(x) >= 4}, key=len, reverse=True)


@dataclass
class Fund:
    schwere: str          # VERSTOSS | WARNUNG
    regel: str            # S1 … S6
    werk: str
    datei: str
    zeile: int
    stelle: str           # der beanstandete Textausschnitt
    treffer: str          # was genau ausgelöst hat
    grund: str
    tipp: str


# --------------------------------------------------------------------------------------
# Vault einlesen
# --------------------------------------------------------------------------------------
def _frontmatter(text: str) -> dict:
    """Minimaler Frontmatter-Parser (flache Keys + einfache Listen) — kein PyYAML nötig."""
    if not text.startswith("---"):
        return {}
    ende = text.find("\n---", 3)
    if ende < 0:
        return {}
    fm = {}
    for zeile in text[3:ende].splitlines():
        z = zeile.split("#")[0].rstrip() if not zeile.strip().startswith("#") else ""
        m = re.match(r"^([a-zA-Z_][\w]*):\s*(.*)$", z)
        if not m:
            continue
        key, wert = m.group(1), m.group(2).strip()
        if wert.startswith("[") and wert.endswith("]"):
            inhalt = wert[1:-1].strip()
            fm[key] = [x.strip().strip('"\'') for x in inhalt.split(",") if x.strip()] if inhalt else []
        else:
            fm[key] = wert.strip('"\'')
    return fm


def _int(wert, default=0) -> int:
    try:
        return int(str(wert).strip())
    except (TypeError, ValueError):
        return default


def lade_werke(root: Path) -> list:
    werke = []
    for p in sorted((root / "vault" / "Bibliothek" / "Werke").glob("*.md")):
        fm = _frontmatter(p.read_text(encoding="utf-8"))
        titel = fm.get("titel") or p.stem
        werke.append(Werk(
            titel=titel,
            datei=str(p.relative_to(root)),
            erlebt_bis=_int(fm.get("spoiler_erlebt_bis"), 0),
            aktuell=_int(fm.get("spoiler_aktuell"), 0),
            gesamt=_int(fm.get("spoiler_gesamt"), _int(fm.get("baende_gesamt"), 0)),
            stand=str(fm.get("spoiler_stand", "")),
            sperrbegriffe=[x for x in fm.get("spoiler_sperrbegriffe", []) if x],
            aliase=[x for x in fm.get("spoiler_aliase", []) if x],
            universum=str(fm.get("universum", "")),
            abgeschlossen=str(fm.get("abgeschlossen", "")),
        ))
        # Reihen im SELBEN Universum, die der Nutzer nie erlebt hat (z. B. Prequel-Reihen):
        # als eigenes Pseudo-Werk mit Stufe `blurb` führen, damit sie nicht über die
        # `voll`-Freigabe der Hauptreihe mitrutschen.
        for name in fm.get("spoiler_unerlebte_reihen", []) or []:
            if name and not any(w.titel == name for w in werke):
                werke.append(Werk(titel=name, datei=str(p.relative_to(root)),
                                  erlebt_bis=0, aktuell=0, gesamt=0,
                                  stand=str(fm.get("spoiler_stand", "")), synthetisch=True))
    return werke


def _bloecke(text: str, marker: str) -> list:
    """Liest ```<marker> … ``` Codeblöcke aus einer Markdown-Notiz."""
    out = []
    for m in re.finditer(r"```" + re.escape(marker) + r"\s*\n(.*?)```", text, re.S):
        for zeile in m.group(1).splitlines():
            z = zeile.strip()
            if z and not z.startswith("#"):
                out.append(z)
    return out


def lade_lexikon(root: Path) -> dict:
    p = root / "vault" / "_System" / "Spoiler-Lexikon.md"
    if not p.exists():
        return {"hart": FALLBACK_HART, "weich": FALLBACK_WEICH,
                "titel": [], "phrasen": [], "quelle": "eingebaut (Lexikon-Notiz fehlt!)"}
    t = p.read_text(encoding="utf-8")
    return {
        "hart": _bloecke(t, "spoiler-hart") or FALLBACK_HART,
        "weich": _bloecke(t, "spoiler-weich") or FALLBACK_WEICH,
        "titel": _bloecke(t, "spoiler-titel-whitelist"),
        "phrasen": _bloecke(t, "spoiler-phrasen-whitelist"),
        "quelle": str(p.relative_to(root)),
    }


def sammle_titel(root: Path) -> list:
    """
    Neutralzone: Werk-/Band-/Kandidaten-/Personen-Titel dürfen Spoiler-Wörter enthalten
    ("Wer stirbt, braucht festes Schuhwerk" ist ein Buchtitel). Sie werden vor der
    Lexikon-Prüfung maskiert.
    """
    titel = set()
    for unter in ("Bibliothek/Werke", "Bibliothek/Autoren", "Bibliothek/Sprecher",
                  "Bibliothek/Universen", "Empfehlungen/Kandidaten"):
        d = root / "vault" / unter
        if d.is_dir():
            titel.update(p.stem for p in d.glob("*.md"))
    # Bandtitel aus den Tabellen der Werk-Notizen: Zeilen, deren erste Zelle eine Bandnummer ist
    for p in (root / "vault" / "Bibliothek" / "Werke").glob("*.md"):
        for zeile in p.read_text(encoding="utf-8").splitlines():
            if not zeile.lstrip().startswith("|"):
                continue
            zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
            if not zellen or not re.match(r"^\*{0,2}\d{1,2}(\s*[-–—]\s*\d{1,2})?\*{0,2}$", zellen[0]):
                continue
            for zelle in zellen[1:]:
                for stueck in re.split(r"\s*/\s*|\s+·\s+", zelle):
                    s = re.sub(r"[*_`⚠️✅▶️⏳🇩🇪🇬🇧]", "", stueck).strip(" „“\"'*")
                    if len(s) >= 8 and not re.match(r"^[\d.,%\s–—-]+$", s):
                        titel.add(s)
    return sorted({t for t in titel if len(t) >= 5}, key=len, reverse=True)


# --------------------------------------------------------------------------------------
# Text gewinnen
# --------------------------------------------------------------------------------------
def text_aus(pfad: Path) -> str:
    roh = pfad.read_text(encoding="utf-8", errors="replace")
    if pfad.suffix.lower() in (".html", ".htm", ".xml", ".svg"):
        return html_zu_text(roh)
    return roh


MARKER = "⟦SPOILERFREI⟧"
# Ausnahme-Marker: <div data-spoilerfrei="Klappentext Bd. 1"> … oder class="… spoilerfrei"
RE_MARKER_HTML = re.compile(r"<[a-zA-Z][^>]*(?:data-spoilerfrei|class\s*=\s*[\"'][^\"']*\bspoilerfrei\b)[^>]*>")
RE_MARKER_MD = re.compile(r"<!--\s*spoilerfrei(?::(start|end))?\b[^>]*-->", re.IGNORECASE)


def html_zu_text(roh: str) -> str:
    # Ausnahme-Marker VOR dem Tag-Strippen in ein Textzeichen retten
    roh = RE_MARKER_HTML.sub(lambda m: m.group(0) + MARKER, roh)
    roh = re.sub(r"<!--.*?-->", " ", roh, flags=re.S)
    roh = re.sub(r"<(script|style)\b.*?</\1>", " ", roh, flags=re.S | re.I)
    # Blockenden zu Zeilenumbrüchen, damit Sätze nicht über Karten hinweg verschmelzen
    roh = re.sub(r"(?i)</(p|div|li|tr|td|th|h[1-6]|section|article|figcaption)>", "\n", roh)
    roh = re.sub(r"(?i)<br\s*/?>", "\n", roh)
    roh = re.sub(r"<[^>]+>", " ", roh)
    roh = htmllib.unescape(roh)
    roh = re.sub(r"[ \t ]+", " ", roh)
    return re.sub(r"\n{2,}", "\n", roh)


def norm(s: str) -> str:
    """Für Vergleiche: Kleinschreibung, Sonderzeichen vereinheitlicht."""
    s = unicodedata.normalize("NFKC", s).lower()
    return s.replace("„", '"').replace("“", '"').replace("’", "'").replace("–", "-").replace("—", "-")


# Abkürzungen, hinter denen KEIN Satz endet ("Bd. 12" darf nicht zerrissen werden)
ABK = r"(?:bd|bde|nr|vol|abb|ca|bzw|ggf|inkl|u|z|d|s|hrsg|übers|jr|st|dt|engl|orig|ff|vgl)"
_SCHUTZ = ""


def saetze(block: str) -> list:
    """Block in prüfbare Segmente zerlegen (Satzenden, Aufzählungen, Tabellenzellen)."""
    geschuetzt = re.sub(rf"\b{ABK}\.", lambda m: m.group(0)[:-1] + _SCHUTZ, block, flags=re.I)
    teile = re.split(r"(?<=[.!?;:])\s+|\s+[·•]\s+|\s*\|\s*", geschuetzt)
    return [t.replace(_SCHUTZ, ".").strip() for t in teile if t.strip()]


# --------------------------------------------------------------------------------------
# Prüfung
# --------------------------------------------------------------------------------------
class Pruefer:
    def __init__(self, root: Path):
        self.root = root
        self.werke = lade_werke(root)
        self.lex = lade_lexikon(root)
        self.titel = sammle_titel(root) + self.lex["titel"]
        self.phrasen = [norm(p) for p in self.lex["phrasen"]]
        self.re_hart = [(m, re.compile(r"\b" + m + r"\b", re.IGNORECASE)) for m in self.lex["hart"]]
        self.re_weich = [(m, re.compile(r"\b" + m + r"\b", re.IGNORECASE)) for m in self.lex["weich"]]
        self.re_titel = [(t, re.compile(re.escape(norm(t)))) for t in self.titel if len(t) >= 5]
        self.re_werke = [(w, [re.compile(r"\b" + re.escape(norm(n)) + r"\b") for n in w.namen()])
                         for w in self.werke]
        self.ausnahmen = []   # protokollierte `spoilerfrei`-Blöcke (prüfbar, s. --ausnahmen)

    # -- Hilfen ------------------------------------------------------------------------
    def maskiere(self, s: str) -> str:
        """Titel (Neutralzone) und bekannte harmlose Phrasen unkenntlich machen."""
        n = norm(s)
        for _, rx in self.re_titel:
            n = rx.sub(" ○ ", n)
        for p in self.phrasen:
            n = n.replace(p, " ○ ")
        return n

    def werke_in(self, s: str) -> list:
        n = norm(s)
        return [w for w, rxs in self.re_werke if any(rx.search(n) for rx in rxs)]

    @staticmethod
    def baender_in(s: str) -> list:
        out = []
        for m in BAND_RE.finditer(s):
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            out.extend(range(min(a, b), max(a, b) + 1))
        return out

    def lexikon_treffer(self, maskiert: str):
        for muster, rx in self.re_hart:
            t = rx.search(maskiert)
            if t:
                return "hart", muster, t.group(0)
        for muster, rx in self.re_weich:
            t = rx.search(maskiert)
            if t:
                return "weich", muster, t.group(0)
        return None, None, None

    # -- Hauptdurchlauf ----------------------------------------------------------------
    def pruefe(self, text: str, datei: str, herkunft: str) -> list:
        """
        herkunft: artefakt | empfehlung | chat | subagent | vault | unbekannt
        Bestimmt die Härte: in 'vault' sind Details erlaubt, sofern in 🔒-Block.
        """
        funde = []
        ist_vault = herkunft == "vault"
        # Empfehlungen/Kandidaten: per Definition ungelesen -> alles ist blurb-pflichtig
        nur_blurb = herkunft in ("empfehlung", "kandidat")

        zeilen = text.splitlines()
        kontext_werke, kontext_alter = [], 99
        in_spoilerblock = False
        in_freizone = False           # <!-- spoilerfrei:start --> … :end

        for i, zeile in enumerate(zeilen, start=1):
            roh = zeile.strip()
            if not roh:
                kontext_alter += 1
                continue

            # --- Ausnahme-Marker: ausgewiesene Neutralzone (Klappentext Bd. 1 o. Ä.) ----
            m_md = RE_MARKER_MD.search(roh)
            if m_md and m_md.group(1) == "start":
                in_freizone = True
                continue
            if m_md and m_md.group(1) == "end":
                in_freizone = False
                continue
            frei = in_freizone or (MARKER in roh) or bool(m_md)
            if frei:
                self.ausnahmen.append({"datei": datei, "zeile": i, "text": kurz(roh)})
            roh = roh.replace(MARKER, " ")

            # 🔒-Callout im Vault: dort ist Spoiliges ausdrücklich erlaubt
            if ist_vault:
                if re.search(r"\[!\w+\][+-]?\s*🔒|🔒\s*SPOILER", zeile):
                    in_spoilerblock = True
                    continue
                if in_spoilerblock:
                    if zeile.lstrip().startswith(">"):
                        continue
                    in_spoilerblock = False

            gefunden = self.werke_in(roh)
            if gefunden:
                kontext_werke, kontext_alter = gefunden, 0
            else:
                kontext_alter += 1
            # Kontext eines Werks trägt max. 3 Zeilen weit (Überschrift -> Absatz)
            aktive = gefunden or (kontext_werke if kontext_alter <= 3 else [])

            # Bandbezug gilt für die ganze Zeile: "Bd. 9: … stirbt …" steht oft in
            # getrennten Segmenten (Tabellenzelle, Doppelpunkt, Aufzählung).
            baender_zeile = self.baender_in(roh)

            for satz in saetze(roh):
                maskiert = self.maskiere(satz)
                art, muster, treffer = self.lexikon_treffer(maskiert)
                baender = self.baender_in(satz) or baender_zeile
                spaeter = bool(SPAETER_RE.search(satz)) or bool(SPAETER_RE.search(roh))

                # --- S1: harte Sperrbegriffe (gelten IMMER, auch ohne Kontext) ---------
                for w in self.werke:
                    if w.voll:
                        continue
                    for begriff in w.sperrbegriffe:
                        if re.search(r"\b" + re.escape(norm(begriff)) + r"\b", norm(satz)):
                            funde.append(Fund(
                                VERSTOSS if not ist_vault else WARNUNG, "S1", w.titel, datei, i,
                                kurz(satz), begriff,
                                f"Sperrbegriff aus [[{w.titel}]] — existiert erst jenseits meiner "
                                f"Grenze (Stand: {stufe_text(w)}).",
                                "Begriff entfernen oder Aussage auf die Neutralzone (§2) zurückführen."
                                if not ist_vault else "In einen `> [!warning]- 🔒 SPOILER`-Block verschieben.",
                            ))

                # Ausgewiesene Neutralzone: Lexikonregeln aus. Sperrbegriffe (S1) gelten
                # trotzdem — ein Figurenname aus Bd. 6 ist auch im Klappentext ein Leck.
                if frei:
                    continue

                if not art and not (nur_blurb and baender):
                    continue

                # --- S5: Empfehlungs-/Kandidatenkontext = per Definition ungelesen ------
                if nur_blurb and art == "hart":
                    funde.append(Fund(
                        VERSTOSS, "S5", "(Kandidat/Empfehlung)", datei, i,
                        kurz(satz), treffer,
                        "Empfohlene Werke sind per Definition ungelesen → nur Klappentext-Ebene "
                        "(Freigabestufe `blurb`).",
                        "Auf Prämisse, Ton, Tempo, Metadaten und Wertungen beschränken — "
                        "keine Ereignisse/Wendungen.",
                    ))
                    continue

                if not aktive:
                    # Kein Werk zuzuordnen: nur in harten Ausgaben und nur bei hartem Treffer
                    if art == "hart" and not ist_vault and herkunft != "unbekannt":
                        funde.append(Fund(
                            WARNUNG, "S4", "(unbekanntes Werk)", datei, i,
                            kurz(satz), treffer,
                            "Handlungsverratende Formulierung ohne erkennbaren Werkbezug — "
                            "fail-closed: unbekannt = ungelesen.",
                            "Werk benennen (dann greift die Grenze) oder Aussage entschärfen.",
                        ))
                    continue

                for w in aktive:
                    if w.voll:
                        continue  # alles erlebt → alles sagbar
                    jenseits = [b for b in baender if b > w.erlebt_bis]

                    # --- S2: Bandreferenz jenseits der Grenze + Spoilerwort -------------
                    if (jenseits or spaeter) and art == "hart":
                        funde.append(Fund(
                            VERSTOSS if not ist_vault else WARNUNG, "S2", w.titel, datei, i,
                            kurz(satz), f"{treffer} + Bd. {jenseits or 'später'}",
                            f"Handlung jenseits meiner Grenze ([[{w.titel}]]: {stufe_text(w)}).",
                            "Nur Neutralzone (§2) zu späteren Bänden — oder als "
                            "'🔒 Details zurückgehalten' ausweisen."
                            if not ist_vault else "In einen `> [!warning]- 🔒 SPOILER`-Block verschieben.",
                        ))
                    # --- S3: Spoilerwort bei unvollständig erlebtem Werk ----------------
                    elif art == "hart":
                        funde.append(Fund(
                            WARNUNG if ist_vault else VERSTOSS, "S3", w.titel, datei, i,
                            kurz(satz), treffer,
                            f"Handlungsverratende Formulierung zu [[{w.titel}]] "
                            f"({stufe_text(w)}) ohne Bandangabe — fail-closed.",
                            "Bandbezug klären; liegt er jenseits der Grenze, Aussage streichen.",
                        ))
                    # --- S6/weich: Urteil nötig ----------------------------------------
                    elif art == "weich" and (jenseits or spaeter or nur_blurb):
                        funde.append(Fund(
                            WARNUNG, "S6", w.titel, datei, i,
                            kurz(satz), treffer,
                            f"Verdächtige Formulierung im Bereich jenseits der Grenze "
                            f"([[{w.titel}]]: {stufe_text(w)}).",
                            "Vom `spoiler-guard` semantisch prüfen lassen.",
                        ))
        return dedupe(funde)


def stufe_text(w: Werk) -> str:
    if w.voll:
        return "komplett erlebt"
    if w.erlebt_bis <= 0:
        return f"nichts erlebt{f', Bd. {w.aktuell} läuft' if w.aktuell else ''}"
    return (f"Details bis Bd. {w.erlebt_bis}"
            + (f", Bd. {w.aktuell} läuft gerade" if w.aktuell else ""))


def kurz(s: str, n: int = 160) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def dedupe(funde: list) -> list:
    gesehen, out = set(), []
    for f in funde:
        k = (f.regel, f.werk, f.datei, f.zeile, f.treffer)
        if k not in gesehen:
            gesehen.add(k)
            out.append(f)
    rang = {VERSTOSS: 0, WARNUNG: 1}
    return sorted(out, key=lambda f: (rang.get(f.schwere, 2), f.datei, f.zeile))


def herkunft_raten(pfad: str) -> str:
    p = norm(pfad)
    if "empfehlungen" in p or "/kandidaten/" in p:
        return "empfehlung"
    if p.startswith("artifacts/") or "/artifacts/" in p or p.endswith(".html"):
        return "artefakt"
    if "vault/" in p:
        return "vault"
    return "unbekannt"


# --------------------------------------------------------------------------------------
# Ausgabe
# --------------------------------------------------------------------------------------
def bericht(funde: list, geprueft: list, lex_quelle: str, werke: list) -> str:
    z = []
    z.append("🔒 SPOILER-CHECK — Grenzen aus vault/Bibliothek/Werke/*.md, Lexikon aus " + lex_quelle)
    z.append("   geprüft: " + (", ".join(geprueft) if geprueft else "(nichts)"))
    verstoesse = [f for f in funde if f.schwere == VERSTOSS]
    warnungen = [f for f in funde if f.schwere == WARNUNG]
    if not funde:
        z.append("")
        z.append("✅ Sauber — keine Spoiler-Treffer.")
        z.append("   Hinweis: Deterministik fängt nur Eindeutiges. Für Paraphrasen den")
        z.append("   Agenten `spoiler-guard` laufen lassen (Pflicht vor jedem Publish).")
        return "\n".join(z)
    for f in verstoesse + warnungen:
        sym = "⛔" if f.schwere == VERSTOSS else "⚠️ "
        z.append("")
        z.append(f"{sym} [{f.regel}] {f.datei}:{f.zeile} · Werk: {f.werk}")
        z.append(f"   Stelle:  {f.stelle}")
        z.append(f"   Treffer: „{f.treffer}“")
        z.append(f"   Grund:   {f.grund}")
        z.append(f"   → {f.tipp}")
    z.append("")
    z.append(f"Ergebnis: {len(verstoesse)} VERSTOSS · {len(warnungen)} Warnung(en)")
    if verstoesse:
        z.append("⛔ Ausgabe/Publish blockiert. Erst bereinigen (Spoiler-Politik §2/§3/§7).")
    return "\n".join(z)


def grenzen_tabelle(werke: list) -> str:
    z = ["🔒 Spoiler-Grenzen (Quelle: Vault-Frontmatter)", ""]
    z.append(f"{'Werk':38} {'Stufe':22} {'erlebt':>7} {'läuft':>6} {'gesamt':>7}")
    z.append("-" * 84)
    for w in sorted(werke, key=lambda x: x.titel):
        z.append(f"{w.titel[:37]:38} {w.stufe[:21]:22} {w.erlebt_bis:>7} "
                 f"{w.aktuell or '-':>6} {w.gesamt or '?':>7}")
    z.append("")
    z.append("Alles nicht Gelistete = Freigabestufe `blurb` (fail-closed).")
    return "\n".join(z)


# --------------------------------------------------------------------------------------
# Gate-Stempel (damit der Stop-Hook weiß, ob ein Artefakt geprüft wurde)
# --------------------------------------------------------------------------------------
def stempel_pfad(root: Path) -> Path:
    return root / ".claude" / "state" / "spoiler-gate.json"


def lade_stempel(root: Path) -> dict:
    p = stempel_pfad(root)
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            return {}
    return {}


def schreibe_stempel(root: Path, eintraege: dict) -> None:
    p = stempel_pfad(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    daten = lade_stempel(root)
    daten.update(eintraege)
    p.write_text(json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16]


# --------------------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Deterministischer Spoiler-Linter für BookAI.")
    ap.add_argument("pfade", nargs="*", help="zu prüfende Dateien")
    ap.add_argument("--stdin", action="store_true", help="Text von stdin prüfen")
    ap.add_argument("--herkunft", default=None,
                    choices=["artefakt", "empfehlung", "kandidat", "chat", "subagent",
                             "vault", "unbekannt"],
                    help="Art der Ausgabe (bestimmt die Härte); sonst aus dem Pfad geraten")
    ap.add_argument("--json", action="store_true", help="Maschinenlesbare Ausgabe")
    ap.add_argument("--gate", action="store_true",
                    help="Ergebnis als Gate-Stempel ablegen (.claude/state/spoiler-gate.json)")
    ap.add_argument("--grenzen", action="store_true", help="nur die Grenzen ausgeben")
    ap.add_argument("--ausnahmen", action="store_true",
                    help="alle als `spoilerfrei` markierten Stellen auflisten (Audit)")
    ap.add_argument("--quiet", action="store_true", help="nur bei Treffern ausgeben")
    ap.add_argument("--root", default=None, help="Repo-Wurzel (Default: automatisch)")
    a = ap.parse_args(argv)

    root = Path(a.root) if a.root else Path(__file__).resolve().parent.parent
    if not (root / "vault").is_dir():
        print(f"Fehler: kein Vault unter {root}", file=sys.stderr)
        return 3

    pruefer = Pruefer(root)

    if a.grenzen:
        print(json.dumps([asdict(w) | {"stufe": w.stufe} for w in pruefer.werke],
                         ensure_ascii=False, indent=2) if a.json
              else grenzen_tabelle(pruefer.werke))
        return 0

    funde, geprueft, stempel = [], [], {}

    if a.stdin:
        text = sys.stdin.read()
        if text.strip():
            h = a.herkunft or "chat"
            funde += pruefer.pruefe(text, f"<stdin:{h}>", h)
            geprueft.append(f"<stdin:{h}>")

    for roh in a.pfade:
        p = Path(roh)
        if not p.is_absolute():
            p = (root / roh) if (root / roh).exists() else p
        if not p.exists() or p.is_dir():
            continue
        try:
            rel = str(p.resolve().relative_to(root))
        except ValueError:
            rel = str(p)
        h = a.herkunft or herkunft_raten(rel)
        inhalt = text_aus(p)
        f = pruefer.pruefe(inhalt, rel, h)
        funde += f
        geprueft.append(rel)
        if a.gate:
            hart = any(x.schwere == VERSTOSS for x in f)
            stempel[rel] = {
                "sha": sha(p.read_text(encoding="utf-8", errors="replace")),
                "status": VERSTOSS if hart else (WARNUNG if f else OK),
                "funde": len(f),
                "herkunft": h,
            }

    if not geprueft and not a.stdin:
        print("Nichts zu prüfen (keine Pfade übergeben).", file=sys.stderr)
        return 3

    if a.gate and stempel:
        schreibe_stempel(root, stempel)

    if a.ausnahmen:
        print(f"🅢 Als `spoilerfrei` ausgewiesene Stellen ({len(pruefer.ausnahmen)}) — "
              f"jede muss Neutralzone (§2) sein:")
        for x in pruefer.ausnahmen:
            print(f"   {x['datei']}:{x['zeile']}  {x['text']}")
        if not pruefer.ausnahmen:
            print("   (keine)")
        print()

    verstoesse = [f for f in funde if f.schwere == VERSTOSS]
    if a.json:
        print(json.dumps({
            "status": VERSTOSS if verstoesse else (WARNUNG if funde else OK),
            "geprueft": geprueft,
            "verstoesse": len(verstoesse),
            "warnungen": len(funde) - len(verstoesse),
            "funde": [asdict(f) for f in funde],
        }, ensure_ascii=False, indent=2))
    elif funde or not a.quiet:
        print(bericht(funde, geprueft, pruefer.lex["quelle"], pruefer.werke))

    return 2 if verstoesse else (1 if funde else 0)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
