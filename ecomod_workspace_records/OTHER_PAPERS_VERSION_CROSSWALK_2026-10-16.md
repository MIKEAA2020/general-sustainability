# Crosswalk audit: the other created paper editions

**Audit date:** 2026-10-16  
**Question:** Did any substantive result or useful earlier-version content disappear from the recently created editions, and does any omission merit restoration?

## Executive finding

**No unintentional, substantive omission that strongly merits restoration was found.** The apparent losses resolve into one of four categories: (1) retained in the new main text, (2) moved to the supplementary material, (3) adapted or corrected because the old wording/result was too broad or wrong, or (4) intentionally omitted because it was unsupported or irrelevant. I recommend **no new paper edition and no restoration commit** on the evidence reviewed.

The most visible candidates are not restore-worthy:

- Paper03 v23 drops v22's `fig_hierarchy`, a plot of a selected dilation expression. The corresponding dilation extrapolation is explicitly demoted to a caution and counterexample in v23 SM S6; restoring the figure as a result would risk reviving the overclaim.
- Paper02 v16 removes a cross-check against a minimax companion that its scripts could not regenerate; it should remain out until independently reproducible.
- Paper11 v67 retracts the earlier claim that cod's surplus production was weakly autocorrelated. The checked values are 0.71–0.91, the opposite of weak. The earlier claim should not be restored.

Two potentially concerning Paper11 details are **not missing**: the old E1 v69 regime-specific signal and prospective-test design are carried into v67's synthesis/discussion, and the clarification that M1b at an Allee threshold of zero is not the Schaefer model is in v67 SI S5.

## Scope and version identities

I refreshed the repository branch and tag refs on 2026-10-16 and searched the branch trees for the relevant filename families; I did not rely on the 2026-10-15 inventory alone. Current branch tips observed:

| Ref | Tip |
|---|---|
| `main` | `217d110f006ec4b6b43755e53350d7043b0d1ddc` |
| `e2-v3-source-year` | `1bf8ef315b8dae66bc50987ff1a8e404acc98264` |
| `lean-audit-v4` | `c2fe8fca63384cbf9243434d4213c6e74543a840` |
| `edwards-framework-e1` | `66a0a71f976e76df403425e85690d2c9dcb4c141` |
| `edwards-framework-e1-audit-implementation` | `8cf4ab0c6515aeb9c7a3dd55fb1e67eff299283a` |
| `archive/paper3-v48-workspace` | `0200b6dc75a51feb40728df07e855facbb791383` |

The latest audited created editions are:

| Lineage | Correct predecessor → current | Current location/status in the refreshed tree |
|---|---|---|
| ECOMOD productivity illusion | v41 → **v42** | v42 on `main`; other branches stop earlier |
| Paper01 obstruction calculus | v72 → **v73** | v73 on `main` and `e2-v3-source-year` |
| Paper02 probabilistic sufficiency | v15 → **v16** | v16 on `main` and `e2-v3-source-year` |
| Paper03 computational certification | v22 → **v23** | v23 on `main` and `e2-v3-source-year` |
| Paper04 minimax dual certificates | v19 → **v20** | v20 on `main` and `e2-v3-source-year` |
| Paper05 exact belief computation | v19 → **v20** | v20 on `main` and `e2-v3-source-year` |
| Paper06 assessment separation (renamed Paper1 line) | v70 → **v71** | v71 on `main` and `e2-v3-source-year`; stale-based `paper1` v64 remains in `superseded/` |
| Paper09 cod/Edwards certification | v43 → **v44** | v44 on `e2-v3-source-year`; Paper09b is a separate line |
| Paper11 forecasting baselines | v66 → **v67** | v67 on `main` and `e2-v3-source-year`; stale-based E1 v69 remains in `superseded/` |
| Paper11c worked-systems audit | v4 → **v5** | v5 on `main` and `e2-v3-source-year` |

Paper07 v54 is excluded because its v52-to-v53 and historical-v19 crosswalks have already been completed and pushed. Paper08 v48, Paper10 v53, and the separate `paper09b`/`paper10b`/`paper11b` lines were not new editions in the audited creation set. No paper version number was allocated during this audit.

