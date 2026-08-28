# E6 — External Novelty Audit: Execution Record (Bounded-Search Level)

**Provenance:** executed 2026-08-26 by the programme agent (Z.ai Code) using targeted web-literature search (11 queries across the six literatures named in `E6_EXTERNAL_MATCHING_MATRIX.md`), against the matrix's own priority ordering and output protocol.

**Status discipline — what this execution is and is not.** This is a genuine external-literature check at the **bounded-search level**: verdicts rest on search-result identification (titles, abstracts, snippets) of published work, not on full-text line-by-line comparison. Two asymmetries follow, and they are deliberate:

- **Positive identifications are robust.** A verdict of `known-equivalent` or `known-and-weaker` cites specific published work whose existence and relevance the search establishes directly. These verdicts do not weaken with more search.
- **Absence claims are bounded.** A verdict of `confirmed-new` here means *no match found in the performed searches*; it is an absence claim limited to those searches and must be re-visited at full-text level during paper drafting.

No theorem *status* (PROVEN / COMPUTED_PARTIAL / …) is changed by this audit; what changes is the **novelty mapping** — what each result must cite, and what remains defensible as a delta.

---

## Verdicts by matrix row

### Row 4.1 — R05 contract-amplitude composition (linear case) vs ISS/vector-Lyapunov small-gain

**Verdict: known-equivalent (mathematical backbone), presentational delta only.**

