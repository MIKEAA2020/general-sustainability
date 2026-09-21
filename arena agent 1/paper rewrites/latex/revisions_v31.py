#!/usr/bin/env python3
"""v31 verified revisions to the v28 source (applied by build_paper2_v31.py).

Each fix below corresponds to a claim of the external review that was verified
against the manuscript and found correct. Claims found incorrect were rejected
(see the verification report).
"""

def _rep(s, old, new):
    assert old in s, "REVISIONS target not found: %r" % old[:70]
    return s.replace(old, new, 1)


def apply_revisions(t):
    # ---- abstract -----------------------------------------------------------
    # "finite-fibre" overstates checkability (continuous fibres are not finite
    # checks); scope honestly to finite-state / polyhedral / finite-horizon.
    t = _rep(t, "polyhedral, finite-fibre, and finite-horizon cases",
                "finite-state, polyhedral, and finite-horizon cases")
    # the sixth mechanism is a policy-specific (singleton) trap, not a
    # class-emptiness theorem (wording also kept inside the 265-word limit).
    t = _rep(t, "empties the epistemic kernel under a biased",
                "empties the kernel of the uncorrected controller under a biased")
    t = _rep(t, "one minimal construction --- with a sixth\nexhibited under a policy-class restriction.",
                "one minimal --- with a sixth under a\npolicy-class restriction.")
    t = _rep(t, "exists exactly when safe-set", "exists iff safe-set")
    t = _rep(t, "and its consequences for monitoring and institutional design ---",
                "and its monitoring and institutional consequences ---")

    # ---- Section 1.2: make the five-plus-six taxonomy explicit --------------
    t = _rep(t, "and one further mechanism is exhibited by construction:",
                "and a sixth is exhibited under a policy-class restriction:")
    t = _rep(t, "\\textbf{The finite-time exit certificate} (Theorem",
                "\\textbf{The finite-time exit certificate} \\emph{(closed-form conditional)} (Theorem")
    t = _rep(t, "\\textbf{Epistemic emptiness by admissibility} (Proposition",
                "\\textbf{Epistemic emptiness by admissibility} \\emph{(minimal construction)} (Proposition")
    t = _rep(t, "\\textbf{The instantaneous common-action obstruction} (Theorem",
                "\\textbf{The instantaneous common-action obstruction} \\emph{(finitely checkable)} (Theorem")
    t = _rep(t, "\\textbf{The delayed-information obstruction} (Theorem",
                "\\textbf{The delayed-information obstruction} \\emph{(closed-form conditional)} (Theorem")
    t = _rep(t, "\\textbf{The fibre certification criterion} (Proposition",
                "\\textbf{The fibre certification criterion} \\emph{(finitely checkable)} (Proposition")
    t = _rep(t, "\\textbf{The certainty-equivalence trap} (Remark",
                "\\textbf{The certainty-equivalence trap} \\emph{(policy-class restriction)} (Remark")
    # item 6 body: the trap is policy-specific, not a class-emptiness claim.
    t = _rep(t,
        "Even an\n  \\emph{injective} observation empties the epistemic kernel of a system\n"
        "  whose perfect-information kernel is nonempty if the policy class is\n"
        "  restricted to certainty-equivalence controllers that apply a fixed\n"
        "  state-feedback law to the uncorrected observation. The kernel empties\n"
        "  by restriction of the policy class, not by loss of information.",
        "Even an\n  \\emph{injective} observation empties the kernel of a system whose\n"
        "  perfect-information kernel is nonempty for the canonical\n"
        "  certainty-equivalence controller --- the perfect-information zeroing\n"
        "  law applied to the uncorrected observation. The trap is a\n"
        "  policy-specific failure: a controller that uses the observation map's\n"
        "  structure (the bias correction) restores viability.")

    # ---- Section 2.1: Viab quantifier (disturbance reading) ----------------
    t = _rep(t,
        "there exists a state-feedback control keeping the trajectory in\n"
        "  \\(\\mathcal{V}\\) for all time (Aubin, 1991).",
        "there exists a state-feedback control keeping the trajectory in\n"
        "  \\(\\mathcal{V}\\) for all time --- no disturbance, or a known\n"
        "  disturbance trajectory (Aubin, 1991).")

    # ---- Section 2.3: belief definition (applied controls are common) ------
    t = _rep(t,
        "of a regulator who knows the dynamics,\n"
        "the disturbance class, and the record \\((y(s))_{s \\le t}\\) is",
        "of a regulator who knows the dynamics,\n"
        "the disturbance class, its own applied controls \\((u(s))_{s<t}\\), and the record \\((y(s))_{s \\le t}\\) is")
    t = _rep(t,
        "where \\(\\xi(\\cdot)\\) ranges over candidate trajectories: the set of\n"
        "current states compatible with the record.",
        "where the applied control history \\(u(\\cdot)\\) in the dynamics is\n"
        "the regulator's own --- common to every candidate trajectory --- and\n"
        "\\(\\xi(\\cdot)\\) ranges over candidate trajectories: the set of current\n"
        "states compatible with the record and the applied controls.")

    # ---- Section 2.4: define the adverse-selection correspondences ---------
    t = _rep(t,
        "correspondences of the exit certificates are \\(D_{\\varepsilon}(x, u)\\)\n"
        "(Theorem~\\ref{thm:exit}) and \\(D_{\\eta}(x)\\) (Theorem~\\ref{thm:common-action}'s proof, local).",
        "correspondences of the exit certificates are\n"
        "\\(D_{\\varepsilon}(x,u) = \\{ d \\in D(x) : D^+ q(x; f(x,u,d)) \\le -\\varepsilon \\}\\)\n"
        "(Theorem~\\ref{thm:exit}) and\n"
        "\\(D_{\\eta}(x) = \\{ d \\in D(x) : \\nabla q_j(x) \\cdot f(x, a, d) \\le -\\eta/2 \\}\\)\n"
        "(Theorem~\\ref{thm:common-action}'s proof, local).")

    # ---- Section 3.3 ladder: reference the defined set ---------------------
    t = _rep(t, "the\nwitness action sets of Section 3.5 complete the ladder",
                "the\n\\(N\\)-step common safe-action sets \\(\\mathcal{A}_N(B)\\) of Section 3.5 complete the ladder")

    # ---- Section 3.5: define A_N(B) before its use -------------------------
    wk = ("and the finite-horizon kernels by \\(\\mathcal W_0 = \\{B : B\\subseteq\\mathcal V\\}\\),\n"
          "\\(\\mathcal W_{k+1} = \\mathrm{Pre}(\\mathcal W_k)\\).")
    t = _rep(t, wk, wk +
        "\nThe \\(N\\)-step common safe-action set at a belief \\(B\\) is\n"
        "\\(\\mathcal{A}_N(B) = \\bigl\\{ a \\in U^B(B) : \\mathrm{Post}(B,a,y) \\in \\mathcal W_{N-1} \\text{ for every possible } y \\bigr\\}\\),\n"
        "so that \\(B \\in \\mathcal W_N \\iff \\mathcal{A}_N(B) \\neq \\varnothing\\).")
    # initial-observation convention + alternating regulator/nature tree
    t = _rep(t,
        "This is the exact finite-horizon\ncounterpart of the sufficient certificates of Sections 3.1--3.4.",
        "This is the exact finite-horizon\ncounterpart of the sufficient certificates of Sections 3.1--3.4."
        " The recursion reads \\(B_0\\) as the belief after the\n"
        "initial observation has been assimilated, and the tree alternates\n"
        "regulator and nature turns --- the regulator selects an action, the\n"
        "adversary a compatible observation --- the standard alternating\n"
        "structure of partial-information games.")

    # ---- Theorem 3 (delayed): quantify over the implementable blind class --
    t = _rep(t,
        "\\textbf{for every\nopen-loop control on the blind window} --- every measurable\n"
        "\\(u(\\cdot) : [0, T_{\\mathrm{obs}}) \\to \\bigcup_{x \\in B_0} U(x)\\), the\n"
        "class of controls that any observation-based policy realizes before the\n"
        "first informative observation, where its actions are a fixed function of\ntime ---",
        "\\textbf{for every implementable blind-window control} --- every\n"
        "measurable \\(u(\\cdot)\\) on \\([0, T_{\\mathrm{obs}})\\) that is admissible at\n"
        "every compatible state throughout the blind window, \\(u(t) \\in U^B(B_t)\\)\n"
        "with \\(B_t\\) the set-membership belief propagated under \\(u(\\cdot)\\) ---\n"
        "which is exactly the class of controls that an observation-based policy\n"
        "can realize before the first informative observation, where its actions\n"
        "are a fixed function of time ---")
    # proof: handle the inadmissible branch
    t = _rep(t,
        "are a fixed open-loop function of time --- the\n"
        "record carries no informative observation before \\(T_{\\mathrm{obs}}\\),\n"
        "so every observation-equivalent branch induces the same actions --- and\n"
        "(H4.2), applied to that open-loop control, supplies",
        "are a fixed open-loop function of time --- the record carries no\n"
        "informative observation before \\(T_{\\mathrm{obs}}\\), so every\n"
        "observation-equivalent branch induces the same actions; if this function\n"
        "is ever inadmissible at a compatible state the policy fails outright\n"
        "under the Section 2.4 convention, and otherwise (H4.2), applied to this\n"
        "implementable open-loop control, supplies")

    # ---- Section 4.1: the certainly-safe set is a set of observations ------
    t = _rep(t, "it is the region where the index may certify safety",
                "it is the set of observation values where the index may certify safety")

    # ---- Section 4.2 intro: the CE trap is a single policy -----------------
    t = _rep(t,
        "The same emptying occurs with a fully\n"
        "\\emph{injective} observation when the policy class is restricted to\ncertainty-equivalence controllers.",
        "The same emptying occurs with a fully\n"
        "\\emph{injective} observation for a single policy: the canonical\n"
        "certainty-equivalence controller that applies a perfect-information law\nto the uncorrected observation.")

    # ---- Remark 3 (CE trap): singleton claim, not class emptiness ----------
    start = "\\begin{remark}[certainty-equivalence obstruction]\\label{rem:ce-trap}"
    end = "\\end{remark}"
    i = t.index(start)
    j = t.index(end, i) + len(end)
    new_remark = (
        "\\begin{remark}[the certainty-equivalence trap]\\label{rem:ce-trap}\n\n"
        "Consider \\(\\dot S = u - g(S)\\) with \\(u \\in [0, \\bar u]\\), \\(g\\) strictly\n"
        "increasing on \\([S_{\\min}, S^* + b]\\), \\(g(0) = 0\\), and\n"
        "\\(\\mathcal{V} = [S_{\\min}, S^*]\\). Assume the range condition\n"
        "\\(g(S + b) \\le \\bar u\\) for every \\(S \\in [S_{\\min}, S^*]\\), so that the\n"
        "controller below is admissible. Under perfect information the zeroing\n"
        "feedback \\(u(t) = g(S(t))\\) gives \\(\\dot S = 0\\), so every\n"
        "\\(S_0 \\in \\mathcal{V}\\) is viable and\n"
        "\\(\\mathrm{Viab}(\\mathcal{V}; U, \\pi_{\\mathrm{perf}}) = \\mathcal{V} \\neq \\varnothing\\).\n"
        "Now take the injective, biased observation \\(\\hat S = S + b\\) with\n"
        "\\(b > 0\\), and the canonical certainty-equivalence controller: the\n"
        "perfect-information zeroing law applied directly to the uncorrected\n"
        "observation, \\(u = g(\\hat S) = g(S + b)\\). Then\n"
        "\\[\\dot S = g(S + b) - g(S) > 0 \\qquad \\forall S,\\]\n"
        "and since \\(g\\) is strictly increasing on the compact interval\n"
        "\\([S_{\\min}, S^* + b]\\), \\(\\dot S\\) is bounded below by a positive\n"
        "constant there; hence \\(S\\) strictly increases and exits above \\(S^*\\) in\n"
        "finite time from every \\(S_0 \\in \\mathcal{V}\\): the kernel of this single\n"
        "controller is empty. The bias-corrected controller\n"
        "\\(u = g(\\hat S - b) = g(S)\\) uses the observation map's structure, restores\n"
        "\\(\\dot S = 0\\), and keeps the kernel nonempty.\n\n"
        "The mechanism is a \\emph{failure of one policy to use the observation\n"
        "map's structure}, not a loss of information: for a known invertible\n"
        "observation the output-feedback class is as powerful as the\n"
        "state-feedback class. The phenomenon is the viability-theoretic analogue\n"
        "of Witsenhausen's counterexample in stochastic control (Witsenhausen,\n"
        "1968): the information pattern --- not the dynamics and not the\n"
        "constraint --- defeats the uncorrected controller. The remark is\n"
        "policy-specific; it does not assert that the entire certainty-equivalence\n"
        "class empties the kernel.\n\n\\end{remark}"
    )
    t = t[:i] + new_remark + t[j:]

    # ---- Discussion: Table 1 row + surrounding prose (CE trap) ---------------
    t = _rep(t,
        "certainty equivalence (Remark~\\ref{rem:ce-trap}) & "
        "\\(\\mathrm{Viab}(\\mathcal{V};\\Pi_{\\mathrm{CE}})=\\varnothing\\) & correct the known bias \\\\",
        "certainty equivalence (Remark~\\ref{rem:ce-trap}) & "
        "kernel of the uncorrected controller \\(u=g(\\hat S)\\) is empty & correct the known bias \\\\")
    t = _rep(t,
        "The certainty-equivalence trap\n(Remark~\\ref{rem:ce-trap}) limits policy classes.",
        "The certainty-equivalence trap\n(Remark~\\ref{rem:ce-trap}) limits a single uncorrected policy.")

    # ---- Conclusion: the sixth mechanism is policy-specific ------------------
    t = _rep(t,
        "viability impossible, plus one through which the policy class alone\nempties the kernel:",
        "viability impossible, plus one through which a single uncorrected policy\nempties the kernel:")
    t = _rep(t,
        "--- with certainty-equivalence control as the\nsixth, policy-class, mechanism.",
        "--- with the uncorrected certainty-equivalence controller as the\nsixth, policy-specific, mechanism.")

    return t
