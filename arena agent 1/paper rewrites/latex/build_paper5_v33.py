#!/usr/bin/env python3
"""Build paper5 v33 from v32: tail-section remnant sweep (user-directed 2026-09-11).

Every substitution asserts exactly one match. Scope: places the v32 pass never
looked (post-References tail, reference list hygiene, citation cross-check).
- Stale supp pointer v8->v9 + S9 added to the supplementary inventory.
- Data Availability gains the deposited sensitivity-battery code and log.
- Orphan reference rescued: Yekutieli 2001 cited at the dependence caveat.
- References formatting: blank line between the Benjamini entries.
NOT touched: everything else (body, proofs, Box, tables, appendices, supp v9).
"""
import os

SRC = "/home/user/paper5_v32/paper5_sampled_governance_v32.tex"
DST = "/home/user/paper5_v33/paper5_sampled_governance_v33.tex"

r = lambda s: s

SUBS = [
("VER-header",
r'''% Periodic Review as Sampled Governance (paper 5, revision v32): redundancy sweep, accessible abstract, and readability revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v33): tail-section remnant sweep and citation-hygiene revision with line numbers for review.'''),

("TAIL-supp-v9",
r'''\texttt{paper5\_supplementary\_v8.md}''',
r'''\texttt{paper5\_supplementary\_v9.md}'''),

("TAIL-supp-S9",
r'''hypotheses with specified tests (S7), and the reproducibility register
(S8).''',
r'''hypotheses with specified tests (S7), the reproducibility register
(S8), and the screen-sensitivity battery and stage-scan decomposition
records (S9).'''),

("TAIL-dataavail-battery",
r'''processed spectral series and routines) and the
power-simulation code and seeds are deposited with the article.''',
r'''processed spectral series and routines), the
power-simulation code and seeds, and the sensitivity-battery code and
log are deposited with the article.'''),

("CITE-yekutieli",
r'''shared assessment methods) is acknowledged. The reported zero count''',
r'''shared assessment methods) is acknowledged (Benjamini and Yekutieli,
2001). The reported zero count'''),

("REFS-benjamini-break",
r'''the Royal Statistical Society B, 57: 289--300. Benjamini, Y., and''',
r'''the Royal Statistical Society B, 57: 289--300.

Benjamini, Y., and'''),
]

def main():
    src = open(SRC).read()
    for name, old, new in SUBS:
        n = src.count(old)
        assert n == 1, f"{name}: {n} matches (expected 1)"
        src = src.replace(old, new)
        print(f"ok {name}")
    assert "supplementary\\_v8" not in src
    assert "supplementary\\_v9" in src
    assert "records (S9)" in src
    assert "sensitivity-battery code and\nlog are deposited" in src
    assert src.count("Yekutieli") == 2, "cite + ref entry"
    assert "289--300.\n\nBenjamini" in src
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w").write(src)
    print("wrote", DST, len(src))

if __name__ == "__main__":
    main()
