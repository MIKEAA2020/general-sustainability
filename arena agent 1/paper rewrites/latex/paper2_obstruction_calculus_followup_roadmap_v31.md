# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v31)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v31 changes:** **Round 12 shipped — the five-item extension round, Lean
skipped by decision.** (1) **P3 edition 4**
(`paper2_probabilistic_sufficiency_v4.tex`): the distributionally robust
interpolation lemma (inf over the ε-contamination set
q = (1−ρ)p + ρr of Σ q v equals the exact mixture
(1−ρ)E_p[v] + ρ min_y v_y; pointwise V^ρ = (1−ρ)V⁰ + ρV¹; concave PWL at
every ρ), the delayed-class ρ-closed form with symmetric-prior levels
{0, (1−ρ)/2, 1}; the probe-count bound
p_wrong(2m+1) ≤ (4ε(1−ε))^((2m+1)/2) ≤ e^(−2n·sep²) verified exactly at
n = 1, 3, 5, 7, 9 (values 1/10, 7/250, 107/12500, 341/125000,
22273/25000000 at ε = 1/10); the general additive deadline law
d(u,θ) = c(u) + h(u)θ ⟹ viability ⟺ z₀ ≥ 1 + T·d₀ + e_p on two instances
(thresholds 21/10 + T/10 and 41/20 + 3T/20). Verify **26/26** (chained
16+21/15/6); 9 pp, overfull 0. (2) **New P2-lineage computational paper**
`paper2_exact_belief_computation_v1.tex` (medium instance, 48 augmented
cells, five controls): exact point-based evaluation (alpha-set values at
7 probed rational beliefs × 3 levels × 3 horizons equal trajectory
enumeration; the k = 6 alpha-set deduplicates 15,625 sequences to 9
witness vectors), survivable-set antichain compression (48 stored sets in
place of 180 raw subset evaluations), the averaging obstruction (every
control's drifts sum to −2/5 per step over the four cells; no
three-periodic policy keeps all four cells alive from z₀ = 2.1, 60-step
certificates), the band structure (four singletons at z₀ = 1.0; exactly
the four coordinate pairs at every z₀ ≥ 1.1), and the observation ladder
(one θ₁ probe reaches 1 for every z₀ ≥ 1.1 and 1/2 at the edge — one
probe exhausts observation above the floor's edge). Verify **11/11**; 3 pp,
overfull 0. (3) **Placement decided:** DR interpolation, probe-count
asymptotics, and the additive deadline law stay in **P3 (edition 4 — same
paper)**: shared delayed-class machinery, exact rational arithmetic, and
the verify chain; PBVI/ZDD scaling on medium instances becomes a
**separate computational paper in the P2 lineage** with its own instance
battery and compression story. (4) **Supersession-banner pass complete**
via `supersession_map_v1.md` — programme-wide pointer map, no frozen file
edited. **Round-12 catches (addendum
`paper2_probabilistic_sufficiency_v4_addendum.md`):** the drift-sum
constant in the scaling draft was wrong (−1/5 → −2/5, caught by the
verifier), the one-probe functional needed expected-survival semantics
(1/2 at the edge, 1 above), and the alpha-set is level-dependent.
**Remaining:** step 4 (P5) pending owner data; formalization (Lean) of the
closed forms deferred by decision; computational-paper scaling (hundreds
of cells) is the next P2-lineage step.

## Flagship board (v17 architecture; status updated)

| # | Flagship | Latest | Status |
|---|----------|--------|--------|
| P1 | Obstruction calculus | v49 + supp v46 | shipped, frozen; owner-side venue decision |
| P2 | Computational certification + library | comp v9 + S1 v6 + `viacert`; **+ exact belief computation v1** | current |
| P3 | Probabilistic sufficiency | **v4 (DR + asymptotics + deadline law)** | current |
| P4 | Worked-systems supplement | ws v10 | current, scan-clean (`592a1ba`) |
| P5 | Applied paper | pending owner data | parked (R12) |

Seeds (byte-frozen): `paper2_stochastic_selector_v2*`,
`paper2_belief_state_v2*`, `hidden_parameter_learning_v1*` (tex + verify
each) + `figs_bs2/` five PDFs + `paper2_belief_state_figures.py`.
Editions frozen in place: P3 v1 (`bd04641`, 15/15), v2 (`36ed76b`, 18/18),
v3 (`c630363`, 23/23); P3 v4 is the current edition (26/26).

## Build-order status

1. P4 ws v10 — done.
2. P2 comp v9 + S1 v6 + `viacert` — done; **exact belief computation v1 added (round 12)**.
3. P3 v4 — done (round 12; v1–v3 frozen).
4. P5 applied paper — pending owner data (unchanged since round 10).
5. Supersession banners — **done (round 12, `supersession_map_v1.md`)**; final roadmap rolls forward with each round.
