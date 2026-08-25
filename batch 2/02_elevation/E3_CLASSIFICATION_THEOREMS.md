# E3 — Classification Theorems (C1–C6)

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 3; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

**Reconciliation note (this expansion):** the card version described C2's nonlinear classification as a "conjectural bridge" and C5's transversality classification as "stated, not proved" — both stale: the later B-tier wave **proved** them (B6 and B7 in `04_open_problems/B_TIER_BRIDGES.md`). This document states both at their proved scope and cross-references.

---

## C1 — Complete scalar-delay classification — PROVEN

### Statement

Consider the linear delay equation

```
ẋ(t) = −α x(t) − β x(t−τ),   α > 0, β ∈ ℝ, τ ≥ 0,
```

with characteristic equation `Δ(λ) := λ + α + β e^{−λτ} = 0`. Let "stable" mean: all roots satisfy `Re λ < 0` (equivalently, the zero solution is locally exponentially stable; by linearity this is the global classification). Then:

- **(i)** `|β| < α` ⟹ stable for **every** `τ ≥ 0` (delay-independent stability);
- **(ii)** `β > α` ⟹ stable **iff** `0 ≤ τ < τ*` where
  `τ* = arccos(−α/β) / √(β² − α²)`;
- **(iii)** `β < −α` ⟹ unstable for **every** `τ ≥ 0` (including `τ = 0`);
- boundary: `β = α` ⟹ stable for every `τ` (no crossing occurs; see Step 3); `β = −α` ⟹ `λ = 0` is a root for every `τ` (marginal, not asymptotically stable).

Every imaginary-axis crossing (as `τ` increases) is **rightward** (`Re λ` crosses from negative to positive); there are no leftward crossings.

### Proof

**Step 1 (no roots in the closed right half-plane when `|β| < α`).** Suppose `Re λ ≥ 0`. From `Δ(λ) = 0`, `|λ + α| = |β|`. But `|λ + α|² = (Re λ + α)² + (Im λ)² ≥ α² > β²`, a contradiction. Hence all roots have `Re λ < 0`, for every `τ ≥ 0` — the bound used nothing about `τ`, giving (i). The same computation with `|β| = α` shows `Re λ ≥ 0` forces `Re λ = 0, Im λ = 0`, i.e. `λ = 0`; but `Δ(0) = α + β`, which vanishes only for `β = −α`. This gives the boundary cases: `β = α` stable ∀τ; `β = −α` has the zero root ∀τ.

**Step 2 (root count is right-continuous and changes only at crossings).** Roots of `Δ` are continuous in `τ`; in any strip `|Im λ| ≤ R` the roots are uniformly bounded away from infinity, and the number of roots with `Re λ > 0` can change only when a root crosses the imaginary axis. (Standard quasipolynomial bookkeeping: `Δ` has finitely many roots in any right half-strip `Re λ ≥ −c, |Im λ| ≤ R`, all simple in `τ` except at crossings; the count is locally constant off crossings.)

**Step 3 (all crossings are rightward).** Let `λ = iω`, `ω ≠ 0`, satisfy `Δ(λ) = 0` at some `τ`. Differentiate `Δ(λ(τ), τ) = 0` in `τ`:

```
λ̇(1 − βτ e^{−λτ}) = βλ e^{−λτ}   ⟹   λ̇ = βλ e^{−λτ} / (1 − βτ e^{−λτ}).
```

At the crossing, `β e^{−iωτ} = −(iω + α)`, so numerator `βλe^{−λτ} = −iω(α + iω) = ω² − iαω` and denominator `1 + τ(α + iω)`. Hence

```
Re λ̇ = Re [ (ω² − iαω)(1 + τα − iτω) ] / |1 + τα + iτω|²
     = [ ω²(1+τα) − ατω² ] / |1 + τα + iτω|²   =   ω² / |1 + τα + iτω|²  > 0.
```

