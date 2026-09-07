# Verification of the Notation/Units Review and the Two Mathematical Claims

This document records what I actually checked rather than accepted, and the outcome of each check. It is
written for the manuscript author (v31) and covers (A) the six notation/unit clarifications and (B) the
reviewer's two mathematical claims. Section/equation numbers refer to `IMPLEMENTED_revision_ECOMOD_v31.md`.

Every numeric or analytic claim below was recomputed from the model equations in `model_sims/char_eq.py`
(which reproduces the manuscript's Eq. (1)–(9) and the characteristic equation) and from the parameter set
`b₀ = 0.5, b_G = 0.8, ρ = 0.05, A_max = 1.2, e = 0.55, r = 0.02`, with an interior equilibrium `A* = 0.8`.

---

## Part A — The six notation/unit items

All six were adopted; the following states the point and the change made.

1. **`σ` defined explicitly.** Added a "Notation and conventions" paragraph in §2.2: `σ` is a dimensionless
   fraction, `0 ≤ σ ≤ 1`, the human-available share of the flow. `σ = 1` means the entire flow yield `bA`
   may be harvested without stock damage; `σ < 1` reserves a share and is set with the population cap so
   that `E ≤ σ·B` (Half-Earth / reservation, §9). `σ b A(t)` is the safe flow harvest; only
   `[E(t) − σ b A(t)]₊` draws down stock. Added a **`σ` row to the SI symbol table** (§S1.2).
2. **`b_G` role and units made explicit.** `b_G` is the value of one hectare of standing stock,
   `gha·ha⁻¹` — a **book-conversion rate, not a yield**, and therefore **not dimensionless**. In (2) the
   capital-growth term `b_G G(A)` has units `gha·ha⁻¹ · ha·yr⁻¹ = gha·yr⁻¹`, matching `bA`; in (4)
   dividing the overshoot flow by `b_G` yields a **stock-loss rate** in `ha·yr⁻¹`, so `1/b_G = γ = 1/V`
   (the harvest coefficient / salvage value) as in §4.1.
3. **What debt degrades.** Made explicit that Eq. (8) degrades **only the flow-yield coefficient `b`**
   (via `e^{−αD}`), not `b_G`, `ρ`, or `A_max`. This is Assumption (8) and a deliberate scope keeping the
   degradation channel (flow productivity) separate from the regeneration channel (rate and ceiling).
   Stated so the reader is not misled that debt erodes the stock or the regeneration rate. A debt
   dependence on `G(A)`/`b_G` is a separately-argued extension, not implied.
4. **Positive-part notation.** `[x]₊ = max(x, 0)` is now defined in the "Notation and conventions"
   paragraph of §2.2, alongside the equations, rather than only appearing inline.
5. **Delay structure stated explicitly.** Added a "Delay structure" note: regeneration delayed (`τ_g`),
   population response delayed (`τ_p`), debt formation and harvest on current values.
6. **`K` is not delayed.** Added explicitly: `K = B/e` is algebraic and computed from the current state;
   the delay enters only through the population's response to a delayed *value* of it, `K(t−τ_p)`.

---

## Part B — The two mathematical claims

### B.1 "The equilibrium family `P = B(A)/e` holds only if `σ = 1`"

**Verdict: CORRECT — confirmed analytically and numerically.** This is the reviewer's strongest point and a
genuine gap that is now stated.

From `dP/dt = 0`, `P* = K(A*) = B(A*)/e`. Imposing `dA/dt = 0` on the family in the deficit region, with
`E* = eP* = B(A*)`:

```
G(A*) = [E* − σ b A*]₊ / b_G
      = [(1−σ) b A* + b_G G(A*)]₊ / b_G
      = G(A*) + (1−σ) b A* / b_G
```

which is satisfied for arbitrary interior `A*` **only if `σ = 1`**. For `σ < 1`, `(1−σ)bA*/b_G > 0` for
`A* > 0`, so no interior equilibrium exists on the family `P = B(A)/e`.

**Numeric confirmation** (`dA/dt` at `P = B/e`; equilibrium locus `P* = (σbA + b_G G(A))/e`):

| `σ` | `A*` | `P*` (true equilibrium) | `P = B/e` | `dA/dt` at `P = B/e` |
|---|---:|---:|---:|---:|
| 1.00 | 0.80 | 0.7467 | 0.7467 | 0.0000 |
| 0.90 | 0.80 | 0.6739 | 0.7467 | −0.0500 |
| 0.70 | 0.80 | 0.5285 | 0.7467 | −0.1500 |
| 0.50 | 0.80 | 0.3830 | 0.7467 | −0.2500 |

At `σ = 1`, `dA/dt = 0` at every `A*`; at `σ < 1`, `dA/dt(P = B/e) < 0` for every interior `A*`, and the
equilibrium locus is `(σbA + b_G G(A))/e`, which is `B/e` minus `(1−σ)bA/e`.

**Change made:** §2.2 notation, §4.3, §5, §6, §8, the Comparison table, and SI §S3.3 now state that the
one-parameter family and the neutral continuum are derived under **full harvest `σ = 1`**, and that a
reservation `σ < 1` shifts the locus to `P = (σbA + b_G G(A))/e < B/e`.

### B.2 "A positive real eigenvalue for every delay is not guaranteed"

**Verdict: CORRECT as a caution, but the claim is TRUE for the representative parameter set — it just needs
its sufficient condition stated rather than implied.** The reviewer is right that it is not a
*parameter-free* theorem; we verified the precise condition under which it holds.

Linearising (4)+(5) at an interior point of the family gives the two-delay characteristic equation
`D(s;τ_g,τ_p) = (s − a₁e^{−sτ_g} − a₃)(s + r) − a_E a₄ e^{−sτ_p} = 0`, with `a₁ = G′(A*)`, `a₃ = b/b_G`,
`a_E = −e/b_G`, `a₄ = r K′(A*)`. The equilibrium condition `P* = K(A*)` gives `−a_E a₄ = r·S` with
`S = a₁ + a₃ = G′(A*) + b/b_G`. Then:

- **Zero eigenvalue:** `D(0) = 0` on the whole family (neutral continuum) — no isolated interior attractor.
- **Zero-delay root:** with `τ_g = τ_p = 0`, `D(λ) = λ(λ + r − S)`, so the non-neutral root is
  `λ = S − r`. A positive real root at zero delay exists **iff `S > r`**, i.e. `G′(A*) + b/b_G > r`.
- **Persistence for every delay:** the root persists provided `F′(0) = r − S + r a₁ τ_g − r S τ_p < 0`
  (then `F(0) = 0`, `F′(0) < 0`, and `F(λ) → ∞` force a positive real root). At the representative
  parameter set (`a₁ = G′(0.8) = −0.0167`, `S = 0.6083`, `r = 0.02`) and `S > r`, this holds over the
  **entire** `(τ_g, τ_p) ∈ [0,400]²` plane: `max F′(0) = −0.5883` (attained at `τ_g = τ_p = 0`).

**Numeric confirmation:**

- Leading real eigenvalue over the delay plane (`A* = 0.8`), real-axis roots:

  | `τ_p` | `τ_g = 0` | 5 | 18 | 30 | 60 | 120 | 200 |
  |:--|---:|---:|---:|---:|---:|---:|---:|
  | 0 | 0.588 | 0.605 | 0.606 | 0.606 | 0.606 | 0.606 | 0.606 |
  | 10 | 0.608 | 0.624 | 0.625 | 0.625 | 0.625 | 0.625 | 0.625 |
  | 25 | 0.608 | 0.624 | 0.625 | 0.625 | 0.625 | 0.625 | 0.625 |
  | 60 | 0.608 | 0.624 | 0.625 | 0.625 | 0.625 | 0.625 | 0.625 |

  The leading eigenvalue is positive and essentially constant (≈ +0.625) across the plane — no Hopf.
- **Full spectrum** at representative delay pairs: leading eigenvalue real `+0.6250` for
  `(τ_g,τ_p) ∈ {(0,0),(10,25),(30,25),(85.4,25),(30,231),(231,25),(200,200),(60,100),(80,120)}`, with
  zero purely imaginary-axis crossings.
- **Exact crossing curves** (`s = iω`, Hale–Huang / Gu–Niculescu–Chen): the `s = iω` scan returns
  **0** crossing points over `ω ∈ [0.05,1.0]`, `τ_g ∈ [0,300]`, three `2π/ω` branches — i.e. no
  imaginary-axis crossing (no Hopf) in the scanned range.

**Change made:** the "positive real eigenvalue for every delay" claim is now stated with its sufficient
condition — `S = b/b_G + G′(A*) > r` (and the delay condition `F′(0) < 0`) — and is explicitly flagged as
**conditional, not parameter-free** (§4.3, §5, §6 prediction 1, §8, the Comparison table, and SI §S3.4).
The abstract now reads "for the representative parameter set … provided `b/b_G + G′(A*) > r`."

---

## Bottom line

- The reviewer's **equilibrium-family/`σ = 1`** point is **correct** and was a genuine omission — now fixed.
- The reviewer's **"not guaranteed for every delay"** point is **correct as a qualification**; the claim
  **is true for the representative parameter set**, and the sufficient condition is now stated explicitly.
- The **six notation/unit items** were all valid and are all incorporated (main text §2.2 and §4.3, plus the
  SI symbol table §S1.2 and §S3.3/§S3.4).

No claim was accepted on face value; every one was checked against the model equations and recomputed.
