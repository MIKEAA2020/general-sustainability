#!/usr/bin/env python3
# Provenance record: regenerates paper1_assessment_separation_v25.tex from v24.
# Usage: point PATH at a copy of v24, run with python3; output is byte-identical to v25.
# (Committed as the audit trail for the v24 -> v25 revision.)
"""Build paper1 v25 from v24: strip change-log / internal dialogue / meta-commentary,
remove chat-history jargon and naive over-hedging, keep all mathematics unchanged."""
import re, sys

PATH = "/home/user/repo/arena agent 1/paper rewrites/latex/paper1_assessment_separation_v25.tex"

src = open(PATH).read()

def block(pattern, replacement, expect=1, flags=re.DOTALL):
    global src
    found = len(re.findall(pattern, src, flags))
    assert found == expect, f"BLOCK expect={expect} found={found}: {pattern[:80]!r}"
    src = re.sub(pattern, lambda m: replacement, src, flags=flags)

def sub(plain, replacement, expect=1):
    """Flexible-whitespace literal substitution."""
    global src
    rx = re.escape(plain)
    rx = rx.replace(r"\ ", r"\s+")
    found = len(re.findall(rx, src))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:80]!r}"
    src = re.sub(rx, lambda m: replacement, src)

# ---------------- B-blocks (large spans) ----------------

# B1: header provenance -> minimal formal header
block(r"\A% LaTeX source generated.*?\(also compatible with pdflatex/xelatex\)\.\n",
"""% The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment
% Amin Abaee. Revision v25. Compiles with tectonic, pdflatex, or xelatex.
""")

# B2: sections 2.2--2.7 (record/model-map/claim-status/failure-class/specialization
# bookkeeping) -> focused datum + quantifier discipline; notation renumbered 2.8 -> 2.4
block(r"\\subsubsection\{2\.2.*?\\subsubsection\{2\.8 Notation\}\\label\{notation\}",
r"""\subsubsection{2.2 The assessment datum}\label{the-assessment-datum}

The results use a typed exact-tube transition datum: a state space \(Z\) carrying typed floors \(s_i \ge 0\) (normalized at zero), an action set, a disturbance class \(D\), a typed safe set \(S\), a destination set \(G\), and tube and successor maps \(\mathrm{Tube}(a,d)\), \(\mathrm{Succ}(a,d)\) as defined in Section 3.1. A transition is safe only if every state visited along it, not merely its endpoint, satisfies the constraints. The witness datum of Section 4.5 is an instance of this datum.

\subsubsection{2.3 Quantifier discipline}\label{quantifier-discipline}

Every assessment operator evaluates the disturbance quantifier innermost: admissibility of an action requires safety for every \(d \in D\). The separation analysed in Section 3 concerns a second quantifier, over scalarization weights, placed outside it: the noncommutation studied is \(\exists a\, \forall w\) versus \(\forall w\, \exists a_w\).

\subsubsection{2.4 Notation}\label{notation}""")

