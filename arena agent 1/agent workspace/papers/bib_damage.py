#!/usr/bin/env python3
"""Detect structural damage in the hand-formatted reference lists.

Two signatures of a botched merge, both visible without compiling:

  A. GLUED ENTRIES -- one line carries two distinct reference heads. Matched as
     a surname-year pattern appearing twice on the same line.

  B. ORDER BREAKS -- the reference list is alphabetical by leading surname, so a
     step backwards marks where a second list was appended or entries were
     shuffled.

Also reports orphan fragments: short lines beginning with a capital that carry
no year anywhere in the entry.
"""
import os
import re
from collections import defaultdict

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

# a reference head: Surname, A.B., ... <year>
HEAD = re.compile(r'[A-ZÅÄÖØÆ][\w\-\'\`]{2,}(?:,|\.)?\s+[A-Z]\.')


def entries_of(p):
    txt = open(p, encoding="utf-8", errors="replace").read()
    lines = strip_comments(txt).splitlines()
    idx = [i for i, l in enumerate(lines)
           if re.search(r'\\(sub)?section\*?\{References', l)]
    if not idx:
        return [], []
    body_lines = lines[idx[-1]:]
    body = "\n".join(body_lines)
    m = re.search(r'\\end\{document\}', body)
    if m:
        body = body[:m.start()]
    ents = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]
    return ents, idx


def leading_name(e):
    s = e.lstrip()
    s = re.sub(r'^\\(?:emph|textbf|textit)\{', '', s)
    m = re.match(r"([A-ZÅÄÖØÆa-zÅäöøæ][\w\-\'\{\}\\\.]{1,})", s)
    if not m:
        return None
    w = m.group(1)
    w = re.sub(r'[\\\.\{\}]', '', w).strip()
    return w.lower() or None


def main():
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        ents, idx = entries_of(p)
        if not ents:
            continue
        ref_start = idx[-1] + 1

        print("=" * 100)
        print("%s   (References at L%d, %d entries)"
              % (fn, ref_start, len(ents)))

        # --- A. glued entries -------------------------------------------
        glued = []
        for e in ents:
            flat = re.sub(r'\s+', ' ', e)
            heads = HEAD.findall(flat)
            if len(heads) >= 2:
                # only flag if a year-boundary sits between them
                ys = re.findall(r'\b(1[89]\d\d|20\d\d)\b', flat)
                if len(ys) >= 2:
                    glued.append(flat)
        if glued:
            print("\n  GLUED ENTRIES: %d" % len(glued))
            for g in glued:
                print("     " + g[:180])

        # --- B. order breaks --------------------------------------------
        names = [(i, leading_name(e)) for i, e in enumerate(ents)]
        names = [(i, n) for i, n in names if n]
        breaks = []
        for a in range(1, len(names)):
            prev = names[a - 1][1]
            cur = names[a][1]
            if prev and cur and cur < prev:
                breaks.append((names[a][0], prev, cur))
        if breaks:
            print("\n  ALPHABETICAL ORDER BREAKS: %d" % len(breaks))
            for i, prev, cur in breaks:
                frag = re.sub(r'\s+', ' ', ents[i])[:95]
                print("     entry %-3d  '%s' -> '%s'   %s"
                      % (i, prev, cur, frag))

        # --- C. orphan fragments ----------------------------------------
        orph = []
        for e in ents:
            flat = re.sub(r'\s+', ' ', e)
            if not re.search(r'\b(1[89]\d\d|20\d\d)\b', flat) and len(flat) > 8:
                if re.match(r'^[A-Z]', flat):
                    orph.append(flat)
        if orph:
            print("\n  FRAGMENTS WITH NO YEAR: %d" % len(orph))
            for o in orph:
                print("     " + o[:120])


if __name__ == "__main__":
    main()
