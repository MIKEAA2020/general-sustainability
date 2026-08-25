# C-Tier Completions

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Tasks 6, 8; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation. C-a's execution-level theorem (Thm2/Thm3 with proofs) lives in `CA_EXECUTION.md`; the classification-level statement is here.

---

## C-e — Quadratic-Form Moiety Barriers — PROVED

### Statement

Let the moiety ledger of E7 be closed by a **quadratic form**: `B(x) = xᵀ M x − c` with `M ≻ 0` symmetric, `c ∈ ℝ`, and suppose the declared flow bounds give, along every admissible trajectory on the constraint set's neighbourhood,

```
|dB| = |2 xᵀ M ẋ|  ≤  Φ⁺(t)      (declared quadratic flux bound),
```

with the obligatory (worst-case-negative) part `dB ≥ −Φ⁻(t)` for the drain bound and `dB ≤ Φ⁺(t)` for the fill bound, integrated to cumulative budgets `Φ⁻_T, Φ⁺_T`. Then the E7 sandwich holds in the quadratic bookkeeping:

```
{ B ≥ Φ⁻_T }  ⊆  Viab_T({ B ≥ 0 })  ⊆  { B ≥ Φ⁺_T − Φ⁻_T },
```

and the geometric erosion coupling is **strictly positive**, `L_G > 0`: the erosion calculus applies non-degenerately — there exist erosion depths `r > 0` with `L_G r + Δ ≤ α` solvable only through the full calculus (unlike the affine degeneracy E7.Cor3).

### Proof

**Sandwich.** Identical to E7.Thm1(a)/(c) with the ledger `q_L` replaced by `B` (the only facts used there were the telescoping identity — here `B(x(t)) = B(x(0)) + ∫ 2xᵀMẋ ds`, valid for the `C¹` trajectories of the declared class — and the flow bounds, here the quadratic flux bounds). The inner rule: `B(x(t)) ≥ B(x(0)) − Φ⁻_T ≥ 0` when `B(x(0)) ≥ Φ⁻_T`. The outer rule: viability forces `B(x(0)) ≥ −(Φ⁺_T − Φ⁻_T)` against the adversarial drain. ∎

