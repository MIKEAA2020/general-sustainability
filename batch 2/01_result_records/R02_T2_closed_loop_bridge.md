# Result Record R02 — Docket T2: The Observation–Assessment–Prescription–Implementation Closed-Loop Bridge

## Field 1 — Result ID and target docket item

`R02` (R02.Thm1 closed-loop robust institutional viability; R02.Lem2 conservative-filter soundness; R02.Prop3 conservative incompleteness; R02.Prop4 common-action necessity; R02.Cor5 measured-disturbance variant; R02.Cor6 eroded closed-loop safety). Target: **T2** ("prove the observation → assessment → prescription → implementation bridge").

## Field 2 — Verdict

**Repairable → proved** (this record, at the sampled, exact/conservative-filter, finite-horizon level). The five distinctions demanded by the docket — measured vs. hidden disturbance, exact vs. conservative filter, prescribed vs. realized action, latency and held commands, all-branches vs. existential implementation — are each enforced by a typed hypothesis or quantifier of Thm1, and the acceptance criterion ("one closed-loop theorem with exact quantifiers and a common-action counterexample") is met in full.

## Field 3 — Exact statement

### Data

1. Review times `0 = t_0 < t_1 < … < t_N = T`; interval `I_k = [t_k, t_{k+1}]`.
2. **Physical layer:** closed state space `X ⊆ ℝ^n`, closed safe set `K ⊆ X`; plant `f: X × U × D → ℝ^n` with `U, D` compact, `f` Lipschitz in `(x,u)` uniformly in `d`, linear growth. For every held `u ∈ U` and measurable `d: I_k → D` the initial-value problem `ẋ = f(x,u,d(t))` has a unique forward-complete solution (denoted `φ_{u,d}`).
3. **Observation layer:** deterministic set-valued observation map `O: X → 𝒴` (closed values; the review-time observation is `Y_k = O(x(t_k))`).
4. **Assessment layer:** information states are pairs `(C, c)` with `C ⊆ X` closed and `c ∈ U` (the deployed/held command). The *conservative update* of a compatible set under a realized-action **set** `Ũ ⊆ U` is
   `Φ(C, Ũ) := {x' ∈ X : ∃x ∈ C, ∃u ∈ Ũ, ∃d ∈ 𝒟: x' = φ_{u,d}(x)(t_{k+1})}`,
   and the post-observation conservative state is `Φ(C, Ũ) ∩ O^{-1}(Y')`.
5. **Prescription layer:** compact command set `U^cmd`; policies map information states to commands.
6. **Implementation layer:** declared non-strategic correspondences (declared independently of the policy class, per schema-audit item CIRC-3): `𝖨: U^cmd × U × 𝒦(X) →` nonempty compact subsets of `U` (realized actions), and `𝖣𝖾𝖯: U^cmd × U →` nonempty compact subsets of `U` (deployed command at the next review; `{u^cmd}` = no latency, `{c}` = one-step full latency, mixtures allowed).
7. **Certificate family:** `𝒱 ⊆ {(C,c) : C ⊆ K closed nonempty, c ∈ U}`, **downward closed** in `C` (`(C,c) ∈ 𝒱`, `∅ ≠ C' ⊆ C` closed ⟹ `(C',c) ∈ 𝒱`).
8. **True compatible sets:** `B_0` declared prior with `B_0 ⊆ C_0`; `B_{k+1} = Φ(B_k, {u^real_k}) ∩ O^{-1}(Y_{k+1})` along the true branch.

### Regulation condition (REG)

`(C,c) ∈ 𝒱` satisfies (REG) if there exists `u^cmd ∈ U^cmd` such that, writing `Ũ := 𝖨(u^cmd, c, C)`:

- **(i) tube clause:** for every `u^real ∈ Ũ`, every `x ∈ C`, every `d ∈ 𝒟`: `φ_{u^real,d}(x)(t) ∈ K` for all `t ∈ I_k`;
- **(ii) successor clause:** for every `c' ∈ 𝖣𝖾𝖯(u^cmd, c)` and every observation value `Y'` with `Φ(C, Ũ) ∩ O^{-1}(Y') ≠ ∅`:
  `(Φ(C, Ũ) ∩ O^{-1}(Y'), c') ∈ 𝒱`.

### R02.Thm1 (closed-loop robust institutional viability)

