#!/usr/bin/env python3
r"""
apply_batch7_wave4_p2.py — fail-loud build of paper2_obstruction_calculus_v9.md from v8.

Implements the wave-4 P2 docket of the joint-audit evaluation record (owner-directed,
cite-don't-drop, non-destructive — hypothesis completion, scoping caveats, relabels,
one-line definitions, wording reframes; never a silent deletion of mathematics):

  R9 [both]   Notation unification + completion of Section 2.4 + per-theorem hypothesis
              renumbering.  Canonical pair frozen: observation structure = $\mathcal{I}$,
              institution = $\mathcal{J}$ (the fraktur institution symbol is retired;
              the v6/v8 projected-kernel placeholder is withdrawn — the hierarchy now
              displays $\mathrm{proj}_{\exists}$ applied explicitly to its two
              information-state terms, and the projection's collection is re-lettered
              $\mathfrak{B}$ off the colliding safe-set letter).  Appendix A.2's Lyapunov
              function is re-lettered $W = S_1 + S_2$ (was the control-set letter $U$).
              Section 2.4 completed: the institution + IRViab definition, the projected
              kernels, the admissibility convention, $D_\varepsilon$, $D_\eta$,
              $\mathcal{A}_{\mathrm{tube}}$ with the robust Reach reading, the formal
              $T_{\mathrm{obs}}$ gloss, $\mathrm{Safe}^{\Pi}_T$, $\Pi_{\mathrm{CE}}$,
              $\mathcal{Y}_{\mathrm{safe}}$, and declared local scopes for the residual
              $a/\varepsilon/d/H/K$ collisions.  Hypotheses renumbered: (H1.1)–(H1.2)
              for Theorem 1, (H3.1)–(H3.3) for Theorem 3, (H4.1)–(H4.3) for Theorem 4.
  R10 [grok]  IRViab one-line definition (the audits' wording, with the canonized
              institution symbol): "the viability kernel of the system whose command
              correspondence is restricted to the institutionally admissible set
              $U_{\mathcal{J}}(x) \subseteq U(x)$" — placed in the hierarchy (§2.1) and
              the notation list (§2.4), scoped DEFINED-NOT-THEOREM, referenced from §6.4.
  Consensus 1 [both]  Theorem 4's circular (H2) restated as (H4.2): a drift condition
              on OPEN-LOOP controls over the blind window $[0, T_{\mathrm{obs}})$ — the
              data of the problem — so (H4.1)'s observation-equivalence (not a
              policy-quantified drift) carries the epistemic step and the timing bound
              (4) is load-bearing.  Proof's first sentence instantiates the restated
              hypothesis; conclusion scoped under (H4.1)–(H4.3); post-proof paragraph
              records the open-loop register, the template status, and the checkable
              special cases.  Claude's δ-minimizer removal DECLINED (grok: keep it).
  Consensus 2 [both]  Theorems 1/3 closed-loop existence hypothesis added — (H1.2) and
              (H3.3): D lower semicontinuous or (locally) constant, or the convexified
              relaxed-inclusion reading (the constraint is convex in the velocity).
              Conclusions scoped under the completed hypotheses; the "exactly
              backwards" convexity parenthetical in Theorem 1's proof corrected;
              §6.5(iv) now names the closed-loop gap.
  Consensus 3 [both]  Theorem 2 reframed in the admissibility register: retitled, the
              §3.2 heading's "hidden modes" withdrawn (Example 1 keeps the genuine
              hidden-mode reading), the state-dependent control set declared a modelling
              primitive with the "inadmissible action = failure" convention explicit,
              the construction presented as the minimal instance of Theorem 3's safety
              case (with the audits' constant-control-set counterfactual recorded), and
              the one-line readings in the abstract, §1.2, §6.1, §7 moved from "safe
              controls" to "admissible controls".  Mathematics unchanged.
  Consensus 5 [both]  Definition 1's clause (i) (EViab, coupled-record semantics, never
              used by a theorem) withdrawn WITH a tombstone in the version log; EViab
              survives as a one-line named contrast class at the a-fortiori caveat
              (referenced by the hierarchy and notation list, so not silently removed).
              Definition 1 defines ERViab alone, in the non-circular
              exists-strategy-for-all-realizations form, with the admissible initial
              beliefs specified.
  Consensus 7 [both]  Corollary 6 restated with the single-floor scoping (crossing one
              floor of an intersection does not put the pair on opposite sides of the
              intersection; the general one-in/one-out form stated alongside); Remark 1's
              $\Pi_{\mathrm{CE}}$ defined (fixed perfect-information regulation laws
              applied uncorrected to the observation; the bias-correcting composite law
              lies outside the class, so the emptiness-by-restriction claim is not
              vacuous).
  Claude section notes  (a) §5(b) reconciled with §6.3 (the correctly-carried-out
              reduction propagates beliefs under a single control signal — common
              controls; the "pointwise selections need not be jointly admissible"
              caveat is scoped to the unchecked-selection reading).  (b) C¹/Dini
              alignment: Theorem 1's statement assumes $q$ of class $C^1$ (the Dini
              display retained with its $C^1$ reduction gloss; the locally Lipschitz
              case still a declared extension); Theorem 4's (H4.2) assumes the same
              class; both proofs' integration step now cites the fundamental theorem of
              calculus along the absolutely continuous trajectory (v8's "Dini
              comparison lemma (Aubin, 1991, Ch. 2)" citation was not one).  (c) The
              hitting-time convention unified: violation = the strict inequality
              $q < 0$; the bound $\inf\{t : q(x(t)) < 0\} \le q(x_0)/\varepsilon$;
              Theorem 4's "violates the constraint at a time not exceeding" phrasing
              corrected; (4) kept strict.

Non-destructive: no frozen result, proof step, table value, or number changes.  Every
edit asserts its anchor occurs exactly once; every mechanical check fails loudly.  The
build is deterministic — running the script twice yields byte-identical output.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper2_obstruction_calculus_v8.md")
DST = os.path.join(HERE, "..", "arena agent 1", "paper rewrites",
                   "paper2_obstruction_calculus_v9.md")


def sub1(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"FAIL [anchor {label}]: expected exactly 1 occurrence, "
                         f"found {n}")
    return text.replace(old, new)


def need(text, needle, label):
    if needle not in text:
        raise SystemExit(f"FAIL [check {label}]: expected string missing: {needle!r}")


def gone(text, needle, label, count=0):
    n = text.count(needle)
    if n != count:
        raise SystemExit(f"FAIL [check {label}]: expected {count} occurrence(s) of "
                         f"{needle!r}, found {n}")


# --------------------------------------------------------------------------
# Version log (v9)
# --------------------------------------------------------------------------
V9_LOG = r"""*Version log (v9).* Implements the wave-4 P2 docket of the joint-audit evaluation record — the notation item R9, the IRViab definition R10, and the theorem-level repairs that v8 registered as follow-ups — non-destructively: hypothesis completion, scoping caveats, relabels, one-line definitions, and wording reframes only. (R9) The observation structure is frozen as $\mathcal{I}$ and the institution as $\mathcal{J}$; the fraktur institution symbol is retired, the kernel hierarchy is displayed with the existential projection applied explicitly to its information-state terms (the projected-kernel placeholder of v8 is withdrawn; the projection's collection is re-lettered off the safe-set letter), the hypotheses are renumbered per theorem — (H1.1)–(H1.2) for Theorem 1, (H3.1)–(H3.3) for Theorem 3, (H4.1)–(H4.3) for Theorem 4 — Appendix A.2's Lyapunov function is re-lettered $W = S_1 + S_2$ (it was the control-set letter; arithmetic unchanged), and Section 2.4 is completed (the institution and its definition, the projected kernels, the admissibility convention, $D_\varepsilon$, $D_\eta$, $\mathcal{A}_{\mathrm{tube}}$ with the robust Reach reading, the formal $T_{\mathrm{obs}}$ gloss, $\mathrm{Safe}^{\Pi}_T$, $\Pi_{\mathrm{CE}}$, $\mathcal{Y}_{\mathrm{safe}}$, and the declared local scopes of $a$, $\varepsilon$, $d$, $H$, $K$). (R10) $\mathrm{IRViab}_{\mathcal{J}}$ receives the audits' one-line definition — the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set $U_{\mathcal{J}}(x) \subseteq U(x)$ — in the hierarchy and the notation list, scoped DEFINED-NOT-THEOREM (no theorem claimed), and referenced from Section 6.4. (Consensus 1) Theorem 4's drift hypothesis is restated as (H4.2), a condition on open-loop controls over the blind window $[0, T_{\mathrm{obs}})$ — the data of the problem, not the policies — so that (H4.1)'s observation-equivalence carries the epistemic step and the timing bound (4) is load-bearing; the proof's first sentence instantiates the restated hypothesis, the conclusion is scoped under (H4.1)–(H4.3), and the post-proof paragraph records the open-loop register, the template status, and the checkable special cases (constant observations; hold-until-$T_{\mathrm{obs}}$ policies); claude's proposal to drop the $\delta$-minimizer apparatus is declined (grok: "the $\delta$-minimizer fallback is correct; keep it"). (Consensus 2) Theorems 1 and 3 receive the closed-loop existence hypothesis — (H1.2) and (H3.3): $D$ lower semicontinuous or (locally) constant, or the convexified relaxed-inclusion reading, which preserves the drift inequality because the constraint is convex in the velocity — with both conclusions scoped under the completed hypotheses; the proof parenthetical that convexity of $D$ was needed "only for Filippov-style closure arguments, which play no role here" was backwards and is corrected (closure and relaxation are the standard tools for exactly this step), and Section 6.5(iv) now names the closed-loop gap. (Consensus 3) Theorem 2 is reframed in the admissibility register: retitled "epistemic emptiness by admissibility — minimal construction", the section heading's "hidden modes" withdrawn (Example 1 keeps the genuine hidden-mode reading), the state-dependent control set declared a modelling primitive with the "inadmissible action = failure" convention explicit, the construction presented as the minimal instance of Theorem 3's safety case with the constant-control-set counterfactual recorded, and the one-line readings in the abstract, Section 1.2, Section 6.1, and Section 7 moved from "safe controls" to "admissible controls". (Consensus 5) Definition 1's clause (i) — $\mathrm{EViab}$ with its coupled-record semantics, never used by a theorem — is withdrawn (this is its tombstone); $\mathrm{EViab}$ survives as a one-line named contrast class at the a-fortiori caveat with no theorem stated for it, and Definition 1 now defines $\mathrm{ERViab}$ alone, in the non-circular exists-strategy-for-all-realizations form, with the admissible initial beliefs specified. (Consensus 7) Corollary 6 is restated with the single-floor scoping (crossing one floor of an intersection does not put the pair on opposite sides of the intersection; the general one-in/one-out form stated alongside), and Remark 1's $\Pi_{\mathrm{CE}}$ is defined — fixed perfect-information regulation laws applied uncorrected to the observation, with the bias-correcting composite law outside the class, so the emptiness-by-restriction claim is no longer vacuous. (Claude section notes) Section 5(b) is reconciled with Section 6.3 (the correctly-carried-out reduction propagates beliefs under a single control signal, so its controls are common controls; the "pointwise selections need not be jointly admissible" caveat is scoped to the unchecked-selection reading); Theorem 1's statement is aligned with its proof — $q$ of class $C^1$, the Dini display retained with its $C^1$ reduction, the locally Lipschitz case still a declared extension, Theorem 4's (H4.2) assuming the same class — and the integration step now cites the fundamental theorem of calculus along the absolutely continuous trajectory (v8's "Dini comparison lemma (Aubin, 1991, Ch. 2)" citation was not one); the hitting-time convention is unified — violation is the strict inequality $q < 0$, the bound is $\inf\{t : q(x(t)) < 0\} \le q(x_0)/\varepsilon$, Theorem 4's "violates the constraint at a time not exceeding" phrasing corrected, and (4) kept strict so a slack still fits before $T_{\mathrm{obs}}$. Registered as follow-ups, deliberately not applied (restructure-scale or new-mathematics items): the singleton-belief identification of $\mathrm{ERViab}$ with $\mathrm{RViab}$ under injective $O$ (a new lemma with proof); the tube form as the official Theorem-3 statement and Theorem-2 plant replacement (grok's elevation items, including the Theorem-5 demotion, the Section 4.2 stub, Appendix A and Section 5(d) relocation); the Marchaud standing-assumption pass, the chattering/relaxed-control remark, the Section 5(c) observer citation, Theorem 2's domain extension below $S = 1$, and the Section 6.4 line errors ("least-constrained" for "most constrained"; "exactly when … and no finer") from claude's section notes. No frozen result, proof body, table, or number is changed beyond the itemized sites."""


def main():
    t = open(SRC, encoding="utf-8").read()

    if not t.startswith("# An Obstruction Calculus for Viability under Incomplete Observation"):
        raise SystemExit("FAIL: v8 title anchor")
    if t.count("*Version log (v8).*") != 1:
        raise SystemExit("FAIL: v8 version log anchor")
    if t.count("## Abstract") != 1:
        raise SystemExit("FAIL: abstract anchor")

    # ----------------------------------------------------- version log splice
    idx = t.find("*Version log (v8).*")
    log_end = t.find("\n\n## Abstract", idx)
    if log_end == -1:
        raise SystemExit("FAIL: version log terminator")
    v9 = t[:idx] + V9_LOG + t[log_end:]

    # =====================================================================
    # R9 / R10 — Section 2.1: the kernel hierarchy (canonical symbols,
    # explicit projected inclusions, IRViab's one-line definition)
    # =====================================================================
    v9 = sub1(
        v9,
        r"- $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$, $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: the **epistemic kernels** — the objects of this paper. Their elements are *states of information*, not physical states (Section 2.3).",
        r"- $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: the **robust epistemic kernel** — the object of this paper (Definition 1). Its elements are *states of information*, not physical states (Section 2.3). The non-robust counterpart $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ is retained as a named contrast class only (the a-fortiori caveat of Section 2.3); no theorem of this paper is stated for it.",
        "§2.1 epistemic-kernel bullet")

    v9 = sub1(
        v9,
        "Projected to physical state space, the informational hierarchy reads",
        r"Projected to physical state space — with $\mathrm{proj}_{\exists}(\mathfrak{B}) = \bigcup_{B \in \mathfrak{B}} B$ the *existential* projection of a collection $\mathfrak{B}$ of information states, applied explicitly to the first two terms, whose native elements are information states — the informational hierarchy reads",
        "§2.1 hierarchy intro")

    v9 = sub1(
        v9,
        r"$$\mathrm{IRViab}_{\mathfrak{I}}(\mathcal{V}) \;\subseteq\; K_{\mathcal{I}} \;\subseteq\; \mathrm{RViab}(\mathcal{V}) \;\subseteq\; \mathrm{Viab}(\mathcal{V}),$$",
        r"$$\mathrm{proj}_{\exists}\big(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\big) \;\subseteq\; \mathrm{proj}_{\exists}\big(\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\big) \;\subseteq\; \mathrm{RViab}(\mathcal{V}) \;\subseteq\; \mathrm{Viab}(\mathcal{V}),$$",
        "§2.1 hierarchy display")

    v9 = sub1(
        v9,
        r"where $K_{\mathcal{I}}$ is the epistemic kernel projected to physical states under the *existential* projection $\mathrm{proj}_{\exists}(\mathfrak{K}) = \bigcup_{B \in \mathfrak{K}} B$ (the hierarchy is read with this projection applied to the first two terms, whose native elements are information states) and $\mathrm{IRViab}_{\mathfrak{I}}$ is the institutionally restricted counterpart (Section 6.4).",
        r"where $\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})$ is the institutionally restricted counterpart (Section 6.4), **defined in one line** as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set $U_{\mathcal{J}}(x) \subseteq U(x)$ — a DEFINED-NOT-THEOREM object: the definition fixes the symbol's meaning, and no theorem of this paper is stated for it.",
        "§2.1 hierarchy where-clause")

    # =====================================================================
    # Consensus 5 — Definition 1 (EViab withdrawn with tombstone; ERViab
    # restated in the non-circular form; admissible initial beliefs)
    # =====================================================================
    v9 = sub1(
        v9,
        "**Definition 1 (epistemic kernels).**\n\n"
        r"""(i) $B_0 \in \mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ if there exists an observation-based policy and an admissible disturbance realization compatible with the record such that every trajectory compatible with the record remains in $\mathcal{V}$ for all time — with the coupling caveat that the record is the one generated by the fixed realization and policy, so "compatible with the record" is read under that same realization, not across all realizations.""" + "\n\n" +
        r"""(ii) $B_0 \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$ if there exists an observation-based policy such that, for *every* admissible disturbance realization compatible with the record, every compatible trajectory remains in $\mathcal{V}$ for all time; trivially $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) \subseteq \mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$.""",
        "**Definition 1 (robust epistemic kernel).**\n\n" +
        r"""$B_0 \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$ if there exists a nonanticipative observation-based policy $\pi$ such that, for every compatible initial state $x_0 \in B_0$ and every admissible disturbance realization $d(\cdot)$, the trajectory of $\dot x = f(x, u(t), d(t))$ generated from $x_0$ by $\pi$'s actions under $d(\cdot)$ — the record being the one that $(\pi, d(\cdot))$ generates — remains in $\mathcal{V}$ for all time. (This is the standard exists-strategy-for-all-realizations form; the qualifier "for every admissible disturbance realization compatible with the record" of the earlier version was circular — the record is generated by the realization — and is replaced by the present quantifier order.) Admissible initial beliefs are the compact information sets $B_0 \subseteq X$ generated by the observation structure — the observation fibres $O^{-1}(y)$, $y \in O(X)$, in the constructions of Sections 3.2–3.4. The existential — non-robust — counterpart $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ is withdrawn as a Definition-level object at this revision (its coupled-record semantics, recorded in the version log, was never used by a theorem) and survives only as the named contrast class of the a-fortiori caveat below.""",
        "Definition 1")

    v9 = sub1(
        v9,
        r"""We use $\mathrm{ERViab}$ throughout, since the disturbance classes of sustainability problems are adverse by construction. The theorems are stated for this robust notion; their emptiness conclusions do not transfer a fortiori to the weaker non-robust one — the robust epistemic kernel is contained in the non-robust one, so an observation-based policy may exist there that no robust policy survives.""",
        r"""We use $\mathrm{ERViab}$ throughout, since the disturbance classes of sustainability problems are adverse by construction. The theorems are stated for this robust notion; their emptiness conclusions do not transfer a fortiori to the weaker non-robust one, $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ — the existential contrast class, in one line: there exist an observation-based policy and *some* admissible disturbance realization under which every compatible trajectory remains in $\mathcal{V}$ for all time (no theorem of this paper is stated for it) — the robust epistemic kernel is contained in the non-robust one, so an observation-based policy may exist there that no robust policy survives.""",
        "§2.3 a-fortiori paragraph (EViab contrast class)")

    v9 = sub1(v9, "With these definitions, the informal statement",
              "With this definition, the informal statement",
              "§2.3 lead-in")

    # =====================================================================
    # R9 — Section 2.4 completed
    # =====================================================================
    v9 = sub1(
        v9,
        r"""We collect the principal symbols used throughout the paper. The state space is $X \subseteq \mathbb{R}^n$; the control set is $U$ (set-valued $U(x)$ at state $x$); the disturbance set is $D$ (set-valued $D(x)$). The dynamics are $\dot x = f(x,u,d)$. The closed constraint set is $\mathcal{V} \subseteq X$, described by finitely many $C^1$ constraint functions $q_j$ ($j = 1,\ldots,m$). The safe-control correspondence at $x \in \mathcal{V}$ is $\mathcal{R}_{\mathcal{V}}(x)$. The observation structure is $\mathcal{I} = (Y, O)$ with observation map $O : X \to Y$; the information set (belief) at time $t$ is $B_t$; the initial belief is $B_0$. The common admissible action set at belief $B$ is $U^B(B) = \bigcap_{x \in B} U(x)$; the common safe-action set is $\mathcal{R}_{\mathcal{V}}^B(B) = \bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x)$. The upper right Dini derivative of $q$ in direction $v$ is $D^+ q(x; v) = \limsup_{h \downarrow 0} [q(x + hv) - q(x)]/h$. The four kernels of the hierarchy are $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}})$, $\mathrm{RViab}(\mathcal{V})$, $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$, $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$, with the institutionally restricted counterpart $\mathrm{IRViab}_{\mathfrak{I}}(\mathcal{V})$. The first informative observation time is $T_{\mathrm{obs}}$.""",
        r"""We collect the principal symbols used throughout the paper and freeze the two structural symbols: the **observation structure** is always $\mathcal{I}$ (calligraphic I) and the **institution** of Section 6.4 is always $\mathcal{J}$ (calligraphic J); the fraktur information symbols of earlier versions are retired, and no other letter serves either role. The state space is $X \subseteq \mathbb{R}^n$; the control set is $U$ (set-valued $U(x)$ at state $x$); the disturbance set is $D$ (set-valued $D(x)$). The dynamics are $\dot x = f(x,u,d)$. The closed constraint set is $\mathcal{V} \subseteq X$, described by finitely many $C^1$ constraint functions $q_j$ ($j = 1,\ldots,m$). The safe-control correspondence at $x \in \mathcal{V}$ is $\mathcal{R}_{\mathcal{V}}(x)$. The observation structure is $\mathcal{I} = (Y, O)$ with observation map $O : X \to Y$; the information set (belief) at time $t$ is $B_t$; the initial belief is $B_0$ — admissible initial beliefs are the compact information sets the observation structure generates, the observation fibres $O^{-1}(y)$, $y \in O(X)$, in the constructions. The common admissible action set at belief $B$ is $U^B(B) = \bigcap_{x \in B} U(x)$ — the only controls an observation-based policy may select without risking inadmissibility, under the convention (explicit from Theorem 2 on) that an action outside $U(x)$ at a compatible state is itself failure; the common safe-action set is $\mathcal{R}_{\mathcal{V}}^B(B) = \bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x)$. The tube-safe action set at review length $\Delta$ is $\mathcal{A}_{\mathrm{tube}}(B, \Delta) = \{ a : \mathrm{Reach}_{[0,\Delta]}(B, a) \subseteq \mathcal{V} \}$, where $\mathrm{Reach}_{[0,\Delta]}(B, a)$ is the *robust* — all-disturbance — reachable set of the system from $B$ under the held action $a$ over $[0,\Delta]$. The first informative observation time is $T_{\mathrm{obs}}$: the first time the observation record discriminates between compatible branches — before it, the branches of Theorem 4's (H4.1) produce identical records. The adverse-selection correspondences of the exit certificates are $D_{\varepsilon}(x, u)$ (Theorem 1) and $D_{\eta}(x)$ (Theorem 3's proof, local). The upper right Dini derivative of $q$ in direction $v$ is $D^+ q(x; v) = \limsup_{h \downarrow 0} [q(x + hv) - q(x)]/h$; for $q$ of class $C^1$ — the class assumed in the exit theorems — $D^+ q(x; v) = \nabla q(x) \cdot v$.

The kernels of the hierarchy are $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}})$ (perfect information), $\mathrm{RViab}(\mathcal{V})$ (robust), and $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$ (the robust epistemic kernel — Definition 1, the object of this paper), with $\mathrm{proj}_{\exists}(\mathfrak{B}) = \bigcup_{B \in \mathfrak{B}} B$ the existential projection of a collection $\mathfrak{B}$ of information states. The non-robust counterpart $\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})$ is retained as a named contrast class only (Section 2.3's a-fortiori caveat; no theorem is stated for it). The institutionally restricted kernel is $\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})$ — DEFINED-NOT-THEOREM: in one line, the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set $U_{\mathcal{J}}(x) \subseteq U(x)$ (Section 6.4). The policy classes are $\pi_{\mathrm{perf}}$ (state feedback), $\Pi_{\mathrm{output}}$, $\Pi_{\mathrm{state}}$, and $\Pi_{\mathrm{CE}}$ — the certainty-equivalence class defined in Remark 1: fixed perfect-information regulation laws applied uncorrected to the observation. The policy-specific safety set of Section 4.1 is $\mathrm{Safe}^{\Pi}_T$; the certainly-safe set of Corollary 6 is $\mathcal{Y}_{\mathrm{safe}}$.

Local scopes, declared once here to prevent the residual letter collisions: $a$ is the strip width in Theorem 1 and the held action in Theorem 3's proof (statement-local); $\varepsilon$ is the drift margin in Theorems 1 and 4, the estimation error of Section 5(c), and the erosion radius of its eroded kernels (site-local); $d$ is the disturbance input in the body and the patch-coupling coefficient of Appendix A (appendix-local); $H$ is the observation-error map $H(\xi, v)$ of Section 2.3's error extension and the harvest vector of Appendix A (appendix-local); $K$ is the safe set of Section 4's certification problems and, locally in Section 2.2, the robust kernel itself, while the buffered set $K_\varepsilon$ of Section 5(c) and the carrying capacities $K_{\max,i}$ of Appendix A.2 are site-local; the Lyapunov function of Appendix A.2 is $W = S_1 + S_2$ (re-lettered from the control-set letter at this revision).""",
        "§2.4 completed notation list")

    # =====================================================================
    # Consensus 3 — Theorem 2's register, one line at each claim site
    # =====================================================================
    v9 = sub1(
        v9,
        r"""2. **Epistemic emptiness by construction** (Theorem 2). A constant observation merges states whose safe controls differ. The unresolved initial observation fibre then lies outside the epistemic kernel, even though every physical state is viable under full information.""",
        r"""2. **Epistemic emptiness by admissibility** (Theorem 2, a minimal construction). A constant observation merges states whose *admissible* controls differ: the state-dependent control set forces a single common action, and that action is unsafe at the boundary, so the unresolved initial observation fibre lies outside the epistemic kernel, even though every physical state is viable under full information. The mechanism is admissibility — the common-action obstruction of Theorem 3 at minimal size — and Example 1 carries the genuine hidden-mode reading.""",
        "§1.2 item 2")

    v9 = sub1(
        v9,
        "an epistemic-emptiness construction where a constant observation merges states whose safe controls differ, a delayed-information obstruction",
        "an epistemic-emptiness construction where a constant observation merges states whose admissible controls differ, a delayed-information obstruction",
        "abstract mechanism-2 line")

    # =====================================================================
    # Consensus 2 (Theorem 1) + C¹/Dini alignment (claude) + hitting-time
    # convention — statement, hypotheses, proof's flagged sentences
    # =====================================================================
    v9 = sub1(
        v9,
        r"""Let $q : X \to \mathbb{R}$ be a constraint function with $\mathcal{V} \subseteq \{ q \ge 0 \}$, and suppose the following hypotheses hold.

(H1) There exist constants $a > 0$ and $\varepsilon > 0$ such that on the strip""",
        r"""Let $q : X \to \mathbb{R}$ be a constraint function of class $C^1$ — the class for which the proof below is carried out; the locally Lipschitz reading remains a declared extension, not proved here — with $\mathcal{V} \subseteq \{ q \ge 0 \}$, and suppose the following hypotheses hold.

(H1.1) There exist constants $a > 0$ and $\varepsilon > 0$ such that on the strip""",
        "Theorem 1 preamble")

    v9 = sub1(
        v9,
        r"""where $D^+ q(x; v) = \limsup_{h \downarrow 0} [q(x + hv) - q(x)]/h$ is the upper right Dini derivative of $q$ in direction $v$.

Then for every admissible control and every initial state $x_0 \in \mathcal{S}_a$ there exists an admissible disturbance realization under which the trajectory leaves $\{ q \ge 0 \}$ — hence leaves $\mathcal{V}$ — by every time strictly larger than $q(x_0)/\varepsilon$, in particular within time at most $a/\varepsilon$ (since $q(x_0) \le a$).""",
        r"""where $D^+ q(x; v) = \limsup_{h \downarrow 0} [q(x + hv) - q(x)]/h$ is the upper right Dini derivative of $q$ in direction $v$ (for $C^1$ $q$, $D^+ q(x; v) = \nabla q(x) \cdot v$ — the form the proof uses).

(H1.2) **Closed-loop existence of the adverse realization.** The disturbance correspondence is lower semicontinuous, or constant, on the strip, so that the state-dependent adverse selection constructed in the proof is realized by an admissible control–disturbance pair for which the Carathéodory existence theorem applies. (Recorded alternative: without (H1.2), the certificate is read against the convexified — relaxed — inclusion $\dot x \in \mathrm{co}\, f(x, u(t), D_{\varepsilon}(x, u(t)))$, which admits solutions under Marchaud-type conditions and preserves the drift inequality because the constraint is convex in the velocity; closure and relaxation are the standard tools for exactly this step.)

Then, under the completed hypotheses (H1.1)–(H1.2), for every admissible control and every initial state $x_0 \in \mathcal{S}_a$ there exists an admissible disturbance realization under which the trajectory attains $q(x(t)) < 0$ — hence leaves $\{ q \ge 0 \} \supseteq \mathcal{V}$ — by every time strictly larger than $q(x_0)/\varepsilon$: $\inf\{ t : q(x(t)) < 0 \} \le q(x_0)/\varepsilon$, in particular within time at most $a/\varepsilon$ (since $q(x_0) \le a$). (Convention, used in both exit theorems: *violation* is the strict inequality $q < 0$; at $q = 0$ the state may still lie on $\partial \mathcal{V} \subseteq \mathcal{V}$.)""",
        "Theorem 1 (H1.2) + conclusion")

    v9 = sub1(
        v9,
        r"""for every measurable control–disturbance pair; convexity of $D$ is not assumed, and is needed only for Filippov-style closure arguments, which play no role here. Fix an admissible control $u(\cdot)$.""",
        r"""for every measurable control–disturbance pair. The adverse realization selected below is *state-dependent*, so its closed-loop realization is an additional requirement — exactly hypothesis (H1.2)'s content ($D$ lower semicontinuous or constant, or the convexified reading of its parenthetical); the remark of earlier versions that convexity of $D$ was needed only for Filippov-style closure arguments was backwards — closure and relaxation are the standard tools for this step — and is corrected at this revision. Fix an admissible control $u(\cdot)$.""",
        "Theorem 1 proof: corrected convexity parenthetical")

    v9 = sub1(
        v9,
        r"""Along the realization $(u(\cdot), d(\cdot))$ from $x_0$, the Dini comparison lemma (e.g. Aubin, 1991, Ch. 2) integrates the inequality to""",
        r"""Along the realization $(u(\cdot), d(\cdot))$ from $x_0$, the fundamental theorem of calculus along the absolutely continuous trajectory integrates the inequality to""",
        "Theorem 1 proof: integration citation")

    # =====================================================================
    # Consensus 3 — §3.2 heading, intro, Theorem 2, post-proof paragraph
    # =====================================================================
    v9 = sub1(v9, "### 3.2 Epistemic emptiness: hidden modes",
              "### 3.2 Epistemic emptiness by admissibility: a minimal construction",
              "§3.2 heading")

    v9 = sub1(
        v9,
        r"""The remaining obstructions are *purely informational*. They apply to systems in which every state is individually viable under full information, and the kernel empties only because the observation structure merges states with incompatible safe controls. In ecological terms,""",
        r"""The remaining obstructions apply to systems in which every state is individually viable under full information and the kernel empties only under the observation structure; their register is stated per mechanism. The minimal construction of this section empties the kernel through *admissibility* — a state-dependent control set whose common action is forced and unsafe at the boundary; the common-action obstruction of the next section and Example 1's hidden-parameter conflict are the informational register proper, merging states with incompatible safe controls. In ecological terms,""",
        "§3.2 intro")

    v9 = sub1(
        v9,
        "**Theorem 2 (epistemic emptiness by construction).**\n\n"
        r"""There exists a system with $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}}) = \mathcal{V} \neq \varnothing$ such that, for a non-injective observation map $O$, every admissible initial information state — the observation fibres $B_0 = O^{-1}(O(S_0))$, $S_0 \in \mathcal{V}$ — lies outside $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: the epistemic kernel over the fibre-induced initial beliefs is empty.""",
        "**Theorem 2 (epistemic emptiness by admissibility — minimal construction).**\n\n"
        r"""There exists a system with $\mathrm{Viab}(\mathcal{V}; U, \pi_{\mathrm{perf}}) = \mathcal{V} \neq \varnothing$ such that, for a non-injective observation map $O$, every admissible initial information state — the observation fibres $B_0 = O^{-1}(O(S_0))$, $S_0 \in \mathcal{V}$ — lies outside $\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: the epistemic kernel over the fibre-induced initial beliefs is empty. The register of the mechanism is *admissibility* rather than a hidden mode: the state-dependent control set of the construction leaves a single common action at the merged belief — one that is outward-drifting at the boundary state — so the emptiness is the common-action obstruction (Theorem 3's safety case) at minimal size, manufactured by the control-set primitive rather than by information; the genuine hidden-mode instance is Example 1.""",
        "Theorem 2 title + register clause")

    v9 = sub1(
        v9,
        r"""The construction isolates the mechanism: the observation merges states whose safe controls differ, and the merged belief admits no common control. The example also shows the empty-kernel phenomenon at its minimal size — two control values, one scalar state. The next theorem generalizes the mechanism from constant observations to arbitrary information sets.""",
        r"""The construction isolates the mechanism, and its register is admissibility: the observation merges states whose *admissible* controls differ — the merged belief admits a common admissible control (the singleton $\{0\}$) but no common *safe* control, because that singleton is outward-drifting at the boundary state $S = 1$. The "inadmissible action = failure" convention is thereby exercised explicitly: an action outside $U(x)$ at a compatible state $x$ is itself failure, and the state-dependent control set $U(S) = \{0, r(S)\}$ is a modelling primitive carrying that convention (Theorem 3's admissibility case uses the same convention, stated there). The example also shows the empty-kernel phenomenon at its minimal size — two control values, one scalar state — as the minimal instance of Theorem 3 rather than a mechanism of equal rank; with a constant control set $[0, \bar u]$ in the same plant the fibre is epistemically viable (a constant control $u = r(m)$, $m \in (1,2)$, drives every state of the fibre to the rest point $m \in (1,2)$), which is why the construction is not presented as a hidden-mode mechanism. The next theorem states the general obstruction, of which this construction is the minimal instance.""",
        "§3.2 post-proof paragraph")

    # =====================================================================
    # Consensus 2 (Theorem 3) — preamble, (H3.3), proof pointer, robust Reach
    # =====================================================================
    v9 = sub1(
        v9,
        r"""Let $B$ be an information set of the declared observation structure. Suppose the following hypotheses hold.

(H1) The selected action is held""",
        r"""Let $B \subseteq \mathcal{V}$ be an information set of the declared observation structure (the safe-control correspondence $\mathcal{R}_{\mathcal{V}}$ is defined on $\mathcal{V}$, so the belief is taken inside it). Suppose the following hypotheses hold.

(H3.1) The selected action is held""",
        "Theorem 3 preamble")

    v9 = sub1(v9, "(H2) Either the **common admissible action set** is empty,",
              "(H3.2) Either the **common admissible action set** is empty,",
              "Theorem 3 (H3.2)")

    v9 = sub1(
        v9,
        r"""\text{(safety obstruction)}$$

Then $B \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: every compatible state""",
        r"""\text{(safety obstruction)}$$

(H3.3) **Closed-loop existence of the local adverse selection (safety case).** The disturbance correspondence is lower semicontinuous, or locally constant near the boundary point at which the obstruction fires, so that the local adverse selection of the proof is realized along the compatible trajectory; alternatively, the certificate is read against the convexified — relaxed — inclusion, which preserves the signed drift (the constraint is convex in the velocity).

Then, under the completed hypotheses (H3.1)–(H3.3), $B \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: every compatible state""",
        "Theorem 3 (H3.3) + conclusion")

    v9 = sub1(
        v9,
        r"""Let the disturbance realize this selection on a small initial interval; then along the compatible trajectory from $\bar x$""",
        r"""Let the disturbance realize this selection on a small initial interval (its closed-loop realization is hypothesis (H3.3)'s content — $D$ lower semicontinuous or locally constant near $\bar x$, or the convexified reading); then along the compatible trajectory from $\bar x$""",
        "Theorem 3 proof: selection realization")

    v9 = sub1(
        v9,
        r"""$$\mathcal{A}_{\mathrm{tube}}(B, \Delta) \;=\; \Big\{ a : \mathrm{Reach}_{[0,\Delta]}(B, a) \subseteq \mathcal{V} \Big\},$$
and $\mathcal{A}_{\mathrm{tube}}(B, \Delta) = \varnothing$ certifies""",
        r"""$$\mathcal{A}_{\mathrm{tube}}(B, \Delta) \;=\; \Big\{ a : \mathrm{Reach}_{[0,\Delta]}(B, a) \subseteq \mathcal{V} \Big\},$$
with $\mathrm{Reach}_{[0,\Delta]}(B, a)$ the robust — all-disturbance — reachable set (the reading declared in Section 2.4), and $\mathcal{A}_{\mathrm{tube}}(B, \Delta) = \varnothing$ certifies""",
        "§3.3 tube form: robust Reach gloss")

    # =====================================================================
    # Consensus 1 — Theorem 4's (H4.2) open-loop restatement + proof
    # instantiation + template scoping; hypothesis renumbering
    # =====================================================================
    v9 = sub1(v9, "(H1) No informative observation arrives",
              "(H4.1) No informative observation arrives",
              "Theorem 4 (H4.1)")

    v9 = sub1(
        v9,
        r"""(H2) There exist a constraint function $q$ with $\mathcal{V} \subseteq \{ q \ge 0 \}$ and a constant $\varepsilon > 0$ such that, for every observation-based policy, there is a compatible initial state $x^* \in B_0$ attaining $q(x^*) = \inf_{x \in B_0} q(x)$ (with $B_0$ compact and $q$ lower semicontinuous; otherwise replace the infimum by $\inf q + \delta$ for an arbitrary $\delta$-minimizer, let $\delta \downarrow 0$, and read the timing bound with $\inf q + \delta$) and an admissible disturbance realization such that, along the realized trajectory from $x^*$ under the policy's actions, the record remains compatible and""",
        r"""(H4.2) There exist a constraint function $q$ of class $C^1$ (the class of Theorem 1's proof) with $\mathcal{V} \subseteq \{ q \ge 0 \}$ and a constant $\varepsilon > 0$ such that, **for every open-loop control on the blind window** — every measurable $u(\cdot) : [0, T_{\mathrm{obs}}) \to \bigcup_{x \in B_0} U(x)$, the class of controls that any observation-based policy realizes before the first informative observation, where its actions are a fixed function of time — there are a compatible initial state $x^* \in B_0$ attaining $q(x^*) = \inf_{x \in B_0} q(x)$ (with $B_0$ compact and $q$ lower semicontinuous; otherwise replace the infimum by $\inf q + \delta$ for an arbitrary $\delta$-minimizer, let $\delta \downarrow 0$, and read the timing bound with $\inf q + \delta$) and an admissible disturbance realization such that, along the realized trajectory from $x^*$ under that open-loop control, the record remains compatible and""",
        "Theorem 4 (H4.2) open-loop restatement")

    v9 = sub1(v9, "(H3) The timing bound holds:", "(H4.3) The timing bound holds:",
              "Theorem 4 (H4.3)")

    v9 = sub1(
        v9,
        r"""Then $B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: information may be accurate but arrive too late.""",
        r"""Then, under the completed hypotheses (H4.1)–(H4.3), $B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})$: information may be accurate but arrive too late.""",
        "Theorem 4 conclusion")

    v9 = sub1(
        v9,
        r"""*Proof.* Fix any observation-based policy. By hypothesis there is a compatible initial state $x^*$ with $q(x^*) = \inf_{x \in B_0} q(x)$ and an admissible disturbance realization satisfying (3), observation-equivalent on $[0, T_{\mathrm{obs}})$ to the other compatible branches. The Dini comparison lemma integrates (3) to""",
        r"""*Proof.* Fix any observation-based policy. By (H4.1) its actions on $[0, T_{\mathrm{obs}})$ are a fixed open-loop function of time — the record carries no informative observation before $T_{\mathrm{obs}}$, so every observation-equivalent branch induces the same actions — and (H4.2), applied to that open-loop control, supplies a compatible initial state $x^*$ with $q(x^*) = \inf_{x \in B_0} q(x)$ and an admissible disturbance realization satisfying (3) along the trajectory from $x^*$ under those actions, observation-equivalent on $[0, T_{\mathrm{obs}})$ to the other compatible branches. For $q$ of class $C^1$ — the class assumed in (H4.2) — the fundamental theorem of calculus along the absolutely continuous trajectory integrates (3) to""",
        "Theorem 4 proof: open-loop instantiation")

    v9 = sub1(
        v9,
        r"""while $q(x(t)) > 0$, so the trajectory violates the constraint at a time not exceeding $t^* = \inf_{x \in B_0} q(x) / \varepsilon$ (the same argument with the $\delta$-minimizer bounds the violation time by $(\inf q + \delta)/\varepsilon$), which by (4) is strictly less than $T_{\mathrm{obs}}$. Until $t^*$,""",
        r"""while $q(x(t)) > 0$, so the trajectory attains the violation convention of Theorem 1 — the strict inequality $q(x(t)) < 0$ — by every time strictly larger than $t^* = \inf_{x \in B_0} q(x) / \varepsilon$ (in particular $\inf\{ t : q(x(t)) < 0 \} \le t^*$; the same argument with the $\delta$-minimizer bounds the violation time by $(\inf q + \delta)/\varepsilon$), and $t^*$ by (4) is strictly less than $T_{\mathrm{obs}}$ — the violation is strict and precedes the first informative observation. Until $t^*$,""",
        "Theorem 4 proof: hitting-time convention")

    v9 = sub1(
        v9,
        r"""The hypothesis (3) is the set-membership form of the drift condition: for *every* policy there is a compatible state and disturbance enforcing the drift; the adversary selects the true state and the disturbance, and the observations cannot expose the selection in time. Condition (4) is the **timing bound**: the first informative observation must precede the enforced exit time $\inf q / \varepsilon$.""",
        r"""The hypothesis (3) is the set-membership form of the drift condition, quantified over open-loop controls on the blind window — a condition on the data of the problem, not on the policies: for every such control there is a compatible state and disturbance enforcing the drift; the adversary selects the true state and the disturbance, and the observations cannot expose the selection in time. It is this open-loop form that makes the timing bound (4) load-bearing — (H4.1) converts the policy's actions into one open-loop control, (H4.2) supplies the drift against it, and (4) then makes the obstruction epistemic rather than dynamic. The hypothesis is checkable in its special cases (constant observations; hold-until-$T_{\mathrm{obs}}$ policies) and is a template in the general case, as the abstract records. Condition (4) is the **timing bound**: it states that the observation arrives *after* the enforced exit time — the cause of the obstruction; read as the design requirement it inverts, the first informative observation must precede the enforced exit time $\inf q / \varepsilon$.""",
        "Theorem 4 post-proof paragraph")

    # =====================================================================
    # Consensus 7 — Corollary 6 single-floor repair
    # =====================================================================
    v9 = sub1(
        v9,
        r"""**Corollary 6 (safety-crossing fibres and the certainly-safe set).** If two admissible states share an observation and lie on opposite sides of a component safety constraint, no exact observation-only certificate exists. The largest set of observations""",
        r"""**Corollary 6 (safety-crossing fibres and the certainly-safe set).** If two admissible states share an observation and lie on opposite sides of the *same* component safety constraint — with the safe set of that certification problem read as the single floor $K = \{ q_j \ge 0 \}$; or, in the general form of the hypothesis, one of the two states lies in $K$ and the other outside $K$ — no exact observation-only certificate exists. (Crossing one floor of an intersection $K = \bigcap_j \{ q_j \ge 0 \}$ does not by itself put the pair on opposite sides of the intersection — the state satisfying floor $j$ may violate floor $i$ — hence the single-floor scoping.) The largest set of observations""",
        "Corollary 6 statement")

    v9 = sub1(
        v9,
        r"""*Proof.* A safety-crossing fibre violates (5), so Theorem 5 denies the certifier. On $\mathcal{Y}_{\mathrm{safe}}$""",
        r"""*Proof.* In the general form (one state in $K$, one outside), the fibre violates (5) for that $K$, so Theorem 5 denies the certifier; in the single-floor form it violates (5) for the floor's own certification problem ($K = \{q_j \ge 0\}$). On $\mathcal{Y}_{\mathrm{safe}}$""",
        "Corollary 6 proof")

    # =====================================================================
    # Consensus 7 — Remark 1's Pi_CE class definition
    # =====================================================================
    v9 = sub1(
        v9,
        r"""Now take the injective, biased observation $\hat S = S + b$ with $b > 0$, and restrict the policy class to **certainty-equivalence controllers** — causal maps that apply a fixed state-feedback law directly to the observation without correcting the bias: $u = g(\hat S)$. Then""",
        r"""Now take the injective, biased observation $\hat S = S + b$ with $b > 0$, and restrict the policy class to the **certainty-equivalence class** $\Pi_{\mathrm{CE}}$, defined here (one formal definition, recorded at this revision): $\Pi_{\mathrm{CE}}$ is the class of causal controllers obtained by taking a fixed *perfect-information regulation law* $k$ of the plant and applying it directly to the uncorrected observation, $u = k(\hat S)$ — no use of the observation map's structure (here, the bias $b$) enters the law. The trap below is the member $k = g$: $u = g(\hat S)$. Then""",
        "Remark 1 Pi_CE definition")

    v9 = sub1(
        v9,
        r"""An observer who inverts the bias, $u = g(\hat S - b) = g(S)$, recovers the perfect-information kernel. The remark is the mechanism""",
        r"""An observer who inverts the bias, $u = g(\hat S - b) = g(S)$, recovers the perfect-information kernel — and lies outside $\Pi_{\mathrm{CE}}$, since the composite law $g(\cdot - b)$ is not a perfect-information law of the plant applied uncorrected. The remark is the mechanism""",
        "Remark 1 corrected-controller scoping")

    # =====================================================================
    # Claude section note (a) — §5(b) reconciled with §6.3
    # =====================================================================
    v9 = sub1(
        v9,
        r"""The reduction is exact for value functions; what it does not supply is a *common prescription* — the estimation-space policy is a set-valued feedback, and its pointwise selections need not be jointly admissible. The common-action obstruction (Theorem 3) is precisely the certificate that no such joint selection exists at the information state in question.""",
        r"""The reduction is exact for value functions; what it does not supply is a *common prescription*. The exact relationship, reconciled with Section 6.3: correctly carried out under the set-membership semantics, the estimation-space solution propagates the belief under a single control signal, so its controls *are* common controls and joint admissibility is built into the estimation-space problem's own admissibility — that is Section 6.3's statement, and it is the correct one for the semantics adopted here. The caveat that the estimation-space policy is a set-valued feedback *whose pointwise selections, taken without that joint-admissibility check, need not be jointly admissible* concerns the unchecked selection reading, not the reduction itself; the common-action obstruction (Theorem 3) is precisely the certificate that no jointly admissible selection exists at the information state in question.""",
        "§5(b) reconciliation")

    # =====================================================================
    # Consensus 3 tail + §6.5(iv) + R10 §6.4 reference
    # =====================================================================
    v9 = sub1(
        v9,
        "The epistemic-emptiness construction (Theorem 2) exhibits the mechanism at minimal size: one scalar state, two safe controls, one constant observation.",
        "The epistemic-emptiness construction (Theorem 2) exhibits the mechanism at minimal size — one scalar state, two admissible controls, one constant observation — in the admissibility register of Section 3.2.",
        "§6.1 mechanism list")

    v9 = sub1(
        v9,
        r"""The epistemic-institutional kernel $\mathrm{IRViab}_{\mathfrak{I}}$ combines them: an institution restricted in what it may observe *and* in what it may command inherits both contractions.""",
        r"""The epistemic-institutional kernel $\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})$ — defined in one line at Section 2.1 as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set $U_{\mathcal{J}}(x) \subseteq U(x)$; DEFINED-NOT-THEOREM, no theorem claimed for it — combines them: an institution restricted in what it may observe *and* in what it may command inherits both contractions.""",
        "§6.4 Institutions + IRViab reference")

    v9 = sub1(
        v9,
        r"""(iv) Theorem 1's measurable-selection step presupposes the closed-graph regularity of Section 2.1; without it the certificate remains a heuristic.""",
        r"""(iv) Theorem 1's adversarial-realization step presupposes both the closed-graph regularity of Section 2.1 and the closed-loop existence hypothesis (H1.2) — $D$ lower semicontinuous or constant, or the convexified reading; without these the certificate remains a heuristic.""",
        "§6.5(iv) closed-loop gap")

    v9 = sub1(
        v9,
        "a constant observation can merge states with incompatible safe controls; the compatible states",
        "a constant observation can merge states with incompatible admissible controls (Theorem 2's admissibility register); the compatible states",
        "§7 conclusion mechanism line")

    # =====================================================================
    # R9 — Appendix A.2 Lyapunov re-letter U -> W (notation only)
    # =====================================================================
    v9 = sub1(v9, "For the coupled system, define $U = S_1 + S_2$; then",
              "For the coupled system, define the Lyapunov function $W = S_1 + S_2$ "
              "(the letter $W$ is used because $U$ is the control-set letter of "
              "Section 2.4); then",
              "A.2 Lyapunov definition")
    v9 = sub1(v9, r"$$\dot U = \phi_1(S_1) + \phi_2(S_2) \le 0,$$",
              r"$$\dot W = \phi_1(S_1) + \phi_2(S_2) \le 0,$$",
              "A.2 Lyapunov display")
    v9 = sub1(v9, "Then $U$ is non-increasing and bounded below by $(C_1 + C_2)/2$, "
              "so $U(t) \\downarrow U_\\infty \\ge (C_1 + C_2)/2$",
              "Then $W$ is non-increasing and bounded below by $(C_1 + C_2)/2$, "
              "so $W(t) \\downarrow W_\\infty \\ge (C_1 + C_2)/2$",
              "A.2 Lyapunov monotonicity")
    v9 = sub1(v9, "and $\\dot U \\equiv 0$ on it (otherwise $U$ would keep decreasing "
              "along the set)",
              "and $\\dot W \\equiv 0$ on it (otherwise $W$ would keep decreasing "
              "along the set)",
              "A.2 Lyapunov omega-limit clause")

    # =====================================================================
    # Mechanical checks
    # =====================================================================
    if not v9.startswith("# An Obstruction Calculus for Viability under Incomplete Observation"):
        raise SystemExit("FAIL: title damaged")
    if v9.count("*Version log (v9).*") != 1 or v9.count("*Version log (v8).*") != 0:
        raise SystemExit("FAIL: version log not replaced exactly once")
    body = "\n".join(l for l in v9.split("\n") if not l.startswith("*Version log (v9).*"))
    log = [l for l in v9.split("\n") if l.startswith("*Version log (v9).*")][0]

    # R9: canonical symbols; no fraktur information symbols; no K_I; no bare H-labels
    for needle, label in [
        (r"\mathfrak{I}", "retired fraktur institution symbol (whole file)"),
        (r"\mathfrak{J}", "fraktur J (never used)"),
        (r"\mathfrak{K}", "retired fraktur collection symbol (whole file)"),
        (r"K_{\mathcal{I}}", "withdrawn projected-kernel placeholder (whole file)"),
    ]:
        gone(v9, needle, label)
    gone(body, "(H1) ", "bare (H1) label")
    gone(body, "(H2) ", "bare (H2) label")
    gone(body, "(H3) ", "bare (H3) label")
    for needle, label in [
        ("(H1.1)", "Theorem 1 hypothesis (H1.1)"),
        ("(H1.2)", "Theorem 1 hypothesis (H1.2)"),
        ("(H3.1)", "Theorem 3 hypothesis (H3.1)"),
        ("(H3.2)", "Theorem 3 hypothesis (H3.2)"),
        ("(H3.3)", "Theorem 3 hypothesis (H3.3)"),
        ("(H4.1)", "Theorem 4 hypothesis (H4.1)"),
        ("(H4.2)", "Theorem 4 hypothesis (H4.2)"),
        ("(H4.3)", "Theorem 4 hypothesis (H4.3)"),
    ]:
        need(body, needle, label)

    # R10: IRViab definition present at its three sites, DEFINED-NOT-THEOREM
    if body.count(r"IRViab}_{\mathcal{J}}") != 4:
        raise SystemExit("FAIL [R10]: IRViab_J must appear exactly 4 times in body "
                         "(hierarchy display, hierarchy where-clause, §2.4, §6.4)")
    if body.count("viability kernel of the system whose command correspondence is "
                  "restricted to the institutionally admissible set") != 3:
        raise SystemExit("FAIL [R10]: the one-line IRViab definition must appear at "
                         "its three sites")
    if body.count("DEFINED-NOT-THEOREM") != 3:
        raise SystemExit("FAIL [R10]: DEFINED-NOT-THEOREM scoping must appear 3 times")

    # Consensus 3: hidden modes gone from the claim sites; Example 1 keeps its
    # genuine hidden-mode reading; admissibility register at every one-line site
    gone(body, "hidden modes", "§3.2 heading's 'hidden modes'")
    if body.count("hidden-mode conflict") != 1:
        raise SystemExit("FAIL [Thm 2 register]: exactly one 'hidden-mode conflict' "
                         "site expected (Example 1's title)")
    gone(body, "safe controls differ", "abstract/§1.2 old register")
    gone(body, "two safe controls", "§6.1 old register")
    gone(body, "incompatible safe controls; the compatible", "§7 old register")
    if body.count("incompatible safe controls") != 2:
        raise SystemExit("FAIL [Thm 2 register]: 'incompatible safe controls' must "
                         "survive exactly twice (the scoped §3.2 intro and §6.4's "
                         "Theorem-3 reading)")
    need(body, "inadmissible action = failure", "the explicit convention")
    need(body, "epistemic emptiness by admissibility", "retitled Theorem 2")
    need(body, "admissibility register", "register named at the claim sites")

    # Consensus 1: Theorem 4's open-loop hypothesis + template scoping
    need(body, "for every open-loop control on the blind window", "(H4.2) restated")
    need(body, "are a fixed open-loop function of time", "proof instantiation")
    need(body, "a condition on the data of the problem, not on the policies",
         "post-proof register")
    need(body, "is a template in the general case", "template scoping")
    need(body, "hold-until-$T_{\\mathrm{obs}}$ policies", "checkable special cases")
    need(body, "makes the timing bound (4) load-bearing", "load-bearing statement")

    # Consensus 2: closed-loop existence hypotheses + corrected parenthetical
    need(body, "(H1.2) **Closed-loop existence of the adverse realization.**",
         "Theorem 1 (H1.2)")
    need(body, "(H3.3) **Closed-loop existence of the local adverse selection",
         "Theorem 3 (H3.3)")
    need(body, "was backwards — closure and relaxation are the standard tools",
         "corrected convexity parenthetical")
    need(body, "the closed-loop existence hypothesis (H1.2)", "§6.5(iv)")
    need(body, "or the convexified reading", "convexified alternative (Thm 3 proof)")
    gone(body, "which play no role here", "the backwards remark")

    # Consensus 5: EViab demoted to contrast class, no Definition clause (i)
    gone(body, "**Definition 1 (epistemic kernels).**", "old Definition 1 title")
    gone(body, "coupling caveat", "the withdrawn coupled-record caveat")
    need(body, "**Definition 1 (robust epistemic kernel).**", "new Definition 1 title")
    need(body, "named contrast class", "EViab's demoted status")
    need(body, "is withdrawn as a Definition-level object", "the withdrawal record")
    if body.count("EViab") != 4:
        raise SystemExit("FAIL [EViab]: expected 4 body occurrences (bullet, "
                         "Definition, a-fortiori, §2.4)")
    if v9.count("EViab") != 6:
        raise SystemExit("FAIL [EViab]: whole-file count must be 6 "
                         "(4 body + 2 version-log tombstone mentions)")

    # Consensus 7: Corollary 6 single-floor; Remark 1's Pi_CE
    need(body, "lie on opposite sides of the *same* component safety constraint",
         "Corollary 6 single-floor scoping")
    need(body, "does not by itself put the pair on opposite sides of the intersection",
         "Corollary 6 intersection caveat")
    need(body, "fixed *perfect-information regulation law*", "Pi_CE definition")
    need(body, "not a perfect-information law of the plant applied uncorrected",
         "Pi_CE membership scoping")

    # Claude section notes: (a) reconciliation, (b) C1/Dini, (c) hitting time
    need(body, "reconciled with Section 6.3", "§5(b)–§6.3 reconciliation")
    need(body, "concerns the unchecked selection reading, not the reduction itself",
         "reconciliation caveat scoping")
    need(body, "be a constraint function of class $C^1$", "Theorem 1 C1 hypothesis")
    need(body, "constraint function $q$ of class $C^1$", "Theorem 4 C1 hypothesis")
    if body.count("the fundamental theorem of calculus along the absolutely "
                  "continuous trajectory") != 2:
        raise SystemExit("FAIL [C1]: FTC integration citation must appear twice "
                         "(Theorems 1 and 4)")
    gone(body, "Dini comparison lemma", "the misattributed citation")
    gone(body, "e.g. Aubin, 1991, Ch. 2", "the wrong Aubin citation")
    if body.count(r"\inf\{ t : q(x(t)) < 0 \}") != 2:
        raise SystemExit("FAIL [hitting time]: the unified exit-time bound must "
                         "appear in both exit theorems")
    need(body, "*violation* is the strict inequality $q < 0$", "the convention note")
    need(body, "attains the violation convention of Theorem 1",
         "Theorem 4 proof convention alignment")
    gone(body, "violates the constraint at a time not exceeding",
         "Theorem 4's old hitting-time phrasing")

    # R9: robust Reach gloss; frozen content untouched
    need(body, "the robust — all-disturbance — reachable set", "robust Reach gloss")
    src_body = "\n".join(l for l in t.split("\n")
                         if not l.startswith("*Version log (v8).*"))
    for needle in ["0.31", "0.10", "0.25", "d = 0.2", "(0.5, 0.8)",
                   "r_i C_i / 4", "K_{\\max,1}", "$a/\\varepsilon$",
                   "$\\inf_{x \\in B_0} q(x) / \\varepsilon$",
                   "$\\inf q + \\delta$", "$T_{\\mathrm{obs}} >$"]:
        if src_body.count(needle) != body.count(needle):
            raise SystemExit(f"FAIL [frozen]: count of {needle!r} changed "
                             f"({src_body.count(needle)} -> {body.count(needle)})")
    gone(body, "define $U = S_1 + S_2$", "A.2 old Lyapunov letter")
    gone(v9, "$\\dot U", "any remaining dot-U")
    need(body, "define the Lyapunov function $W = S_1 + S_2$", "A.2 W re-letter")
    if body.count(r"\dot W") != 2:
        raise SystemExit("FAIL [A.2]: exactly two dot-W sites expected "
                         "(the display and the omega-limit clause)")
    if body.count(r"W_\infty") != 1 or body.count(r"U_\infty") != 0:
        raise SystemExit("FAIL [A.2]: Lyapunov limit re-letter incomplete")

    # Proof cores byte-identical (spot anchors of every untouched proof step)
    for needle, label in [
        (r"$$q(x(t)) \;\le\; q(x_0) - \varepsilon t$$", "Thm 1 comparison display"),
        (r"$$\nabla q_j(\bar x) \cdot f(\bar x, a, \bar d) < 0.$$", "Thm 3 display"),
        (r"$$q(x(t)) \;\le\; q(x^*) - \varepsilon t \;=\; \inf_{x \in B_0} q(x) - \varepsilon t$$", "Thm 4 comparison display"),
        (r"$$D^+ q(x(t); f(x(t), u(t), d(t))) \;\le\; -\varepsilon \qquad \text{while } q(x(t)) > 0, \tag{3}$$", "display (3)"),
        (r"$$\sup_{u \in U(x)} \inf_{d \in D(x)} D^+ q(x; f(x,u,d)) \;\le\; -\varepsilon \qquad \forall x \in \mathcal{S}_a, \tag{1}$$", "display (1)"),
        (r"$$T_{\mathrm{obs}} \;>\; \frac{\inf_{x \in B_0} q(x)}{\varepsilon}. \tag{4}$$", "display (4)"),
        ("no Elliott–Kalton upgrade to a closed-loop strategy is required for the "
         "stated claim", "Thm 1 proof tail"),
        ("the flow of $\\dot S = -r(S)$ with $r > 0$ moves $B_t$ monotonically "
         "downward", "Thm 2 proof core"),
        ("The system has no disturbance and no estimation error: the failure is "
         "caused entirely by the non-injectivity of $O$. □", "Thm 2 proof end"),
        ("Until $t^*$, the record contains no informative observation: the violating "
         "branch is observation-equivalent", "Thm 4 proof tail"),
        ("Since $\\pi$ was arbitrary, no observation-based policy keeps every "
         "compatible trajectory in $\\mathcal{V}$", "Thm 3 proof end"),
        ("$q_j$ strictly decreases from $q_j(\\bar x) = 0$ at rate at least "
         "$\\eta/2$", "Thm 3 local selection core"),
    ]:
        need(body, needle, f"proof core: {label}")
        if t.count(needle) != 1:
            raise SystemExit(f"FAIL [proof core {label}]: source anchor not unique")

    open(DST, "w", encoding="utf-8").write(v9)
    wc_old, wc_new = len(t.split()), len(v9.split())
    print(f"OK: wrote {DST}")
    print(f"    words: {wc_old} -> {wc_new} (delta {wc_new - wc_old})")
    print(f"    lines: {len(t.splitlines())} -> {len(v9.splitlines())}")
    print(f"    version log: {len(log)} chars; body checks passed "
          f"({v9.count('Version log') - 1} retired log references purged)")


if __name__ == "__main__":
    main()
