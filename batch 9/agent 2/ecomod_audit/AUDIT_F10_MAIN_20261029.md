# Audit of `followup_F10_main.txt`

**Audited item:** F10 main-manuscript LaTeX source, 233 lines / 5,011 words.
**Audit date:** 2026-10-29.
**Scope:** claims and methods in the supplied main source, internal arithmetic/logic, citation integrity, and build/reproducibility status. The supplied text was later byte-compared with the F10 source on `origin/main`; that repository package includes the SI, results macros, figures, derived data, scripts and compiled PDFs. Several initial “not found in checkout” observations below refer only to the then-current working-tree branch, not to the declared `main`-branch availability URL. The package outputs were spot-checked, but the full test suite and TeX build were not rerun in this environment.

## Overall assessment

**Promising measurement-compatibility and partial-identification study, but the current framing overstates what is empirically tested.** The attached main source is not standalone, but its exact matching source and required build/results files are present in the F10 package on `origin/main`. The text is notably cautious about the distinction between global-hectare accounts, land-cover classes, and biomass stocks. It appropriately labels the Brazilian mapped-cover result as a local endpoint comparison, the biomass-allocation intervals as conditional sets rather than confidence intervals, and the account-availability results as not establishing physical trends. It also correctly separates whole-cell biomass from forest-area-normalized density and does not claim that validation of stock levels validates local change.

The central contribution currently supported is a **feasibility/compatibility and identifiability audit**: it reports availability of account records, screens candidate boundaries/endpoints, describes local MapBiomas cover, documents limitations of the inspected biomass and reference products, and shows that very weak allocation assumptions leave the sign of local group biomass change unidentified. It does **not** estimate national forest-stock trends, account–asset divergence, or forest-to-cropland conversion associations—and the manuscript says so. The title (“a boundary-matched test of composition masking”) and four research questions nevertheless suggest those empirical tests will be answered. Reframe the paper around the compatibility/identifiability result or provide the missing matched physical-change and association analyses.

## 1. High-priority findings

### 1.1 Study framing and questions exceed the analyses actually reported — High

**Locations:** title and abstract; Introduction, lines 30–38; Results, lines 114–192; Discussion/conclusion, lines 194–208.

The four questions ask for: (1) matched forest extent and biomass changes; (2) whether physical assets rise/fall/remain unresolved when national biocapacity rises; (3) account–asset divergence and conversion associations; and (4) whether adding independent asset information changes an assessment. The reported results do not estimate country-level physical biomass change, account–asset divergence, forest-to-cropland association, or reporting/classification performance. Instead, they show that candidate national comparisons are not yet admitted, present Brazilian cover endpoints, and derive allocation-only biomass-difference sets containing zero. The conclusion explicitly says those national trends and associations are not estimated.

The caveats are good, but they do not fully resolve the mismatch between the promised empirical “test” and the achieved design. The zero-containing allocation sets are a conditional non-identification result, not evidence that masking occurred or did not occur.

**Recommendation:** either narrow the title, abstract, and research questions to a *boundary/measurement compatibility and partial-identification assessment*—and describe composition masking as the motivating hypothesis—or add an actual matched, uncertainty-aware physical-change analysis and the specified account/asset and conversion comparisons. Do not describe account availability plus a local cover example as an empirical test of account–asset divergence.

### 1.2 Build and reproducibility are package-dependent, not a missing-artifact defect — Moderate

**Locations:** source line 10; figure environments at lines 118–121 and 149–152; Data and code availability, lines 210–211.

The attached text alone requires `\input{results/availability_numbers.tex}` and references `results/account_coverage_F06.pdf` and `results/brazil/BRA_F05_support_fractions.pdf`, so it is not a standalone build. However, the F10 package at the exact declared `origin/main` URL contains those files, the matching SI, derived tables, processing code, source/metadata registries, and compiled main/SI PDFs. A byte comparison confirms the attached main source is identical to the package's `followup_F10_main.tex`; the C17 companion cited in the bibliography is also present. Thus the earlier worktree-only absence is not a reproducibility defect in the published package.

The package records 134 passing tests in both normal and optimized Python modes and QA metadata for the PDFs. These logs were not independently rerun here: the test attempt stopped at missing Python dependencies, and no TeX build was performed. The package README documents the build/test commands and `requirements_F10.txt`.

**Action:** keep the source-to-package path explicit and stable; preferably link the CSV coverage/support table directly where the SI refers to it. For an independent audit, install the declared requirements and rerun the tests/build from the package root. Raw CCI/MapBiomas/reference archives are not redistributed, so the source registry and checksums remain important to distinguish reproducible derived outputs from access to the original inputs.

