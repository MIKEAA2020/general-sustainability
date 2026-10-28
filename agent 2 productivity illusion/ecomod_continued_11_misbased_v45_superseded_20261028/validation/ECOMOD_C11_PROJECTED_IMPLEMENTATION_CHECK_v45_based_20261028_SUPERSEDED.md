# ECOMOD Continued 11 local draft: projected-quality implementation and output check

**Date:** 2026-10-28  
**Draft:** `../ecomod_continued_11_revision_draft_20261028/`  
**Lineage:** local successor draft to archived Continued 10 (C10); not yet an issued release.  
**Purpose:** document what the revised projected-quality implementation and newly regenerated outputs establish, and keep that evidence separate from historical C10 provenance.

## 1. Scope and bottom line

The separate draft now specifies the quality state continuously as

\[
K_q=[0,q_{\max}],\qquad
\dot q(t)=\Pi_{T_{K_q}(q(t))}G_c(q(t-\tau_g)),\qquad
G_c(x)=\rho_c x\left(1-\frac{x}{q_{\max}}\right),
\]

with admissible continuous history. Here `q` is an uncalibrated, model-defined index; `q_max=1` is an imposed admissibility bound, not an estimated ecological threshold; and `rho_c` and `tau_g` are scenario parameters, not estimates from recovery studies.

A new local test **passed**. It establishes exact equality of the tested discrete state arrays for the copied v45 post-Euler clipping rule and an explicit tangent-cone projected Euler update, plus decreasing time-refinement errors in scalar quality and in the tested full-model scenario. This establishes consistency for those local implementations and cases. It does **not** establish which exact code/configuration produced every archived C10 result.

The draft's regenerated Figure 1 PNG is byte-identical to the archived C10 PNG. Its PDF is byte-identical after normalizing only the changing `/CreationDate` metadata. The regenerated drawdown CSV and drawdown/recovery table bodies also retain the archived displayed values. The new SI delay-table generator has now been run; it reproduces the archived displayed precision in the tested rows, but is a fresh revised run, not historical provenance for the old table.

The separate historical provenance report remains controlling for the unresolved C10 run-to-output links, including the high-resolution Table 2(b) bisection and the originally generated full SI Table S2 sweep: `/home/user/ECOMOD_C10_RESULTS_PROVENANCE_20261028.md`.

## 2. Code, environment, and immutable boundary

### Source snapshot and files

- Base candidate: `ecomod-v45-workspace-archive-20261026`, commit `eab8e82eb5171d70711c1b319a83f99492e6fca8`.
- The copied `work/twoland_fixed.py` remains unchanged; SHA-256 `7f2e47ab9a8047bfe335aaf02a90893b06aceba86c26b6f946999f94617e0c27`.
- New revision solver: `work/twoland_fixed_projected.py`; SHA-256 `51486131bdf83ac53f1132bb2cbf9344e8ec5bd1a907a1e1de77dc23ced3e0e5`.
- Numerical test: `work/test_projected_quality_consistency.py`; SHA-256 `16da76b11e1a829237cf79f9f62d28b3a49591faf501038a7955786a9670d97d`.
- New revised SI delay-table generator: `work/generate_revised_si_delay_table.py`; SHA-256 `3b225222de36dc3214ce6323428ef458876fef1d2ae89614892b9462ee023142`.

The original v45 package, archived C10 files, c8/c9, `main`, pins, checksums, and DOI deposits were not changed by this draft work.

### Environment observed for this local check

- Python `3.13.16`
- NumPy `2.3.5`
- SciPy `1.17.1`
- Matplotlib `3.10.9`
- openpyxl `3.1.5`
- No Python lockfile/environment pin was present in the copied ECOMOD package. The numerical test and simulation solver use NumPy; Matplotlib is used for figures; SciPy and openpyxl are used by other analysis/empirical scripts.
- `pdflatex` became available after installing Debian TeX Live packages `texlive-latex-extra` and `texlive-publishers` in this sandbox: pdfTeX `3.141592653-2.6-1.40.26` (TeX Live 2025/dev/Debian), with `elsarticle` v3.4c. Tectonic, latexmk, XeLaTeX, and LuaLaTeX remain absent.
- The assembled main and SI were each compiled in three passes with pdfLaTeX; the build record is `../ecomod_continued_11_revision_draft_20261028/output_revision_projected/continued_11_tex_build_20261028.log`. These are document-build details, not evidence about the historical Python simulation environment. The archived C10 `LINEAGE.md` separately records Tectonic 0.17.0 for its earlier document build.

