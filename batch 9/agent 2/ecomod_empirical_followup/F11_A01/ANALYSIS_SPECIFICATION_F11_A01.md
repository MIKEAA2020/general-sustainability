# Exploratory analysis specification — F11 A01

This specification documents the implemented analysis **after exploratory execution began**. It is not a preregistration, a prospective field protocol or evidence that hypotheses were fixed before outcomes were inspected. The footprint and source endpoints were inherited from the earlier geometry-only selection, unchanged.

## Inputs and fixed support

- The exact 256 × 256 native-cell Brazilian rectangle, 65,536 cells and 61,830.3436 ha.
- ESA CCI Biomass v7.0 native 2015/2023 AGB and AGB-SD; exact query URLs, lengths and SHA-256 hashes in the unchanged F10 registry. No endpoint substitution or extrapolation.
- WGS84 cell areas and Collection 11 area-weighted group fractions, with integer positive-overlap certificates. Guarded F05/F07 local range decoding and derivations are independently rerun.
- Formations: classes 3, 5, 6 and 49. Added savanna: classes 4 and 7. Their union is a distinct target, not a confidence interval. Plantations remain distinct.
- All cells are retained: zeros, mixed cells, changed classes and zero-SD observations. No substitution for missing values is allowed. Actual source values are finite and in range on the complete rectangle.

## Estimands and experiments

1. **Point-map cancellation:** form each full-cell mass from density × its own WGS84 area. Compute positive/negative local differences, net, total variation and cancellation. These are not gross biological processes or calibrated physical change.
2. **Information ablation:** aligned square blocks with sides 1, 2, 4, 8, 16, 32, 64, 128 and 256 native cells. Preserve footprint, endpoint definitions, group geometry and weights. Observe only block mass, forgetting internal cell masses. Compute sharp allocation sets from pure/present block topology; compare width and sign with the one-window baseline.
3. **Extremal group witnesses:** construct both change extremes using nonnegative mass partitioning. Verify all cell totals and absent/pure support. Do not serialize native arrays or cellwise allocations.
4. **Coherent joint identification:** partition cells into formations, added savanna and complement. Derive the sharp two-dimensional difference polygon and check four strict sign quadrants. Reduce computation to seven component-presence patterns per endpoint, then reconstruct a feasible allocation for every native cell. Check the analytic polygon against a separate pattern-allocation LP in 73 directions; the geometric proof, not the finite check, establishes sharpness.
5. **Contrast sensitivity:** in each mixed cell assume, solely for sensitivity, reciprocal component-density ratios bounded by a common R. Sparse values are 1, 1.5, 2, 3, 5, 10, 100 and infinity. A 121-point geometric grid from 1 to 10 renders the curve. Root finding in log R locates the first loss of a strictly positive lower difference bound. Each mapped group is evaluated separately; the ratio models are not claimed to be one jointly calibrated ecological model.
6. **Stored-SD audit:** recompute counts and positive-AGB SD quantiles directly from the fresh native payloads and compare all numeric fields with R03. No SD floor, independence assumption or confidence calibration is introduced.

## Primary and sensitivity assumptions

The **primary** identification model conditions on exact point maps, classes and epoch correspondence; allows nonnegative component densities with no finite cap; and imposes no temporal, spatial, growth or ecological plausibility coupling. Sharpness is within this model, not a guarantee about true biomass. The contrast family is auxiliary and uncalibrated. R=1 is homogeneous allocation by assumption, not an admitted forest-stock estimate; infinity recovers the primary model.

Integer counts determine absent/pure/mixed membership. Exact fractions 0 and 1 are assigned only to topologically certified endpoint cases, after checking area-integration agreement. Mixed fractions are never thresholded into pure/absent membership. Their actual area weights, not intersection-count fractions, enter the finite-R formulas.

## Checks and limits

Toy kernel identities and independent linear-program checks cover bounds and nesting. All eight national holds are preserved. No national extrapolation, transition association, classifier accuracy, statistical confidence coverage, causal effect, biological gross turnover or probability of a true sign is estimated. Source identity, numerical reproducibility and ecological validation are different claims throughout.
