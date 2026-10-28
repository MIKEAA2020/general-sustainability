# Follow-up paper: first implemented pass (F01)

**29 October 2026. Stage 1 completed within its limited scope; the empirical paper is not complete.**

## Deliverables now available

- A compiled [six-page working manuscript](../manuscript/followup_F01_stage1.pdf) and matching TeX.
- A consolidated [working protocol](../protocol/PROTOCOL_F01.md) with prior-information disclosure, inference boundaries and amendment requirements.
- A source-frozen, executable national-account preflight and biomass schema audit.
- Actual country/territory eligibility and candidate-pilot tables, a generated coverage figure and machine-readable results.
- Tested WGS84 area, extent/density decomposition and local-net-change cancellation kernels.
- Source/method provenance, use restrictions and an explicit staged continuation plan.

## Real data audit, not anticipated ecological results

| Audit item | Executed result |
|---|---:|
| National account records parsed | 13,652 |
| National workbook columns | 51 |
| Country/territory identifiers | 236 |
| Account-only 2015–2023 preflight pass | 183 |
| Account-only preflight fail | 53 |
| Predeclared candidate countries | 8 |
| Candidates passing the account-only screen | 8 |
| Largest component/total rounding discrepancy in the window | 2 gha |
| Biomass NetCDF files retrieved and opened | 2 |
| Raw empirical input files hash-frozen | 3 |
| Unit tests passed | 13 |
| Synthetic mixed decomposition cases in tests | 500 |
| Working manuscript pages | 6 |
| Unresolved citations/references or overfull boxes | 0 |

The account screen checks availability, publication scope and numeric integrity, not physical comparability. The eight candidates are Brazil, Indonesia, Democratic Republic of the Congo, Cameroon, Canada, Finland, France and Australia. They are a deliberate logistical/environmental contrast and not a probability sample. The currently recorded full-study eligible count is zero **because eligibility has not been evaluated**, not because all countries failed. No country account-change signs, biomass pixel values, biomass-change signs or divergence prevalence were computed.

## Findings that prevent avoidable errors

1. **Do not equate nominal 50 km with equal-area pixels.** The retrieved aggregate has 0.5° coordinates. The new WGS84 kernel integrates actual bounds and has analytic/partition checks.
2. **Do not apply a forest-area multiplier to an already whole-cell density.** The v7 guide defines the aggregate per grid-cell area and describes a covariance-aware aggregate uncertainty calculation. This denominator must be reconciled before stock extraction.
3. **Do not use target-derived quality flags as independent truth.** The provider script derives them from the endpoint maps, their uncertainties and rule/filter operations. Its variance formula does not add a temporal covariance term. Neither a provider significance label nor its one-SD-bound construction is a calibrated 95% study decision rule.
4. **Do not silently repair source metadata.** The downloaded change file's `time` bounds attribute references absent `time_bnds1`, and in-file flag meanings are missing. A quality legend was located externally in the provider code; the original NetCDF is unchanged and the missing bounds remain documented.
5. **Do not treat an account's own areas as independent validation.** They are useful account inputs but share its lineage. Independent physical support still needs to be acquired and reconciled.
6. **Do not interpret noisy cancellation as a mechanism.** An implemented null smoke test demonstrates why the full calibrated support/error experiment is mandatory. The local-net-change summaries are not gross biological gain/loss flows.

These are actual source/method observations, not scientific findings about forest trends. The provider code was inspected but never executed. The restricted guide is not republished, and the raw inputs stay outside the deliverable directory.

## Next step: physical pilot, with concrete acceptance gates

The next revision should work through the following in order:

1. Download/read the version-frozen validation and uncertainty reports already located on the ESA documentation page; record which independent references and spatial/temporal covariance models they actually justify.
2. Freeze a country/territory boundary source and forest/land-cover definition, including France's territorial extent, Canada's high-latitude coverage, disputed boundaries and valid CCI support. A global coordinate rectangle is not a complete measurement mask.
3. Test bounded native-resolution/subset access on declared landscapes before scaling. Register every source file/tile, exact epochs, mask denominator, units and no-data/zero convention. Do not download the approximately 800 GB collection or infer fine transitions from coarse maps.
4. Select a genuinely suitable independent forest-to-cropland transition reference. Distinguish harvest, fire, plantation dynamics and regrowth; tree-cover loss alone is not cropland conversion. Determine whether a reference-sample change estimate is possible.
5. Produce a **physical-pilot coverage/lineage table** that can actually accept, reject or narrow countries/intervals without looking at account–asset sign agreement. Freeze that table before estimating prevalence or reporting-package performance.
6. Implement spatial/temporal covariance, bias and missing/converted-pixel scenarios, then the whole-pipeline noisy-null and misspecification experiment. Compare package scores on common cases/weights and show coverage loss.

If support or uncertainty gates fail, retain unresolved outcomes or narrow the estimand. Do not replace missing independent measurements with an NFA residual, provider-derived flag, borrowed simulation result or unvalidated ecological index.

## Remaining work after the pilot

- Calibrated estimates and comparisons, not just algebraic identities.
- Extent/density and within-asset spatial-cancellation results with effective-support/noisy-null checks.
- Conditional temporal-path comparisons only where observation timing supports them.
- Conversion associations only when the transition is independently observed and validated; no default causal effect claim.
- A completed main manuscript and SI written from actual estimates, with mixed/null cases, coverage, uncertainty and related-paper overlap disclosed.

F01 is preserved as an immutable first-stage release. Later work belongs in new revision directories. Earlier plans, reviews, submitted documents and C13 remain unchanged.
