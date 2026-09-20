# S-Note: Mathematical basis and verification artifacts of SafeTransition 1.0.0

*Supplementary note to the software description "SafeTransition: exact
rational certification of transition safety for sustainability assessment"
( Environmental Modelling & Software, submission).*

*Accompanies:* A. Abaee (2026). *SafeTransition: exact rational certification
of transition safety for sustainability assessment.* Verification deposit:
<https://doi.org/10.6084/m9.figshare.33764023>.

---

## S1. The assessment-operator framework, as implemented

A typed transition datum consists of a phase state `z = (q, x, s1, ..., sn)`
(phase flag, fund coordinates, typed floors normalized to zero), a finite
action set, a disturbance set, an exact tube `Tube(a, d)` for each action and
disturbance (the set of states visited over the review period), a
transition-safe set `S`, and a destination set `G` reached under an endpoint
reset with gain vector `e`.

Five operators map a state to its admissible actions (companion manuscript
"Aggregate Indices and Transition Safety", Section 3; quoted section numbering
there):

| Operator | Condition on each `(a, d)` | Destination test |
| --- | --- | --- |
| Typed, noncompensatory `E_typ` | `Tube(a,d) ⊆ {x ≥ 0, s_i ≥ 0 ∀i}` | successor in `G` |
| Scalarized aggregate `E_w` | `Tube(a,d) ⊆ {x ≥ 0, w·s ≥ 0}` | successor in `G`, `w·s ≥ 0` |
| Exact-tube physical `E_tube,phys` | `Tube(a,d) ⊆ {x ≥ 0}` | successor in `G_phys` |
| Endpoint-only physical `E_end` | endpoints in `{x ≥ 0}` | successor in `G_phys` |
| Typed-endpoint `E_end,typ` | endpoints in `S` | successor in `G` |

Because `End(a,d) ⊆ Tube(a,d)` and `S ⊆ S^w ⊆ S^phys`, the chain
`E_typ(z) ⊆ E_w(z) ⊆ E_tube,phys(z) ⊆ E_end(z)` holds at every state and
weight; the library verifies it exactly on request (`check_chain`).

The accepted-state set `V[E] = {z : E(z) ≠ ∅}` and the compensatory accepted
set `V_weak = ⋂_w V_w` follow; the witnessed separation
`V_typ ⊊ V_weak` (strict in general) is the formal statement of what a
composite index cannot see. The library's `compute` interface reports the
per-weight licensing thresholds `ρ1` and `ρ2` between which the aggregate
operator licenses plans the typed operator rejects.

## S2. The recursions

**Typed recursion.** On an explicit state–action graph, `W_1 = {z : E_typ(z) ≠ ∅}`
and `W_{k+1} = {z : some action keeps every visited state safe and its
successor lies in W_k}`. Polynomial in graph size and horizon for
constant-time predicates.

