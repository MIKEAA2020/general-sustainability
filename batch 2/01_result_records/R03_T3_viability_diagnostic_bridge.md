# Result Record R03 — Docket T3: The Viability–Diagnostic Bridge

## Field 1 — Result ID and target docket item

`R03` (R03.Thm1 certificate trichotomy; R03.Thm2 stock-to-rate margin failure; R03.Thm3 aggregate margins are not kernels; R03.Lem4 compactness horizon closure; R03.Cor5 combined-error erosion conversion). Target: **T3** ("determine when a diagnostic margin or finite-horizon estimate is sound for nonviability; complete for viability; an inner/outer certificate; merely descriptive").

## Field 2 — Verdict

**Repairable → proved (assembled + new witnesses).** The packet holds all positive components (adversarial exit, erosion lemma, local-horizon bracket) but no record states the bridge classification or the necessity counterexamples; this record assembles the positives with clause-level matches and supplies the new negative witnesses the docket demands ("counterexample showing why local stock-to-rate or aggregate margins are not kernels").

## Field 3 — Exact statement

**Setting.** Diagnostics are functionals `M(x)` computed from model + observation data at a state (e.g., robust finite-horizon value `V_T(x)` in the sense of A001 Definition 15.1 at `sources/A001_topdown_source.txt` lines 1796–1804; distance-type margins `dist(x, ∂K)`; stock-to-rate ratios `(S − S_min)/r`; aggregate margins `dist(P(x), ∂P(K))`).

**R03.Thm1 (certificate trichotomy).** With `RViab_T(K)` the robust viability kernel on horizon `T` and `RViab_∞(K)` its infinite-horizon limit:

