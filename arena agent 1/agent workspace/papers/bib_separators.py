#!/usr/bin/env python3
"""Check whether each reference list separates its entries with blank lines.

In LaTeX a single newline is just a space. If a hand-formatted reference list has
entries on consecutive lines with no blank line between them, the whole list
typesets as ONE paragraph instead of one paragraph per entry -- the references
run together into a blob.

An entry head is identified precisely: a line starting with a surname followed by
a comma and one or more initials ("Calafiore, G." / "Campi, M.C. and"), which
avoids matching wrapped continuation lines that merely start with a capital.
"""
import os
import re

from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

# surname, then comma, then initials -- optionally wrapped in \emph/\textbf
HEAD = re.compile(
    r"^(?:\\(?:emph|textbf|textit)\{)?"
    r"[A-ZÅÄÖØÆ][\w\-\'\{\}\\\.]{1,30},"
    r"(?:\s+[A-Z]\.(?:[,]?\s*[A-Z]\.)*)"
)


def main():
    print("%-46s %7s %7s  %s" % ("file", "heads", "blanks", "verdict"))
    print("-" * 92)
    bad = []
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        lines = strip_comments(open(p, encoding="utf-8",
                                    errors="replace").read()).splitlines()
        idx = [i for i, l in enumerate(lines)
               if re.search(r'\\(sub)?section\*?\{References', l)]
        if not idx:
            continue
        body = lines[idx[-1] + 1:]
        end = next((i for i, l in enumerate(body)
                    if re.search(r'\\end\{document\}', l)), len(body))
        body = body[:end]
        while body and not body[-1].strip():
            body.pop()

        head_at = [i for i, l in enumerate(body) if HEAD.match(l)]
        if not head_at:
            continue
        # The FIRST head is preceded by the \label or heading line, not by a
        # blank line, so it must not be counted as unseparated. (Earlier version
        # compared against offset 0 and so false-flagged the first entry in
        # every list whose References section carries a \label.)
        first = head_at[0]
        # A multi-author entry wrapped across lines puts further
        # "Surname, A.B.," heads on continuation lines. Those are not new
        # entries. They are identified by the PREVIOUS line ending in a comma --
        # the author list is still open. A genuine new entry follows a line that
        # ends the previous entry (a period, a year, a page range).
        unsep_at = [i for i in head_at
                    if i != first
                    and body[i - 1].strip()
                    and not body[i - 1].rstrip().endswith(",")
                    # an author list also stays open across "... and" / "... &"
                    and not re.search(r'(?:\band|\&)\s*$',
                                      body[i - 1].rstrip())]
        unsep = len(unsep_at)
        verdict = "OK" if unsep == 0 else "%d ENTRIES RUN TOGETHER" % unsep
        if unsep:
            bad.append((fn, len(head_at), unsep, unsep_at[:5]))
        print("%-46s %7d %7d  %s" %
              (fn[:46], len(head_at),
               sum(1 for l in body if not l.strip()), verdict))
    print("-" * 92)
    for fn, h, u, at in bad:
        print("\n%s: %d heads, %d not preceded by a blank line" % (fn, h, u))
        print("   first unseparated head offsets in list: %s" % at)


if __name__ == "__main__":
    main()