*If `(C_0, c_0) ∈ 𝒱`, `B_0 ⊆ C_0`, and (REG) holds at every `(C,c) ∈ 𝒱`, then there is a causal, observation-history-based prescription policy `π` such that for every true initial state `x_0 ∈ B_0`, every observation realization, every implementation branch `u^real_k ∈ 𝖨(π_k, c_k, C_k)`, every deployment branch `c_{k+1} ∈ 𝖣𝖾𝖯(π_k, c_k)`, and every disturbance realization `d_k ∈ 𝒟` on each interval, the closed-loop trajectory exists, is unique on each interval, and satisfies*

```
x(t) ∈ K   for all t ∈ [0, T].
```

*Moreover the institution's own information state `(C_k, c_k)` remains in `𝒱` and satisfies `B_k ⊆ C_k` for all `k`, and `π` is computable from `(C_k, c_k)` alone.*

### R02.Lem2 (conservative soundness)

*For any inclusion-monotone conservative update (in particular `Φ` above, in both arguments), `B_k ⊆ C_k` for all `k` along every branch — conservative assessment never understates compatibility.*

### R02.Prop3 (conservative incompleteness)

*There exist a plant, safe set, observation map, prior, and two admissible filters — one exact, one conservative (coarser observation processing) — with the same data, such that the exact filter satisfies the hypotheses of Thm1 while the conservative one violates (REG) through a common-action obstruction. Conservative assessment is therefore sound but incomplete: it can reject safe systems, never certify unsafe ones.*

### R02.Prop4 (common-action necessity)

*If `(C,c)` is reachable and contains a state on `∂K`, no informative observation arrives before the next prescription, and*

```
⋂_{x ∈ C} {u ∈ U : every branch from x under u stays in K on I_k} = ∅,
```

*then no observation-based policy is robustly safe from `(C,c)`: `(C,c)` lies in no certificate family satisfying (REG).*

### R02.Cor5 (measured-disturbance variant)

*If the disturbance factors as `d = (d^m, d^h)` with the measured component `d^m(t_k)` revealed before the `k`-th prescription, then (REG) may be weakened: the witness command may depend on the revealed value, and clauses (i)–(ii) quantify over `d^h` only, conditionally on the revealed `d^m`. The conclusion of Thm1 holds conditionally on each realized measured sequence.*

### R02.Cor6 (eroded closed-loop safety)

*If, additionally, the erosion-lemma hypotheses of corrected `02` Lemma 2 hold for `K` (two-sided tubular radius `ρ`, `C^{1,1}` signed distance, normal correspondence) and the closed-loop velocity envelope has Lipschitz gain `L_G` and boundary margin `α`, then the tube clause (i) may be verified on the eroded set `K_{−r}` in place of `K` provided*

```
L_G r + Δ_ε ≤ α,   0 < r < ρ,   K_{−r} ≠ ∅,
```

*with `Δ_ε = Cε + μ` the combined implementation/observation/model error budget (`C = L_u(L_κ a_o + a_u)` per corrected `02`; `μ` the plant-model error). The conclusion (true-state safety in `K`) then holds with that budget.*

## Field 4 — State and phase space

Extended sampled phase space per `TCS-1.0` §2.1: physical block `x ∈ X`; held-command block `c ∈ U` (implementation/queue state); information block `C ⊆ X` (compatible-set estimate — the `b` block in the canonical typing). The decision chain instantiated is exactly `TCS-1.0` §3: physical state → `O` → observation → conservative filter `Φ` → information state → `π` → prescription → `𝖨/𝖣𝖾𝖯` → realized action and next deployed command → plant. Model class: sampled ODE with held actions (`sampled_hybrid` without interior events, per the corrected `08` architecture).

## Field 5 — Quantifier order and information pattern

The theorem's conclusion quantifier chain:

```
∃π (causal, observation-history-based)
 ∀x_0 ∈ B_0  ∀observations  ∀u^real branches  ∀deployment branches  ∀d ∈ 𝒟:
   trajectory exists uniquely and stays in K on [0,T].
```

The prescription precedes the realization of `u^real` and `d` on each interval (`π_k` is a function of `(C_k, c_k)`, i.e. of history up to `t_k`); the realized action is chosen by the *institutional correspondence* (all-branches semantics: `∀u^real ∈ 𝖨`), not by the policy — the master prompt's rule that one causal policy must be distinguished from disturbance-observing controls is enforced structurally: the policy cannot see `d` (except the measured component in Cor5, which is declared information, not control of the quantifier order) and cannot see `u^real` before prescribing.

