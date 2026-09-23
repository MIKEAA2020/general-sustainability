#!/usr/bin/env python3
"""
v37 — full alignment after the Section 3 spine reorder.

Main text:
  * hypothesis labels track the subsection in which the theorem sits, so they
    are renumbered to the new subsections:
        H1.x = exit (was 3.1)          -> H5.x (now 3.5)
        H3.x = common-action (was 3.3) -> H2.x (now 3.2)
        H4.x = delayed (was 3.4)       -> H3.x (now 3.3)

Supplementary:
  1. same hypothesis-label renumbering;
  2. S1 (complete proofs) reordered to the new main spine:
        recursion, common-action, uniform-margin, ladder, delayed,
        exit, emptiness, fibre, certainly-safe, monotone;
  3. equation tags renumbered to the new physical order
        (1)->(4), (2)->(1), (3)->(2), (4)->(3), (5) unchanged;
  4. in-text equation references remapped consistently.
"""

import re, sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v36_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v36_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v37_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v37_Automatica_routes_supplementary.tex"

H_FIRST = {"1": "5", "3": "2", "4": "3"}
TAG_MAP = {"1": "4", "2": "1", "3": "2", "4": "3"}


def main():
    main = open(MAIN, encoding="utf-8").read()
    supp = open(SUPP, encoding="utf-8").read()

    # ============ MAIN ============
    m = re.sub(r"H([134])\.([123])",
               lambda mm: f"H{H_FIRST[mm.group(1)]}.{mm.group(2)}", main)
    assert not re.search(r"H[14]\.[123]", m), "stale old H-label in main"

    # ============ SUPP: reorder S1 ============
    lines = supp.splitlines(keepends=True)

    def idx(prefix):
        for i, l in enumerate(lines):
            if l.rstrip("\n").startswith(prefix):
                return i
        sys.exit(f"anchor not found: {prefix!r}")

    a_exit = idx("\\begin{theorem}[finite-time exit certificate]")
    a_empt = idx("\\begin{proposition}[epistemic emptiness by admissibility")
    a_comm = idx("\\begin{theorem}[common-action obstruction]")
    a_um   = idx("\\begin{proposition}[uniform margin gives")
    a_lad  = idx("\\begin{proposition}[obstruction ladder]")
    a_dly  = idx("\\begin{theorem}[delayed-information obstruction]")
    a_rec  = idx("\\begin{theorem}[finite-horizon soundness and completeness]")
    a_fib  = idx("\\begin{proposition}[observation-fibre criterion]")
    a_cs   = idx("\\begin{corollary}[safety-crossing fibres")
    a_mon  = idx("\\begin{proposition}[monotonicity of the epistemic kernel]")
    a_s2   = idx("\\section*{S2. The sufficiency landscape (full)}")

    order = [a_exit, a_empt, a_comm, a_um, a_lad, a_dly, a_rec, a_fib, a_cs, a_mon, a_s2]
    assert order == sorted(order), f"supp block order broken: {order}"

    exit_blk = lines[a_exit:a_empt]
    empt_blk = lines[a_empt:a_comm]
    comm_blk = lines[a_comm:a_um]
    um_blk   = lines[a_um:a_lad]
    lad_blk  = lines[a_lad:a_dly]
    dly_blk  = lines[a_dly:a_rec]
    rec_blk  = lines[a_rec:a_fib]
    fib_blk  = lines[a_fib:a_cs]
    cs_blk   = lines[a_cs:a_mon]
    mon_blk  = lines[a_mon:a_s2]

    new_s1 = (rec_blk + comm_blk + um_blk + lad_blk + dly_blk +
              exit_blk + empt_blk + fib_blk + cs_blk + mon_blk)
    s = "".join(lines[:a_exit] + new_s1 + lines[a_s2:])

    # ============ SUPP: hypotheses + equations ============
    s = re.sub(r"H([134])\.([123])",
               lambda mm: f"H{H_FIRST[mm.group(1)]}.{mm.group(2)}", s)
    assert not re.search(r"H[14]\.[123]", s), "stale old H-label in supp"

    s = re.sub(r"\\tag\{([1-4])\}",
               lambda mm: "\\tag{" + TAG_MAP[mm.group(1)] + "}", s)

    def sub(txt, old, new, name):
        n = txt.count(old)
        assert n == 1, f"[supp:{name}] {n} occurrences (expected 1): {old!r}"
        return txt.replace(old, new)

    s = sub(s, "condition (1) gives", "condition (4) gives", "c1")
    s = sub(s, "by (1). For", "by (4). For", "b1")
    s = sub(s, "realization satisfying (3) along the trajectory", "realization satisfying (2) along the trajectory", "s3")
    s = sub(s, "trajectory integrates (3) to", "trajectory integrates (2) to", "i3")
    s = sub(s, "by (4) is strictly less", "by (3) is strictly less", "b4")
    s = sub(s, "Condition (4) certifies this threshold", "Condition (3) certifies this threshold", "c4")
    s = sub(s, "and (4) states that", "and (3) states that", "a4")
    s = sub(s, "even when (4)", "even when (3)", "e4")

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
