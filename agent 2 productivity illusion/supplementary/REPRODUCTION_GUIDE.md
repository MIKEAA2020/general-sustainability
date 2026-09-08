# Reproduction Guide & Code Map

Companion to the manuscript *Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion*. This guide tells a reader how to rebuild every numeric result and figure.

Workflow: **reproduce the exact model** → **run the basin/characteristic analyses** → **render the figures** → **verify the claims**.

---

## 1. Environment & dependencies

| Item | Requirement |
|---|---|
| Python | ≥ 3.11 |
| `model_sims/` runtime | `numpy`, `scipy` (integration, spectral roots) |
| Figure rendering | `matplotlib` (`Agg` backend) |
| Results serialisation | `json` (stdlib) |
| Optional heavy backends | `sentence-transformers`, `transformers`, `hypothesis` (only for the gap-scan tooling, not the model) |

Install the project (optional, for the audit tooling) with `pip install -e .` (see `pyproject.toml`). The model itself is plain NumPy/SciPy and needs no package install.

**No stochastic seed is required** — the model is deterministic. There is no random number generation in the model or its sweeps.

---

## 2. File / folder structure

```
agent 2 productivity illusion/
├── model_sims/                      # the model and analyses
│   ├── corrected.py                 # corrected S0 simulator (deficit-driven stock-flow)
│   ├── topdown.py                   # top-down analysis of S0 (regimes, ratios, closed forms)
│   ├── char_eq.py                   # linearisation coefficients + characteristic-equation roots
│   ├── r1_basin.py                  # R1 basin recompute (recover/collapse dichotomy)
│   ├── r1_figure.py                 # renders the R1 basin figures
│   ├── r2_figure.py                 # renders the R2 characteristic-equation figures
│   ├── models.py                    # helpers incl. corrected_s0_summary, mask_run
│   ├── numeric_claims.py            # auto verifiers for reported numerical claims
│   ├── _run_sensitivity.py          # ρ-sensitivity sweep
│   ├── _run_topdown.py              # runner that writes data/topdown_results.json + top-down figures
│   ├── twoland_fixed.py             # root-cause-corrected two-book model (quality split; SI S5.2)
│   ├── twoland_nfa_proxy.py         # world NFA proxy decomposition (SI S5.1)
│   ├── twoland_nfa_proxy_sensitivity.py  # α-sensitivity of the proxy decomposition (SI S5.1)
│   ├── verify_tab_conv_basin.py     # re-derives `tab:conv` Δb_conv/λ_+ and `tab:basin` thresholds (SI S5.2)
│   ├── recovery_metric_and_tau_p_scan.py  # SI S5.4 R_c(T) gate-sign + S5.5 τ_p-extended delay scan
│   └── r1_r2_report.py / r1_r2_sensitivity.py
├── scans/                           # rendered model figures (inputs for the SI figure set)
├── data/
│   ├── topdown_results.json         # verified top-down numeric record
│   └── r1_r2_sensitivity_results.json
├── graphical_abstract/              # build_graphical_abstract.py -> .pdf/.png/.tiff
└── supplementary/                   # this package
```

---

## 3. Reproduce every numeric result & figure

The canonical entry point is the top-down runner, which recomputes and re-serialises the verified results.

```bash
# 1) Regenerate the verified top-down record + the three top-down figures
python -m model_sims._run_topdown

# 2) Recompute the R1 basin (recover/collapse dichotomy) and R2 spectrum, and render their figures
python -m model_sims.r1_figure
python -m model_sims.r2_figure
# (basin/char recompute + numeric verification)
python -m model_sims.numeric_claims

# 3) r- (regeneration-rate) sensitivity
python -m model_sims._run_sensitivity

# 4) Regenerate the graphical abstract
python graphical_abstract/build_graphical_abstract.py
```

**Baseline parameters** are set in the modules below and should be left unchanged for the standard figures (see the SI S4.1 table): `ρ=0.05`, `A_max=1.2`, `b₀=0.5`, `b_G=0.8`, `e=0.55`, `r=0.02`, `A_ext=0.02`. In `_run_topdown.py`, `topdown.py` and `char_eq.py`, `corrected.py` the relevant signature is e.g. `corrected_s0(endpoint=..., rho=0.05, Amax=1.2, b0=0.5, bG=0.8, e=0.55, ...)`.

