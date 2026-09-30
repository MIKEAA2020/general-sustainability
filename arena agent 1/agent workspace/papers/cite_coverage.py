#!/usr/bin/env python3
"""Check that every in-text author-year citation still has a matching entry in
the reference list, after the duplicate entries were removed.

These papers cite by hand -- "(Abaee, 2026)", "Moxnes (1998)", "K\\\"unsch
(1989)" -- with no \\cite and no BibTeX, so nothing checks this automatically and
a deleted bibliography entry would silently leave a citation pointing at nothing.

For each file: collect the (surname, year) pairs cited in the body, collect the
(surname, year) pairs present in the reference list, and report cited pairs with
no reference-list counterpart.
"""
import os
import re

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

YEAR = r'(1[89]\d\d|20\d\d)'


def surname_of(s):
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = re.sub(r'[{}\\]', '', s)
    s = s.strip().strip(',').strip()
    return s.lower()


def ref_pairs(body):
    """(surname, year) for every reference-list entry."""
    out = set()
    for e in re.split(r'\n\s*\n', body):
        flat = re.sub(r'\s+', ' ', e).strip()
        if not flat:
            continue
        ys = re.findall(YEAR, flat)
        if not ys:
            continue
        head = flat[:60]
        m = re.match(r'([A-ZÅÄÖØÆ][\w\-\'\.]*)', head)
        if not m:
            continue
        sur = surname_of(m.group(1))
        for y in ys:
            out.add((sur, y))
    return out


def cite_pairs(live):
    """(surname, year) for every in-text citation."""
    out = set()
    # (Surname, 2020) and (Surname and Other, 2020)
    for m in re.finditer(r'\(([A-ZÅÄÖØÆ][^()]{0,120}?),?\s*' + YEAR + r'\)', live):
        inner = m.group(1)
        for part in re.split(r'\band\b|&|;', inner):
            part = part.strip().rstrip(',').strip()
            mm = re.search(r'([A-ZÅÄÖØÆ][\w\-\'\.]*)\s*$', part)
            if mm:
                out.add((surname_of(mm.group(1)), m.group(2)))
    # Surname (2020)
    for m in re.finditer(r'([A-ZÅÄÖØÆ][\w\-\'\.]*)\s*\(' + YEAR + r'\)', live):
        out.add((surname_of(m.group(1)), m.group(2)))
    # Surname, A., 2020.  (reference-list style, in case a ref sits in body)
    return out


def main():
    problems = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        live = strip_comments(txt)
        lines = live.splitlines()
        idx = [i for i, l in enumerate(lines)
               if re.search(r'\\(sub)?section\*?\{References', l)]
        if not idx:
            continue
        cut = idx[-1]
        body = live[:sum(len(l) + 1 for l in lines[:cut])]
        refs = "\n".join(lines[cut:])
        m = re.search(r'\\end\{document\}', refs)
        if m:
            refs = refs[:m.start()]

        rp = ref_pairs(refs)
        cp = cite_pairs(body)
        # only surname+year pairs; ignore years that are not in reference keys
        missing = sorted((s, y) for s, y in cp
                         if y not in {yy for _, yy in rp}
                         or not any(ss == s and yy == y for ss, yy in rp))
        # a citation may be satisfied by ANY entry of that year if the surname
        # failed to parse; report only surname+year mismatches
        missing = sorted((s, y) for s, y in cp if (s, y) not in rp)
        if missing:
            problems += len(missing)
            print("=" * 92)
            print(fn)
            for s, y in missing:
                print("   cited but not in reference list: %s %s" % (s, y))
    print("=" * 92)
    print("cited-but-missing pairs: %d" % problems)
    print("(note: hand-formatted lists and name variants such as 'et al.' can "
          "produce some false positives; each hit needs a look)")


if __name__ == "__main__":
    main()
