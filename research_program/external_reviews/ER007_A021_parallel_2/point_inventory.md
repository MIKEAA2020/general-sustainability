# ER007 Point Inventory — A021 Parallel Proof Response 2

## Status

Received for later joint adjudication with the internal provisional proof, ER006, and forthcoming parallel responses. No recommendation is implemented from ER007 alone.

## Valid or potentially valid points to adjudicate

1. Compactness of `C([−τ,0],Kx)` must be qualified for degenerate finite/totally disconnected target sets.
2. Backward uniqueness is route-specific; a semiflow persistence theorem may avoid it.
3. Finite-time tracking should allow different initial histories and bound initial mismatch plus coupling.
4. Uniform boundedness/Lipschitz assumptions on a common neighborhood are preferable to unexplained compact confinement.
5. An elementary graph transform is invalid unless images remain single-valued graphs over the base.
6. Fibre contraction over a noninvertible base may require an inverse-limit graph.
7. Time-T invariance alone needs a uniqueness/class argument before full semiflow invariance follows.
8. NHIM bunching needs inverse-tangent/conorm control, not only a forward tangent norm.
9. Quantitative C1 `O(epsilon)` closeness needs stronger regularity/uniform derivative control.
10. A compact embedded Banach manifold is finite-dimensional.
11. Vertical projection needs global embedding/injectivity, not merely local transversality.
12. RFDE compactness/smoothing must be localized to uniformly bounded solution families.
13. Hopf persistence must distinguish coupling `epsilon` from bifurcation parameter `mu`.
14. Nonlinear Hopf branch and criticality require sufficient smoothness and nonzero first Lyapunov coefficient.
15. Yield-parity limitation is appropriately narrow.

## Internal inconsistencies in ER007 to preserve for joint review

1. The specialist assessment says Theorem 2’s graph transform is false in the stated generality, but Output B calls Theorem 2 valid and Output C repeats the invalid image/intersection graph transform. The final assessment again calls Theorem 2 proved. These positions cannot all be adopted.
2. The review correctly says finite-time assumptions should allow differing initial histories, but its publication-ready LaTeX reverts to identical initial data and a common compact set.
3. The review correctly demands inverse-tangent bunching, but its publication-ready NHIM theorem uses only forward tangent growth and `beta>r alpha` without defining alpha as backward expansion/conorm control.
4. The review correctly separates Hopf parameter `mu` from coupling `epsilon`, but Output E and the publication-ready LaTeX still formulate the root curve primarily in epsilon and even state `alpha'(0) != 0` after reparameterization.
5. The review says global compactness of RFDE time maps needs bounded-solution localization, while its LaTeX says the semiflow is compact for all `t>tau` without that qualification.
6. The noncompactness diagnosis is written unqualified in Output A even though the specialist assessment itself supplies finite/totally disconnected exceptions.
7. The hypothesis table marks `C1` closeness `O(epsilon)` as verified although the review itself says this needs stronger regularity than mere `C1`.
8. The claim that compactness of the base automatically supplies the whole bounded-geometry/tubular package needs the precise theorem and embedding hypotheses.

## Alignment with the internal proof

ER007’s strongest corrections support narrowing the internal result further:

- finite-time tracking is the only unconditional theorem;
- the compact NHIM theorem should state exact inverse-tangent bunching and stronger regularity;
- the vertical graph requires a global embedding argument;
- the direct Hopf theorem should use a distinct bifurcation parameter.

The invalid elementary graph transform criticized by ER007 does not appear in the current internal proof, so compare by content rather than theorem number.