# B3: notation body -> symbol definitions only (drop booking, record fields, Appendix pointer)
block(r"The following symbols are used throughout the paper\..*?consolidated in Appendix A\.",
r"""The following symbols are used throughout the paper.

\begin{itemize}
\tightlist
\item
  \(z \in Z\): a state; \(a\): an action; \(d \in D\): a disturbance; \(s = (s_1, \ldots, s_n)\): typed floors (normalized so that \(s_i \ge 0\) is the binding constraint); \(x\): the reserve stock (bridge stock) on the witness.
\item
  \(W_+ = \mathbb{R}^n_+ \setminus \{0\}\): the full nonnegative scalarization cone excluding the origin (Section 3.1); \(w \in W_+\): a nonnegative scalarization weight; a subfamily is written \(W\), as in Proposition 4; \(r = w_2 / w_1\): the weight ratio used on the witness (the resource increment of Section 5.5 is \(\kappa\)).
\item
  \(S = S^{\mathrm{phys}} \cap \{ s_i \ge 0,\ i = 1..n \}\) and \(G = G^{\mathrm{phys}} \cap \{ s \ge 0 \}\): typed safe and destination sets; \(S^w, G^w\): their scalarized counterparts at weight \(w\); \(S^{\mathrm{phys}}, G^{\mathrm{phys}}\): their physical counterparts; on the witness \(S = S_0\), the transition-safe set of Section 4.5.
\item
  \(\mathrm{Tube}(a,d)\): the full set of states visited during the interval under action \(a\) and disturbance \(d\); \(\mathrm{End}(a,d)\): the endpoint values visited; \(\mathrm{Succ}(a,d)\): the successor set after any endpoint reset.
\item
  \(E_{\mathrm{typ}}(z)\), \(E_w(z)\), \(E_{\mathrm{tube,phys}}(z)\), \(E_{\mathrm{end}}(z)\), \(E_{\mathrm{end,typ}}(z)\): the assessment operators of Section 3.1.
\item
  \(\mathcal{V}[E] = \{ z : E(z) \neq \varnothing \}\): the accepted-state set of operator \(E\); in particular \(\mathcal{V}_{\mathrm{typ}} = \mathcal{V}[E_{\mathrm{typ}}]\), \(\mathcal{V}_w = \mathcal{V}[E_w]\), \(\mathcal{V}_{\mathrm{weak}} = \bigcap_{w \in W_+} \mathcal{V}_w\), \(\mathcal{V}_{\mathrm{phys}} = \mathcal{V}[E_{\mathrm{tube,phys}}]\), \(\mathcal{V}_{\mathrm{end}} = \mathcal{V}[E_{\mathrm{end}}]\).
\item
  Witness datum (Section 4.5): phase state \((q, x, s_1, s_2)\); gain vector \(e = (1/4, 1/4)\); rescue cost \(c = 1\); depth of worst-case dip \(2\); menu \{NO-SWITCH, FAST, SLOW, STAGED\}.
\item
  Discrepancy sets (Section 4.6): \(\mathcal{Q}\) aggregate-versus-direct-floor discrepancy region; \(R\) rescue set; \(I\) impossibility region; \(\mathrm{FP}_{\mathrm{agg}} = \mathcal{V}_{\mathrm{weak}} \setminus \mathcal{V}_{\mathrm{typ}}\) the genuine acceptance gap; \(\rho_1, \rho_2\) the per-weight licensing thresholds.
\item
  \(\mathcal{A}\): the action set (Sections 4.1 and 5.5); \(\mathsf{Aug}_\kappa\): the resource-augmentation map, with increment \(\kappa\) and minimal rescue threshold \(\kappa^*\).
\end{itemize}

The gain vector \(e\) of the witness datum and the standard basis vector \(e_k\) in Remark 2 are distinct objects.""")

# B4: remove Appendix A (internal declaration/registration diary) up to References
block(r"\\subsection\{Appendix A.*?\\end\{center\}\n\n\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\n\n(?=\\subsection\{References\})",
"")

# B5: 6.1 -> formal negative-certificate discussion (drop editorial + programme diary)
block(r"\\subsubsection\{6\.1 Negative certificates as first-class\s+results\}\\label\{negative-certificates-as-first-class-results\}.*?disciplinary analogy of this\s+paragraph\.",
r"""\subsubsection{6.1 Negative certificates}\label{negative-certificates}

A negative certificate --- a rejection with an exhibited violated constraint for each action, exhausting the action set --- is a complete verdict, not an inconclusive one. Theorem 5(7) is an instance: four actions, four exhibited violations, certifying impossibility on \(I\) together with the resource threshold of Section 5.5 and the per-weight licensing thresholds of Theorem 5(6). Related scored forecast-evaluation studies apply assessment discipline of the same kind to the Northern cod and Edwards Aquifer systems (Abaee, 2026b, 2026c); the separation results here rest on their displayed proofs and the machine-checked finite instance of Section 4.9.""")