## Method and status terms

For each lineage I compared the predecessor's available main source and supplementary source/notes with the current main **and** SI sources. I used the edition notes as a map, then checked the specific potentially missing blocks against the actual current text (including the stale-based Paper1 v64 and E1 v69 side editions). The archived verifier counts below are the versions' recorded checks; I did not rerun every edition's full verification suite.

- **Retained:** the result/content is still present, possibly under a new heading or number.
- **Moved:** content is present in SI/appendix rather than the main text.
- **Adapted:** retained with corrected scope, hypotheses, evidence, or presentation.
- **Intentionally omitted:** absent by design, with a stated reason.
- **Unexplained absence:** no current location or adequate reason found. **None was found that warrants restoration.**

## Per-lineage crosswalks

### 1. ECOMOD v41 → v42

**Retained:** the two-land model, composition/identifiability result, demand ceiling and drawdown results, recovery dynamics, empirical NFA analysis, and the model's stated limits. v42 recasts the contribution as three propositions and preserves the principal outputs. Its edition note records a numeric-token audit: the v41 numbers appear in v42 main or SI, with only formatting/citation years and the machine-precision residual treated specially.

**Moved:** the one-stock history/comparator is SI S7; full derivations and model structure are S1–S2; numerical protocol and verification are S3; robustness sweeps and the drawdown/recovery tables are S4; data vintages and identifiability details are S5; policy extensions are S6. The old observability-ladder material is retained in the SI observation-operator hierarchy.

**Adapted:** the main article now foregrounds what aggregate biocapacity identifies and what it does not, rather than reproducing the v41 history-first structure. The v41 one-stock comparator is explicitly marked as a comparator, not a two-land result.

**Recommendation:** **Do not restore the one-stock history or data ladders to the main text.** They are traceable in S4–S7 and do not carry the new article's central claim. No substantive result is absent.

**Evidence:** `CHANGELOG_v41_to_v42.md`; v41 main source; v42 main and supplementary source, especially S2–S7.

### 2. Paper01 obstruction calculus v72 → v73

**Retained:** the v73 supplementary concordance (Table S1.1) maps the v72 result set: selector principle; finite-horizon soundness/completeness; common-action/Farkas/Helly results; delayed-information obstruction; LP instantiation; finite-time exit; oracle-recourse obstruction; exact certifier/fibre criterion; certainty-equivalence trap; static-observation reduction; two-phase decomposition; window no-go; resource case; and probabilistic counterpart.

**Moved:** the probabilistic result family (v72 Theorem 8 and Propositions 10–11), sufficiency landscape, detailed constructions, figures, and much of the proof/Lean record are in S4–S9 rather than the main text.

**Adapted:** the certainty-equivalence trap is promoted from remark to proposition without changing its statement. The static-observation theorem is sharpened to say the Nagumo test is sufficient, not necessary. The two example models are kept distinct; the hold-class label is corrected; the case-study coverage table now displays all 48 cells; the remedy column is new.

**Recommendation:** **No restoration.** The direct concordance is unusually complete, and it reports no weakened theorem, dropped hypothesis, or changed numerical value. Archived verifier: 30/30 checks.

**Evidence:** `paper01_obstruction_calculus_v73_supplementary.tex`, S1/Table S1.1; `CHANGELOG_v72_to_v73.md`.

### 3. Paper02 probabilistic sufficiency v15 → v16

**Retained/adapted:** support reduction, deficit/value results, delayed hidden-regime classes, noisy sensing, majority-of-probes result, and the contamination layer are carried into v16's theorem structure. The v15 distributionally robust section is not simply deleted: v16 states the one-stage contamination result and its limits (Proposition 8.1), gives the correct convexity statement, and adds the delayed-class prior-contamination formula (Proposition 8.2). The estimation-space/qualitative-POMDP comparison is compressed into the related-work section, not lost.

**Moved:** the formerly main-text grid/deadline/audit tables are in generated SI tables; verification and Lean scope are consolidated in SI S7–S8.

