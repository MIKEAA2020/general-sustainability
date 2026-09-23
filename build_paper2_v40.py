#!/usr/bin/env python3
"""
Pass C (v40) — three strengthening edits:
  * GAP 5  worked POMDP instance (two-floor conflict) in Section 9, plus a
           correctness fix to Proposition (degenerate limit): "V_k -> 0" is not
           derivable for an averaged initial belief; the correct bound is
           V_k <= 1 - min_x b(x) < 1, stated for the deterministic kernels.
  * GAP 6  precise checkability statement for the timing certificate (finite
           blind-window control classes), after Remark (threshold form).
  * GAP 7  a three-state "insufficient post-observation recourse" example,
           added to the supplementary as A.3, with a pointer in Section 6.5(ii).
"""

import sys

LATEX_DIR = "/home/user/arena agent 1/paper rewrites/latex"
MAIN = f"{LATEX_DIR}/paper2_obstruction_calculus_v39_Automatica_routes.tex"
SUPP = f"{LATEX_DIR}/paper2_obstruction_calculus_v39_Automatica_routes_supplementary.tex"
MAIN_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v40_Automatica_routes.tex"
SUPP_OUT = f"{LATEX_DIR}/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.tex"


def sub(text, old, new, name):
    n = text.count(old)
    assert n == 1, f"[{name}] {n} occurrences (expected 1): {old[:70]!r}"
    return text.replace(old, new)


