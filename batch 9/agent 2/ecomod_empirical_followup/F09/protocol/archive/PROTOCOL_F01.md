# F01 working protocol and staged implementation

**29 October 2026 — Stage 1 implementation, not a completed empirical finding or registered preregistration.**

## Study question and boundaries

When national biological-supply accounts improve, what happens to independently estimated forest extent and above-ground woody biomass on matched spatial and temporal supports? Where are local net gains and losses spatially offset, and is independently validated forest-to-cropland conversion associated with any account–asset divergence?

This paper tests observable, bounded propositions motivated by ECOMOD; it does not calibrate ECOMOD quality, infer physical capital from an account residual, assert global stock decline, or validate its entire delayed model. C13 is the current theoretical companion (commit `014bbe7093e5dc2cdc8c8d8524ae22f8b7c192b5`). Earlier review/planning documents remain source inputs, not revised manuscripts.

The forest–cropland core is retained. Soil, wetland and assessed-fish modules remain conditional. No scalar ecological-capital total or depletion horizon will be manufactured. Mixed, opposite, unresolved and null outcomes remain eligible results.

## Stages and gates

1. **Specification and source preflight (F01, this delivery):** consolidate reviews; freeze a working configuration; audit all national account identifiers; retrieve small biomass files; inspect coordinates, units, uncertainty and source methods; implement tested estimand kernels; start the manuscript. This is implemented, not just a new plan.
2. **Boundary-matched physical pilot:** reconcile eight candidate countries' territories and forest masks; retrieve bounded native-resolution subsets or justified aggregates; audit missing/converted pixels and observation lineage; inspect product validation and uncertainty documentation; validate a transition source. Do not compute divergence prevalence until the eligible physical sample is frozen.
3. **Calibration and extraction:** run full-pipeline noisy-null, misspecification and effective-support simulations with tuning/evaluation separation. Compare simple account/endpoint/trend baselines with spatial/path packages on identical support. Use probability-sampled or otherwise justified independent references where available. Exclude quality flags constructed from the target maps from the role of independent truth.
4. **Core empirical estimation:** estimate stock, extent and density changes with spatial/temporal covariance and bias scenarios; retain unresolved and excluded cases; estimate local-net-change cancellation only at defensible support; test conversion associations only where independently observed. No causal effects from overlays alone.
5. **Manuscript completion and release:** write results from generated tables, complete SI, check references and lineage, rerun from the manifest, and state overlap with the theoretical paper. Archive a new revision rather than overwriting this F01 snapshot.

## Fixed starting choices

- Primary account window: **2015–2023**; secondary candidate **2010–2020**, subject to the documented cross-sensor limitations and a separate gate.
- Account vintage: **NEFBA Edition 2026, results/metadata v1.0**. Use absolute total B as primary; terrestrial, excluding-built-up, forest-component and per-person results are separately labelled sensitivities.
- Flags `+++`, `++` and `+` all publish the biocapacity and production quantities needed here. Their differences concern trade/consumption detail and must not be treated as graded biomass accuracy. Exclude `-`, `X`, and estimated-only/missing-required-value cases from the account preflight pass.
- Require all nine primary-window years and numeric, nonnegative required account components, population and relevant areas. Check five-component total reconciliation within the maximum 3 gha rounding bound for five separately rounded components and a rounded total. This is a numerical integrity tolerance, not an ecological threshold.
- Candidate pilot: **Brazil, Indonesia, Democratic Republic of the Congo, Cameroon, Canada, Finland, France and Australia**. These are a deliberate logistical/environmental contrast, not a random sample or a preselected set of positive masking cases. Every candidate remains conditional on territorial and physical-data checks. No national outcome signs were used to choose them.
- No global native-resolution download. Stage 1 caps each retrieved file at 25 MB. Raw/restricted inputs stay in an external cache; publish hashes, retrieval instructions and derived tables subject to source terms.

## Estimands and inference

For a defined support, biomass stock is the integral of density over the **correct area denominator**. The source product's density may refer to total grid-cell area, not forest area. Do not multiply a whole-cell average by forest area again, and do not call it forest-only density without an independent mask and justified transformation.

