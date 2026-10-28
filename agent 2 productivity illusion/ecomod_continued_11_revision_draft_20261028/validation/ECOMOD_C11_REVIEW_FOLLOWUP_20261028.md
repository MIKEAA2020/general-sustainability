# ECOMOD Continued 11 — verified targeted-review follow-up

**Date:** 2026-10-28
**Scope:** version-matched C11 main manuscript, SI, projected solver, and supporting run outputs in this draft package.
**Status:** verified review findings applied; source checks and numerical reruns passed; main and SI rebuilt. This is a draft update, not a release or publication.

## Scope and boundary

This follow-up applies the R1–R5 and SI/table corrections identified during the completed C11 review. The manuscript/SI edits are in `parts/`; the assembled TeX and PDFs were rebuilt from those sources. The historical C10 provenance and hard-bound audit records were not modified. Results below distinguish tested-run evidence from mathematical invariance.

## Verified findings and changes

### R1 — conversion contribution and aggregate change

The identity in Proposition 1 is retained, but the statement is now sufficient rather than “only if”: with no restoration, fixed debt, maintenance balance, and unchanged quality, the conversion term is the only term in the identity and determines the sign of net `B_dot`. If the other terms are active, their magnitudes also matter. The proof now gives, for `M = mu A_r - eta_f A_f`,

`M_dot = -(mu + eta_f) M - eta_f u_c`.

Thus `M = 0` is not invariant during active conversion. The reduced comparison is identified as pointwise, not as a trajectory result. An admissible checked example also confirmed that the sufficient conditions are not necessary: a positive conversion contribution `+0.131764706 gha/yr` and nonzero maintenance contribution `-0.025500000 gha/yr` yield positive net `B_dot = +0.106264706 gha/yr`.

### R2 — B-only information and the capital-land floor

The overbroad controller-impossibility language has been removed. For `y = A_c - A_c^min >= 0`, the stated rate law satisfies `0 <= u_c <= y/tau_conv`; with nonnegative restoration, `y_dot >= -y/tau_conv`, and hence `y(t) >= y(0) exp(-t/tau_conv)`. This continuous-time bound protects the capital-land floor from safe initial states. A no-conversion policy also preserves it. Aggregate `B` does not identify `A_c` or support arbitrary `A_c`-dependent rules, but that information limitation alone is not universal control impossibility; any claim conditional on a provision objective must specify the controller class, state uncertainty, and objective.

### R3 — matched debt inputs and fixed points

The fixed-point roots and solver integrations now use the same unrounded demand inputs. With `A_tot=2.5 ha`, `A_c^min=0.05 ha`, `k=mu/(mu+eta_f)=0.545454545455`, the maintenance-balanced floor allocation has `A_f=1.336363636364 ha`, `A_r=1.113636363636 ha`, and `E_ceil=1.138409090909 gha`.

| Demand | Fixed point `D*` (gha yr) | `B(D*)` (gha) | Persistent shortfall (gha) | Euler result, `T=1200 yr`, `dt=0.1 yr` |
|---|---:|---:|---:|---:|
| `E_ceil + 0.02 = 1.158409090909 gha` | 1.209654900 | 1.097926346 | 0.060482745 | `D(T)=1.209654898` |
| `E_ceil + 0.10 = 1.238409090909 gha` | 5.394537512 | 0.968682215 | 0.269726876 | `D(T)=5.394537512` |

The reproducible calculation is `work/verify_debt_equilibria_c11.py`; its output is retained at `output_revision_projected/debt_equilibria_review_followup_20261028.log`. These are scenario values; they do not resolve which rounded or unrounded input sequence produced a prior author-run value.

### R4 — reserve threshold, run evidence, and SI gate-table windows

`A_r^min=0.10 ha` is now identified as a post-hoc monitoring threshold, not a constraint enforced by area reconstruction. The drawdown initial state `A_c0=1.18 ha`, `A_f0=0.6 ha`, `A_tot=2.5 ha` therefore has `A_r0=0.72 ha`, not at least `0.80 ha`.

