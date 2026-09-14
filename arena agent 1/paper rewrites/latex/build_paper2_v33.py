#!/usr/bin/env python3
"""
Pass 1 (v33) — surgical physical spine reorder of Section 3.

Reads v32 main + supplementary, writes v33 main + supplementary.

Guardrails:
  * Blocks are moved whole; theorem/proposition/remark/example bodies are
    byte-identical (only the subsubsection title numbers change).
  * Every hardcoded order-dependent "Section 3.x" / "Sections 3.x--3.y"
    textual reference is remapped to the new spine numbering.
  * The Section 1.4 organization sentence is rewritten to the new order.
  * The two now-false forward connectors ("the next section", "The next
    theorem") are corrected.

Target spine (new subsection numbering):
  3.1 Finite-horizon completeness (finite systems)        [A = recursion]
  3.2 The instantaneous common-action obstruction         [B]
  3.3 The delayed-information obstruction                 [C = sigma*]
  3.4 The sparse finite witness                          [D = Helly]
  3.5 The finite-time exit certificate                    [support]
  3.6 Epistemic emptiness by admissibility                [support]
"""

import re
import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN_IN = f"{LATEX_DIR}/paper2_obstruction_calculus_v32_Automatica_routes.tex"
SUPP_IN = f"{LATEX_DIR}/paper2_obstruction_calculus_v32_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v33_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v33_Automatica_routes_supplementary.tex"


def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)


def find_line(lines, anchor, must=True):
    """Return index of the line whose rstripped content equals `anchor`."""
    for i, line in enumerate(lines):
        if line.rstrip("\n") == anchor:
            return i
    if must:
        sys.exit(f"ANCHOR NOT FOUND: {anchor!r}")
    return None


def find_first_after(lines, anchor, start):
    for i in range(start, len(lines)):
        if lines[i].rstrip("\n") == anchor:
            return i
    sys.exit(f"ANCHOR NOT FOUND (after {start}): {anchor!r}")


