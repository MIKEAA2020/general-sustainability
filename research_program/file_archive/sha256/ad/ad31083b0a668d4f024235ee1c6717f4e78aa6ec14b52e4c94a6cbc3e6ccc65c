# C4 Sixth-Derivative Orbit-Ball Sensitivity

## Objective

Test whether the sixth-derivative coefficient bound used in the block-Neumann tail estimate is stable under corrections of the size expected from the continuum periodic-orbit validation.

## Test ball

Use a physical-sup perturbation radius

\[
r_u=2\times10^{-5},
\]

slightly larger than the current inverse-times-off-grid-defect scale (`about 1.45e-5`).

Eighty random real trigonometric perturbations through mode 20 were normalized in physical supremum norm. Eight additional constant coordinate perturbations were included.

## Results

Base sixth-derivative coefficient sum:

\[
L_6=9.21338\times10^{-5}.
\]

Across 88 perturbations:

\[
L_6^{\min}=9.21257\times10^{-5},
\]

\[
L_6^{\max}=9.21464\times10^{-5}.
\]

Maximum change:

\[
1.264\times10^{-8}.
\]

Empirical sensitivity:

\[
\frac{\Delta L_6}{r_u}
\approx6.32\times10^{-4}.
\]

This is negligible relative to the factor-two validation allowance. The factor-two target

\[
2L_6\approx1.84268\times10^{-4}
\]

still lies below the required block-Neumann threshold `2e-4` by approximately

\[
1.57\times10^{-5}.
\]

## Interpretation

Orbit-ball sensitivity is unlikely to consume the sixth-derivative validation margin. The remaining task is an all-direction interval bound, not evidence of numerical instability.

A rigorous implementation should prove an orbit-ball Lipschitz constant below approximately

\[
0.78,
\]

because `0.78*(2e-5)` would consume the remaining `1.57e-5` margin. The empirical value is around `6.3e-4`, more than three orders of magnitude smaller.

## Status

`SIXTH_DERIVATIVE_ORBIT_BALL_SENSITIVITY_NUMERICALLY_NEGLIGIBLE`

`INTERVAL_ALL_DIRECTION_SENSITIVITY_PENDING`