#!/usr/bin/env python3
"""
sort_and_verify.py - deterministic disentanglement of
'humanizing audits/p4 body made accessible.txt' (1,760 lines, 2 audits mixed).

Established composition (see SORTING_REPORT.md for the evidence):
  - GROK audit                        = original lines 1-424
      (complete: sections 1-12, no reference list)
  - GEMINI audit, output 1, main body = original lines 425-1115
      ('gemini:' label, title, sections 1-7.5)
  - GEMINI audit, output 1, condensed ending = original lines 1116-1180
      (sections 8-9 + references; superseded by output 2)
  - GEMINI audit, output 2 (detailed tail) = original lines 1181-1760
      (sections 7.6-12 + Data and Code Availability + References)

This script (idempotently) rebuilds the two sorted files and then verifies:
  (V1) each sorted file's audit content is byte-identical to the concatenation
       of its declared original line slices (nothing rewritten, nothing lost);
  (V2) the declared slices partition the original file exactly (every original
       line appears in exactly one sorted location);
  (V3) the original file is only ever read (its md5 is recorded).

Run:  python3 'humanizing audits/sorted/sort_and_verify.py'
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AUDITS = os.path.dirname(HERE)
ORIG = os.path.join(AUDITS, "p4 body made accessible.txt")
GROK_OUT = os.path.join(HERE, "p4 body made accessible - GROK audit (sorted).txt")
GEM_OUT = os.path.join(HERE, "p4 body made accessible - GEMINI audit (sorted).txt")

# 1-indexed inclusive line ranges in the original file
GROK_SEG = [(1, 424)]
GEM_SEG = [(425, 1115), (1181, 1760)]
GEM_ANNEX = [(1116, 1180)]

HDR_BEGIN = "<!-- SORTING: HEADER BEGIN (editorial block added during sorting; not part of the audit) -->"
HDR_END = "<!-- SORTING: HEADER END -->"
M2 = "<!-- SORTING: SECOND GEMINI OUTPUT BEGINS HERE (original file lines 1181-1760) -->"
MANNEX = "<!-- SORTING: ANNEX BEGINS HERE - gemini output 1's superseded condensed ending (original file lines 1116-1180) -->"

GROK_HEADER = f"""{HDR_BEGIN}
This file is the GROK audit extracted from 'p4 body made accessible.txt'
(the owner's 'grok:' material). Its audit content is byte-identical to
original lines 1-424 of that file: a complete body accessibility rewrite
covering sections 1-12, in British spelling with \\( \\) inline math and
no reference list.
Provenance and evidence: see SORTING_REPORT.md in this folder.
{HDR_END}
"""

GEM_HEADER = f"""{HDR_BEGIN}
This file is the GEMINI audit extracted from 'p4 body made accessible.txt'
(the owner's 'gemini:' material), reassembled in reading order from the two
gemini outputs that were concatenated out of order in the original file:

  Main body    : original lines 425-1115 ('gemini:' label, title, sections 1-7.5)
  Second output: original lines 1181-1760 (sections 7.6-12, Data and Code
                 Availability, References) - the detailed tail that the first
                 output had compressed; inserted below at its marker
  Annex        : original lines 1116-1180 (sections 8-9 + references) - the
                 first output's condensed ending, superseded by the detailed
                 tail, preserved as an annex so no byte of the original is lost

All audit content is byte-identical to the original slices. The editorial
marker lines are HTML comments and are not part of the audit text.
Provenance and evidence: see SORTING_REPORT.md in this folder.
{HDR_END}
"""


def orig_lines():
    with open(ORIG, encoding="utf-8") as f:
        return f.read().split("\n")


def content_line_count(lines):
    """Number of real content lines (a trailing newline yields one empty
    split element that is not a line)."""
    return len(lines) - (1 if lines and lines[-1] == "" else 0)


def slice_text(lines, a, b):
    """1-indexed inclusive slice."""
    return "\n".join(lines[a - 1 : b])


def build():
    lines = orig_lines()

    grok_body = "\n".join(slice_text(lines, a, b) for a, b in GROK_SEG)
    with open(GROK_OUT, "w", encoding="utf-8") as f:
        f.write(GROK_HEADER + "\n" + grok_body + "\n")

    part1 = slice_text(lines, *GEM_SEG[0])
    part2 = slice_text(lines, *GEM_SEG[1])
    annex = slice_text(lines, *GEM_ANNEX[0])
    with open(GEM_OUT, "w", encoding="utf-8") as f:
        f.write(GEM_HEADER + "\n" + part1 + "\n")
        f.write("\n" + M2 + "\n" + part2 + "\n")
        f.write("\n" + MANNEX + "\n" + annex + "\n")
    return len(lines)


def strip_editorial(text):
    """Remove the editorial header block; return (body, had_header)."""
    ls = text.split("\n")
    if HDR_BEGIN in ls and HDR_END in ls:
        i0, i1 = ls.index(HDR_BEGIN), ls.index(HDR_END)
        rest = ls[i1 + 1 :]
        while rest and rest[0] == "":
            rest = rest[1:]
        return "\n".join(rest), True
    return text, False


def verify():
    lines = orig_lines()
    n = content_line_count(lines)
    ok = True
    checks = []

    # --- V1a: grok sorted file reproduces its slice byte-for-byte ---
    with open(GROK_OUT, encoding="utf-8") as f:
        g = f.read()
    g_body, had_hdr = strip_editorial(g)
    expected_g = "\n".join(slice_text(lines, a, b) for a, b in GROK_SEG)
    c1 = had_hdr and g_body.rstrip("\n") == expected_g.rstrip("\n")
    checks.append(("V1a grok byte-identity", c1))
    ok &= c1

    # --- V1b: gemini sorted file reproduces its three slices byte-for-byte ---
    with open(GEM_OUT, encoding="utf-8") as f:
        m = f.read()
    m_body, had_hdr = strip_editorial(m)
    exp_p1 = slice_text(lines, *GEM_SEG[0]).rstrip("\n")
    exp_p2 = slice_text(lines, *GEM_SEG[1]).rstrip("\n")
    exp_an = slice_text(lines, *GEM_ANNEX[0]).rstrip("\n")
    ls = m_body.split("\n")
    try:
        i2 = ls.index(M2)
        ia = ls.index(MANNEX)
        got_p1 = "\n".join(ls[:i2]).rstrip("\n")
        got_p2 = "\n".join(ls[i2 + 1 : ia]).rstrip("\n")
        got_an = "\n".join(ls[ia + 1 :]).rstrip("\n")
        c2 = had_hdr and got_p1 == exp_p1 and got_p2 == exp_p2 and got_an == exp_an
    except ValueError:
        c2 = False
    checks.append(("V1b gemini byte-identity (3 segments)", c2))
    ok &= c2

    # --- V2: the slices partition the original exactly ---
    covered = {}
    for a, b in GROK_SEG + GEM_SEG + GEM_ANNEX:
        for i in range(a, b + 1):
            covered[i] = covered.get(i, 0) + 1
    missing = [i for i in range(1, n + 1) if i not in covered]
    dupes = [i for i, c in covered.items() if c > 1]
    c3 = not missing and not dupes
    checks.append(
        (
            f"V2 partition of all {n} original lines (missing={len(missing)}, duplicated={len(dupes)})",
            c3,
        )
    )
    ok &= c3

    # --- V3: record original's md5 (the script never writes to it) ---
    with open(ORIG, "rb") as f:
        h = hashlib.md5(f.read()).hexdigest()
    checks.append((f"V3 original md5 {h} (read-only)", True))

    for name, res in checks:
        print(("PASS " if res else "FAIL ") + name)
    print("RESULT:", "ALL CHECKS PASS" if ok else "VERIFICATION FAILED")
    return ok


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "rebuild"
    if mode in ("rebuild", "build"):
        n = build()
        print(f"rebuilt sorted files from {n - 1} original content lines")
    sys.exit(0 if verify() else 1)
