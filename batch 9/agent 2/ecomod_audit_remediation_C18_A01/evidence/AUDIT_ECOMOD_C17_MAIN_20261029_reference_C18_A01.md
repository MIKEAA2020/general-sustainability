# Audit of `ecomod_C17_main.tex`

**Target:** `batch 9/agent 2/ecomod_c17/ecomod_C17_main.tex` in the repository's `main` package (623 lines / 11,797 words; LaTeX source).
**Audit date:** 2026-10-29.
**Materials checked:** main source and its companion C17 package on `origin/main`, including SI, model code, derived numerical CSVs, figures, metadata, and PDFs. Model calculations were rerun from a temporary extraction; the empirical source datasets were not retrieved or independently recomputed.

## Overall assessment

**The paper is a carefully qualified, stylized model study with a descriptive NFA account decomposition. Its central mathematical claims are internally coherent, and the model's reported numerical calculations were reproducible from the included code.** It consistently distinguishes model-defined area and quality states from measured ecosystem stocks, and distinguishes NFA account movements from biomass, soil, wetland, or fish-stock changes. The static identified-set construction and the conditional conversion mechanism are correctly stated under their assumptions.

The primary actionable weakness is **reproducibility of the empirical NFA/OWID results**: the package contains the results in prose, tables, and images, but no annual source-data extract or script that regenerates the account decomposition and cropland-proxy calculations. The metadata hashes figure assets, but do not identify/checksum the NFA workbook and OWID input snapshots used for the reported estimates. This is not evidence that the numerical claims are wrong, but prevents independent reproduction of an important part of the paper.

A secondary conceptual point is that the model's “quality” index is a stylized state whose associated per-hectare account readout is **non-monotone** and depends on the quality-growth rate. The manuscript discloses this, but could make the terminology even harder to misread as a measured or monotone ecological-condition variable.

## 1. Substantive and mathematical checks

### 1.1 Conversion identity and interpretation — Coherent under stated assumptions

With \(B=b_fA_f+\Upsilon(q)A_c\), the land transfers conserve area and yield
\[
\dot B=(b_f-\Upsilon(q))u_c+b_f(\mu A_r-\eta_fA_f)+b_{G,c}G'_c(q)A_c\dot q+uR_{rc}+A_f\dot b_f.
\]
This matches the main text and SI. The conversion term is positive exactly when fast-land's modeled contribution per hectare exceeds the capital-land readout. The manuscript correctly cautions that this is not necessarily the sign of total \(\dot B\), since retirement/maintenance, quality, debt, technology, and restoration also contribute.

The fixed-demand balance formula, affine deficit-side Jacobian, determinant/trace conditions, and debt fixed-point condition are algebraically consistent for the reduced cases stated. The no-fold/no-critical-slowing result is properly restricted to the reduced equality relation and is not generalized to every full-model path or the separate surplus equilibrium family.

### 1.2 Static identification bounds — Correct under their explicit attainability assumption

The bounds for \(A_c\) from \(B\) alone and from \((B,A_f)\) follow from the area constraint and the stipulated independent, continuously attainable interval \(u\in[u_-,u_+]\), with \(0<u_-\le u_+<b_f\). The illustrative values reproduce the package results: the \(B\)-only set is approximately \([0.05,1.658163]\) ha; adding independently observed fast-land area narrows it to \([0.606061,0.8]\) ha; adding the stated \(q=0.9\) identifies about 0.717360 ha. These are static, deterministic compatibility sets, not confidence intervals or dynamically reachable ranges, as the manuscript says.

### 1.3 Model units, budget identity, and trajectories — Independently rerun

Units are internally consistent: \(G_c(q)\) has units yr\(^{-1}\), \(b_{G,c}G_c(q)\) has units gha ha\(^{-1}\), conversion/restoration are area flows, and the debt state \(D\) is in gha yr so \(\alpha D\) is dimensionless. The full contribution-budget identity includes conversion, maintenance/retirement, restoration, quality readout, and the derivative of fast-land yield; no term needs to be added or removed.

I installed the package's declared numerical requirements in a temporary environment and reran `code/simulate_budgets.py`, `code/verify_budgets.py --full`, `code/verify_manuscript_sources.py`, and `code/verify_reference_refinement.py` on an extracted copy of `origin/main` (no repository source files were changed). Results:

- All **28** condition/timestep trajectories recomputed; the verifier passed, including the static-bound check, endpoint witnesses, state/area guards, timestep-refinement closure, and source-integrity checks.
- The maximum discrepancy in 1,000 synthetic chain-rule checks was \(5.55\times10^{-17}\).
- The four finest-grid closure residuals and reported baseline budget terms reproduced. For the 100-year fixed-demand case, conversion contributes 0.547925 gha and the endpoint increase is 0.231310 gha; the residual is \(8.04\times10^{-5}\) gha. The restoration run's minimum and terminal capital area (0.401217 and 0.678295 ha) also reproduce.
- The fixed-demand timestep/reference diagnostics reproduce the main text's reported values.

This validates the package's stated numerical implementation for these specified histories and parameters; it is not empirical validation of the model or its ecological interpretation. The package also contains matching compiled PDFs and QA metadata reporting zero compiler warnings/overfull boxes/unresolved citations. I did not rebuild the PDFs locally because `latexmk` is not installed in this environment.

### 1.4 NFA account arithmetic — Internally plausible; input series not independently checked

