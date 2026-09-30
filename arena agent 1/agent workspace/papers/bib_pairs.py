#!/usr/bin/env python3
"""Dump the full text of every duplicate bibliography group, with the line range
of each copy, so the more complete entry can be kept and the other removed.
"""
import os
import re
from collections import defaultdict

from bib_dupes import key
from label_fetch import UNITS, SUPPS, strip_comments, PAPERS


def main():
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        raw = open(p, encoding="utf-8", errors="replace").read()
        lines = strip_comments(raw).splitlines()
        idx = [i for i, l in enumerate(lines)
               if re.search(r'\\(sub)?section\*?\{References', l)]
        if not idx:
            continue
        body_lines = lines[idx[-1]:]
        body = "\n".join(body_lines)
        m = re.search(r'\\end\{document\}', body)
        if m:
            body = body[:m.start()]
        entries = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]
        entries = [e for e in entries if re.search(r'\b(1[89]\d\d|20\d\d)\b', e)]

        g = defaultdict(list)
        for e in entries:
            g[key(e)].append(e)
        dups = {k: v for k, v in g.items() if len(v) > 1}
        if not dups:
            continue

        print("#" * 100)
        print(fn)
        for k, v in dups.items():
            print("\n  GROUP  %s" % k)
            for e in v:
                # locate it in the raw file
                flat = re.sub(r'\s+', ' ', e)[:60]
                ln = None
                for i, l in enumerate(open(p, encoding="utf-8",
                                           errors="replace")):
                    if flat[:50] in re.sub(r'\s+', ' ', l):
                        ln = i + 1
                        break
                print("    [L%s] len=%d" % (ln, len(e)))
                print("       %s" % re.sub(r'\s+', ' ', e))


if __name__ == "__main__":
    main()
