# ER029 Point Inventory — Preliminary, Pending Remaining Numerical Audits

## Status

Received during the numerical audit batch. No implementation before joint batch completion.

## Strong points

1. Correct empirical-versus-continuum distinction.
2. Correct need for validated orbit, full spectrum, projections, and prefactors.
3. Correct separation of binding numerics from slack/coupling and theorem matching.
4. Correct refusal to promote NAIM/graph/Hopf from grids alone.
5. Useful outline of a future validated monodromy package.

## Numerical/data errors and superseded findings

1. The `dt=0.25` stable multiplier is available: `0.68774849`; ER029 incorrectly leaves it unlisted.
2. The `dt=0.10` phase error is about `2.25e-3`, not `4.3e-3`.
3. Grid convergence toward one supports the phase multiplier but does not by itself prove algebraic simplicity.
4. Direct period `370.95 yr`, orbit ranges, long-horizon convergence, and floor margin `0.00147554` are already computed; they are not missing or circularly inferred.
5. The orbit is the reproduced C4 large-cycle candidate in the lower bistable window; there is no contradiction with the monostable interval `(5.63,64.4)` because the lower large-cycle window is `(3.78487,about 5.63)`.
6. A provisional slack block at `tau=10`, its exact-refined rightmost pair, and global numerical root count are now available.
7. `M_c about 4.55356` is estimated; it is not safely set to one.

## Mathematical errors

1. **Phase simplicity overclaim:** numerical phase convergence does not establish algebraic simplicity of the continuum multiplier.
2. **One-period bunching error:** `q_1 approximately 0.68767 M_s` omits the measured tangent/inverse-tangent factor and the slower product slack rate. Product bunching cannot be checked from the binding multiplier alone.
3. **Full-normal rate overclaim:** the leading binding exponent does not prove `beta_x>r alpha` for the full continuum complement.
4. **Compactness wording:** eventual compactness is consistent with accumulation at zero but does not validate continuum eigenvalue placement from grids.
5. **C4 fold transfer:** any statement that the C4 event has a `+1` multiplier is unsupported; C4 classification remains open.
6. **Yield parity:** parity removes the exponential certificate; it does not force total coupling to be order one.
7. **Self-contained theorem sketch:** the proposed theorem omits essential map/semiflow, bundle, localization, projection, and sampled-to-semiflow details and is not a proof.
8. **Smoothness check:** the relevant quantity is the full outer-floor argument, not merely `min Z(t)`.
9. **Publication block:** it repeats outdated missing-period/branch/floor claims and should not be implemented.

## Provisional disposition

Retain ER029's validated-numerics roadmap and conservative no-promotion boundary. Reject its one-period bunching, phase-simplicity, branch, period/floor, fold, parity, and theorem-sketch claims. Defer any numerical remark.