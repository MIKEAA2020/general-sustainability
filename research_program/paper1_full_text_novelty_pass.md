# Paper 1 Independent-Result Gate — Full-Text Novelty Pass (Search Level)

**Provenance:** executed 2026-08-28 by the programme agent (Z.ai Code) using targeted web-literature search (12 queries; raw result files preserved at `paper1_instantiation/novelty_searches/q1..q12*.json`), against the strengthened Paper 1 candidate of `paper1_typed_false_positive_theorem.md` (Theorems A/B/C) and the residual-obligation list of `batch 2/02_elevation/E6_NOVELTY_AUDIT_EXECUTION.md` ("the full-text pass remains open at paper-drafting time").

**Status discipline — what this pass is and is not.** Same asymmetries as E6, restated:
- **Positive identifications are robust.** A verdict of `known-equivalent` or `known-and-weaker` cites specific published work whose existence and relevance the search establishes directly.
- **Absence claims are bounded.** `no-match-found` means *no match in the performed searches*; a full database sweep (MathSciNet/Zentralblatt/Google Scholar forward search) remains available to a later external audit.
- **No theorem status changes.** The theorems are already proved internally; what this pass fixes is the **novelty mapping** — what must be cited as backbone and what is defensible as delta — and with it the Paper 1 gate decision.

---

## 1. What was audited

Not the backward recursion (already adjudicated: `internal_provisional_Paper1_operatorII_novelty_answer.md` — the recursion is a typed instance of established robust predecessor/reach-avoid/capture-basin constructions; that verdict STANDS and is not re-litigated here). The audited object is the **strengthening**: the assessment-hierarchy theorem (endpoint-only ⊇ scalarized ⊇ noncompensatory), the quantifier localization (`E_typ = ⋂_w E_w` per state; the predecessors differ exactly by the order of ∃plan and ∀weights), the witness datum with its closed-form regions, per-weight plan disagreement, rescue/impossibility split, and the multi-stage propagation.

## 2. Verdicts by literature

### 2.1 Multi-objective optimization (weighted-sum scalarization) — **known-and-weaker; the static analogue must be cited**

