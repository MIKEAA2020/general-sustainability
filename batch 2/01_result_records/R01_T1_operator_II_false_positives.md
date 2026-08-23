# Result Record R01 — Docket T1: False Positives of Endpoint-Only and Aggregate Transformation Tests

## Field 1 — Result ID and target docket item

`R01` (three results: R01.Thm1 endpoint-only unsoundness; R01.Thm2 aggregate unsoundness; R01.Prop3 divergence mechanism). Target: **T1** ("a theorem proving false positives of endpoint-only/aggregate transformation tests"). Strengthens the proved exact-tube Operator II predecessor (corrected `04`).

## Field 2 — Verdict

- R01.Thm1, R01.Thm2: **proved** (new negative results).
- R01.Prop3: **proved** (mechanism generalization).
- The underlying exact-tube recursion itself: **classical but useful** (robust backward reachability; consistent with the packet's own provisional novelty answer, `control/03` §2A item 4).

## Field 3 — Exact statement

All statements use the Operator II data of corrected `04` §1 (finite review times `0=t_0<…<t_m=T`, meta-actions `A_k`, disturbance sets `D_k`, exact tubes `Tube_k`, exact successor sets `Succ_k`, transition-safe sets `S_k`, terminal set `G`), with the robust predecessor

```
RPre_k(W) = {(q,x) ∈ S_k : ∃a ∈ A_k ∀d ∈ D_k : Tube_k(q,x,a,d) ⊆ S_k  and  Succ_k(q,x,a,d) ⊆ W}
```

and its **endpoint-only weakening** `RPre^e_k(W)` defined by deleting the tube clause.

**R01.Thm1 (endpoint-only false positives).** There exist admissible Operator II data with Lipschitz right-hand side, compact action and disturbance sets, unique forward-complete solutions, and a nonempty exact-tube kernel `W_0`, such that:

1. `W_0 = ∅` (no state is robustly transformable), while
2. the endpoint-only recursion returns `W^e_0 = S_0 ≠ ∅`.

Consequently the endpoint-only test certifies robust transformability for states at which every causal policy violates transition safety within the first interval. Moreover, the endpoint-only recursion is sound for given data only if no accepted state admits a mid-interval excursion out of `S_k` — i.e. only if the tube clause never binds; it is degenerate exactly when within-interval transition safety is automatic.

**R01.Thm2 (aggregate false positives).** Let `P: X → Y` be an aggregate/projection map and let the *aggregate transformation test* replace `Tube_k ⊆ S_k` by `P(Tube_k) ⊆ P(S_k)` (and endpoints correspondingly). There exist admissible data with a noncompensatory safe set (product of component constraints) for which:

1. every trajectory satisfies `P(x(t)) ∈ P(S)` for all `t` (the aggregate test passes on every branch, forever), while
2. the componentwise viability kernel is empty — no admissible policy keeps the state in `S` for any positive time.

**R01.Prop3 (divergence mechanism).** In the witness of Thm1 the failure is not an artifact: if, in some direction `e`, the safe set `S_k` has width `w > 0` and the unmeasured-disturbance branch divergence in direction `e` satisfies `⟨e, x^{d_1}(t) − x^{d_2}(t)⟩ ≥ βt` for all policies and some `β > 0`, then no causal policy can keep the tube in `S_k` beyond time `w/β`, whatever the endpoint behavior. Endpoint-only tests are blind to exactly this quantity.

## Field 4 — State and phase space

Thm1: one architecture `q`, `X = ℝ` (finite-dimensional ODE class; phase state is the physical coordinate alone). Thm2: `X = ℝ²`, safe set `S = [0,1]×[0,1]`, aggregate `P(x_1,x_2) = x_1 + x_2`, aggregate space `Y = ℝ`. Both are sampled systems with within-interval continuous evolution and review-time meta-actions, per `TCS-1.0` §2.2 (sampled systems use flows between review times plus held commands).

## Field 5 — Quantifier order and information pattern

Exactly the Operator II order of corrected `04` §1: `∃a ∈ A_k ∀d ∈ D_k` (action chosen before disturbance; disturbance unmeasured within the interval; full phase state observed at review times). Thm1's hard direction uses the adversarial reading of `∀d` (both disturbance branches must be safe simultaneously under one action). No disturbance-observing control is admitted (master prompt, non-negotiable rule 1).

## Field 6 — Assumptions, including existence/completeness

- `f` Lipschitz in `(x,u)` uniformly in `d`; compact `U`, `D`; linear growth ⟹ unique, forward-complete solutions for held actions and measurable disturbances (satisfied by both witnesses).
- `Tube_k`, `Succ_k` are the *exact* all-branch sets of the declared solution concept (as required by corrected `04` §1 items 3–4; conservative outer tubes would only enlarge the false positives).
- Thm2's safe set is a product of component intervals (noncompensatory registry, `TCS-1.0` §2.5); no `Ω`-authorized substitution (axiom 4).

## Field 7 — Mapping type

`COUNTEREXAMPLE_OR_LIMIT` for the soundness of endpoint-only and aggregate tests (they are `REJECTED_MAPPING` instruments); the results *support* the `TRANSFORMATION` mapping type of the exact-tube predecessor by proving its tube clause cannot be dropped or projected.

## Field 8 — Self-contained proof

### Proof of R01.Thm1

**Data.** Two stages: `t_0 = 0 < t_1 = 1 < t_2 = 2`; one architecture. Dynamics `ẋ = u + d` with `u ∈ U = [−1,1]` (meta-action = any causal within-interval rule measurable in `t`, constant or not) and unmeasured disturbance `d(t) ∈ D = {−1, +1}` (constant on the interval — the declared disturbance class `𝒟` consists of the two constant branches; measurability and admissibility are immediate). Solutions are unique for each `(u(·), d)` and forward complete.

Safe sets: `S_0 = [−1/4, 1/4]` (binding), `S_1 = ℝ` (non-binding final interval). Terminal destination `G = [−1, 1]`.

**Step 1 — exact stage-1 predecessor.** `W_1 = RPre_1(G)` requires `∃u(·) ∀d ∈ {±1}: Succ_1(x, u, d) ⊆ [−1,1]` (the tube clause against `S_1 = ℝ` is void). Choose the constant rule `u ≡ −x`; then `∫₀¹u = −x` and the endpoints are `x − x + d ∈ {−1, +1} ⊆ G`, for **every** `x ∈ ℝ`. Hence `W_1 = ℝ`.

**Step 2 — exact stage-0 predecessor is empty.** `W_0 = {x ∈ S_0 : ∃u(·) ∀d ∈ {±1}: Tube_0(x,u,d) ⊆ S_0 and Succ ⊆ W_1 = ℝ}`. The successor clause is void (`W_1 = ℝ`), so `W_0` is exactly the set of states with a robustly tube-safe action. Let `x^{+}(t)`, `x^{−}(t)` be the two branch trajectories under one rule `u(·)` (the rule cannot depend on the unmeasured `d`). Then
`x^{+}(t) − x^{−}(t) = ∫₀^t [(u+1) − (u−1)] ds = 2t.`
Both branch trajectories must lie in `S_0`, an interval of width `1/2`. Two points `2t` apart both lie in an interval of width `1/2` only if `2t ≤ 1/2`, i.e. `t ≤ 1/4`. For `t > 1/4` this is impossible, **for every** `x ∈ S_0` and every rule `u(·)`. Hence no robustly tube-safe action exists anywhere in `S_0`, and `W_0 = ∅`: no state is robustly transformable.

**Step 3 — endpoint-only predecessor is full.** `W^e_0 = {x ∈ S_0 : ∃u(·) ∀d: Succ_0(x,u,d) ⊆ W_1 = ℝ}`. The successor clause is void, so `W^e_0 = S_0 ≠ ∅` (any rule witnesses, e.g. `u ≡ 0`, whose endpoints `x ± 1` are trivially in `ℝ`).

**Step 4 — degeneracy claim.** The same computation shows the general point: whenever the successor sets `Succ_k` can be steered into the next-stage set while the branch tubes diverge faster than the safe-set width absorbs, the endpoint-only recursion accepts and the true recursion rejects. Soundness of the endpoint-only recursion for given data is equivalent to: for every accepted `(q,x)` and every accepted action, `Tube_k ⊆ S_k` — i.e. the tube clause never binds on the accepted set. ∎

**Remark (why the packet's exact-tube clause is not dispensable).** Step 2 is the operational content: the endpoint test measures *dispersion at review times*, which the controller can cancel (`u ≡ −x` re-synchronizes endpoints exactly); the tube condition measures *uncontrolled within-interval dispersion* (`2t`), which no causal rule can cancel. These are different quantities; the theorem proves conflating them is unsound, not merely imprudent.

### Proof of R01.Thm2

**Data.** `X = ℝ²`, `S = [0,1]×[0,1]`, dynamics
`ẋ_1 = c + u, ẋ_2 = −(c + u)`, with `u ∈ [−1,1]` and constant `c > 1` (e.g. `c = 2`). Aggregate `P(x_1,x_2) = x_1 + x_2`, `P(S) = [0,2]`.

**Step 1 — the aggregate is exactly constant.** For every admissible rule and every branch, `d/dt (x_1 + x_2) = 0`, so `P(x(t)) ≡ P(x(0)) ∈ [0,2]` for every trajectory starting in `S`. Hence `P(Tube) ⊆ P(S)` and `P(Succ) ⊆ P(S)` hold on every branch for all time: the aggregate transformation test passes unconditionally.

**Step 2 — the componentwise kernel is empty.** Since `c > 1`, the velocity set is `c + u ∈ [c−1, c+1] ⊂ (0, ∞)`: `x_1` is strictly increasing at rate at least `c−1` and `x_2` strictly decreasing at rate at least `c−1`, for **every** admissible control. From any `x ∈ S`, either `x_1` reaches `1` or `x_2` reaches `0` within time `1/(c−1)`. Both faces belong to `∂S` and the velocity points strictly outward on them (`ẋ_1 > 0` on `{x_1 = 1}`, `ẋ_2 < 0` on `{x_2 = 0}`), so every trajectory exits `S` in finite time and no state is viable: `Viab(S) = ∅` (robustly and even existentially, since the sign of `c+u` is control-independent).

**Step 3 — conclusion.** The aggregate test certifies safety forever on every branch; the true noncompensatory kernel is empty. By the noncompensation axiom (`TCS-1.0` §9, axiom 4), the componentwise failure is not erased by the aggregate surplus: the two flows compensate in the aggregate while both components are destroyed — precisely the structure axiom 4 forbids aggregating away. ∎

### Proof of R01.Prop3

Let `e` be a unit direction and suppose `S_k ∩ (x + ℝe)` has width `w` (i.e. `sup{⟨e, y−x⟩ : y ∈ S_k, ⟨e', y−x⟩ = 0 ∀e'⊥e} − inf{…} = w` — concretely, the extent of `S_k` along `e`). If two admissible disturbance branches satisfy `⟨e, x^{d_1}(t) − x^{d_2}(t)⟩ ≥ βt` for `t ∈ [0, t_{k+1}−t_k]` under **every** causal rule (divergence is policy-independent — as in Step 2 of Thm1, where the divergence `2t` is the integral of the disturbance difference), then at any time `t` with `βt > w` the two branch states cannot both lie in `S_k`. Hence every tube exits `S_k` by time `w/β`. The endpoint-only test never evaluates the pair `(w, β)`; the exact-tube test does. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

The two witnesses *are* the counterexamples (Fields 3, 8). Additionally: if `D_k` is a singleton (no unmeasured disturbance) **and** within-interval rules are restricted to held-constant controls with convex safe sets, endpoint tests can be sound (the tube is then the chord between state and endpoint, contained in a convex `S_k` whenever endpoints are); this identifies exactly the two hypotheses whose absence breaks soundness: *branch multiplicity* and *non-convex or time-varying tube geometry*. Both hypotheses are generic in the programme's sampled-governance setting (corrected `08`), so the failure is structural, not pathological.

## Field 10 — Interface producer/consumer contract

- **Producer:** this record (negative soundness results for weakened Operator II tests).
- **Consumer:** Paper 1 (transformation section: may cite that endpoint/aggregate certification is *provably* insufficient, so the exact-tube clause is mandatory); the monograph composition chapter; any downstream module tempted to certify an architecture change from endpoint snapshots (e.g., A018-style ledger snapshots between regimes).
- **Type/unit map:** none needed (pure metatheorem about the Operator II data).
- **Failure condition:** the results are revoked only if the Operator II data of corrected `04` change (e.g., a solution concept in which tubes are determined by endpoints — true only for convex `S_k`, singleton `D_k`, held convexifying rules, per Field 9).

## Field 11 — Error, horizon, and safety erosion for approximations

Not an approximation result: the theorems are exact. For *conservative outer tubes* the packet's Corollary 3 (corrected `04`) remains controlling: outer tubes give inner certificates; R01 shows that *no* tube information at all gives no certificate — the two results bracket the information requirement: **endpoints alone: unsound (R01.Thm1); exact tubes: exact (corrected `04`); outer tubes: sufficient (corrected `04` Cor. 3)**.

## Field 12 — Selector and implementation regularity

None claimed or needed: the negative results hold for *arbitrary* causal rules, so they hold a fortiori for any measurable/Lipschitz/regular selector subclass. (This is the pleasant quantifier direction: refuting all rules refutes regular subfamilies.)

## Field 13 — Stochastic/hybrid/RFDE qualifications

- The witnesses are deterministic-disturbance sampled ODE systems (the weakest class), so the negative results transfer to every richer class that contains it (RFDE with zero delay, hybrid without events, stochastic degenerate laws) — containment mappings are identity embeddings, `EXACT_SPECIALIZATION`.
- For genuinely stochastic branches, `β` in Prop3 becomes the branch-divergence rate of the support; chance-constrained endpoint tests fail identically whenever the support has two branches — no new phenomenon.

## Field 14 — Novelty status with exact references

- Internal evidence: the packet's provisional novelty answer already assesses the exact-tube recursion as "mathematically standard" (`control/03` §2A item 4) and its acceptance criterion for T1 explicitly demands "a theorem proving false positives of endpoint-only/aggregate transformation tests" (`11_OPEN_THEOREM_DOCKET.md` T1) — i.e., the packet itself flags these negative results as the missing content; this record supplies them.
- The divergence argument (Prop3) is elementary; the *packaging* (soundness degeneracy of endpoint-only robust predecessor recursions) is, to the packet's internal knowledge, new, but **external literature verification against robust reachability / hybrid-safety verification literature is outstanding** (packet self-containment report caveat). No external bibliographic claim is made here.

## Field 15 — Publication destination

Paper 1 (architecture/transformation section — as a boxed impossibility proposition with the one-dimensional witness); Paper 2 (theorem atlas, counterexample register). Monograph: composition/transformation chapter.

## Field 16 — Remaining obligations and revocation triggers

- Obligations: external novelty check (Field 14); a two-architecture instantiated transformation example for Paper 1 (per corrected `04` §9 item 4) should carry the endpoint-false-positive example as its motivation.
- Revocation triggers: change of the Operator II data conventions (Field 10); discovery of an external theorem identical in scope (would demote novelty, not truth).

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R01",
  "target": "T1",
  "depends_on": ["corrected_theorems/04_operator_II_transformation_candidate.md (exact-tube predecessor, data conventions)"],
  "unblocks": ["Paper 1 transformation discipline", "R09.M3 (aggregate witness reuse)", "R03.Thm3 (aggregate margin counterexample reuses R01.Thm2 system)"],
  "status": {"R01.Thm1": "proved", "R01.Thm2": "proved", "R01.Prop3": "proved"},
  "mapping_type": "COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "internal-new; external check outstanding"
}
```