## Field 6 — Assumptions, including existence/completeness

Existence/uniqueness/forward completeness: hypothesis 2 (Lipschitz + linear growth + compact `U,D`). Nonempty `𝖨`, `𝖣𝖾𝖯` values (hypothesis 6) guarantee every implementation/deployment branch is well-defined. Nonemptiness of the conservative sets along the true branch is proved, not assumed (Step 3 of the proof). The certificate family's nonemptiness is the load-bearing hypothesis: (REG) at every `(C,c) ∈ 𝒱` is the "assessment succeeds" assumption — Thm1 is deliberately conditional in the same sense as the packet's exact-filter theorems (corrected `08`: "assumes, rather than derives, exact compatible-state sets"), with the conservative variant made explicit so that the condition is verifiable with outer approximations.

## Field 7 — Mapping type

`EXACT_SPECIALIZATION` of the `TCS-1.0` execution chain (§3) to the sampled class, plus `TRANSFORMATION`-free composition: no reduction between model classes is claimed. Prop3 is `COUNTEREXAMPLE_OR_LIMIT` for filter-exactness claims.

## Field 8 — Self-contained proof

### Proof of R02.Thm1

Define the closed loop inductively. Base: `(C_0, c_0) ∈ 𝒱` (hypothesis). Step, given `(C_k, c_k) ∈ 𝒱` and the true state `x(t_k) ∈ B_k`:

**Choice of prescription.** Let `π_k := u^cmd` be any witness of (REG) at `(C_k, c_k)`. This is a function of `(C_k, c_k)` only, hence causal in the observation/command history (see causality note below).

**Realization.** The implementation selects `u^real_k ∈ Ũ_k := 𝖨(π_k, c_k, C_k)`; deployment selects `c_{k+1} ∈ 𝖣𝖾𝖯(π_k, c_k)`. Both are arbitrary within their declared correspondences (all-branches).

**Safety on the interval.** The true state `x(t_k) ∈ B_k ⊆ C_k` (induction; base `B_0 ⊆ C_0`). Clause (REG)(i) at `(C_k, c_k)` applies to every `x ∈ C_k`, in particular to `x(t_k)`, with the realized `u^real_k ∈ Ũ_k` and every `d ∈ 𝒟`. By hypothesis 2 the solution exists and is unique on `I_k`, and

```
x(t) ∈ K   ∀t ∈ I_k.                                   (†)
```

**Successor certificate.** The institution computes (from its own data `C_k, π_k, c_k` — no observation of `u^real` needed, since `Ũ_k` is determined by the correspondence):

```
C_{k+1} := Φ(C_k, Ũ_k) ∩ O^{-1}(Y_{k+1}),   Y_{k+1} = O(x(t_{k+1})).
```

`C_{k+1} ≠ ∅`: the true endpoint `x(t_{k+1})` is reachable from `x(t_k) ∈ C_k` under the realized `u^real_k ∈ Ũ_k` and the realized disturbance, hence `x(t_{k+1}) ∈ Φ(C_k, Ũ_k)`; and `x(t_{k+1}) ∈ O^{-1}(Y_{k+1})` by definition of `Y_{k+1}`. So `Y_{k+1}` is among the observation values with nonempty intersection in clause (REG)(ii), and therefore

```
(C_{k+1}, c_{k+1}) ∈ 𝒱.                                 (‡)
```

This closes the induction on the certificate: `(C_k, c_k) ∈ 𝒱` for all `k ∈ {0,…,N}` (with `c_{k+1}` determined at each step).

**Conservative soundness (Lem2, embedded).** Claim `B_k ⊆ C_k` for all `k`. Base holds. Inductive step: `Φ` is monotone in the set argument (a union over a subset is a subset of the union over the superset) and in the action-set argument, hence

```
B_{k+1} = Φ(B_k, {u^real_k}) ∩ O^{-1}(Y_{k+1})
        ⊆ Φ(C_k, {u^real_k}) ∩ O^{-1}(Y_{k+1})
        ⊆ Φ(C_k, Ũ_k) ∩ O^{-1}(Y_{k+1}) = C_{k+1}.
```

**Conclusion.** Chaining (†) over `k = 0,…,N−1` gives `x(t) ∈ K` for all `t ∈ [0,T]`, for every branch of observations, implementation, deployment, and disturbance, and every `x_0 ∈ B_0`. Causality note: `C_{k+1}` is computed from `C_k`, `π_k`, `c_k` (institution-internal) and the observation `Y_{k+1}` (received at `t_{k+1}`); by induction `C_k` is a function of `Y_1,…,Y_k` and the initial data, so `π_k` is a function of the observation history — observation-based and causal. ∎ (Thm1 and Lem2)

