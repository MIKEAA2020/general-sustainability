# ECOMOD C19 A01 — companion references and main/SI division decision

**Date:** 31 October 2026  
**Source:** published C18 A01, commit `688701d6053ea1d89a37b9c708ef29c9b2e8ddf5`  
**Revision:** additive C19 A01; C18, C17, unrelated companions, and all earlier packages remain unchanged.

## 1. Decision in brief

The main manuscript should remain a self-contained account of the model, mechanisms, essential numerical evidence, empirical account decomposition, conclusions, and limitations. The SI should remain the specialist layer for derivations, implementation diagnostics, full grids and sensitivity analyses, observation protocols, comparator experiments, endpoint witnesses, and reproduction detail.

The broad C18 allocation was therefore scientifically sound, but its execution needed four corrections:

1. replace the companion working-paper records with the posted DOI records;
2. make every retained SI figure and table explicitly visible at the relevant main-text claim;
3. remove duplicated main-text apparatus—a repeated yield-sweep panel, four full proofs already derived in SI, repeated numerical diagnostics, and repeated Discussion numbers—without removing any result or numerical evidence;
4. avoid carrying potentially stale theorem/section numbering from older companion working versions into citations of the newly posted versions.

No core result was moved out of the main. No new result, extended discussion, or unrelated reference was added to the SI. No equation, parameter value, simulation output, empirical observation, conclusion, or limitation was changed.

Final documents: **39-page main**, **31-page SI**; C18 was 41/31 pages.

## 2. Companion-reference resolution

Citation keys and claim scope are preserved.

