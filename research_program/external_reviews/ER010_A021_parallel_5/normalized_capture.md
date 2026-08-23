# ER010 Normalized Capture — A021 Parallel Proof Response 5

## Route and conclusion

ER010 explicitly adopts Route F. It rejects every currently available invariant-graph proof and treats the graph as conjectural. It claims two proved results:

1. finite-time binding tracking plus a slack-neighborhood estimate;
2. a direct local full-RFDE Hopf theorem under explicit equilibrium/spectral assumptions.

## Diagnosis

ER010 identifies:

- noncompactness without equicontinuity;
- no manifold structure;
- full normal bundle includes binding-transverse and slack directions;
- noninvertible/collapsing RFDE histories obstruct a single-valued graph;
- persistence moves both coordinates, so any graph is over a perturbed base.

It gives a concrete history-collapse mechanism using `F=0` and `T>=tau`.

## Finite-time/slack theorem

Under local C1 well-posedness, exponentially stable slack linearization, and a bounded region with uniformly bounded/Lipschitz data, ER010 proves:

- finite-time `O(epsilon)` tracking of the binding block;
- a variation-of-constants inequality for the slack deviation;
- a local bootstrap giving exponential decay of initial slack error plus an `O(epsilon)` floor;
- an `O(|log epsilon|)` transient only when the initial slack error is order one.

No invariant graph or infinite-time binding tracking is claimed.

## Graph conjecture

ER010 states a graph conjecture requiring a compact C^r binding manifold, two-sided base flow, full exponential splitting, normal domination, C1 small time-map perturbation, and a projection diffeomorphism. It explicitly does not claim those hypotheses for A021.

## Hypothesis table

ER010 compares the A021 setting to an infinite-dimensional NHIM theorem and concludes that every essential geometric hypothesis is false or unverified for the stated history cube.

## Direct Hopf theorem

ER010 rescales time to fix the history interval and treats delay as a coefficient. It assumes:

- constant equilibrium;
- zero excluded from both spectra;
- a simple binding imaginary pair;
- no other binding or slack imaginary roots;
- transverse crossing in delay.

It then uses equilibrium and characteristic implicit-function arguments to derive a critical-delay curve `tau_*(epsilon)=tau_*+O(epsilon)` for the full RFDE. It does not use an invariant graph and excludes global-fold conclusions.

## Parity

ER010 correctly says the yield-gap estimate loses exponential smallness at parity and does not rule out other reduction mechanisms.

## Proposed publication text

The replacement LaTeX makes the graph a conjecture, states the finite-time/slack theorem and direct Hopf theorem, and labels the original history cube as neither compact nor a manifold.