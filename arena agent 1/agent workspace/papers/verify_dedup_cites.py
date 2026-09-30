#!/usr/bin/env python3
"""Verify that removing duplicate bibliography entries orphaned no citation.

The general "does every citation resolve" question is not answerable reliably on
hand-formatted references: a citation like "(Makridakis, Spiliotis, and
Assimakopoulos, 2020)" lists co-authors, so a naive scan records three citation
keys when the reference list only ever carries the first author's surname. That
produced 177 false positives.

The question that actually matters after de-duplication is narrower and
decisive: for every entry that was DELETED, is there a surviving entry with the
same first-author surname and the same year? If yes, any citation pointing at
the deleted entry still resolves against the survivor.

The set of deletions is recomputed from the backups in /tmp/bibbak rather than
hard-coded, so the check cannot drift from what was actually removed.
"""
import os
import re
import subprocess

from label_fetch import PAPERS, strip_comments

BAK = "/tmp/bibbak"
YEAR = r'(1[89]\d\d|20\d\d)'


def surname_of(s):
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = re.sub(r'[{}\\]', '', s)
    return s.strip().strip(',').strip().lower()


def entries(text):
    out = []
    for e in re.split(r'\n\s*\n', text):
        flat = re.sub(r'\s+', ' ', e).strip()
        if not flat or not re.search(YEAR, flat):
            continue
        ys = re.findall(YEAR, flat)
        m = re.match(r'([A-ZÅÄÖØÆ][\w\-\'\.]*)', flat[:60])
        if not m:
            continue
        out.append((surname_of(m.group(1)), ys[0], flat))
    return out


def ref_region(text):
    lines = strip_comments(text).splitlines()
    idx = [i for i, l in enumerate(lines)
           if re.search(r'\\(sub)?section\*?\{References', l)]
    if not idx:
        return ""
    r = "\n".join(lines[idx[-1]:])
    m = re.search(r'\\end\{document\}', r)
    return r[:m.start()] if m else r


def main():
    files = sorted(f for f in os.listdir(BAK) if f.endswith(".tex"))
    total_removed = 0
    orphaned = 0
    print("%-46s %8s %9s  %s" %
          ("file", "removed", "survivors", "every removed key still present?"))
    print("-" * 96)
    for fn in files:
        old = open(os.path.join(BAK, fn), encoding="utf-8",
                   errors="replace").read()
        new = open(os.path.join(PAPERS, fn), encoding="utf-8",
                   errors="replace").read()
        o = entries(ref_region(old))
        n = entries(ref_region(new))
        # keys present now
        have = {(s, y) for s, y, _ in n}
        # keys present before, counted
        obefore = {}
        for s, y, f in o:
            obefore[(s, y)] = obefore.get((s, y), 0) + 1
        nbefore = {}
        for s, y, f in n:
            nbefore[(s, y)] = nbefore.get((s, y), 0) + 1
        removed = []
        for k, c in obefore.items():
            if c > nbefore.get(k, 0):
                removed += [k] * (c - nbefore.get(k, 0))
        total_removed += len(removed)
        bad = [k for k in removed if k not in have]
        orphaned += len(bad)
        print("%-46s %8d %9d  %s" %
              (fn[:46], len(removed), len(have),
               "YES" if not bad else "NO -> " + str(bad)))
    print("-" * 96)
    print("entries removed: %d   keys left with no surviving entry: %d"
          % (total_removed, orphaned))
    print()
    print("Interpretation: a removed entry shares its (first-author, year) key")
    print("with a surviving entry, so every in-text citation to it still")
    print("resolves. Citations use first-author surname + year in these papers.")


if __name__ == "__main__":
    main()