### Proof of R02.Prop3 (incompleteness witness)

**Plant.** `X = ℝ × {±1}` with coordinates `(z, θ)`, `θ` a hidden mode; held commands `u ∈ {−1, +1}` on unit intervals `I_k = [k, k+1)`; no exogenous disturbance; dynamics

```
ż = θu − 1.
```

Safe set `K = {(z,θ) : z ≥ 0}`. Read the two branches: for `θ = +1`, `u = +1` *holds* (`ż = 0`) and `u = −1` *crashes* (`ż = −2`); for `θ = −1` the roles swap. A command safe for one mode crashes the other at rate 2; the mode-matched command always holds. Prior `C_0 = {(3,+1), (3,−1)}`.

**Observation maps.** `O^{ex}_k(z,θ) = (z,θ)` for `k ≥ 1` (the exact processor receives the mode from `t_1` on; at `t_0` no mode information); `O^{co}_k(z,θ) = z` for all `k` (the conservative processor trusts only `z` — a declared coarsening, i.e. an outer processor that discards the mode channel).

**Exact filter: viable forever.** On `[0,1]` the exact institution also faces the pair; the common command `u = +1` is safe on `[0,1]` for both branches (the `θ=−1` branch falls from 3 to 1, staying in `K`). At `t_1` the mode is revealed, the compatible set becomes a singleton `{(z,θ)}`, and the matched hold command keeps `z` constant forever: clause (REG) holds on the certificate family consisting of the initial pair and the singletons, and Thm1 certifies robust institutional viability on every horizon.

**Conservative filter: genuinely nonviable.** Under any `z`-only policy, let `(z⁺, z⁻)` be the two mode-branch positions. Whatever command is held, exactly one branch holds and the other falls at rate 2, so

```
z⁺(k+1) + z⁻(k+1) = z⁺(k) + z⁻(k) − 2   for every admissible command,
```

hence `z⁺ + z⁻ = 6 − 2k` after `k` intervals. Keeping both branches in `K` forever requires `z⁺ + z⁻ ≥ 0` forever — impossible: **every** `z`-only policy exits `K` by `t = 3`. Moreover the obstruction is locally visible: at `t_2` the conservative compatible set (under the forced safe play of the first two intervals) is `C = {(1,+1), (1,−1)}`, and each member has exactly one safe command on `[2,3]` (the mismatched command exits within time `1/2 < 1`), the two commands being opposite: the common safe-command intersection is empty, so (REG) fails at this reachable state — the Prop4 obstruction, reached by the conservative dynamics. The conservative bridge therefore correctly refuses certification, and the refusal is not an artifact: the conservative information pattern is truly nonviable.

**Conclusion.** Same plant, same `K`, same prior: the exact filter satisfies the bridge's hypotheses and the closed loop is viable; the sound conservative filter violates (REG) at a reachable state and the conservative closed loop is nonviable. Conservative assessment is sound (it never certifies an unsafe system — Lem2) but incomplete (it rejects — here, correctly at its own information level, but *needlessly at the physical level* — a system the exact processor governs safely): filter exactness is a semantic property of the declared assessment layer, not a refinement of the same judgment. (The witness transplants the packet's hidden-mode conflict, `sources/A001_topdown_source.txt` line 558 / Example 4.1, and Theorem 4.2's observation-empties-kernel phenomenon, into the closed-loop setting with a forced decay that makes the distinction a *viability* difference, not merely a certificate difference.) ∎

### Proof of R02.Prop4 (necessity)

Suppose `(C,c)` is reachable, contains a boundary state, no informative observation precedes the next prescription, and the per-state safe-command intersection is empty. Any observation-based policy must select one command `u ∈ U` from the information available at `(C,c)`. Robust safety on `I_k` requires, in particular, safety of every compatible state `x ∈ C` under that `u`. For each `x ∈ C` the set of commands safe at `x` is exactly the corresponding member of the intersection; the intersection being empty, no `u` is safe for all `x ∈ C` simultaneously. Hence every candidate first command fails, so no policy is robustly safe from `(C,c)`, and `(C,c)` can belong to no certificate family on which (REG) holds (REG would demand a witness command). This is the one-step argument of corrected `06` §3, transplanted verbatim to the closed-loop setting. ∎

