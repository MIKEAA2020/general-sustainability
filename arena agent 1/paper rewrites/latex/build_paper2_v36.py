#!/usr/bin/env python3
"""
v36 — fix equation-tag ordering defect introduced by the Section 3 reorder.

After the reorder the hardcoded equation tags appear physically in the order
(2),(3),(4),(1),(5): equation (1) (the exit drift condition) now sits in
Section 3.5, after (2) (Section 3.2) and (3),(4) (Section 3.3). This pass
renumbers the Section 3 tags into reading order and remaps every hardcoded
in-text reference:

    old (1) [exit drift, now 3.5]   -> (4)
    old (2) [common-action, now 3.2] -> (1)
    old (3) [delayed drift, now 3.3] -> (2)
    old (4) [delayed timing, now 3.3] -> (3)
    (5) [fibre criterion, Section 4, unmoved] -> (5) unchanged

The supplementary is self-contained with its own ordered tags (1)-(5) and is
not touched.
"""

import re, sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN_IN = f"{LATEX_DIR}/paper2_obstruction_calculus_v35_Automatica_routes.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v36_Automatica_routes.tex"


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1): {old!r}"
    return text.replace(old, new)


def main():
    text = open(MAIN_IN, encoding="utf-8").read()

    # ---- 1. tag renumbering (single regex pass, no cascade) ------------
    tag_map = {"1": "4", "2": "1", "3": "2", "4": "3"}
    text = re.sub(r"\\tag\{([1-4])\}", lambda m: "\\tag{" + tag_map[m.group(1)] + "}", text)

    # ---- 2. in-text references ------------------------------------------
    # old (1) -> (4)
    text = sub(text, "By (1), the adverse-selection correspondence", "By (4), the adverse-selection correspondence", "by1")
    text = sub(text, "integrates (1) along the resulting trajectory", "integrates (4) along the resulting trajectory", "int1")
    text = sub(text, "Two readings of (1) matter", "Two readings of (4) matter", "read1")
    text = sub(text, "Second, (1) is an outward-drift certificate", "Second, (4) is an outward-drift certificate", "second1")
    # old (2) -> (1)
    text = sub(text, "Condition (2) is checkable", "Condition (1) is checkable", "cond2")
    text = sub(text, "The instantaneous condition (2) is the", "The instantaneous condition (1) is the", "inst2")
    # old (3) -> (2)
    text = sub(text, "realizing the drift (3); integrating (3) gives", "realizing the drift (2); integrating (2) gives", "drift3")
    text = sub(text, "The hypothesis (3) is the set-membership form", "The hypothesis (2) is the set-membership form", "hyp3")
    text = sub(text, "computable from the drift certificate (3),", "computable from the drift certificate (2),", "cert3")
    # old (4) -> (3)
    text = sub(text, "which (4) places strictly before", "which (3) places strictly before", "w4")
    text = sub(text, "timing bound (4) its force", "timing bound (3) its force", "tb4")
    text = sub(text, "and (4) then makes the obstruction epistemic", "and (3) then makes the obstruction epistemic", "a4")
    text = sub(text, "Condition (4) is", "Condition (3) is", "cond4is")
    text = sub(text, "Condition (4) certifies this threshold", "Condition (3) certifies this threshold", "cond4cert")
    text = sub(text, "and (4) states that", "and (3) states that", "a4states")
    text = sub(text, "even when (4)", "even when (3)", "even4")

    open(MAIN_OUT, "w", encoding="utf-8").write(text)
    print(f"wrote {MAIN_OUT}  ({len(text)} bytes)")


if __name__ == "__main__":
    main()