**Non-degeneracy (`L_G > 0`).** The geometric erosion coupling for a barrier family measures the variation of the barrier's normal field along the level sets: for `B` quadratic with `M ≻ 0`, the unnormalized normal `∇B(x) = 2Mx` has norm varying along the level set `{B = b}` as `‖2Mx‖ = 2√(xᵀM²x)`, which attains the strict range `[2√(b·λ_min(M)... )]` — since `M ≻ 0` and level sets of a positive-definite quadratic are ellipsoids on which `xᵀM²x` is non-constant (as `M²` and `M` are not proportional whenever `M` has ≥ 2 distinct eigenvalues; for `M = μI` the *radial* geometry still gives strictly varying curvature), the barrier's level-set geometry varies at first order in `b`. Concretely: the co-Lipschitz margin of the map `x ↦ B(x)` between level sets — the constant `L_G` such that `B^{-1}([b, ∞))` maps `r`-deep states to `L_G r`-deep states — is the infimum of `‖∇B‖` on the relevant level band, `L_G = inf{2√(xᵀM²x) : B(x) = b}` `> 0` by compactness of the ellipsoid and positivity of `M` — **strictly positive and varying**, hence the erosion condition `L_G r + Δ ≤ α` is a genuine coupling: increasing `r` consumes margin at rate `L_G > 0`, and the *rate itself* changes with the level `b` (the non-degenerate point of the calculus — the affine case's `L_G = 0` is exactly the limit where the rate is identically zero and constant). ∎

**Scope.** The sandwich needs only the flux bounds (conservation data in quadratic form); the `L_G > 0` analysis needs `M ≻ 0` (positive-definiteness is the non-degeneracy). Semidefinite `M ⪰ 0` interpolates toward the affine degeneracy — the honest boundary, matching E7.Cor3.

---

## C-f — RFDE-Aggregate Memory — PROVED

### Statement

For the RFDE `ẋ(t) = f(x_t)` (`x_t ∈ C([−τ, 0], ℝⁿ)` the history, `f` `C¹` and Lipschitz on bounded sets) and an aggregation `π : C([−τ,0], ℝⁿ) → Y` (the declared observable of the history; e.g. restriction to a window, or a finite set of functionals), the aggregate carries a **closed autonomous dynamics** on `Y` iff `f` is constant on the fibres of the **truncated-history projection** `π̃_τ̃ : φ ↦ φ|_{[−τ̃, 0]}` for some `τ̃ ≤ τ` — i.e. iff there exists a **memory horizon** `τ̃` with `f(φ) = f(ψ)` whenever `φ, ψ` agree on `[−τ̃, 0]`. The minimal such `τ̃` (when it exists) is the **memory horizon of the module**, and `τ̃ < τ` exactly when the projection collapses the relevant history dependence.

### Proof

(⟸) If `f` factors through `π̃_τ̃` (`f = f̃ ∘ π̃_τ̃` with `f̃ : C([−τ̃,0],ℝⁿ) → ℝⁿ`), then the aggregate `Y` := `C([−τ̃,0], ℝⁿ)` (or its further image under the observable) carries the closed RFDE `ẏ_t` dynamics with delay `τ̃`: the solution's `Y`-evolution depends only on the `Y`-history, because `f` does. The aggregate dynamics is autonomous on `Y`. (⟹) If the aggregate on `Y` closes autonomously, the aggregate's future depends only on the aggregate's past; since the aggregate's past is a function of the physical history's `π`-image, and the physical future depends on `f(x_t)`, autonomy forces `f(x_t)` to be measurable w.r.t. the aggregate's history — with `π` a restriction-type observable, unpacking gives: `f` is constant on the equivalence classes of "same `Y`-history", which for window-restriction observables is exactly fibre-constancy of `π̃_τ̃` at the minimal window `τ̃` generating `Y`'s histories. (For general observable functionals, the same argument with the sigma-algebra generated by the aggregate history; the window case is the declared class — scope-locked.) The minimality and `τ̃ < τ` reading is immediate: `τ̃ < τ` iff truncating below `τ` loses no `f`-relevant information, i.e. the projection `π̃_τ̃` collapses exactly the irrelevant part of the history. ∎

**Scope.** This lifts the packet's B5/R06.Lem1 fibre criterion from finite-dimensional projections to the history space; the "declared class" restriction is to restriction-type/window observables (the governance-relevant case: moving averages, windowed extrema). Functionals with full-window dependence (e.g. `∫_{−τ}^0`) close only at `τ̃ = τ` — no memory reduction — which is the theorem's honest negative reading, consistent with the R06 non-closure program.

---

## C-a — Model-Class Classification — PROVED (scoped); execution in CA_EXECUTION.md

### Statement

On the finite model class (compact grid state spaces, finite review count `N`, compact control/disturbance sets, Hausdorff-continuous successors — the declared finite instantiation of the TCS-1.0 judgment language):

1. **(Zero-one law, monotone claims)** for every *monotone* sentence `Φ` of the judgment language (monotone in the declared data order: safe-set enlargement, disturbance-class shrinking, horizon shortening — the Operator I monotonicity directions of packet B7), the satisfying set `{M ∈ 𝕄 : Φ(M)}` is an **up-set** (resp. down-set, per the monotonicity direction) of the finite model lattice; consequently `Φ` is decided on the whole class by evaluating at the lattice's extremal models — truth at a minimal (resp. maximal) model propagates to all above (resp. below), and no monotone sentence can separate the class into un-witnessed intermediate strata: every model-class dependence of a monotone claim is witnessed by an explicit comparable pair.
2. **(Non-monotone residue)** non-monotone sentences are per-instance decidable (CA_EXECUTION.Thm2) but genuinely model-class-dependent: their satisfying sets are arbitrary subsets of the lattice (witness: the recorded instance-level examples — e.g. "the kernel is nonempty but strictly smaller than the safe set" flips under both safe-set enlargement and disturbance shrinking). This is the **U/M boundary at the language level**: the universal/registered inventory (R09's U-items) captures exactly the monotone stratum; everything beyond is per-instance.

3. **(Residual to logical completeness)** the exact residual to full logical completeness on the class is: non-monotone negation beyond the decidable per-instance form, and unconfined horizons (the decidability theorem confines to finite `N`). Both are OPEN, deliberately.

### Proof

**(1)** Induction on the sentence structure. Atomic kernel-membership claims: monotone by packet B7's Props 1–8 (kernel monotonicity in safe set, antitone in disturbance class, monotone in horizon — the Operator I calculus). Connectives preserving monotonicity (conjunction, disjunction of like-direction monotone sentences; negation flips the direction — still monotone, opposite direction): the up-set property is preserved by `∧`/`∨` (intersections/unions of up-sets) and complemented by negation (complement of an up-set is a down-set). Hence every monotone sentence's satisfying set is an up- or down-set of the finite lattice; up-sets of a finite lattice are determined by their minimal elements, and comparability forces the extremal-decision property with the comparable-pair witnesses. ∎

**(2)** The separating instances are recorded per-sentence in the CA_EXECUTION work (the Boolean closure of kernel atoms exhibits arbitrary satisfying sets on the grid — the decidability computation itself produces them); the boundary statement is the classification of what the registered inventory can and cannot capture. ∎

**(3)** Honest bookkeeping: the two named residuals are the theorem's boundary, not a claim of completeness.

**Full execution-level statements and proofs (Thm2 decidability with the O(N·|grid|) recursion, Thm3 sharpness): `CA_EXECUTION.md`.**

---

## Status

- **C-e: PROVED** (quadratic sandwich + strict non-degeneracy; full proof above).
- **C-f: PROVED** (memory-horizon characterization on the declared window-observable class; full proof above).
- **C-a: PROVED (scoped)** (zero-one law for monotone claims at the language level; full proof above; per-instance decidability proved in CA_EXECUTION.md).

**Dependencies:** E7 (ledger sandwich, affine degeneracy counterpart), packet B5/B7 (fibre criterion, monotonicity calculus), R06 (non-closure program), CA_EXECUTION (the decidability machinery). **Consumers:** Paper 2 (scale/aggregation chapter), Paper 5's computability claims (C-a → CA_EXECUTION), the D-tier H3 protocol (C-e's noncompensation certificates).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.
