# Computation Closure Docket

## C1. A021 validated continuum periodic orbit

**Inputs:** K80/K120/K240 Fourier coefficients, phase-fixed Newton solution, finite storage hull, off-grid residual, derivative bounds, CAP dossier.

**Still required:** rigorous infinite-tail or validated collocation/Sobolev enclosure; true orbit ball; preserved floor margin; exact phase condition; outward-rounded certificate.

**Output gate:** interval existence and local uniqueness of one continuum periodic orbit in a declared RFDE phase space.

## C2. Continuum monodromy and Floquet data

**Required:** validated variational equation, monodromy/operator enclosure, simple neutral phase direction, stable multiplier enclosure, spectral projection bounds, finite-to-continuum error.

**Do not accept:** mesh convergence or finite matrices alone.

## C3. Product bunching and localization

**Required:** prefactor-aware tangent/normal estimates on the validated orbit/tube; continuum product inequality; invariant graph localization; projected-base representation.

**Dependency:** C1 and C2.

## C4. Concrete A021 coupling

**Required:** unique declared or source-derived `G,f,g`, regularity class, tube/slack preservation, derivative bounds, perturbation norm, mapping to the abstract graph theorem.

**Dependency:** C1–C3. If no source-derived coupling exists, state a new model class rather than claim completion of the old application.

## C5. A025 fold certification

**Required:** scaled Moore–Spence system, phase condition, bordered normalization, interval Newton/Krawczyk enclosure, nondegeneracy, and transfer from discretized collocation to the continuous DDE.

**Do not accept:** continuation turning point, high-accuracy Newton residual, or Hopf certificate as a fold certificate.

## C6. Stage/spatial version reconciliation

**Required:** one hashed equation/parameter/code version; reconcile stage equilibria; retain `g_stage` as a timescale with rate `1/g_stage`; prevent stale `C_E` transfer; rerun modal/spatial outputs; establish one independent validated result before Paper 7.

## C7. A011/A012/A018/A020/A022–A025 publication artifacts

For each claimed computation archive:

- exact source and parameter hash;
- histories/initial conditions;
- solver/compiler/library versions;
- tolerances, meshes, event rules, root counts;
- seeds and random-number policy;
- raw and processed outputs;
- independent rerun provenance;
- environment/lock file;
- persistent release identifier when stable.

## C8. Reproducibility status matrix

Return one row per claim: source truth status; local rerun status; interval/continuum status; artifact completeness; independent rerun; promotion gate; revocation trigger.
