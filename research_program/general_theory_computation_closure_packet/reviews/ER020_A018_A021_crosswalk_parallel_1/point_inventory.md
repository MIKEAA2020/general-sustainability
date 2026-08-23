# ER020 Point Inventory — Preliminary, Pending Remaining Parallel Audits

## Status

Received as the first of several A018-to-A021 crosswalk audits. No implementation or final adjudication is authorized until the announced batch is complete and reviewed jointly without recency bias.

## Strong points

1. Correct final status: `PARTIAL_CROSSWALK_ONLY`.
2. Correctly identifies C4 as the closest architectural match.
3. Correctly forbids silent transfer of C3 spectra to C4, ungated results to gated systems, or Candidate B data to Candidate A.
4. Correctly forbids dropping `U` from C5 without a closure/projection argument.
5. Correctly separates a compact equilibrium point from a regional graph.
6. Correctly requires one named periodic orbit, branch identity, complete Floquet complement, simple phase multiplier, invariant projections, and off-fold parameter choice.
7. Correctly refuses to infer full Floquet stability from selected dominant multipliers.
8. Correctly identifies concrete `f,g`, slack blocks, uniform yield-gap region, and `C1` perturbation bounds as missing.
9. Correctly requires prefactor-aware bunching rather than sign-only rates.
10. Correctly separates persistence, stable foliation, asymptotic phase, and vertical projection.
11. Correctly preserves the existing finite-time, slack-tube, equilibrium, and characteristic-crossing hierarchy.
12. Correctly recommends no A021 source change from this audit alone.

## Access-limited claims that are false at workspace level

1. The canonical A018 and A021 files are accessible in the shared workspace and have been inspected internally.
2. Exact C3 equations, Candidate-A parameters, C4 working equations, equilibrium, delay placement, characteristic matrix, Hopf data, and selected Floquet evidence are available.
3. A021 explicitly defines the product supremum norm in the corrected source.
4. `F^k` can be crosswalked to the C4 working vector field after a formal model-selection decision; it is not algebraically unavailable.
5. A018 explicitly states the dynamic-target closure and when `U` is a driven nonfeedback auxiliary.
6. Units and parameter tables exist in A018, although the crosswalk still needs exact extraction.

These corrections do not overturn ER020's final partial-crosswalk decision because concrete slack/coupling and complete NAIM data remain missing.

## Additional substantive issue exposed by ER020

The C3/C4 memory equation contains an outer `max(0,·)`, which is not globally `C1` at its switching surface. A local persistence argument must choose a neighborhood in which the floor is inactive (as A018 states near the interior equilibrium, and for certain reported periodic orbits) or replace/match the nonsmooth formulation. This localization should be checked for any selected invariant object and perturbation tube.

## Comparison with the internal attempt

ER020 and the internal crosswalk agree on:

- C4 as the natural architectural candidate;
- no positive-dimensional concrete NAIM selected;
- missing concrete slack/coupling formulas;
- incomplete full Floquet/projection/prefactor data;
- domination not verified;
- exact theorem not source matched;
- no theorem promotion.

They differ because the internal attempt had source access and therefore established the exact C4 equations, Candidate-A parameters, equilibrium candidate, fixed delay structure, and existing characteristic/Floquet evidence.

## Provisional disposition

Retain ER020's safeguards and no-promotion decision. Correct its access-limited `MISSING_FROM_SOURCE` entries using the internal source crosswalk. Add the floor-inactivity/smooth-neighborhood check to the joint batch docket. Await the remaining audits before any source or action-status change.