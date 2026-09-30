#!/usr/bin/env python3
"""Find duplicate bibliography entries within each unit's reference list.

These papers use hand-formatted reference lists -- no \\bibitem, no BibTeX -- so
no tool checks them for duplicates. A work cited twice under two different
typographic conventions is a real defect: the reference list shows one entry
twice and the reader cannot tell they are the same source.

Strategy: take the text from the References heading to the end of the document,
split it into entries on blank lines, then compare entries by a NORMALISED key
that is insensitive to the formatting differences these papers actually exhibit
(punctuation, \\emph vs \\textbf, full vs abbreviated journal, " and " vs ",",
presence of a DOI/URL, accented vs unaccented characters).

The key is the author surnames plus the leading digits of the year plus the
first digits of the title, which survives all of the above.
"""
import os
import re
import unicodedata
from collections import defaultdict

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)          # strip latex commands
    s = re.sub(r'[{}\\]', ' ', s)
    s = re.sub(r'https?://\S+|doi:\S*', ' ', s)
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def key(entry):
    n = norm(entry)
    # year: first 4-digit number 18xx-20xx
    y = re.search(r'\b(1[89]\d\d|20\d\d)\b', n)
    # crude author: text before the year
    auth = n[:y.start()] if y else n[:40]
    surnames = [w for w in auth.split() if len(w) > 2][:2]
    # title: after the year, first content words
    title = n[y.end():] if y else n
    tw = [w for w in title.split() if len(w) > 3][:3]
    return "|".join(surnames) + "#" + (y.group(1) if y else "?") + "#" + "".join(tw)


def main():
    total = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        lines = strip_comments(txt).splitlines()
        idx = [i for i, l in enumerate(lines)
               if re.search(r'\\(sub)?section\*?\{References|\\begin\{thebibliography\}', l)]
        if not idx:
            continue
        start = idx[-1]
        body = "\n".join(lines[start:])
        # stop at any \end{document} or appendix marker
        m = re.search(r'\\end\{document\}', body)
        if m:
            body = body[:m.start()]
        entries = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]
        # keep only entries that look like references (contain a year)
        entries = [e for e in entries if re.search(r'\b(1[89]\d\d|20\d\d)\b', e)]

        groups = defaultdict(list)
        for e in entries:
            groups[key(e)].append(e)

        dups = {k: v for k, v in groups.items() if len(v) > 1}
        if dups:
            print("=" * 100)
            print("%s  (%d entries scanned, %d duplicate groups)"
                  % (fn, len(entries), len(dups)))
            for k, v in dups.items():
                total += len(v) - 1
                print("\n  [%s]  x%d" % (k, len(v)))
                for e in v:
                    print("     - " + re.sub(r'\s+', ' ', e)[:170])
    print("=" * 100)
    print("redundant bibliography entries: %d" % total)


if __name__ == "__main__":
    main()