**Intentionally omitted:** (i) the paragraph cross-checking a minimax companion's interpolation record, because this paper's scripts could not regenerate it; (ii) an unrelated Zenodo fisheries citation. The first is an unverified cross-paper assertion, not a self-contained result; the second is not relevant evidence.

**Recommendation:** **Do not restore either omission.** Restore the companion comparison only if its exact inputs and result can be independently reproduced and made part of this paper's record. Archived verifier: 62/62 checks.

**Evidence:** `paper02_probabilistic_sufficiency_v16_CHANGELOG_v15_to_v16.md`; v15 source; v16 §§3–8 and SI S6–S8.

### 4. Paper03 computational certification v22 → v23

**Retained/moved:** the continuous-to-finite bridge, finite certificate, dual interpretation, rank/size results, exact three-branch instance, solver scope, and verification architecture remain. The main bridge proof is in Appendix A; the ladder proofs are in Appendix B; the remaining proofs, instance arithmetic, and verification record are in SI S1–S8.

**Adapted/added:** the uniform-mesh result becomes a law for every aligned mesh (Proposition 5.3); the shared-authority ladder, support-versus-rank explanation, exact observer-erosion table, and intermediate-observer installation bracket are made explicit. The pair-control description and several numerical labels/sign conventions are corrected. The v22 dilation extrapolation is demoted to a caution and paired with a counterexample in v23 SM S6.

**Intentionally omitted:** v22's `fig_hierarchy` plots zeros of a selected algebraic dilation expression. It has no direct replacement as a result figure; the mathematical caution and counterexample are retained in SM S6. Restoring the old plot without its former implication would add little and could invite the superseded extrapolation.

**Recommendation:** **Do not restore the figure or the old dilation claim.** The remaining v22 results are represented in the article/appendices/SI. Archived verifier: 63/63 checks.

**Evidence:** `paper03_computational_certification_v23_CHANGELOG_v22_to_v23.md`; v22 main/SI; v23 main, Appendix A–B, and SI S6.

### 5. Paper04 minimax dual certificates v19 → v20

**Retained/moved:** the common-action dual certificate, finite-support logic, taxonomy, benchmark, finite review envelope, robust values over a coupling class, integrated certificate, and Lean/verification scope remain. The benchmark and static/dynamic computations are now self-contained; detailed proofs, generated tables, and verification records are in SI S1–S8.

**Adapted/corrected:** the support bound is corrected from the v19 Carathéodory argument to Helly plus LP duality, and tightness is given for every dimension. The action set is made compact where required; the benchmark maximizer and policy counts are corrected; the integrated-certificate sign is fixed; action-dependent observation partitions are allowed in the finite review theorem. These are corrections, not losses.

**Intentionally omitted:** the duplicated v19 Theorem 3/4 presentation, the retired-candidate narrative, uncited references, and the inconsistent check-count/provenance prose. The mathematical content is either represented by the corrected theorem or was not a result.

**Recommendation:** **No restoration.** Reinstating the earlier bound, counts, or sign would restore known errors. Archived verifier: 66/66 checks.

**Evidence:** `paper04_minimax_dual_certificates_v20_CHANGELOG_v19_to_v20.md`; v19 source; v20 main and SI S1–S8.

### 6. Paper05 exact belief computation v19 → v20

**Retained/moved:** the four- and five-parameter classifications, pair law, thresholds, observation/feedback results, and point-based computations are retained. The old master/census detail, certificates, complete cube records, observation tables, alpha-set tables, float study, and Lean inventory are in SI S1–S9. v20 adds the six-cube classification and a common linear criterion rather than dropping the earlier classifications.

**Adapted/corrected:** v19's five-cube counts that included stored objects with multiplicity are replaced with counts of distinct admissible sets. The deadline law is proved in both directions; the `j=0` ladder entry is corrected; exact finite-horizon/indefinite-horizon equivalence is stated with its transient condition.

