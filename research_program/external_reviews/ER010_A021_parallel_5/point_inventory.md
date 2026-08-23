# ER010 Point Inventory — A021 Parallel Proof Response 5

## Status

Received for later joint adjudication with the internal proof and ER006–ER009. No recommendation is implemented from ER010 alone.

## Strong contributions

1. Most conservative and internally coherent route choice so far: finite-time theorem plus graph conjecture.
2. Concrete noninvertible history-collapse mechanism.
3. Full normal-bundle diagnosis.
4. Useful slack-neighborhood variation-of-constants estimate and logarithmic-transient distinction.
5. Direct full-RFDE Hopf theorem independent of the graph.
6. Fixed phase space through time rescaling for delay bifurcation.
7. Explicit refusal to transfer local Hopf to global folds.
8. Strong concrete verification checklist.

## Issues for joint adjudication

1. Noncompactness is again stated without the finite/totally disconnected qualification identified by ER006/ER007.
2. Under merely `C1` slack nonlinearity, the remainder is `o(||eta||)`, not necessarily `O(||eta||^2)`. The quadratic inequality and bootstrap require `C1,1`/`C2`, or must use a modulus-of-continuity estimate consistently.
3. The abstract variation-of-constants injection/evaluation notation should match the selected RFDE phase-space theorem; the norm estimate is plausible but the displayed `X0` object is not literally an element of the continuous-history space.
4. The cited Bates–Lu–Zeng bibliographic entry appears incorrect. The authoritative memoir is *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*, Memoirs AMS 135 (1998), no. 645, not the Trans. AMS citation stated here.
5. The blanket statement that time maps are completely continuous for all bounded histories still needs bounded-solution/localization assumptions.
6. The direct Hopf spectral-crossing argument is strong, but a nonlinear Hopf branch requires the smoothness hypotheses of the exact RFDE Hopf theorem; `C1` alone is generally insufficient. Criticality/local uniqueness requires additional nondegeneracy such as nonzero first Lyapunov coefficient where claimed.
7. The phrase “every reduction that treats epsilon as small fails” at parity is too strong. Parity removes the yield-gap guarantee; `C_gap` and `epsilon_phys` might still be small for another reason.
8. The claim that a compact time-T map cannot be invertible on open infinite-dimensional sets is directionally useful but should be stated with the exact map/local-domain assumptions.
9. The publication-ready status sentence still states the history cube is simply “not compact” without the degenerate-target qualification.
10. The direct characteristic matrix notation is substantially improved over prior responses but still needs concrete functional derivatives for A021.

## Comparison with internal proof

ER010 strongly supports the internal hierarchy and improves its slack estimate. For the final joint version, consider adopting:

- ER010’s Route F decision;
- ER010’s slack variation-of-constants estimate after strengthening regularity or replacing the quadratic remainder by a modulus;
- ER010’s fixed-phase-space direct Hopf setup;
- the internal proof’s correctly cited BLZ conditional template;
- ER006/ER007 inverse-tangent bunching and compactness qualifications.

The final implementation should continue to withhold the invariant graph for concrete A021.