### Proof of R02.Cor5

Run the induction of Thm1 conditionally on the realized measured sequence `(d^m(t_k))_k`. The witness at `(C,c)` may be chosen as a function `u^cmd(d^m)` of the revealed value; clauses (i)–(ii) quantify over hidden components only, with the measured values fixed. All steps of the proof are unchanged, relativized to the fixed measured sequence; the conclusion holds for each such sequence separately, hence for all. ∎

### Proof of R02.Cor6

Clause (i) verified on `K_{−r}` means the closed-loop velocity field at points of `∂K_{−r}` satisfies the erosion-lemma inequality with total perturbation budget `Δ_ε` (interface-free by construction: the theorem's own realization error is the budget — observation error `a_o ε` through the command map's Lipschitz constant `L_κ`, implementation error `a_u ε`, plant-model error `μ`, converted by `C = L_u(L_κ a_o + a_u)` exactly as in corrected `02`). By corrected `02` Lemma 2 (clause-level match: identical hypotheses, identical conclusion), `K_{−r}` is strongly invariant under the closed-loop envelope, and membership `x ∈ K_{−r}` implies `x(t) ∈ K_{−r} ⊆ K` for all subsequent times. Substituting `K_{−r}` for `K` in clause (i) of (REG) therefore yields true-state safety in `K` under the stated budget condition. The feasible interval for `r` may be empty — this caveat is retained verbatim from corrected `02`. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Three boundary witnesses:

1. **Common-action necessity:** Prop4 + its instantiation inside Prop3 (and the packet's own hidden-mode example, `sources/A001_topdown_source.txt` line 558, Example 4.1): individually viable compatible states with empty common safe command — information structure, not dynamics, is the failure.
2. **Latency is not cosmetic:** with `𝖣𝖾𝖯 ≡ {c}` (full one-step latency), clause (i) must hold for the *previous* command on every interval; the certificate family indexed by `c` is what makes this checkable. In the Prop3 plant with latency one, a `θ`-safe command issued at `t_1` deploys at `t_2`, so the interval `[t_1,t_2]` runs on the *parking* command — safe only if parking was chosen with foresight: the certificate family must therefore distinguish `c`-values, which it does by construction.
3. **All-branches vs. existential:** replacing `∀u^real ∈ 𝖨` by `∃` converts the judgment into the some-branch (cherry-picking) one; the two are related by the monotonicity reversal of corrected `01` Prop 7 — enlarging `𝖨` shrinks all-branches safety (Thm1) while enlarging some-branch safety. The theorem proves the governance-relevant (all-branches) direction only.

Outside scope (no claim): measurable/continuous/Lipschitz selectors for the witness correspondence (see Field 12); stochastic observation laws; RFDE history-state filters; interior events; infinite horizon without the compactness closure of R03.Lem4.

## Field 10 — Interface producer/consumer contract

- **Producer object:** closed-loop guarantee `Thm1` + certificate condition `(REG)` + conservative-update soundness `Lem2`, with types: `(C,c)`-certificates, correspondence `𝖨/𝖣𝖾𝖯`, observation `O`, plant `f`.
- **Consumer objects:** (i) institutional-operationalization module (Wave 3/E1 of the research plan): must instantiate `𝖨` from real authority/compliance/latency records and check (REG); (ii) Paper 5 closed-loop falsification design: the certificate condition is the falsifiable object (failure of (REG) at a reachable `(C,c)` is a predicted governance breakdown); (iii) R08's typed lift maps (information-state judgments of the hierarchy become instances).
- **Type/unit map:** prescriptions `u^cmd ∈ U^cmd` and realized actions `u^real ∈ U` are distinct types joined only by `𝖨` (`TCS-1.0` §2.3); compatible sets carry physical units; no aggregation across blocks is performed.
- **Failure condition:** revocation if any hypothesis of Field 6 is withdrawn on an application (in particular: strategic `𝖨` (CIRC-3), non-conservative filter claimed as conservative, or selector regularity assumed without proof).

## Field 11 — Error, horizon, and safety erosion for approximations

Cor6 is the erosion interface: error budget `Δ_ε = Cε + μ`, erosion depth `r = cε` feasible when `(L_G c + C)ε + μ ≤ α`, `cε < ρ`, `K_{−cε} ≠ ∅`; horizon finite `T` (infinite horizon via R03.Lem4 under compactness). The conservative filter's coarseness is *not* an error budget in this sense — it is exactness loss in the assessment layer, whose consequence is incompleteness (Prop3), not erosion.

## Field 12 — Selector and implementation regularity

Thm1's policy is an arbitrary selector of the (REG)-witness correspondence (axiom-of-choice level, consistent with the packet's selector discipline: corrected `08` limitation 1, corrected `01` §"Measurable selection is not Lipschitz implementation"). Claiming measurable/continuous/computable `π` requires a selection theorem on `𝒱` — an open obligation (research plan D2). Implementation regularity enters only through the declared correspondences' compactness; `𝖨` may be nonconvex (all-branches quantifier is set-algebraic, no convexification needed for the *judgment*; convexification matters only if envelope strong-invariance tools are invoked, as in Cor6, where the relaxation-exactness caveat of corrected `03` §7 applies).