**Intentionally omitted:** the unsupported “four orders of magnitude”/power-set compression framing, the claim that raw subset evaluations were performed, and the v19 “period ≤ 3” statement. The v20 edition says what was enumerated/certified and withdraws those broader claims. Unused isoperimetric/Dedekind references are also dropped.

**Recommendation:** **Do not restore the withdrawn claims or old counts.** The earlier mathematical results are retained; the corrections improve the record. Archived full verifier: 53/53 checks.

**Evidence:** `paper05_exact_belief_computation_v20_CHANGELOG_v19_to_v20.md`; v19 source; v20 main and SI S1–S9.

### 7. Paper06 assessment separation v70 → v71, including stale Paper1 v64

**Correct lineage:** v71 is based on renamed-lineage v70, not stale Paper1 v63. It keeps the research-article structure of the stale-based Paper1 v64, then ports the v63→v70 content changes into that structure. The stale `paper1_assessment_separation_v64` edition remains preserved under `superseded/`; it was not overwritten or deleted.

**Retained/adapted:** the separation theorem and acceptance semantics; quantifier-order results; finite-menu geometry; witness datum; horizon persistence; blend/time-sharing and common-shock results; design tests; resource-transition reading; and limitations are in v71's main article. v70's path-to-margin synchronization lemma and fixed-weight countermechanism are added to v71. The strict-interior hypotheses, LPI direction caveat, slice-flip constants, terminology map, and reporting implications are corrected. The stale v64 main-text structure and result numbering map into v71.

**Moved/expanded:** the substitutability spectrum, common-shock variant, full resource benchmark, checklist/minimum report, verification record, and per-literature positioning are in v71 SI. The v69 Markdown framework supplement is reproduced in full as S9, rather than left at v64's summary level.

**Intentionally omitted or explicitly status-limited:** v70's merged bibliography, assembly artifact, and unnumbered result paragraphs are not replicated. S9 retains the “yield-gap soft-minimum” and “coupling creates viability” ideas only as **unsupported/not reproducible as written**; these are not presented as established findings.

**Recommendation:** **No restoration.** The v70 and stale-v64 content blocks are traceable in v71 main/SI. Do not promote the two status-limited extension claims without a reproducible derivation. The previously created Paper1 v64 remains preserved as the user directed.

**Evidence:** `CHANGELOG_v70_to_v71.md`; current v71 main/SI; stale Paper1 v64 main/SI in `superseded/`; local direct comparison of the v70 source and v69 supplement against v71 S1–S9.

### 8. Paper09 cod/Edwards certification v43 → v44

**Retained/moved:** the two earlier system blocks are integrated into one article. Cod's nominal kernels, no-dominance/vacuity result, constructive boundary, exact/certified horizons, stress replays, carrying-capacity/model-form sensitivity, stochastic results, floor durations, uncertainty, xteNCAM comparison, and self-viability question map to v44 §§3 and SI S1–S7. The alternative Fox/Allee forms and profile details are in SI S6. The Edwards attractor/kernel, governance/supply comparison, bounded-defect and out-of-sample results, replays, and bootstrap uncertainty map to v44 §4 and SI S8–S11. The prior cross-system coda is replaced by the explicit synthesis in §5.

**Adapted:** the two applications are stated under a common monotone-kernel theorem and the frozen protocols are reproduced in SI S13. Full data panels, horizon grids, bootstrap material, and protocol/check records are in SI S1–S14 rather than spread through the main text.

**Absent:** no prior substantive result was found without a current main/SI landing. The shorter main text reflects consolidation and transfer of supporting material, not deletion of either application.

**Recommendation:** **No restoration.** Keeping the full grids and diagnostics in the SI makes the main argument clearer without losing the record. Archived verifier: 77/77 checks.

**Evidence:** `paper09_cod_certification_v44_CHANGELOG_v43_to_v44.md`; v43 source; v44 main and SI S1–S14.

### 9. Paper11 forecasting baselines v66 → v67, including stale E1 v69

**Correct lineage:** v67 is based on v66, the combined cod-plus-Edwards predecessor. The cod half carries the substantive v69 improvements from the stale-base E1 v69 edition; v69 itself remains preserved under `superseded/`.

