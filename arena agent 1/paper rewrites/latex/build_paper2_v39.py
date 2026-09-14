#!/usr/bin/env python3
"""
Pass B (v39) — two strengthening edits:
  * GAP 4  scope paragraph after the Helly worked certificate: a concrete
           counterexample showing the convexity hypotheses are essential.
  * GAP 3  a worked three-method comparison (barrier / estimation-tube /
           obstruction) on the two-floor system, added to the supplementary S2,
           with a pointer sentence in main Section 6.3.
"""

import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v38_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v38_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v39_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v39_Automatica_routes_supplementary.tex"


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1): {old[:60]!r}"
    return text.replace(old, new)


def main():
    m = open(MAIN, encoding="utf-8").read()
    s = open(SUPP, encoding="utf-8").read()

    # ---- GAP 4: scope paragraph after the Helly worked certificate ----
    m = sub(
        m,
        "incompatible states are exactly the \\(m+1\\)-state witness of\n"
        "Proposition~\\ref{prop:helly}.\n",
        "incompatible states are exactly the \\(m+1\\)-state witness of\n"
        "Proposition~\\ref{prop:helly}.\n"
        "\n"
        "\\textbf{Scope of the convexity hypotheses.} Convexity is essential to the witness: without it the bound fails even in a single control dimension. Take \\(U=\\mathbb R\\) (\\(m=1\\)) and three nonconvex safe-action sets \\(\\mathcal R_1=\\{0,1\\}\\), \\(\\mathcal R_2=\\{0,2\\}\\), \\(\\mathcal R_3=\\{1,2\\}\\). Each pair intersects (\\(\\mathcal R_1\\cap\\mathcal R_2=\\{0\\}\\), \\(\\mathcal R_1\\cap\\mathcal R_3=\\{1\\}\\), \\(\\mathcal R_2\\cap\\mathcal R_3=\\{2\\}\\)), yet the three-way intersection is empty, so no \\((m+1)=2\\)-state witness exists. The convexity hypotheses of Proposition~\\ref{prop:helly} exclude exactly this failure mode.\n",
        "helly-scope",
    )

    # ---- GAP 3: pointer sentence at end of Section 6.3 ----------------
    m = sub(
        m,
        "the obstruction calculus answers \\emph{why not, and what to change}.\n",
        "the obstruction calculus answers \\emph{why not, and what to change}. A single worked system carrying the three methods side by side --- barrier certificate, estimation-tube reduction, and obstruction certificate --- is given in the Supplementary Material (S2).\n",
        "sec63-pointer",
    )

    # ---- GAP 3: worked comparison in supplementary S2 ------------------
    comp = (
        "\n"
        "\\textbf{A worked comparison: barrier, estimation-tube, and obstruction certificates on one system.} The two-floor system of Section 3.4 makes the division of labour concrete. Two states \\(x_1\\) and \\(x_2\\) share one observation; the single control \\(u\\in[0,1]\\) must satisfy \\(u\\le 0.4\\) at \\(x_1\\) (floor 1 active) and \\(u\\ge 0.6\\) at \\(x_2\\) (floor 2 active).\n"
        "\n"
        "\\emph{Barrier certificates.} A barrier certificate certifies safety from a scalar function whose zero level set separates the unsafe region from all trajectories under some state feedback. Here there is no state to feed back --- the observation merges \\(x_1\\) and \\(x_2\\) --- so an admissible barrier would have to be constant on the fibre \\(\\{x_1,x_2\\}\\), and no such function can separate the two floors' incompatible requirements. The programme therefore reports ``no barrier found,'' a verdict that does not distinguish ``unsafe'' from ``unsafe for the class of barrier functions tried.''\n"
        "\n"
        "\\emph{Estimation-tube reduction.} Lifting to the estimation space replaces the merged observation by perfect information about the belief \\(\\{x_1,x_2\\}\\). The belief-state viability problem then has empty value --- no common control keeps both floors safe --- so the estimation-space kernel is empty. The reduction returns the verdict exactly, but as a black box: it does not isolate which feature of the observation is responsible.\n"
        "\n"
        "\\emph{Obstruction certificate.} The common-action obstruction (Theorem~\\ref{thm:common-action}) fires with the explicit Farkas certificate \\(\\lambda=(1/2,1/2)\\) for the stacked system \\(u\\le 0.4\\), \\(-u\\le -0.6\\), with \\(\\lambda^{\\top}A=0\\) and \\(\\lambda^{\\top}b=-0.1<0\\) --- the infeasibility margin \\(0.1\\) of Section 3.4. The sparse witness of Section 3.4 records that \\(m+1=2\\) states already suffice, and the certificate licenses a concrete remedy: any observation separating \\(x_1\\) from \\(x_2\\) restores one-step viability. This is the division of labour the paper relies on --- the barrier programme and the estimation-tube reduction certify \\emph{that} the kernel is empty; the obstruction calculus certifies \\emph{why}, and names the observation feature to change.\n"
        "\n"
    )
    s = sub(
        s,
        "applies to both.\n"
        "\n"
        "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}",
        "applies to both.\n"
        + comp +
        "\n"
        "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}",
        "supp-comparison",
    )

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
