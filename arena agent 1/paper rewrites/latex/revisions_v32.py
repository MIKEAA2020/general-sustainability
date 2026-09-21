#!/usr/bin/env python3
"""v32 revisions: Tier A + Tier B + the Helly sparse-witness theorem.

Applied on top of revisions_v31.apply_revisions (same shared v28 source).
"""

def _rep(s, old, new):
    assert old in s, "REVISIONS-v32 target not found: %r" % old[:70]
    return s.replace(old, new, 1)


def apply_revisions_v32(t):
    # ---- Tier A1: convexification wording (H1.2 and H3.3) -----------------
    t = _rep(t,
        "preserves the drift\ninequality because the constraint is convex in the velocity; closure and",
        "preserves the drift\ninequality because, for \\(C^1\\) \\(q\\), the directional derivative\n\\(\\nabla q(x)\\cdot v\\) is affine in the velocity; closure and")
    t = _rep(t,
        "signed drift (the constraint is convex in the velocity).",
        "signed drift (for \\(C^1\\) \\(q\\) the directional derivative is affine in the velocity).")

    # ---- Tier A2: zero-margin phrasing ------------------------------------
    t = _rep(t,
        "Theorem~\\ref{thm:delayed} refines Theorem~\\ref{thm:common-action} quantitatively:\n"
        "the common-action obstruction is a \\textbf{zero-margin formal analogue}\n"
        "of the delayed tube-safety obstruction. The two certificates are separate; the common-action obstruction is the zero-margin instance\n"
        "(\\(\\inf_{x \\in B} q(x) = 0\\) with \\(T_{\\mathrm{obs}} > 0\\) --- any\n"
        "strictly positive observation delay is then too late under a uniform\n"
        "outward drift), and the pair is not related as a\n"
        "\\(T_{\\mathrm{obs}} \\to \\infty\\) limit.",
        "Theorem~\\ref{thm:delayed} complements Theorem~\\ref{thm:common-action} quantitatively:\n"
        "the common-action obstruction is a \\textbf{formal zero-margin counterpart}\n"
        "of the delayed tube-safety obstruction, and the two certificates remain\n"
        "distinct --- the one a local action-feasibility condition, the other a\n"
        "finite-time survival-value condition --- so the pair is not related as a\n"
        "\\(T_{\\mathrm{obs}} \\to \\infty\\) limit.")

    # ---- Tier A3 + A4: continuous-time conventions + sufficiency qualification ----
    t = _rep(t,
        "extensions are noted\nbelow). A policy is observation-based if its action depends on the\n"
        "record only through the information set \\(B_t\\); under the\n"
        "set-membership semantics the information set is a sufficient statistic,\n"
        "so observation-based and record-based policies coincide.",
        "extensions are noted\nbelow). Between reviews the record \\(y(t)=O(x(t))\\) is observed\n"
        "continuously but cannot change the held action; the certificates of\n"
        "Sections 3.2--3.4 use the record only through what it discriminates\n"
        "(observation-equivalence), so they remain valid under any refinement of\n"
        "the within-interval record that does not separate compatible branches.\n"
        "A policy is observation-based if its action depends on the\n"
        "record only through the information set \\(B_t\\); under the delay-free\n"
        "set-membership semantics used here the information set is a sufficient\n"
        "statistic, so observation-based and record-based policies coincide (with\n"
        "delays, hidden parameters, or history-dependent constraints the belief\n"
        "must be augmented and sufficiency is not automatic; Section 6.5).")
    t = _rep(t,
        "which holds in the set-membership semantics used\nthroughout.",
        "which holds in the delay-free set-membership semantics used\nthroughout.")

    # ---- Tier A5: Example 1 vs the discrete abstraction --------------------
    t = _rep(t,
        "\\textbf{A one-step instance.} Example~\\ref{ex:hidden-mode}, read as a\nfinite system on one step, is the smallest obstruction tree.",
        "\\textbf{A one-step instance.} The discrete one-step abstraction of\n"
        "Example~\\ref{ex:hidden-mode} --- transition \\(z^+ = z + \\theta u\\) on\nthe grid \\(z \\in \\{-1,0,1\\}\\), preserving the common-action mechanism\n--- is the smallest obstruction tree.")

    # ---- Tier A6: exponential belief-space caveat --------------------------
    t = _rep(t,
        "so that \\(B \\in \\mathcal W_N \\iff \\mathcal{A}_N(B) \\neq \\varnothing\\).",
        "so that \\(B \\in \\mathcal W_N \\iff \\mathcal{A}_N(B) \\neq \\varnothing\\). "
        "The recursion is exact but of worst-case complexity exponential in\n"
        "\\(|X|\\) --- the belief space contains up to \\(2^{|X|}\\) beliefs --- so\n"
        "finite-checkability is per belief, not a polynomial-time global procedure.")

    # ---- Tier A7: Farkas finite-witness caveat -----------------------------
    t = _rep(t,
        "in the assessment-separation analysis of Abaee (2026).",
        "in the assessment-separation analysis of Abaee (2026). The certificate\n"
        "is finite when the safe-action constraints over the belief admit a finite\n"
        "representation (finitely many constraints across the compatible states);\n"
        "for infinite beliefs a finite-witness reduction is not automatic --- the\n"
        "Helly-type witness of Proposition~\\ref{prop:helly} supplies one under the\n"
        "convexity hypotheses stated there.")

    # ---- Tier B1: reach set is over all solutions --------------------------
    t = _rep(t,
        "\\emph{robust} ---\nall-disturbance --- reachable set",
        "\\emph{robust} ---\nall-disturbance, all-solution --- reachable set")

    # ---- Tier B2: ladder as nested necessary conditions --------------------
    t = _rep(t,
        "The obstruction ladder. The common response sets are nested,",
        "The obstruction ladder. The common response sets form nested necessary\nconditions for viability,")

    # ---- Theorem D (Helly) + its mentions ---------------------------------
    helly = (
        "\\begin{proposition}[sparse common-action witness]\\label{prop:helly}\n"
        "Let \\(B\\subseteq\\mathcal V\\) be an information set, \\(U(x)\\subseteq U\\)\n"
        "with \\(U\\subseteq\\mathbb R^m\\) compact and convex and \\(U(x)\\) convex and\n"
        "closed, let the dynamics be affine in the control,\n"
        "\\(f(x,u,d)=f_0(x,d)+f_u(x,d)\\,u\\), with \\(D(x)\\) compact, and let\n"
        "\\(\\mathcal V\\) have \\(C^1\\) constraint functions \\(q_j\\). Then each\n"
        "safe-control set \\(\\mathcal R_{\\mathcal V}(x)\\) is a compact convex\n"
        "subset of \\(U\\), and the safety-case common-action obstruction\n"
        "\\(\\bigcap_{x\\in B}\\mathcal R_{\\mathcal V}(x)=\\varnothing\\) holds if and\n"
        "only if it is witnessed by at most \\(m+1\\) compatible states: there\n"
        "exist \\(x_1,\\dots,x_{m+1}\\in B\\) with\n"
        "\\(\\bigcap_{i=1}^{m+1}\\mathcal R_{\\mathcal V}(x_i)=\\varnothing\\). The\n"
        "admissibility analogue (with \\(\\mathcal R_{\\mathcal V}(x)\\) replaced by\n"
        "\\(U(x)\\)) holds under the same convexity assumptions.\n"
        "\\end{proposition}\n\n"
        "\\textbf{Proof.} For fixed \\((x,j,d)\\) the inequality\n"
        "\\(\\nabla q_j(x)\\cdot f(x,u,d)\\ge 0\\) is affine in \\(u\\), so\n"
        "\\(\\mathcal R_{\\mathcal V}(x)\\), an intersection of closed halfspaces\n"
        "(over active \\(j\\) and \\(d\\in D(x)\\)) with the closed convex \\(U(x)\\),\n"
        "is closed and convex; contained in the compact \\(U\\), it is compact. If\n"
        "the intersection over all \\(x\\in B\\) is empty, then by compactness some\n"
        "finite subfamily of \\(\\{\\mathcal R_{\\mathcal V}(x)\\}_{x\\in B}\\) already\n"
        "has empty intersection, and by the finite Helly theorem at most \\(m+1\\)\n"
        "members suffice; the converse direction is immediate. \\hfill\\(\\square\\)\n\n"
    )
    t = _rep(t, "\\textbf{A worked certificate (two floors, one scalar action).}",
             helly + "\\textbf{A worked certificate (two floors, one scalar action).}")

    # §1.2: five refinements (add the Helly witness)
    t = _rep(t,
        "Four refinements complete the picture:\na comparison-function form sharpens the exit-time bound\n"
        "(Remark~\\ref{rem:comparison}); a uniform-margin condition connects the\n"
        "instantaneous and tube obstructions\n"
        "(Proposition~\\ref{prop:uniform-margin}); the timing obstruction has a\n"
        "sharp threshold form (Remark~\\ref{rem:sigma}); and backward belief\n"
        "recursion is sound and complete on any finite horizon in finite systems\n"
        "(Theorem~\\ref{thm:finite-horizon}).",
        "Five refinements complete the picture:\na comparison-function form sharpens the exit-time bound\n"
        "(Remark~\\ref{rem:comparison}); a uniform-margin condition connects the\n"
        "instantaneous and tube obstructions\n"
        "(Proposition~\\ref{prop:uniform-margin}); the timing obstruction has a\n"
        "sharp threshold form (Remark~\\ref{rem:sigma}); a Helly-type sparse\n"
        "witness bounds the common-action obstruction by \\(m+1\\) compatible\n"
        "states (Proposition~\\ref{prop:helly}); and backward belief recursion is\n"
        "sound and complete on any finite horizon in finite systems\n"
        "(Theorem~\\ref{thm:finite-horizon}).")

    # §1.4 range note: prop:helly (Proposition 3) falls inside the existing
    # "Propositions~\ref{prop:emptiness}--\ref{prop:ladder}" range (2--5), so no
    # edit is needed here; the range already covers it.

    # worked certificate: the two states are the m+1 witness
    t = _rep(t,
        "restores one-step\nviability (Figure~\\ref{fig:common-action}).",
        "restores one-step\nviability (Figure~\\ref{fig:common-action}). With \\(m=1\\), the two\n"
        "incompatible states are exactly the \\(m+1\\)-state witness of\nProposition~\\ref{prop:helly}.")

    return t