# B6: 6.2 limitations -> six proper items, formal wording
block(r"\\begin\{enumerate\}\n\\def\\labelenumi\{\(\\roman\{enumi\}\)\}\n\\tightlist\n\\item\n  The assessment-separation theorem is an existence result.*?small finite rational datum\.\n\\end\{enumerate\}",
r"""\begin{enumerate}
\def\labelenumi{(\roman{enumi})}
\tightlist
\item
  The separation theorem is an existence result with an open region; it does not imply the gap is large in any given application, and where the assessments coincide it yields nothing.
\item
  Novelty statements reflect bounded literature search (Section 5.2).
\item
  The operators cover finite horizons with exact tubes and specified disturbance sets; infinite horizons, partial observation, stochastic chance constraints, and endogenous event times are not treated.
\item
  No empirical claims are made.
\item
  The governance, intergenerational, and composition extensions are stated at partial status in the Supplementary Material and are not used in the proofs.
\item
  Computational tractability: on a finite explicit state--action--disturbance graph with constant-time predicate evaluation, the backward recursion is polynomial in the graph size and horizon. For continuous, hybrid, or belief-state models, the graph itself may be exponentially large, infinite, or only approximately representable; exact tube inclusion may be computationally hard or undecidable; and grid cardinality grows as \(N_{\mathrm{grid}} = \prod_{i=1}^n N_i\) --- exponentially in dimension when floors are coordinates. The witness is tractable because its datum is small, finite, and rational.
\end{enumerate}""")

# B7: references -> alphabetical order (Abaee first), clean companion entries
block(r"Asheim, G\. B\. \(1994\)\..*?\(the Edwards Aquifer side\)\.",
"""Abaee, A. (2026a). Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons. Zenodo. https://doi.org/10.5281/zenodo.22554177.

Abaee, A. (2026b). Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Abaee, A. (2026c). Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Asheim, G. B. (1994). Net national product as an indicator of sustainability. \\emph{Scandinavian Journal of Economics}, 96(2), 257--265.

Aubin, J.-P. (1991). \\emph{Viability Theory}. Birkh\\"auser, Boston.

Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). \\emph{Viability Theory: New Directions}, 2nd ed.~Birkh\\"auser, Boston.""")

# ---------------- S-edits (targeted) ----------------
sub("September 6, 2026", "September 10, 2026")
sub("Two companion results bound the separation:", "Two further results bound the separation:")
sub("The ``only'' claim is scoped to the deterministic menu, within which the separation is structural, not an artifact of a poor choice of weights; continuum statements are proved in full and the rational instance verified by exact-integer computation.",
    "Within the deterministic menu the separation is structural, not an artifact of weight choice. Continuum statements are proved analytically, and the rational instance is checked by exact-integer computation.")
sub("is developed for the companion ledger study (Abaee, 2026a) and is not re-argued here; no theorem of this paper touches material cycles.",
    "is developed in the companion ledger study (Abaee, 2026a) and is not re-argued here; no theorem of this paper concerns material cycles.")
sub("The aggregate question --- whether total capital can be maintained --- is ill-posed for the reason Remark 1 and the witness of Section 4.5 make precise.",
    "The aggregate question --- whether total capital can be maintained --- is ambiguous between the two quantifier orders made precise in Remark 1 and Section 4.5.")
sub("The stronger possibility, which this paper proves to be real, is that no choice of weights repairs the difficulty.",
    "The stronger possibility, established here, is that no choice of weights repairs the difficulty.")
sub("The second is \\emph{status drift}. Conceptual frameworks state aspirations as theorems, and conditional results circulate as unconditional ones. Every claim below is therefore labelled with its logical status --- definition, theorem, conditional statement, or open question --- distinguishing what is proved, what is verified on a finite machine artifact, and what is asserted without proof.",
    "The second is the circulation of conditional results as unconditional ones. Each result below therefore states its assumptions and status explicitly.")
sub("It is a distinct phenomenon from the \\emph{productivity illusion} of adequate delivery from a quietly reduced base, which concerns the productive base and is treated in Abaee (2026a), where that base sits inside the ledger.",
    "It is distinct from the \\emph{productivity illusion} --- adequate delivery from a reduced productive base --- treated in Abaee (2026a).")
sub("what it fails to see is not the base but the individual floor mid-interval --- the compensatory form of the illusion as it arises in aggregation, the acceptance gap of Theorem 5(4).",
    "what it does not detect is the individual floor mid-interval --- the compensatory form of the illusion in aggregation, the acceptance gap of Theorem 5(4).")
sub("The paper proves the always-valid inclusion (Remark 1), proves the pointwise action-set identity of the noncompensatory operator with the common-plan set over the full cone (Proposition 3(ii)) and isolates its mechanism (Remark 1), and exhibits an explicit rational witness on which the acceptance gap",
    "Remark 1 states the always-valid inclusion; Proposition 3(ii) identifies the noncompensatory operator with the common-plan set over the full cone; and Theorem 5 exhibits an explicit rational witness on which the acceptance gap")
