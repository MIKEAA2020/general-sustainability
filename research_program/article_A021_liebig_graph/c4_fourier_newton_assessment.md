# C4 Fourier Newton Assessment — Module 1 Numerical Preconditioner

## Objective

Advance the radii-polynomial specification from a raw Fourier seed to a phase-fixed, high-accuracy finite Fourier collocation solution with an explicit numerical Jacobian inverse. This supplies the finite Newton/preconditioner data needed before outward-rounded bounds are computed.

## Configuration

- Model: gated Candidate-A C4 at `tau=4.5`.
- Fourier truncation: `K=80` (`161` real collocation phases, four states).
- Unknowns: `644` state samples plus period.
- Phase condition: integral orthogonality to the derivative of the phase-corrected reference orbit.
- Delayed `Z` evaluated by exact Fourier phase shift.
- Smooth branch used only because the full floor argument remains positive.

## Newton correction

Initial finite collocation residual:

\[
5.47\times10^{-4}.
\]

After one Newton correction:

\[
3.73\times10^{-10}.
\]

The final residual is

\[
1.54\times10^{-10},
\]

and the final Newton correction norm is

\[
1.29\times10^{-11}.
\]

The corrected period is

\[
P=370.9311778394287~\mathrm{yr},
\]

only `6.96e-9 yr` below the phase-interpolated seed period.

The maximum state correction from the `K=80` seed is

\[
3.38\times10^{-4}.
\]

## Approximate inverse diagnostics

The finite Jacobian has

\[
\|J^{-1}\|_\infty\approx1847.86,
\]

and numerical infinity-norm condition number

\[
\kappa_\infty(J)\approx1.02\times10^7.
\]

The double-precision inverse defect is

\[
\|I-J^{-1}J\|_\infty\approx2.83\times10^{-9}.
\]

The large inverse norm confirms that outward-rounded preconditioning and a carefully scaled phase condition are necessary. It also explains why raw residual size alone cannot be treated as the radii-polynomial bound `Y`.

## Smoothness margin

At the corrected collocation nodes, the minimum full memory-floor argument is

\[
1.47554288\times10^{-3}>0.
\]

This remains numerical nodewise evidence; interval convolution and a between-node/tail bound are still required.

## What is newly closed

1. A finite Fourier nonlinear system and phase condition are explicitly implemented.
2. A high-accuracy finite solution is obtained.
3. A usable numerical approximate inverse/preconditioner is available.
4. The period and phase are corrected simultaneously.
5. The floor margin survives the Newton correction.

## What remains for a radii proof

1. Recompute the inverse and residual with outward-rounded interval arithmetic.
2. Convert the collocation representation to the chosen `ell1_nu` coefficient norm.
3. Bound the analytic convolution tail beyond `K=80`.
4. Compute rigorous `Y,Z0,Z1,Z2` and a negative radii polynomial.
5. Validate the floor margin on the entire radii ball.

## Status

`FINITE_FOURIER_NEWTON_SYSTEM_SOLVED_HIGH_ACCURACY`

This is not yet `CAP-ORB`; it is the numerical preconditioner input to that proof.