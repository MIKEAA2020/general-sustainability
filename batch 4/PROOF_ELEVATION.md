# PROOF_ELEVATION — Consolidated Repair of the Reconstructed Theorems

**Provenance.** This document supersedes the `batch 4/PROOF_ELEVATION.md` produced on 2026-08-25 and lost with the sandbox reset before it was pushed (worklog Task 23 preserves its blueprint). It is **recreated and strengthened**: it now contains (i) a joint assessment of the three independent repair attempts — the lost original (reconstructed from the worklog blueprint, "M" below), `batch 4/agent 1 attempt/` ("A1"), and `batch 4/agent 2 attempt/` (also promoted to the `batch 4/` root, "A2") — and (ii) the consolidated repair: for each of `PROOF_REAUDIT.md`'s 27 findings, the strongest *correct* treatment across the three attempts, with the defects of the weaker attempts corrected before implementation.

**Standing rule (unchanged from Task 23).** Do not regress a claim unless it is false; demote to conjecture only if plausible and genuinely out of reach; punish inflation as well as softening. Every consolidated move below is a demotion, a scope-lock, a sign/scope correction, or a replacement of a false sentence by a true one of equal or greater force. **Zero claims softened.** The one demotion-to-conjecture in M's blueprint (E3.C6.3 (⟹) under prior coarseness) is **eliminated** by the joint process: A1 and A2 independently produced a *provable exact characterisation* that replaces the failed iff, so no conjecture is needed anywhere in this document.

**Verification.** The two mathematical disputes between A1 and A2 were adjudicated numerically before consolidation (script preserved at `reaudit/verify_joint_disputes.py`; results reproduced inline in §I.3). All 13 A2 verification suites (444 assertions) and the A1 developments are on file in `batch 4/`.

---

# Part I — Joint assessment of the three attempts

## I.1 What each attempt is

| | M (lost original, worklog Task 23) | A1 (`agent 1 attempt/`) | A2 (`agent 2 attempt/` = `batch 4/` root) |
|---|---|---|---|
| Shape | 891-line single document; per-finding complete proofs | 6 long-form dossiers (one proof per file for the four Class-1 findings + E2.B2(a)) + one 1330-line file covering all remaining findings | 15 short-form REPAIRED dossiers + 13 verification suites (444 assertions, all passing at production time) + 2 drop-in replacement sections |
| Method | re-read the source statements; matched notation; proof-first | "one proof this turn" per file; deepest conceptual analysis of *why* each proof fails | verification-first: every claim, counterexample, and repair is asserted numerically |
| Distinctive strengths | Form A / Form B framing of B1 (resolves C4); the L_B/L_G separation; strongest-negative reading of E4.Thm2 | Found errors **the audit itself made** (B10 semicontinuity; B9 reverse-inclusion refutation; the E4 witness-gap); the co-Lipschitz companion (E4.Lem1(E)); the uniform-exhaustion hypothesis for B7(1); the E3.C2 Farkas-variant correction | Sharp quantitative forms everywhere (moduli, tight radii, reach formula); **two new findings no other attempt caught** (B6 part (2) sign error; the E4 r≡0 vacuity D3); the two-depth B1 theorem; dynamical closure for A3.Thm1; the reparametrized A3 metric |
| Defects found by the joint process | E3.C6.3 (⟸) was graded "PROVEN" — too generous: the landing gap (`x(t_d) ∈ Viab_full`) was missed; the conjecture-demotion was unnecessary | No per-finding numerical verification; B6 part (2) left untreated; B1 formulated only at the two special depths rather than the general (R, r) pair | **Two mathematical errors**, both caught by A1 and adjudicated numerically (§I.3): B9(c) union-over-splits "completeness" is false; B10(1) "both values attained" is false for the pessimistic value |

## I.2 Points of full agreement (all three attempts + the audit)

The following are confirmed by all three attempts independently and are adopted verbatim:

