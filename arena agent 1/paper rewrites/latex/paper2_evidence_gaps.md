# Evidence-Gap Analysis — "An Obstruction Calculus for Viability under Incomplete Observation" (v37)

Scope: systematic audit of the v37 main text and supplementary against the
standard of evidence a theory paper must meet — complete proofs, worked
examples, counterexamples, reproducible numerics, and claims that match what
is actually demonstrated. Gaps are ordered roughly by severity.

---

## GAP 1 (critical, internal contradiction): the code/data availability statement contradicts the coverage audit

**Where.** Declarations block (main, end of file):
> "Data availability. No data were used; all constructions are symbolic. Code availability. No code was used or produced; all constructions are symbolic."

**Versus** Section 8, which presents:
- "A reproducible delayed hidden-regime model" — "The audit runs on the exact instance specified here";
- "A coverage audit" over the grid z₀ ∈ {1.0, 1.1, …, 2.5} × T_obs ∈ {1,2,3}, reporting Table 1 and Figure `fig_p2_coverage.png`;
- Remark (joint completeness in the delayed class): "of the 42 nonviable cells, 30 are certified by the common-action certificate and the remaining 12 … none is uncovered."

The audit is a computation (the workspace contains `route2_numerics.py`, which generates the coverage figure). The manuscript both claims the audit is "reproducible" and declares that no code was used or produced. The cell counts (30/12/42) are unverifiable as published because no code is archived.

**Why it matters.** A reviewer who reaches the declarations after Section 8 will flag this immediately. It also violates the standing instruction to archive the verification code at `https://zenodo.org/records/22545740`.

**What closes it.** Archive the audit code (the delayed hidden-regime solver + coverage figure generator) at the Zenodo record, cite it from Section 8, and rewrite the declaration to "Code availability. The coverage-audit code is archived at … (DOI)." Or, if the audit is genuinely hand-computable, state that explicitly and drop the word "reproducible."

---

## GAP 2 (claim/evidence mismatch): the abstract overclaims finite checkability

**Where.** Abstract: "finitely checkable in the finite-state, polyhedral, and finite-horizon cases and analytic drift-and-timing conditions elsewhere."

**Versus what is demonstrated.** Finite checkability is actually shown only for:
- the common-action obstruction (Farkas pair for polyhedral safe-action sets, Theorem 2);
- the fibre criterion (Proposition 6);
- the finite-horizon recursion (Theorem 1, exact but exponential in |X|).

The **delayed-information/timing obstruction** (Theorem 3) is not finitely checkable in general — the text concedes the hypothesis "is checkable in its special cases (constant observations; hold-until-T_obs policies) and is a template to be instantiated in the general case." The exit certificate (Theorem 4) is an analytic drift condition. So the abstract's blanket "polyhedral" finite-checkability claim overreaches the body.

**What closes it.** Either (a) qualify the abstract ("finitely checkable for the common-action, fibre, and finite-horizon certificates in the finite-state and polyhedral cases; the drift-and-timing certificates are analytic conditions"), or (b) actually supply a polyhedral checkability result for the timing obstruction (e.g., an LP/occupancy-measure reduction of H3.2 when the blind-window control class is piecewise-constant).

---

## GAP 3 (positioning asserted, not demonstrated): no worked comparison against barrier certificates or the estimation-tube programme

**Where.** §6.2–6.3 assert complementarity: barrier methods "do not address" information-set emptiness; the estimation-tube reduction "preserves values" and the calculus "delimits its reach rather than contradict it."

**What is missing.** There is no single shared example showing:
1. a system where a barrier certificate would certify safety while an obstruction certificate certifies a *specific mode* of failure; or
2. a system where the estimation-tube value function is nonempty yet the common-action obstruction fires (or vice versa), making the "local certificate layer" claim concrete.

The only shared running example is the hidden-regime/fishery family. The complementarity claims are plausible but currently rest on assertion.

**What closes it.** One subsection ("A shared example, three methods"): pick one plant (the two-floor hidden-regime system, or the coupled-patch model), and demonstrate (i) what the barrier-certificate programme can/cannot say, (ii) what the estimation-tube reduction returns, (iii) which obstruction certificate fires and what design change it licenses.

---

## GAP 4 (hypotheses undefended): the Helly sparse witness lacks a boundary counterexample

**Where.** Proposition 4 (sparse common-action witness) requires affine-in-control dynamics, compact convex U, C¹ q_j. The Farkas discussion says "for infinite beliefs a finite-witness reduction is not automatic."

**What is missing.** No example or remark shows what happens when the hypotheses fail (non-convex U(x), control-nonlinear f), and the gap between "m+1 states witness emptiness" and "checkable" is left unexamined.

**What closes it.** A short counterexample (e.g., a non-convex safe-action set with an empty intersection but no m+1 witness) or a scope remark stating precisely what the convexity buys. This also sharpens the honest-scope tone the paper already uses elsewhere.

---

## GAP 5 (thin section): §9 probabilistic development is asserted connection, not demonstrated

**Where.** §9: Theorem (belief-state safety value) is "standard value iteration… (Smallwood and Sondik, 1973)"; the chance-constrained obstruction and degenerate limit are short propositions; the closing line concedes "a continuous-state limit requires uniform concentration… not developed here."

**What is missing.** No worked instance connects the belief-state values to the certificates — e.g., computing V_k for the hidden-regime example and showing V_k ↔ the common-action/timing verdicts, and no numerical illustration.