---

## 4. Output registry

Which script produces which figure / number. All paths relative to the project root.

| Figure / output | Produced by | Source figure in package |
|---|---|---|
| `scans/feedback_diagram.png` | (feedback-loop diagram; see manuscript §7). Regenerate with `model_sims/rebuild_S1_feedback_diagram.py`. | `FIGURES/S1_feedback_diagram.png` |
| `scans/topdown_macro_ratios.png` | `_run_topdown.py` | `FIGURES/S2_macro_ratios_RB_vs_RA.png` |
| `scans/topdown_ratio_separation.png` | `_run_topdown.py` | `FIGURES/S3_flow_share_separation.png` |
| `scans/topdown_delay_boundary.png` | `_run_topdown.py` | `FIGURES/S4_delay_boundary_cliff.png` |
| `IMPLEMENTED_demo.png` | (overshoot demo; see manuscript §10, `demo_unified.py`) | `FIGURES/S5_demo_overshoot_run.png` |
| `IMPLEMENTED_demo_masking.png` | (masking window; see manuscript §10, `mask_rk4.py`) | `FIGURES/S6_masking_window.png` |
| `scans/r1_recovery_vs_collapse.png` | `r1_figure.py` | `FIGURES/S7_recovery_vs_collapse.png` |
| `scans/eco_recovery_insight.png` | `r1_figure.py` | `FIGURES/S8_recovery_insight.png` |
| `scans/r2_char_spectrum.png` | `r2_figure.py` | `FIGURES/S9_char_spectrum.png` |
| `scans/r2_a11_vs_delay.png` | `r2_figure.py` | `FIGURES/S10_a11_vs_delay.png` |
| `scans/sustainable_yield_regimes.png` | (regime table figure; see manuscript §4.1) | `FIGURES/S11_sustainable_yield_regimes.png` |
| `scans/r1_basin_baseline.png` | `r1_figure.py` | `FIGURES/S12_basin_baseline.png` |
| `scans/r1_basin_delay_response.png` | `r1_figure.py` | `FIGURES/S13_basin_delay_response.png` |
| `graphical_abstract/graphical_abstract.pdf/.png/.tiff` | `build_graphical_abstract.py` | `FIGURES/S14_graphical_abstract.png` |
| `data/topdown_results.json` | `_run_topdown.py` | — |
| `data/r1_r2_sensitivity_results.json` | `r1_r2_sensitivity.py` | — |

**Note on two figure drivers named in the manuscript.** The manuscript's `§10` references `demo_unified.py` (overshoot demo) and `mask_rk4.py` (masking window). These two drivers are documented in the text but are not present in this repository snapshot; the underlying computations are captured in the `mask_run` helper (`model_sims/models.py`, with the §10 configuration) and in the reported, converged values. A reader wanting to fully re-run those two figures should restore the two drivers from the manuscript's stated parametrisation.

---

## 5. Verification protocol

Every reported number carries its protocol (see manuscript §8):

- **Solver:** method-of-steps with RK4 (or `dde23`/`pydelay`), the exact `[·]₊` switch (never a smooth ramp, which leaks depletion when `E < bA`), clamping `A ≥ A_ext`, `P ≥ 0`, `K ≥ K_min`, and an explicit extinction floor (so "collapse" is a model result, not a clamp). Where a smooth variant replaces `[·]₊` (reference implementation only), its width `w` is fixed and reported with insensitivity to `w`.
- **Convergence:** state `dt`, history functions, and a `Δt`-convergence table (e.g. scenario A `A*`: 0.8022 at `dt=0.5` vs 0.8021 at `dt=0.05`).
- **Termination convention:** the endpoint `D_E` is method-dependent (5.26 / 6.74 / 18.70 for the frozen/crashed/un-clamped endings) and must be reported with its convention.

Run the automated numeric verification with `python -m model_sims.numeric_claims` (tolerance `0.02`; verifies e.g. `frac_recover_nodelay = 0.399`, `frac_recover_baseline = 0.053`).
