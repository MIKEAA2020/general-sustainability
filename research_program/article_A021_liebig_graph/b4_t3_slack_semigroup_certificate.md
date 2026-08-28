# B4 Continuum Transfer — Stage T3: The Slack-Block Semigroup Certificate

## Status

**CERTIFIED (2026-08-28).** The slack block's semigroup norm is rigorously
enclosed at the two transfer horizons, in outward-rounded interval
arithmetic, with the rightmost characteristic roots interval-certified
(enclosure, simplicity, and global rightmost-ness). The certificate closes
the slack channel — the risk concentrator of the B4 transfer — with
factors of 2.4 (35 periods) and 1.6 (40 periods, the theorem's own
quarter-target) against the required thresholds.

Runner: `../validated_computations/a021_c4/b4_t3_slack_semigroup_certificate.py`
(registers 0 roots with `Re lam >= -0.0005`, exactly 3 with `Re lam >= -0.05`;
artifact `b4_t3_slack_semigroup_certificate.json`; deterministic; all checks
pass).

## The object

The slack block of the two-block periodic-NAIM scaffold: the identical gated
Candidate-A C4 equations, institutional delay `tau_y = 10 yr`, linearized at
the declared equilibrium `y_* = (89.52562, 397.8665, ln2/10, 2.08962)` —
exactly the slack object of all committed discrete evidence
(`computations/c4_slack_semigroup_prefactor.py`,
`computations/c4_equilibrium_spectrum.py`). The linear constant-coefficient
DDE

    x'(t) = J x(t) + D x(t - 10),

with `D` of rank one (`D[3,2]` the only nonzero entry). The semigroup
`T_y(t)` acts on the history space `C([-10,0], R^4)` with the sup norm.

## What is certified

**Root certificates (T3a).** With `Delta(lam) = lam I - J - D e^{-lam 10}`:

1. The rightmost pair and the third root are enclosed in disks of radius
   `1e-6` on whose boundary the interval winding number of `det Delta` is
   exactly 1 (existence, location, simplicity):
   `lam_{1,2} = -0.00052673009564... +- 0.0220846350193... i`,
   `lam_3 = -0.00103151651412...`.
2. ZERO roots with `Re lam >= -0.0005` (the pair is globally rightmost —
   the interval-arithmetic upgrade of the committed 70-digit count).
3. EXACTLY THREE roots with `Re lam >= -0.05` (the three enclosed ones).
4. The analytic exterior Neumann exclusion beyond
   `|lam| > ||J||_2 + ||D||_2 e^{-a tau}` on each rectangle.

**Semigroup norm certificate (T3b).** For the certified binding period
`P_hat in [P - 3e-7, P + 3e-7]`, `P = 370.931177839426` (the A1 Stage-4d
certificate), and `T_n = n P_hat`:

    ||T_y(T_n)||  <=  Sum_{j=1,2,3} e^{Re lam_j (T_n - 10)} F_j  +  B2(T_n),

with `F_j` the sharp operator norm of `phi -> Res_j b(lam_j, phi)` — the
residue `Res_j = adj(Delta(lam_j)) / det'(lam_j)` of `Delta^{-1}` and the
functional `b(lam, phi) = phi(0) + e^{-lam 10} D int_{-10}^0 e^{-lam s} phi(s) ds`
— and `B2` the rigorous remainder bound along `Re lam = -0.05` (finite
window bounded absolutely through interval enclosures of `Delta^{-1}`;
tail bounded by a Neumann expansion of `Delta^{-1}` beyond `|lam| > ||J||_inf
+ ||D||_inf e^{0.5}` combined with second-mean-value bounds for the
oscillatory pieces, whose phases are linear with frequencies
`>= T_n - 5 tau > 0`; the whole term carries the factor
`e^{-0.05 (T_n - 10)} = e^{-648}` at 35 periods).

The mathematical basis is the classical Laplace/residue representation of
solutions of retarded functional differential equations for `t > tau` (the
eventually compact semigroup): for `t + theta > 0`,

    x(t+theta) = Sum_{j=1,2,3} e^{lam_j (t+theta)} Res_j b(lam_j, phi)
                 + (1/2 pi i) int_{Re lam = -0.05} e^{lam(t+theta)}
                   Delta(lam)^{-1} b(lam, phi) dlam,

