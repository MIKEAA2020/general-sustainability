#!/usr/bin/env python3
"""Map the damage in paper08's reference list.

Two failure modes, both from entries being split and re-joined wrongly:

  HEADLESS  - an entry that begins with a journal name, volume/pages, or DOI:
              the tail of a reference whose author-title head is elsewhere.

  GLUED     - one line holding the end of one reference and the start of the
              next, with no blank line between them.

For each, the DOI (when present) is the key that links a stray tail back to the
entry it belongs to, so the report pairs them up where it can.
"""
import os
import re

from label_fetch import PAPERS, strip_comments

FN = "paper08_governance_delay_v46.tex"

# a line that starts an entry with an author surname then initials
AUTHOR_HEAD = re.compile(r'^(?:\\(?:emph|textbf|textit)\{)?[A-ZÅÄÖ][\w\-\'\{\}\\\.]{1,30},\s')
# a line that starts with a journal/publisher/volume -- i.e. no author
HEADLESS = re.compile(
    r'^(?:Ambio|Nature|Science|Theoretical Ecology|J\.|Ann\.|Proc\.|SIAM|'
    r'Philosophical|ICES|World Bank|Springer|Wiley|Prentice|Cambridge|'
    r'doi:|https?://|\d+\s*\(|--?\d)')


def main():
    p = os.path.join(PAPERS, FN)
    raw = open(p, encoding="utf-8", errors="replace").read()
    lines = strip_comments(raw).splitlines()
    idx = [i for i, l in enumerate(lines)
           if re.search(r'\\subsection\*{References}', l)]
    start = idx[-1] + 1
    body = lines[start:]
    end = next((i for i, l in enumerate(body)
                if re.search(r'\\begin\{center\}|\\section\*\{Declarations\}', l)),
               len(body))
    body = body[:end]
    print("reference list: lines %d-%d (%d lines)"
          % (start + 1, start + end, len(body)))

    # split into entries on blank lines
    entries = []
    cur, at = [], None
    for i, l in enumerate(body):
        if l.strip():
            if at is None:
                at = start + i + 1
            cur.append(l)
        else:
            if cur:
                entries.append((at, cur))
            cur, at = [], None
    if cur:
        entries.append((at, cur))

    print("entries: %d\n" % len(entries))

    print("=" * 100)
    print("HEADLESS entries (tails with no author-title head)")
    print("=" * 100)
    for at, ls in entries:
        flat = re.sub(r'\s+', ' ', " ".join(ls)).strip()
        if HEADLESS.match(flat) and not AUTHOR_HEAD.match(ls[0]):
            print("\n  L%d  %s" % (at, flat[:150]))

    print("\n" + "=" * 100)
    print("GLUED lines (end of one reference + start of the next)")
    print("=" * 100)
    for at, ls in entries:
        for j, l in enumerate(ls):
            # a DOI or page range followed by a new author head
            for m in re.finditer(r'(?:doi:\S+|pp\.~\d+|\b\d+--\d+\.)\s+'
                                 r'([A-Z][\w\-\']{2,},\s+[A-Z]\.)', l):
                print("\n  L%d  ...%s [>>> %s] %s"
                      % (at + j, l[max(0, m.start() - 70):m.start()],
                         m.group(1).strip(),
                         l[m.end():m.end() + 90]))

    print("\n" + "=" * 100)
    print("DOI index: which entries carry which DOI")
    print("=" * 100)
    seen = {}
    for at, ls in entries:
        flat = re.sub(r'\s+', ' ', " ".join(ls)).strip()
        for d in re.findall(r'doi:(10\.\S+?)(?=[\s,]|$)', flat):
            seen.setdefault(d, []).append((at, flat[:95]))
    for d, where in sorted(seen.items()):
        if len(where) > 1:
            print("\n  %s  appears %d times:" % (d, len(where)))
            for at, f in where:
                print("      L%-5d %s" % (at, f))
        else:
            print("  %s  L%d" % (d, where[0][0]))


if __name__ == "__main__":
    main()