## 2. Substantive checks and qualifications

### 2.1 Conditional allocation calculation is internally coherent, but intentionally very weak

**Locations:** Methods, “Conditional biomass-allocation sets”; Results, Table `allocation`, lines 177–192.

Under the stated model—fixed whole-cell biomass totals, nonnegative within-cell allocation, no density cap, and no temporal coupling—the lower bound from pure mapped-group cells and upper bound from every cell with positive group overlap are coherent. The difference interval \([L_{2023}-U_{2015},\ U_{2023}-L_{2015}]\) follows for independent endpoint allocations. The displayed formations interval \([-223.97,282.00]\times10^3\) Mg contains zero, as does the formations-plus-savanna interval. This supports the stated conclusion that the sign is unidentified *under those assumptions*.

It does not identify a forest-specific biomass trend, and the interval's width is partly a direct consequence of allowing arbitrary concentration of biomass within any mixed cell and no temporal constraint. The paper does state these limitations; retain them wherever the interval is summarized. Avoid calling these intervals uncertainty bounds on the true forest-stock trend.

**Rounding note:** the formations-plus-savanna endpoints displayed to two decimals subtract to 259.54, while the displayed change upper endpoint is 259.53. The F10 package's unrounded allocation CSV gives 489,288.5391 − 229,754.7757 = 259,533.7634 Mg, which rounds to 259.53 × 10³ Mg; this is consistent with calculating differences before rounding endpoints. The SI gives more digits but still rounds each value independently, so add a brief note that difference bounds are computed from unrounded endpoints to prevent apparent arithmetic discrepancies.

### 2.2 Local cover changes are descriptive, not a validated forest-area change estimate

**Locations:** Results, Table `brazil_cover` and text, lines 128–152.

The overlap-area calculations are clearly presented as mapped classifications, and the article warns that the footprint is not a probability sample, the groups overlap, map labels can be temporally filtered/gap-filled, and these endpoints do not establish ecological change or account–asset divergence. These safeguards are important. The “formations” and “formations plus savanna” quantities are distinct targets; the latter is not an uncertainty band around the former. Keep that distinction in the title/abstract and any graphical summary.

No independent accuracy assessment of Collection 11 or local transition labels is supplied here. The later text says Collection 9 reference artifacts do not offer a compatible paired sample; accordingly, this draft should not imply that the reported mapped-cover changes are accuracy-adjusted or validated local transitions.

### 2.3 Biomass-change uncertainty limitation is properly identified but not quantified

**Locations:** Methods, “Uncertainty, validation and information comparisons”; Results, lines 163–175; Discussion, lines 201–205.

The distinction between within-stack or spatial covariance and cross-year covariance is correct in concept. The source explicitly says the absence of a cross-year term in a provider variance expression does not imply zero covariance, and it does not transfer stock-validation error statistics to local change. That is a strength. The matching SI and package-derived tables are available at the declared F10 path; a spot-check found the local zero-SD counts and allocation endpoints consistent with their CSV summaries. Raw product payloads are not redistributed, and the full pipeline/test suite was not rerun here, so raster-level screens and external product interpretations are supported by the package’s source registries and verification records rather than an independent raw-data rerun. The paper correctly avoids converting those descriptive screens into a confidence interval or local change-error model; preserve this limit.

## 3. Editorial and traceability checks

- The source scan found **15 citation keys and 15 matching bibliography entries**, with no missing or duplicate citation keys and no duplicate labels.
- The `results/availability_numbers.tex` macros and referenced figures are supplied in the matching F10 package on `origin/main`; the isolated text attachment would not compile without them.
- The abstract uses macro-generated account totals and says all eight candidate countries pass the account criteria, while the results say no candidate meets all territorial, forest-support, complete-coverage and change-validation criteria for analytical admission. These statements are compatible only if “pass account criteria” is clearly distinguished from “admitted to physical analysis,” as the current body generally does. Add that distinction to the abstract if the macro sentence could be read as an eight-country physical sample.
- The country selection is described as purposive, not probabilistic. The resulting eight-country screening must not be generalized as a representative estimate of national account–asset compatibility.

## 4. Bottom line

The paper is careful about what its observations cannot establish, and the conditional biomass-allocation derivation appears coherent under its explicitly minimal assumptions. Its strongest current result is a boundary/measurement feasibility assessment plus a local non-identification demonstration—not a measured test of national composition masking. Reframe the contribution accordingly or add the missing physical-change analysis. The declared F10 package is present and matches the attachment; for a fully independent check, rerun its tests/build and document the unrounded-results note in the manuscript.
