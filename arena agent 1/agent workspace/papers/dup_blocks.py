#!/usr/bin/env python3
"""Find duplicated blocks WITHIN each paper (not across papers).

The framework check compared paper 1 against papers 2-5. This looks for the other
kind of duplication: the same passage appearing twice inside one file, which is
what concatenation leaves behind -- repeated abstracts, author-contribution
statements, AI-use declarations, data-availability paragraphs.

Reports the full text of each duplicated block so the decision can be made by
reading it rather than by trusting a similarity score.

Only near-identical blocks are reported (normalised equality after stripping
LaTeX commands and whitespace), so paraphrases are not flagged.
"""
import os
import re
import unicodedata
from collections import defaultdict

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

MIN_WORDS = 12


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)
    s = re.sub(r'[{}\\\$&_^~]', ' ', s)
    s = re.sub(r'[^a-zA-Z0-9 ]', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def blocks(lines):
    """Split into blocks on blank lines, remembering line spans."""
    out, cur, start = [], [], None
    for i, l in enumerate(lines):
        if l.strip():
            if start is None:
                start = i
            cur.append(l)
        else:
            if cur:
                out.append((start, i - 1, "\n".join(cur)))
            cur, start = [], None
    if cur:
        out.append((start, len(lines) - 1, "\n".join(cur)))
    return out


def main():
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        raw = open(p, encoding="utf-8", errors="replace").read().splitlines()
        lines = strip_comments("\n".join(raw)).splitlines()
        bs = blocks(lines)
        g = defaultdict(list)
        for a, b, t in bs:
            n = norm(t)
            if len(n.split()) >= MIN_WORDS:
                g[n].append((a, b, t))
        dups = {k: v for k, v in g.items() if len(v) > 1}
        if not dups:
            continue
        print("#" * 100)
        print("%s   %d duplicated block(s)" % (fn, len(dups)))
        for k, v in dups.items():
            print("\n" + "-" * 96)
            print("appears %d times, %d words each:" % (len(v), len(k.split())))
            for a, b, t in v:
                print("   [lines %d-%d of the live text]" % (a + 1, b + 1))
            print()
            print(re.sub(r'\n', ' ', v[0][2])[:1400])


if __name__ == "__main__":
    main()