## Field 13 — Stochastic/hybrid/RFDE qualifications

- **RFDE:** the proof pattern transfers to the history-space setting of corrected `08` (sampled RFDE finite-clopen knowledge kernel) with `C` a compact history set and `Φ` the exact translated-history update, *provided* the history-class closure conditions (uniform boundedness, equi-Lipschitz, translated-history membership — corrected `08` §RFDE history closure) hold; this qualification is declared, not proved here.
- **Hybrid:** review-synchronised events fold into the successor clause (reset maps compose with `Φ`); interior/variable events are outside scope (packet's standing gap).
- **Stochastic:** chance-constrained versions need the law-support alignment guard (schema audit QF-2; corrected `01` Prop 8); no stochastic claim is made.

## Field 14 — Novelty status with exact references

- Internal: the docket T2 acceptance criteria are met; the packet's existing components (corrected `01` hierarchy; corrected `06` §2–§4; corrected `08` information-state kernel; A001 Thm 13.2 at `sources/A001_topdown_source.txt` line 1611 — which the error register lists as assumption-driven) supply the pieces, but **no packet record composes them into one closed-loop quantifier chain with the conservative/exact, latency, all-branches, and measured/hidden distinctions simultaneously**; that composition, and the sound-but-incomplete conservative-filter calculus (Lem2/Prop3), are the new content.
- External: perception/observer-based robust control and verified-controller literatures contain related compositional guarantees; **exact bibliographic matching is outstanding** (packet self-containment caveat). No external novelty claim is made.

## Field 15 — Publication destination

Paper 1 (governance architecture section: the bridge as the theory's central closed-loop theorem); Paper 2 (theorem atlas: Thm1 + Lem2 + Prop3 with full proof); Paper 5 (closed-loop empirical design: (REG) as the falsifiable certificate). Monograph: chapter on the execution chain.

## Field 16 — Remaining obligations and revocation triggers

Obligations: selector regularity (D2); RFDE/history-space instantiation with the closure conditions verified on one application; stochastic variant with support alignment; external novelty audit (F1); an instantiated institutional case (E1/E2). Revocation triggers: withdrawal of the non-strategic `𝖨` declaration (CIRC-3) — the theorem's quantifier chain would become a fixed-point claim; discovery that a conservative update is not inclusion-monotone (breaks Lem2); any application asserting (REG) without exhibiting the certificate family.

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R02",
  "target": "T2",
  "depends_on": [
    "corrected_theorems/01_operator_I_hierarchy.md (judgment quantifiers, Prop 7)",
    "corrected_theorems/06_A001_selected_operatorI_audit.md (common-action obstruction §3, delayed-information §4)",
    "corrected_theorems/08_A002_sampled_hybrid_audit.md (sampled kernel chain, selector caution)",
    "corrected_theorems/02_operator_I_strong_invariance_and_erosion.md (Lemma 2, for Cor6)"
  ],
  "unblocks": ["T8 typed hierarchy maps (R08)", "institutional operationalization (Wave E)", "Paper 5 closed-loop design", "R04 policy/information map field"],
  "status": {"R02.Thm1": "proved", "R02.Lem2": "proved", "R02.Prop3": "proved", "R02.Prop4": "proved", "R02.Cor5": "proved", "R02.Cor6": "proved (clause-level assembly)"},
  "mapping_type": "EXACT_SPECIALIZATION (of the TCS-1.0 execution chain) + COUNTEREXAMPLE_OR_LIMIT (Prop3)",
  "novelty": "internal-new composition; external check outstanding"
}
```
