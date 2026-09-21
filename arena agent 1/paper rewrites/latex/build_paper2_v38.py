#!/usr/bin/env python3
"""
Pass A (v38) — prerequisite repairs:
  * GAP 1  reproduce the coverage audit: cite the audit script; fix the
           contradictory "Code availability" declaration.
  * GAP 2  qualify the abstract's finite-checkability claim.
  * GAP 9  make the proof-collection sentence in Section 1.4 literally true.
  * (fix)  restore the missing Section 6.3 heading (referenced from three
           places but absent after the reorder).
"""

import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v37_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v37_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v38_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v38_Automatica_routes_supplementary.tex"


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1): {old[:60]!r}"
    return text.replace(old, new)


def main():
    m = open(MAIN, encoding="utf-8").read()
    s = open(SUPP, encoding="utf-8").read()

    # ---- restore missing Section 6.3 ------------------------------
    m = sub(
        m,
        "which barrier methods do not address.\n"
        "\n"
        "The estimation-tube programme shows that imperfect measurement",
        "which barrier methods do not address.\n"
        "\n"
        "\\subsubsection{6.3 Relation to the estimation-tube\n"
        "programme}\\label{relation-to-the-estimation-tube-programme}\n"
        "\n"
        "The estimation-tube programme shows that imperfect measurement",
        "sec63",
    )

    # ---- GAP 2: abstract qualification -----------------------------
    m = sub(
        m,
        "finitely\n"
        "checkable in the finite-state, polyhedral, and finite-horizon cases and analytic drift-and-timing conditions elsewhere.",
        "finitely\n"
        "checkable in the common-action, fibre-certification, and finite-horizon forms and analytic drift-and-timing conditions elsewhere.",
        "abstract",
    )

    # ---- GAP 9: proof-collection sentence --------------------------
    m = sub(
        m,
        "Proof sketches of the Section 3 results are given in the main text; the complete proofs, the expanded sufficiency review, and the auxiliary constructions are collected in the Supplementary Material.",
        "Proof sketches of the Section 3 results are given in the main text; the complete proofs of the Section 3 certificates, the expanded sufficiency review, and the auxiliary constructions are collected in the Supplementary Material; the results of Sections 7 and 9 are proved in the main text.",
        "sec14",
    )

    # ---- GAP 1: audit wording + code citation ----------------------
    m = sub(
        m,
        "To quantify the gap conceded in Section 6.5, we audit",
        "To quantify the gap identified in Section 6.5, we audit",
        "conceded",
    )
    m = sub(
        m,
        "report the true verdict, the one-step certificate, and the timing bound.",
        "report the true verdict, the one-step certificate, and the timing bound. The audit is reproduced by the script \\texttt{paper2\\_coverage\\_audit.py} (archived with the verification code at \\url{https://zenodo.org/records/22545740}), which also regenerates Table~\\ref{tab:coverage} and Figure~\\ref{fig:coverage}.",
        "audit-code",
    )

    # ---- GAP 1: declarations ---------------------------------------
    m = sub(
        m,
        "\\textbf{Data availability.} No data were used; all constructions are symbolic.\\quad \\textbf{Code availability.} No code was used or produced; all constructions are symbolic.",
        "\\textbf{Data availability.} No external data were used.\\quad \\textbf{Code availability.} The coverage-audit script \\texttt{paper2\\_coverage\\_audit.py} is archived at \\url{https://zenodo.org/records/22545740}.",
        "declarations",
    )

    # ---- supplementary: S1 intro -----------------------------------
    s = sub(
        s,
        "This supplement collects the material condensed from the main text: the complete proofs (S1), the expanded sufficiency review (S2), the bounded constructions and scope remarks (S3), and three additional figures (S4).",
        "This supplement collects the material condensed from the main text: the complete proofs of the Section 3 certificates (S1), the expanded sufficiency review (S2), the bounded constructions and scope remarks (S3), and three additional figures (S4).",
        "supp-intro",
    )

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