def main():
    lines = read_lines(MAIN_IN)

    # ---- locate block boundaries ---------------------------------------
    exit_start = find_line(lines, "\\subsubsection{3.1 The finite-time exit")
    empt_start = find_line(lines,
        "\\subsubsection{3.2 Epistemic emptiness by admissibility: a minimal")
    comm_start = find_line(lines, "\\subsubsection{3.3 The instantaneous common-action")
    dely_start = find_line(lines, "\\subsubsection{3.4 The delayed-information")
    recu_start = find_line(lines,
        "\\subsubsection{3.5 Finite-horizon completeness (finite systems)}\\label{finite-horizon-completeness}")
    sec4_idx   = find_line(lines, "\\subsection{4. Certification Limits}\\label{certification-limits}")

    helly_start = find_line(lines,
        "\\begin{proposition}[sparse common-action witness]\\label{prop:helly}")
    figure_idx  = find_first_after(lines, "\\begin{figure}[htbp]", helly_start)

    # sanity: strict ascending order
    order = [exit_start, empt_start, comm_start, helly_start, figure_idx,
             dely_start, recu_start, sec4_idx]
    assert order == sorted(order), f"boundary order broken: {order}"

    exit_block  = lines[exit_start:empt_start]
    empt_block  = lines[empt_start:comm_start]
    comm_head   = lines[comm_start:helly_start]
    helly_block = lines[helly_start:figure_idx]
    comm_tail   = lines[figure_idx:dely_start]
    dely_block  = lines[dely_start:recu_start]
    recu_block  = lines[recu_start:sec4_idx]

    helly_title = [
        "\\subsubsection{3.4 The sparse finite\n",
        "witness}\\label{the-sparse-finite-witness}\n",
        "\n",
    ]

    # ---- reassemble: new spine order ------------------------------------
    new_sec3 = (
        recu_block + comm_head + comm_tail + dely_block +
        helly_title + helly_block + exit_block + empt_block
    )
    new_lines = lines[:exit_start] + new_sec3 + lines[sec4_idx:]
    text = "".join(new_lines)

    # ---- renumber subsubsection titles ----------------------------------
    title_map = [
        ("\\subsubsection{3.1 The finite-time exit",
         "\\subsubsection{3.5 The finite-time exit"),
        ("\\subsubsection{3.2 Epistemic emptiness by admissibility: a minimal",
         "\\subsubsection{3.6 Epistemic emptiness by admissibility: a minimal"),
        ("\\subsubsection{3.3 The instantaneous common-action",
         "\\subsubsection{3.2 The instantaneous common-action"),
        ("\\subsubsection{3.4 The delayed-information",
         "\\subsubsection{3.3 The delayed-information"),
        ("\\subsubsection{3.5 Finite-horizon completeness (finite systems)}",
         "\\subsubsection{3.1 Finite-horizon completeness (finite systems)}"),
    ]
    for old, new in title_map:
        assert text.count(old) == 1, f"title not unique/absent: {old!r} (count={text.count(old)})"
        text = text.replace(old, new)

    # ---- remap hardcoded "Section(s) 3.x" references --------------------
    # ranges first (plural forms; en-dash and double-hyphen variants)
    range_map = [
        ("Sections 3.1--3.4", "Sections 3.2--3.3 and 3.5--3.6"),
        ("Sections 3.2--3.4", "Sections 3.2--3.3 and 3.6"),
        ("Sections 3.1\u20133.4", "Sections 3.2\u20133.3 and 3.5\u20133.6"),
        ("Sections 3.2\u20133.4", "Sections 3.2\u20133.3 and 3.6"),
    ]
    for old, new in range_map:
        if old in text:
            text = text.replace(old, new)

    # singular mapping (single regex pass; no cascade)
    sing_map = {"1": "5", "2": "6", "3": "2", "4": "3", "5": "1"}
    def repl(m):
        return "Section 3." + sing_map[m.group(1)]
    text = re.sub(r"Section\s+3\.([1-5])", repl, text)

    # ---- Section 1.4 organization sentence ------------------------------
    org_old = ("Section 3 develops the obstruction calculus "
               "(Theorem~\\ref{thm:exit}--\\ref{thm:finite-horizon}, "
               "Propositions~\\ref{prop:emptiness}--\\ref{prop:ladder}, "
               "Remarks~\\ref{rem:comparison}--\\ref{rem:sigma}, and "
               "Example~\\ref{ex:hidden-mode}): the finite-time exit certificate, "
               "the admissibility and common-action obstructions, the "
               "delayed-information obstruction with its threshold form, the "
               "obstruction ladder, and finite-horizon completeness.")
    org_new = ("Section 3 develops the obstruction calculus "
               "(Theorem~\\ref{thm:finite-horizon}--\\ref{thm:exit}, "
               "Propositions~\\ref{prop:uniform-margin}--\\ref{prop:emptiness}, "
               "Remarks~\\ref{rem:sigma}--\\ref{rem:comparison}, and "
               "Example~\\ref{ex:hidden-mode}): finite-horizon completeness, the "
               "instantaneous common-action obstruction with its ladder and "
               "sparse witness, the delayed-information obstruction with its "
               "threshold form, and --- as supporting certificates --- the "
               "finite-time exit certificate and the admissibility obstruction.")
    assert text.count(org_old) == 1, "organization sentence not found uniquely"
    text = text.replace(org_old, org_new)

    # ---- false forward-connector fixes ----------------------------------
    c1_old = "obstruction of the next section and Example"
    c1_new = "obstruction of Section 3.2 and Example"
    assert text.count(c1_old) == 1, "connector 1 not found uniquely"
    text = text.replace(c1_old, c1_new)

    c2_old = "The next\ntheorem states the general obstruction"
    c2_new = "Theorem~\\ref{thm:common-action} states the general obstruction"
    assert text.count(c2_old) == 1, "connector 2 not found uniquely"
    text = text.replace(c2_old, c2_new)

    with open(MAIN_OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {MAIN_OUT}  ({len(text)} bytes)")

    # ---- supplementary: two Section 3.x references ----------------------
    supp = read_lines(SUPP_IN)
    s = "".join(supp)
    smap = [
        ("in the constructions of Sections 3.2--3.4.",
         "in the constructions of Sections 3.2--3.3 and 3.6."),
        ("and the recursive predecessor of Section 3.5 ---",
         "and the recursive predecessor of Section 3.1 ---"),
    ]
    for old, new in smap:
        assert s.count(old) == 1, f"supp string not found uniquely: {old!r}"
        s = s.replace(old, new)
    with open(SUPP_OUT, "w", encoding="utf-8") as f:
        f.write(s)
    print(f"wrote {SUPP_OUT}  ({len(s)} bytes)")


if __name__ == "__main__":
    main()
