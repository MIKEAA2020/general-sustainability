# External Verification Sources for A018–A025

## Invariant-manifold scope

1. Eldering, *Persistence of noncompact normally hyperbolic invariant manifolds*: https://arxiv.org/pdf/1204.1310
   - Normal hyperbolicity requires normal contraction/expansion to dominate tangent dynamics through a spectral-gap condition.
   - Classical persistence assumes compactness; noncompact extensions require bounded geometry and additional uniformity.
   - This supports the audit finding that A021’s stable slack equilibrium alone does not establish a normally hyperbolic graph over unrestricted binding histories.

2. General Fenichel references and expositions emphasize compact normally hyperbolic manifolds and tangent/normal rate domination. A finite-dimensional Fenichel citation does not automatically supply an RFDE-semiflow theorem.

## First-passage formulas

3. Standard Brownian first-passage references confirm that a drifted Brownian motion reaches a fixed barrier with an inverse-Gaussian law having mean `distance/drift`, shape `distance²/diffusion²`, and variance `distance*diffusion²/drift³`. One accessible summary is: https://metricgate.com/docs/first-passage-time/

4. Transforming geometric Brownian motion to log space yields a Brownian first-passage problem. This supports A024’s Itô formula and inverse-Gaussian passage-time result under the declared GBM surrogate.

These sources verify the general mathematical background only. They do not verify the packet’s numerical parameter values, continuation branches, data tables, or software outputs.