## 3. Projected solver and update order

The new solver keeps `work/twoland_fixed.py` intact and imports `work/twoland_fixed_projected.py` from the applicable revised-run producers. In the projected solver:

1. Before a run, `q(s)=q0` and `B(s)=B0` are stored as constant pre-run histories. The solver preallocates at least `max(tau_g,tau_p)+1 yr` of that history. In the controlled wave pair, the common pre-run `B` history is no-wave; the active scenario changes `B` at `t=0` through the logistic technology tail.
2. At step `k`, the current states are read from `t_{k-1}`. The time-dependent technology input and delayed values are evaluated at `t_k`. Delayed `q` and `B` are linearly interpolated; the delay buffer uses the existing `_interp` routine.
3. The delayed raw quality velocity is `G_c(q(t_k-tau_g))`. It is projected onto the tangent cone at the current quality `q(t_{k-1})` before the Euler state update. The implementation projects outward velocity to zero at either boundary when necessary.
4. Other rates are computed from the current state and the stated delayed inputs. All state updates use the same explicit Euler step; the updated quality is then clipped to `[0,q_max]` as a finite-step safeguard, bounded states are clipped, and reserve area is set as `A_tot-A_f-A_c`.
5. The updated `B` is stored in the delayed history after the state update.

The one-stock comparator in SI is a separate formulation. No smooth alternative is selected as the current ECOMOD model.

## 4. Numerical consistency tests

The full console output is saved at `output_revision_projected/projected_quality_consistency.log`.

### Same-grid discrete update comparison

Using the copied v45 candidate solver (`twoland_fixed.py`) and the new projected solver with the Figure 1 baseline initial state and parameters, `T=100 yr`, `dt=0.05 yr`, and `tau_g=5, 20, 40 yr`, all tested arrays were exactly equal:

`Af`, `Ac`, `q`, `Pp`, `Dd`, `Ar`, `B`, `E`, and `T_b`.

The initial scenario was `A_f0=0.6 ha`, `A_c0=1.5 ha`, `q0=0.9`, `P0=1.2 cap`, `D0=0`, frozen `E=0.825 gha`, `A_tot=2.5 ha`, with the baseline values encoded in `make_fig_model.py`. This is a same-grid comparison of the two local discrete updates; it is not a provenance proof for the archive.

### Scalar quality refinement

For constant history `q(s)=0.9`, `rho_c=0.08 yr^-1`, `q_max=1`, and `tau_g=20` or `40 yr`, the continuous projected path is exactly

\[
q(t)=\min(1,0.9+0.0072t),
\]

and reaches the cap at `125/9 = 13.888888… yr`, before either delay elapses. The maximum error of the piecewise-linear discrete path against that continuous path was the same for `tau_g=20` and `40`:

| `dt` (yr) | maximum quality error |
|---:|---:|
| 0.1 | `7.1e-5` |
| 0.05 | `6.2e-5` |
| 0.025 | `4.4e-5` |
| 0.0125 | `8.8e-6` |

For the distinct `tau_g=5 yr` case, comparison against a linearly interpolated `dt=0.00025 yr` reference gave maximum errors `2.17632062e-4`, `1.08661278e-4`, `5.40870776e-5`, and `2.67776406e-5` at `dt=0.1`, `0.05`, `0.025`, and `0.0125 yr`, respectively.

### Full Figure 1 scenario refinement

For the frozen-demand Figure 1 scenario (`tau_g=20 yr`, `T=400 yr`, initial state and parameter values as above), each coarse run was compared on common time nodes with a projected-solver reference at `dt=0.003125 yr`:

| `dt` (yr) | `A_c` max error (ha) | `B` max error (gha) | `P` max error (cap) | `D` max error (gha yr) | `q` max error |
|---:|---:|---:|---:|---:|---:|
| 0.1 | 0.00467314 | 0.00379877 | 0.000520008 | 0.00422169 | `1.53e-13` |
| 0.05 | 0.00221430 | 0.00179916 | 0.000252144 | 0.00200063 | `1.54e-13` |
| 0.025 | 0.00102297 | 0.000831026 | 0.000117784 | 0.000924251 | `1.85e-13` |
| 0.0125 | 0.000436247 | 0.000354341 | `5.05035e-5` | 0.000394136 | `1.23e-13` |

