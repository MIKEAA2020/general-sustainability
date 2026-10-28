# ECOMOD C11 targeted-review follow-up — version-matched SI and code

**Date:** 2026-10-28  
**Relationship to original review:** Addendum; the original report remains unchanged as the assessment of its 35-page PDF input. This follow-up records the dispositions after the revised, version-matched C11 main text, SI, code, and run outputs were supplied.  
**C11 draft branch:** `agent/p06-ecomod-c11-local-draft-20261028`  
**C11 commit:** `d2b5e2c9e60c6e2a26b04a199dbe34064508251e`

## Version match

The original review assessed the 35-page main PDF with SHA-256 `1433afaf75dc43f318545a695277d7b05a31aeb950a1283de962829199ce43db`. The C11 draft branch has since been updated. The following are the exact artifacts in commit `d2b5e2c9e60c6e2a26b04a199dbe34064508251e` reviewed for this addendum:

| C11 artifact | Pages | SHA-256 |
|---|---:|---|
| `ecomod_continued_11_revision_draft_20261028.pdf` | 36 | `653b72b7f46a12d5fb7338f8d284bb5fe8fddfa27ada6464e6cadedeb4fd34a5` |
| `ecomod_continued_11_revision_draft_20261028_SI.pdf` | 23 | `7bd9535ae39b8a717b5674d46d5db989d4b5b29902c16447aeb8ac3818da16fe` |
| `ecomod_continued_11_revision_draft_20261028.tex` | — | `0b3b5e1ce614b7da20ebfedbed1e9c7826e5e70843b5f6bf005585ddfbc32798` |
| `ecomod_continued_11_revision_draft_20261028_SI.tex` | — | `fe04e90fb350f353d6ddd34a9fbe94a460700101fc05609d775046c54bb063e4` |
| `parts/si_00.tex` | — | `08278162b1c718ce7a6ef36a79def3df6291c923fe81b263db752d07f98d5d6f` |
| `parts/si_01.tex` | — | `5025a0e2e781437b2d188e90514aae0fb80f80c3ffb7b0b66df4ca63933a720f` |
| `parts/si_02.tex` | — | `1836a6201b17018d1bc7052b5dfce0f3b9d9dbc6b08045af7cd48dfc8d0757e8` |
| `work/verify_debt_equilibria_c11.py` | — | `02b1f60d0330f878b183d699f6549e902f8e68692db7190aff415c446032165c` |
| `drawdown_depth.py` | — | `d439b3fd3d23c091aa63d320a72e9a45d4fed126ae0a6a0f0fda68e6a901a106` |
| `work/recovery_metric_and_tau_p_scan.py` | — | `fe0ee7474e02f0d06ad226ef2a65cda4be99ec5b33d0bfee911356b35456307b` |

The C11-local checksum manifest and verification record are in the same branch. This follow-up does not treat the old PDF extraction or its missing-SI status as evidence about the new version.

## Revised findings and dispositions

### Core C10 audit findings

- **E1, projected quality law — addressed.** The main specification retains the projected delayed-quality law, admissible history, and imposed quality interval. The version-matched SI now includes a method-of-steps uniqueness/invariance statement for the nonnegative delayed input; it does not transfer raw unconstrained-DDE characteristic roots to the projected system.
- **E2, 20/40-year delay comparison — addressed with scope.** The matching baseline paths are identified as saturation-induced degeneracy, not general delay robustness.
- **E3, population-delay classification — addressed.** The delay is located in carrying capacity, not population's own crowding term; the Hutchinson stability classification is not retained.
- **E4, debt derivative — verified in version-matched SI.** The deficit-active debt row includes `partial D_dot/partial D = alpha b_f A_f - eta`; the spectrum is confined to its stated one-sided active branch.
- **E5, recovery endpoint — reconciled.** The correctly configured projected solver (`A_tot=2.5`, `chi_r=0.10`) gives `A_c(400)=0.6771 ha` and recovery fraction `0.4634`, consistent with the displayed `0.677 ha` and `0.46` at `dt=0.1 yr`.
- **E6, equality families — addressed.** The equality point, fixed-demand surplus no-conversion family, and endogenous-population equality family are distinguished; the deficit-side spectrum is not presented as two-sided stability of an isolated equality point.

### R1 — sign of net aggregate change

The identity is retained, but the conversion term is no longer said to determine the sign of net `B_dot` “only if” maintenance balances retirement and quality is unchanged. Those restrictions are sufficient, not necessary, and the net sign depends on active terms. The pointwise comparison is separated from a claimed trajectory closure. With `M=mu A_r-eta_f A_f` and restoration off, the SI gives `M_dot=-(mu+eta_f)M-eta_f u_c`, so `M=0` is not invariant during active conversion.

