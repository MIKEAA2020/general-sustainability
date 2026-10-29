# Audit resolution and source-change account — C18 A01

Date: 2026-10-30. Basis: C17 main audit commit `44f48861d6c20a3a8419798d18f03b16130ebbef` and SI audit commit `8c4691ca927d1abcfb6368a4c1198c56208ad180`. Exact audit texts are retained as references in `evidence/`.

## 1. Repository-first recovery, before supplementation

The full repository tree was searched at pinned main `d21febdf35aff3b2f38c4f61b1cdbd551a220373`. Recovery covers 189 files, including the entire C17 package, historical v42–v44 drawdown CSVs/scripts, earlier model/empirical routines, and the original 2026 workbook and OWID snapshots in `batch 9/agent 2/ecomod_audit/reference/`. Each recovered file is checked against its Git blob and SHA-256; recovery itself is not treated as proof of model/version equivalence.

**Correction to the missing-file interpretation:** the drawdown file and primary empirical inputs were missing from the C17 package, not from the repository. The user's v42 lead was valid. v42/v43 numerical drawdown values match, but v44 final recovery endpoints differ: for initial Ac=0.4, P=1, the final restoration area changes from 1.26155303334 to 1.19049347087. v44 uses corrected histories. Its CSV additionally belongs to the current-quality comparator: the current-quality implementation matches every v44 minimum within 5.6e-16 and every final area within 1.5e-15. It cannot be relabelled as the exact selected delayed-quality artifact. C18 therefore preserves the old files and regenerates a clearly versioned selected-model grid.

## 2. Finding-by-finding disposition

| Audit item | Action and evidence | Disposition |
|---|---|---|
| Empirical inputs, pipeline and hashes absent from C17 | Recovered exact NFA Edition 2026 v1.0 workbook and OWID CSV snapshots; produced 63-year joined data, population conversion, endpoints, five components, first crossing, LMDI anchors/fallback, crop calibration, source registry and regenerated main Figures 2–3. | Closed as a package reproducibility gap. |
| Promised drawdown CSV absent from C17 | Recovered v42–v44 originals, established current/delayed distinction, regenerated 248 selected-model rows plus bisections and law sensitivity. SI now names the actual versioned path. | Closed. |
| Gate-sign executable/data absent | Reimplemented nine disclosed interventions with the selected delayed-quality law; outputs at dt=0.1, 0.05, 0.025, complete extrema, fixed reference convention and separate B/E. Replaced displayed rows with generated inputs. | Closed for the stated policies; no field-validation claim. |
| One-stock executable/data/roots absent | Implemented exact positive part, RK4 with substage delayed interpolation, current-G account readout, constant prehistory, floor, full trajectory, fixed-demand mask/sweep, delay pair, all 416 grid cells and characteristic equation roots. Regenerated all four figures. | Closed for the stated comparator. |
| Non-monotone quality/readout | First-use warning plus explicit growth-flow interpretation, symmetric/noninjective observation function, baseline numerical change and independent physical-mapping requirement. Equation retained. | Closed as a labeling/interpretation issue. |
| Fixed-demand override | Main Methods explicitly sets E=constant and restoration off while population continues to evolve. An executable test checks that the override changes demand linkage, not population dynamics. | Closed. |
| Operational empirical prediction map | Added SI S11 with independent observables, parameters/calibration, estimands and rejection outcomes for all five items, sampling, uncertainty, dependence and prospective-test requirements. Main points to and summarizes it. P4 is distinguished as cap/history consistency rather than empirical generality. | Operationalization closed; actual physical dynamic validation remains unperformed. |
| Rounded floor entries | Explicit note: 0.050 entries are rounded values above the floor; CSV includes the gap. Example gap is 4.60e-7 ha at Ac0=1, P0=3. Finite arithmetic caveat distinguished from the continuous bound. | Closed. |
| Component sums and printed rounding | Annual component–total residual retained, not forcibly balanced: maximum 2 gha, relative <2e-10. Explained the 2022 independently rounded 0.0001-percentage-point sum discrepancy. | Closed. |
| Empirical/model residual C conflated by notation | Distinct C^emp and C^mod in main/SI, symbol table and model bounds/proof. Empirical residual not substituted for the capital contribution. | Closed. |
| Comparator conversion versus debt gaps | Added interpretation of immediately available fast output versus growth-valued aggregate; explains why conversion can be active at E≤B and why thresholds are not transferable to two-land model. Notes negative logistic growth above Amax. | Closed. |

## 3. Numerical results and independent execution scope

