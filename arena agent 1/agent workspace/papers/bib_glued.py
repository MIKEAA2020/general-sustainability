#!/usr/bin/env python3
"""Tight detector for GLUED bibliography entries.

A glued entry is two references merged onto one line: the first entry runs to its
natural end (a DOI, or a page range), and the next entry's author head starts
immediately after on the same line instead of on a new line.

The earlier detector flagged every multi-author entry because "In: Proceedings
(2009)" supplies a second year and each "Surname, A.B." supplies a second head.
This version requires the second head to appear AFTER an end-of-entry marker --
a doi:, or a terminal page range -- and excludes heads introduced by "In:",
"Edited by", proceedings editors and similar.
"""
import os
import re

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

# an author head that starts an entry: Surname, A. or Surname, A.B.,
NEW_HEAD = re.compile(
    r'(?:doi:\S+|pp\.~\d+|\b\d+--\d+\.)\s+'
    r'([A-Z][\w\-\']{2,},\s+(?:[A-Z]\.[,]?\s*){1,})'
)

# contexts where a following author-list is legitimate, not a new entry
LEGIT = re.compile(r'\b(?:In|in|Edited by|eds?\.|Edited)\b\s*:?\s*$')


def main():
    total = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8", errors="replace").read()
        lines = strip_comments(txt).splitlines()
        idx = [i for i, l in enumerate(lines)
               if re.search(r'\\(sub)?section\*?\{References', l)]
        if not idx:
            continue
        body = "\n".join(lines[idx[-1]:])
        m = re.search(r'\\end\{document\}', body)
        if m:
            body = body[:m.start()]
        ents = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]

        hits = []
        for e in ents:
            flat = re.sub(r'\s+', ' ', e)
            for m in NEW_HEAD.finditer(flat):
                before = flat[:m.start()]
                if LEGIT.search(before[-14:]):
                    continue
                hits.append((flat, m.group(1).strip()))
        if hits:
            print("=" * 100)
            print("%s   (%d glued candidates)" % (fn, len(hits)))
            for flat, head in hits:
                total += 1
                i = flat.find(head)
                print("\n   ...%s [>>> %s] %s"
                      % (flat[max(0, i - 80):i], head, flat[i + len(head):i + len(head) + 90]))
    print("=" * 100)
    print("glued-entry candidates: %d" % total)


if __name__ == "__main__":
    main()
