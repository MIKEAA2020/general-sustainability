# Result Record R05 — Docket T5: Tubular Assume–Guarantee Composition with a Gain Operator and Feasibility Fixed Point

## Field 1 — Result ID and target docket item

`R05` (R05.Thm1 contract-amplitude composition [Version A]; R05.Thm2 eroded composition with state-dependent contracts [Version B]; R05.Cor3 linear gain feasibility and small-gain condition; R05.Ex4 coupling-collapse counterexample; R05.Open5 the precise open problem). Target: **T5** ("useful assume–guarantee or nonlinear small-gain theorem allowing state-dependent interface contracts without hiding shared controls or nonconvex implementation").

## Field 2 — Verdict

**Partially closed by new restricted theorems; the general nonlinear small-gain problem remains genuinely open** (precise statement with all missing hypotheses in Field 16 / R05.Open5). Version A and Version B are proved completely; the docket's acceptance elements are delivered: a true gain operator (the normalized interface-tightening matrix `Γ`), a true fixed point (the maximal feasible erosion vector `r* = A⁻¹b`, computable by a contraction iteration), a counterexample outside the hypotheses (the coupling-collapse witness), and no insertion of nonlinear functions into numerical matrices (gains are declared Lipschitz constants of the true interface maps, never matrix-ized dynamics).

## Field 3 — Exact statement

### Data

`N` modules. Module `i`: state `x_i ∈ ℝ^{n_i}`; closed safe set `Q_i` with two-sided tubular radius `ρ_i > 0` and `C^{1,1}` signed distance in the tube (the erosion-lemma geometry of corrected `02` Lemma 2, including normal correspondence between `∂Q_i^{−r}` and `∂Q_i`). Coupled dynamics:

```
ẋ_i ∈ F_i(x_i, z_i(x), d_i) + Δ_i B,   z_i(x) = (z_ij(x_j))_{j≠i},  d_i ∈ D_i,
```

with interface maps `z_ij` defined and Lipschitz on the `ρ_j`-tube of `Q_j`; exogenous error budgets `Δ_i ≥ 0`; compact disturbance sets `D_i`. Fix nominal interface values `ẑ_ij` and define the **contract amplitudes**

```
δ_ij(r) := sup{ ‖z_ij(x_j) − ẑ_ij‖ : x_j ∈ Q_j^{−r} },   0 ≤ r < ρ_j
```

(the guarantee module `j` offers at erosion depth `r`). Let `G_i(x_i) := clco{F_i(x_i, ẑ_i, d_i) : d_i ∈ D_i}` be the nominal envelope.

**Hypotheses.**

- **(H1)** Each `G_i` has nonempty compact convex values, is locally Hausdorff-Lipschitz near `Q_i` with constant `L_i`, and has linear growth (forward completeness).
- **(H2)** *Boundary margin:* for every `x_i ∈ ∂Q_i` and `ζ ∈ N^P_{Q_i}(x_i)`: `sup_{v ∈ G_i(x_i)} ⟨ζ, v⟩ ≤ −α_i‖ζ‖` with `α_i > 0`.
- **(H3)** *Interface sensitivity:* `‖F_i(x_i, z, d) − F_i(x_i, z′, d)‖ ≤ Λ_i‖z − z′‖` for all `d ∈ D_i`, uniformly on the tube of `Q_i`.
- **(H4)** The joint closed-loop envelope `G(x) := clco{ (v_i)_i : v_i ∈ F_i(x_i, z_i(x), d_i) }` satisfies the strong-invariance regularity (compact convex values, local Hausdorff-Lipschitz on a neighborhood of `Π_i Q_i`, growth) — automatic if `F_i` is jointly Lipschitz in `(x_i, z)` and each `z_ij` is Lipschitz.

### R05.Thm1 (Version A — contract-amplitude composition)

*If for every `i`*

```
Λ_i Σ_{j≠i} δ_ij(0) + Δ_i ≤ α_i,
```

*then `Q := Π_i Q_i` is strongly invariant for the coupled system: every solution starting in `Q` remains in `Q` for all forward time, under every disturbance realization. Each module's boundary margin absorbs the worst-case in-contract interface variation of its partners.*

