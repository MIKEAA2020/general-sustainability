# Supporting figure captions (S1–S14)

Each figure is produced by the script named; see `REPRODUCTION_GUIDE.md` for full run instructions and the output registry.

| Fig | Source file | Caption |
|---|---|---|
| **S1** | `scans/feedback_diagram.png` | **Feedback diagram.** The causal loop with the deficit switch: `A →^{b} B → K → P → E`, with `E − bA` deciding the switch, `D →^{α} b`, and an exogenous bounded `T_b`. Two positive-feedback loops compound: Loop 1 (stock-liquidation, `A↓→B↓→deficit↑→liquidation↑→A↓`) and Loop 2 (debt-erosion, `D↑→b↓→B↓→deficit↑→D↑`). |
| **S2** | `scans/topdown_macro_ratios.png` | **Macro-ratio safe-operating space.** The baseline basin in the `R_B`–`R_A` plane (two panels, `τ_g=10` and 30), showing the `R_B = 1` boundary as both the basin separator (recover/collapse) and the safe-operating boundary, with the `R_A > 1` buffer. |
| **S3** | `scans/topdown_ratio_separation.png` | **Flow-share separation.** The ψ-regime closed form `R_A^eq = (1 + b_Gρ/b)/2` (and `ψ* = 2/(1 + b_Gρ/b)`): how far the leading indicator `R_A` sits above the trigger `R_B` as the regime index `b_Gρ/b` grows. |
| **S4** | `scans/topdown_delay_boundary.png` | **Delay-boundary cliff.** The `τ_g`-driven transition in the `(τ_g, τ_p)` plane: zero imaginary-axis crossings (`Re λ ≈ +0.625` constant), the recover fraction collapsing across an ≈18–20 yr band, and recover/collapse independence from the demographic lag. |
| **S5** | `IMPLEMENTED_demo.png` | **Representative overshoot run.** Stock `A`, biocapacity `B` and population `P` all rise (logistic overshoot / boom), then collapse to the extinction floor with debt `D` building — the delayed-regeneration overshoot and the debt → degradation → collapse route. |
| **S6** | `IMPLEMENTED_demo_masking.png` | **Productivity illusion (masking window).** Panel a: `B` rises while `A` falls over a narrow window (`t ≈ 1.4 → 6.8` yr). Panel b: window width vs initial deficit — max ≈5.4 yr at deficit 0.06, collapsing to zero at ≈0.075. |
| **S7** | `scans/r1_recovery_vs_collapse.png` | **Recovery vs collapse.** The same initial condition `(A₀,P₀)=(1.0,0.1)` recovering (`A→A_max`, `τ_g=10`) versus collapsing (`A→A_ext`, overshoot `A→1.36`, `τ_g=30`). |
| **S8** | `scans/eco_recovery_insight.png` | **Recovery insight.** Density-dependent, sigmoidal recovery trajectory and the decoupling of regeneration *rate* (sets recovery time) from regeneration *lag* (sets recovery outcome). |
| **S9** | `scans/r2_char_spectrum.png` | **Characteristic spectrum.** Leading eigenvalue `Re λ_max` vs regeneration delay `τ_g`, showing it is always positive real (monotone vicious-cycle growth, no Hopf crossing); damped oscillatory modes shown as the complex-roots cloud. |
| **S10** | `scans/r2_a11_vs_delay.png` | **`a₁₁` vs delay.** Manuscript `a₁₁ = G′(A*) + b/b_G` vs `A*`, with the `r` threshold: `a₁₁ > r` everywhere (zero-delay condition violated). |
| **S11** | `scans/sustainable_yield_regimes.png` | **Sustainable-yield regimes.** The `B(A)` curve shape by regime — capital-dominated (interior MSY), flow-dominated (monotone, boundary `A_max`), and the marginal case. |
| **S12** | `scans/r1_basin_baseline.png` | **Basin heatmap.** Two-panel recover/collapse basin for `(τ_g,τ_p)=(0,0)` and `(30,25)`, with the closed-form separatrix `A_c(E)` overlaid and the sustainable point marked. |
| **S13** | `scans/r1_basin_delay_response.png` | **Basin delay response.** Recover fraction vs regeneration delay `τ_g` (solid) showing the abrupt basin collapse, with the demographic-lag `τ_p=25` line. |
| **S14** | `graphical_abstract/graphical_abstract.png` | **Graphical abstract.** Three-panel banner: the orchard (flow = biocapacity · stock = capital), the coupling (delayed loop, deficit switch, debt), and the illusion (biocapacity rises while stock falls; `R_B = 1`; no warning at long lag). |
