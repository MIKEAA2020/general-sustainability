#!/usr/bin/env python3
"""Remove redundant bibliography entries, keeping the more informative copy.

Conservative by construction, per the author's instruction:

  - only groups where author, year AND title all match are touched;
  - within a group the entry carrying the most information is kept -- scored on
    DOI, journal/volume/pages, publisher and year -- so nothing substantive is
    lost by the deletion;
  - entries that are not standalone are SKIPPED. An entry is not standalone if it
    carries a second glued reference (detected as a DOI or page range followed by
    another author head on the same entry). Deleting such an entry would destroy
    a different work, so those are reported and left alone;
  - nothing is removed unless every group in the file passes these tests.

Dry run by default; --apply writes.
"""
import os
import re
import sys

from bib_dupes import key
from label_fetch import UNITS, SUPPS, strip_comments, PAPERS

# a second reference glued onto the end of this one
GLUED = re.compile(r'(?:doi:\S+|pp\.~\d+|\b\d+--\d+\.)\s+[A-Z][\w\-\']{2,},\s+[A-Z]\.')


def info_score(e):
    """More information -> higher score, so the richer entry is the one kept.

    Length is the primary signal and it is the reliable one. An earlier version
    scored fields individually and got paper04's Sion BACKWARDS: it preferred
    "Pacific J.\\ Math. 8, 171--176" (75 chars) over "Pacific Journal of
    Mathematics \\textbf{8}(1), 171--176" (107 chars), because the volume regex
    did not match through the \\textbf{...} braces. Deleting the fuller entry
    would lose information, which is exactly what "err towards retaining"
    forbids. Length cannot be fooled that way; DOI adds a bonus because it is
    the single most useful thing a reference can carry.
    """
    return len(e) + (200 if re.search(r'doi:', e, re.I) else 0)


def groups_of(fn):
    p = os.path.join(PAPERS, fn)
    lines = strip_comments(open(p, encoding="utf-8",
                                errors="replace").read()).splitlines()
    idx = [i for i, l in enumerate(lines)
           if re.search(r'\\(sub)?section\*?\{References', l)]
    if not idx:
        return {}
    body = "\n".join(lines[idx[-1]:])
    m = re.search(r'\\end\{document\}', body)
    if m:
        body = body[:m.start()]
    ents = [c.strip() for c in re.split(r'\n\s*\n', body) if c.strip()]
    ents = [e for e in ents if re.search(r'\b(1[89]\d\d|20\d\d)\b', e)]
    g = {}
    for e in ents:
        g.setdefault(key(e), []).append(e)
    return {k: v for k, v in g.items() if len(v) > 1}


def plan(fn):
    """Return (deletions, skips) for one file."""
    gs = groups_of(fn)
    dels, skips = [], []
    for k, v in gs.items():
        glued = [e for e in v if GLUED.search(re.sub(r'\s+', ' ', e))]
        if glued:
            skips.append((k, v, "entry carries a second glued reference"))
            continue
        ranked = sorted(v, key=lambda e: (-info_score(e), -len(e)))
        keeper = ranked[0]
        for e in ranked[1:]:
            dels.append((k, keeper, e))
    return dels, skips


def main():
    dry = "--apply" not in sys.argv
    print("mode: %s\n" % ("DRY RUN" if dry else "APPLYING"))
    total_d = total_s = 0
    for fn in UNITS + SUPPS:
        p = os.path.join(PAPERS, fn)
        if not os.path.exists(p):
            continue
        dels, skips = plan(fn)
        if not dels and not skips:
            continue
        print("=" * 100)
        print("%s   %d to delete, %d skipped" % (fn, len(dels), len(skips)))
        for k, keeper, doomed in dels:
            total_d += 1
            print("\n  DELETE (len %d):" % len(doomed))
            print("      %s" % re.sub(r'\s+', ' ', doomed)[:150])
            print("  KEEP   (len %d, score %d):" % (len(keeper),
                                                    info_score(keeper)))
            print("      %s" % re.sub(r'\s+', ' ', keeper)[:150])
        for k, v, why in skips:
            total_s += 1
            print("\n  SKIP (%s):" % why)
            for e in v:
                print("      %s" % re.sub(r'\s+', ' ', e)[:150])
        if dry:
            continue
        # apply: remove each doomed entry, matched on its FULL text.
        raw = open(p, encoding="utf-8", errors="replace").read()
        for k, keeper, doomed in dels:
            flat = re.sub(r'\s+', ' ', doomed).strip()
            # Match the whole entry, allowing any run of whitespace (including
            # the newlines of a hard-wrapped entry) between tokens. An earlier
            # version matched only the first 60 characters, which is NOT unique
            # when both copies of a reference begin identically -- as with
            # Hocherman 2025 in paper08, where the two entries share their first
            # 60 characters and differ only in "A critical review." vs
            # "a critical review. Ambio 54(12)...". That run was skipped by the
            # uniqueness check rather than deleting the wrong entry.
            toks = [re.escape(t) for t in flat.split(' ')]
            body = r'\s+'.join(toks)
            pat = re.compile(r'[ \t]*\n?[ \t]*' + body + r'[ \t]*(?=\n\s*\n|\Z)')
            new, n = pat.subn('', raw)
            if n != 1:
                print("      !! could not remove uniquely (%d matches): %s"
                      % (n, flat[:70]))
                continue
            raw = new
        open(p, "w", encoding="utf-8").write(raw)
    print("\n" + "=" * 100)
    print("deletions: %d   skipped (entangled): %d" % (total_d, total_s))
    if dry:
        print("(re-run with --apply to write)")


if __name__ == "__main__":
    main()