| Key | Posted title | DOI now used | Records updated |
|---|---|---|---|
| `Abaee2026a` | *Governance Delay and the Stability of Harvested Stocks: Mobilising and Protective Feedback Rules, and the Review Interval as a Design Parameter* | [10.20944/preprints202610.3095.v1](https://doi.org/10.20944/preprints202610.3095.v1) | Main and SI |
| `Abaee2026b` | *Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules* | [10.20944/preprints202610.2983.v1](https://doi.org/10.20944/preprints202610.2983.v1) | Main and SI |
| `Abaee2026c` | *Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons* | [10.20944/preprints202610.3123.v1](https://doi.org/10.20944/preprints202610.3123.v1) | Main only; SI has no citation and therefore receives no unused bibliography entry |

The transition-certification title is materially different from C18’s working title, so changing only its URL would have left an incorrect record. Publisher pages verify the posted titles, version-1 status, and posting dates: 29 October 2026 for `.2983`, and 30 October 2026 for `.3095` and `.3123`. These are preprints, not represented as peer-reviewed publications.

Older working-version locators were not carried forward blindly. The main and SI now identify the transition companion’s **compensatory-acceptance result** and **diagonal-gap analysis** descriptively, and cite the ledger companion without the old section-number locator. The substantive claims are unchanged, while the references no longer depend on unverified theorem or section numbering from another version.

All three DOI links are embedded in the main PDF; the two cited DOI links are embedded in the SI PDF. The former GitHub “Manuscript” links and the superseded transition title are absent from both live documents, while remaining available in the frozen C18 sources for provenance.

## 3. Main-text placement by content

| Main location | Retained in main and why | Specialist material assigned to SI |
|---|---|---|
| §1 Introduction | Problem, account-versus-stock distinction, analogies, three research questions, contributions, and study boundary. These are necessary for a general reader. | No separate SI introduction or extended literature review. |
| §2.1 Two-land model | Complete state definitions, account equation, shortfall/conversion rule, conserved land flows, restoration gate, quality/population/debt equations, units, and feedback interpretations. | SI S1 supplies the full symbol/unit ledger and inactive-extension conventions; SI Table S1 is cited here through the parameter-table caption. |
| §2.2 Parameters and grounding | Baseline values and evidence status remain in main Table 1 because the simulations cannot be interpreted without them. | Recovery-study detail and non-calibration qualifications remain in SI S5.5. |
| §2.3 Data and empirical measures | NFA edition, years, exact workbook fields, account categories, population conversion, proxy boundary, and log identity. | Full annual processing, precision checks, Divisia details, proxy calibration/sensitivity, observation mappings, and measurement specifications remain in SI S5. |
| §2.4 Numerical implementation | Fixed-demand intervention, integration scheme, delay interpolation, projection/clipping, state bounds, histories, and timestep choices. The main remains sufficient to understand what was computed. | Exact finite-step error arrays and current-quality sensitivity remain in SI S3/Table S2. The main reports the checks’ scope without duplicating all diagnostics. |
| §3.1 Composition mask | Composition diagnostic, Proposition 1, baseline masking numbers, identification limitation, and main Fig. 1a. These are the paper’s central mechanism. | General varying-debt/quality/restoration identity in SI S2.1 and regime summary in SI Table S7. Main retains a one-sentence proof sketch. |
| §3.2 Minimum-area boundary, not a fold | Balance relation, affine matrix, no-fold/no-critical-slowing conclusion, demand ceiling, baseline eigenvalues, proximity values, and main Fig. 1b–c/Table 2. | Full yield sweep and slope in SI Table S3; minimum-area grid in SI Table S4; derivations and debt fixed-point detail in SI S2.2–S2.4. |
| §3.3 Technology and debt | Boundedness proposition, sustained-shortfall interpretation, and the essential matched peak-debt numbers. | Full wave/no-wave summaries in SI Table S13 and trajectories in SI Fig. S5. |
| §3.4 Recovery | Need for an explicit return flow, partial-recovery numbers, and gate-sign policy interpretation. | Full recovery cases in SI Table S5 and all nine gate/conversion-freeze policies at three timesteps in SI Table S6. |
| §3.5 Sharp static identification | Exact compatible-area formulas, assumptions, numerical intervals, and main Table 3. This is a named core contribution and part of the abstract, so it must remain main. | Sharpness/feasibility construction in SI S9, endpoint witnesses in SI Table S14, observation mapping in SI Table S10, and observability ladder in SI Table S11. |
| §3.6 Integrated contribution budgets | Full accounting identity, key fixed-demand and restoration contributions, closure interpretation, and main Table 4. | Four-condition budget in SI Table S15, technology/debt split in SI Table S16, and seven-step refinement in SI Table S17. |
| §3.7 NFA account composition | Aggregate/per-person results, component contributions, main Figs. 2–3 and Table 5, and the calibrated proxy result with its limitation. These are the essential empirical evidence. | Same-edition endpoint detail in SI Table S8 and anchor sensitivity in SI Table S9; annual processing and fallback protocols remain in SI S5. |
| §3.8 Falsifiable predictions | P1–P5 and the independent observations required to test them. | Operational estimands/rejection rules in SI Table S18 and sampling/uncertainty protocol in SI S11. |
| §4 Discussion | Synthesis, measurement and policy implications, relation to prior work, and limitations. Repeated Results numbers were compressed rather than repeated again. | One-stock comparator remains SI-only (Figs. S1–S4); the unpopulated physical-stock specification remains SI Table S12. Neither is allowed to become a second results narrative. |
| §5 Conclusions | All central model, identification, budget, NFA, recovery, and physical-stock boundary conclusions, including the key numerical values. | No conclusion is SI-only. |

### Why the main has three figures rather than padding to a larger count

The three main figures contain **eight panels**: three model-dynamics panels, three NFA aggregate/per-person panels, and two account-composition panels. They cover the central mechanism, drawdown response, empirical aggregate contrast, and component attribution.

SI Figs. S1–S4 concern a separate one-stock comparator, and SI Fig. S5 is an additional technology-wave control. Promoting them would increase the float count without improving the main argument and could blur the distinction between the two-land results and auxiliary controls. They therefore remain in SI, with explicit main-text citations at the exact claims they support.

The six main tables are likewise limited to baseline parameters, floor-proximity results, sharp identification intervals, key contribution budgets, NFA component evidence, and the compact scope summary. Full sweeps, grids, sensitivities, witnesses, and refinement tables remain in SI.

## 4. SI placement by section

| SI section | Role and placement decision |
|---|---|
| S1 Symbols and model extensions | Specialist notation, units, and inactive-extension conventions. Appropriate for SI; Table S1 is explicitly cited in main Methods. |
| S2 Derivations and proofs | Full mathematical derivations and branch/debt qualifications. Appropriate for SI; propositions and concise proof sketches remain main. |
| S3 Numerical methods and sensitivity | Complete update diagnostics and current-quality comparator. Appropriate for SI; Table S2 is explicitly cited in main Methods/Results. |
| S4 Extended model results | Full yield sweep, drawdown grid, recovery cases, gate policies, and regime table (S3–S7). Supporting detail, not hidden core findings; the main reports the essential values. |
| S5 Empirical details | Annual transformations, proxy decomposition/sensitivity, observation mappings, observability ladder, and unpopulated physical-stock specification (S8–S12). Appropriate for SI; the main retains the empirical results and limitations. |
| S6 Policy extensions | Reserved shares, typed floors, and institutional/aggregation comparisons. Supporting extensions remain here; the main retains the policy implications. |
| S7 One-stock comparator | Auxiliary formulation with Figs. S1–S4. Correctly kept out of the main results; the main explicitly warns that it is not evidence for the two-land state \(A_c\). |
| S8 Controlled technology wave | Matched control with Table S13/Fig. S5. Appropriate for SI; main retains the essential debt comparison. |
| S9 Identification proof and witnesses | Sharpness construction and Table S14. Appropriate for SI; exact interval formulas and example remain main. |
| S10 Budgets, refinement, and execution | Full budgets, technology/debt split, refinement, and executable map (S15–S17). Appropriate for SI; key budget evidence remains main. |
| S11 Operational prediction map | Independent observables, estimands, rejection outcomes, sampling and uncertainty protocol (S18). Appropriate for SI; predictions and data requirements remain main. |

## 5. Explicit SI-float linkage

Every retained SI float is named in the main PDF at the following relevant point:

| SI float(s) | Main-text citation point |
|---|---|
| Table S1 | Baseline parameter/evidence discussion in §2.2 |
| Table S2 | Numerical implementation in §2.4; delay sensitivity in §3.2 and the scope summary |
| Tables S3 and S4 | Fixed-demand/yield and drawdown results in §3.2 |
| Tables S5 and S6 | Recovery and restoration-gate results in §3.4 |
| Table S7 | Composition-premium/neutrality/discount definition in §3.1 |
| Tables S8 and S9 | NFA endpoint sensitivity and proxy-anchor sensitivity in §3.7 |
| Tables S10 and S11 | Observation packages and sharp identification in §3.5 |
| Table S12 | Physical-stock measurement limitation in §4.2 |
| Table S13 and Fig. S5 | Matched technology-wave/debt evidence in §3.3 |
| Figs. S1, S2, S3, S4 | One-stock comparator qualification in §4.1 |
| Table S14 | Sharpness and feasible endpoint witnesses in §3.5 |
| Tables S15, S16, S17 | Full budgets, technology/debt split, and refinement in §3.6 |
| Table S18 | Operational falsification map in §3.8 |

Automated checks confirm all 18 SI table citations and all 5 SI figure citations in both the main source and the extracted main-PDF text.

## 6. Compression, replacement, and deletion account

### Main-text compression without evidence loss

- **Duplicated yield-sweep panel removed:** former main Table 2(a) is no longer duplicated. All four rows and the additional balance-branch-slope column remain in SI Table S3; baseline values and the yield-sweep conclusion remain in main prose. Main Table 2 now contains only the floor-proximity results.
- **Four proof environments replaced by proof sketches:** Propositions 1–4, all equations, assumptions, and results remain main. Full derivations were already present in SI S2 and S9 and remain there unchanged.
- **Numerical diagnostics compressed:** the main retains algorithm, intervention, history, bounds, timestep, and validation-scope statements. Exact error arrays and current-quality comparisons remain in SI S3/Table S2.
- **Discussion repetition compressed:** duplicated NFA and baseline numbers remain in Results and Conclusions. The one-stock equilibrium equation and full comparator detail remain in SI S7; the main retains the monotone-illustration qualification and the warning against transferring comparator claims to the two-land model.
- **No SI results or discussion were added or deleted.** SI section titles and float labels are unchanged.

### Reference replacements

- Three main companion records and two cited SI companion records were replaced with posted titles and DOI links.
- The superseded transition title and old working-paper URLs were intentionally removed from the live documents; they remain in `inherited_C18/` for source history.
- Old theorem/section-number locators were replaced with descriptive, content-based locators; the claims themselves were not broadened or narrowed.
- No unused SI record for `Abaee2026c` was introduced.

### Layout-only change

The SI bibliography changed from `\small` to `\footnotesize` after the longer DOI records left only the final United Nations reference on a new page. No reference content was removed. The SI again ends cleanly on page 31.

### Package-selection account

C19 intentionally does **not** duplicate C18’s full 27 MB historical archive. It contains the exact inputs, frozen C18 sources, current numerical outputs, figure assets, and evidence needed for this editorial revision and its reproduction. Sixty-six inherited files are byte-verified against published C18; `requirements_C19_A01.txt` adds the PDF-test dependency, and `DATA_LICENSE_C19_A01.md` corrects package-specific paths while preserving attribution. This is not a deletion from C18 or any earlier package: the complete C18 archive remains preserved at its original local and remote paths.

No data file, figure, numerical result, manuscript section, citation key, or earlier version was deleted.

## 7. Verification completed

- Main/SI compilation: **39/31 pages**.
- LaTeX: **0 warnings, 0 overfull boxes, 0 unresolved references/citations**; four main and two SI underfull boxes were visually checked and are non-obstructive.
- Regression tests: **60/60 normal Python and 60/60 optimized Python** after the final reproduction-evidence check was added.
- Live reproduction in a disposable lean-package copy: all three pipelines passed; **26/26 numerical data files byte-identical**, **3/3 PNG figures byte-identical**, and **7/7 PDF figures matched in geometry and extracted content**.
- DOI hyperlink checks passed in the actual PDFs.
- All 23 SI floats are explicitly cited in the main source and visible main-PDF text.
- Full-page thumbnail review covered every page; readable review covered revised table/proof pages, the measurement/companion-citation page, both companion bibliographies, and the SI sweep page.
- Numerical evidence, physical-stock non-claims, author identity, ORCID, declarations, and attribution remain unchanged.
