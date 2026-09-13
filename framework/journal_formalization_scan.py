#!/usr/bin/env python3
"""Journal-formalization scanner — automated guard against diary/meta/hedge regressions.

Scans a manuscript for:
  A. changelog / process-diary patterns (dates, "rerun", "post-hoc", "first execution",
     "updated", version numbers of the manuscript itself, changelog/audit/phase words);
  B. naive over-hedging (metaphor apologies, "map is not the territory" constructions,
     "goes without saying", "of course", "obviously", "to be clear", "interestingly", ...);
  C. informal / chat-register terms (coin-flip, kink, cash, dissolves, nailed, dumpster, ...);
  D. navigation / methodological self-description fragments ("this section shows",
     "as noted below we", "the rest of this paper", "we now turn to", ... — light
     navigational cross-references like "(Section 4.2)" are permitted and not flagged);
  E. references to earlier manuscript states ("v12/v13/v15", "previous version",
     "earlier draft", "superseded").

Legitimate uses are whitelisted: pre-registration language ("pre-registered",
"registered", "frozen" as in frozen specification), "companion" papers, archive file
paths, and the Data availability section's provenance file names.

Usage: python3 journal_formalization_scan.py <file.md> [--verbose]
Exit code 0 = no flagged patterns; 1 = flagged patterns listed.
"""
import re
import sys

WHITELIST_LINES = re.compile(
    r"`[^`]*`"                    # inline code / file paths
    r"|https?://\S+"              # URLs
)

PATTERNS = {
    "A-diary/changelog": [
        r"\b2026-\d\d-\d\d\b", r"\b20\d\d-\d\d-\d\d\b", r"\brerun\b", r"\bre-run\b",
        r"\bpost-hoc\b", r"\bpost hoc\b", r"\bfirst execution\b", r"\bexecuted \d",
        r"\bupdated (above|in the table|below)\b", r"\bwas updated\b", r"\bnow examined\b",
        r"\bnot yet run\b", r"\breported as not done\b", r"\breplacement files\b",
        r"\bverification-transcript\b", r"\bchangelog\b", r"\bPhase [A-Z]\b",
        r"\bphases?\b.*\bimplement", r"\bthis pass\b",
        r"\baudit (of|layer|campaign)\b", r"\baudits of\b",
        r"\bprovenance note\b", r"\bcorrected here\b", r"\bdisclosed as\b",
        r"\bunder the verification\b", r"\bsuperseded\b", r"\bprevious versions?\b",
    ],
    "B-naive-hedging": [
        r"\bgoes without saying\b", r"\bneedless to say\b", r"\bit should be noted\b",
        r"\bof course\b", r"\bobviously\b", r"\bto be clear\b", r"\binterestingly\b",
        r"\bremarkably\b", r"\bnot surprisingly\b", r"\bmap is not the territory\b",
        r"\bmetaphor\b", r"\bapology\b", r"\bas the saying goes\b", r"\bnaturally\b",
        r"\bneedless\b", r"\bself-evident\b", r"\bit goes without\b", r"\bworth noting\b",
    ],
    "C-informal/chat": [
        r"\bcoin-flip\b", r"\bcoin flip\b", r"\bkink\b", r"\bdissolves\b",
        r"\bstapled\b", r"\bnailed\b", r"\banyway\b", r"\bobviously\b", r"\bhonestly\b",
        r"\bstrawman\b", r"\bstraw-man\b", r"\bphantom\b", r"\bdiary\b", r"\bTODO\b",
        r"\bFIXME\b", r"\bneeds calibrating\b", r"\bas follows;\b",
    ],
    "D-navigation/self-description": [
        r"\bthis (section|paper|article) (shows|documents|demonstrates|aims to)\b",
        r"\bthe rest of this (paper|section)\b", r"\bwe now turn to\b",
        r"\bin what follows\b", r"\bas we shall see\b", r"\bas discussed above\b",
        r"\bas noted above\b", r"\brecall that\b", r"\bit is worth emphasizing\b",
        r"\bnote that\b", r"\bwe note that\b", r"\bthe point of this\b",
        r"\bshould be emphasized\b", r"\bwe emphasize\b",
    ],
    "E-manuscript-state-references": [
        r"\bv1[0-9]\b", r"\bv[0-9]+\b", r"\bmanuscript version\b",
        r"\bprevious version\b", r"\bearlier (draft|version)\b", r"\bolder version\b",
    ],
}

def main():
    path = sys.argv[1]
    verbose = "--verbose" in sys.argv
    text = open(path).read()
    lines = text.split("\n")
    flagged = []
    for line_no, line in enumerate(lines, 1):
        stripped = WHITELIST_LINES.sub(" ", line)
        for group, pats in PATTERNS.items():
            for p in pats:
                for m in re.finditer(p, stripped, re.IGNORECASE):
                    flagged.append((group, p, line_no, line.strip()[:110]))
    if flagged:
        seen = set()
        for group, p, line_no, ctx in flagged:
            key = (group, line_no, ctx)
            if key in seen:
                continue
            seen.add(key)
            print(f"[{group}] L{line_no}: {ctx}")
            if verbose:
                print(f"          pattern: {p}")
        print(f"\n{len(seen)} flagged lines")
        return 1
    print(f"{path}: 0 flagged patterns (diary/hedge/informal/navigation/version-state)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
