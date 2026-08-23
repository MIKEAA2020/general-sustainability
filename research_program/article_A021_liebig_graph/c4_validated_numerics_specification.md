# Validated-Numerics Specification for the C4 Periodic NAIM Candidate

## Objective

Convert the current empirical C4 periodic-orbit and monodromy evidence into a computer-assisted proof with outward-rounded bounds. This specification is executable by an interval Fourier/collocation package; it does not claim that the proof has already run.

## Fixed object

- Model: gated Candidate-A C4 working core.
- Delay: `tau_x=4.5 yr`.
- Periodic branch: selected lower-window large-cycle candidate.
- Reference period after subgrid phase correction:

\[
P_0=370.9311778463889~\mathrm{yr}.
\]

- Reference phase: maximum of `N`.
- Fourier seed: 512 positive and 512 negative modes per state in `computations/c4_tau4p5_cap_seed.npz`.
- Direct spectral residual:

\[
\|u'_0-F(u_0,u_0(\cdot-\tau_x))\|_\infty
\le6.80\times10^{-6}.
\]

- Endpoint phase mismatch before periodic Fourier representation:

\[
\le4.90\times10^{-7}.
\]

- Minimum full memory-floor argument:

\[
m_{\rm floor}=1.4755423\times10^{-3}.
\]

## Module V1 — Periodic-orbit enclosure

### Fourier formulation

Set `s=t/P` and write

\[
u(s)=\sum_{k\in\mathbb Z}a_ke^{2\pi i k s},
\qquad a_{-k}=\overline{a_k}.
\]

The delayed memory coordinate is

\[
Z(s-\tau_x/P)
=
\sum_k a_{k,Z}e^{-2\pi i k\tau_x/P}e^{2\pi i k s}.
\]

Solve

\[
\mathcal F(a,P)=0,
\]

where the four differential components are

\[
2\pi ik a_{k,j}-P\widehat{F_j(u,u_{Z,\rm del})}_k=0,
\]

and append the phase condition

\[
\int_0^1\langle u(s)-u_0(s),u_0'(s)\rangle\,ds=0.
\]

Work in the weighted convolution Banach algebra

\[
\ell^1_\nu
=\left\{a:\sum_k|a_k|\nu^{|k|}<\infty\right\},
\qquad \nu>1.
\]

### Smooth-branch condition

Within the candidate ball of radius `r`, prove

\[
m_{\rm floor}-L_{\rm floor}r>0.
\]

Then the outer `max` is identically the smooth positive branch throughout the validated orbit tube.

### Radii-polynomial test

Let `A_K` be an interval approximate inverse of the truncated Jacobian at modes `|k|<=K`, with analytic diagonal inverse on the tail. Compute outward-rounded bounds

\[
Y=\|A\mathcal F(\bar a,\bar P)\|,
\]

\[
Z_0=\|I-AA^\dagger\|,
\qquad
Z_1=\|A(A^\dagger-D\mathcal F(\bar a,\bar P))\|,
\]

and a Lipschitz bound `Z_2(r)` for the derivative. Validate a radius `r_orb` such that

\[
p(r)=Y+(Z_0+Z_1)r+Z_2(r)r^2-r<0.
\]

### Required output

- interval period `[P_-,P_+]`;
- unique periodic orbit in the phase-fixed ball;
- `C1` or stronger orbit error bound;
- validated floor margin;
- explicit Fourier-tail bound.

## Module V2 — Monodromy and Floquet enclosure

### Variational equation

Along the validated orbit,

\[
\dot v(t)=A(t)v(t)+D(t)v_Z(t-\tau_x),
\]

where `A(t)` and `D(t)` are the exact derivatives of the smooth C4 branch.

Use the same Fourier/collocation representation to validate the one-period solution operator or a finite-rank projection plus a compact tail bound.

### Phase multiplier

The exact tangent function `u'(t)` supplies multiplier `1`. Prove algebraic simplicity by validating that the phase-fixed variational boundary-value operator is invertible on the complement.

### Stable multiplier disks

Prove:

1. exactly one multiplier lies in a disk `D(1,r_phase)`;
2. the leading nontrivial multiplier lies in a disk centered near `0.68767` with outer modulus below a chosen `mu_*<1`;
3. every remaining nonzero multiplier lies in `|mu|<=r_tail<mu_*`;
4. the associated Riesz projections are bounded in the history supremum norm.

A sufficient target is

\[
r_{\rm phase}<10^{-4},
\qquad
\mu_*<0.69.
\]

## Module V3 — Slack equilibrium enclosure

For the identical C4 slack block at `tau_y=10`, validate the characteristic determinant count already supported numerically:

\[
\lambda_{1,2}
=-0.00052673009564114
\pm0.0220846350193287i.
\]

Use interval argument-principle winding or interval Newton plus a validated contour lower bound to prove:

- this pair is unique in `Re lambda>=-0.0006`;
- no roots lie in `Re lambda>=-0.0005`;
- the next root is left of `-0.0010` except for the separately enclosed real root near `-0.0010315`.

Then validate the semigroup operator norm at `T=40P` directly or through a resolvent/Laplace bound.

## Module V4 — Continuum product bunching

The finite-discrete extrapolations are

\[
q_{30}\approx0.9516,
\qquad
q_{35}\approx0.3376,
\qquad
q_{40}\approx0.1164.
\]

Use `T=40P` for validation. Combine outward-rounded errors:

\[
q_{40}^{\rm cont}
\le
(M_c+\delta_c)
\max\left
\{
\|S_{x,40}^{\rm num}\|+\delta_x,
\|T_{y,40}^{\rm num}\|+\delta_y
\right
<\frac14.
\]

The target `1/4`, rather than merely `1`, reserves margin for chart transport, inverse-base estimates, and nonlinear perturbation remainders.

## Module V5 — Coupling and theorem boundary

The validated unperturbed product does not identify A021's actual coupling. A concrete persistence theorem still requires either:

1. source-derived `G,f,g` and a verified `C1` tube; or
2. an explicitly declared new two-block perturbation class

\[
\dot z=H_0(z_t)+R_\varepsilon(z_t),
\qquad
\|R_\varepsilon\|_{C^1(\mathcal U)}\le C|\varepsilon|.
\]

Do not call option 2 the original A021 vector-Liebig model unless the coupling is supplied.

## Acceptance conditions for theorem promotion

Promotion is permitted only if all are true:

- `CAP-ORB`: validated unique periodic orbit and floor margin;
- `CAP-FLOQ`: simple unit multiplier and complete stable spectral enclosure;
- `CAP-PROJ`: bounded continuum invariant projections;
- `CAP-SLACK`: validated slack root count and operator norm;
- `CAP-BUNCH`: continuum `q_40<1/4`;
- `MODEL-COUPLING`: concrete or explicitly declared perturbation class;
- `THEOREM`: exact persistence theorem match or complete graph-transform proof;
- `SEMIFLOW`: sampled-to-semiflow promotion proved;
- `PROJECTION`: projected binding curve is a global embedding.

Until then the manuscript remains at numerical-NAIM-candidate status.

## Machine artifacts

- `computations/c4_tau4p5_cap_seed.npz`
- `computations/c4_tau4p5_cap_seed.json`
- `computations/prepare_c4_cap_seed.py`
- existing orbit, monodromy, root-count, and prefactor scripts/JSON summaries.