The linear-gain / matrix spectral-radius condition ρ(Γ) < 1 for interconnection stability is classical and fully established: Dashkovskiy–Rüffer (2007, *An ISS small-gain theorem for general networks*, ~467 citations — the max-form generalization, explicitly described as the nonlinear generalization of ρ(Γ)<1); the network ISS literature that followed (Rüffer's monotone-operator treatment; Liu et al. 2011 cyclic small-gain); and the linear-gain Lyapunov hybrid case (Mironchenko–Liberzon-type results with gain matrix Γ_M and ρ(A)). The E6 matrix's priority-one fear — "the deficit-budget form may coincide with known vector-Lyapunov conditions" — is **confirmed**: the stability content of R05.Thm1/2 is the known small-gain condition in linear-gain form.

**Required action for Paper 2:** R05's composition section must cite the ISS small-gain literature as the backbone and claim only the *contract-amplitude/erosion bookkeeping* (deficit budgets δ_ij, margins α_i, wired into certificate status) as the delta — a **presentational/operational** delta, not a mathematical one. Paper 2 must not present the linear composition theorem as new mathematics.

### Row 2.2 — E2.B1 measurable selection for safe-action maps vs Quincampoix/Aubin regulation selection

**Verdict: known-equivalent (re-instantiation confirmed — the matrix's highest-priority check).**

Selection procedures of the regulation map are classical viability theory: the search surface confirms "one can naturally use selection procedures of the regulation map (Chapter 6 of Aubin, *Viability Theory*)" and the surrounding literature (Quincampoix's viability-kernel characterization work; Cardaliaguet's survey of viability results for differential games; Krawczyk's applied outline). The measurable-selection-for-viable-controls result that E2.B1 re-instantiates is, as the matrix feared, a known result type in this literature.

**Required action:** E2.B1 must be labelled "known result type, re-proved at the programme's scope" in Paper 2's atlas, citing Aubin's regulation-map selection and the Kuratowski–Ryll-Nardzewski-based viability selection literature. The defensible delta for E2 is the **(REG)-certificate-family packaging** (certificates as first-class typed objects with status fields) — packaging, not mathematics.

### Row 4.2 — A4 monotone-operator assume–guarantee vs nonlinear ISS small-gain

**Verdict: known-and-weaker (existence mechanism close to known); delta confirmed as the shared-control witness + erosion semantics.**

The max-form nonlinear small-gain theorem for networks (Dashkovskiy–Rüffer 2007 and successors) is established via exactly the monotone/fixed-point machinery A4's existence proof uses (Tarski-type greatest-fixed-point constructions appear in Rüffer's monotone-operator formulation). The existence theorem itself is therefore close to known proof technology, as the matrix expected.

**Confirmed deltas:** (i) the **shared-control nonconvexity witness** (A4.Ex3) — no ISS counterpart surfaced in the searches; (ii) the **erosion-depth contract semantics** (contracts as *numbers* with depth bookkeeping, not gain functions); (iii) the control-in-the-loop setting (implementation sets, not signal gains). Paper 1/Paper 2 must cite Dashkovskiy–Rüffer as the backbone and claim (i)–(iii).

### Row 6.2 — A4/Tarski numeric contracts vs quantitative assume–guarantee

**Verdict: known-and-weaker; a direct near-neighbour exists and must be cited.**

Eqtami et al. (2019, *A Quantitative Approach on Assume-Guarantee Contracts*, ~29 citations) constructs quantitative assume-guarantee contracts for subsystems with a **fixed-point algorithm computing contract parameters** so that all subsystems fulfill their contracts simultaneously — this is numeric-contract AG with fixed-point composition, exactly the region the matrix flagged ("numeric-contract AG is the candidate delta"). The Pacti tool (assume-guarantee contracts for compositional analysis) confirms an active applied literature.

**Confirmed delta (narrowed):** the *dynamical* setting — A4's contracts are erosion depths tied to viability/invariance under dynamics with shared controls and nonconvex implementation sets, versus Eqtami's interface/parameter contracts. The sharpness witness stands. The claim "numeric contracts + fixed-point composition" itself is **not** new.

### Row 3.1 — B1 sampled-data erosion theorem vs inter-sample safety literature

**Verdict: known-and-weaker; the field is established and crowded; delta confirmed as the two-depth conversion bookkeeping.**

The searches surface an active sampled-data safety literature: Mitchell (2012, *Ensuring safety of nonlinear sampled-data systems* — inter-sample trajectory safety with sampled-data control policies); Taylor et al. (*Safety of sampled-data systems with control barrier functions*, SD-CBFs — relating continuous-time CBF properties to sampled-data practical safety); Niu et al. (2021+, CBF-constraint-at-sampling-time guarantees for unknown sampled-data systems). Inter-sample confinement is precisely this literature's subject.

**Confirmed delta:** the **three-hypothesis certificate form with explicit two-depth erosion bookkeeping** (sample-time depth R → continuous-time depth r at cost V_max·T_s ≤ R − r; the repaired B1.Thm1 form) as a *conversion certificate* wired into the status discipline. Paper 5 must cite the SD-CBF/sampled-data safety literature and claim only the depth-bookkeeping form.

### Row 3.3 — E4 generation transfer vs hybrid/impulse invariance

**Verdict: known-and-weaker for the invariance conditions; delta confirmed as the non-derivability witness.**

Hybrid jump-invariance is established: Aubin's viable impulse differential inclusions (hybrid systems *as* impulse differential inclusions — the "Substratum" line; Aubin–Haddad impulse viability) and Chai–Sanfelice–Teel (2018, forward invariance of sets for impulsive differential inclusions, ~67 citations).

**Confirmed delta:** the **depth co-Lipschitz jump margin as declared data** together with the **refutation showing it is not derivable** from the other data — the non-derivability witness has no surfaced counterpart and is the citable delta.

### Row 5.1 — C3 closure classification vs moment-closure literature

**Verdict: known-and-weaker (ingredients established); delta confirmed as the iff-classification form.**

The moment-closure literature is established and self-aware about closure validity: Kuehn (2015/2016, *Moment Closure — A Brief Review*, ~205 citations; 2024, *Preserving Bifurcations through Moment Closures*); Murrell et al. (2004, conditions a second-order closure should satisfy). The two-patch quadratic positive case is, as the matrix expected, elementary/folklore-adjacent.

**Confirmed delta:** the **fibre-constancy iff classification** (exact-closure characterization as projectability) as a theorem form. The searches surface closure *conditions and desiderata*, not an iff-classification theorem. Bounded-search evidence; re-verify at full text.

### Row 1.1 — B3 Operator II exact tubes vs HJ reachability error bounds

**Verdict: known-and-weaker; the error-bound framework is established.**

Bokanowski–Zidani and collaborators (error estimates for HJB under state constraints; reachability and minimal times for state-constrained nonlinear problems) establish the error-bound framework the matrix named. The **exact-tube-at-finite-review-depth discipline** (finite architecture, fixed review, typed disturbance/review semantics) remains the delta — presentational-adjacent but tied to the certification semantics. Compare at full text during Paper 2 drafting.

### Rows with no match found (bounded search) — deltas stand, absence bounded

- **Row 3.2 (A3 budgeted piecewise-history space, interleaved-segment topology):** hybrid estimation/observability literature exists (piecewise-affine hybrid systems, discrete-sensor estimation) but no surfaced match for the *budgeted* history-space class with clopen-fibre kernel closure. Verdict: no match found (bounded search).
- **Row 4.3 (E7/C-e moiety barriers):** searches surface process-safety *regulatory* material-balance practice and the general barrier-certificate literature, but no surfaced match for **conservation-based barriers yielding kernel bounds from flux data alone** in the noncompensatory multi-moiety (Farkas-tied) form. Verdict: no match found (bounded search) — one of the stronger delta candidates, consistent with its role as Paper 3's bridge theorem.
- **Row 6.1 (E1.A2 judgment calculus):** compositional-reasoning calculi exist (assume-guarantee rule soundness/completeness lineage); the **sustainability-judgment typing over the TCS-1.0 inventory with status discipline** stands as the delta (typing/packaging, honestly labelled).
- **Rows 1.2/1.3 (C4.2 uniform-horizon; C-a.Thm2 decidability typing):** termination/uniform-horizon arguments and game-solving complexity results exist in the named literatures; the *diagnostic-soundness* tying and the per-sentence O(N·|grid|) judgment typing stand as bounded-search deltas.

---

## What this means for the programme's novelty claim

1. **The two feared re-instantiations are confirmed.** R05's linear composition (ISS small-gain backbone) and E2.B1's measurable selection (regulation-map selection) must be cited as known result types. Neither was load-bearing as a novelty claim, but Paper 2's atlas chapters must now say so explicitly.
2. **A4's exposure is real but survivable:** the numeric-contract AG near-neighbour (Eqtami 2019) and the small-gain backbone both require citation; the defensible deltas are the shared-control witness, the erosion-depth semantics, and the dynamical setting.
3. **The strongest defensible mathematical deltas** (bounded-search level): E7/C-e moiety barriers from flux data (no match found), the C3 iff-classification form, the E4 non-derivability witness, the A3 budgeted history-space class, and the B1 two-depth conversion bookkeeping.
4. **The integrated-architecture claim is unaffected — and is now clearly the main claim.** No surfaced literature provides: a typed canonical system schema with mapping registry; certificate/status discipline as a first-class layer; or the negative-certificate methodology (complexity retained only on scored evidence). The programme's novelty claim should be **the architecture and the discipline**, with individual theorems cited against their backbones. This aligns with the post-v1.0 positioning: with negative empirical certificates, the distinctiveness claim rests on the typed noncompensatory kernel machinery, the admission/certificate discipline, and the negative-certificate semantics — exactly the layers where the searches found no counterpart.
5. **Forecast-benchmarking adjacency (the "Makridakis with vocabulary" risk):** no surfaced literature pairs persistence-benchmark negative certificates with a typed viability architecture; the cod/Edwards negative certificates should be positioned as *methodology outputs* of the architecture, not as standalone forecast results.

## Residual obligations (full-text level, at paper-drafting time)

- Full-text comparison for rows 4.1, 4.2, 6.2, 3.1 (the known-and-weaker verdicts' exact scopes).
- The absence claims (rows 3.2, 4.3, 6.1, 1.2, 1.3) re-checked against full databases (MathSciNet/Zentralblatt/Google Scholar forward searches) — bounded-search evidence only.
- G5's register row updated to **EXECUTED (bounded-search level)** — not "fully executed"; the full-text pass remained open and was assigned to the paper-drafting wave. **Update 2026-08-28: executed for Paper 1's strengthened independent result at the search level (`research_program/paper1_full_text_novelty_pass.md`, 12 queries, raw results at `research_program/paper1_instantiation/novelty_searches/`) — the deeper database sweep remains available to external review.**

## Search record

11 queries executed 2026-08-26 via the z-ai web-search function (queries and result files preserved in this section's provenance; key citations: Dashkovskiy–Rüffer 2007 arXiv:math/0506434 / Springer s00498-007-0014-8; Liu–Nesic–Dower–Liberzon 2011 S0005109811003177; Mironchenko–Liberzon hybrid Lyapunov small-gain; Aubin *Viability Theory* ch. 6 regulation selection; Cardaliaguet viability-games survey; Eqtami et al. 2019 quantitative AG contracts; Pacti; Mitchell 2012 sampled-data safety; Taylor et al. SD-CBF; Niu et al. 2021; Chai–Sanfelice–Teel 2018; Kuehn 2015 arXiv:1505.02190 and 2024 SIMA 23M158440X; Murrell et al. 2004; Bokanowski–Zidani error-estimate line; Aubin–Haddad impulse viability line).