Every crossing is rightward. (The denominator cannot vanish: `1 + τα + iτω = 0` would need `τα = −1 < 0`.) This is the computation that was numerically verified in session for the parameter sweep of the programme's delay modules; the display above is the closed form.

**Step 4 (case (ii)).** Let `β > α`. At `τ = 0` the equation is `ẋ = −(α+β)x` with `α + β > 0`: stable. A crossing at `λ = iω` requires `|iω + α| = β`, i.e. `ω = ±√(β²−α²) =: ±ω₀` — the **only** possible crossing frequencies. For `ω = ω₀ > 0`: `α + iω₀ = −β e^{−iω₀τ}` gives `cos(ω₀τ) = −α/β`, `sin(ω₀τ) = ω₀/β > 0`, so crossings occur at `τ_k = (arccos(−α/β) + 2kπ)/ω₀`, `k = 0, 1, 2, …`. The first is `τ* = arccos(−α/β)/ω₀`. By Step 3 all crossings are rightward, so the unstable-root count is nondecreasing in `τ`, starts at 0, and becomes ≥ 1 exactly at `τ*`: stability ⟺ `τ < τ*`. (At `τ = τ*` the root `iω₀` is on the axis — not stable.)

**Step 5 (case (iii)).** Let `β < −α`. At `τ = 0`: `α + β < 0`, unstable. By Step 3 the unstable-root count never decreases, so unstable for all `τ ≥ 0`. ∎

**Scope.** This is the *complete* classification for the scalar two-term equation. Multi-delay/matrix variants reduce to the same crossing-direction calculus term-by-term but the count is bookkeeping-heavy; no claim is made beyond the stated class. The classification is the mathematical backbone of the programme's delay-bifurcation screening (A021/A025 chain) and is independent of any particular application.

---

## C2 — Substitution classification — PROVEN (linear exact; nonlinear at B6's scope)

### Statement

