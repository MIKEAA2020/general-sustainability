# ER018 Point Inventory — Preliminary Intake Pending Parallel Audit 2

## Status

Received as the first of two parallel audits. This inventory preserves strong points and flags issues for later joint adjudication. No source implementation or final disposition is made until the second audit is received.

## Strong points

1. Correctly refuses to fabricate missing A021 kinetics, parameters, spectra, equilibria, or periodic solutions.
2. Correctly distinguishes abstract equilibrium/periodic-orbit templates from concrete A021 verification.
3. Correctly treats a zero-dimensional equilibrium as an equilibrium-continuation problem rather than a regional graph.
4. Correctly identifies the periodic-orbit tangent multiplier and all nontrivial Floquet modes as the relevant splitting data.
5. Correctly includes inverse-tangent/conorm prefactors in the map bunching inequalities.
6. Correctly states that slack stability supplies only the slack normal rate.
7. Correctly requires a numerical domination table rather than sign-only assertions.
8. Correctly localizes RFDE smoothness and perturbation estimates to bounded trajectory tubes.
9. Correctly separates a semiflow theorem from a sampled-map theorem plus a sampled-to-semiflow proof.
10. Correctly preserves the final conservative theorem hierarchy and supplies no publication overclaim.

## Issues for joint adjudication

1. The statement that `C([−tau,0],K_x)` is noncompact unless `K_x` is a singleton is false. Finite or sufficiently disconnected targets can force continuous histories to be constant. Use the established path-rich/nonempty-interior qualification.
2. The blanket statement that the history family is not a `C2` Banach submanifold is too broad without target hypotheses. Mapping-space manifold structures may exist; this still does not provide compactness, finite dimensionality, invariance, or normal hyperbolicity.
3. “The only” compact finite-dimensional invariant manifolds nameable without a vector field is rhetorically too strong. Equilibria and periodic orbits are the only useful generic templates supplied here, but higher-dimensional invariant manifolds are logically possible and simply unverifiable without `F`.
4. A finite union of equilibria and periodic orbits is not automatically one embedded manifold of a fixed dimension; components of mixed dimensions must not be bundled as a single manifold.
5. The BLZ citation to a 1999 TAMS article with the 1998 memoir title is bibliographically suspect and conflicts with the verified source already used in A021: Bates–Lu–Zeng, Memoirs AMS 135 (1998), no. 645. ER018 expressly admits the source PDF was not open, so its theorem-number and exact-statement discussion cannot count as source matching.
6. The periodic-orbit persistence reference remains a template until an exact RFDE Poincaré/periodic-orbit theorem is matched; the earlier sketch was not a completed proof.
7. The `alpha=-infinity` convention for a zero tangent bundle is unnecessary and potentially confusing; state that tangent bunching is vacuous.
8. Complete continuity and differentiability claims must retain the bounded-solution and positive-time localization already adopted in the manuscript.
9. If delay is varied, smooth fixed-space parameterization remains model-structure dependent; generic dilation on `C0` is not automatically differentiable.

## Preliminary effect on current implementation

ER018 does not identify an omitted manuscript-level correction beyond qualifications already present in the implemented source. It mainly confirms that the three open actions—construct a concrete NAIM, compute domination, and match an exact theorem—cannot be executed from the currently available model record. Final assessment is deferred until the second parallel audit.