**What closes it.** One worked example: compute the safety value for the two-floor or hidden-regime POMDP, tabulate V_k against the certificate verdicts, and state the correspondence (the degenerate-limit proposition already supplies the machinery).

---

## GAP 6 (flagship certificate is a template): the delayed-information obstruction has no general computational instantiation

**Where.** Theorem 3 quantifies H3.2 over "every implementable blind-window control" — an infinite quantification over open-loop controls. The paper claims the certificate is checkable only in special cases.

**Why it matters.** The paper's selling point is "computationally interpretable certificates" (Conclusion). The flagship timing certificate is the one for which no general checkability result is given, which sits awkwardly with the abstract's finite-checkability claim (Gap 2).

**What closes it.** Supply a concrete instantiation: e.g., for polyhedral data and piecewise-constant blind-window controls, express H3.2 as a finite LP/robust-reachability check, with a theorem + proof. If a general reduction is genuinely hard, state that as a scoped limitation with one fully worked special case (constant-observation, hold-until-T_obs).

---

## GAP 7 (named but never exhibited): the post-observation-recourse failure mode has no example

**Where.** §6.5(ii) names "insufficient post-observation recourse" — a common blind-window control keeps every branch safe, yet no observation-adapted control can recover every branch once the distinguishing observation arrives — and says only the finite-horizon recursion captures it.

**What is missing.** A concrete system exhibiting exactly this mode. Naming a limitation without exhibiting it leaves the reader unsure the mode is real.

**What closes it.** A small constructed example (two regimes, a blind window, then a reveal after which no single post-reveal policy recovers both branches) with a proof that blind-window survival holds but post-reveal recovery fails. This converts §6.5(ii) from abstract caveat to concrete fact and gives Open Problem 1 a sharp target.

---

## GAP 8 (applied audience unserved): governance claims are unvalidated and the case study is one-dimensional

**Where.** §6.4 derives five design consequences (timing, coarseness, aggregation, bias, institutions); §6.5(vi) concedes they are "design conclusions… not empirical findings"; §8 concedes "the audit is symbolic and one-dimensional."

**What is missing.** No empirical anchor whatsoever — no real fisheries/indicator dataset, no observed monitoring-frequency or bias parameters. For a paper targeting sustainability governance this is the largest evidential weakness relative to its stated audience.

**What closes it (cheapest-to-strongest).**
1. Extend the case study to a second, two-dimensional instance (e.g., the coupled-patch system with a coarse shared indicator) so "multidimensional belief-space campaign deferred" becomes at least partially delivered.
2. Add a calibration paragraph mapping the certificates' parameters (ε, T_obs, bias b, floor) onto quantities estimable from published stock-assessment data, even if no new data are analyzed.
3. Optionally, one real-data illustration (e.g., a published fishery's observation schedule) to make the timing bound concrete.

---

## GAP 9 (asymmetry): full proofs are "collected in the Supplementary" but not for §3.4 or §7/§9

**Where.** §1.4: "Proof sketches of the Section 3 results are given in the main text; the complete proofs… are collected in the Supplementary Material." Supplementary S1 is titled "Complete proofs."

**What is missing.**
- Proposition 4 (Helly) has a full proof in the main only — not in S1.
- §7 (Theorems 8–9) and §9 (Theorem, Propositions) carry full proofs inline in the main and are absent from S1.
So "complete proofs collected in the Supplementary" is not literally true.

**What closes it.** Either (a) mirror the §3.4 and §7/§9 proofs into S1 (redundant but literal), or (b) reword §1.4 to "complete proofs of the Section 3 certificates are collected in the Supplementary; the results of Sections 7 and 9 are proved in the main text." (b) is preferable — no redundancy.

---

## GAP 10 (no quantitative converse): "sound but not complete" is never quantified

**Where.** §6.5(i) and §7 concede non-completeness; the only positive converse results are one-step (Theorem 8) and static-observation (Theorem 9).

**What is missing.** No partial converse of the form "if no certificate fires on [0,T] then some policy is viable on [0,T]" (or a separation showing none exists), which would upgrade the paper's central limitation from a concession to a boundary result.

**What closes it.** State and prove (or refute with a counterexample) a finite-horizon partial converse for the common-action + timing certificates; the coverage audit already gestures at this ("jointly complete in the delayed class").

---

## Minor items

- **M1.** The coverage table (Table 1) is hand-typeset while its companion figure is generated; publish both from the same code so the 30/12/42 counts are machine-checkable (ties to Gap 1).
- **M2.** §6.4 "Bias" claims the correction is "the one governance structures can omit"; this is a behavioral claim with no citation — either cite the information-design/governance literature or soften to a design observation.
- **M3.** The Zenodo reference (Abaee 2026) is cited for a *different* paper (compensatory aggregation); the verification code has no entry of its own (ties to Gap 1).

---

## What is already strong (do not disturb)

- The ladder structure (Selector → admissibility → safety → tube → recursion) is tight and correctly cross-referenced.
- The two bounded constructions in the supplementary (A.1 coupling-creates-viability, A.2 emptiness-despite-factorwise-viability) are genuinely good evidence of the "not just dynamics" point.
- The coverage audit, once reproducible, is exactly the right kind of evidence for a certificate paper.
- Proof sketches are correct and appropriately scaled; hypotheses (H2.x/H3.x/H5.x) and equation tags are now consistent after the reorder.