These are empirical timestep-refinement comparisons to a finer numerical reference, not an analytic error bound or proof of convergence for every model scenario.

### Interpretation of the 20/40-year pair

Under the baseline constant history, `tau_g=20` and `tau_g=40` generate exactly the same quality path: quality reaches the imposed ceiling at `125/9 yr` before either delayed input first reaches the post-initial trajectory. Thus the baseline 20/40-year comparison is a saturation-induced degeneracy, not general delay robustness. The `tau_g=5 yr` case is distinct.

## 5. Revised runs and mapping to draft outputs

| Revised run | Code and settings | Draft outputs |
|---|---|---|
| Frozen-demand Figure 1 | `make_fig_model.py` → `twoland_fixed_projected.py`; `T=400 yr`, `dt=0.05 yr`, `E=0.825 gha`, `A_f0=0.6 ha`, `A_c0=1.5 ha`, `q0=0.9`, `P0=1.2 cap`, `D0=0`, `tau_g=20 yr`, `tau_p=25 yr`; baseline `rho_c=0.08`, `b_f0=0.85`, `b_c=0.05`, `b_Gc=0.8`, `alpha=0.03`, `eta_f=0.05`, `eta=0.05`, `mu=0.06`, `e=0.55`, `r=0.02`, `A_tot=2.5`, `tau_conv=1`. `E_fixed` disables surplus-gated restoration; the wave is off. Histories of `q` and `B` are constant at their initial values. | `figures/fig1_model_dynamics.png` and `.pdf`; local run reports 149.0 yr mask, `E_ceil=1.1384 gha`, capital contribution `0.08364→0.04038 gha`, and fast contribution `0.51000→0.78462 gha`. |
| Drawdown sweep / Figure 1(c) / SI drawdown and recovery tables | `drawdown_depth.py` → projected solver; `T=400 yr`, `dt=0.1 yr`, `A_f0=0.6 ha`, `q0=0.9`, `tau_g=20 yr`, `tau_p=25 yr`, `chi_r=0.10` and `0`, `A_c0={0.40,0.70,1.00,1.18} ha`, `P0=1.0…4.0 cap` by `0.1`. Pre-run `q`/`B` histories are constant. | `si_drawdown_depth.csv`; `make_fig_model.py` consumes it for Figure 1(c); `work/render_si_model_tables.py` writes `parts/si_tab_drawdown.tex` and `parts/si_tab_recovery.tex`. |
| New SI delay/current-quality comparison | `work/generate_revised_si_delay_table.py`; `tau_g={5,20,40} yr`, `tau_p=25 yr`; floor-threshold runs use `A_c0=1.0 ha`, `A_f0=0.6 ha`, `q0=0.9`, default `P0` bracket `[1,5]` with 40-step bisection, `T=800 yr`, `dt=0.1 yr`; demonstration summary uses `A_c0=1.5 ha`, `A_f0=0.6 ha`, `q0=0.9`, `P0=1.2 cap`, `E_fixed=0.825 gha`, `T=400 yr`, `dt=0.05 yr`. Both code variants use the same baseline parameters; the current-quality variant is a sensitivity comparator only. | `output_revision_projected/si_delay_sensitivity.csv` and `parts/si_tab_delay.tex`; the assembled SI inlines the generated table. Full-precision delayed thresholds are `2.9545817402`, `2.9544285887`, and `2.9544285887 cap` for `tau_g=5,20,40 yr`; the first differs, the 20/40 rows are equal. The displayed new table matches archived values after rounding; this does not prove the historical generator. |
| Recovery endpoint in main Results | Projected delayed-quality sweep above; `A_c0=1.0 ha`, `P0=2.0 cap`, `chi_r=0.10`, `T=400 yr`; table body uses the sweep's `dt=0.1 yr`. | Main Results now report `A_c(T)=0.677 ha` and `R_c=0.46`, matching `parts/si_tab_recovery.tex`. A separate fine-grid reconstruction at `dt=0.05 yr` gives about `0.6782 ha`, consistent within the timestep difference. The old `0.828 ha / 0.71` values remain in the excluded current-quality snapshot, not as the delayed-quality result. |

