# Second-fold search on the upper branch — PRE-REGISTRATION (frozen before execution)

**Owner instruction** (session message, verbatim protocol):

1. **Seeded carry continuation** starting from a converged cycle near
   \( \tau_+ = 150.358 \), stepping downward in \( \tau \), carrying the
   delay history.
2. **Collocation / Moore–Spence refinement** at any suspected turning
   point.
3. **Krawczyk certification** if a candidate fold is found.
4. Report separately:
   - mathematical branch existence,
   - generic basin reachability,
   - any collocation failures.

**Owner verdict rule** (verbatim): "If a second fold is found and
certified, then the current model has two folds. If not, the honest
result remains: Under the pre-registered protocol, the current
Candidate-A gated model has one certified lower fold at
\( \tau_f \approx 5.5872362 \), with an upper basin boundary near
\( 148.6\text{–}149.5 \) whose exact bifurcation nature is unresolved."

This document freezes every parameter, grid, seed, acceptance criterion,
and stop rule before any continuation step is taken. The git history
provides the freeze→execute ordering (this pre-registration is committed
before the results). Nothing below is chosen with reference to any
observation made below \( \tau = 130 \) — no record of any kind exists
there (the P4 five-regime campaign's `small_upper` records end at
\( \tau = 130.0 \) because that was the campaign's pre-registered window
end, not a failure).

## 0. Model and machinery (frozen, all committed code imported unmodified)

- **Model**: `a025_fold/a025_model.py` — the audited Candidate-A gated
  model (SHA-256 `c1dae18bd8d470fe786b018f1896b3d25e5ab50a1ee8a014e7d9
  524574f05d2f`, Task 65's model-consistency audit: identical to all four
  manuscripts' model statements at the registered baseline). Parameters
  (bit-verified at stage 0 against the declared numbers):
  r = 0.02, K = 100, q = 0.001, eta = 0.914, Emax = 30, delta0 = 0.01,
  Dref = 1, taum = 5, k = 10, delta = ln 2 / 10, Zref = 1.
- **Collocation / continuation / fold machinery**:
  `a025_fold/a025_fold_pipeline.py` (Fourier collocation m = 64 primary,
  phase condition, Newton with stall-acceptance 3e-9, Moore–Spence fold
  solve) and `p4_five_regime_campaign/p4_campaign.py`
  (`continue_tau`, `pseudo_arclength_pass`, `augmented_newton`,
  `FloquetTracker`, `refine_crossing`, `_fourier_eval_cols`) — imported
  unmodified; code hashes recorded at stage 0.
- **Basin machinery**: `p4_five_regime_campaign/p4_kernels.py`
  `basin_run` (method-of-steps RK4, circular delay buffer, linear
  interpolation of the delayed read at the exact tau), verified
  equivalent to `a025_model.rhs` to < 1e-12 over 20,000 random states at
  stage 0.
- **Interval machinery**: `interval_lib.py` + the assembly of
  `a025_fold/a025_fold_krawczyk.py` (exact circulant shift family,
  interval Jacobian of the Moore–Spence system, double-double centered
  dots) — imported unmodified by `second_fold_krawczyk.py`.

## 1. Seed (frozen)

The P4 campaign's converged `small_upper` cycle at
\( \tau = 150.30847731014137 = \tau_+ - 0.05 \) (the `switch` record,
residual 6.2e-12, N_ptp 0.1003, T 159.279, Floquet mu1 = 1.0000878,
unstable), read from `p4_five_regime_campaign/p4_branch_orbits.npz`
key `150.30847731`. Its collocation residual is re-verified
\( \le 1e-10 \) at stage 0 before any continuation step. This is the
converged cycle nearest to the interval-certified upper Hopf
\( \tau_+ \in [150.3584773101408, 150.3584773101421] \).

## 2. Stage A — seeded carry continuation, stepping DOWNWARD in tau

- Natural-parameter continuation DOWN in \( \tau \) with the campaign's
  own frozen rules (imported function, no re-tuning): secant predictor
  from the previous converged orbit (the carried delay history — the
  orbit supplies the delayed-Z segment of the collocation system),
  `fp.newton` corrector (tolerance 1e-11, stall-accept 3e-9), acceptance
  only if peak-to-peak > 1e-6 and Nyquist-relative < 0.01; step growth
  x1.3 (cap 0.5), step shrink x0.4 on failure, dtau_min 1e-7,
  max_points 400, dtau0 = 0.2, direction = -1.
- Floquet tracking (variational segment map, Arnoldi 128, deterministic
  LCG start seed 1) at every accepted point, recorded per point
  (mu1 mod/re/im, mu2/mu3, trivial, alignment) — the campaign's schema.
- **Stop rules** (frozen):
  - **S-floor**: \( \tau \le 5.587236199 \) (the certified lower fold's
    tau 5.587236198690 plus 1e-9; the a-priori floor of the search —
    no stop-rule dependence on what is found in between);
  - **S-stall**: the campaign's stall rules (dtau collapse below
    dtau_min, > 200 failures, or tau progression stopped);
  - **S-budget**: 400 accepted points.