**Belief-space recursion** (companion manuscript "An Obstruction Calculus
for Viability under Incomplete Observation", robust epistemic kernel):
states carry observation labels γ; an action is admissible for a belief `B`
when no state in the fibre of `B` enters a violation under it; the belief
updates to the labels reachable under the action. `W_k` denotes the
k-step viable beliefs; the recursion is sound and complete in finite
systems. Beliefs in `W_1 \ W_2` exhibit post-observation recourse failure.

## S3. The certificate family

**Farkas certificates.** For a stacked rational system `Au ≤ b`, Fourier–
Motzkin elimination with provenance tracking derives rows together with
their multiplier vectors over the original rows. A derived contradiction
`0 ≤ c, c < 0` yields, after normalization, `λ ≥ 0` with `λᵀA = 0` and
`λᵀb < 0`; the library returns `λ` with the infeasibility margin
`−λᵀb > 0` and re-verifies both identities exactly before returning.

**Common-action obstruction.** Fires when the safe-action sets of
pairwise-compatible states intersect emptily while each is nonempty; a
minimal conflicting subfamily is reported.

**Observation-fibre criterion.** An exact observation-only certifier exists
iff safe-set membership is constant on observation fibres; a violating
fibre is reported otherwise.

## S4. The twenty-four benchmark checks

The `benchmark` module re-derives, in exact rational arithmetic, every
deposited value of the resource-transition benchmark (Schaefer realization:
`r = 4`, `K = 10`, `B_lim = 2`, `H_max = 13`, `δ0 = 1/2`):

1. witness datum `(x, s1, s2) = (1/2, 6/5, 6/5)`; gain `e = (1/4, 1/4)`; cost `c = 1`;
2. FAST tubes `(6/5, −3/10, 6/5)` benign and `(6/5, −4/5, 6/5)` adverse; `s2` flat;
3. STAGED at the rescue witness: fund `3/2 → 1/2`, `s1: 6/5 → 29/20`;
4. parameters exact;
5. stock levels `16/5`, `17/10`, `6/5`, all below `K/2` (surplus increasing);
6. certified leg slopes `3/yr`, `4/yr`;
7. quota range `[3 + σ(17/10), 3 + σ(16/5)]`;
8. quota admissibility, peak `1463/125 ≤ 13`;
9. closed season on `(1/2, 1)`;
10. benign branch tracks its line exactly (`σ(L) − H* = −3`);
11. strike drops the stock by `δ0 = 1/2` (`17/10 → 6/5`);
12. conservatism: `σ ≥ 528/125 ≥ 4` on the adverse recovery leg;
13. benign recovery: `3 ≤ σ(17/10) = 1411/250`;
14. tubes conservative for the nonlinear realization;
15. index `s1 + s2` at `w = (1,1)`: `(12/5, 2/5, 12/5)`, min `2/5 > 0`;
16. floor breached on both branches (`−4/5` adverse, `−3/10` benign);
17. typed reading: FAST and SLOW both typed-infeasible at the witness;
18. licensing thresholds `ρ1 = (2 − s1)/s2 = 2/3`, `ρ2 = s1/(2 − s2) = 3/2`;
19. no weight ratio licenses a typed-safe plan (`ρ1 < 1 < ρ2`);
20. rescue threshold `κ* = 1 − x`; witness shortfall `1/2`; rescue witness `3/2 ≥ c`;
21. sustained-yield quota `σ(16/5) = 1088/125`, admissible;
22. STAGED rebuild: stock `16/5 → 69/20`, both margins improve by `e = 1/4`;
23. STAGED quota `[2051/250, 8539/1000]`, admissible;
24. schedule values assembled from verified exact quantities.

All 24 checks pass; runtime under one second on a laptop CPU.

## S5. Package artifact tree

```
safetransition/
├── pyproject.toml, LICENSE (MIT), CITATION.cff, README.md, CHANGELOG.md
├── dashboard.html                  # rendered single-file dashboard
├── docs/
│   ├── EMS_submission_plan.md
│   └── EMS_style_notes.md
├── examples/
│   ├── northern_cod_dashboard.py   # benchmark + certificates → dashboard
│   └── partial_observation.py      # recourse failure; fibre criterion; Farkas
├── src/safetransition/             # 9 modules, 1,269 lines
└── tests/                          # 27 tests, 283 lines
```

## S6. Citation

- Abaee, A. (2026). *SafeTransition: exact rational certification of
  transition safety for sustainability assessment* (software description,
  EMS submission).
- Abaee, A. (2026). *Verification code and figure pipeline for Aggregate
  Indices and Transition Safety* [data set]. figshare.
  <https://doi.org/10.6084/m9.figshare.33764023>
- Abaee, A. (2026). *Aggregate Indices and Transition Safety: A
  Quantifier-Order Separation Between Scalarized and Coordinate-Wise
  Feasibility* (companion manuscript).
- Abaee, A. (2026). *An Obstruction Calculus for Viability under Incomplete
  Observation* (companion manuscript).