sub("\\textbf{Claimed.} (i) The action-set identity \\(E_{\\mathrm{typ}}(z)", "\\textbf{Contributions.} (i) The action-set identity \\(E_{\\mathrm{typ}}(z)")
sub("\\textbf{Claimed.} (i) The action-set identity \\(E_{\\mathrm{typ}} =", "\\textbf{Proved here.} (i) The action-set identity \\(E_{\\mathrm{typ}} =")
sub("\\textbf{Not claimed.} A universal ranking of all weak- and strong-sustainability doctrines; a proof that any particular set of environmental boundaries ought to be treated noncompensatorily; an empirical result about any specific resource system; or the governance, intergenerational, and composition extensions, which are stated at their actual (partial) status in the Supplementary Material.",
    "\\textbf{Scope.} No universal ranking of weak- and strong-sustainability doctrines; no proof that any particular set of environmental boundaries ought to be treated noncompensatorily; no empirical result about any specific resource system. The governance, intergenerational, and composition extensions are stated at partial status in the Supplementary Material.")
sub("theorem: menu convexification of the witness menu closes the acceptance gap exactly at", "theorem: menu convexification closes the acceptance gap exactly at")
sub("theorem, under which menu convexification of the witness menu closes the gap exactly at", "theorem, under which menu convexification closes the gap exactly at")
sub("\\textbf{Conceded as established.}", "\\textbf{Established.}")
sub("No claim mixes types without a declared bridge.", "No statement combines quantities of different type except through an explicit bridge.")
sub("This section fixes the typed framework that the theorems require. It is a minimal realization, not a completed universal architecture.",
    "This section fixes the definitions the theorems require.")
sub("Five operators are distinguished; they share the same disturbance quantifier and differ in constraint structure, with one additional difference for the fourth: the endpoint operator also replaces the tube evaluation map by the endpoint map. The fifth, defined after the chain, is the typed-endpoint operator deposited so that the photograph reading of Section 5.4 states its own witness.",
    "Five operators are distinguished. They share the same disturbance quantifier and differ in constraint structure, except that the endpoint operator also replaces tube evaluation by endpoint evaluation. The fifth is the typed-endpoint operator, used in Section 5.4.")
sub("The endpoint operator is included because aggregated accounting in practice is frequently endpoint accounting: the index is evaluated on audited snapshots, while the typed floors of strong sustainability are constraints on the whole trajectory. The distinction is exactly the distinction between an assessment that sees the trajectory and one that sees only its photograph. A photograph of output cannot in general certify the condition of the system that produced it --- the productivity-illusion reading developed for the companion ledger study (Abaee, 2026a) --- and the typed-endpoint operator defined below makes the floor-level version of the claim exact on the witness.",
    "The endpoint operator represents aggregated accounting evaluated on audited snapshots, while typed floors constrain the whole trajectory: evaluation on the full tube versus evaluation on endpoints only. Endpoint values cannot in general certify the condition of the system that produced them (cf.\\ the productivity-illusion analysis in Abaee, 2026a); the typed-endpoint operator below states the floor-level version of this observation exactly on the witness.")
sub("because the witness's physical constraint touches only the monotone reserve stock.", "because on the witness the physical constraint involves only the monotone reserve stock.")
sub("The \\textbf{typed-endpoint} operator (typed floors at endpoints only) is deposited here as a Definition, so that the photograph reading of Section 5.4 states its own witness:",
    "Definition (typed-endpoint operator). The \\textbf{typed-endpoint} operator evaluates typed floors at endpoints only:")
sub("It sits between the chain's first and last links, \\(E_{\\mathrm{typ}}(z) \\subseteq E_{\\mathrm{end,typ}}(z) \\subseteq E_{\\mathrm{end}}(z)\\), by the recorded inclusions \\(\\mathrm{End}(a,d) \\subseteq \\mathrm{Tube}(a,d)\\), \\(S \\subseteq S^{\\mathrm{phys}}\\), and \\(G \\subseteq G^{\\mathrm{phys}}\\) --- one-line set facts, not part of Proposition 3(i).",
    "It satisfies \\(E_{\\mathrm{typ}}(z) \\subseteq E_{\\mathrm{end,typ}}(z) \\subseteq E_{\\mathrm{end}}(z)\\), since \\(\\mathrm{End}(a,d) \\subseteq \\mathrm{Tube}(a,d)\\), \\(S \\subseteq S^{\\mathrm{phys}}\\), and \\(G \\subseteq G^{\\mathrm{phys}}\\).")