- Full preserved budget verification rerun: **28/28 trajectories**, with the existing static sets, witnesses, chain-rule and decreasing closure checks passing. This is a fresh execution, not reliance on the main auditor's report.
- New compiled two-land implementation matches the separate preserved C17 F100 and R400 state arrays exactly at dt=0.05.
- Drawdown bisections at dt=0.05, T=1000: P0 = **2.40984841359, 2.70017253143, 2.97752223954, 3.14036184458** for Ac0 = 0.4, 0.7, 1.0, 1.18. The selected Ac0=1 coarse-step threshold rounds to **2.954**, while the current-quality sensitivity rounds to **2.955**. One SI sentence carrying the latter value for the selected law was corrected; the pre-existing delay table already made the distinction.
- No substantive displayed drawdown/recovery/gate conclusion changed at its stated precision. The complete full-precision outputs now identify the selected specification.
- Empirical results reproduce: log B change **0.221997**; log per-person change **−0.748840**; first production-footprint/B crossing **1973**; central proxy terms **+0.268662, +0.037710, −0.084375**. Maximum log-identity error 3.4e-16 and LMDI closure 3.7e-15.
- One-stock positive real roots: **0.588333333333** without delays and **0.624999996792** at (30,25); neutral-root residual zero. These establish the stated roots, not a certified complete spectrum.
- Comparator masking interval: **2.13–5.14 yr**, width **3.01 yr**. A falls 0.936535→0.866584 while B rises 0.575175→0.600091.
- Comparator finite grid: **83/208** high endpoints at regeneration delay 0, **11/208** at 30 yr; no intermediate endpoints under the declared cutoffs. These remain finite-grid categories, not basin probabilities.
- Full comparator floor contact refines **720.800→720.750→720.725 yr**. Peak debt refines **21.8074→21.6377→21.5539**; numerical sensitivity is reported explicitly, not disguised as ecological precision.
- New regressions: **40 tests passing normally and 40 under python -O**. This includes preserved-source hash/blob identity, annual transformations, snapshot/version distinction, model cases, override, threshold, gate, comparator and source-structure checks.

## 4. Complete substantive source-change account

The exact line-level changes are `evidence/source_diff_main_C18_A01.patch` and `evidence/source_diff_SI_C18_A01.patch`; the deterministic constructor is `code/prepare_revision_C18_A01.py`.

**Main additions:** first-use and Results state/readout explanation; explicit fixed-demand intervention; short empirical-test-design paragraph; current-package availability, attribution and hash statement; table rounding note. The empirical-prediction sentence is selectively clarified and linked to the operational map, rather than leaving an unoperationalized empirical label. All three main figures are regenerated from the selected model or recovered exact empirical snapshots.

**SI additions:** distinct residual symbols; rounded-floor note and actual CSV path; generated selected-model drawdown, recovery and gate rows; gate reference/timestep details; annual transformation and source-rounding note; comparator operator interpretation and numerical diagnostics; executable artifact map; S11 prediction/falsification protocol. Four comparator figures are regenerated from their stated equations. The coarse-step selected-law threshold is corrected from 2.955 to 2.954 in one sentence.

**Preserved without scientific compression:** all original section and proposition/equation/figure/table labels, the proofs and conditional claims, the original bibliography entries, author identity and ORCID, the existing model-bounds/budget table artifacts, and the original declarations. Existing narrative/analogies and conclusions are not wholesale replaced or shortened. Inline supplementary table bodies are replaced by equivalent generated row inputs, not removed. No old C17 source/PDF/data asset is edited; historical sources retain their bytes. Earlier manuscript versions and unrelated companions/deposits are outside the revision.

## 5. Build and visual QA

Main: **41 pages**; SI: **31 pages**, compared with preserved C17's 40/27. Final builds have **zero LaTeX warnings, zero overfull boxes and no unresolved references/citations**. There are three main and two SI underfull-box diagnostics, recorded rather than suppressed. All pages were checked in rendered contact views; the new figures, gates, comparator and long prediction table were additionally inspected at readable resolution. Overlapping close-demand annotations in Figure 1 were separated with leaders before finalization. Final hashes and diagnostics are in `metadata/document_verification_C18_A01.json`.

## 6. Remaining scientific boundary

No new common-boundary global physical-stock inventory, fitted physical observation map, causal ecological intervention study or field validation has been produced. Those cannot be obtained by relabelling NFA accounting residuals. The present closure is exact-source accounting reproduction, current-package model reproducibility and prospective empirical operationalization. This limitation remains explicit in the manuscript and must not be described as a successfully validated global ecological-capital model.

Publication is additive under a unique C18 path. The publication receipt separately records every prior remote path/hash/mode preserved and byte verification of the new package. No cleanup or merge is authorized or performed here.
