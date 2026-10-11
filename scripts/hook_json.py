#!/usr/bin/env python3
"""
hook_json.py — JSON-Helfer für die Hook-Skripte, ersetzt `jq` (2026-10-11).

Warum: Unter Windows fehlt `jq` meist. Die Spoiler-Hooks prüften dann still gar
nichts (`command -v jq || exit 0`). Python ist ohnehin Pflicht (spoiler_check.py),
also lesen und schreiben die Hooks ihr JSON jetzt hierüber.

Lesen (JSON auf stdin, erster nicht-leerer Pfad gewinnt, sonst --standard):
    hook_json.py feld tool_name
    hook_json.py feld tool_input.file_path tool_input.path
    hook_json.py feld 'tool_input.edits[].new_string'      # Liste → mit \\n verbunden
    hook_json.py feld tool_input.action --standard publish

Schreiben (Text auf stdin):
    hook_json.py ausgabe sessionstart   → hookSpecificOutput.additionalContext
    hook_json.py ausgabe deny           → PreToolUse permissionDecision "deny" + Grund
    hook_json.py ausgabe hinweis        → PreToolUse nur additionalContext (keine Entscheidung)
    hook_json.py ausgabe system         → systemMessage

Nur Standardbibliothek. Fehler → leere Ausgabe, Exit 0 (ein Hook darf nie die Arbeit sprengen).
"""
import json
import sys


def lies(daten, pfad):
    teile = pfad.split(".")
    werte = [daten]
    for teil in teile:
        neu = []
        liste = teil.endswith("[]")
        name = teil[:-2] if liste else teil
        for w in werte:
            if not isinstance(w, dict) or name not in w:
                continue
            x = w[name]
            if liste:
                neu.extend(x if isinstance(x, list) else [])
            else:
                neu.append(x)
        werte = neu
    texte = [w if isinstance(w, str) else json.dumps(w, ensure_ascii=False) for w in werte if w not in (None, "")]
    return "\n".join(texte)


def main():
    for strom in (sys.stdin, sys.stdout):
        if hasattr(strom, "reconfigure"):
            strom.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    if not args:
        return 0
    eingabe = sys.stdin.read()

    if args[0] == "feld":
        standard = ""
        if "--standard" in args:
            i = args.index("--standard")
            standard = args[i + 1] if i + 1 < len(args) else ""
            args = args[:i] + args[i + 2:]
        try:
            daten = json.loads(eingabe) if eingabe.strip() else {}
        except ValueError:
            daten = {}
        for pfad in args[1:]:
            wert = lies(daten, pfad)
            if wert:
                sys.stdout.write(wert)
                return 0
        sys.stdout.write(standard)
        return 0

    if args[0] == "ausgabe" and len(args) > 1:
        art, text = args[1], eingabe
        if art == "sessionstart":
            obj = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}
        elif art == "deny":
            obj = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                          "permissionDecisionReason": text}}
        elif art == "hinweis":
            # Bewusst OHNE permissionDecision: normaler Ablauf, nur Kontext für Claude.
            # Früher stand hier "defer" — laut Doku in interaktiven Sitzungen wirkungslos,
            # und additionalContext wird bei "defer" verworfen (geprüft 2026-10-11,
            # https://code.claude.com/docs/en/hooks.md).
            obj = {"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": text}}
        elif art == "system":
            obj = {"systemMessage": text}
        else:
            return 0
        sys.stdout.write(json.dumps(obj, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