1. **(Outer / sound for nonviability.)** If `M` is an *adversarial-exit certificate* — there exist `q, a, ε > 0`, a strip `𝒮_a = {0 ≤ q ≤ a}`, and the lower-game information pattern such that for every admissible control and every state in the strip an admissible nonanticipative disturbance realizes `D^+q ≤ −ε`, with existence up to exit — then `M(x) < 0` certifies `x ∉ RViab_∞(K)`, and the exit occurs within time `a/ε`. The certificate is sound for nonviability and requires no policy search.
2. **(Inner / sound for viability.)** If `M` is a *margin-with-budget certificate* — `K` satisfies the erosion-lemma hypotheses (two-sided tubular radius `ρ`, `C^{1,1}` signed distance, normal correspondence), the certified closed-loop envelope has Hausdorff-Lipschitz gain `L_G` and boundary margin `α`, and the diagnostic error budget satisfies `Δ = Δ_ε + μ` with `L_G r + Δ ≤ α`, `0 < r < ρ`, `K_{−r} ≠ ∅` — then `M(x) ≥ r` certifies `x ∈ RViab_∞(K_{−r}) ⊆ RViab_∞(K)`.
3. **(Descriptive.)** If `M` carries neither an adversarial quantifier pattern (case 1) nor a margin/budget/regularity package (case 2), then `M` implies neither nonviability nor viability: both failure directions are witnessed (Thm2: soundness failure of the safety direction for stock-to-rate margins; Thm3: kernel-hood failure for aggregate margins; and the packet's own soft-landing failure for the nonviability direction, see Field 9).

**R03.Thm2 (stock-to-rate margins are unsound without a rate-persistence band).** For the stock process `Ẋ = −e^t` with `K = {X ≥ 0}` and `S_min = 0`: the stock-to-rate diagnostic horizon from `X(0) = a` is `T_diag = a/r(0) = a`, while the true exit time is `T* = ln(1 + a)`. The ratio `T_diag/T* = a/ln(1+a) → ∞` as `a → ∞`: the overestimate is unbounded, so no constant-factor correction can restore soundness. The rate-band hypothesis of the A002 local-horizon bracket (`thm:horizon`, `sources/A002_general_theory_source.txt` line 2161; accepted conditionally in corrected `09`) is therefore not merely technical: without it, stock-to-rate margins are descriptive only.

**R03.Thm3 (aggregate margins are not kernels).** In the system of R01.Thm2 (`ẋ_1 = c+u, ẋ_2 = −(c+u)`, `c > 1`, `S = [0,1]²`, aggregate `P = x_1+x_2`), the aggregate margin `dist(P(x), ∂P(S))` is constant and positive along **every** trajectory (`P ≡ const ∈ (0,2)` for `x ∈ int S`), for all time; yet `RViab(S) = CViab(S) = ∅`. Aggregate margins are therefore not viability kernels in either direction, and no erosion of the aggregate level set restores safety (the erosion direction is orthogonal to the failing components).

**R03.Lem4 (compactness closure of the horizon limit).** For the sampled robust problem with compact state space (or a compact invariant enclosure), compact action sets, and successor maps `Succ(x,u,d)` that are Hausdorff-upper-semicontinuous in `u` uniformly in `(x,d)` with closed values: defining `R_0 = K` and `R_{n+1} = {x ∈ K : ∃u ∀d : Succ(x,u,d) ⊆ R_n}`, the family `(R_n)` is decreasing and

```
R_∞ := ⋂_n R_n = RViab_∞(K):
```

a state is robustly viable on every finite horizon if and only if it is robustly viable on the infinite horizon, and `R_∞` is the largest robustly invariant subset of `K`. Consequently the hierarchy's non-implication 8 (corrected `01`: "Finite-horizon viability does not imply infinite-horizon viability without a closure/compactness argument") closes exactly at these hypotheses: without compactness/upper semicontinuity the implication fails; with them, viability at *all* finite horizons is equivalent to infinite-horizon viability.

**R03.Cor5 (combined-error erosion conversion).** If a margin certificate is computed with observation error `≤ a_o ε`, implementation error `≤ a_u ε`, and plant-model error `≤ μ`, then under the erosion-lemma hypotheses the certified inner kernel is `K_{−r}` with

```
(L_G c + C)ε + μ ≤ α,   C = L_u(L_κ a_o + a_u),   r = cε < ρ,
```

exactly the error conversion of corrected `02`; the feasible interval for `c` may be empty, in which case the diagnostic certifies nothing.

## Field 4 — State and phase space

Thm2: scalar ODE, `X = ℝ_{≥0}`, nonautonomous rate (declared model class: ODE with known time-varying rate — the diagnostic's information). Thm3: `ℝ²` with noncompensatory box constraint and aggregate projection (as R01.Thm2). Lem4: sampled system, compact `X`, `U`, `D`, successor correspondence (the packet's canonical sampled setting, corrected `08`).

## Field 5 — Quantifier order and information pattern

Thm1(1): `∀π ∃` nonanticipative disturbance `: exit by a/ε` (adversarial lower game; corrected `06` §7's repaired quantifiers). Thm1(2): `∃κ ∀d ∀φ : stay` (all-solutions strong invariance; corrected `02` Theorem 1 pattern). Thm2/Thm3: no quantifier pattern — that is the point: the diagnostics carry none, and the theorems show the consequences. Lem4: `∃u ∀d` per step, `∃π ∀d ∀φ` globally (robust kernel).

## Field 6 — Assumptions, including existence/completeness

Thm1(1): measurable/nonanticipative disturbance selection and existence up to exit (as in corrected `06` §7). Thm1(2)/Cor5: erosion-lemma regularity (corrected `02` Lemma 2 hypotheses, including the normal correspondence and the exclusion of arbitrary closed sets — the packet's `K = ⋃_j [2j, 2j+1]` counterexample for uniform erosion remains controlling). Lem4: compactness + Hausdorff-usc successor maps (explicitly the hypotheses the packet's sampled kernel theorems already carry: corrected `08` assumes Hausdorff continuity, which is stronger than the upper semicontinuity used here). Thm2/Thm3: Lipschitz dynamics, unique forward-complete solutions.

## Field 7 — Mapping type

Thm1: `EXACT_SPECIALIZATION` of the classification question onto the packet's two existing certificate types + `COUNTEREXAMPLE_OR_LIMIT` for the residual class. Thm2: `COUNTEREXAMPLE_OR_LIMIT` (necessity witness for `thm:horizon`'s hypothesis). Thm3: `COUNTEREXAMPLE_OR_LIMIT` (reuses R01.Thm2's system — internal dependency edge). Lem4: `EXACT_SPECIALIZATION` of classical viability-limit machinery to the packet's sampled class, with proof supplied for self-containment. Cor5: clause-level theorem match to corrected `02`.

## Field 8 — Self-contained proof

### Proof of R03.Thm1

**(1)** is the corrected adversarial-exit theorem of A001 Theorem 5.2 (repaired quantifiers and conclusion; corrected `06` §7 accepts it): for every control policy there exists a nonanticipative disturbance strategy driving `q` across 0 within `a/ε`; hence `x ∉ RViab_T(K)` for `T ≥ a/ε`, and a fortiori `x ∉ RViab_∞(K)`. Clause-level match; no new mathematics.

**(2)** is corrected `02` Lemma 2 with its error conversion: the margin `α` at `∂K`, the Lipschitz budget `L_G r`, and the total perturbation `Δ` give strong invariance of `K_{−r}` under the *certified* closed-loop envelope; membership `x ∈ K_{−r}` therefore implies eternal stay in `K_{−r} ⊆ K` under all declared disturbances and all solutions (all-solutions semantics via the envelope inclusion, corrected `02` Theorem 1). Clause-level match.

**(3)** is established by the two witnesses below plus the packet's soft-landing witness: a diagnostic with neither the adversarial pattern nor the margin/budget package can point in either direction and be wrong — soundness fails in the safety direction (Thm2: `T_diag` overestimates exit time unboundedly; Thm3: aggregate margin positive forever while the kernel is empty) and completeness fails in the nonviability direction (Field 9: soft landing never exits while `T_diag` is finite). ∎

### Proof of R03.Thm2

Rate `r(t) = e^t`; from `X(0) = a > 0`: `X(t) = a − (e^t − 1)`, so `X` reaches 0 at `T* = ln(1+a)` exactly. The diagnostic at `t = 0` uses the current rate `r(0) = 1`, giving `T_diag = X(0)/r(0) = a`. Ratio `a/ln(1+a)`: at `a = 10` it is `10/ln 11 ≈ 4.17`; as `a → ∞` it diverges. For every claimed soundness factor `F` there is an initial stock with `T_diag > F·T*`: the diagnostic asserts safety for a horizon that exceeds the true horizon by more than any fixed factor. Since the A002 local-horizon bracket's hypothesis ("rate remains within the declared relative band on an interval already long enough to force crossing" — corrected `09`, adjudication row "Local-horizon bracket") is violated here by construction (`r` leaves every band `[r(0)(1−δ), r(0)(1+δ)]` exponentially fast), the witness proves that hypothesis necessary. ∎

### Proof of R03.Thm3

Immediate from R01.Thm2 (proved there): `P(x(t)) ≡ P(x(0)) ∈ P(S)` for every trajectory, so the aggregate margin `dist(P(x(t)), ∂P(S))` is a positive constant along every branch for all time — the aggregate diagnostic can never register any deterioration. Meanwhile `RViab(S) = CViab(S) = ∅` (R01.Thm2 Step 2: both components are driven out within time `1/(c−1)` under every control). Erosion of aggregate level sets `P^{-1}([δ, 2−δ])` intersects `S` in strict subsets but every such subset still has empty kernel, since the destruction mechanism (fibre-internal transfer at rate `≥ c−1 > 0`) is invisible to `P` and unaffected by `δ`. ∎

### Proof of R03.Lem4

Write `Pre(W) := {x ∈ K : ∃u ∀d : Succ(x,u,d) ⊆ W}` so `R_{n+1} = R_n ∩ Pre(R_n) = Pre(R_n)` (`Pre(W) ⊆ K` by construction and `R_n ⊆ K`).

**Monotonicity.** `R_1 = Pre(K) ⊆ K = R_0`; if `R_n ⊆ R_{n−1}` then `Pre(R_n) ⊆ Pre(R_{n−1})`, so `R_{n+1} ⊆ R_n`: decreasing. Each `R_n` is compact (closed subsets of the compact enclosure; closedness of `Pre` follows from closed values of `Succ` and compactness of `U, D` — standard, and the same closedness the packet's sampled kernel theorem uses).

**Set algebra (no continuity needed).** For any decreasing family `W_n ↓ W_∞` with closed values:

```
Pre(W_∞) = ⋂_n Pre(W_n).
```

Indeed, `x ∈ Pre(W_∞)` ⟺ `Succ(x,u,d) ⊆ W_∞ ⊆ W_n` for some `u` and all `d` ⟺ `x ∈ ⋂_n Pre(W_n)`; conversely `x ∈ ⋂_n Pre(W_n)` gives, for some fixed `u` — careful: the witness `u` may depend on `n`; the fix is the next step.

**Fixed point.** Claim `R_∞ = ⋂_n R_n` satisfies `R_∞ = Pre(R_∞)`; in particular `R_∞` is robustly invariant (witness command at every point), and it is the largest such subset of `K` (any robustly invariant `W ⊆ K` satisfies `W ⊆ Pre(W) ⊆ … ⊆ R_n` for all `n`).

*Inclusion `Pre(R_∞) ⊆ R_∞`:* `Pre(R_∞) ⊆ Pre(R_n) = R_{n+1} ⊆ R_n` for every `n`; intersect.

*Inclusion `R_∞ ⊆ Pre(R_∞)`:* let `x ∈ R_∞`. For each `n`, `x ∈ R_{n+1} = Pre(R_n)`, so there is `u_n ∈ U` with `Succ(x,u_n,d) ⊆ R_n` for all `d`. By compactness of `U`, a subsequence `u_{n_j} → u* ∈ U`. Fix `m`; for `n_j ≥ m`, `Succ(x, u_{n_j}, d) ⊆ R_{n_j} ⊆ R_m`. By Hausdorff-upper-semicontinuity of `Succ(x,·,d)` at `u*` and closedness of `R_m`: `Succ(x, u*, d) ⊆ R_m`. This holds for every `m`, hence `Succ(x,u*,d) ⊆ ⋂_m R_m = R_∞` for all `d`, i.e. `x ∈ Pre(R_∞)`. 

**Equivalence with infinite-horizon viability.** `R_∞` robustly invariant and `⊆ K` ⟹ every `x ∈ R_∞` is robustly viable forever (recursively choose the witness command; concatenation is the policy — an arbitrary selector, Field 12). Conversely, if `x` is robustly viable on every finite horizon `n`, then by backward induction `x ∈ R_n` for every `n` (the standard finite-horizon characterization the packet's sampled kernel theorem supplies; corrected `08`), so `x ∈ R_∞`. Hence `R_∞ = RViab_∞(K)`, and finite-horizon viability at *all* horizons is equivalent to infinite-horizon viability. ∎

### Proof of R03.Cor5

Clause-level assembly of corrected `02` (Lemma 2 + error conversion): the three error sources enter the perturbation budget of the closed-loop envelope as `Δ_ε = Cε` with `C = L_u(L_κ a_o + a_u)` plus the model error `μ` (added to the budget since the envelope inclusion `Ḡ_ε ⊆ G + ΔB` carries it linearly); the erosion condition `L_G r + Δ_ε + μ ≤ α` is then exactly the lemma's hypothesis, and the conclusion is strong invariance of `K_{−r}`, `r = cε`. Empty-feasible-interval caveat retained. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

- **Thm2's reverse direction (completeness failure):** the soft-landing process `Ẋ = −cX²` never reaches 0 (`X(t) = X(0)/(1+cX(0)t) → 0` only asymptotically), so the true horizon is `∞` while the stock-to-rate diagnostic gives the finite value `X(0)/(cX(0)²) = 1/(cX(0))`: margins cannot certify safety either — both directions of the "descriptive" verdict are witnessed.
- **Lem4's necessity:** dropping compactness, the standard escape-to-infinity failure applies (the packet's own remark on A001 Theorem 14.2: "Without dissipativity, mass can escape to infinity and the nested-empty-intersection argument fails" — the same mechanism blocks the horizon limit without confinement); dropping Hausdorff-usc, the witness subsequence argument fails and `R_∞` can fail to be a fixed point (predecessor chains can shrink strictly in the limit — the outer-semicontinuity pathology the packet records in A002's Proposition on OSC insufficiency, corrected `08`).
- **Erosion outside regular sets:** the packet's `K = ⋃_{j≥1}[2j,2j+1]` counterexample (corrected `02`) remains controlling for Thm1(2): without tubular regularity, margins do not convert to invariant erosions at any constant factor.

## Field 10 — Interface producer/consumer contract

- **Producer:** the trichotomy classification + Lem4 + Cor5, typed over (diagnostic functional, certificate pattern, error budget, horizon).
- **Consumers:** Paper 5 falsification design (a proposed empirical diagnostic must declare which trichotomy class it is in; only class (1) may be cited as a falsifier of viability claims, only class (2) as a safety certificate); Paper 3 componentwise diagnostics (Thm3 prohibits aggregate-level depletion claims — ties to the componentwise deficit design `Λ = [D]_+` of corrected `05`); R04's admission certificate (diagnostic field must instantiate Cor5's budget).
- **Failure condition:** revocation if the adversarial-exit theorem or erosion lemma hypotheses are weakened on an application; any aggregate diagnostic used as a kernel claim violates Thm3 and must be rejected at review.

## Field 11 — Error, horizon, and safety erosion for approximations

Cor5 is the complete statement: error `(a_o, a_u, μ) → Δ_ε = Cε + μ`, horizon `∞` (via Lem4 under compactness; finite otherwise), erosion `r = cε` with `(L_G c + C)ε + μ ≤ α`, `cε < ρ`, `K_{−cε} ≠ ∅`; feasible interval possibly empty. Thm2 makes precise *why* rate diagnostics have no constant conversion factor: the error is state/path-dependent and unbounded.

## Field 12 — Selector and implementation regularity

Lem4's policy is an arbitrary selector of the witness correspondence (consistent with the packet's selector discipline); measurable/continuous selector claims need a selection theorem (open obligation D2, shared with R02). Thm1(2) requires the *implementable* feedback's regularity exactly as corrected `02` states (Lipschitz `κ` or re-checked Filippov envelope) — a measurable selector alone does not establish the erosion conversion.

## Field 13 — Stochastic/hybrid/RFDE qualifications

Thm1(1): the adversarial pattern is the deterministic lower game; a stochastic analogue requires the law-support alignment (QF-2) and becomes a chance-nonviability statement — not claimed. Lem4: sampled class only; the RFDE analogue needs the history-space compactness (equi-Lipschitz history classes, corrected `08`) — declared, not proved. Hybrid: interior events void the predecessor algebra (event-time branching); review-synchronised events compose as in corrected `08`.

## Field 14 — Novelty status with exact references

Internal: Thm1's trichotomy is the missing classification the docket demands; Thm2 and Thm3 are new witnesses; Lem4 supplies the compactness closure that corrected `01`'s non-implication 8 explicitly leaves open. External: the finite-to-infinite horizon closure is classical viability/dynamic-programming machinery (the packet itself cites the viability literature for kernel limits, A002 line 69: `aubin1991`, `saintpierre1994`); the *trichotomy packaging* and the unbounded-ratio stock-to-rate witness are, to internal knowledge, new — **external literature check outstanding**, no bibliographic novelty claim made.

## Field 15 — Publication destination

Paper 2 (theorem atlas: Lem4 + Thm1 as the diagnostic-bridge section); Paper 5 (core methodological content: the trichotomy as the falsification-design grammar, Thm2/Thm3 as boxed counterexamples); Paper 3 (Thm3's prohibition on aggregate depletion claims, cited from the componentwise diagnostics section).

## Field 16 — Remaining obligations and revocation triggers

Obligations: instantiate Cor5's constants on the selected empirical case (E1); external novelty check; verify Hausdorff-usc of the application successor maps (Lem4's hypothesis — the packet's theorems assume the stronger Hausdorff continuity, so applications verified under corrected `08` inherit it). Revocation triggers: any use of a stock-to-rate or aggregate margin as a kernel/certificate claim (violates Thm2/Thm3 — reviewer-enforceable); withdrawal of compactness in an infinite-horizon application of Lem4.

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R03",
  "target": "T3",
  "depends_on": [
    "corrected_theorems/02_operator_I_strong_invariance_and_erosion.md (Theorem 1, Lemma 2, error conversion)",
    "corrected_theorems/06_A001_selected_operatorI_audit.md (§7 adversarial exit)",
    "corrected_theorems/09_A002_reduction_diagnostic_audit.md (local-horizon bracket scope)",
    "corrected_theorems/08_A002_sampled_hybrid_audit.md (sampled kernel machinery)",
    "R01 (Thm2 system reused in R03.Thm3)"
  ],
  "unblocks": ["Paper 5 falsification design", "R04 diagnostic field", "R09 Part M.4", "empirical case E1"],
  "status": {"R03.Thm1": "proved (assembly + new witnesses)", "R03.Thm2": "proved", "R03.Thm3": "proved", "R03.Lem4": "proved (classical machinery, self-contained proof)", "R03.Cor5": "proved (clause-level)"},
  "mapping_type": "EXACT_SPECIALIZATION + COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "trichotomy packaging internal-new; horizon closure classical; external check outstanding"
}
```