- **Linear domain.** Let the constraint system be `Ax ≤ b` on moiety blocks with the substitution question "does a feasible allocation exist that compensates component `i`'s deficit `d_i < 0` using component `j`'s surplus `s_j > 0` through the declared linear pathway matrix `P`?" Then the question is a finite linear feasibility problem, and by **Farkas' lemma** exactly one of the following holds: (a) the allocation exists; (b) there is a dual covector `y ≥ 0` with `y^⊤A ≤ 0` on the relevant cone and `y^⊤(b + correction) < 0` — an explicit *noncompensability certificate*. The classification is exact and decidable.
- **Nonlinear domain.** With `C¹` constraints `g_k(x) ≤ 0`: **local** substitution stability holds under **MFCQ** at the contact points (the linearized feasibility persists under small perturbations), and **global** noncompensability admits a separating covector drawn from the **Clarke generalized Jacobian** of the active constraints (Farkas with `∂_C g` in place of `A`). Full proof: B6 in `04_open_problems/B_TIER_BRIDGES.md` (proved there this wave; the earlier card's "conjectural bridge" label was stale and is withdrawn).

### Proof (linear case, self-contained)

Feasibility of the substitution system `Ax ≤ b, x ∈ K` (with the deficit/surflux structure folded into `A, b`) is decided exactly by Farkas: either `∃x` with `Ax ≤ b`, or `∃y ≥ 0` with `y^⊤A = 0` and `y^⊤b < 0`. The second alternative *is* the noncompensability certificate: it exhibits the direction along which no feasible compensation exists, i.e. the deficit is structural (the moiety cannot be substituted — the noncompensation axiom's analytic form, packet B6). ∎ (Nonlinear case: see B6's file.)

---

## C3 — Aggregation closure classification — PROVED

### Statement and proof

- **Exact autonomous closure ⟺ fibre-constancy (packet B5 / R06.Lem1).** An aggregate `π : X → Y` carries a closed autonomous dynamics for the full system iff the vector field's `dπ`-image is constant on the fibres of `π` (the fibre criterion); proof is the packet's (dPF fibre-constant ⟺ projectable), re-read as the classification. Any projection violating fibre-constancy produces cross-fibre drift that no aggregate law can close.
- **Non-atomic base measure: no finite raw-moment family closes (R06.Thm3).** On a non-atomic population state `Σ`, every finite family of raw moments `μ_{k₁},…,μ_{k_m}` fails closure: the moment dynamics involve higher moments not in the family (Liouville-type strictly-increasing degree), and non-atomicity provides witnesses separating any candidate closure law. Scope-locked to the non-atomic case by the joint audit (finite/atomic counterexample below).
- **Finite/atomic positive case — the two-patch quadratic closure (NEW, proved in session).** Two patches `x₁, x₂` with `ẋ_i = x_i²` (quadratic local growth) and the equal-weight aggregation `m = (x₁+x₂)/2`, `v = ((x₁−x₂)/2)²`. Then

  ```
  ṁ = m² + v,      v̇ = 4 m v        —  EXACT two-moment closure.
  ```

  *Proof:* `ṁ = (ẋ₁+ẋ₂)/2 = (x₁²+x₂²)/2 = ((x₁+x₂)² + (x₁−x₂)²)/4 = m² + v`; and `v̇ = 2·((x₁−x₂)/2)·((ẋ₁−ẋ₂)/2) = (x₁−x₂)(x₁²−x₂²)/2 = (x₁−x₂)²(x₁+x₂)/2 = 4v·(2m)/2 = 4mv`. ∎ (Verified numerically to `1e−8` in session; the identity is exact as the algebra shows.) This is the positive existence result demarcating R06.Thm3's scope: non-atomicity, not quadraticity, is what forbids closure.
- **Approximate closure → erosion (R06.Cor4).** When fibre-constancy fails by a defect `ε`, closure holds to accuracy `ε` with the kernel claim degrading through the erosion conversion `(L_G c + C)ε ≤ α` — the lifting-typed corollary proved in R06.

---

## C4 — Diagnostic classification — PROVED

### C4.1 — Separation ⟺ soundness

**Statement.** A diagnostic margin functional `M : X → ℝ ∪ {±∞}` is **sound** for the nonviability judgment (whenever `M(x) < 0`, `x` lies outside the viability kernel `Viab`) **iff** `{M < 0} ∩ Viab = ∅`.

**Proof.** Both directions are the definition of soundness unfolded over the kernel: soundness says every state with `M(x) < 0` is a nonviability certificate, i.e. `{M < 0} ⊆ X ∖ Viab`, which is precisely the separation. The theorem's content is the *reformulation*: it converts the proof obligation on `M` (a statement about all `x`) into a *geometric separation check* between two computable/estimable sets — and the R03 trichotomy then classifies which diagnostics admit the check. ∎

### C4.2 — Uniform-horizon theorem

**Statement.** Let `R_n` be the `n`-review predecessor sets (`R_0 = K`, `R_{n+1} = Pre(R_n)`) with `R_n` closed and `R_{n+1} ⊆ R_n` (Hausdorff-continuous successors, compact `X`). Let `C ⊆ X` be compact with `C ∩ R_∞ = ∅` (`R_∞ = ⋂ R_n` the certified kernel). Then there exists `N < ∞` with `C ∩ R_N = ∅`: every state of `C` is certified nonviable at a **uniform** finite horizon.

**Proof.** `X ∖ R_n` is increasing in `n` (since `R_n` decreases) and open (each `R_n` closed). For `x ∈ C`: `x ∉ R_∞ = ⋂ R_n`, so some `n(x)` has `x ∈ X ∖ R_{n(x)}`; hence `C ⊆ ⋃_n (X ∖ R_n)`, an increasing open cover of the compact `C`. Extract a finite subcover; by monotonicity of the cover it is `X ∖ R_N` for `N = max` of the finitely many indices. Then `C ∩ R_N = ∅`. ∎

**Remark (rate vs horizon).** The theorem gives a uniform *horizon* `N`; it does **not** give a uniform *rate* of margin decay, and no claim of diverging exit times is made (an earlier session draft claimed an unproven diverging-exit-time witness; it was withdrawn after verification — recorded in the worklog).

### C6.3 — Delayed-revelation lemma

**Statement.** Let the observation reveal a hidden parameter/disturbance exactly at time `t_d` (before `t_d`, only a prior is observed; after, the full state). The delayed information is **inert** (the delayed-observation kernel equals the full-information kernel) **iff** the viability obstruction is unreachable before `t_d` — precisely: iff no trajectory starting in the kernel can hit the obstruction set `X ∖ K` before `t_d` under *any* policy admissible for the prior.

**Proof.** (⟸) Assume the obstruction is unreached before `t_d` (the buffer condition: `dist(x(t), X ∖ K) > 0` on `[0, t_d)` along all prior-admissible kernel trajectories — equivalently the `t_d`-truncated kernel equals the full kernel on the truncation). Construct the delayed policy: run any safe prior-admissible policy on `[0, t_d)` (inert by hypothesis), then switch to the full-information optimal policy revealed at `t_d`. The concatenation is causal (it uses only available information on each interval) and achieves the full-information kernel; hence the delayed kernel ⊇ full kernel, and ⊇ is trivial. (⟹) If some prior-admissible trajectory reaches the obstruction before `t_d`, the uninformed policy must hedge against all revelations on `[0, t_d)`, and the R02.Prop3 construction (quantized observation with the buffer threshold `t = 3` in that witness) exhibits a strictly smaller delayed kernel. ∎

---

## C5 — Bifurcation classification — PROVED (at B7's declared scope)

Both extremal witnesses and the transversality classification theorem are **proved in B7** (`04_open_problems/B_TIER_BRIDGES.md`): no-bifurcation + continuous boundary ⟹ no kernel change (Hausdorff-continuity of the kernel in the data); transversal contact ⟹ kernel change; genericity of the non-degenerate strata via jet-transversality. The card's "PARTIAL" label was the pre-B7 status and is withdrawn. The residual beyond B7's scope (kernels under *non-generic* simultaneous contact families) remains open and is registered.

---

## C6 — Information/implementation classifications — PROVED (C6.1, C6.2 packet-level; C6.3 above)

- **C6.1 (refinement monotonicity):** observing more is never worse for the kernel, *iff* the typed-lift hypotheses of the packet's information records hold (the refinement lifts to the information block without disturbing the policy class). The failure witness without the lift hypothesis is R02.Prop3's coarsening.
- **C6.2 (implementation enlargement):** enlarging the realized-action set is never worse on *all branches* — the all-branches quantifier is what makes it monotone; the fixed-policy reading is non-monotone (R08's converse family).
- **C6.3:** proved above.

---

## Status

- **C1: PROVEN** (complete classification, full proof above).
- **C2: PROVEN** (linear exact, self-contained above; nonlinear at B6's proved scope, cross-referenced).
- **C3: PROVED** (fibre criterion packet-proved; non-atomic theorem in R06; two-atom closure proved above with exact algebra; approximate closure in R06.Cor4).
- **C4.1, C4.2: PROVEN** (full proofs above). **C4.3 rate-vs-horizon:** separation proved, rate claims withdrawn (honest boundary).
- **C5: PROVED at B7's declared scope** (cross-referenced; genericity strata residual open).
- **C6: PROVED** (C6.1/C6.2 packet-level with typed-lift hypotheses; C6.3 full proof above).

**Dependencies:** packet B5/B6/B7; R02.Prop3, R03 (trichotomy, Lem4), R06 (Lem1, Thm3, Cor4), B6, B7. **Consumers:** Paper 2 (theorem atlas), the delay-bifurcation screening in Paper 4's chain, C-a (the classification language feeds the decidability theorem's kernel-type enumeration).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.
