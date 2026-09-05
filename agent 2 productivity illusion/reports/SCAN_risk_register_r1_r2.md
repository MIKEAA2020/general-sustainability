# R1 / R2 resolution — corrected (1''') basin recompute and characteristic-equation set

*Generated for the corrected model (see `model_sims/corrected.py`, `model_sims/char_eq.py`, `model_sims/r1_basin.py`, `model_sims/r1_r2_report.py`).*

## R1 — corrected-(1''') basin recompute (recover vs collapse)

- **Grid (documented):** `A0` grid `13x16=208`, `P` straddles the sustainable population `P*=b0 A_max/e = 1.0909`.
- **No delay `(0,0)`:** recover (A->A_max) = **39.9%**, collapse = **60.1%**.
- **Baseline `(30,25)`:** recover = **5.3%**, collapse = **94.7%**.
- **Mechanism:** with the regeneration delay, the stock overshoots A_max (up to ~1.36), the population (tracking delayed K) overshoots into `E>bA`, and the vicious-cycle liquidation drives A to A_ext. The recover basin collapses abruptly as tau_g rises through ~20 yr (see `scans/r1_basin_delay_response.png`).
- **Recover boundary at A0=1.0 (no delay):** recovers for `P0 <= 0.85`.
- **Separatrix = equilibrium line (`P0 < B(A0)/e`):** agreement with the recover/collapse classification is **99.0%** (no delay) vs **64.4%** (baseline `(30,25)`). So under no delay the boundary curve is exactly the family line `P0 = B(A0)/e` (the numerical witness to R2's neutral continuum); under baseline delays the recover basin collapses to the strip `[(1.2, 1.091, 11)]` — i.e. only `A0 ≈ A_max` with `P0 ≲ B(A_max)/e ≈ 1.09` recovers (5.3%), and nothing else.
- **Delay response** (tau_p=0): tau_g=0.0: 0.42, tau_g=8.0: 0.42, tau_g=16.0: 0.42, tau_g=24.0: 0.10, tau_g=32.0: 0.10, tau_g=40.0: 0.21, tau_g=48.0: 0.42, tau_g=56.0: 0.27, tau_g=64.0: 0.31.

## R2 — corrected characteristic equation / crossing curves / full spectrum

- **Reference equilibrium** A*=0.8 (an interior point of the family `P=B(A)/e`); coefficients {'a1': -0.01667, 'a3': 0.625, 'aE': -0.6875, 'a4': 0.0177, 'a5': -0.02, 'r': 0.02, 'Astar': 0.8, 'Pstar': 0.74667}.
- **Neutral zero eigenvalue confirmed:** `D(0) = 0.00e+00` — the corrected S0 has a one-parameter family of equilibria and **no isolated interior attractor**.
- **Real roots (no delay):** [-0.0, 0.5883]; leading mode `Re λ = 0.5883` **> 0 (monotone vicious-cycle growth).**
- **Real roots (30,25):** [-0.2437, -0.0, 0.625]; leading mode `Re λ = 0.625` still > 0. Complex modes (13) all have **negative** real part (damped), so the instability is monotone, not a Hopf.
- **No exact stability-crossing curve:** scanning `s=i ω` over the whole family finds **no** imaginary-axis crossing (`hopf_crossing_found=False`). Hence the manuscript's `χ` two-gain Hopf classification (derived for the ORIGINAL model's interior attractor) does **not** transfer; instead the corrected S0 has a structurally unstable interior point.
- **Manuscript `a₁₁ < r` violated everywhere:** max `a₁₁ = 0.6583` at A*=0.2 (`a₁₁ = G'(A*)+b/b_G`). `a₁₁ > r = 0.02` for every reference equilibrium on the family (`a11_gt_r_everywhere = True`) — the zero-delay stability condition is never satisfied.
- **Figure set:** `scans/r1_basin_baseline.png`, `scans/r1_basin_delay_response.png`, `scans/r2_char_spectrum.png`, `scans/r2_a11_vs_delay.png`.
