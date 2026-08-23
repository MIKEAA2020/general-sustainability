# ER012 Completed Remainder — Line-Level Intake and Adjudication Addendum

## Receipt identity

This addendum records the complete continuation resupplied by the user, beginning “Continuation (from the block-diagonal equilibrium Jacobian)” and ending with the safeguard against hiding a missing theorem behind “standard arguments.” It supplements `normalized_capture.md`, `remainder_capture.md`, and `point_inventory.md`. The source response contains: completion of Lemma C7; Corollary C7.1; direct Hopf Hypothesis (H) and Theorem H.1; yield parity; graph-status diagnosis; publication-ready LaTeX; a 12-item verification checklist; and final safeguards.

## Proposition-level preservation

### C7 — equilibrium continuation

ER012 defines the finite-dimensional equilibrium map

\[
\mathcal F(x,y,\varepsilon)=
\bigl(F(\widehat x)+\varepsilon f(\widehat x,\widehat y),
G(\widehat y)+\varepsilon g(\widehat x,\widehat y)\bigr)
\]

and applies the finite-dimensional implicit-function theorem at the product equilibrium. Absence of zero characteristic roots makes the equilibrium Jacobian invertible, yielding a unique local `C^r` branch and an `O(epsilon)` displacement. It then invokes RFDE spectral continuity to retain hyperbolicity and attraction for small coupling. It expressly limits this to a point, not a graph over a history region.

**Correction:** the displayed derivative blocks are `DF(hat x*) o iota_X` and `DG(hat y*) o iota_Y`, whereas with ER012’s definition
`Delta(0)=0 I - DF(hat x*)(e^{0·}I)`, they equal `-Delta_x(0)` and `-Delta_y(0)`, not “precisely” the characteristic matrices. Invertibility is unaffected. “Compact characteristic spectra” is imprecise; use continuity/localization of characteristic roots in a right half-plane.

### C7.1 — periodic orbit

ER012 asserts persistence of a hyperbolic attracting binding periodic orbit crossed with the slack equilibrium. It proposes a Poincaré-section fixed-point argument, using `C^1 O(epsilon)` closeness of solution/variational maps. It correctly limits the resulting graph, after phase choice, to the orbit rather than a history region.

**Correction:** a fixed time-`T` map need not map a transverse section to itself. The proof must define the return-time function and Poincaré return map, verify smoothness/transversality in the RFDE phase space (normally after the smoothing time), and then apply hyperbolic fixed-point persistence, or cite an exact RFDE periodic-orbit persistence theorem. The claim remains conditional in the controlling audit.

### H — direct characteristic crossing and Hopf

ER012 introduces a physical bifurcation parameter `mu`, continues the equilibrium in `(mu,epsilon)`, forms the full characteristic matrix, and assumes:

1. a simple binding pair at `±i omega*`;
2. no other imaginary binding roots/nonresonance;
3. no imaginary slack roots;
4. transverse crossing in `mu`;
5. `C^r` parameter dependence with `r>=1`.

It uses block diagonality, a root implicit-function theorem, and a scalar IFT on the real part to derive

\[
\mu_*(\varepsilon)=\mu_*+O(\varepsilon),\qquad
\omega(\varepsilon)=\omega_*+O(\varepsilon).
\]

It then invokes spectral separation/Rouché arguments and an RFDE Hopf theorem to claim a nonlinear Hopf bifurcation. It correctly excludes non-equilibrium binding objects and global folds.

**Controlling correction:** the hypotheses prove persistence of a simple transverse characteristic crossing, not the stated nonlinear Hopf branch under only `r>=1`. A nonlinear RFDE Hopf theorem must be identified exactly and its higher smoothness and nonlinear nondegeneracy assumptions verified. If delay is varied, formulate the family on a fixed phase space (for example by time rescaling) before asserting `C^r` parameter dependence. The global spectral-exclusion step also needs theorem-matched uniform root localization, not only compact-contour language.

### Yield parity

ER012 correctly says parity removes the exponential yield-gap certificate. Its sentence that “every argument that uses small epsilon loses its small parameter from the yield gap” is retained only with the final qualification: `C_gap`, physical coupling, or another independent mechanism could remain small. Parity defeats this certificate, not all perturbative reductions.

### Original graph diagnosis

ER012 restates noncompactness, lack of manifold structure, missing binding-normal directions, semiflow noninvertibility, and embedding-versus-vertical-graph concerns. The core diagnosis is accepted.

**Qualifications:**

- noncompactness must be stated for the intended path-rich target domains, not every nonsingleton compact target;
- the blanket denial of mapping-space Banach-manifold structure is too strong;
- neither qualification rescues compactness, finite dimensionality, invariance, or normal hyperbolicity for the A021 history cube.

### Publication-ready graph conjecture

ER012 proposes a compact binding NAIM, a complemented product splitting, stable rates, tangent growth, localized tubular control, persistence, attraction, and a separate projection-diffeomorphism condition.

**Corrections before any use:**

- replace simplified `beta>r alpha` by the exact selected theorem’s conorm/inverse-tangent inequalities;
- use a complete stable/tangent/unstable splitting consistent with the claim (or explicitly impose a purely normally attracting case);
- verify the perturbation topology and parameter regularity behind `C^1 O(epsilon)`;
- correct the Bates–Lu–Zeng citation and match the exact theorem;
- retain the graph over the perturbed projected base only;
- do not call the text a theorem for concrete A021.

### Verification checklist

All 12 obligations are retained by content: explicit compact invariant object and dimension; confinement; tangent growth; every normal rate; exact domination; `C^1` perturbation norm; projection transversality; route-specific backward uniqueness; equilibrium/characteristic Hopf checks; uniform yield gap; neighborhood/constants/maximal time; and smoothing/equicontinuity.

**Correction to item 12:** eventual/complete continuity must be localized to bounded solution families with uniform vector-field bounds and stated for the exact time threshold supplied by the RFDE theorem; boundedness alone is not enough, and no blanket global complete-continuity assertion should be made.

## Net decision

The resupplied exact continuation confirms rather than overturns expanded decision `D-A021-JOINT-02`. Adopt the equilibrium IFT after the sign correction; retain periodic-orbit persistence only conditionally with an exact return-map/theorem argument; retain the direct characteristic-crossing curve; demote the nonlinear Hopf conclusion until exact smoothness and nondegeneracy are supplied; retain narrow parity language; and keep the graph conjectural with exact theorem matching. No A021 source implementation is authorized by this intake.