### R05.Thm2 (Version B — eroded composition with state-dependent contracts)

*If there exists an erosion vector `r ∈ Π_i [0, ρ_i)` such that for every `i`*

```
L_i r_i + Λ_i Σ_{j≠i} δ_ij(r_j) + Δ_i ≤ α_i,
```

*then `Q^r := Π_i Q_i^{−r_i}` is strongly invariant for the coupled system. The condition is a genuine assume–guarantee loop: module `i`'s admissible erosion `r_i` both consumes its own margin (term `L_i r_i`) and tightens the contracts it can guarantee its partners (`δ_ij(r_j)` decreasing in `r_j` — state-dependent interface contracts).*

### R05.Cor3 (linear gain feasibility — the small-gain condition)

Assume the **linear tightening bounds** `δ_ij(r) ≤ δ_ij(0) − σ_ij r` with `σ_ij ≥ 0` (contract tightens at rate `σ_ij` as module `j` retreats into its safe set). Define

```
b_i := α_i − Δ_i − Λ_i Σ_{j≠i} δ_ij(0)   (base budgets),
A := diag(L_i) − M,   M_ij := Λ_i σ_ij (i ≠ j),  M_ii := 0,
Γ := diag(L_i)^{-1} M   (the gain operator).
```

Then:

1. **(Fixed point / feasibility.)** If `ρ(Γ) < 1` (spectral radius — the *small-gain condition*), then `A⁻¹ = Σ_{k≥0} Γ^k diag(L)^{-1} ≥ 0`, the erosion fixed-point iteration `r^{(k+1)} := diag(L)^{-1}(b + M r^{(k)})` converges monotonically upward to `r* := A⁻¹b` from `r^{(0)} = 0`, and the feasibility condition of Thm2 (without the tubular cap) holds **iff** `A⁻¹b ≥ 0`; `r*` is the componentwise-maximal feasible erosion vector.
2. **(Certification.)** The composition is certified by Thm2 whenever `ρ(Γ) < 1`, `A⁻¹b ≥ 0`, and `A⁻¹b < ρ` componentwise (take `r = r*`). If `A⁻¹b ≥ ρ` in some component, certification requires solving the capped feasibility (a finite linear program); if `A⁻¹b ≱ 0`, no feasible erosion exists and the composition is refused.
3. **(Two modules, explicit.)** For `N = 2`: `ρ(Γ) < 1` ⟺ `Λ_1σ_12 · Λ_2σ_21 < L_1 L_2` (the classical small-gain product), and `A⁻¹b ≥ 0` ⟺

```
L_2 b_1 + Λ_1 σ_12 b_2 ≥ 0    and    Λ_2 σ_21 b_1 + L_1 b_2 ≥ 0
```

*(budget tradeoff: one module's deficit must be coverable by the partner's slack through the gain path). Version A is the special case `b ≥ 0` (no erosion needed). If both budgets are negative, no `r ≥ 0` is feasible — the loop cannot be closed at any depth.*

### R05.Ex4 (coupling-collapse counterexample — outside the hypotheses)

The positive linear system `ẋ_1 = −a_1x_1 + c_1x_2`, `ẋ_2 = −a_2x_2 + c_2x_1`, `x ≥ 0`, with boxes `Q_i = [0, k_i]` and `c_1c_2 > a_1a_2`: each isolated module (`c_i = 0`) has the full box as its viability kernel (decay to 0), but the coupled kernel of `Q_1 × Q_2` is exactly `{(0,0)}` — every other nonnegative initial condition grows along the positive Perron eigenvector and exits any bounded box in finite time. The gain product `c_1c_2 > a_1a_2` is precisely the violation of Cor3's small-gain condition (with `z_ij = x_j`, `σ_ij = 1`, `Λ_i = c_i`, `L_i = a_i`, `δ_ij(r) = k_j/2 − r`), and the theorem correctly refuses certification at every erosion depth (the required depths exceed the tubular radii). Factorwise safety is destroyed by the interface loop — composition without a gain condition is unsound.

## Field 4 — State and phase space

Product phase space `Π_i ℝ^{n_i}` (finite-dimensional ODE/differential-inclusion class); safe sets closed with tubular geometry; no delay, no events, no information state (deterministic full-state strong invariance — the weakest and cleanest class for a first composition theorem beyond corrected `03`).

