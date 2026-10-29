# Audit of `ecomod_C17_SI.tex`

**Target:** `batch 9/agent 2/ecomod_c17/ecomod_C17_SI.tex` in the C17 package on `origin/main` (704 lines / 10,370 words).
**Audit date:** 2026-10-29.
**Scope:** derivations, numerical tables, empirical support, package/build dependencies, and consistency with the C17 main manuscript. The SI source and its package outputs were inspected. I did not rerun every supplementary experiment or the empirical NFA/OWID calculations.

## Overall assessment

**The SI is technically detailed and generally careful about scope.** The displayed proofs for the composition and contribution-budget identities, the deficit-side affine system, debt fixed points, log-mean decomposition, and static identified sets are internally coherent under the stated assumptions. It consistently separates the model's uncalibrated states from physical ecological observations, identifies the projected delay paths' saturation-induced equality, and avoids turning finite-grid or model outputs into general ecological claims.

The C17 package contains the compiled SI PDF; its SHA-256 matches `metadata/document_verification.json` (27 pages; that metadata reports zero compiler warnings, overfull boxes, or unresolved references/citations). Internal `\ref` targets and citation keys resolve, and the four `\input` table files plus the five figure assets are present. I did not rebuild the PDF because `latexmk` is unavailable in this environment.

The main action items are reproducibility and traceability: the SI says its full drawdown grid is in `si_drawdown_depth.csv`, but that file is not included in the C17 package; several other supplementary experiment groups (gate-sign and one-stock comparator results) also lack a C17-versioned executable/data source. In addition, the detailed NFA/proxy results have no packaged annual input extract or transformation script. These do not establish that the reported values are wrong, but they limit independent reproduction.

## 1. Mathematical and numerical checks

### 1.1 Derivations — No major algebraic error found

- Differentiating \(B=b_fA_f+\Upsilon(q)A_c\) and substituting the land-flow equations gives the SI's five-channel budget: conversion, maintenance/retirement, quality readout, restoration, and fast-yield change. The technology/debt split in \(\dot b_f=e^{-\alpha D}\dot T_b-\alpha b_f\dot D\) is correct.
- The deficit-side matrix, its trace and determinant, and the statement that its spectrum is constant along the specified frozen-parameter branch are consistent with the main text. The qualification that this is a one-sided, active-shortfall spectrum—not a two-sided stability classification at \(S=0\)—is important and is stated.
- The delayed projected quality path's convergence argument is appropriate for the nonnegative logistic input and imposed upper bound. The SI correctly avoids importing characteristic roots from the raw unconstrained delay equation and distinguishes the delay in carrying capacity from a delay in population's own crowding term.
- The debt fixed-point monotonicity condition \(\eta>\alpha b_{f0}k(A_{tot}-A_c^{\min})\) is the derivative condition needed for uniqueness at the floor. The reported baseline values are consistent with that condition.
- The log-mean Divisia identity is exact when the stated endpoint components are positive. The fallback to a level identity when the residual is nonpositive is appropriate. The tables correctly show that proxy contributions change with the 1961 anchor and are not physical-stock attributions.
- The static bounds and endpoint witnesses are consistent with the assumptions of an independently attainable yield interval and exact inputs. As the SI says, they are not dynamic reachability sets or confidence intervals.

### 1.2 Numerical reporting — Rounded values occasionally look like exact floor hits

**Location:** S3 drawdown-depth table, especially rows printed as `0.050`.

The model's continuous bound \(A_c-A_c^{\min}\ge(A_c(0)-A_c^{\min})e^{-t/\tau_{conv}}\) means trajectories approach, but do not reach, the floor in finite time under the stated conversion law. Yet several entries in the table round to `0.050` at three decimals. An older `manuscript_ECOMOD_v44_src/si_drawdown_depth.csv` in the repository shows, for example, positive distances above the floor for the corresponding high-demand runs; the C17 SI's rounded entries obscure those distances.

**Action:** add a note that entries displayed as 0.050 are rounded values above the floor, or increase precision/use `>0.050` for those cells. This would align the table with the asymptotic-floor statement and avoid suggesting that numerical clipping occurred in the drawdown grid.

The 1961–2022 component contributions also sum to 24.5451 percentage points using the individually displayed rows, versus the total 24.5450. This is consistent with independent rounding of the unrounded inputs; a short rounding note would prevent an apparent 0.0001-point discrepancy.

## 2. Reproducibility and traceability findings

### 2.1 Cited drawdown CSV is absent from the C17 package — High

**Location:** S3, line 227: “the full \(P_0\) grid … is in `si_drawdown_depth.csv`.”

That CSV is not present in the C17 directory or C17 artifact manifest. A similarly named CSV exists under an older v44 source tree, but the SI does not point readers there and does not establish that the older copy is the exact C17 result. The C17 package's active `simulate_budgets.py` does not generate the S3 drawdown grid.