`drawdown_depth.py` now records minimum reserve and maximum fast-land area for each tested row. Across its `dt=0.1 yr` grid, minimum reserve was `0.511011156 ha` for `chi_r=0.10` and `0.600000000 ha` for `chi_r=0`; maximum `A_f` was `1.617006141 ha` in both tested sweeps. The SI gate comparison has a minimum reserve of `0.602 ha`. These finite tested-run minima exceed the monitor but do not establish an invariant. `A_f^max` is documented as an optional ceiling not imposed in the reported runs.

The gate-integrator extrema now include the initial state (`t=0`); the no-restoration maximum `A_c` in the gate table is therefore `0.058 ha`, not `0.057 ha`. The caption now states that `R_c` is reported at `T=100` and `900 yr`, end-state fields are at `T=2000 yr`, and trajectory extrema/peak debt use the inclusive interval `[0,2000] yr`. The exact outputs are retained in `output_revision_projected/gate_extrema_review_followup_20261028.log`.

### R5 and SI/table corrections

- Supply-only identification is scoped to the observation relation: observations of `Upsilon(q)` over interior `q` values can constrain `b_c` and the product `b_G,c rho_c` (given `q_max`), but do not by themselves establish dynamic non-identifiability. Informative quality trajectories could identify dynamic parameters under additional known-input/history assumptions.
- The additive comparator uses a distinct `alpha_add` with units `ha^-1 yr^-1`; this is dimensionally distinct from multiplicative `alpha` in `exp(-alpha D)`.
- Transient debt bounds retain `D(0)`: `D(t) <= max{D(0), S_bar/eta}`. The crossover `S^dagger` is described as an asymptotic comparison for a sustained shortfall, not a transient trajectory threshold.
- Monotonicity is reported only across the tested finite grid/bisections; no general continuity theorem is claimed.
- Forest, fisheries, and soil references remain as measurement context, but the SI no longer presents cross-study `t_50`/`tau_r` medians as locally reproduced fits; the source data and harmonized fit generator were not present in this package.
- The projected delayed-quality law is accompanied by a method-of-steps uniqueness/invariance statement scoped to its nonnegative delayed input and interval projection.

## Source/code checks and build

Executed in the C11 package:

- `python drawdown_depth.py` regenerated `si_drawdown_depth.csv` with new `minAr`/`maxAf` diagnostics; the displayed drawdown/recovery table values were regenerated from that CSV.
- `python work/verify_debt_equilibria_c11.py` reproduced both debt roots and matched integrations above.
- The SI gate integrator was run via `work/recovery_metric_and_tau_p_scan.py:s54()` after correcting its extrema window.
- `python assemble.py` and `python check_c11_sources.py` pass. The source checker now guards the pointwise/noninvariant statement, reserve-monitor scope, matched debt inputs, transient initial-debt term, finite-grid qualification, comparator coefficient, empirical-fit scope, and `t=0` extrema in the helper code.
- `build_c11.sh` was run with Tectonic 0.17.0 because `pdflatex` is not installed in this workspace. The build script now supports Tectonic as a portable fallback while retaining pdfLaTeX as its default. Three ordered passes were completed for the main document and three for the SI.
- PDF artifact inspection with `pypdf` confirms the restored title and clickable mailto and ORCID annotations in both files, with no unresolved markers. Visual spot-checks rendered from the final PDFs cover the title page, the revised main parameter table/debt discussion/policy section, the SI symbols and numerical-method pages, the corrected gate table, and the final pages; no clipping or overlap was seen. Current selected-page renders are retained under `output_submission_cleanup_20261028/renders/`.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `ecomod_continued_11_revision_draft_20261028.pdf` | 36 | `653b72b7f46a12d5fb7338f8d284bb5fe8fddfa27ada6464e6cadedeb4fd34a5` |
| `ecomod_continued_11_revision_draft_20261028_SI.pdf` | 23 | `7bd9535ae39b8a717b5674d46d5db989d4b5b29902c16447aeb8ac3818da16fe` |

Final PDF checks are retained in `output_submission_cleanup_20261028/pdf_artifact_check.log`; build logs and the source-check log are under `output_submission_cleanup_20261028/`. There are no unresolved labels/citations or float overflow warnings. Tectonic reports one 2.608 pt overfull box during first-page output, nonfatal title/author PDF-string warnings, and underfull boxes in dense table/bibliography material.

The refreshed `SHA256SUMS_C11_LOCAL_20261028.txt` is a C11-local manifest only; no historical v45/C10 checksum list was changed.