**Retained/moved:** the Northern cod protocol, specifications, scored ladder, bootstrap/DM margins, period decomposition, fixed windows, variant passes, operating-characteristic simulations, outcome years, vintage/reference-point record, survey-suspension record, verification material, and catch-timing sensitivity appear in v67 main or SI S1–S14. The Edwards ladder, protocol deviations, fixed windows, uncertainty, service-series and pumpage layers, and climate analysis are in v67 §§2/4 and SI S15–S22. Cross-system profiles and verification are S23–S24.

**Important earlier material verified present:** the E1 v69 “regime signal” paragraph is adapted into v67's discussion of what transfers and its prospective-test design (including external regime boundaries, consistent catch timing, both horizons, and both specifications). The v69 SI clarification that M1b at `s_A = 0` is not the Schaefer model is present in v67 SI S5.

**Intentionally omitted/adapted:** v66's cross-system claim that cod failed because of “weakly autocorrelated surplus production” is withdrawn. The computed cod apparent-net-production autocorrelations are 0.71–0.91; the earlier analogy to near-white recharge had the sign of the evidence wrong. v67 replaces it with Proposition 2's increment decomposition and a horizon-crossover remark, and never pools the two systems.

**Recommendation:** **Do not restore the withdrawn cross-system claim.** No material from the stale E1 v69 edition that carries a defensible result was found absent from v67. Archived verifier: 139/139 checks.

**Evidence:** `paper11_forecasting_baselines_v67_CHANGELOG_v66_to_v67.md`; v66 main, Edwards part, and SI Markdown; stale E1 v69 main/SI; v67 main and SI S1–S24.

### 10. Paper11c worked-systems audit v4 → v5

**Retained/moved:** the v5 change record says all fourteen v4 counts are preserved, now as instances, strictness witnesses, or theorem boundaries. The 36-pair master table and mechanisms, full 511-belief census, stationary policies, authority/sustainer tables, monitoring partitions, 93-cell timing grid, larger-cap scaling, benchmark/drift tables, and verification record are in SI S1–S11. The new article also extends the census and gives closed forms and the monitoring-design theorem.

**Adapted/corrected:** the fixed-thread counts (25/26/26/28) are retained in SI but explicitly reclassified as artifacts of quantifying over instruments rather than a fixed thread. The aggregate monotonicity statement is limited to safe-set trajectories; the v4 counterexample at the boundary is disclosed. The continuous-fibre dual quantities are distinguished rather than conflated.

**Recommendation:** **No restoration.** The prior counts and details are traceable; the corrections should stand. Archived verifier: 64/64 checks.

**Evidence:** `paper11c_worked_systems_audit_v5_CHANGELOG_v4_to_v5.md`; v4 source; v5 main and SI S1–S11.

## Restore decision

| Candidate earlier item | Status in current edition | Decision |
|---|---|---|
| Paper02 minimax-companion interpolation cross-check | Removed because it could not be regenerated from this paper's scripts | Do not restore unless independently reproduced |
| Paper03 `fig_hierarchy`/dilation extrapolation | Figure omitted; caution and counterexample retained in SM S6 | Do not restore as a result |
| Paper04 old support argument, benchmark values, policy counts, sign convention | Corrected in v20 | Do not restore old statements |
| Paper05 compression/power-set and “period ≤ 3” claims | Withdrawn as unsupported; valid classifications remain | Do not restore |
| Paper06 merged bibliography/assembly artifact | Non-scientific presentation artifacts; scientific blocks in v71 main/SI | Do not restore |
| Paper11 weakly-autocorrelated-cod explanation | Contradicted by the checked data and explicitly retracted | Do not restore |
| Paper11c fixed-thread “alternatives” | Retained in SI, classified as a counting artifact | Do not promote as a valid alternative |
| ECOMOD single-stock history | Retained in SI S7 | Leave supplementary |

**Bottom line:** The audit supports maintaining the created editions as shipped. I found no unexplained absence that justifies a new numbered edition. The restoration threshold is not met; prior editions remain preserved, and no result was pushed as a new paper version.