sub("On the witness datum of Section 4.5 it carries a one-line witness of the photograph claim: FAST's endpoint values of \\(s_1\\) equal the initial \\(s_1\\), and its successor lies in \\(G\\) whenever \\(x \\ge 0\\) (the action table and the proof of Theorem 5(1)), so \\(E_{\\mathrm{end,typ}}(z) \\neq \\varnothing\\) at every \\(z \\in X_0\\), while \\(E_{\\mathrm{typ}}(z)\\) requires \\(s_1 \\ge 2\\) (Theorem 5(1)). The machine artifact of Section 4.9 checks the physical endpoint operator only; this typed-endpoint observation is asserted by inspection of the recorded action table, not machine-verified.",
    "On the witness datum of Section 4.5, FAST's endpoint values of \\(s_1\\) equal the initial \\(s_1\\) and its successor lies in \\(G\\) whenever \\(x \\ge 0\\) (action table in Section 4.5; proof of Theorem 5(1)), so \\(E_{\\mathrm{end,typ}}(z) \\neq \\varnothing\\) at every \\(z \\in X_0\\), while \\(E_{\\mathrm{typ}}(z) \\neq \\varnothing\\) requires \\(s_1 \\ge 2\\) (Theorem 5(1)). This observation follows by inspection of the action table and is not part of the machine-checked artifact of Section 4.9.")
sub("With this notation the central noncommutation is visually explicit:", "The central noncommutation is then:")
sub("in a declared topology --- are available; they are not needed anywhere in this paper and are stated only to delimit the mechanism.",
    "in a specified topology --- are available but not needed here.")
sub("Remark 1 isolates the mechanism. The separation exhibited in Section 4.5 is a strict instance of this inclusion, witnessed by states at which the nonemptiness witnesses differ with the weight.",
    "The separation in Section 4.5 is a strict instance of this inclusion, at states where the nonemptiness witnesses differ with the weight.")
sub("Remark 2 says that at a \\emph{fixed} trajectory the full-cone aggregate is lossless: nonnegativity of every weighted sum is equivalent to componentwise nonnegativity. The separation established below is therefore entirely dynamic --- a matter of quantifier order --- and not a form of static scalarization blindness.",
    "At a \\emph{fixed} trajectory the full-cone aggregate is therefore lossless: nonnegativity of every weighted sum is equivalent to componentwise nonnegativity. The separation below is entirely dynamic --- a matter of quantifier order --- not static scalarization blindness.")
sub("Part (i) is constraint-set monotonicity of viability/reachability operators under nested safe sets (Aubin, 1991; Frankowska, 1989). The claim of this paper is part (ii) and the witnessed strictness of the resulting inclusion.",
    "Part (i) is standard constraint-set monotonicity under nested safe sets (Aubin, 1991; Frankowska, 1989); part (ii) is proved above, and its strictness is witnessed in Theorem 5.")
sub("maintainability witnessed by the destination hold policy, a declared datum.", "maintainability witnessed by the destination hold policy.")
sub("componentwise to both typed floors; \\(e\\) is declared strictly positive so that successors are interior to \\(G\\), and no inequality of Theorem 5 binds on its magnitude.",
    "componentwise to both typed floors; \\(e\\) is strictly positive, so successors are interior to \\(G\\), and no inequality of Theorem 5 binds on its magnitude.")
sub("\\emph{Define the following sets, distinguished precisely:} -", "\\emph{Define:} -")
sub("already-typed slice of the discrepancy region, whose states are typed-transformable at the declared cost, witnessed by STAGED.",
    "already-typed slice of the discrepancy region, whose states are typed-transformable at cost \\(c = 1\\), witnessed by STAGED.")
sub("The noncompensatory assessment requires either one floor to survive its own worst-case dip or the bridge stock to be fundable.",
    "The noncompensatory assessment requires either one floor to survive its own worst-case dip (\\(s_i \\ge 2\\)) or the bridge stock to cover the rescue cost (\\(x \\ge 1\\)).")