Das & Dennis (1997/1998, *A closer look at drawbacks of minimizing weighted sums of objectives for Pareto set generation in multicriteria optimization problems*, Struct. Optim. 14; surfaced directly with citing literature: Ghane-Kanafi 2015; MIT OCW ESD.77; GERAD notes; OR StackExchange) establish that **weighted sums cannot generate points on nonconvex parts of the Pareto front** — the canonical static scalarization limitation. The mechanism there is **frontier geometry under a single optimization**; the mechanism here is **the action quantifier under per-weight feasibility** (∃a∀w vs ∀w∃a) — a different failure mode, and one that persists even where every per-weight problem is feasible (no frontier nonconvexity is involved: the witness datum's per-weight feasible sets are nonempty for every cone weight). **Delta stands; Das–Dennis cited as the static backbone.**

### 2.2 Control barrier functions (multiple barriers vs aggregate certificates) — **known-and-weaker; the composition line must be cited**

An active literature composes multiple CBFs: combinatorial/nested Boolean CBF composition (arXiv, *Combinatorial Control Barrier Functions*), compatibility of multiple CBFs under input bounds (2025), multiple barrier certificates for forward invariance in hybrid inclusions (UCSC hybrid-systems line). The field's known facts include: a conjunction of barriers is not certified by a single barrier function, and compatibility across multiple barriers is a genuine difficulty — the **static/feedback cousin** of the noncompensatory registry. What the searches do not surface: the **assessment-side theorem** — per-scalarization feasible plan sets with the exact quantifier localization, the closed-cone pointwise equivalence, and a witness where every scalarization has its own safe plan but no plan is safe for all. **Delta stands at bounded-search level; the composition/compatibility line cited as the neighbour.**

### 2.3 Viability theory — **hierarchy inclusion = standard constraint monotonicity (concede); localization + witness = no match found**

The viability-kernel literature (Aubin; Frankowska 1990, viability kernels of differential inclusions with constraints; Saint-Pierre; Maidens 2013 Lagrangian kernel approximation; Krawczyk 2013 applied survey) treats kernels under a **single constraint set**, and the monotonicity of the kernel in the constraint set is standard: `K(S ∩ S') ⊆ K(S) ∩ K(S')`. **Theorem A(i)'s inclusions are exactly this monotonicity applied to `S_typed ⊆ S_w ⊆ S_phys` — this must be, and is herewith, conceded as known mathematics, not claimed.** What no surfaced source has: (i) the **per-state action-set identity** `E_typ = ⋂_{w∈C} E_w` (Theorem A(ii)) — the localization of the entire assessment gap in the plan quantifier, with the closed-cone choice making the pointwise aggregate lossless (Lemma 3); (ii) a **witness datum whose regions are closed-form** with the per-weight plan disagreement exhibited and split into a rescue set and a certified impossibility region. No "vector viability kernel" or multicriteria-kernel separation surfaced. **Delta stands at bounded-search level.**

### 2.4 Sustainability economics (weak/strong, genuine savings, critical natural capital) — **the debate is established conceptually and empirically; no formal dynamic separation theorem surfaced**

The weak/strong sustainability debate is a mature literature: substitutability-based definitions (environmentandsociety.org; scipublications 2021; the THRIVE/strong-sustainability line); Genuine Savings as the leading weak-sustainability indicator with its critical literature (World Bank; **Boos 2015, *Genuine Savings as an Indicator for "Weak" Sustainability*, cited 79+**; Hanley et al. empirical testing of GS; Di Gennaro 2025 extensions); strong sustainability in the SEEA framework (**Usubiaga-Liaño et al. 2025**, critical-natural-capital preservation); capital-theory critiques (the Pezzey/NPV-unsustainability line surfaced via the Stern capital-theory appraisal). The searches surface **indicator critiques, measurement debates, and conceptual taxonomies — no theorem that separates scalarized from noncompensatory assessment as feasibility operators on a dynamical system**. One close-sounding hit ("The problems with weak sustainability and associated indicators" — the computational underpinning of an index defines what it can measure) is again indicator-level analysis. **The strengthening is the dynamic formalization of this debate's core claim; the debate literature is cited as motivation, not as prior art for the theorem form.**

### 2.5 MCDA (compensability analysis) — **known-and-weaker; must be cited as the static decision-analysis analogue**

The MCDA literature already maps compensatory aggregation ↔ weak sustainability and outranking/noncompensatory methods ↔ strong sustainability: **Cinelli et al. 2014** (*Analysis of the potentials of multi criteria decision analysis for sustainability assessment*, cited 1257 — ELECTRE/PROMETHEE/DRSA as non-compensatory approaches supporting a strong-sustainability concept), **Schär et al. 2025** (*Analysing the Compensatory Properties of the Outranking…*), Wulf et al. 2025 (compensating vs outranking aggregation for energy sustainability assessment). This is the **static preference/aggregation** analysis of exactly the compensability distinction — established and to be cited. The theorem's content — **dynamic transition feasibility under declared disturbances, with the quantifier localization and the rescue/impossibility split** — is not the MCDA question (no surfaced source asks it). **Delta stands at bounded-search level.**

### 2.6 Multi-objective RL / safe RL / reachability games — **adjacent; scalarization-dependent policies known, the feasibility separation not surfaced**

Constrained MORL with linear scalarization is established (the NeurIPS/MLR constrained-MORL framework line; scalarization-dependent optimal policies are a staple of the MORL literature — Vamplew's preference-vector line via the surfaced surveys); reachability-estimation safe RL (RESPO, NeurIPS) and concurrent reachability/safety games are established. That **optimal plans depend on the scalarization** is trivially known in MORL — and is precisely why Theorem A(ii) matters: it shows the dependence is not an optimality artifact but can infect **feasibility/safety itself**, with the closed-cone equivalence making the static layer lossless so the gap is purely the quantifier. No surfaced source states the feasibility-side separation. **Delta stands at bounded-search level; MORL scalarization line cited.**

### 2.7 Hybrid safe-transition synthesis — **backbone established (E6 already adjudicated this line)**

Temporal-logic reach-avoid-stay synthesis, switching-protocol synthesis, and mode-transition safety (the surfaced FOCAS-lab reach-avoid-stay line; LTL-guided safe RL; reactive switching protocols) confirm again that the **transition machinery itself** is established — consistent with the provisional answer. Nothing surfaced on assessment-doctrine separation. **No change to the standing adjudication.**

### 2.8 Pure quantifier logic — **no applied counterpart**

The quantifier-commutation literature surfaced is pure logic (StackExchange/math-overflow-level; Timany's commuting-quantifier notes) — no control/viability/sustainability application. **No match found (bounded search).**

## 3. The novelty map for the manuscript (what Paper 1 cites vs claims)

**Cited as backbone / known result types (never claimed):**
1. The backward robust-predecessor recursion: Aubin–Bayen–Saint-Pierre; Saint-Pierre; capture basins; hybrid reachability (Lygeros–Tomlin–Sastry line) — per the standing provisional answer.
2. Constraint-set monotonicity of viability kernels (Theorem A(i)'s inclusions): the Aubin/Frankowska kernel lineage.
3. Weighted-sum static limitations: Das–Dennis 1997/1998.
4. Compensability analysis in MCDA: Cinelli et al. 2014; Schär et al. 2025; the outranking line.
5. Multiple-CBF composition/compatibility: the combinatorial/compatibility CBF line.
6. Scalarization-dependent optimal policies in MORL: the preference-vector line.
7. The weak/strong sustainability debate and Genuine Savings (motivation, not prior art for the theorem form): Neumayer's critique line; World Bank GS; Boos 2015; Hanley et al.; Usubiaga-Liaño et al. 2025.

**Claimed as the contribution (bounded-search deltas, honestly labelled):**
1. **Theorem A(ii):** the per-state identity `E_typ = ⋂_{w∈C} E_w` and the quantifier-order characterization of the two assessment predecessors — the noncompensatory assessment is exactly "one plan for every price vector", the aggregate family is "a plan per price vector", and the gap is their noncommutativity. With the closed cone the pointwise aggregate is lossless (Lemma 3), so the separation is *purely* dynamic.
2. **Theorem B:** a transparent two-architecture datum with closed-form assessment regions, the false-positive triangle `{s_1 < 2, s_2 < 2, s_1+s_2 ≥ 2}`, per-weight plan disagreement (FAST-only/SLOW-only/both weight classes), and the rescue/impossibility split at the bridging budget `x ≥ c` — the negative-certificate form with four exhibited per-action violations.
3. **Theorem C:** the hierarchy and the separation propagate through the multi-stage backward induction.
4. The **interpretation**: the first formal dynamic separation of the weak and strong sustainability assessment doctrines on one transition system with one robustness standard — every aggregate accepts (each licensing a different physical transition), the noncompensatory registry rejects, and the typed analysis names the resource that converts false positives into certified transformations.

## 4. Publication-safe novelty language

> We do not introduce backward reachability, robust predecessors, capture basins, or the monotonicity of viability kernels in their constraint sets. Our contribution is a theorem about **assessment doctrines** on the same exact-tube transformation datum: we show that the noncompensatory (strong-sustainability) assessment equals the intersection of all closed-cone scalarized (weak-sustainability) assessments *at the level of plans* — `E_typ = ⋂_w E_w` — while at the level of feasible states the aggregate family is strictly coarser, because "a plan exists for each price vector" does not commute to "one plan exists for all price vectors". On an explicit two-architecture datum the gap is a region with interior in which every price vector certifies its own transition and no transition respects the floors; the typed recursion splits this false-positive set into a rescue set (fundable bridges) and a certified impossibility region, and the separation propagates through the backward induction. The static companions of this distinction — weighted-sum limitations on nonconvex fronts (Das–Dennis), compensability analysis in MCDA (Cinelli et al.), multiple-barrier composition — do not address the dynamic quantifier structure.

## 5. Claim to reject (retained from the provisional answer)

Reject, again and now with the strengthening in hand: *"the first general theorem for robust transformation between system architectures"* — still not supported; robust reach-avoid with resets is established. The supported claim is the assessment-doctrine separation above.

## 6. Gate decision

The four gate items of `paper1_typed_false_positive_theorem.md` §10:

| item | verdict |
|---|---|
| novelty vs robust predecessor/reach-avoid-maintain theory | **closed at the search level**: the strengthening's deltas (A(ii) localization, B witness + split, C propagation) have **no surfaced counterpart** in six literatures (bounded absence); every backbone identified and mapped for citation; the concession list (§3, items 1–2) is explicit |
| nonduplication vs Paper 2 | **established** (theorem file §3 seam + §10; F02 owns static compensation, Lemma 3 is its closed-cone complement proved locally) |
| target-journal contribution fit | the contribution profile is now the **assessment-separation theorem + witness**, not the recursion — the broad methods/sustainability-theory route the provisional answer §5 named as viable with exactly this strengthening |
| nontrivial instantiation | **executed** (25/25 machine checks, exact integer arithmetic) |

**Decision: Paper 1's independent-result gate is CLOSED at the internal level.** Paper 1 proceeds to manuscript drafting as a journal article. Conditions attached, per the bounded-absence discipline: (i) the manuscript's novelty claims use §4's language with the §3 concession list verbatim; (ii) if external review or a later database sweep overturns a no-match-found verdict, the fallback destination (monograph/series introduction, per the architecture doc) applies unchanged; (iii) the E6/G-POS register line "full-text pass remains open" is discharged by this file at the search level — the deeper database sweep remains available to external review and is recorded as such.

## 7. Search record

12 queries executed 2026-08-28 via the z-ai web-search function; raw results at `paper1_instantiation/novelty_searches/`: (q1) weighted-sum/Das-Dennis; (q2) multiple-CBF conjunction; (q3) vector/multicriteria viability kernels; (q4) weak/strong sustainability formal models; (q5) genuine savings critiques; (q6) multi-objective reachability/safe RL; (q7) noncompensatory MCDA/outranking compensability; (q8) kernel/aggregate Lyapunov constraints; (q9) safe mode-transition synthesis; (q10) price-dependent optimal paths/capital theory; (q11) quantifier commutation (applied); (q12) weak-sustainability false positives/threshold transitions. Key citations surfaced: Das–Dennis 1997/1998; Ghane-Kanafi 2015; combinatorial CBF composition (arXiv); multiple-barrier hybrid invariance (UCSC); CBF compatibility 2025; Frankowska 1990; Maidens 2013; Krawczyk 2013; Aubin viability lineage; Boos 2015; Hanley et al. GS testing; Di Gennaro 2025; Usubiaga-Liaño et al. 2025; Cinelli et al. 2014; Schär et al. 2025; Wulf et al. 2025; constrained-MORL frameworks (NeurIPS 2024, MLR); RESPO; concurrent reachability/safety games; LTL-guided safe RL; switching-protocol synthesis; Pezzey/NPV-unsustainability line via the capital-theory appraisal.
