#!/usr/bin/env python3
"""
Pass 2 (v34) — connective/consistency polish after the v33 surgical reorder.

Edits (all content-preserving; math untouched):
  E1  recursion opening re-framed for its new lead position
  E2  recursion closing: "of the following subsections"
  E3  common-action section: one-sentence lead-in
  E4  emptiness opening: "The remaining obstructions" -> "The admissibility
      obstruction"
  E5  Section 1.2 contributions: six items reordered to the new spine
      (common-action, delayed, exit, emptiness, fibre, CE-trap)
  E6  Section 1.2 "Five refinements" reordered to the new spine
  E7  Section 7: fix duplicated phrase "that gap precise: it exhibits"
"""

import sys, re

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN_IN = f"{LATEX_DIR}/paper2_obstruction_calculus_v33_Automatica_routes.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v34_Automatica_routes.tex"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] found {n} occurrences (expected 1)"
    return text.replace(old, new)


def main():
    text = read(MAIN_IN)

    # ---- E1: recursion opening -----------------------------------------
    e1_old = (
        "The certificates of Sections 3.2--3.3 and 3.5--3.6 are sufficient conditions, not a\n"
        "complete characterization of the epistemic kernel. In the finite setting\n"
        "the calculus is complete: backward recursion over beliefs --- the set-membership analogue of the belief-state recursion of partially observable Markov processes (Smallwood and Sondik, 1973) --- is sound and complete on any finite horizon, and nonviability is certified by a\n"
        "finite obstruction tree."
    )
    e1_new = (
        "In the finite setting the calculus is complete: backward recursion over beliefs --- the set-membership analogue of the belief-state recursion of partially observable Markov processes (Smallwood and Sondik, 1973) --- is sound and complete on any finite horizon, and nonviability is certified by a finite obstruction tree. The certificates of Sections 3.2--3.3 and 3.5--3.6 are sufficient conditions, not a complete characterization of the epistemic kernel."
    )
    text = sub(text, e1_old, e1_new, "E1")

    # ---- E2: recursion closing -----------------------------------------
    e2_old = (
        "counterpart of the sufficient certificates of Sections 3.2--3.3 and 3.5--3.6."
    )
    e2_new = (
        "counterpart of the sufficient certificates of the following subsections."
    )
    text = sub(text, e2_old, e2_new, "E2")

    # ---- E3: common-action lead-in -------------------------------------
    e3_old = (
        "obstruction}\\label{the-instantaneous-common-action-obstruction}\n"
        "\n"
        "\\begin{theorem}[common-action obstruction]\\label{thm:common-action}"
    )
    e3_new = (
        "obstruction}\\label{the-instantaneous-common-action-obstruction}\n"
        "\n"
        "The instantaneous obstruction is the static core of the calculus: it certifies nonviability at a single information state, without a timing or horizon argument.\n"
        "\n"
        "\\begin{theorem}[common-action obstruction]\\label{thm:common-action}"
    )
    text = sub(text, e3_old, e3_new, "E3")

    # ---- E4: emptiness opening -----------------------------------------
    e4_old = (
        "The remaining obstructions apply to systems in which every state is\n"
        "individually viable under full information and the kernel empties only under the observation structure."
    )
    e4_new = (
        "The admissibility obstruction applies to systems in which every state is\n"
        "individually viable under full information and the kernel empties only under the observation structure."
    )
    text = sub(text, e4_old, e4_new, "E4")

    # ---- E5: reorder the six contribution items ------------------------
    start = text.index("\\begin{enumerate}\n\\def\\labelenumi{\\arabic{enumi}.}")
    end = text.index("\\end{enumerate}", start)
    block = text[start:end]
    # split into items on lines that are exactly "\item"
    parts = re.split(r"(?m)^(\\item)\n", block)
    # parts[0] = preamble; then alternating ("\item", body), ("\item", body), ...
    assert len(parts) == 1 + 2 * 6, f"unexpected item split: {len(parts)}"
    preamble = parts[0]
    assert preamble.rstrip("\n").endswith("\\def\\labelenumi{\\arabic{enumi}.}"), "preamble shape unexpected"
    items = []
    for i in range(1, len(parts), 2):
        items.append(parts[i] + "\n" + parts[i + 1])
    assert len(items) == 6

    def key(it):
        m = re.search(r"\\textbf\{([^}]*)\}", it)
        return m.group(1)

    keys = [key(it) for it in items]
    expected_keys = [
        "The finite-time exit certificate",
        "Epistemic emptiness by admissibility",
        "The instantaneous common-action obstruction",
        "The delayed-information obstruction",
        "The fibre certification criterion",
        "The certainty-equivalence trap",
    ]
    assert keys == expected_keys, f"item keys mismatch: {keys}"

    order = [
        "The instantaneous common-action obstruction",
        "The delayed-information obstruction",
        "The finite-time exit certificate",
        "Epistemic emptiness by admissibility",
        "The fibre certification criterion",
        "The certainty-equivalence trap",
    ]
    reordered = [items[keys.index(k)] for k in order]
    new_block = preamble + "".join(reordered)
    text = text[:start] + new_block + text[end:]

    # ---- E6: Five refinements reorder ----------------------------------
    e6_old = (
        "Five refinements complete the picture:\n"
        "a comparison-function form sharpens the exit-time bound\n"
        "(Remark~\\ref{rem:comparison}); a uniform-margin condition connects the\n"
        "instantaneous and tube obstructions\n"
        "(Proposition~\\ref{prop:uniform-margin}); the timing obstruction has a\n"
        "sharp threshold form (Remark~\\ref{rem:sigma}); a Helly-type sparse\n"
        "witness bounds the common-action obstruction by \\(m+1\\) compatible\n"
        "states (Proposition~\\ref{prop:helly}); and backward belief recursion is\n"
        "sound and complete on any finite horizon in finite systems\n"
        "(Theorem~\\ref{thm:finite-horizon})."
    )
    e6_new = (
        "Five refinements complete the picture:\n"
        "backward belief recursion is sound and complete on any finite horizon\n"
        "in finite systems (Theorem~\\ref{thm:finite-horizon}); a uniform-margin\n"
        "condition connects the instantaneous and tube obstructions\n"
        "(Proposition~\\ref{prop:uniform-margin}); the timing obstruction has a\n"
        "sharp threshold form (Remark~\\ref{rem:sigma}); a Helly-type sparse\n"
        "witness bounds the common-action obstruction by \\(m+1\\) compatible\n"
        "states (Proposition~\\ref{prop:helly}); and a comparison-function form\n"
        "sharpens the exit-time bound (Remark~\\ref{rem:comparison})."
    )
    text = sub(text, e6_old, e6_new, "E6")

    # ---- E7: duplicated phrase fix -------------------------------------
    e7_old = "This section makes that gap precise: it exhibits that gap precise: it exhibits two settings"
    e7_new = "This section makes that gap precise: it exhibits two settings"
    text = sub(text, e7_old, e7_new, "E7")

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {MAIN_OUT}  ({len(text)} bytes)")


if __name__ == "__main__":
    main()