sub("figs_p1/fig1_witness_v22.png", "figs_p1/fig1_witness_v25.png")
sub("The point \\((x, s_1, s_2) = (\\tfrac12, \\tfrac1{10}, \\tfrac1{10})\\) is annotated separately in Panel A's caption, since it is not a point of the two-dimensional \\(s\\)-plane alone.",
    "The point \\((x, s_1, s_2) = (\\tfrac12, \\tfrac1{10}, \\tfrac1{10})\\), which lies outside the \\(s\\)-plane section, is annotated in Panel A.")
sub("The same region is not to be labelled ``false positive'' without fixing \\(x\\): at \\(x \\ge 1\\) it is rescue, at \\(x < 1\\) it is impossibility.",
    "The region is the rescue set at \\(x \\ge 1\\) and the impossibility region at \\(x < 1\\); only the latter is a false positive.")
sub("The witness datum of Section 4.5 is immune to this erasure.", "The witness datum of Section 4.5 is not subject to this erasure.")
sub("A companion software artifact (deterministic, exact integer arithmetic at scale 40; no floating point, tolerances, or randomness) checks the finite rational instance of Proposition 3, Proposition 4, Theorem 5, and Remark 6: it verifies the action classifications, the region identities, and the accepted-set identities on a \\(31^3 = 29{,}791\\)-state grid (a product of 31-point chains on \\(x, s_1, s_2\\); the box endpoints are part of the artifact's configuration and are archived with it), with a finite verification set containing the analytically identified critical weight ratios \\(\\rho_1, \\rho_2\\) and their midpoint \\((\\rho_1 + \\rho_2)/2\\) for every enumerated grid state. All 25 checks pass; re-execution reproduces the outputs exactly; the checks are enumerated one by one, with their recorded pass status, in the Supplementary Material (S8).",
    "An accompanying software artifact (deterministic exact-integer arithmetic; no floating point, tolerances, or randomness) checks the finite rational instance of Proposition 3, Proposition 4, Theorem 5, and Remark 6: the action classifications, the region identities, and the accepted-set identities on a \\(31^3 = 29{,}791\\)-state grid over \\((x, s_1, s_2)\\), with a finite verification set containing the critical weight ratios \\(\\rho_1, \\rho_2\\) and their midpoint for every enumerated grid state. All 25 checks pass and re-execution reproduces them exactly; they are enumerated in the Supplementary Material (S8).")
sub("Symbolic theorem & Exact continuum identities and inequalities for the declared witness & Displayed proofs",
    "Continuum statements & Exact identities and inequalities on the witness datum & Displayed proofs")
sub("Machine artifact & Exact finite rational checks of the classification on the enumerated grid & Deterministic computation",
    "Finite rational instance & Classifications on the enumerated grid & Deterministic computation")
sub("Empirical implication & Conditional design requirements only & Not established here",
    "Empirical claims & None in this article & ---")
sub("The declared action space is the finite menu", "The action space is the finite menu")
sub("not the Pareto-frontier geometry under which weighted sums fail to reach nonconvex frontier parts (Das and Dennis, 1997); the two mechanisms are distinct, and both are explicit.",
    "not the Pareto-frontier geometry under which weighted sums fail to reach nonconvex frontier parts (Das and Dennis, 1997); the two mechanisms are distinct.")
sub("the gap survives sequential time-sharing and dissolves only under convexification, so the structural character",
    "the gap survives sequential time-sharing and closes only under convexification, so the structural character")
sub("so the compensatory doctrine's blind spot is not the existence of an aggregate index but the \\emph{policy dependence} of the aggregate-feasible transition: the index certifies a set of transitions, no one of which the noncompensatory assessment accepts.",
    "so the compensatory doctrine's limitation is not the existence of an aggregate index but the \\emph{policy dependence} of the aggregate-feasible transition: the index certifies a set of transitions, none of which the noncompensatory assessment accepts.")
sub("Theorem 8 closes this reading on the menu side: a single convexified blend serves every weight on the impossibility region, so the measured value of information is the cost of the finite deterministic menu rather than of the weight information itself. Proposition 9 sharpens it further: the value of information is dissolved by convexifying the action space, not by sharing actions in time",
    "Theorem 8 qualifies this reading: a single convexified blend serves every weight on the impossibility region, so the value of information reflects the finite deterministic menu rather than the weight information itself. Proposition 9 sharpens the point: the value of information is removed by convexifying the action space, not by sharing actions in time")