**Action:** include the exact CSV in C17 and add it to the manifest, or provide a versioned script/configuration that regenerates it and update the prose to give the actual stable path. The rounded table alone is not a substitute for the explicitly promised full grid.

### 2.2 S4 gate-sign and S7 one-stock calculations lack current-package reproduction artifacts — Moderate

The C17 package's executable numerical implementation covers four M1/M2 budget conditions and the static identification bounds. It does not implement the gate-sign sweep in S4 or the one-stock comparator's trajectories, finite-grid classification, or reported characteristic roots in S7. The four one-stock figures are documented as extracted from an earlier PDF; C17 includes the images but not their generating script or underlying grid/trajectory data. The equations, parameters, and selected conditions are described, but a reader cannot independently regenerate these supplementary results from the C17 package as it stands.

**Action:** add versioned scripts/configurations and compact outputs for the S4/S7 results, or identify the exact prior source artifact and version that reproduces them. Keep the explicit statement that S7 is a separate comparator, not a reduction or stability result for the two-land model.

### 2.3 Empirical endpoints and proxy are not independently reproducible from C17 — High

**Locations:** S5 Data and vintages, endpoint table, Divisia sensitivity, cropland calibration, and associated figures; C17 package metadata/data files.

The SI gives useful field names, edition, vintages, years, endpoint values, and OWID definitions. However, the C17 package contains no extracted annual NFA/OWID input series and no script that regenerates the endpoint table, component contributions, first year \(E_{prod}/B>1\), or proxy/anchor sensitivity table. The manifest includes the published figures but no corresponding derived empirical series. This is consistent with the main-paper audit: empirical claims are cited and qualified, but the source computations cannot be independently reproduced from C17 artifacts alone.

**Action:** add a derived annual series and a script for the exact NFA fields, population conversion, OWID area/yield merge, Divisia decomposition, and sensitivity/fallback rules. Record source release identifiers and file hashes; if raw source files cannot be redistributed, document their exact acquisition/version and checksums. Regenerate the empirical figures from this pipeline or state their provenance and non-reproducible inputs explicitly.

### 2.4 `C` is reused for two different residuals — Low

**Locations:** Symbols table S1, empirical proxy sections S5, and static identification proof S9.

The symbols table defines \(C=B-X\) as the empirical crop-proxy remainder. In the static bounds proof, \(C=B-b_fA_f\) is the model observation residual. The quantities are structurally analogous but not generally identical because the empirical proxy uses \(\hat b_f\), not model yield \(b_f\), and is expressly not assumed equal to model capital contribution.

**Action:** use distinct notation (for example, \(C_{proxy}\) and \(C_{obs}\)) or explicitly state when the same letter is being locally redefined. This would reduce the risk of conflating an empirical residual with the identified model product.

### 2.5 Explain the one-stock comparator's two shortfall/account operators — Low to Moderate

**Location:** S7 equations, lines 474–487.

In the comparator, total account value is \(B=bA+b_GG(A)\), but the area-conversion rule responds to \([E-\sigma bA]_+\), whereas debt responds to \([E-B]_+\). These are distinct gaps. The comparator is carefully labelled as separate from the two-land model, but the SI does not explain why the regeneration-value term enters the reported aggregate \(B\) but not the human-available term driving conversion.

**Action:** state the interpretation of the two operators (for example, whether the growth-linked component is counted in the aggregate but not immediately available to meet demand), and avoid comparing its threshold or trajectory directly with the two-land model without that distinction.

## 3. Consistency with the main manuscript

- The SI's main-model assumptions and results generally match the main source, including the fixed-demand scenario's exogenous demand override (population still evolves), the one-sided affine spectrum, and the conditional status of the “no fold” result.
- The explanation that \(q\) can rise while \(\Upsilon(q)\) falls is particularly useful here: the yield readout is non-monotone and peaks at \(q=1/2\). Retain this caveat anywhere the state is called “quality”; it is not an empirical ecological-condition measure.
- The SI's empirical section reinforces the main manuscript's distinction between NFA account values and physical stocks. The main-paper recommendations about packaging the empirical input data/code and making “testable predictions” more operational remain applicable.

## Bottom line

The SI's derivations and core model identities are sound under their stated assumptions, and the compiled package passes its recorded document checks. The biggest correction is to supply the specifically cited `si_drawdown_depth.csv` and reproducibility artifacts for supplementary experiment groups not covered by the current C17 simulation script. Clarify rounded near-floor entries, distinguish the two uses of \(C\), and explain the one-stock comparator's different conversion/debt shortfall definitions. The NFA/OWID tables also need an auditable data-processing path; no physical-stock inference should be added without independent observations.
