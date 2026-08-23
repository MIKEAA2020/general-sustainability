# Paper VIII validation status

## Completed

- Corrected the collocation-map dimensions in `paper_VIII_interval_folds_corrected.tex`.
- Separated interval certification of the Hopf cubic roots from phase-formula delay evaluation.
- Reclassified the small-branch result as numerical continuation evidence, not a fold certificate.
- Restored the companion's Floquet-multiplier evidence as supporting evidence only.
- Added the Moore--Spence formulation and the fold nondegeneracy conditions.

## Floating-point pseudo-arclength continuation

A scaled pseudo-arclength system was solved using the existing `m=64`
collocation residual. It found a branch point at `tau=5.5870644140` with
residual `1.62e-12`, beyond the earlier fixed-`tau` endpoint, and then
followed the branch back toward smaller `tau`. A finer scan showed the
smallest fixed-`tau` singular value decreasing toward the turning region,
with residuals near `1e-14`.

This establishes that fixed-`tau` solver failure at `tau=5.590` is not a
nonexistence result, but it does not certify a fold.

## Moore--Spence and Jacobian status

The analytic collocation Jacobian was repaired after identifying an omitted
spectral derivative contribution. It now agrees with central finite
 differences at the existing orbit:

- relative full-Jacobian discrepancy: approximately `1.4e-10`;
- maximum entry discrepancy: approximately `2.8e-10`;
- all state and period column discrepancies: below approximately `7e-10`.

A Moore--Spence solve using this corrected Jacobian and the unscaled
augmented residual terminated immediately because the initial nullvector
residual was only `2.52e-7` and the optimizer's gradient criterion was
satisfied prematurely. A rescaled attempt, multiplying the `Jv` block by
`1e5`, moved away from the initial point but did not converge after 100
function evaluations:

- final `tau`: `5.5841495071`;
- `||F||`: `3.63e-4`;
- scaled `||Jv||`: `1.32e-5`;
- normalization residual: `1.59e-5`;
- combined scaled residual: `3.64e-4`.

The rescaled solve is therefore also inconclusive. No Moore--Spence zero,
fold nondegeneracy check, interval enclosure, or continuous-DDE validation
has been obtained.

## Current conclusion

The corrected Jacobian is now numerically cross-checked, but the augmented
fold solve still needs a better formulation. The next feasible improvement
is to use a dedicated Newton solve with an analytic/block Jacobian of the
Moore--Spence system, proper variable scaling, and a nullvector normalization
such as `ell^T v=1` rather than relying on least-squares termination. The
present paper should continue to report only numerical continuation evidence
for the fold.
