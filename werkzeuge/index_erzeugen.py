#!/usr/bin/env python3
"""Erzeugt wissensbasis/index.json neu aus den vorhandenen Modul-Dateien.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python3 werkzeuge/index_erzeugen.py

Die bereits eingetragene basis_url bleibt erhalten. Nach jeder inhaltlichen
Aenderung an den Modulen dieses Werkzeug ausfuehren und das Ergebnis committen.
"""
import os
import re
import json
import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(REPO, "wissensbasis")
INDEX = os.path.join(BASE, "index.json")
PLATZHALTER = "https://raw.githubusercontent.com/__OWNER__/__REPO__/main/wissensbasis/"

stand_line = re.compile(r"^\**\s*Stand\b.*?[: ]\s*\**\s*([A-Za-zäöüÄÖÜ]+\.?\s*20\d{2})", re.IGNORECASE)
month = r"(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s*20\d{2}"
h1_re = re.compile(r"^#\s+(.+)$")
h1_month = re.compile(month, re.IGNORECASE)


def head(path, n=30):
    with open(path, encoding="utf-8") as f:
        return [next(f, "") for _ in range(n)]


def titel_stand(path):
    titel = stand = None
    for s in (l.strip() for l in head(path)):
        if titel is None:
            m = h1_re.match(s)
            if m:
                titel = m.group(1).strip()
        if stand is None:
            m = stand_line.search(s)
            if m:
                stand = m.group(1).strip()
    return titel, stand


def main():
    # bestehende basis_url bewahren
    basis_url = PLATZHALTER
    if os.path.exists(INDEX):
        try:
            with open(INDEX, encoding="utf-8") as f:
                basis_url = json.load(f).get("basis_url", PLATZHALTER)
        except Exception:
            pass

    # Modul-Stand aus Index/README je Modulordner
    modul_stand = {}
    for d in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, d)
        if not os.path.isdir(p):
            continue
        cand = [f for f in sorted(os.listdir(p)) if f.lower().endswith(".md")
                and (f.lower().startswith("00") or "index" in f.lower() or "readme" in f.lower())]
        st = None
        for f in cand:
            _, s = titel_stand(os.path.join(p, f))
            if s:
                st = s
                break
            for line in head(os.path.join(p, f)):
                m = h1_month.search(line)
                if m:
                    st = m.group(0)
                    break
            if st:
                break
        if st:
            modul_stand[d] = st

    entries = []
    for root, dirs, files in os.walk(BASE):
        dirs.sort()
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), BASE).replace("\\", "/")
            modul = rel.split("/")[0] if "/" in rel else "(wurzel)"
            titel, stand = titel_stand(os.path.join(root, fn))
            if not stand:
                stand = modul_stand.get(modul, "unbekannt")
            entries.append({"modul": modul, "datei": rel,
                            "titel": titel or fn[:-3], "stand": stand})

    index = {
        "basis_url": basis_url,
        "generiert_am": datetime.date.today().isoformat(),
        "anzahl_module": len(entries),
        "hinweis": "Basis-URL im Feld basis_url. Bei einem Repo-Umzug hier und in skills/socialmedia-agentur/SKILL.md anpassen.",
        "modul_stand": modul_stand,
        "module": entries,
    }
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"index.json neu erzeugt: {len(entries)} Module, basis_url = {basis_url}")


if __name__ == "__main__":
    main()
