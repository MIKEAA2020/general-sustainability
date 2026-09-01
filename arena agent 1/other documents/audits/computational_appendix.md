# Computational Appendix — Numerical Illustrations
## Companion to *A Viability Theory of Constrained Sustainability under Uncertainty, Coupling, and Recoverability*

This companion records the concrete numerical illustrations and parameter values used
to verify the results in the main article. The article states the general results;
this appendix provides the specific instances that were computed during verification.
All values were obtained by direct computation (analytic evaluation, ODE time-domain
simulation, root finding, or randomized sampling).

---

## A. Corollary 6.1 — constrained MSY (piecewise formula)

Logistic growth `g(S) = r·S·(1−S/C)`, `H* = rC/4` at `S_m = C/2`. The reduced formula
`min(H*, H_sink)` overstates the true constrained MSY when the floor is above the
MSY stock. Parameters: `r = 1, C = 10` (so `H* = 2.5, S_m = 5`), `H_sink = 4`. (The article's single-instance witness uses `H_sink = 3`; the overstatement `9/10` is independent of the loose sink cap.)

| `S_min` | `min(H*,H_sink)` | `min(g(S_min),H_sink)` | Verdict |
|---|---|---|---|
| 5.0 | 2.500 | 2.500 | match |
| 7.0 | 2.500 | 2.100 | overstated |
| 9.0 | 2.500 | 0.900 | overstated |

Single-instance witness used in the article: `r=1, C=10, S_min=8` gives
`g(8) = 8/5 = 1.6 < H* = 25/10 = 2.5`, overstatement `9/10`.

---

## B. Theorem 12.1 — over-extraction comparison

Payoffs `πᵢ(h) = aᵢh − h²`, damage `dᵢ(H) = cᵢH²/2`. Interior comparison:
`H_Nash = Σa/(2+Σc)`, `H_soc = Σa/(2+n·Σc)`.

| Scenario (`n=2`) | `H_Nash` | `H_soc` | strict `>` |
|---|---|---|---|
| symmetric `π,d` | 1.923 | 1.200 | ✓ |
| asymmetric benefits `a=9,1.2` | 2.000 | 1.500 | ✓ |
| one zero-damage agent | 2.250 | 1.600 | ✓ |
| all zero damages | 4.000 | 4.000 | ✗ (equal) |

Witness: `a₁=a₂=5, c₁=c₂=0.8` gives `H_Nash = 10/3.6 = 2.78 > H_soc = 10/5.2 = 1.92`;
decoupled (`c=0`) gives `H_Nash = H_soc = 5`.

---

## C. Corollary 8.1 — CES essentiality

`F(A,R) = Y₀[α(A/A₀)^ρ + (1−α)(R/R₀)^ρ]^{1/ρ}`, `ρ = (σ−1)/σ`.

- `F(A,0) = 0` for `σ ≤ 1`; `F(A,0) = Y₀·α^{σ/(σ−1)}·(A/A₀)` for `σ > 1`.
- Witness `σ=2, α=0.5, Y₀=10, A₀=2`: `F(5,0) = 3.125`, `F(10,0) = 6.25`.
- `c_max(R) = +∞` when `σ>1` and `μ_A > δ_A`; verified that `Φ(A) ≈ (μ_A−δ_A)·A`
  with ratio → 1 as `A→∞` (e.g. at `A=10¹⁵`, ratio = 1.000000).

---

## D. Remark 6.1 — sink obstructions

`δ ≡ 0` or `δ(K_max) < w(H_min)` force an empty kernel. Witness: `K_max=2, H_min=1,
w(H)=0.5H, δ(K)=0.1K` gives `δ(K_max)=0.2 < w(H_min)=0.5`, `K†=5 > K_max=2`.

---

## E. Theorem 4.3 — delay margin

`ẋ = −ax − Bx(t−τ)`, stable for `τ < τ_crit = arccos(−a/B)/√(B²−a²)` when `B>a`.

- Witness `a=1, B=2`: `τ_crit = arccos(−1/2)/√3 ≈ 1.209`. Stable at `0.4·τ_crit`,
  unstable at `1.6·τ_crit`. Stable for all `τ` when `B ≤ a` (e.g. `a=1, B=0.5`).

---

## F. Theorem 6.6 — pollution-suppressed growth

`g(S,K) = S(1 − S/C(K))`, `C(K) = 10/(1+0.05K)`, `w(H)=0.5H`, `δ(K)=0.3K`.

- The `H_min`-control dominates coordinatewise (S higher, K lower).
- Rectangle `[S_∘(K_max), ∞)×[0,K_max]` is invariant.
- Threshold stock `S(K)` needed for viability increases in `K`:
  `0.528, 0.531, 0.534` at `K = 0, 2, 4` (frontier is a strictly decreasing curve).

---

## G. Theorem 4.4 — observer safety buffer

On the boundary, `L·ē ≤ η` preserves `Q`; `L·ē > η` causes exit. Witness
`ẋ = −z + u + d`, `u∈[0,2]`, `d∈[−0.1,0.1]`, margin `η=0.2`, sensitivity `L=1`:
safe for `ē ≤ 0.2`, exit for `ē > 0.2`.

---

## H. Theorem 4.7 — hidden-mode conflict

`ż = θu`, `θ ∈ {−1,+1}`, `u ∈ {−1,+1}`, `z ≥ 0`. At `z=0`: `R((0,+1)) = {+1}`,
`R((0,-1)) = {-1}`, common action empty. Each state individually in `RViab`; the
joint belief `{(0,+1),(0,-1)}` is not in `ERViab`. `Viab = RViab` (six states) but
`K_I = ∅` under constant observation — a purely epistemic contraction.

---

## I. Theorem 10.1 — jump discontinuity

Two-patch MSY, `C₁=10, C₂=12`, `d=0.2`: decoupled equilibrium `(5,6)` at `d=0`;
no equilibrium for any `d>0` (so kernel empty), since `d>0, C₁≠C₂` forces `C₁=C₂`.

---

## J. Theorem 12.1 — Clark under-extraction

Open-access stock `S_OA = c/(pq)`. Witness `p=10, c=5, q=1`: `S_OA = 0.5`. A per-unit
harvest tax `t` shifts `S_OA(t) = c/((p−t)q)`: `S_OA(0)=0.50`, `S_OA(1)=0.56`,
`S_OA(4)=0.83` (increasing in `t`).
