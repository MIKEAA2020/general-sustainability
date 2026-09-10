# NUMERICAL AUDIT — MASTER vs REVISION (independent re-computation)

Ran by `audit_basin.py`, `audit_numerics.py`, `audit_s0.py`, `mask_rk4.py`, `deficit_map.py`,
`regression_test.py`. Everything below is **re-computed**, not re-read. Each entry gives the result,
the model it was computed on, and whether it confirms / corrects / supersedes the master.

## A. Corrected model `(1‴)` — constant-parameter S0 structure (the key structural finding)

Integrating the corrected S0 (`α = 0`, no technology, no delays, narrow softplus ramp `w=0.02`,
`ρ=0.08, b₀=0.5, b_G=0.6, e=0.55, r=0.02, A_ext=0.02`):

- **The "sustainable" state is a one-sided boundary, not a unique attractor.** Setting
  `dP/dt = 0` gives `P = K = B/e`, hence `E = eP = B`; then
  `dA/dt = G(A) − [E − bA]₊/b_G = G(A) − [b_G G(A)]₊/b_G = 0` for **any** `A`. So the S0 has a
  *continuum* of equilibria `(A*, P* = B*(A*)/e)` — and the flow-only end `A → A_max,
  P → b₀A_max/e` is where `E = B = bA` coincides (the orchard limit).
- **The continuum is one-sided.** Any overshoot that puts `E > bA` (population `P` above the
  sustainable level) triggers the stock-liquidation **vicious cycle** and the run collapses to
  `A → A_ext, P → 0` (verified: `t=100` `A≈1.200`, `t=200` `A≈1.198`, `t=400` `A→0.020` — the
  overshoot rolls over into collapse). This is precisely the master's Part 6 F3 / Part 4 decision 6
  ("sustainable point is a **boundary of the deficit regime**; one-sided stability").
- **Contrast with the original model.** The original S0 (gross depletion) has a **unique interior
  attractor** `M* = 0.740, P* = 0.370`. That is a *different* object from the corrected S0's
  one-sided boundary. → **12G.2's basin fraction does not transfer.** See risk R1.

## B. Original model — independent re-confirmation (master's numbers hold)

| Quantity | Re-computed | Master claims | Verdict |
|---|---|---|---|
| unique interior attractor `M*,P*` (`e=1.15, α=0`) | `0.740, 0.370` | `0.740, 0.370` | CONFIRMED |
| basin stable-frac `(0,0)` (fig_basin grid) | `0.5062` | `0.506` | CONFIRMED |
| basin stable-frac `(30,25)` (fig_basin grid) | `0.0437` | `0.042` | CONFIRMED (grid-sensitive) |
| basin stable-frac `(0,0)` (coarser `basin.py` grid) | `0.479` | — | grid- / dt-dependent |
| IC `(1.0,0.1)` at `(0,0)` / `(20,20)` / `(30,25)` | S / S / C | S / recovers / collapses | CONFIRMED |
| `(20,20)` min `M` over run | `0.640` | `0.631` | CONFIRMED (dt-sensitive) |
| `(30,25)` min `M` over run | `0.000` (collapse) | `< 0.6` | CONFIRMED |
| Scenario A `M_fin,P_fin,D_fin` | `0.800, 0.400, 0` | `0.8/0.4` | CONFIRMED |
| Scenario B `M_fin` (recovers, P collapses) | `1.194`, `P≈0.007` | `≈1.19` | CONFIRMED (12G.4) |
| Scenario C `M_fin` | `1.193` | `≈1.19` | CONFIRMED (12G.4) |
| Scenario D `M_fin,P_fin,D_fin` | `0,0,4.826` | collapse | CONFIRMED (12G.5) |
| Scenario E `D_fin` | `5.262` | `≈5.26` | CONFIRMED (12A.3) |
| Scenario F (Half-Earth) `M_fin,P_fin` | `0.970, 0.243` | `0.970, 0.243` | CONFIRMED |

## C. Masking illusion (corrected reduced model, converged RK4 — supersedes the master's numbers)

Re-verified with `mask_rk4.py` (converged over `dt = 0.25→0.01`) and `deficit_map.py`:

- A **genuine** mask exists **only for a small initial deficit**. Window `≈5.4 yr` at deficit
  `E − b₀A₀ = 0.06` (`B 0.576→0.647` while `A 0.959→0.858`, `dt=0.02`), **converged**.
- Window width **vanishes at deficit ≈0.075** (≈**15 % of the initial flow yield `b₀A₀`**); beyond it the
  run goes straight to the extinction floor with **no** mask. (Re-confirmed in `regression_test.py`:
  at `E=0.75` and `E=0.90`, window width `= 0`.)
- **The master's headline demonstration sets are SUPERSEDED as numbers.** `12A.1`
  (`α=0.5, Δb=0.3, t_wave=100 ⇒ B 0.5→0.618, M→0.847`) and `12G.7`
  (`e=1.15, α=0.2, Δb=0.8, t_wave=100, κ=0.05 ⇒ B 0.711→0.832, M→0.834`, "118 sets") were computed on the
  **original gross-depletion model**; they do **not** reproduce under `(1‴)`. The mechanism
  (narrow / bounded / transient) is retained; the specific numbers are not.

## D. What the audit changes in the revision (already applied)

1. `§8` gains a **provenance note**: basin-shrinkage `0.506→0.042`, Scenario B/C `M≈1.19`, `D_E≈5.26`,
   and `τ*` are **original-model** quantities; the corrected `(1‴)` S0 is a **one-sided boundary**, not
   a unique interior attractor, so the corrected basin must be recomputed & reported separately (risk R1).
2. `§5` Scenario B/C note tagged as original-model.
3. Masking "~8 % overshoot" corrected to **"deficit ≈0.075, ≈15 % of `b₀A₀`"** in `§1`, `§5`, `§10`.