- The stage-A output is the branch record
  `second_fold_branch.csv` + `second_fold_orbits.npz`; every accepted
  point carries its own residual, Nyquist content, and multipliers.

## 3. Stage B — turning-point adjudication and Moore–Spence refinement

Triggered when Stage A stops by S-stall before the S-floor.

1. **Moore–Spence fold solve at m = 64** from the last converged point
   (the campaign's own usage). Acceptance criteria (frozen): MS residual
   \( \le 1e-10 \) AND the returned \( \tau_f \) within 1.0 of the stall
   point. A converged MS solution whose \( \tau_f \) lies inside
   \( [5.5872361977, 5.5872361997] \) (the certified lower-fold
   enclosure widened by 1e-6/2e-9) is classified as **the already
   certified lower fold** — a connection finding, NOT a second fold.
   An MS convergence rejected under these rules is recorded as such.
2. **Pseudo-arclength pass** through the suspected turn (Keller,
   ds0 = 0.05, window (S-floor, 150.5), up to 16 points past a tangent
   tau-sign change, max 220 steps) — records points past any turn.
3. If the MS solve is accepted (a candidate second fold): **three-order
   Moore–Spence** (m = 64/96/128, Fourier-resampled seeds — the
   campaign's seeding) with agreement criterion: the three \( \tau_f \)
   values agree to \( \le 1e-6 \) (the campaign's ORDER_AGREEMENT).
4. **Resolution ladder** (runs once, only if the arclength pass fails
   AND the MS solve is rejected/diverges — the stall is then recorded as
   a collocation failure): fresh m = 96 and m = 128 Newton solves seeded
   by Fourier-resampling of the last converged m = 64 orbit. These are
   pre-registered resolution cross-checks (the P4 campaign's analogous
   m = 128 attempt was a recorded deviation; here it is in the plan).
5. A +1-crossing bracket (dominant real multiplier, |mu1_im| < 1e-6,
   bisection refinement to width \( \le 1e-3 \), the campaign's
   `refine_crossing`) that is NOT accompanied by a stall/turn is
   recorded as a multiplier crossing only — not a fold claim.

## 4. Stage C — interval Krawczyk certification (if a candidate fold is accepted at Stage B)

- System: the m = 64 Moore–Spence system
  \( G(z) = [F(w,\tau);\ J(w,\tau)v;\ \ell\cdot v - 1] \),
  \( z = (w, \tau, v) \in \mathbb{R}^{387} \), with the exact circulant
  shift, interval Jacobian, and dd-centered dots of
  `a025_fold_krawczyk.py` — the same machinery that certified the lower
  fold (re-certified 2026-09-03), applied at the new nominal point.
- **tau-box** (constructed — no prior interval exists for the second
  fold): \( [\min_m \tau_f^{(m)} - 1e-8,\ \max_m \tau_f^{(m)} + 1e-8] \)
  over the three collocation orders of Stage B.3.
- **Radii ladder** (multiplicative, every attempt logged in the solver
  log; a certificate at any rung is valid — the Krawczyk theorem is
  unconditional on the tuning, which only searches for a box where it
  holds): base (ry, rt, rv) = (2e-9, 2e-8, 1.5e-8); rungs x1, x2.5,
  x6, x15, x40; at most 4 tightening iterations per rung.
- **Certificate requirements** (all must hold):
  1. inclusion \( K(Z) \subset \mathrm{int}(Z) \) componentwise
     (=> exactly one zero of G in Z; G' nonsingular throughout Z);
  2. the left-nullvector angle bound (sigma_2 bound) with
     \( \sin\theta < 0.1 \);
  3. both nondegeneracy constants \( \psi^T F_\tau \) and
     \( \psi^T D^2F[v,v] \) exclude zero;
  4. the full FD self-verification battery of the lower-fold
     certificate passes at the new nominal BEFORE the certificate is
     issued: pipeline J / F_tau / S cross-checks (< 1e-10 / 1e-10 /
     1e-12), all 194 (w, tau)-columns of the Jv-row block vs central
     differences (< 1e-4 relative), and the psi^T D2F[v,v] straight-line
     second difference (< 10% relative).
- **Scope honesty** (unchanged from the lower-fold certificate): this
  certifies the DISCRETIZED m = 64 collocation system's fold. The
  continuum off-grid residual stage and the infinite-dimensional (RFDE)
  lift remain open, as they do for the lower fold.

## 5. Stage D — generic basin reachability (frozen grids)

Machinery, histories, and classification exactly the campaign's: H1 =
(90, Z*, 0.5 E*), H2 = (5, Z*, 15), H3 = (1.01 N*, 1.01 Z*, 1.01 E*);
dt = 0.02; horizon 4e4; tail 1800; captured = tail RSD >= 2%;
settles = < 0.1%; else intermediate; clip and gate-floor flags
recorded.

- **Grid A** (always run — fills the campaign's untested 130–147 gap
  below the capture onset):
  \( \tau \in \{133, 136, 139, 142, 144, 145, 146\} \times \{H1, H2,
  H3\} \).
- **Grid B** (if a fold candidate is accepted at Stage B with location
  \( \tau_{f2} \)): \( \tau \in \{\tau_{f2} - 2, \tau_{f2} - 1,
  \tau_{f2} - 0.5, \tau_{f2}, \tau_{f2} + 0.5, \tau_{f2} + 1,
  \tau_{f2} + 2\} \) (rounded to the nearest 0.05) x {H1, H2, H3}, plus
  dt-halving (dt = 0.01) at \( \tau_{f2} \) for all three histories.
- **Grid B'** (if NO fold — the stall location \( \tau_c \) replaces
  \( \tau_{f2} \) in the same rule).
- The basin archive is reported SEPARATELY from branch existence: the
  basin runs say nothing about the mathematical branch; the collocation
  records say nothing about basins.

## 6. Records, reporting, and the verdict

- Records: `second_fold_branch.csv` (the campaign's branch schema),
  `second_fold_basin.csv` (the campaign's basin schema),
  `second_fold_orbits.npz`, `second_fold_ms.npz` (z, ell at m =
  64/96/128), `second_fold_krawczyk.json` (if Stage C runs),
  `second_fold_results.json`, `second_fold_status.json`, the solver log
  `second_fold_run.log`, and `second_fold_report.md`.
- The report has three separate sections exactly as instructed —
  (i) mathematical branch existence, (ii) generic basin reachability,
  (iii) collocation failures — and then applies the owner's verdict
  rule verbatim.
- Comparison discipline: the only inherited numbers used are the frozen
  certified inputs (the tau +/- interval certificates, the lower-fold
  Krawczyk enclosure, the campaign's seed orbit and basin
  classifications at the grid points they already cover). No legacy
  or exploratory number steers any choice; the search region below
  \( \tau = 130 \) has no prior records of any kind.

## 7. Provenance statement

Executed by `second_fold_search.py` (stages 0/A/B/D and report
assembly) and `second_fold_krawczyk.py` (stage C) in this directory.
All parameters, grids, seeds, acceptance criteria, stop rules, and the
radii ladder are the frozen ones above; deviations (if any) will be
recorded as deviations with reasons, never silently. The first-fold
(lower-fold) certificate is untouched; this search writes only into
this directory, the artifact manifest, PROOF_MANIFEST, and the repo
worklog.