1. **A3.Thm1 is false** (`sin(ks)` witness) and the repair is a segment-regularity hypothesis (equicontinuity / common modulus / Lipschitz budget — the three attempts name the same hypothesis at three levels of generality, A2's modulus being the most general).
2. **B6.Thm1(1) is false** (parabola witness) and the "iff" is irreparable by any strengthening of the MFCQ data; exact local constancy holds exactly for *strictly* feasible directions; a quantitative `O(‖x−x̄‖‖d‖)` substitute holds in general.
3. **E4.Thm2's budget paragraph is arithmetically wrong** in both branches; the corrected finite-horizon threshold is `(b/(ℓ−1))(1−ℓ^{−G})` (resp. `bG`), the infinite-horizon criterion is "`b = 0`, or `ℓ > 1` with `r₀ ≥ b/(ℓ−1)`", and the corrected negative is **strictly stronger** than the recorded one: a contracting reset (`ℓ < 1`) with any deficit is unsustainable at *every* initial margin.
4. **E4.Lem1's margin definition is degenerate** (vacuous pairs `(ℓ, b)` with `b ≥ ℓ·r̄_g`); adding non-vacuity `b < ℓ·r̄_g` makes the declared-data refutation stand.
5. **E2.B2(a)** is closed by the one-line metric decomposition `O = ⋃ₙ{dist(·, U∖O) ≥ 1/n}`.
6. **E2.B1(a)**'s subfamily-inheritance sentence is backwards; post-fixed sets are join-closed, not subset-closed; the correct transfer runs the recursion *in* `𝒱*`.
7. **B1.Thm1**'s "verbatim r-eroded statement" needs a successor certificate at depth `3r/2`; the delivered depth is `r/2` at samples, `K` throughout.
8. **B10.Thm1(2)**: the universal safe-command set is not closed under Berge alone; the existential set is.
9. **C-a.Thm3**'s "arbitrary subsets" must be "arbitrary *definable* subsets" (the kernel-membership language does not separate table-distinct models).
10. **E7.Cor3 / C-e** misidentify `L_G` (a property of the velocity envelope, per packet 02 Lemma 2) as a barrier-geometry constant; the affine/quadratic contrast must be restated in terms of barrier constants (`L_n`, reach) with `L_G` untouched.
11. **A4.Thm1 Step 2** has the sign of `α` flipped relative to the controlling packet; the corrected chain is `⟨n_i, f_i⟩ ≤ −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i ≤ 0`; the conclusion survives.
12. **E7.Thm2**'s noncompensation clause must use the outer bound `D⁻_{i,T} − F⁻_{i,T}`, not the committed budget.
13. **E7.Thm1(b)** must be split (robust-kernel emptying vs pathwise exit); **(c)** is sharp at `D⁻_T − F⁻_T`.
14. **A3.Thm2** needs `ℬ` finite for termination; the bound is `|𝒜|·|ℬ|` (sharp), `dim` was undefined; the clopen clause was vacuous.
15. **C-f.Thm1** must be scope-locked to window/restriction observables; the general-observable case is open with the σ-algebra obstruction stated.
16. **B7.Thm1(3)** needs a versal-unfolding hypothesis (constant-family counterexample `f ≡ 0`); parts (1), (2) stand.

## I.3 The two adjudicated disputes (A1 vs A2), settled numerically

### Dispute 1 — B9: is the product-split family complete "in the existential form"?

A2's repaired B9 asserts, as clause (c):

> `K_p = ⋃ { ∩_k W_k^{(p_k)} : ∏ p_k = p }`  (completeness over budget splits)

A1's §IV asserts the opposite and supplies a witness: states `{x, y₁, y₂}` with `K = {x, y₁, y₂, safe}`, one policy, `x → y₁` or `y₂` w.p. `½` each, `ℙ(X₂ ∈ K | y₁) = 0.2`, `ℙ(X₂ ∈ K | y₂) = 0.8`. Then `ℙ(survive | x) = ½·0.2 + ½·0.8 = 0.5`, so `x ∈ K_{1/2}`; but for **every** split `(t_init, t_term)` with `t_init·t_term = ½`:

- `t_term ≤ 0.2` forces `t_init ≥ 2.5 > 1` — invalid;
- `0.2 < t_term ≤ 0.8` gives `W₁ = {y₂}`, `ℙ(X₁ ∈ W₁ | x) = ½`, requiring `t_init ≤ ½` while `t_init = ½/t_term ≥ 0.625` — contradiction;
- `t_term > 0.8` gives `W₁ = ∅`.

**Verdict (verified by exhaustive split search, `reaudit/verify_joint_disputes.py`): A1 is right; A2's (c) is FALSE.** `x ∈ K_{1/2}` lies in no split's `W₂`. The error in A2's proof of (c) is exactly the one A2 themselves diagnosed for *fixed* splits in their own §1.1: the constructed `p_k` are *averages* over the reachable state distribution, while the recursion demands *uniform per-state* conditional bounds. A2's numerical check B5 passed only because their 4-state model's good successor has conditional survival exactly `1.0`, making the model split-complete — a model-specific accident. **Consolidation:** A2's (c) is *struck*; the exact characterisations that survive are A2's (a) value iteration and A1's (C) residual-budget DP (both independently correct — see Finding 9 in Part II).

### Dispute 2 — B10: is the pessimistic leader value attained?

The audit's Finding 10 parenthetically claims the pessimistic objective is "in fact continuous by Berge". A2's repair follows the audit: "Both leader objectives are usc … Both therefore attain their maxima on compact `C`", and their repaired theorem (1) asserts existence of a pessimistic Stackelberg pair unconditionally. A1's §V proves the opposite:

- `φ(c) = max_{BR(c)} v_l` **is** usc (attains its max) — everyone agrees;
- `ψ(c) = min_{BR(c)} v_l` is **lsc**, not usc: with `BR` usc compact-valued, the min-attaining selections pass to the graph limit from *below* (`liminf ψ(c_n) ≥ ψ(c)`), which is lower semicontinuity.
- **Non-attainment witness** (verified numerically): `C = [0,1]`, `Π = {a,b}`, `v_f(c,a) = 0`, `v_f(c,b) = c−1`, `v_l(c,a) = c`, `v_l(c,b) = 0`. Then `BR(c) = {a}` for `c < 1`, `BR(1) = {a,b}` (usc — values jump *up*), `ψ(c) = c` for `c < 1`, `ψ(1) = min(1,0) = 0`. So `sup ψ = 1` is **not attained**: `ψ(1−10⁻ᵏ) → 1 > ψ(1) = 0`, `limsup_{c→1⁻} ψ(c) = 1 > ψ(1)` — ψ is not usc, and no pessimistic Stackelberg pair exists.

**Verdict: A1 is right; A2's (1) is FALSE in its pessimistic half; the audit's parenthetical is also wrong.** Note this also means the *original* B10(1) proof's sentence "the leader's pessimistic objective … is usc … hence attains its max" is a fourth false sentence in the original that the audit's Finding 10 did not flag (the audit verified "B10 part (1)'s existence half — Berge plus compactness", which is correct only for the optimistic value). **Consolidation:** pessimistic existence becomes *conditional* (on `BR` lsc, or single-valued, or `v_l` constant on fibres); the optimistic half, A2's coincidence characterisation, and A2's reduction-license table all stand. See Finding 10.

## I.4 New findings contributed by each attempt (beyond the audit)

| Attempt | New findings beyond PROOF_REAUDIT |
|---|---|
| M (blueprint) | Form A / Form B resolution of C4; the "stronger negative" reading of E4.Thm2; L_B separation |
| A1 | **(N1)** the original E3.C6.3 proof's parenthetical has the inclusions reversed ("⊇ is trivial" should be "⊆"); **(N2)** the recorded E4 vanishing-neighbourhood witness fails *even after* non-vacuity (the collapse hides in the vacuous zone; the linear piece must extend to the inradius); **(N3)** the co-Lipschitz + exterior-preserving derivation `(κ, 0)` — the *only* cheap-data margin derivation; **(N4)** B7(1)'s uniform-exhaustion hypothesis (the audit's "plausible but unelaborated step" named); **(N5)** E3.C2's two Farkas variants are *different alternatives* (`y^⊤A ≤ 0` is Farkas for `Ax = b, x ≥ 0`, not for `Ax ≤ b`); **(N6)** B10 pessimistic non-attainment (§I.3); **(N7)** B9 reverse-inclusion refutation (§I.3) |
| A2 | **(N8)** B6 part (2) has the **blocking direction's sign wrong** (`−d` for `d`): on the parabola witness `−d ∈ T_C` at every point, so the recorded hypothesis is false on the theorem's own example; **(N9)** E4's budget recursion admits `r ≡ 0`, so the forward budget theory is vacuous without a minimal-erosion lower bound `ρ_g > 0` (their D3); **(N10)** the backwards/minimal-required-depth form `u₀ = max(ρ, ρℓ^{−G} + b(ℓ^{−G}−1)/(1−ℓ))` and the exponential law `u₀ ~ (ρ + b/(1−ℓ))ℓ^{−G}`; **(N11)** the A3 moving-break ill-definedness (segment domains differ across `k`) repaired by reparametrization to `[0,1]`; **(N12)** the TV counterexample `(s+1)^k` closing the Helly escape route; **(N13)** the reach formula `τ = √c·√λ_min/λ_max` and `L_n = 1/τ` for quadratic barriers; **(N14)** B10's existential/universal reduction-license table (which target theorem needs which safe-command set) |

All seven A1 findings (N1–N7) and all seven A2 findings (N8–N14) are incorporated into the consolidated repairs below.

## I.5 Consolidation rule

For each finding: adopt the *strongest correct* treatment. Where the attempts disagree, the adjudication in §I.3 governs. Where one attempt went further than the others without error, the further step is adopted (e.g. A2's two-depth B1 subsumes A1's (D) and M's Form A/Form B; A1's B10 semicontinuity analysis supersedes A2's; both exact characterisations of B9 are kept and their relationship stated). No attempt's error is propagated: A2's B9(c) and B10-pessimistic-existence are struck from the consolidated result.

---

# Part II — The consolidated repairs

Notation follows the source files. "Status" lines give the proposed register label (Part III tabulates). Full developments: A1's files for the long-form proofs, A2's REPAIRED dossiers (at the `batch 4/` root, corrected per §I.3) for the quantitative and verified forms.

---

## Finding 1 — A3.Thm1 (Class 1: false as stated) — CONSOLIDATED

**Disposition.** The recorded statement is **false**; replaced, not qualified. Consolidated repair = A2's structure (general modulus, reparametrized metric, both counterexamples, dynamical closure) with A1's left-edge continuity condition (A2 has it independently) and the residue-list correction (the stale "Helly selection" reference is removed; see Finding 1′).

**Corrected statement (consolidated).** Fix `τ > 0`, `n ≥ 1`, `B ∈ ℕ`, `J, M ≥ 0`, and a modulus `ω` (nondecreasing, `ω(0) = 0`, continuous at `0`). Let `ℋ(B, J, M, ω)` be the càdlàg histories on `[−τ, 0]` with ≤ `B` breaks, jumps ≤ `J`, `‖φ‖ ≤ M`, and `‖φ(s) − φ(s')‖ ≤ ω(|s − s'|)` on each closed inter-break segment.

1. **Metric.** Pad the break set to `σ(φ) ∈ Δ_B` and reparametrize each segment affinely to `g_j(φ) : [0,1] → ℝⁿ` (A2's N11 — this also repairs the recorded topology's ill-definedness for moving breaks). `d(φ, ψ) := ‖σ(φ) − σ(ψ)‖_∞ + max_j ‖g_j(φ) − g_j(ψ)‖_{C[0,1]}`.
2. **Theorem.** `(ℋ(B, J, M, ω), d)` is **compact metrizable**; `d`-convergence is exactly break-tuple convergence plus uniform segment convergence (breaks may move; a jump travelling to an endpoint converges to a jump there); the break count is upper semicontinuous along limits.
3. **Sharpness.** Neither `(H1)–(H3)` alone (`sin(2πks)`, uniformly 1-separated) nor with a uniform total-variation bound (`(s+1)^k` with `TV = 1` exactly, the subsequence `{2^j}` ¼-separated — A2's N12, closing the Helly escape route) yields compactness. Uniform bounded variation gives only Helly's *pointwise* selection, a strictly weaker topology that cannot carry A3.Thm3's closed-predecessor step.
4. **Dynamical closure (A2 Prop 4.1).** If between events `ẋ = f(x_t)` with `‖f‖ ≤ V`, jumps ≤ `J`, event budget `B_e` per unit time, then every history window lies in `ℋ(⌈B_e τ⌉, J, M, ω_V)` with `ω_V(h) = Vh`. **The added hypothesis is a theorem about solution windows, not a new declaration** — the recorded A3.Thm1 was stated for a class the dynamics never leaves; it merely failed to name the one property the dynamics supplies for free.
5. **Delayed evaluation (A1 §5 = A2 Prop 5.1).** `t ↦ x_t` is `d`-continuous at every `t₀` with `dist({t₀, t₀ − τ}, E) > 0` (A1's left-edge condition; A2 states it identically); discontinuous at event epochs in general, sharply.

**Status.** A3.Thm1: `PROVEN (repaired: common-modulus hypothesis added; derived from the declared velocity bound by dynamical closure)`. A3.Thm3: condition list extended with the segment modulus (in substance unchanged — see Finding 1′). B8: still `CONDITIONAL` (also gated on E4.Lem1's repair, Finding 4).

### Finding 1′ — the two A3 file defects flagged by the owner (both confirmed live)

- **Dangling artifact (C1).** `batch 2/04_open_problems/A3_VARIABLE_EVENT_KERNEL.md` cites `A3_KERNEL_CERTIFICATE.json` twice (provenance header; status section) as an existing toy-instance artifact; **no such file exists anywhere in the tree**. Fix applied: both citations now state the artifact is **NOT IN TREE** (lost with the filesystem reset, not rebuilt); the manifest's COMPUTED_PARTIAL row is retained as a register entry only and certifies nothing.
- **Stale Helly residue.** The live residue list item 3 reads "Unbounded break counts defeat Thm1's compactness (the Helly selection needs the finite budget)". After the repair the proof no longer routes through Helly (it routes through Arzelà–Ascoli on the reparametrized segments), and bounded TV is refuted as a sufficient hypothesis in any case (Counterexample 2). Fix applied: the residue item now reads: unbounded break counts defeat the embedding `Δ_B × AS^{B+1}` (there is no fixed finite product to be compact in), and no bounded-variation or Helly-type substitute exists (Counterexample 2).

---

## Finding 2 — B6.Thm1 (Class 1: false as stated) — CONSOLIDATED

**Disposition.** Part (1) **false as stated** (parabola witness; robust to every strengthening of the MFCQ data — A2 §0: with witness `v̄ = (0,1)`, `⟨∇g, v̄⟩ = −1` at *every* point of the parabola with the same `γ = 1` and 2-Lipschitz `∇g`). Part (2) also carries **two defects the audit did not flag**: its hypothesis ("the pathway's blocked position realizes a first contact…") was never well-formed, and it excludes `−d` where it must exclude `d` (A2's N8: on the parabola, `−d ∈ T_C` at every point, so the recorded hypothesis is false on the theorem's own example). Consolidated repair = A2's quantitative part (1) + A2's corrected part (2) + A1's tangential/ray distinction.

**Corrected statement (consolidated).** `g ∈ C^{1,1}` near `x̄`, `∇g` L-Lipschitz, `𝒢 = {g ≤ 0}`, MFCQ data `(γ, v̄)` at `x̄`. Put `U = {‖x − x̄‖ < γ/(2L)}`.

**(1)** For every `x ∈ 𝒢 ∩ U`:
- **(a)** `A(x) ⊆ A(x̄)`; MFCQ holds at `x` with the same `v̄`, constant `γ/2`; Abadie holds: `T_𝒢(x) = {v : ⟨∇g_k(x), v⟩ ≤ 0, k ∈ A(x)}`.
- **(b)** **Quantitative lower semicontinuity:** for every `d ∈ T_𝒢(x̄)` there is `d_x ∈ T_𝒢(x)` with `‖d_x − d‖ ≤ (2L/γ)‖x − x̄‖‖d‖` (constructed as `d + t v̄`). The linear rate is sharp in order (closed form `2a/√(4a²+1)` on the witness).
- **(c)** **Exact constancy at the sharp hypothesis:** if `d` is *strictly* feasible at `x̄` (`⟨∇g_k(x̄), d⟩ < 0` on the active set), then `d ∈ T_𝒢(x)` for all `x ∈ 𝒢` near `x̄` — no modulus, no approximation. Sharp: weak feasibility cannot be stabilised (the witness's `d = (1,0)`).
- **(d)** Upper semicontinuity of `x ↦ T_𝒢(x)` **fails** in general (witness `w = (−1, −½)`).

**(2)** Under the single well-formed hypothesis **(BLK)** `d ∉ T_C(𝒢, x_b)`: there exists `ξ ∈ N_C(𝒢, x_b)` with `⟨ξ, d⟩ > 0 ≥ sup_{T_C} ⟨ξ, ·⟩`; under MFCQ at `x_b`, `ξ = Σ_{k∈A(x_b)} λ_k ∇g_k(x_b)` with `λ ≥ 0` explicit; for affine `g` this reduces exactly to the homogeneous Farkas alternative (a single active row certifies). The blocking direction is `d`, **not** `−d`.

**Reading (A1).** The original conflated *tangential* feasibility (`d ∈ T_𝒢(x̄)` — feasible curves with tangent `d`, possibly leaving the ray) with *ray* feasibility (`x̄ + sd ∈ 𝒢` for small `s`). The witness's `d = (1,0)` is in `T_𝒢(x̄)` yet the ray leaves `𝒢` immediately. Downstream consumers must say which they mean; E3.C2/E7.Thm2 consume the *strict local alternative* and the linear case, both intact.

**Status.** B6.Thm1: `PROVEN (repaired — (1) quantitative lsc + exact strict-constancy; (2) hypothesis (BLK) stated, sign of the blocking direction corrected, multiplier representation added)`. Original "iff" and "locally constant projection": **withdrawn** (false, not conjectures).

---

## Finding 3 — E4.Thm2 budget paragraph (Class 1: false as stated) — CONSOLIDATED

**Disposition.** Both recorded thresholds wrong; infinite-horizon branch wrong in the flattering direction. Consolidated repair = A2's three-layer correction (forward threshold; the new D3 non-vacuity of the budget question; the backwards minimal-depth form) + A1's invariance restatement (D). All three attempts agree on the arithmetic; A2's D3/N9/N10 additions are adopted; A1's (D) is adopted.

**Corrected statement (consolidated).** For `r_{g+1} = ℓ r_g − b` (`ℓ > 0`, `b ≥ 0`, `r₀ ≥ 0`):

- **(A) Closed form.** `r_g = r* + ℓ^g(r₀ − r*)`, `r* = b/(ℓ−1)` (`ℓ ≠ 1`); `r_g = r₀ − gb` (`ℓ = 1`).
- **(B) Forward threshold (tight).** Nonnegative on `{0..G}` iff `r₀ ≥ (b/(ℓ−1))(1 − ℓ^{−G})` (`ℓ ≠ 1`), resp. `r₀ ≥ bG` (`ℓ = 1`). The recorded `b(ℓ^G−1)/(ℓ−1)` is `ℓ^G ×` the correct threshold — too weak for `ℓ < 1`, too strong for `ℓ > 1`.
- **(C) Infinite horizon.** Nonnegative for all `g` iff `b = 0` (any `ℓ`), or `ℓ > 1` with `r₀ ≥ b/(ℓ−1)`. The recorded "`ℓ < 1` with `r₀ ≥ b/(1−ℓ)`" is the fixed point of `r ↦ ℓr + b` — the **wrong sign of the deficit**; the true fixed point is negative, and the sequence is eventually negative at every initial margin.
- **(D) The budget question is vacuous without a lower bound (A2's D3, new).** `r ≡ 0` is always admissible and delivers invariance of the uneroded path, so the forward form carries no content. The substantive question is the **backwards** one.
- **(E) Minimal required initial depth (A2's N10).** With genuine lower bounds `0 < ρ_g ≤ R_g` (within-generation erosion needs depth at least `ρ_g`), a budget exists iff `r₀ ≥ u₀`, where `u_G := ρ_G`, `u_g := max(ρ_g, (u_{g+1} + b)/ℓ)`; for constant `ρ`: `u₀ = max(ρ, ρℓ^{−G} + b(ℓ^{−G}−1)/(1−ℓ))` (`ℓ ≠ 1`), `u₀ = ρ + Gb` (`ℓ = 1`). **Sustainability at unbounded horizon iff `ℓ > 1`, or `ℓ = 1` with `b = 0`.** For `ℓ < 1` the required margin grows as `u₀ ~ (ρ + b/(1−ℓ))·ℓ^{−G}` — **exponentially in the horizon, even when `b = 0`** (a contracting reset maps depth `r` to `ℓr`; maintaining `ρ` costs `ρℓ^{−G}` regardless of deficit).
- **(F) Invariance under a solvable budget (A1's (D)).** Under recorded hypotheses (1)–(3) plus `r_g ≥ 0` (indeed `r_g ∈ [ρ_g, R_g]`) for `g ≤ G`, the eroded path is strongly invariant; the recorded induction is retained verbatim. If the budget fails, E4.Thm2 is **silent** (failure of invariance is an R03 adversarial-exit question).

**The corrected negative is stronger than the recorded one, and points the opposite way:** the record said a contracting reset is sustainable given enough initial margin; the truth is that *no initial margin buys intergenerational sustainability under a depth-contracting transition* — the buffer is consumed exponentially. Withdrawal obligation: every downstream citation of "the geometric budget `r₀ ≥ b/(1−ℓ)`" (grep `b/(1−ℓ)` and "geometric budget" before Paper 2 is finalised).

**Status.** E4.Thm2: `PROVEN (repaired — budget threshold (b/(ℓ−1))(1−ℓ^{−G}); sustainability requires ℓ>1 or (ℓ=1, b=0); original formula ℓ^G× too small for ℓ<1)`. **E4.Thm3's statement must carry the `ρ_g > 0` hypothesis** (obligation; see Finding 3′).

### Finding 3′ — E4.Thm3 obligation

E4.Thm3 consumes Thm2's invariance conclusion; without `ρ_g > 0` the assembly is vacuous (D3). Fix applied to the source: Thm3's hypotheses now include the genuine lower bounds `0 < ρ_g ≤ R_g`.

---

## Finding 4 — E4.Lem1(ii) (Class 1: false as written) — CONSOLIDATED

**Disposition.** The margin definition admits vacuous pairs (`b ≥ ℓ·r̄_g` makes the inclusion read as `K_{g+1}` at every tested `r`), so the recorded "no uniform `(ℓ, b)` with `b < ∞` exists" is false of *every* `K`-preserving family. Consolidated repair = non-vacuity + A2's inradius-extending witness + A1's (B) and (E).

**Corrected statement (consolidated).** `(ℓ, b)` is a **non-vacuous margin** of `R_g` if `ℓ > 0`, `0 ≤ b < ℓ·r̄_g`, and `R_g(K_{g,−r}) ⊆ K_{g+1,−(ℓr−b)}` for `r ∈ (b/ℓ, r̄_g]` (the `≤ 0`-read convention retained below `b/ℓ`). Then:

- **(i)** the transfer reading stands (deficit `b` consumed once per generation);
- **(ii)** the margin is **declared data** — not derivable from Lipschitz continuity plus boundary margins. Witness (A2, consolidated with A1's (B)): on `K = K′ = [0,1]` the family `φ_g(x) = x/g` on `[0, ½]`, `φ_g(x) = 1/(2g) + (x−½)(2 − 1/g)` on `(½, 1]` — continuous, increasing bijections, uniform Lipschitz constant 2 — collapses the incenter's depth `½` to `1/(2g) → 0`, so every non-vacuous pair fails at the predicted generation `g > 1/(ℓ − 2b)` (verified exactly: `(1, 0.4) → g = 6`; `(0.5, 0.2) → g = 11`; `(1, 0.49) → g = 51`). **A1's (B) is adopted as a necessary clause:** the *recorded* vanishing-neighbourhood witness (linear collapse only on `[0, ρ_g]`, `ρ_g ↓ 0`) is **not** a witness even against non-vacuous pairs — the collapse hides in the vacuous zone `r < b/ℓ`; the linear piece must extend to a uniformly positive depth (the inradius) for the test to bite. The audit's own numerical checks (λ = 1/20 at the inradius) were a different and correct witness;
- **(iii)** the **only** cheap-data derivation (A1's (E)): if `R` is co-Lipschitz with constant `κ` near `K` *and exterior-preserving* (`R(X∖K) ⊆ X′∖K′`), then `(κ, 0)` is a non-vacuous margin. Exterior-preservation is not optional (co-Lipschitz controls distances to the image of the complement, not to the complement);
- **(iv)** per-map existence is cheap and irrelevant (A1's (F)): each single reset admits `(λ, 0)`; the honesty clause is that a *family*-uniform pair is not readable from the shared cheap data.

**Status.** E4.Lem1: `PROVEN (repaired — non-vacuity hypothesis b < ℓ·r̄_g added; witness extended to the inradius; co-Lipschitz+exterior companion recorded)`.

---

## Finding 5 — E2.B2(a) Step 3 (Class 2: gap) — CONSOLIDATED

**Disposition.** Step 3 proved the closed-set statement and asserted the open-set one KRN requires. One-line repair, all three attempts identical. A1's extras adopted as remarks.

**Consolidated repair.** For open `O ⊆ U`: `O = ⋃ₙ Fₙ`, `Fₙ = {y : dist(y, U∖O) ≥ 1/n}` closed, `Fₙ ↑ O`; hence `{x : A_W(x) ∩ O ≠ ∅} = ⋃ₙ {x : A_W(x) ∩ Fₙ ≠ ∅}` is `F_σ`, so `A_W` is weakly measurable (KRN). The **metric** hypothesis is exactly what is needed (in a general regular space open sets need not be `F_σ`) — stated rather than left implicit. A1's additions: a constructive Borel selector (uniform limit of finitely-valued maps, no external selection theorem invoked) and a Castaing representation; and the honesty note that B2(a) does **not** close R02 Field 12 (a different correspondence — inflating it would be a false promotion).

**Status.** E2.B2(a): `PROVEN (repaired — one-line metric decomposition; conclusion unchanged)`.

---

## Finding 6 — E2.B1(a) (Class 2: backwards inheritance) — CONSOLIDATED

**Consolidated repair.** Knaster–Tarski core retained. The sentence "consistency is inherited by subfamilies" is **false** (A2's 2-point counterexample `Γ({1}) = {2}`; A1 and the audit give 3-point witnesses — all correct). Post-fixed sets are closed under **joins**, not subsets. Correct transfer: `Γ(C) ⊆ Γ(𝒱*) = 𝒱*` for every `C ⊆ 𝒱*`, so `R02.Thm1` applies to `𝒱*` itself and the recursion may be *started* from any `C ⊆ 𝒱*` provided certificate states are *tracked in `𝒱*`*. (REG)(ii) makes a smaller family *harder* to certify — `𝒱*` imposes the weakest closure obligation while containing every reachable certificate state.

**Status.** E2.B1(a): `PROVEN (repaired — subfamily claim re-scoped; join-closure and 𝒱*-tracking stated)`.

---

## Finding 7 — E3.C6.3 (Class 2: example for proof) — CONSOLIDATED

**Disposition.** M's blueprint graded (⟸) "PROVEN" and demoted (⟹) to a conjecture under prior coarseness — **both moves are superseded**. A1 and A2 independently found the landing gap in the (⟸) argument (the concatenation needs `x(t_d) ∈ Viab_full`, not merely `x(t_d) ∈ K`), and both replaced the whole iff with a provable exact characterisation, eliminating the conjecture.

**Consolidated repair.**

- **(i)** `Viab_del ⊆ Viab_full` always.
- **(ii) Exact characterisation (A2).** With the truncated kernel `T_del := {x₀ : ∃ prior-admissible π, x(t) ∈ K on [0, t_d] and x(t_d) ∈ Viab_full}`: `Viab_del = T_del`, hence `Viab_del = Viab_full ⟺ Viab_full ⊆ T_del` — every full-viable state admits a prior-admissible policy that stays safe to `t_d` **and lands in `Viab_full`**. Both directions proved directly (no example needed).
- **(iii) Sufficient condition.** If `Viab_full` is invariant under prior-admissible policies up to `t_d`, then equality holds.
- **(iv) The recorded hypothesis is the wrong quantifier** (A1's (D)): "no trajectory under *any* prior-admissible policy hits `X∖K`" is sufficient (any safe prior policy then lands… — note: even then, only together with the landing condition) and strictly stronger than needed; it constrains unsafe policies, which are irrelevant to viability. Its negation does **not** imply unequal kernels.
- **(v) R02.Prop3 is a sharpness witness** (a system where `Viab_full ⊄ T_del` and the inclusion is strict), not a proof of anything general.
- **(vi)** A1's (N1) applied: the source proof's parenthetical "and ⊇ is trivial" has the inclusions reversed — the trivial direction is `⊆` (delayed policies are a subclass); the concatenation establishes `⊇`.

**Status.** E3.C6.3: `PROVEN (repaired — truncated-kernel characterisation; the recorded iff replaced by a provable equivalence; R02.Prop3 recorded as sharpness witness)`. **The single demotion-to-conjecture of M's blueprint is withdrawn as unnecessary.**

---

## Finding 8 — B1.Thm1 (Class 2: over-strong conclusion) — CONSOLIDATED

**Disposition.** The headline is ambiguous; on the invariance reading it is **irreparably false** (A2's counterexample: `K = [0,1]`, `r = 0.4`, sampled dynamics `x_{k+1} = min(x_k + 0.2, 0.8)`, linear between samples — all three hypotheses hold, `x₀ = 0.4 ∈ K_{−r}`, the sample states `0.4, 0.6, 0.8, 0.8, …` leave `K_{−r}` at `k = 2` while remaining in `K_{−r/2}` at samples and in `K` throughout). No nonzero sample period admits continuous-time invariance of an eroded set under these hypotheses — structural, not a gap. The "verbatim" iteration needs the successor certificate at depth `3r/2` (shortfall `r`; all three attempts agree). Consolidated repair = **A2's two-depth theorem** (subsumes A1's (A)–(D) and M's Form A / Form B) with A2's tightness and bridge corollary.

**Corrected statement (consolidated).** Let `K ⊆ ℝⁿ` closed, `R > r ≥ 0`, sampled closed loop with period `T_s`. Assume: (1) envelope `x(t) ∈ B̄(x_k, ρ)` with `ρ ≤ V_max T_s`; (2) **confinement** `V_max T_s ≤ R − r`; (3) **successor certificate at depth `R`**: `x_k ∈ K_{−R} ⟹ x_{k+1} ∈ K_{−R}`. Then for `x₀ ∈ K_{−R}`: **(a)** `x_k ∈ K_{−R}` at every sample; **(b)** `x(t) ∈ K_{−r}` for every `t`. The confinement bound is **tight** (an outward excursion of `V_max T_s` from depth `R` reaches depth `R − V_max T_s`). Sample-period budget: `T_s ≤ (R − r)/V_max`. The record's proved content is the case `(R, r) = (r_rec/2, 0)`; the claimed invariance reading is the case `(R, r) = (R, R)`, which requires `V_max T_s ≤ 0`.

**C4 resolution (R02.Cor6).** Corollary (the closed bridge): packet Lemma 2 at depth `R` supplies hypothesis 3; under `L_G R + Δ ≤ α`, `0 < R < ρ`, `V_max T_s ≤ R − r`, every sampled trajectory from `K_{−R}` is safe at depth `r` continuously. **Both sides of the three-way disagreement were partly right:** the manifest's "bridge open" is superseded — the bridge closes *at the two-depth form with explicit bookkeeping*; the three asserting documents are corrected — the conclusion is at depth `r < R`, not at the certified depth, and B1's invariance headline was false. Part IV's citation form updated accordingly.

**Status.** B1.Thm1: `PROVEN (repaired — two-depth form (R, r); confinement tight; invariance reading refuted and withdrawn)`. R02.Cor6: `PROVEN_CONDITIONAL` with the bridge **closed at the two-depth form** (residual conditions: model-level verification of `L_G R + Δ ≤ α` and `V_max T_s ≤ R − r`; the empirical NOT CONFIRMED gate is untouched).

---

## Finding 9 — B9.Thm1(1) (Class 2: hand-waved reverse inclusion) — CONSOLIDATED, WITH ADJUDICATION

**Disposition.** The reverse inclusion is **false**, not merely unproved — refuted by two independent witnesses (A1's `y₁/y₂` model, §I.3; A2's 4-state model for fixed splits). A2's (c) union-over-splits completeness is also **false** (refuted by A1's witness; adjudicated in §I.3 — struck from the consolidated result). The consolidated repair keeps both correct exact characterisations and states their relationship.

**Corrected statement (consolidated).** Reviews `k = 0..N`, `X` compact, `K` closed, `Π` compact, laws weakly measurable.

- **(a) Value-iteration characterisation (A2).** `V₀ = 1_K`, `V_{k+1}(x) = sup_π ∫ V_k dℒ(·|x,π)`. Then `V_N(x) = sup_π ℙ(survive N)`, so `K_p = {x : V_N(x) ≥ p}` — ordinary dynamic programming for the joint chance constraint, needing **no quantile convention**.
- **(b) Soundness of any fixed split (all three).** For any `(p_k)` with `∏ p_k = p`: `∩_k W_k ⊆ K_p` (tower rule; measurable selector via E2.B2(a)). The quantile-budget recursion is a sound lower bound — what a certificate wants.
- **(c) Incompleteness of the split family (A1, adjudicated).** There are models and `p` with `x ∈ K_p` and `x ∉ ∩_k W_k^{(p_k)}` for **every** split `(p_k)` with `∏ p_k = p` (the `y₁/y₂` witness: `x ∈ K_{1/2}`, no split captures). Fixed-split equality and union-over-splits completeness are both **false**; the original's "attainment is where the compactness is used" does not repair it (compactness gives attainment of quantile *functions*, not uniformity of conditional *probabilities* across reachable states).
- **(d) The exact quantile-form recursion (A1's (C)).** Track the remaining budget as a state: `V_N(x, q) = 1` iff `q ≤ 0` or (`x ∈ K` and `q ≤ 1`); `V_k(x, q) = 1` iff `x ∈ K` and `∃u ∃ measurable r : X → [0,1]` with `E[r(X′)|x,u] ≥ q` and `V_{k+1}(y, r(y)) = 1` a.e. Then `x ∈ K_p ⟺ V₀(x, p) = 1`. This is the complete descendant of the recorded quantile recursion — the budget becomes state-dependent, which is precisely what the mixture witnesses demand.
- **(e) p = 1 reduction (A1's (D)).** Under support alignment, the `p = 1` case of (d) is the robust predecessor `{x : ∃u, D(x,u) ⊆ K}` — complete. (The audit's suggested "prove the reverse inclusion under support alignment" holds *only* at `p = 1`; at general `p` even support alignment does not rescue it — both witnesses are support-aligned.)
- **(f) Closedness of `K_p`.** The Fatou step is retained (audit-verified).
- **(g)** The multivariate quantile-*set* primitive needs a declared convention (A2's §1.2); (a) and (d) need none. Parts (2) and (3) of the original are unaffected ((3) legitimately consumes quantile sets *once the convention is declared* — now stated in the theorem rather than a footnote).

**Consumer note.** Paper 2 should cite (a) for the characterisation and (b) for certificates; it must not cite a fixed-split (or union-over-splits) equality.

**Status.** B9.Thm1: `PROVEN (restricted; repaired — forward inclusion + V-iteration + residual-budget DP; reverse inclusion and split-completeness refuted by explicit witnesses)`.

---

## Finding 10 — B10.Thm1(1) (Class 2: asserted coincidence) — CONSOLIDATED, WITH ADJUDICATION

**Disposition.** Per §I.3: the pessimistic objective is **lsc**, not usc; the pessimistic value need not be attained (A1's non-attainment witness, verified); the audit's "continuous by Berge" parenthetical and A2's "both values attained" are both wrong; A2's coincidence characterisation is right. Consolidated:

- **(A) Berge.** `BR` nonempty, compact-valued, closed graph; `v̄_f` continuous.
- **(B) Semicontinuity (A1).** `φ = max_{BR} v_l` is **usc** and attains its max (optimistic existence — unconditional). `ψ = min_{BR} v_l` is **lsc** and attains its *minimum*; `sup ψ` need not be attained (witness §I.3).
- **(C) Pessimistic existence is conditional.** Under `BR` lower semicontinuous, or `BR` single-valued, or `v_l` constant on `BR`-fibres, `ψ` is usc/continuous and a pessimistic Stackelberg pair exists. (Sufficient for all at once: `Π` compact convex and `v_f(c, ·)` strictly concave — the standard Stackelberg declaration.)
- **(D) Coincidence characterisation (A2).** `V_pes ≤ V_opt` always; equality iff `v_l(c*_opt, ·)` is constant on `BR(c*_opt)` (verified on 200 random instances). The gap `V_opt − V_pes` is the **price of follower non-uniqueness** — a governance quantity, not an artefact. The original's displayed equation holds only with `π*` *attaining the inner minimum* (A1).
- **(E)** The original's sentence "the leader's pessimistic objective … is usc … hence attains its max" is **false** — a fourth false sentence in the original that the audit's Finding 10 did not flag (recorded here as A1's N6).

**Status.** B10.Thm1(1): `PROVEN (repaired — optimistic existence unconditional; pessimistic existence conditional on BR lsc / single-valuedness / fibre-constancy; coincidence characterised exactly)`.

---

## Finding 11 — B10.Thm1(2) (Class 2: closed-graph inheritance) — CONSOLIDATED

**Consolidated repair.** For closed `F ⊆ Π`: the **existential** set `E_F = {c : BR(c) ∩ F ≠ ∅}` is closed under Berge alone (it is the level set `{c : max_{π∈F} v_f(c,π) = v̄_f(c)}`); the **universal** set `U_F = {c : BR(c) ⊆ F}` is generally **open** (strict inequality between continuous functions) and is closed iff `BR` is lsc (A2's Prop 2.1). The record's governance question ("some follower response keeps the system viable") is the existential form — available unconditionally. **Reduction license (A2's table, adopted):**

| target theorem | quantifier | set needed | hypothesis |
|---|---|---|---|
| E2.B2(a) measurable selection | existential | `E_Safe` | Berge alone ✓ |
| B1.Thm1 (two-depth) | existential in the follower | `E_Safe` | Berge alone ✓ |
| R02.Thm1 robust viability | universal over branches | `U_Safe` | **+ BR lower semicontinuous** |

The original's "all non-strategic theorems apply with `U := C`" is inflation (A1): only the existential reduction is licensed without extra hypothesis.

**Status.** B10.Thm1(2): `PROVEN (repaired — existential closed under Berge; universal conditional on BR lsc; reduction license split per target)`.

---

## Finding 12 — C-a.Thm3 (Class 2: separation failure) — CONSOLIDATED

**Consolidated repair.** The satisfying sets of sentences are exactly the Boolean algebra `𝔅` generated by the kernel-membership atoms. Models are language-indistinguishable iff they agree on every atom (two-table witness: `Succ(a) = {b}` vs `{a,b}`, identical kernels `{a,b}`); `𝔅` may be strictly smaller than `P(𝕄)` (4-model lattice: 2 of 16 subsets definable). **Completeness on the quotient** (A1's (B)): every subset of `𝕄/≡_𝕃` is definable (finite atom-valuation conjunctions, disjoined). Sharpness survives: definable non-monotone sentences exist (the recorded `∅ ≠ Viab ≠ K` witness re-verified: false → true → false as `K` grows), so no extremal shortcut; per-instance decidability (Thm2) unaffected. C_TIER_COMPLETIONS §C-a(2) carries the same "arbitrary subsets" claim and is amended identically.

**Downstream (A2's caution, adopted).** The narrowing is a scope fact for Paper 1 and Paper 5: a model can be **unidentifiable from kernel data alone** — two governance instantiations with different transition structure can be indistinguishable by every judgment the framework can express. Stated affirmatively beside the existing "no specific model has been verified" caveat.

**Status.** C-a.Thm3: `PROVEN (repaired — arbitrariness re-scoped to the definable Boolean algebra; quotient completeness stated)`.

---

## Finding 13 — E7.Cor3 and C-e (Class 3: wrong object) — CONSOLIDATED

**Consolidated repair.** Two constants, cleanly separated:

- `L_G` — the packet's **envelope** modulus (`d_H(G(x), G(p)) ≤ L_G‖x−p‖`), a property of the dynamics. The claim "`L_G = 0` for affine barriers" is **false** (A2's half-space envelope counterexample: `L_G = 1` exactly on a moiety floor). The claim "`L_G = inf 2√(xᵀM²x)`" is the wrong object (a barrier-geometry quantity).
- `L_n` / reach — the **barrier** geometry. Affine: `s_K` is affine with `C^{1,1}` seminorm 0, `L_n = sup‖Dn‖ = 0`, tubular radius `ρ = ∞`: the erosion calculus `L_G r + Δ ≤ α` applies **globally** — fully operative, not degenerate (the recorded "degenerates to `Δ ≤ α`" would license unbounded erosion with no budget — unsafe as well as false). Quadratic (`B = c − xᵀMx`, `M ≻ 0`): finite reach `τ = √c·√λ_min/λ_max` (A2's N13; = `b²/a` for semi-axes `a ≥ b`, verified to 1e-6), `L_n = 1/τ > 0`, calculus confined to `r < τ`.
- **Comparison sandwich (A1, adopted):** with `m_B = inf‖∇B‖`, `M_B = sup‖∇B‖` on a band: `{B ≥ B|∂K + M_B r} ⊆ K_{−r} ⊆ {B ≥ B|∂K + m_B r}`.
- **Translation-invariance clause (A1, adopted):** if additionally `G` is translation-invariant near `K` (in particular state-independent), then `L_G = 0` *is* available and Lemma 2 reduces to `Δ ≤ α` — this is the true content of the recorded claim, and E7.Thm1(a)'s integral identity coincides with it exactly when the `q_L`-velocity is state-independent (the ledger statement and Lemma 2 at `L_G = 0` are otherwise different facts).
- The C-e sandwich keeps the sharp outer bound `{B ≥ Φ⁻_T}` (the recorded `{B ≥ Φ⁺_T − Φ⁻_T}` repeats the F⁺-for-F⁻ substitution of Finding 16 and is weaker than the proof).

**Status.** E7.Cor3: `PROVEN (repaired — restated with L_n and ρ = ∞; L_G untouched)`. C-e.Thm1: `PROVEN (repaired — finite reach τ = √c·√λ_min/λ_max, L_n = 1/τ; sharp sandwich)`. Manifest row: "Quadratic moiety sandwich with `L_G > 0`" → "…with finite tubular radius `τ` and normal variation `L_n = 1/τ`". Withdrawn: both recorded `L_G` identifications.

---

## Finding 14 — A4.Thm1 Step 2 (Class 3: sign) — CONSOLIDATED

**Consolidated repair.** The corrected chain (matching packet 02 Lemma 2):

```
⟨n_i, f_i(x_i, u)⟩ ≤ −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i ≤ 0,
```

the last inequality being exactly `(∗)` of Step 1. `α_i` is a *margin* (what the velocity field gains on the uneroded boundary); erosion, interface defect, and implementation error *spend* it. **The error is not cosmetic** (A2's counterexample: with `α = 0.4, L_G = 0.2, r = 0.05, Δ = 0.1` the recorded bound `α + Lr = +0.41` admits the outward velocity `w = +0.205`, which exits `K_{−r}` at the first integration step, while the packet bound gives `−0.29` and correctly forbids it). Step 1, Step 3, the statement, A4.Thm2, and A4.Ex3 are correct and unchanged; the conclusion of Thm1 stands verbatim. **Obligation:** grep `revised_articles/` for `α` with a positive sign in erosion inequalities before Paper 2 is finalised.

**Status.** A4.Thm1: `PROVEN (repaired — Step 2 sign corrected; conclusion unchanged)`.

---

## Finding 15 — E7.Thm2 (Class 3: noncompensation bound) — CONSOLIDATED

**Consolidated repair.** (i) product inclusion per moiety (unchanged, correct); (ii) **sharp** noncompensation: `q_{L_i}(0) < D⁻_{i,T} − F⁻_{i,T}` for some `i` ⟹ outside the product kernel, and no cross-moiety transfer can rescue it — `q_{L_i}(T)` is invariant under moiety-`j` flows (verified: one distinct value across 200 random draws); (iii) the certificate is the moiety-`i` ledger identity (`e_i`) — a **conservation** fact, not a feasibility computation; the recorded Farkas invocation is unnecessary and is removed (Farkas/B6 re-enters only when a conversion pathway *is* declared — A1's clause, adopted). Explicit refutation of the recorded committed-budget test: with `D⁻ = 0.4`, `F ∈ [0.2, 1.0]`, `T = 10`, every `q(0) ∈ [2.0, 4.0)` is declared non-viable by the record yet is viable under `D ≡ D⁻` (min `q = 0.0 … 1.9 ≥ 0`). Sharpness of the corrected bound: `q(0) = D⁻_T − F⁻_T` is viable under `D ≡ D⁻` against `F ≡ F⁻`.

**Status.** E7.Thm2: `PROVEN (repaired — noncompensation re-scoped to the sharp outer bound D⁻−F⁻; ledger-identity certificate; Farkas invocation removed as unnecessary)`.

---

## Finding 16 — E7.Thm1(b),(c),(d) (Class 3: mismatch + sub-sharp) — CONSOLIDATED

**Consolidated repair.** (b) split: **(b1)** `F ≡ 0` admissible ⟹ `Viab_T = ∅` for `T > q_L(0)/γ` (the adversarial-exit certificate — what the hypothesis actually supports); **(b2)** `F ≤ 0` for *every* realization ⟹ every trajectory exits by `q_L(0)/γ`; **(b3)** (A2, adopted) under `F ≤ F⁺`: exit by `q_L(0)/(γ − F⁺)` when `γ > F⁺`, no exit forced when `γ ≤ F⁺`. (c) **sharp**: `q_L(0) ≥ D⁻_T − F⁻_T`, with sharpness proved (the recorded `F⁺` substitution is true but weaker by `F⁺_T − F⁻_T`; on the worked numbers the sharp bound is tighter by 8.0). (d) sandwich `{q ≥ D_T} ⊆ Viab ⊆ {q ≥ D⁻_T − F⁻_T}` with the committed `D_T` inner bound (the recorded `D⁺_T`-budget notation corrected) and the gap identified as commitment slack plus ignored regeneration. The mixed-regime honesty paragraph unchanged.

**Status.** E7.Thm1: `PROVEN (repaired — (b) split with sharp exit time; (c) sharp outer bound with sharpness proof; (d) corrected sandwich)`.

---

## Finding 17 — A3.Thm2 (Class 3: typing) — CONSOLIDATED

**Consolidated repair.** `𝒜` finite, `O` clopen-fibred ⟹ the predecessor is well-defined on the quotient (clopenness makes `O` locally constant — the substantive use, which lives in the history space). **`ℬ` finite** ⟹ termination in at most `|𝒜|·|ℬ|` strict decreases — **sharp** (one-element-per-step chain; A2) — and the limit is the gfp. The bound `|𝒜|·dim` was undefined; the "clopen in W's coordinates" clause was vacuous (finite discrete quotient) and is dropped; the compact-`ℬ` case gives gfp existence only, with termination **not** claimed (A1's (C); A2's non-termination example: 12 strict decreases in 60 steps on `ℬ = [0,1]`). The finiteness hypothesis is not ad hoc — the file's own Reading names the governance-relevant class (quota reviews, survey triggers, mode switches), all finite-information. A3.Thm3's condition list becomes *budgeted + transversal + clopen + finite information states* (+ segment modulus, Finding 1).

**Status.** A3.Thm2: `PROVEN (repaired — ℬ declared finite; sharp termination bound; vacuous clopen clause dropped)`.

---

## Finding 18 — C-f.Thm1 (Class 3: scope) — CONSOLIDATED

**Consolidated repair.** Statement scope-locked to **window-restriction observables** `π̃_τ̃`; both directions proved at that scope (autonomy of the window dynamics ⟺ `f` factors through `π̃_τ̃`; memory horizon = minimal such `τ̃`). The general-observable case is **open**, with the obstruction stated precisely (A2: the integral functional `∫_{−τ}^0` is fibre-constant on no window — verified for `τ̃ ∈ {0.9, 0.75, 0.6, 0.5, 0.25}` — so its horizon is exactly `τ`, a fact about that observable, not a theorem instance; what autonomy gives in general is measurability of `f(x_t)` against the aggregate history's σ-algebra, weaker than fibre-constancy of any truncation). A1's (C) framing adopted: the general form is the definition of a factor system, not a theorem of this file. The file's own Scope paragraph was already honest; the Statement now matches it.

**Status.** C-f.Thm1: `PROVEN (repaired, scope-aligned to window observables; general-observable case OPEN with the obstruction stated)`.

---

## Finding 19 — B7.Thm1(3) (Class 3: genericity) — CONSOLIDATED

**Consolidated repair.** Thom's jet transversality is a statement about a *space of maps*; a residual set of *parameters* in a fixed one-parameter family requires the family to be a **versal unfolding** of the contact geometry (equivalently, its jet-extension is transverse to the tangency stratification). Counterexample (A2): `f ≡ 0`, `K = [−1,1]` — every `λ` gives tangential contact; the transversal-contact set is empty, not residual (0 of 41 grid values). Contrast: `f = λ` — transversal for every `λ ≠ 0`; exceptional set `{0}`, residual as claimed. Consolidated statement: **(3a)** for a residual set of `C^k` *families* (Whitney topology), the contact set is empty or transversal (A1); **(3b)** for a *fixed* family, transversality at `λ₁` is a hypothesis of part (2), not a conclusion — no residual-in-`Λ` claim without versality. **A1's (N4) adopted for part (1):** the exhaustion `Viab(λ) = ∩_n V_n(λ)` is Hausdorff-continuous only under a **uniform** exhaustion radius on a neighbourhood — named as a hypothesis (structural stability supplies it when the conjugacy modulus is uniform; the implication is plausible and used, but is now stated rather than implicit). Part (2) unchanged.

**Status.** B7.Thm1: `(1), (2) PROVEN (repaired — uniform exhaustion named); (3) PROVEN_CONDITIONAL on versality (narrowed — no strengthening available; the counterexample family satisfies every recorded hypothesis)`.

---

## Finding 20 — Minor items — CONSOLIDATED

- **C-a.Thm2 complexity:** `O(G²·|U|·|D|)` bit operations, or `O(G·|U|·|D|)` word operations under the word-parallel convention — **which is now named** (A1 + A2, consistent). Headline `O(N·G·|U|·|D|)` unaffected under the word convention.
- **E3.C2 Farkas:** the statement's `y^⊤A ≤ 0` and the proof's `y^⊤A = 0` are **different alternatives** (A1's (N5), refining the audit's "both are valid variants"): the recorded `Ax ≤ b` system pairs with `y ≥ 0, y^⊤A = 0, y^⊤b < 0`; the `≤ 0` form is the alternative for `Ax = b, x ≥ 0`. The file now states the first, consistently in statement and proof. Typo "surflux" → "surplus".
- **A4.Thm1-Explicit:** the composite condition `δ₁₂(δ₂₁(r)) ≤ r` is non-strict; at equality (`γ₁₂γ₂₁ = 1` in the linear shadow) the feasible set is a ray with no least positive contract — one clause added; R05.Cor3's strict form is what buys uniqueness and the spectral gap (A1's analysis adopted).
- **A4 Setting-section lemma:** `φ_i(s) ≥ φ_i(r*)` (not `=`) — the typo is corrected; A4.Thm2's own proof already had it right.
- **E1.A1 Move 1:** the two readings (adversary promotion vs input quantifier) coincide **iff** the promoted block realises exactly the admissible disturbance class — a **matching hypothesis**, now named, not a definition (all three attempts agree).

---

# Part III — Status-register consequences (consolidated)

Per TCS-1.0 §9 axiom 5 (status monotonicity): every move is a demotion, a scope-lock, a correction, or a replacement of a false sentence by a true one of equal or greater force. **No promotions.** Rows marked ▲ carry adjudications from §I.3.

| Row | Current | Consolidated | Basis |
|---|---|---|---|
| A3.Thm1 | PROVEN (reconstructed) | **PROVEN (repaired: common-modulus hypothesis; derived from the velocity bound)** — original FALSE_AS_STATED, refuted by two counterexamples | F1 |
| A3.Thm2 | PROVEN (reconstructed) | PROVEN (repaired: ℬ finite; sharp bound; vacuous clause dropped) | F17 |
| A3.Thm3 | PROVEN_CONDITIONAL (reconstructed) | PROVEN_CONDITIONAL — condition list: budgeted (+modulus, free by dynamical closure) + transversal + clopen + **finite information states** | F1, F17 |
| A4.Thm1 | PROVEN (reconstructed) | PROVEN (repaired: Step 2 sign; conclusion unchanged) | F14 |
| A4.Thm2 | PROVEN (reconstructed) | PROVEN (verified; untouched) | audit ✓ |
| B1.Thm1 | PROVEN (reconstructed) | **PROVEN (repaired: two-depth form; invariance reading refuted and withdrawn)** | F8 |
| R02.Cor6 | PROVEN_CONDITIONAL (bridge open) | PROVEN_CONDITIONAL — **bridge closed at the two-depth form** (`L_G R + Δ ≤ α`, `V_max T_s ≤ R − r`); the three asserting documents corrected to the depth bookkeeping | F8 / C4 |
| B6.Thm1 | PROVEN (reconstructed) | **PROVEN (repaired: (1) quantitative + strict-constancy; (2) (BLK) + multipliers, blocking-direction sign corrected)** | F2 |
| B7.Thm1 | PROVEN (reconstructed) | (1),(2) PROVEN (uniform exhaustion named); (3) **PROVEN_CONDITIONAL on versality** (narrowed; no strengthening available) | F19 |
| B9.Thm1 | PROVEN (restricted; reconstructed) | **PROVEN (restricted; repaired: forward + V-iteration + residual-budget DP; reverse inclusion and split-completeness refuted)** ▲ | F9 |
| B10.Thm1 | PROVEN (reconstructed) | **PROVEN (repaired: optimistic existence unconditional; pessimistic existence conditional; coincidence characterised; reduction license split)** ▲ | F10, F11 |
| C-a.Thm2 | PROVEN (reconstructed) | PROVEN (word-parallel convention named) | F20 |
| C-a.Thm3 | PROVEN (reconstructed) | PROVEN (repaired: definable Boolean algebra; quotient completeness) | F12 |
| C-e.Thm1 | PROVEN (reconstructed) | PROVEN (repaired: finite reach τ, L_n = 1/τ; sharp sandwich) — row text updated | F13 |
| C-f.Thm1 | PROVEN (reconstructed) | PROVEN (repaired, scope-aligned to window observables; general case OPEN) | F18 |
| E1.A1 | PROVEN (reconstructed) | PROVEN (matching hypothesis named on Move 1) | F20 |
| E1.A2 | PROVEN (reconstructed) | PROVEN (verified; untouched) | audit ✓ |
| E2.B1(a) | PROVEN (reconstructed) | PROVEN (repaired: subfamily claim re-scoped; 𝒱*-tracking) | F6 |
| E2.B1(b) | PROVEN (reconstructed) | PROVEN (verified; untouched) | audit ✓ |
| E2.B2(a) | PROVEN (reconstructed) | PROVEN (repaired: one-line metric decomposition) | F5 |
| E3.C1, C3, C4.1, C4.2 | PROVEN (reconstructed) | PROVEN (verified; untouched) | audit ✓ |
| E3.C2 | PROVEN (reconstructed) | PROVEN (one Farkas alternative; typo) | F20 |
| E3.C6.3 | PROVEN (reconstructed) | **PROVEN (repaired: truncated-kernel characterisation; no conjecture needed)** | F7 |
| E4.Lem1 | PROVEN (reconstructed) | PROVEN (repaired: non-vacuity; inradius witness; co-Lipschitz companion) | F4 |
| E4.Thm2 | PROVEN (reconstructed) | PROVEN (repaired: corrected thresholds; stronger negative; exponential law) | F3 |
| E4.Thm3 | PROVED (assembly) | PROVEN — statement now carries `ρ_g > 0` | F3′ |
| E7.Thm1 | PROVEN (reconstructed) | PROVEN (repaired: (b) split; (c) sharp; (d) sandwich) | F16 |
| E7.Thm2 | PROVEN (reconstructed) | PROVEN (repaired: sharp outer bound; ledger certificate) | F15 |
| E7.Cor3 | (file-level) | PROVEN (repaired: L_n, ρ = ∞; L_G untouched) | F13 |
| WAVE_E_UPDATE.md §1/§2 | (see C3–C5) | corrected per CROSS_DOCUMENT_CONSISTENCY bucket-B fixes | C3–C5 |

**Withdrawn claims** (false as stated; not conjectures): A3.Thm1 as recorded; B6.Thm1(1) "iff" and the locally-constant projection; B6.Thm1(2) `−d` exclusion; E4.Thm2 both recorded thresholds; E4.Lem1 "no uniform (ℓ,b) with b < ∞"; E3.C6.3 iff as recorded; B1.Thm1 invariance reading and "verbatim" iteration; B9.Thm1(1) fixed-split equality; B10 optimistic/pessimistic coincidence, ψ-usc, and universal closed-graph inheritance; C-a.Thm3 raw-lattice arbitrariness; E7.Cor3 `L_G = 0`; C-e `L_G = inf 2√(xᵀM²x)`; E7.Thm2 committed-budget noncompensation; B7.Thm1(3) unconditional genericity.

**The one demotion-to-conjecture of the lost original (E3.C6.3 (⟹) under prior coarseness) is eliminated** — the joint process replaced it with a provable exact characterisation. No row above is demoted to conjecture; every conclusion either survives at corrected scope or is replaced by a stronger true statement, except B7.Thm1(3), which is *narrowed* under an explicit hypothesis (the single case where no strengthening exists).

---

# Part IV — Implementation map

This document is the authority for the implementation commits that follow it (each committed and pushed separately per the push discipline):

1. **F6** — `PROOF_MANIFEST.md` Part VI §B table separator: literal `\n` → real newline (rendering only; no status or hash touched).
2. **Source-file repairs** — the ten theorem files receive the consolidated statements of Part II as replacement sections with repair notes pointing here and to the `batch 4/*_REPAIRED.md` dossiers; the two A3 defects of Finding 1′ (dangling certificate citations; stale Helly residue) are fixed in the same pass; E4.Thm3 carries `ρ_g > 0`; E3.C6.3's reversed-inclusion parenthetical is corrected.
3. **Register updates** — `PROOF_MANIFEST.md` rows per Part III; Part IV's B1 citation form updated to the two-depth wording; the R02.Cor6 row records the closed-at-two-depth bridge.
4. **Bucket B documentation fixes** — F2 (Edwards README M2m clause), F3 (NOT_REPRODUCIBLE scope to the three `pcp_*` columns), C1 (A3 citations; manifest COMPUTED_PARTIAL path column), C2 (reproduction command corrected), C3 (WAVE_E_UPDATE §2 computation labels), C5 (WAVE_E_UPDATE E5 row), C6 (B4 row → 35-period prefactor-aware figure with the assessment cited).
5. **Tooling and crosswalk** — the 13 verification suites committed under `reaudit/` (with the joint-dispute script); the C7 manuscript-taxonomy ↔ manifest-vocabulary crosswalk appended to the manifest.
6. **Worklog** — the session worklog committed at the repository root.

F1 (retention-field semantics) and F4 (`build_panel.py` destructive write) require owner decisions on code behaviour and are **not** applied; they remain recorded in `WAVE_E_RERUN.md` with their options. C8 (traceability reports predating the register) is structural and is recorded as an obligation in the crosswalk note rather than silently rewritten.