sub("This is because actual prices may be strictly positive,", "Actual prices may be strictly positive,")
sub("\\subsubsection{5.3 What the theorem does not say}", "\\subsubsection{5.3 Scope delimitations}")
sub("\\subsubsection{5.3 Scope delimitations}\\label{what-the-theorem-does-not-say}", "\\subsubsection{5.3 Scope delimitations}\\label{scope-delimitations}")
sub("\\textbf{No aggregate blindness at fixed trajectories.} Remark 2 establishes the opposite: at a fixed trajectory, the full-cone aggregate is lossless.",
    "\\textbf{No aggregate blindness at fixed trajectories.} By Remark 2, at a fixed trajectory the full-cone aggregate is lossless.")
sub("All statements are for finite-horizon exact-tube data with declared disturbance sets.", "All statements are for finite-horizon exact-tube data with specified disturbance sets.")
sub("so the full cone is the strictest compensatory reading. A practitioner restricting weights to a policy-relevant family obtains a strictly weaker separation guarantee.",
    "so the full cone is the strictest compensatory reading, and the separation persists a fortiori for restricted families.")
sub("\\textbf{No transfer to empirical systems.} The theorem is about assessment operators on a declared datum; it asserts nothing about any fishery or aquifer.",
    "\\textbf{No empirical transfer.} The theorems concern assessment operators on a specified datum and imply no empirical claim about any resource system.")
sub("and the witness's reserve stock is deliberately kept out of the weighted aggregate (a design choice recorded in Section 4.5, not a consequence of aggregation).",
    "and the witness's reserve stock is excluded from the weighted aggregate by construction (Section 4.5), not by consequence of aggregation.")
sub("The impossibility region is a negative certificate relative to the declared four-action menu; with a larger menu it can shrink or vanish, and Section 5.5 states the completeness status that an application must report.",
    "The impossibility region is a negative certificate relative to the specified four-action menu; with a larger menu it can shrink or vanish (see the completeness requirement in Section 5.5).")
sub("The separation is exhibited on, and claimed for, the declared action-indexed class only.", "The separation is exhibited for, and scoped to, the specified action-indexed class.")
sub("The convexification question is nevertheless answered, not bracketed: the blend family of Theorem 8 collapses",
    "Theorem 8 resolves the convexification question: the blend family collapses")
sub("so the structural character of the separation is owed to the convexity of the action space, not to temporal sharing.",
    "so the structural character of the separation is due to the convexity of the action space, not to temporal sharing.")
sub("The separation theorem has four implications, each stated at its actual strength.", "The separation theorem has four implications.")
sub("reweighting alone cannot substitute for it within the witness semantics (Section 5.5). This is a theorem about the witness, not a universal policy law: it applies where a resource-controlled rescue action exists.",
    "reweighting alone cannot substitute for it on the witness datum (Section 5.5). This applies where a resource-controlled rescue action exists; it is not a universal policy claim.")
sub("Reporting regimes that evaluate endpoints only --- audited annual snapshots, the form taken by much aggregated sustainability accounting --- evaluate only the weakest operator of the chain of Section 3.1. Under those semantics they license transitions that violate typed floors mid-interval without the assessment detecting it (the typed-endpoint operator \\(E_{\\mathrm{end,typ}}\\) of Section 3.1 is the one-line witness: on the witness datum, FAST is typed-endpoint-admissible at every state of \\(X_0\\) while typed-tube-admissible only for \\(s_1 \\ge 2\\) --- an inspection of the recorded action table, not one of the artifact's 25 checks); the per-floor reporting of the Third implication is what detects the discrepancy. The paper asserts nothing empirical about any particular reporting regime.",
    "Reporting regimes that evaluate endpoints only, as in audited annual snapshots, evaluate only the weakest operator of the chain of Section 3.1. Under those semantics they license transitions that violate typed floors mid-interval without detection (on the witness datum, FAST is typed-endpoint-admissible at every state of \\(X_0\\) but typed-tube-admissible only for \\(s_1 \\ge 2\\), by inspection of the action table in Section 4.5); the per-floor reporting of the third implication detects the discrepancy. No empirical claim about any particular reporting regime is made here.")
