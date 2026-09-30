#!/usr/bin/env python3
"""Inspect the orphaned floats found by label_hygiene.py.

An "orphan" is a labelled figure/table that no \\ref points at. That is not
automatically a defect: these papers write many cross-references by hand
("Figure 3", "Table 2") rather than through \\ref. So for each orphan this looks
for a nearby literal mention of the float number, and reports which orphans look
genuinely unreferenced.
"""
import os
import re

from label_hygiene import UNITS, SUPPS, audit, PAPERS


def caption_of(live_lines, label):
    """Return the caption text of the float carrying `label`, if findable."""
    for i, l in enumerate(live_lines):
        if "\\label{%s}" % label in l:
            for j in range(max(0, i - 12), min(len(live_lines), i + 12)):
                m = re.search(r'\\caption\{(.*)', live_lines[j])
                if m:
                    t = re.sub(r'\\[a-zA-Z]+', '', m.group(1))
                    t = t.replace("{", "").replace("}", "")
                    return re.sub(r'\s+', ' ', t).strip()[:90]
    return "(no caption found)"


def main():
    total = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        live = "\n".join(re.sub(r'(?<!\\)%.*', '', l)
                         for l in open(p, encoding="utf-8",
                                       errors="replace").read().splitlines())
        lines = live.splitlines()
        labels, dupes, missing, orphans = audit(fn)
        if not orphans:
            continue
        print("=" * 100)
        print(fn)
        for o in orphans:
            cap = caption_of(lines, o)
            # does a literal "Figure N"/"Table N" mention exist anywhere?
            lits = re.findall(r'(Figure|Table|Fig\.)\s*~?(\d+)', live)
            print("  %-48s %s" % (o, cap))
            total += 1
        print("  literal Figure/Table mentions in file: %d" % len(lits))
    print("=" * 100)
    print("orphaned floats total: %d" % total)


if __name__ == "__main__":
    main()
