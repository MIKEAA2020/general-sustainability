#!/usr/bin/env python3
"""
v42 — fix #1: remove the duplicated References heading (and its multiply-defined
label) in the supplementary. The main text is carried forward unchanged from v41
(the expanded scope is kept, as instructed).
"""

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v41_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v41_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v42_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v42_Automatica_routes_supplementary.tex"


def main():
    m = open(MAIN, encoding="utf-8").read()
    s = open(SUPP, encoding="utf-8").read()

    dup = "\\subsection{References}\\label{references}\n\n\\subsection{References}\\label{references}"
    n = s.count(dup)
    assert n == 1, f"expected exactly one duplicated References block, found {n}"
    s = s.replace(dup, "\\subsection{References}\\label{references}")

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes) [unchanged copy]")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes) [References duplication fixed]")


if __name__ == "__main__":
    main()