For the Figure 1 and drawdown rows, the remaining baseline defaults are `q_max=1`, `A_c_min=0.05 ha`, `K_min=0.02 cap`, `sigma_f=sigma_c=1`, `chi_r=0.10 gha^-1 yr^-1`, `Delta b=1 gha ha^-1`, `kappa_w=0.1 yr^-1`, and `t_wave=40 yr`; the technology wave is off. In the frozen-demand Figure 1 run, `E_fixed` explicitly disables surplus-gated restoration despite the stored `chi_r` default. All histories are admissible and constant at the stated initial values before `t=0`.

### Output comparisons

- Draft Figure 1 PNG SHA-256: `c96e1579e8bb32fb584e131514d6ada9f8c9f177384e415d23aa4f745870f796`, identical to the archived C10 Figure 1 PNG.
- Figure 1 PDF bytes differ because `/CreationDate` differs (`D:20261024205711Z` vs `D:20261028010615Z`); after replacing only that metadata field with a common placeholder, the PDFs compare byte-for-byte equal.
- Draft drawdown CSV SHA-256: `073c63778c46042d029a842d5a12529c207e5b2797bd56f4ca8f221951942417`, also the v45/archive value. The draft drawdown and recovery table bodies compare equal to the copied v45 modular table files and retain the C10 displayed entries.
- New delay CSV SHA-256: `9452a99cb53cdc33a8b1a1cb8ebd480f3a9a715b23577c34c1d50304d36911cd`.
- Test and generator logs: `output_revision_projected/projected_quality_consistency.log` and `output_revision_projected/revised_si_delay_table.log`.

## 6. Historical provenance remains separate and incomplete

- The local candidate solver's same-grid equality and the Figure 1 hash match support a reproducible local result. They do not prove that a particular archived C10 artifact was produced by the same executable file, configuration, dependencies, history initialization, interpolation, timestep, projection order, or generator.
- The old C10 output directory contains no simulation source. The v45 snapshot at commit `eab8e82…` is the best-supported local producer package, not a C10 release tag or a complete artifact-to-run manifest.
- Historical provenance for the full old SI Table S2 sweep remains unestablished. The fresh generator now provides a revision run with explicit settings and matching rounded values; it does not retroactively identify the old run.
- The historical Table 2(b) high-resolution bisection column remains unlinked to an exact preserved generator/configuration. The manuscript's displayed values are unchanged by this revision.
- The legacy current-quality table fragments and helpers are retained as comparison material only; they are not substituted for the projected delayed-quality baseline.
- In this pass, the wave scan, SI gate-sign table, NFA extraction, and other static analytical tables were not regenerated as a new full release. Their previously verified values remain separate; this report does not extend the new projected-run claim to them.

## 7. Assembly and checks

`python assemble.py` synchronized modular `parts/` with `ecomod_continued_11_revision_draft_20261028.tex` and `ecomod_continued_11_revision_draft_20261028_SI.tex`, inlining SI table bodies. Source SHA-256 values: main `f49b3d3a27b1ffbe92b9a6278d973db75409ec1747638f916a4cccf36923baf4`; SI `c51202d73d14da027f8d1022346a2cb5f3c16100f55b63d7757daa009ba6d33d`. A source-level label/citation scan found no duplicate labels, missing internal references, missing citation keys, or uncited bibliography entries after replacing a main-to-SI cross-reference with explicit “SI Table S2” wording. A source-only environment/group-balance scan also passed.

Both assembled documents were then compiled with pdfLaTeX in three passes each. The main PDF is 36 pages (SHA-256 `05b64926739021c9fea39589a9c17ca29442f2bf1e8e979d63ff021e5deefd4d`); the SI is 22 pages (SHA-256 `e0f53f5f5a3c10a6f9c4886ea76dcd00ec9a896ea67f84c684713a4b31ea55d0`). Final logs have no unresolved citations/references, label-rerun notices, or overfull boxes; nonfatal underfull-box and main-PDF-string warnings remain. The first SI compilation exposed single-backslash row endings in the generated delay table; the generator was corrected, its table regenerated, and the synchronized SI rebuilt. Build details are in `output_revision_projected/continued_11_tex_build_20261028.log`.