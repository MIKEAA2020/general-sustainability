# Minimal Two-Block Periodic-NAIM Scaffold

## Purpose

This document performs the next feasible step after selecting and numerically verifying a gated C4 periodic binding orbit. It defines a concrete **uncoupled** two-block product and derives quantitative targets for a future persistence proof. It does not invent the vector-Liebig coupling and does not promote the A021 manuscript.

## Concrete unperturbed product

Use a common history phase space

\[
B=C([-10,0],\mathbb R^4)\times C([-10,0],\mathbb R^4).
\]

### Binding block

- gated Candidate-A C4;
- institutional delay `tau_x=4.5 yr` (the functional evaluates `Z_x(-4.5)`);
- selected attracting periodic orbit `Gamma_x`;
- reproduced period `P_x=370.95 yr`;
- binding normal multiplier `mu_x approximately 0.68769`;
- binding normal exponent `beta_x approximately 0.00100936 /yr`;
- phase-tangent history norm ratio `M_c approximately 4.55356`.

### Slack block

- identical gated Candidate-A C4 equations and parameters;
- institutional delay `tau_y=10 yr` (the functional evaluates `Z_y(-10)`);
- equilibrium

\[
y_*=(89.52562,397.8665,\ln2/10,2.08962).
\]

Method-of-lines convergence and direct determinant refinement give the rightmost characteristic pair

\[
\lambda_{y,\pm}
=-0.00052673009564114
\pm 0.0220846350193287i,
\]

with determinant residual below `3e-21`. Other refined roots include

\[
-0.00103151651411957
\]

and

\[
-0.171955805544438\pm0.291612075038603i.
\]

The provisional slack rate is

\[
\beta_y\approx0.00052673\ {\rm yr}^{-1}.
\]

This is faster than the same equilibrium at `tau=4.5` and remains within the source-stated stable interval. Different block delays are represented on the common maximal history interval `[-10,0]`.

## Product invariant object

At zero coupling,

\[
\mathcal M_0
=\Gamma_x\times\{\widehat y_*\}
\subset B.
\]

It is a compact one-dimensional history manifold if the selected C4 cycle is accepted as a smooth embedded periodic orbit. The tangent bundle is the phase direction of `Gamma_x`. The normal bundle consists of:

1. every nonphase binding-history direction;
2. the complete slack history space.

The asymptotic product rate is provisionally

\[
\beta=\min(\beta_x,\beta_y)
\approx0.00052673\ {\rm yr}^{-1},
\]

controlled by the slack equilibrium.

## Quantitative bunching target

For `C1` persistence, a representative time-map sufficient condition is

\[
M_sM_c e^{-\beta T}<1,
\]

because the phase exponent is zero. With `M_c approximately 4.55356`, the required time is

\[
T>\frac{\log(M_sM_c)}{\beta}.
\]

Illustrative thresholds are:

| assumed full normal prefactor `M_s` | required `T` (yr) | binding periods |
|---:|---:|---:|
| 1 | about 2878 | about 7.8 |
| 10 | about 7249 | about 19.5 |
| 100 | about 11620 | about 31.3 |
| 1000 | about 15991 | about 43.1 |

At 40 binding periods (`T approximately 14838 yr`), bunching would hold if the rigorous product prefactor satisfies approximately

\[
M_s<\frac{e^{\beta T}}{M_c}\approx 5.5\times10^2.
\]

The finite-discrete binding computation shows strong nonnormal transients and a phase-projection norm near `547`, so an explicit prefactor estimate is indispensable; a spectral-radius argument alone is not accepted.

## Coupling status

The actual A021 coordinate-level residuals `f,g` and physical coupling remain absent. Therefore the present scaffold supports only the perturbation class

\[
\dot z=H_0(z_t)+R_\varepsilon(z_t),
\qquad
\|R_\varepsilon\|_{C^1(\mathcal U)}\le C|\varepsilon|,
\]

on a tube `U` around `M_0`. It does not identify `R_epsilon` with the vector-Liebig system until the source supplies or authorizes explicit coupling equations.

## Newly closed items

1. Minimal block count selected: two.
2. Binding core/operator/delay selected.
3. Named positive-dimensional C4 periodic object selected and reproduced.
4. Slack core/operator/delay/equilibrium selected.
5. Common maximal history space defined.
6. Binding and slack rightmost numerical rates estimated.
7. Product rate and prefactor-dependent bunching target derived.

## Remaining theorem-critical items

1. Rigorous enclosure of the binding Floquet spectrum and phase simplicity.
2. Rigorous enclosure proving the slack pair is globally rightmost.
3. Continuum invariant projections and normal prefactors.
4. Exact BLZ theorem text and conclusion.
5. Concrete A021 `f,g` and a uniform `C1` tube.
6. Joint audit-batch adjudication before manuscript implementation.

## Disposition

The unperturbed product has advanced to a **fully specified numerical periodic-NAIM scaffold**. It remains a numerical candidate rather than a proved Banach-semiflow NAIM.