## Field 5 — Quantifier order and information pattern

All-solutions strong invariance: `∀x(0) ∈ Q^r ∀d(·) ∀solutions: x(t) ∈ Q^r ∀t ≥ 0`. One implicit feedback per module is allowed inside `F_i` (folded into the envelope); no disturbance-observing structure is assumed or needed. The assume–guarantee quantifier structure is *static* (contract bounds), not strategic: module `j`'s guarantee is a set bound on `z_ij`, never a policy.

## Field 6 — Assumptions, including existence/completeness

(H1)–(H4) as in Field 3; solutions of the joint inclusion exist (Filippov under (H4)) and are forward complete (growth in H1). The tubular/`C^{1,1}` geometry excludes arbitrary closed sets — the packet's `⋃_j[2j,2j+1]` counterexample (corrected `02`) remains controlling: without tubular regularity there is no uniform erosion calculus at all, hence no Version B.

## Field 7 — Mapping type

`EXACT_SPECIALIZATION` of the erosion lemma (corrected `02`) to product geometry, composed with the proximal-normal product calculus of corrected `03` — a genuine extension of the packet's composition toolkit from *joint shared-control feasibility* (corrected `03`) to *interface-contract composition*; Ex4 is `COUNTEREXAMPLE_OR_LIMIT`.

## Field 8 — Self-contained proof

### Proof of R05.Thm1