The checked counterexample remains valid: conversion contribution `+0.131764706 gha/yr`, nonzero maintenance contribution `-0.025500000 gha/yr`, net `B_dot=+0.106264706 gha/yr`.

### R2 — B-only control and the capital-land floor

The universal B-only impossibility claim is replaced by the narrower information limitation: aggregate `B` does not reconstruct `A_c` or implement arbitrary `A_c`-dependent policies. For `y=A_c-A_c^min>=0`, the stated law gives `0<=u_c<=y/tau_conv`; with `R_rc>=0`, `y_dot>=-y/tau_conv`, hence `y(t)>=y(0) exp(-t/tau_conv)`. This continuous-time bound preserves the floor from safe starts; a no-conversion policy also does so. Any impossibility claim subject to a provision objective would require a specified controller class, uncertainty set, and objective.

### R3 — debt roots and matched demand inputs

The revised main text and SI use unrounded, matched demands based on `E_ceil=1.138409090909 gha`. The versioned script `work/verify_debt_equilibria_c11.py` independently bisects each root and integrates the canonical projected solver from the matching floor state (`D(0)=0`, `q(0)=q_max`, `dt=0.1 yr`, `T=1200 yr`).

| Demand | `D*` (gha yr) | `B(D*)` (gha) | `S*` (gha) | Integrated `D(T)` |
|---|---:|---:|---:|---:|
| `E_ceil + 0.02 = 1.158409090909 gha` | 1.209654900 | 1.097926346 | 0.060482745 | 1.209654898 |
| `E_ceil + 0.10 = 1.238409090909 gha` | 5.394537512 | 0.968682215 | 0.269726876 | 5.394537512 |

These resolve the mismatch for the stated unrounded inputs. They do not identify which rounded input sequence produced any earlier author-run value.

### R4 — reserve floor and gate-table windows

`A_r^min=0.10 ha` is now explicitly a post-hoc monitor, not an invariant enforced by area reconstruction. The drawdown state with `A_c0=1.18 ha`, `A_f0=0.6 ha`, and `A_tot=2.5 ha` starts at `A_r0=0.72 ha`, correcting the earlier `at least 0.80 ha` statement.

The versioned drawdown grid (`dt=0.1 yr`) has minimum reserve `0.511011156 ha` with `chi_r=0.10` and `0.600000000 ha` with `chi_r=0`; the gate comparison's minimum is `0.602 ha`. Both tested sweeps also report maximum `A_f=1.617006141 ha`. These are run-specific checks, not a global invariance proof. The optional `A_f^max` ceiling is not enforced in the reported model.

The SI gate helper now includes `t=0` in extrema: the no-restoration row's maximum `A_c` is `0.058 ha`, not `0.057 ha`. Its caption separates recovery metrics at `T=100,900 yr`, end-state columns at `T=2000 yr`, and extrema over inclusive `[0,2000] yr`.

### R5 and remaining SI scope

- Supply-only identification is scoped to the observation relation: it constrains at most `b_G,c rho_c` (given `q_max`); informative quality trajectories could identify dynamic parameters under additional known-history/input conditions.
- The additive comparator has a distinct `alpha_add`, with units `ha^-1 yr^-1`, not the units of multiplicative `alpha`.
- The transient debt bound retains `D(0)`, and `S^dagger` is described as a sustained-shortfall asymptotic comparison, not a transient threshold.
- Monotonicity statements are limited to the tested finite grids/bisections; no general continuity theorem is claimed.
- Unreproduced cross-study forest/fish recovery-fit medians were removed from the main/SI narrative. The references remain measurement context; no harmonized recovery-curve fit is claimed.

## Reproducibility checks and residual limits

The version-matched `python check_c11_sources.py` passed. The C11 build completed with three ordered passes per document using Tectonic 0.17.0 because pdfLaTeX was unavailable in the workspace. The rebuilt main and SI have 36 and 23 pages. PDF inspection confirmed the title, mailto and ORCID links. No unresolved labels/citations or float-overflow warnings remained; the log records one 2.608 pt first-page overfull box and nonfatal underfull/PDF-string warnings.

One numerical discrepancy remains open: the canonical SI/main population-refinement figures report maximum errors `0.000252` and `0.000118 cap`; rerunning the versioned solver against the stated `dt=0.003125 yr` reference gives `0.000244934` and `0.000114441 cap`. The `A_c`, `B`, and `D` errors reproduce at the displayed precision. This small mismatch is disclosed, not silently resolved.

The original review's historical C10 producer-to-output questions remain separate. Neither these corrections nor the tested reserve minima establish a universal reserve-floor invariant or historical provenance for earlier C10 runs.
