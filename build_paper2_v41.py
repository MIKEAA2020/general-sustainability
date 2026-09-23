#!/usr/bin/env python3
"""
Pass D (v41) — final strengthening pass:
  * GAP 8   two-dimensional aggregation instance in the case study, a
            calibration paragraph mapping certificate parameters to
            stock-assessment quantities, and an updated closing.
  * GAP 10  upgrade the coverage Remark from an audit observation to a proven
            identity (joint completeness in the delayed class).
"""

import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v40_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v41_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v41_Automatica_routes_supplementary.tex"


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1): {old[:70]!r}"
    return text.replace(old, new)


def main():
    m = open(MAIN, encoding="utf-8").read()
    s = open(SUPP, encoding="utf-8").read()

    # ---- GAP 8: two-dimensional aggregation instance ------------------
    m = sub(
        m,
        "the index can certify safety only when it reads high.",
        "the index can certify safety only when it reads high.\n"
        "\n"
        "\\textbf{Two-dimensional aggregation.} The fibre criterion also governs a multidimensional stock. Take a two-species state \\((S_{1}, S_{2}) \\in [0,1]^{2}\\) with the floor \\(S_{1} \\ge 0.4\\), and suppose the regulator observes only the aggregate \\(I = S_{1} + S_{2}\\). The states \\((0.5, 0.5)\\) and \\((0.2, 0.8)\\) are both compatible with the reading \\(I = 1.0\\), yet the first satisfies the floor and the second violates it, so by Proposition~\\ref{prop:fibre} no exact observation-only certifier exists; by Corollary~\\ref{cor:certainly-safe} the certainly-safe readings are exactly \\(I \\ge 1.4\\) (the smallest \\(S_{1}\\) compatible with \\(I\\) is \\(I - 1\\), so \\(I - 1 \\ge 0.4\\)). An aggregate reading below \\(1.4\\) must therefore fall silent, however carefully thresholded --- the two-dimensional form of the aggregation consequence of Section 6.4.",
        "twodim",
    )

    # ---- GAP 10: proven joint completeness ----------------------------
    m = sub(
        m,
        "In this class the two certificates are jointly complete, and the Section 6.5 gap reduces to the timing cells.\n"
        "\\end{remark}",
        "In this class the two certificates are jointly complete, and the Section 6.5 gap reduces to the timing cells.\n"
        "\\end{remark}\n"
        "\n"
        "\\emph{Why joint completeness holds in this class.} The ground truth is the identity \\(B_{0} \\in \\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V}) \\iff z_{0} \\ge 1 + T_{\\mathrm{obs}}\\) established in the reproducible-model paragraph above, so nonviability holds exactly when \\(z_{0} < 1 + T_{\\mathrm{obs}}\\). The two certificates partition that set: the common-action certificate fires exactly when \\(z_{0} < 2\\), and the timing bound fires exactly when \\(z_{0} \\ge 2\\) and \\(T_{\\mathrm{obs}} > z_{0} - 1\\), that is \\(2 \\le z_{0} < 1 + T_{\\mathrm{obs}}\\); the two conditions are disjoint and their union is \\(\\{z_{0} < 1 + T_{\\mathrm{obs}}\\}\\). Every nonviable cell is therefore certified by exactly one certificate, so within the delayed hidden-regime class the pair \\(\\text{(common-action, timing)}\\) is a complete characterization at every horizon, and the gap of Section 6.5 is exactly the timing cells.",
        "joint-completeness",
    )

    # ---- GAP 8: calibration paragraph + updated closing ---------------
    m = sub(
        m,
        "The audit is symbolic and one-dimensional; a multidimensional belief-space\n"
        "numerical campaign is deferred to future work, and the case study makes\n"
        "no claim of a general-purpose computational calculus.",
        "\\textbf{Calibration.} The certificate parameters correspond to quantities estimable from standard stock-assessment practice: the drift margin \\(\\varepsilon\\) is a net growth rate at the floor; the first informative observation time \\(T_{\\mathrm{obs}}\\) is the assessment or review periodicity; the bias \\(b\\) of the certainty-equivalence instance is the systematic error of the indicator; and the floor is the reference point of the management rule. Calibrating these four numbers from a published assessment is all the machinery the certificates require; the present section stays symbolic, and the empirical calibration is left to applied studies.\n"
        "\n"
        "The audit is symbolic and one-dimensional (with the two-dimensional aggregation instance above); a multidimensional belief-space\n"
        "numerical campaign is deferred to future work, and the case study makes\n"
        "no claim of a general-purpose computational calculus.",
        "calibration",
    )

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
