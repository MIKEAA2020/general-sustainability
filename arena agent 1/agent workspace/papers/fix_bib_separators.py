#!/usr/bin/env python3
"""Insert the missing blank line before each reference entry that currently runs
into the previous one, so every entry typesets as its own paragraph.

Operates on the ORIGINAL file (comments preserved) by matching the entry head
text to a line in the raw file, then inserting a single blank line above it.
Idempotent: re-running after the fix finds nothing to do.
"""
import os
import re
import sys

from bib_separators import HEAD
from label_fetch import UNITS, SUPPS, strip_comments, PAPERS


def targets(fn):
    """Return the raw-file line numbers that need a blank line inserted."""
    p = os.path.join(PAPERS, fn)
    raw = open(p, encoding="utf-8", errors="replace").read().splitlines()
    lines = strip_comments("\n".join(raw)).splitlines()

    idx = [i for i, l in enumerate(lines)
           if re.search(r'\\(sub)?section\*?\{References', l)]
    if not idx:
        return []
    body = lines[idx[-1] + 1:]
    end = next((i for i, l in enumerate(body)
                if re.search(r'\\end\{document\}', l)), len(body))
    body = body[:end]

    head_at = [i for i, l in enumerate(body) if HEAD.match(l)]
    if not head_at:
        return []
    first = head_at[0]
    unsep = [i for i in head_at
             if i != first
             and body[i - 1].strip()
             and not body[i - 1].rstrip().endswith(",")
             and not re.search(r'(?:\band|\&)\s*$', body[i - 1].rstrip())]

    # comment-stripping preserves line numbering, so body offset == raw offset
    return [idx[-1] + 1 + i for i in unsep]


def apply_fix(fn, dry=True):
    p = os.path.join(PAPERS, fn)
    ln = targets(fn)
    if not ln:
        return 0
    raw = open(p, encoding="utf-8", errors="replace").read().splitlines()
    # insert from the bottom up so earlier indices stay valid
    for n in sorted(ln, reverse=True):
        # n is a 0-based index into raw; insert a blank before it
        if raw[n - 1].strip():
            raw.insert(n, "")
    if not dry:
        open(p, "w", encoding="utf-8").write("\n".join(raw) + "\n")
    return len(ln)


def main():
    dry = "--apply" not in sys.argv
    print("mode: %s\n" % ("DRY RUN" if dry else "APPLYING"))
    total = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        n = apply_fix(fn, dry=dry)
        if n:
            total += n
            print("  %-52s %d blank line(s)" % (fn[:52], n))
    print("\ntotal: %d" % total)
    if dry:
        print("(re-run with --apply to write)")


if __name__ == "__main__":
    main()