Where total forest areas A0,A1 are positive and stocks Q0,Q1 are defined on compatible supports, compute D0=Q0/A0 and D1=Q1/A1. The exact symmetric decomposition is:

- extent contribution = (A1−A0)(D1+D0)/2;
- density contribution = (D1−D0)(A1+A0)/2.

These sum to Q1−Q0 and are descriptive identities, not causal effects. The supplied kernel refuses zero-area endpoints rather than inventing counterfactual density. Appearing/disappearing strata need a separately stated convention and sensitivity analysis.

For local stock changes ΔQi on the same observed support, report G=Σmax(ΔQi,0), L=Σmax(−ΔQi,0), net=G−L, offset=min(G,L), and cancellation fraction 1−|G−L|/(G+L) when G+L>0. The zero denominator is undefined, not a perfect score. G and L summarize **local net changes**, not observed gross growth, harvest, recruitment or mortality flows. Pure noise can create high apparent cancellation; calibrated support/error checks are required before interpreting it.

Account increase/decrease is a descriptive sign, not ecological safety. Physical change resolution requires an uncertainty model with justified coverage; provider qualitative flags are not automatically a 95% confidence interval. Practical-change thresholds and the final classifier must be set using the blinded calibration/validation stage and documented in an amendment before outcome estimation. No stock-loss significance or reporting-rule accuracy claim is permitted in F01.

## Required refinements from the reviews

- **F1 — availability/exclusion:** distinguish retrospective observation from real-time availability. Exclude future-only, target-derived and shared-reference information from contrasts that claim independent predictive or diagnostic value; keep the resulting coverage loss visible.
- **F2 — identical support:** compare rules on exact common cases/weights and pairwise overlap; also report full eligible coverage. Do not attribute a score difference to an information package when the evaluated countries/years differ.
- **F3 — identification/redundancy:** audit whether a new feature is algebraically recoverable from existing fields. Better prediction does not establish a physical latent-state interpretation or an independently observed mechanism.
- **Calibration:** compare candidate rules/gate ablations with separate tuning and held-out evaluation and Monte Carlo uncertainty. Do not copy another study's margins, simulated truths or false-retention rates.
- **Spatial/path modules:** explicitly model spatial cancellation and compare true repeated paths with endpoints/trends only when observation timing and support warrant it. Demography requires repeated independent demographic observations.

## Stage 1 findings that change implementation

The national accounts are accessible and contain their own category areas. Those areas are part of the account lineage and cannot serve as independent physical validation of that account. All eight candidates pass the account-only screen; none is yet certified as a fully eligible physical comparison.

The downloaded CCI aggregate is a 0.5° grid despite its nominal 50 km label. Use true cell bounds and latitude-dependent area, not constant square-kilometre weights. The native product footprint and missing data must be respected; a global bounding rectangle is not evidence of globally observed land.

Targeted reading of the v7 Product User Guide, especially sections 2.3, 4 and 5, establishes that change products require bias/quality caution and that aggregated density is per grid-cell area. Aggregate uncertainty includes a spatial covariance calculation. The downloaded change file has a dangling `time_bnds1` reference and lacks in-file flag meanings. These are ingestion/documentation issues, not proof that all source data are unusable; preserve original metadata and record any future repair.

The provider change-generation code was **inspected, not executed**. Its change SD uses a zero-temporal-covariance variance sum; flag construction uses the same endpoint estimates and one-SD bounds, plus additional rule/filter operations. Thus its flags are target-derived diagnostics, not independent validation truth and not a calibrated 95% decision rule. Source code examples contain older-version filename text, so freeze actual v7 input bytes rather than trusting example names. The quality legend can be documented from the source code, but that does not settle the validity of its decisions in this study.

## Prior knowledge, registration and amendments

Prior plans, literature and world-level NFA results were already reviewed. Source discovery inspected the schema and the earliest Afghan historical rows; no new paired country endpoint changes were computed before the F01 configuration. F01 is a working protocol with an explicit disclosure, not a claim of pristine prospective or externally registered preregistration. No biomass pixel values/change signs or country account changes are computed in Stage 1. Later deviations require dated amendments, reason and impact on inference, rather than silent changes to this file.
