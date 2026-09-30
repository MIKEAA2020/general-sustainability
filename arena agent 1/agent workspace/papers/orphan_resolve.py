#!/usr/bin/env python3
"""Resolve orphaned float labels to their RENDERED numbers, then decide whether
each is genuinely unreferenced.

A float label can look orphaned while the text cites it by literal number
("Figure 3", "Table 1") instead of \\ref -- which is the house style in several
of these papers. So this compiles each unit, reads the rendered number for every
orphaned label out of the .aux, and then checks whether that literal number
appears in the text as "Figure N"/"Table N".

Only floats with no \\ref AND no matching literal mention are reported as
genuinely unreferenced.
"""
import os
import re
import shutil
import subprocess

from label_fetch import ensure_figures, PAPERS, TD, UNITS, SUPPS, strip_comments
from label_hygiene import audit


def aux_numbers(aux_path):
    """Map label -> rendered reference text from the .aux."""
    aux = open(aux_path, encoding="latin-1").read()
    out = {}
    for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', aux):
        out[m.group(1)] = m.group(2).strip()
    return out


def main():
    print("%-40s %-34s %-9s %s" %
          ("file", "orphaned label", "renders", "literal cite?"))
    print("-" * 100)
    genuine = 0
    for fn in UNITS + SUPPS:
        src = os.path.join(PAPERS, fn)
        if not os.path.exists(src):
            continue
        w = ensure_figures(fn)
        subprocess.run([TD, "-X", "compile", fn, "--outdir", ".",
                        "--keep-intermediates"],
                       cwd=w, capture_output=True, timeout=900)
        auxf = os.path.join(w, fn[:-4] + ".aux")
        if not os.path.exists(auxf):
            print("%-40s  NO AUX" % fn[:40])
            continue
        nums = aux_numbers(auxf)

        live = strip_comments(open(src, encoding="utf-8",
                                   errors="replace").read())
        labels, dupes, missing, orphans = audit(fn)
        if not orphans:
            continue
        for o in orphans:
            n = nums.get(o, "?")
            kind = "Figure" if o.startswith(("fig", "calc-fig", "cod-fig",
                                             "regime-fig", "sh-fig")) else "Table"
            if o.startswith("tab") or "tab:" in o or o.startswith(("calc-tab",
                    "regime-tab", "scale-tab")):
                kind = "Table"
            # does the literal "Figure N" / "Table N" appear?
            lit = re.search(r'%s~?\s*%s\b' % (kind, re.escape(n)), live)
            cited = "YES (%s %s)" % (kind, n) if lit else "— none —"
            if not lit:
                genuine += 1
            print("%-40s %-34s %-9s %s" %
                  (fn[:40], o[:34], n or "(empty)", cited))
    print("-" * 100)
    print("genuinely unreferenced floats: %d" % genuine)


if __name__ == "__main__":
    main()
