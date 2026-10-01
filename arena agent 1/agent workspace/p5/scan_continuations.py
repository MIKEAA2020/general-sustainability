#!/usr/bin/env python3
"""REPORT-ONLY detector for detached bibliography tails (the K gap).

The shipped K.split-refs rule fires only when a fragment has NO year AND opens
with one of ~18 hardcoded journal/publisher names (TAIL_LEAD). Three of the
seven tails repaired in paper09 v32 were invisible to it:

    "Water Data for Texas, well 6837203 (J-17). https://..."  opens with a title
    "Geological Survey Circular 1186, Denver, CO."            opens with a title
    "Fish. Res. 240, 105959."                                 carries a year

This is a SECOND SIGNAL, run across the corpus in report-only mode so its
false-positive rate can be measured before anything is made fatal. It does not
change the gate and does not fail anything.

The question it asks is the one the shipped rule does not: could this fragment
stand alone as a reference? A standalone reference needs an author-like opening
and a year. A fragment that has neither, or that only pretends to, is a tail.

Usage:  python3 scan_continuations.py [--all]   (--all = show clean files too)
"""
from __future__ import annotations

import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import phase0_scan as p0

PAPERS = "/home/user/papers/"

YEAR = re.compile(r'\b(?:1[89]\d{2}|20\d{2})\b')

# an author-like opening: "Surname,", "Surname, A. B.,", "{\AA}str{\"o}m,",
# or a corporate author "DFO.", "World Bank.", "Texas Water Development Board."
AUTHORISH = re.compile(
    r'^(?:\{?\\?[A-ZÄÖÅÉ]|\{)'
    r'(?:[^{},]{0,60}?),\s*(?:[A-Z]\.|[A-Z][a-z]+|and\s|\(|\d{4}|et)'
    r'|^(?:[A-Z][\w\'\-]*(?:\s+[A-Z][\w\'\-]*){0,4})\.\s')

# a bare publisher/city tail: 2-5 capitalised words, comma-separated, no year.
# "Birkhaeuser, Boston."  "Prentice-Hall, Upper Saddle River, NJ."
# "Cambridge University Press, Cambridge."  "Fisheries and Oceans Canada, Ottawa."
PLACE_TAIL = re.compile(
    r'^[A-ZÄÖÅ][\w\'\-]*(?:\s+(?:and|of|for|the|de|van)\s+[a-zA-Z\'\-]*'
    r'|\s+[A-Z][\w\'\-]*){0,4}'
    r'(?:,\s*[A-ZÄÖÅ][\w\'\-]*(?:\s+[A-Z][\w\'\-]*){0,3}){1,3}\.?$')

# the previous entry is left grammatically incomplete -- it ends on an
# abbreviation or an initial, so the next fragment is probably its tail
DANGLING = re.compile(
    r'(?:U\.S\.|U\.K\.|N\.J\.|pp\.| eds?\.|et al\.|'
    r'(?:^|\s)[A-Z]\.(?:\s?[A-Z]\.)*|Vol\.|No\.|doi:|https?://\S+)\s*$')

# opens mid-sentence: lowercase, or a continuation word
CONTINUATION = re.compile(r'^(?:and|of|for|the|in|with|to|from|[a-z])')


def is_junk(f: str) -> bool:
    """LaTeX noise that ref_entries() picks up but is not a bibliography entry."""
    if len(f) < 15:
        return True
    if f[0] in "\\{}":
        return True
    if not re.search(r'[A-Za-z]{4}', f):
        return True
    if "." not in f:
        return True
    return False


def signals(frag: str, prev: str) -> list:
    """Which independent signals say this fragment is a tail?

    D is deliberately NOT a standalone signal: it fires on 77% of all
    candidates because plenty of legitimate entries follow an entry that ends
    in an abbreviation or a URL. It is only ever reported as a CONFIRMATION of
    A/B/C, never on its own.
    """
    out = []
    f = frag.strip()
    if not f or is_junk(f):
        return out

    if p0.TAIL_LEAD.match(f) and not YEAR.search(f):
        out.append("A:shipped-rule")

    if not YEAR.search(f) and not AUTHORISH.match(f) and len(f) < 130:
        out.append("B:no-year+no-author")

    if PLACE_TAIL.match(f) and not YEAR.search(f):
        out.append("C:place-tail")

    # E (continuation-word) was removed after triage: 3 hits, all false
    # positives, all "von Neumann, J. (1928)..." -- a lowercase nobiliary
    # particle is not evidence of a tail.

    # confirming only -- never sufficient on its own
    if out and prev.strip() and DANGLING.search(prev.strip()):
        out.append("+D:prev-dangling")

    return out


def main() -> int:
    show_all = "--all" in sys.argv
    files = sorted(f for f in os.listdir(PAPERS) if f.endswith(".tex"))
    live = p0.live_heads(files)
    rows = []
    for fn in files:
        raw = io.open(PAPERS + fn, encoding="utf-8", errors="replace").read()
        c = p0.strip_comments(raw)
        ents = p0.ref_entries(c)
        status = 'LIVE' if fn in live else 'superseded'
        for i, (ln, e) in enumerate(ents):
            prev = ents[i - 1][1] if i else ""
            sig = signals(e, prev)
            if sig:
                rows.append((fn, ln, e, sig, status))

    # group by which signals fired, so the false-positive rate is per-signal
    from collections import Counter, defaultdict
    bysig = Counter()
    for _, _, _, sig, _ in rows:
        for s in sig:
            bysig[s] += 1

    print("REPORT-ONLY — detached-tail second signal")
    print("scanned %d files, %d candidate fragments\n" % (len(files), len(rows)))
    print("hits by signal (a fragment can fire several):")
    for s, n in bysig.most_common():
        print("   %-24s %3d" % (s, n))
    print()

    # first: what the SHIPPED rule already catches (signal A alone)
    only_a = [r for r in rows if r[3] == ["A:shipped-rule"]]
    new_only = [r for r in rows if r[3] != ["A:shipped-rule"]]
    print("already caught by the shipped rule : %d" % len(only_a))
    print("NEWLY surfaced by the second signal: %d\n" % len(new_only))

    cur = None
    for fn, ln, e, sig, st in sorted(new_only):
        if fn != cur:
            cur = fn
            print("--- %s" % fn)
        print("    L%-6d %-40s %-28s %s" % (ln, e[:40], ",".join(sig), st))

    live_rows = [r for r in rows if r[4] == 'LIVE']
    print("ON LIVE HEADS: %d candidate fragment(s)" % len(live_rows))
    for fn, ln, e, sig, st in sorted(live_rows):
        print("   %-42s L%-6d %-34s %s" % (fn, ln, e[:34], ",".join(sig)))
    print()

    if show_all:
        print("\n--- also flagged by the shipped rule ---")
        for fn, ln, e, sig, st in sorted(only_a):
            print("    %-46s L%-6d %-44s %s" % (fn, ln, e[:44], st))
    return 0


if __name__ == "__main__":
    sys.exit(main())