def main():
    m = open(MAIN, encoding="utf-8").read()
    s = open(SUPP, encoding="utf-8").read()

    # ---- GAP 5: correct Prop (degenerate) statement -------------------
    m = sub(
        m,
        "\\begin{proposition}[degenerate (deterministic) limit]\\label{prop:degenerate}\n"
        "Let \\(X, A, D, Y\\) be finite, fix the deterministic maps \\(x^{+} = F(x,a,d)\\) and \\(y = O(x,a,x^{+})\\) of Section 3.1, and suppose the stochastic transition and likelihood have supports \\(\\{F(x,a,d) : d \\in D(x)\\}\\) and \\(\\{O(x,a,x^{+}) : x^{+} \\text{ reachable}\\}\\), converging to the corresponding Dirac measures uniformly in \\((x,a)\\). Then, for a belief \\(b\\) carried by a set \\(B \\subseteq \\mathcal{V}\\), \\(V_{k}(b) \\to 1\\) if \\(B \\in \\mathcal{W}_{k}\\) and \\(V_{k}(b) \\to 0\\) otherwise.\n"
        "\\end{proposition}",
        "\\begin{proposition}[degenerate (deterministic) limit]\\label{prop:degenerate}\n"
        "Let \\(X, A, D, Y\\) be finite with the deterministic maps \\(x^{+} = F(x,a,d)\\) and \\(y = O(x,a,x^{+})\\) of Section 3.1, and let the stochastic transition and likelihood have supports \\(\\{F(x,a,d) : d \\in D(x)\\}\\) and \\(\\{O(x,a,x^{+}) : x^{+} \\text{ reachable}\\}\\). Then the posterior support under the belief-state update is exactly the set-valued post-state \\(\\mathrm{Post}(B,a,y)\\) of Section 3.1, so the support of the belief-state recursion follows the set-valued recursion \\(\\mathcal{W}_{k}\\). For a belief \\(b\\) carried by \\(B \\subseteq \\mathcal{V}\\) and the disturbance read adversarially within its support, \\(V_{k}(b) = 1\\) if \\(B \\in \\mathcal{W}_{k}\\), while if \\(B \\notin \\mathcal{W}_{k}\\) then \\(V_{k}(b) \\le 1 - \\min_{x \\in B} b(x) < 1\\).\n"
        "\\end{proposition}",
        "prop-degenerate",
    )
    m = sub(
        m,
        "\\emph{Proof.} On the finite simplex product, value iteration is continuous in \\((T, g)\\) uniformly in \\((x,a)\\). At the limit the posterior support is exactly the set-valued post-state \\(\\mathrm{Post}(B, a, y)\\) of Section 3.1, and the recursion becomes \\(V_{k+1}(B) = \\max_{a} \\min_{y \\text{ possible}} V_{k}(\\mathrm{Post}(B,a,y))\\) with \\(V_{0}(B) = 1\\); by Theorem~\\ref{thm:finite-horizon} its value is the indicator of \\(B \\in \\mathcal{W}_{k}\\). \\hfill\\(\\square\\)",
        "\\emph{Proof.} Under the deterministic kernels the posterior is supported exactly on \\(\\mathrm{Post}(B,a,y)\\), so the support of the belief evolves by the set-valued recursion. If \\(B \\in \\mathcal{W}_{k}\\), the witness actions of Theorem~\\ref{thm:finite-horizon} keep every compatible branch in \\(\\mathcal{V}\\), giving \\(V_{k}(b) = 1\\). If \\(B \\notin \\mathcal{W}_{k}\\), every action leaves some compatible state \\(x \\in B\\) of mass \\(b(x)\\) with a successor outside \\(\\mathcal{V}\\) under an admissible disturbance, so the one-step survival probability under every action is at most \\(1 - \\min_{x \\in B} b(x)\\); since \\(V_{k}\\) is non-increasing in \\(k\\), \\(V_{k}(b) \\le 1 - \\min_{x \\in B} b(x) < 1\\). \\hfill\\(\\square\\)",
        "prop-degenerate-proof",
    )
    # closing paragraph: name the deficit
    m = sub(
        m,
        "a continuous-state limit requires uniform concentration of the kernels, which is not developed here.",
        "a continuous-state limit requires uniform concentration of the kernels, which is not developed here. The deficit from \\(1\\) is at least the smallest compatible mass \\(\\min_{x \\in B} b(x)\\).",
        "degen-closing",
    )

    # ---- GAP 5: worked POMDP instance before Section 10 ---------------
    m = sub(
        m,
        "\\subsection{10. Conclusion}\\label{conclusion}",
        "\\textbf{A worked instance (the two-floor conflict).} Read the two-floor system of Section 3.4 as a finite POMDP: states \\(x_{1}\\) and \\(x_{2}\\) share one observation; the action \\(u \\in [0,1]\\) is admissible; the one-step violation probability is \\(p(x_{1}, u) = 1\\) for \\(u > 0.4\\) and \\(0\\) otherwise, and \\(p(x_{2}, u) = 1\\) for \\(u < 0.6\\) and \\(0\\) otherwise; the prior is uniform, \\(b_{0} = (1/2, 1/2)\\). Then \\(\\sum_{x} b_{0}(x)\\, p(x, u) \\ge 1/2\\) for every \\(u\\), so Proposition~\\ref{prop:chance} gives \\(V_{k}(b_{0}) \\le 1/2\\) for all \\(k \\ge 1\\), and the chance constraint \\(\\mathbb{P}_{b,\\pi} \\ge 1 - \\varepsilon\\) is infeasible for every \\(\\varepsilon < 1/2\\). The bound is attained: \\(V_{1}(b_{0}) = 1/2\\) (each action sacrifices exactly one floor), and the surviving floor is thereafter kept safe by its own action, so \\(V_{k}(b_{0}) = 1/2\\) for all \\(k\\). At the degenerate limit this reads \\(B_{0} = \\{x_{1}, x_{2}\\} \\notin \\mathcal{W}_{1}\\) with \\(V_{k}(b_{0}) = 1 - \\min_{x \\in B_{0}} b_{0}(x) = 1/2\\), the bound of Proposition~\\ref{prop:degenerate} --- the chance-constrained obstruction evaluated at its exact value.\n"
        "\n"
        "\\subsection{10. Conclusion}\\label{conclusion}",
        "pomdp-instance",
    )

    # ---- GAP 6: checkability paragraph after Remark (sigma) -----------
    m = sub(
        m,
        "delayed-information analogue of the tube and common-action\n"
        "correspondences.\n"
        "\\end{remark}\n"
        "\n"
        "\\begin{figure}[htbp]",
        "delayed-information analogue of the tube and common-action\n"
        "correspondences.\n"
        "\\end{remark}\n"
        "\n"
        "\\textbf{Checkability of the timing certificate.} The drift hypothesis (3) is finitely checkable whenever the blind-window control class is finite: if \\(B_{0}\\) is finite and the admissible blind-window controls form a finite family (hold-until-\\(T_{\\mathrm{obs}}\\) controls with \\(u\\) in a finite set, or piecewise-constant controls on a finite partition), the certificate reduces to the finite check that every candidate control enforces exit before \\(T_{\\mathrm{obs}}\\), each worst-case exit time computed by branchwise integration or by the recursion of Section 3.1. The hidden-regime instance of Section 8 is this check in closed form: the worst branch declines at unit rate, giving \\(\\sigma^{*}(B_{0}) = z_{0} - 1\\), and the certificate fires exactly when \\(T_{\\mathrm{obs}} > z_{0} - 1\\). For continuous control classes the check is a template rather than a finite procedure; closing that gap is part of Open Problem~\\ref{op:dynamic}.\n"
        "\n"
        "\\begin{figure}[htbp]",
        "checkability",
    )

    # ---- GAP 7: pointer in Section 6.5(ii) ----------------------------
    m = sub(
        m,
        "the finite-horizon recursion (Section 3.1) captures that mode, but no continuous-time certificate for it is supplied here.",
        "the finite-horizon recursion (Section 3.1) captures that mode, but no continuous-time certificate for it is supplied here. An explicit instance --- a three-state system whose root belief is one-step viable yet whose post-observation belief is nonviable, with no certificate firing --- is given in the Supplementary Material (S3, A.3).",
        "recourse-pointer",
    )

    # ---- GAP 7: example A.3 in the supplementary ----------------------
    a3 = (
        "\n"
        "\\textbf{A.3 Example (insufficient post-observation recourse).} A three-state system shows the mode of Section 6.5(ii) concretely. Take \\(\\mathcal{V} = \\{x_{1}, x_{2}, x_{4}\\}\\) with \\(x_{3} \\notin \\mathcal{V}\\) a violation, actions \\(A = \\{a, b\\}\\), and no disturbance. Transitions: \\(x_{1}\\) maps to \\(x_{1}\\) under \\(a\\) and to \\(x_{4}\\) under \\(b\\); \\(x_{2}\\) maps to \\(x_{4}\\) under \\(a\\) and to \\(x_{2}\\) under \\(b\\); \\(x_{4}\\) maps to \\(x_{3}\\) under both actions, so \\(x_{4}\\) lies in \\(\\mathcal{V}\\) but outside the kernel. The observation merges \\(x_{1}\\) and \\(x_{2}\\) at the first step and is exact thereafter. The root belief \\(B_{0} = \\{x_{1}, x_{2}\\}\\) is one-step viable: action \\(a\\) keeps both states in \\(\\mathcal{V}\\) (reaching \\(x_{1}\\) and \\(x_{4}\\)), as does \\(b\\) (reaching \\(x_{4}\\) and \\(x_{2}\\)), so the common-action certificate is silent and no exit occurs in the first step. After the first observation, however, the trajectory is at \\(x_{4}\\) for one of the two possible initial states (under \\(a\\) it is \\(x_{2}\\), under \\(b\\) it is \\(x_{1}\\)), and \\(x_{4}\\) has no safe action, so that branch exits at the second step regardless of what the policy learns. Hence \\(B_{0} \\notin \\mathcal{W}_{2}\\) although \\(B_{0} \\in \\mathcal{W}_{1}\\): the failure is a post-observation recourse failure, witnessed only by the recursion (Theorem~\\ref{thm:finite-horizon}) --- the exit certificate is silent at the root because both \\(x_{1}\\) and \\(x_{2}\\) are individually viable under full information, and the timing certificate is silent because the observation arrives without delay.\n"
    )
    s = sub(
        s,
        "factorwise viability at an incompatible operating point is not (A.2).\n"
        "\n"
        "\n"
        "\\section*{S4. Additional figures}",
        "factorwise viability at an incompatible operating point is not (A.2).\n"
        + a3 +
        "\n"
        "\n"
        "\\section*{S4. Additional figures}",
        "supp-a3",
    )

    open(MAIN_OUT, "w", encoding="utf-8").write(m)
    open(SUPP_OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {MAIN_OUT} ({len(m)} bytes)")
    print(f"wrote {SUPP_OUT} ({len(s)} bytes)")


if __name__ == "__main__":
    main()