Let `x ∈ ∂Q` and `ζ ∈ N^P_Q(x)`. For finite products, `N^P_Q(x) = Π_i N^P_{Q_i}(x_i)` (the product formula already used by corrected `03` §2's proof). If `x_j ∈ int Q_j` then `N^P_{Q_j}(x_j) = {0}` (a ball around an interior point lies in `Q_j`), so `ζ` has nonzero components only on the active set `A(x) = {i : x_i ∈ ∂Q_i} ≠ ∅`.

For `i ∈ A(x)` and a realized velocity `v_i ∈ F_i(x_i, z_i(x), d_i) + Δ_iB`: since `x_j ∈ Q_j` for every `j` (as `x ∈ Q`), `‖z_ij(x_j) − ẑ_ij‖ ≤ δ_ij(0)`, hence `‖z_i(x) − ẑ_i‖ ≤ Σ_{j≠i} δ_ij(0)` (declared norm convention; any equivalent norm changes only constants). By (H3) there is `w_i ∈ F_i(x_i, ẑ_i, d_i)` with `‖v_i − w_i − e_i‖ = 0` for some `‖e_i‖ ≤ Δ_i`, so `v_i ∈ G_i(x_i) + (Λ_i Σ_{j≠i} δ_ij(0) + Δ_i)B`. Using (H2) (homogeneous form on the proximal-normal cone):

```
⟨ζ_i, v_i⟩ ≤ sup_{G_i(x_i)}⟨ζ_i, ·⟩ + (Λ_i Σ_{j≠i} δ_ij(0) + Δ_i)‖ζ_i‖ ≤ (−α_i + Λ_i Σ_j δ_ij(0) + Δ_i)‖ζ_i‖ ≤ 0.
```

Inactive blocks contribute `⟨ζ_j, v_j⟩ = 0`. Therefore `sup_{v ∈ G(x)} ⟨ζ, v⟩ = Σ_{i∈A} sup ⟨ζ_i, ·⟩ ≤ 0` (the inequality is preserved by closure and convexification). The proximal-normal strong-invariance criterion with (H1)/(H4) regularity yields strong invariance of `Q` (the same lemma corrected `02` Theorem 1 and corrected `03` §2 invoke). ∎

### Proof of R05.Thm2

Let `x ∈ ∂Q^r`, `ζ ∈ N^P_{Q^r}(x) = Π_i N^P_{Q_i^{−r_i}}(x_i)`, active set `A(x) = {i : x_i ∈ ∂Q_i^{−r_i}}`. For `i ∈ A(x)`: let `p_i ∈ ∂Q_i` be the corresponding boundary point with common unit normal `n_i` (the tubular normal correspondence, corrected `02` Lemma 2 hypothesis), so `‖x_i − p_i‖ = r_i` and `ζ_i` is a nonnegative multiple of `n_i` on the regular part (and a proximal limit thereof generally — the inequality argument below is applied to proximal normals directly, exactly as in corrected `02` Lemma 2's proof). For a realized velocity `v_i ∈ F_i(x_i, z_i(x), d_i) + Δ_iB`:

- since `x_j ∈ Q_j^{−r_j}` for all `j` (as `x ∈ Q^r`), `‖z_ij(x_j) − ẑ_ij‖ ≤ δ_ij(r_j)`;
- by (H3) and the envelope definition, `v_i ∈ G_i(x_i) + (Λ_i Σ_{j≠i} δ_ij(r_j) + Δ_i)B`;
- by (H1)'s Lipschitz property, `sup_{G_i(x_i)}⟨n_i, ·⟩ ≤ sup_{G_i(p_i)}⟨n_i, ·⟩ + L_i‖x_i − p_i‖ ≤ −α_i + L_i r_i` (the erosion computation of corrected `02` Lemma 2, clause-level match).

Combining:

```
⟨ζ_i, v_i⟩ ≤ ‖ζ_i‖ ( −α_i + L_i r_i + Λ_i Σ_{j≠i} δ_ij(r_j) + Δ_i ) ≤ 0
```

by the feasibility hypothesis of Thm2. Inactive blocks contribute zero. Convexification preserves the inequality; the strong-invariance criterion gives strong invariance of `Q^r`. ∎

### Proof of R05.Cor3

*Part 1.* `Γ ≥ 0` entrywise. `ρ(Γ) < 1` implies the Neumann series `Σ_{k≥0}Γ^k` converges, is entrywise `≥ 0`, and equals `(I − Γ)^{-1}`. Since `A = diag(L)(I − Γ)`:

```
A⁻¹ = (I − Γ)^{-1} diag(L)^{-1} = Σ_{k≥0} Γ^k diag(L)^{-1} ≥ 0.
```

The fixed-point map is `Φ(r) := diag(L)^{-1}(b + Mr) = Γr + diag(L)^{-1}b`. From `r^{(0)} = 0`: `Φ^k(0) = Σ_{m<k} Γ^m diag(L)^{-1}b`, which is entrywise nondecreasing in `k` (each summand `Γ^m diag(L)^{-1}b ≥ 0`) and converges to `Σ_{m≥0}Γ^m diag(L)^{-1}b = A⁻¹b = r*`. (For general `b` with negative components the iterates still converge to `r*` by the contraction property of `Φ`; monotonicity holds whenever `diag(L)^{-1}b ≥ 0`.)

*Feasibility equivalence (uncapped).* If `r ≥ 0` and `Ar ≤ b`, multiplying by `A⁻¹ ≥ 0` (order-preserving since entrywise nonnegative) gives `r ≤ A⁻¹b`, hence `A⁻¹b ≥ 0`. Conversely, if `A⁻¹b ≥ 0`, take `r* := A⁻¹b`: then `Ar* = b ≤ b`, so `r*` is feasible. Hence `{r ≥ 0 : Ar ≤ b} ≠ ∅ ⟺ A⁻¹b ≥ 0`, and every feasible `r` satisfies `r ≤ r*`: `r*` is the componentwise-maximal feasible erosion vector.

*Part 2.* Immediate from Part 1 with the cap `r* < ρ` (any feasible `r ≤ r*` can be used if it fits; if `r*` exceeds the cap, feasibility of the capped system is a finite linear program — exact but not closed-form).

*Part 3.* `N = 2`: `A = [[L_1, −Λ_1σ_12], [−Λ_2σ_21, L_2]]`; `ρ(Γ) < 1` with `Γ = [[0, Λ_1σ_12/L_1],[Λ_2σ_21/L_2, 0]]` gives `ρ(Γ)² = (Λ_1σ_12Λ_2σ_21)/(L_1L_2) < 1`, the stated product. `det A = L_1L_2 − Λ_1σ_12Λ_2σ_21 > 0`, so `A⁻¹ = (1/det A)[[L_2, Λ_1σ_12],[Λ_2σ_21, L_1]] ≥ 0` and `A⁻¹b ≥ 0` expands to the two stated tradeoff inequalities. If `b_1 < 0` and `b_2 < 0` then `L_2b_1 + Λ_1σ_12b_2 < 0` and `Λ_2σ_21b_1 + L_1b_2 < 0`: both fail — no feasible `r ≥ 0` exists (directly: at `r = 0` both constraints are violated, and each constraint can only be repaired by the *other* variable, which is itself blocked). ∎

### Verification of R05.Ex4

Isolated modules: `ẋ_i = −a_ix_i` decays inside `[0,k_i]` — full box viable. Coupled with `c_1c_2 > a_1a_2`: the Metzler matrix has a real eigenvalue `λ_+ > 0` with positive right and left eigenvectors `v, w > 0`; for every `x_0 ≥ 0, x_0 ≠ 0`, `⟨w, x_0⟩ > 0` and `x(t) ≥ e^{λ_+ t}⟨w,x_0⟩v/‖v‖·v − (lower modes)` grows unboundedly along `v`, hence exits the bounded box in finite time; `(0,0)` alone is an equilibrium. Kernel of the box under the coupled (uncontrolled) dynamics: `{0}`. Certificate side: `z_ij(x_j) = x_j` gives `δ_ij(r) = k_j/2 − r` (nominal `ẑ_ij = k_j/2`), `σ_ij = 1`, `Λ_i = c_i`, `L_i = a_i`, `α_i = a_ik_i − c_ik_j/2` (requires the nominal to be contracting — if even the nominal escapes, `b_i < −α_i`-type failure is immediate), `b_i = a_ik_i − c_ik_j`. `c_1c_2 > a_1a_2` violates the product condition; in the symmetric case `a_i = a, c_i = c > a, k_i = k` the feasibility inequality `(a−c)r ≤ (a−c)k` requires `r ≥ k > ρ = k/2`: refused at every admissible depth, matching the true collapse. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Ex4 (gain loop) and the packet's shared-control infeasibility witness (corrected `03` §1: `u ≥ 1/2` vs `u ≤ −1/2` with empty intersection at the origin) are the two boundary witnesses — one for interface-gain failure, one for shared-control failure; both must be excluded by hypothesis, and they fail for different reasons (gain product vs. joint feasibility), which is why `TCS-1.0` §5's composition gate needs both theorems (CIRC-2). Outside scope additionally: nonconvex implementation (envelope convexification is a relaxation — realized trajectories are envelope solutions, but relaxation *exactness* is not claimed, per corrected `03` §7); non-tubular safe sets (no uniform erosion calculus — corrected `02`'s `⋃_j[2j,2j+1]` witness); delay/events (no claims).

## Field 10 — Interface producer/consumer contract

- **Producer:** the assume–guarantee certificate: per module `(α_i, L_i, Λ_i, Δ_i, ρ_i)`, per interface `(δ_ij(·), σ_ij)`, plus the computed `(r*, Γ, ρ(Γ))` and the verdict.
- **Consumers:** R06 (scale composition: moment-closure approximations enter as `Δ`-budgets); the A023 spatial branch and polycentric composition docket (each spatial/jurisdictional interface must export `(z_ij, δ_ij, σ_ij)` records); Paper 2 (theorem + counterexample); the monograph composition chapter.
- **Failure condition:** certificate revoked if any exported constant is invalidated (e.g., a module's `α_i` recomputed after a model-version change — version identity axiom 7); using `Γ` entries as *dynamics* rather than Lipschitz constants violates the docket's "no nonlinear functions inserted into a numerical matrix without reduction" and is reviewer-rejectable.

## Field 11 — Error, horizon, and safety erosion for approximations

The erosion triple is intrinsic: error budgets `Δ_i` (exogenous) and `Λ_iδ_ij(r_j)` (interface), erosion depths `r_i`, margins `α_i`, horizons infinite (strong invariance), tubular caps `ρ_i`. Approximate contracts (interface bounds known only up to `ε`) add `ε` to every `δ_ij(0)` — i.e. to the `b` vector — shrinking `r*` accordingly; the feasibility condition converts contract uncertainty into depth, exactly the erosion discipline the schema's GAP-3 proposes to type.

## Field 12 — Selector and implementation regularity

No selector is needed: strong invariance is a statement about *all* trajectories of the coupled inclusion; the per-module feedback (if any) is inside `F_i` and its regularity is carried by (H1)/(H4) — the corrected `02` caution (measurable selection is not Lipschitz implementation) applies unchanged: a module claiming an implemented feedback must verify the envelope contains it.

## Field 13 — Stochastic/hybrid/RFDE qualifications

Deterministic ODE inclusion class only. Hybrid resets void the tubular argument across events (reset preservation would need a jump-margin analogue — open); RFDE histories replace `x_j` by `x_{j,t}` with `δ_ij` defined on history sets — the translated-history closure of corrected `08` would be required (not done here); stochastic versions are chance-level statements needing QF-2 support alignment (not claimed).

## Field 14 — Novelty status with exact references

Internal: extends corrected `03` from shared-control joint feasibility to interface-contract composition with erosion — no packet record does this; the docket's acceptance items (gain operator, fixed point, counterexample) are all present. External: small-gain theorems with gain operators and spectral-radius conditions are classical in robust control and ISS theory, and tubular/erosion arguments are standard in strong-invariance theory; **the specific packaging — contract amplitudes as interface suprema over eroded sets, feasibility as a linear system whose M-matrix property is the small-gain condition, and the maximal feasible erosion vector as the fixed point — requires external literature matching that this packet cannot provide** (self-containment report caveat). No bibliographic novelty claim is made; the verdict "restricted new theorem, classical skeleton" is the honest status.

## Field 15 — Publication destination

Paper 2 (abstract composition section: Thm1, Thm2, Cor3 with proofs; Ex4 beside corrected `03`'s counterexamples); monograph composition chapter; conditional docket for the nonlinear extension.

## Field 16 — Remaining obligations and revocation triggers

**R05.Open5 (the precise open problem — nonlinear small-gain with nonconvex implementation and shared controls).** Statement target: an assume–guarantee theorem for `N` modules with (a) *nonlinear* gain operators `Γ_ij(r)` (nonlinear tightening functions, not linearized `σ_ij`), (b) set-valued nonconvex implementation correspondences inside `F_i`, (c) genuinely shared control channels (corrected `03`'s joint-feasibility clause), (d) non-tubular or nonsmooth safe sets. Missing hypotheses that any proof must supply: (i) a nonlinear fixed-point/contraction condition replacing `ρ(Γ) < 1` (candidate: a gain-loop composition condition in the sense of nonlinear small-gain theory — the external literature check of Field 14 is prerequisite); (ii) a relaxation-exactness or trajectory-level substitute for envelope convexification under nonconvex `𝖨`; (iii) an erosion calculus for the declared set geometry (or a proof that tubular geometry is necessary — the `⋃[2j,2j+1]` witness suggests it is); (iv) joint feasibility of shared channels integrated with the contract loop (merging corrected `03`'s `R(x) ≠ ∅` clause with the gain condition — no published-in-packet proof exists). Other obligations: external novelty audit; instantiation of the certificate constants on one application pair (candidate: A023 spatial interface). Revocation triggers: invalidation of any exported constant (Field 10); discovery of an external theorem covering Version B in full (demotes to classical).

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R05",
  "target": "T5",
  "depends_on": [
    "corrected_theorems/02_operator_I_strong_invariance_and_erosion.md (Theorem 1 pattern, Lemma 2 erosion computation, error conversion)",
    "corrected_theorems/03_restricted_composition.md (product proximal-normal calculus, shared-control counterexample, relaxation-exactness caveat)"
  ],
  "unblocks": ["R06 (Δ-budgets for approximate aggregation)", "A023 spatial branch", "polycentric composition docket", "TCS-1.1 composition-gate enumeration (CIRC-2)"],
  "status": {"R05.Thm1": "proved", "R05.Thm2": "proved", "R05.Cor3": "proved", "R05.Ex4": "proved counterexample", "R05.Open5": "open (hypotheses enumerated)"},
  "mapping_type": "EXACT_SPECIALIZATION + COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "restricted new theorem on classical skeleton; external check outstanding"
}
```