the contour at `-0.05` picking up exactly the three certified roots. The
representation was verified numerically to 5-6 digits against a direct
method-of-steps integration of the DDE (the constant-unit history), before
the interval machinery was built.

## The certified numbers

| horizon | certified bound | requirement | margin |
|---|---:|---:|---:|
| `n = 35` (`T = 35 P_hat ~ 12982.6 yr`) | `||T_y|| <= 0.0899163` | `< 1/M_c = 0.2196084` | 2.44x |
| `n = 40` (`T = 40 P_hat ~ 14837.2 yr`) | `||T_y|| <= 0.0338848` | `< 0.25/M_c = 0.0549021` | 1.62x |

Decomposition at `n = 35`: the pair contributes `2 x 0.0448942`, `lam_3`
contributes `1.28e-4`, and the remainder `B2` is below `1e-600`. At
`n = 40`: `2 x 0.0169329` and `1.89e-5`. Both bounds exceed the committed
method-of-lines extrapolated norms (`0.07414` at 35 periods, `0.02557` at
40), as they must: those discretizations underestimate the continuum norm.

For comparison with the discrete evidence's own reading (`P_x = 370.95`,
the RK4 period estimate), the bound at `35 x 370.95` is `0.0899164` — the
period discrepancy is immaterial at the certified radii.

## What the certificate does and does not establish

Established: the slack channel of the product bunching inequality
`q_n = M_c max{||S_x^n||, ||T_y(n P_x)||} < 1` is closed at both horizons —
the slack side contributes at most `M_c x 0.0899163 = 0.41007` at
`n = 35` and `M_c x 0.0338848 = 0.15437` at `n = 40` (using the Stage-T4
certified prefactor bound `M_c <= 4.590009620`), both below 1 with the
binding channel still to be added.

Not established here: the binding channel (`||S_x^n||`, Stages T1/T2); the
theorem's remaining hypotheses (H1, H2 — see the transfer specification);
the coupled-system statement (the A2 coupling class remains declared,
awaiting the author decision — what the transfer certifies is the two-block
scaffold's bunching, not the coupled system's persistence).

Honesty statements:

- The certificate is for the linearization at the DECLARED point `y_*` (the
  scaffold's own slack object). The residual of `y_*` as an equilibrium of
  the nonlinear C4 right-hand side (componentwise `|rhs| <= 3.6e-7`) is a
  nonlinear-localization (H1) matter and does not enter the linear semigroup
  norm.
- The output history segment covers `[T_n - 10, T_n]`; all output times
  exceed `10` by more than three orders of magnitude, so the
  representation applies on the whole segment.
- The winding-count machinery is genuine outward-rounded interval
  arithmetic (mpmath `iv`, 50 digits); the contour integrals of `det Delta`
  are enclosed over adaptive segment boxes with the argument accumulation
  tracked continuously (each increment enclosure intersected with a
  rigorous variation bound `diam(box)/min|det| < pi/2`), and the total is
  discriminated to a unique integer.

## Relation to the committed evidence

- The committed `slack_root_count_verification.md` counted the same roots
  at 70-digit point precision ("high-confidence numerical root-count
  certification, not a formal computer-assisted proof"). The present
  certificate upgrades exactly that gap: the counts and the root enclosures
  are now interval-arithmetic certificates. The committed refined root
  values are reproduced (the committed strings carry their own ~2e-18
  refinement uncertainty; the present Newton refinement at 60 digits
  agrees within 5.5e-18 and the interval disks enclose both).
- The committed method-of-lines semigroup norms
  (`c4_slack_semigroup_inf_convergence.json`) are the discrete evidence;
  the certified bounds are consistent with (exceed) their extrapolated
  continuum limits, and the effective asymptotic constant of the observed
  norms (~69 at 35 periods) is now explained and bounded by the
  residue-functional decomposition: the pair mode's functional norm
  (`F_j ~ 41.9` including the delay-read amplification channel) times the
  two conjugate modes, plus the `lam_3` mode.