sub("\\textbf{Rescue as an action-synthesis theorem.} Rescue is an operation on the impossibility region. Rather than saying the recursion ``names the binding resource,'' define a resource-augmentation map",
    "\\textbf{Rescue as action synthesis.} Rescue is an operation on the impossibility region. Define a resource-augmentation map")
sub("where \\(\\mathcal{A}_\\kappa\\) denotes the augmented menu. On the witness, for the STAGED action and \\(x < 1\\): \\(\\kappa^* = 1 - x\\), the exact resource increment that converts an impossibility-region state into a typed-transformable one. States of the rescue set \\(R\\) need no augmentation --- STAGED is typed-admissible there as it stands --- which is exactly why \\(R\\) is not part of the acceptance gap. This turns the second policy implication into a theorem.",
    "where \\(\\mathcal{A}_\\kappa\\) denotes the augmented menu. \\textbf{Proposition (rescue threshold).} \\emph{On the witness datum, for the STAGED action and \\(x < 1\\), \\(\\kappa^* = 1 - x\\).} \\emph{Proof.} STAGED is typed-admissible exactly when its \\(x\\)-tube stays nonnegative, i.e.\\ when \\(x + \\kappa \\ge 1\\); the least such increment is \\(1 - x\\). \\ensuremath{\\square} The increment converts an impossibility-region state into a typed-transformable one. States of the rescue set \\(R\\) need no augmentation, since STAGED is typed-admissible there; this is why \\(R\\) is not part of the acceptance gap.")
sub("Section 4.5, the following load-bearing data:", "Section 4.5, the following additional specifications:")
sub("whether \\(\\mathcal{A}\\) is exhaustive, a registered policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is ``no safe transition exists among the registered actions,'' not ``no safe transition exists.''",
    "whether \\(\\mathcal{A}\\) is exhaustive, a listed policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is ``no safe transition exists among the listed actions,'' not ``no safe transition exists.''")
sub("A declared \\(D\\) is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility.",
    "A specified disturbance set is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility.")
sub("Whether the destination maintainability witness is physical, simulated, or merely declared.",
    "Whether the destination maintainability witness is established physically, by simulation, or by assumption.")
sub("The theorem ranks no doctrine: Section 5.1 scopes the formalizations, and after Theorem 8 the structural character of the separation is a property of the finite deterministic menu, not of weak or strong sustainability as traditions (Sections 4.10--4.11).",
    "The theorem establishes no ranking of doctrines: Section 5.1 delimits the formalizations, and by Theorem 8 the structural character of the separation is a property of the finite deterministic menu, not of either tradition (Sections 4.10--4.11).")
sub("Theorem 8 scopes this reply: such a single transition is not, in general, a member of the declared deterministic menu but a convexified action, so the honest question for a reporting convention is whether its action set admits the relevant menu convexification --- and Proposition 9 shows that permitting mere temporal alternation does not provide it.",
    "Theorem 8 qualifies this requirement: such a single transition is not, in general, a member of the specified deterministic menu but a convexified action, so the relevant question for a reporting convention is whether its action set admits the required menu convexification --- and Proposition 9 shows that temporal alternation alone does not provide it.")
sub("Framework extensions (governance constructors with declared support, the implementability ladder, the commons obstruction, intergenerational structures, the nested-impossibility theorem, composition interfaces), the planetary-boundaries application note, the full set of framework definitions, and the declared conjectures are provided in the accompanying supplementary file \\texttt{paper1\\_supplementary\\_v3.md}, together with their status declarations; the machine artifact's 25 checks are enumerated in its S8.",
    "Framework extensions (governance constructors, the implementability ladder, the commons obstruction, intergenerational structures, the nested-impossibility theorem, composition interfaces), the planetary-boundaries application note, the full framework definitions, and the conjectures are given in the accompanying Supplementary Material, which also enumerates the machine artifact's 25 checks (S8).")
sub("The symbolic proofs are contained in this article. The companion verification artifact (exact-integer regression checks of the finite rational instance, all 25 checks, deterministic and re-executable) is deposited in a public repository with stable identifier, software version, execution command, and expected output hashes; a link is provided with the submission.",
    "The proofs are contained in this article. The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived in a public repository; a link is provided with the submission.")

open(PATH, "w").write(src)
print("OK - all substitutions applied")