The reported log identity \(0.970837-0.748840=0.221997\) is arithmetically consistent. Printed component contributions sum to the reported 2023 total within rounding; the 2022 figures differ from the total by 0.0001 percentage point at printed precision, consistent with independent rounding. The cropland proxy is correctly described as an index-scaled, base-year-anchored account split; the residual is not treated as physical capital. The selected central-anchor Divisia decomposition terms sum to the reported total log change at printed precision.

I did not retrieve the NFA workbook or OWID series (nor independently verify their release metadata), so the 1961/2023 source values, component percentages, first-crossing year, and proxy inputs remain claims supported by citations and package presentation, not a fresh data rerun.

## 2. Priority findings and actions

### 2.1 Empirical source data and processing are not reproducible from the C17 package — High

**Locations:** Data and empirical measures, lines 184–196 and 420–467; Figs. 2–3 and Table `nfa_components`; Data availability, lines 566–567; package `metadata/provenance.json` and `artifact_manifest.json`.

The package has no NFA workbook snapshot, annual world/component extract, OWID cropland/yield extract, or script that recalculates the empirical figures/table and proxy decomposition. The package's model scripts reproduce the simulations, identification sets, budgets, and associated numerical files, but not the reported NFA and OWID calculations. Moreover, `fig2_nfa_aggregation_face.png` and `fig3_composition_attribution.png` are documented as lossless extractions from a prior review PDF rather than figures generated from included empirical data/code. The provenance metadata hashes these image assets and gives their prior-PDF origin, but does not supply checksums for the underlying account/yield inputs. Thus the Data availability statement's assertion that source versions and file hashes are in metadata is not sufficiently substantiated for these empirical inputs.

**Action:** add either (a) a compact annual derived-data file for 1961–2023 (and 1961–2022 sensitivity) plus a script that recreates the per-capita measures, component attribution, first-crossing year, and proxy sensitivity, or (b) a precise reproducibility note identifying the source snapshots/release IDs, download dates, checksums, exact workbook fields, transformation code, and any licensing barrier to redistributing the source data. Generate Figs. 2–3 from that same reproducible pipeline. Keep the strong caveat that the account decomposition is not physical-stock evidence.

### 2.2 “Quality” state/readout deserves especially explicit labeling — Moderate

**Locations:** Eqs. (1)–(3), (10); Results lines 211–239 and 520; Limitations lines 540–542.

The state \(q\) is explicitly uncalibrated and nondecreasing, but the modeled capital-land readout is \(\Upsilon(q)=b_c+b_{G,c}\rho_cq(1-q/q_{\max})\). It peaks at \(q=q_{\max}/2\), then falls as \(q\) rises toward its imposed ceiling. The baseline example therefore has the “quality” state rise from 0.9 to 1 while its per-hectare readout falls. The text acknowledges that this is a property of the observation function, not a decline in the quality state, and does not interpret \(q\) as measured ecological condition. Still, “quality” may invite a monotone-condition interpretation.

**Action:** consider calling \(q\) a *regeneration/readout state* (or explicitly state at first use that larger \(q\) need not mean a larger annual account contribution). Alternatively, justify the non-monotone mapping as an intentional growth-flow contribution and keep the distinction visible in figure legends and conclusions. Do not describe the modeled fall in \(\Upsilon\) as a measured deterioration in ecological condition.

### 2.3 Make scenario overrides explicit in the main Methods — Low

**Locations:** Eq. (4), which defines \(E=eP\); fixed-demand results and Fig. 1a; SI S10.

The SI says population evolves during the fixed-demand budget condition while demand is held exogenous. This is a legitimate controlled comparison, but it overrides the general relation \(E=eP\). State that override next to the fixed-demand scenario in the main Methods, so the reader does not infer that population and demand are linked in that run.

### 2.4 “Falsifiable empirical predictions” need a data/criterion map — Moderate

**Locations:** Introduction's final paragraph and Results “Falsifiable predictions,” lines 468–477.

The paper is clear that parameters are illustrative and that aggregate \(B\) alone cannot test the predictions. Several numbered items are primarily model implications (e.g. the 20/40-year delay equality is a saturation artifact of the chosen initial history; restoration requires a specified return-flow rule). The labels “testable empirical predictions” can sound stronger than the present operationalization.

**Action:** either call these *model-derived empirical hypotheses/implications*, or add a brief table for each prediction specifying the observable, required independent data, model parameter(s) to estimate, and a result that would falsify it. Distinguish direct algebraic consequences of the chosen model from predictions robust to parameter/history variation.

## 3. Editorial/build checks

- **45 citation keys** have matching bibliography entries; no uncited/missing keys were found. All 52 labels are unique and every explicit `\\ref`/`\\eqref` target resolves.
- The main source's two `\\input` table rows and three main figures are present in the package. The package's C17 main PDF hash matches its document-verification metadata (40 pages; recorded zero warnings and unresolved references).
- The model's fixed-demand numerical scenario is made clear in the SI, but a one-sentence main-text clarification would improve consistency with \(E=eP\).

## Bottom line

The mathematical mechanism, sharp static bounds, and integrated model budgets are coherent under their explicit assumptions; the included numerical implementation passed a full 28-run recomputation. The article also draws a careful boundary around the NFA evidence: it analyzes annual account composition, not physical ecological stocks. Before submission, make the empirical NFA/OWID calculations reproducible (or narrow the availability claim), and keep the stylized, non-monotone quality/readout mapping unmistakably distinct from measured ecosystem condition. The scope and operationalization of the five “empirical predictions” could also be sharpened.
