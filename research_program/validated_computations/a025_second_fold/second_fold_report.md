# Second-fold search on the upper branch — EXECUTION REPORT

**Protocol**: the pre-registered plan
(`SECOND_FOLD_PREREGISTRATION.md`, committed as a3823c5 BEFORE any
continuation step; the machinery committed as 363003b before execution),
executed 2026-09-02 17:27–17:51 UTC by `second_fold_search.py` +
`second_fold_krawczyk.py` (this directory). The owner instruction this
executes, verbatim:

1. Seeded carry continuation starting from a converged cycle near
   \( \tau_+ = 150.358 \), stepping downward in \( \tau \), carrying the
   delay history.
2. Collocation / Moore–Spence refinement at any suspected turning point.
3. Krawczyk certification if a candidate fold is found.
4. Report separately: mathematical branch existence, generic basin
   reachability, any collocation failures.

Everything below ran under the frozen rules: the committed
`a025_model.py` (SHA-256 `c1dae18b…f05d2f`, the Task-65-audited
Candidate-A gated model), the committed collocation/continuation/Floquet
machinery imported unmodified, the frozen seed, grids, acceptance
criteria, stop rules, and radii ladder. Stage 0 verified: PAR
bit-identical to the declared numbers; the numba RHS equivalent to
`a025_model.rhs` to 5.68e-14 over 20,000 random states; the seed residual
6.20e-12; the model's characteristic roots at the certified tau-/tau+
midpoints pure-imaginary to ~1e-18 with |char| ~ 1e-19.

## Headline

**A second fold was found and certified.** The upper branch, continued
downward from the converged cycle at \( \tau_+ - 0.05 \), does not
terminate at the campaign's window end (τ = 130), does not fail
collocation anywhere, and does not reach the lower fold's τ: it turns at

\[
\tau_{f2} \in [64.40232720336789,\ 64.40232720337167]
\]

— an interval-Krawczyk-certified simple nondegenerate fold of the m=64
collocation Moore–Spence system, with three-collocation-order agreement
5.53e-7 (≤ 1e-6 criterion). Sixteen pseudo-arclength points past the
turn were recorded: the branch returns upward in τ as a **stable**
arm (μ1 = 0.9993 → 0.9435, monotone decreasing).

Under the owner's verdict rule — "If a second fold is found and
certified, then the current model has two folds" — **the current
Candidate-A gated model has two folds**:

| Fold | τ_f (certified) | Certificate | T_f | Amplitude (N_ptp) |
|---|---|---|---|---|
| lower (the S-branch of the small/large arms) | [5.587236198689, 5.587236198690] | inherited (a025_fold_krawczyk.json, untouched) | 315.322 | ≈ 22.3 |
| **upper (this campaign)** | **[64.402327203368, 64.402327203372]** | **second_fold_krawczyk.json (this directory)** | **72.8855** | **≈ 10.5** |

---

## (i) Mathematical branch existence

**The upper small branch exists on \( 64.40232720337 \lesssim \tau \le
150.30847731 \) — an unstable arm that emanates from the subcritical
Hopf at \( \tau_+ = 150.3584773101414 \) (eq loses stability there) and
grows in amplitude as τ decreases, meeting a fold at \( \tau_{f2} \),
past which the branch returns upward in τ as a stable arm.**

Records (all in `second_fold_branch.csv`, 200 rows; orbits in
`second_fold_orbits.npz`):

- **Seed** (the campaign's converged `switch` cycle): τ = 150.30847731014137
  (= τ+ − 0.05), residual 6.2e-12, N_ptp 0.1003, T 159.279, μ1 = 1.0000878.
- **Seeded carry continuation downward** (natural parameter, secant
  predictor carrying the previous converged orbit — the delay history of
  the collocation system — as seed): 183 accepted points, τ from
  150.308477310 down to 64.402327895, residuals ≤ 3.7e-12, Nyquist
  content < 0.01 at every point. Selected points:

| τ | N_ptp | T | E range | μ1 |
|---|---|---|---|---|
| 149.989 | 0.272 | 158.99 | [2.026, 2.158] | 1.00065 |
| 129.902 | 1.878 | 140.67 | [1.707, 2.760] | 1.04946 |
| 99.902 | 3.497 | 111.51 | [1.440, 3.995] | 1.16817 |
| 74.902 | 6.295 | 83.11 | — | **1.27745 (peak)** |
| 64.702 | 9.586 | 73.42 | [0.943, 13.833] | 1.10504 |
| 64.403120 | 10.485 | 72.90 | — | 1.00705 |
| 64.402328 | 10.535 | 72.89 | [0.919, 15.542] | 1.00069 |

  The unstable arm's dominant multiplier is real and > 1 at every
  point (imaginary part identically zero to 1e-6), peaking at 1.27745
  (τ = 74.902) and returning to +1 exactly at the fold — the classic
  saddle-node signature (a +1 crossing is not observed *along* the arm;
  the multiplier reaches +1 AT the turning point, as at the lower fold).
- **The turn**: the continuation micro-stepped and stalled in the fold
  region at τ = 64.402327895 (step collapse 0.2 → 5.3e-7, residuals
  still ~2e-12 — a genuine turning-point stall, NOT a resolution
  failure).
- **Moore–Spence m=64 from the stall point**: τ_f2 = 64.4023272033699,
  T_f = 72.88553760491024, |M| = 1.78e-12. Acceptance per the frozen
  rules: residual ok (1.78e-12 ≤ 1e-10), proximity ok (7e-7 ≤ 1.0),
  not the lower fold → **accepted**.
- **Three-order Moore–Spence** (Fourier-resampled seeds, the campaign's
  method): m=64: 64.402327203370 / m=96: 64.402326653161 /
  m=128: 64.402326650819 — **agreement 5.526e-7 ≤ 1e-6 PASS**. (The
  m=96 and m=128 values agree with each other to 2.3e-9; the 5.5e-7
  gap to m=64 is the m=64 discretization error at this amplitude —
  the certificate is for the m=64 system, with the three-order
  agreement as the discretization cross-check.)
- **Pseudo-arclength through the turn** (Keller): 16 points past the
  tangent sign change recorded, τ = 64.4023279 → 64.4382853, amplitude
  10.535 → 10.888, **μ1 = 0.9993 → 0.9435 — the past-turn arm is
  STABLE** (monotone decreasing, real at every point). The upper branch
  is therefore an S-branch mirroring the lower one: an unstable
  subcritical arm from the Hopf at τ+, a fold, and a stable returning
  arm.
- **Interval Krawczyk certificate** (the lower-fold certificate's
  machinery at the new nominal): unique zero of the Moore–Spence system
  in the box, G' nonsingular throughout, both nondegeneracy constants
  excluding zero:
  - τ_f2 final enclosure **[64.40232720336789, 64.40232720337167]**
    (width 3.8e-12; the τ-component of the initial K image is
    3.4e-14 wide);
  - \( \psi^T F_\tau \in [0.257936, 0.260750] \), excludes 0;
  - \( \psi^T D^2F[v,v] \in [-5.886629\mathrm{e}{-4}, -5.877021\mathrm{e}{-4}] \),
    excludes 0 (negative — the τ-minimum orientation of this turn, vs
    the lower fold's positive τ-maximum orientation);
  - left-nullvector angle bound sin(θ) ≤ 2.96e-6 (componentwise
    halfwidth 4.18e-6);
  - the FD self-verification battery passed BEFORE certification:
    pipeline J / F_τ / S cross-checks 1.59e-12 / 5.47e-13 / 4.22e-15;
    all 194 Jv-block columns vs central differences, max rel err
    7.77e-9; the ψᵀD2F[v,v] second difference 9.17e-4 relative;
  - polished center |G|_inf = 1.02e-12; runtime 269 s.
- **Scope** (unchanged from the lower-fold certificate): the
  certificate is for the DISCRETIZED m=64 system; the continuum
  off-grid residual stage and the infinite-dimensional (RFDE) lift
  remain open for both folds.

**What is NOT established**: the past-turn stable arm is recorded for
16 points only (τ ≤ 64.438), per the frozen arclength budget. Its
continuation toward the E~Emax face-cycle family that the basin archive
captures at 148.6–155 (N_ptp ~ 44, E ∈ [0.35, 29.9]) is the natural
conjecture — same S-branch structure as the lower fold, whose stable
large arm IS the basin-captured family — but it is UNVERIFIED: the
face family itself is not Fourier-collocatable (the P4 campaign's
honest B4 failure), and no record exists on the stable arm between
64.438 and 148.6. The connection is the obvious follow-up campaign
(owner-gated).

## (ii) Generic basin reachability

**Near the second fold, the stable past-turn arm is NOT generically
reachable; the capture onset near 148.6–149.5 is a basin boundary, not
the fold.** (`second_fold_basin.csv`, 45 runs, the campaign's machinery
and classification verbatim: H1/H2/H3, dt = 0.02, horizon 4e4, tail
1800.)

- **Grid B (around τ_f2, ±2/±1/±0.5)**: all 21 runs at
  τ ∈ {62.4, 63.4, 63.9, 64.4, 64.9, 65.4, 66.4} × {H1, H2, H3}
  **settle** to the equilibrium (tail RSD ≤ 1e-4; tail N = 89.552
  flat). dt-halving at τ = 64.4: UNCHANGED for all three histories.
  Generic initial conditions do not find the stable arm that exists
  mathematically just past the fold — its basin is empty or negligible
  at this distance from the equilibrium's own stability window
  (the eq is stable on 3.666 < τ < 150.358).
- **Grid A (the campaign's untested 130–147 gap)**: all 21 runs at
  τ ∈ {133, 136, 139, 142, 144, 145, 146} × {H1, H2, H3} **settle**;
  H1 turns "intermediate" at 145 and 146 (tail RSD 0.0012 / 0.0017 —
  critical slowing toward the capture window). No capture anywhere
  below 147.
- Together with the P4 campaign's basin archive (all settle at
  6–130; H1 capture onset at [148.6, 149.5]; captured at 149.5–155),
  the generic-reachability picture is: **the face-cycle attractor
  becomes generically reachable only in the upper window ~148.6–149.5
  and above, while the mathematical bistability created by the second
  fold (eq + stable arm) extends from τ_f2 = 64.4023 to τ+ =
  150.358.** The upper basin boundary near 148.6–149.5 is therefore a
  BASIN boundary inside a long bistable window — not the birth of the
  stable family (that is the fold at 64.4023) and not the eq's
  stability boundary (that is τ+ = 150.358, interval-certified). The
  exact nature of the 148.6–149.5 boundary remains a basin question
  (its location is defined by the histories, as the campaign's
  reversed-asymmetry finding already showed); what the second-fold
  result resolves is that it is NOT a fold of cycles — the fold is at
  64.4023.

## (iii) Collocation failures

**None on the search path.** The entire seeded carry continuation
(183 natural points, τ 150.308 → 64.402) converged with residuals
≤ 3.7e-12 and Nyquist content < 0.01; the Moore–Spence solve converged
to 1.78e-12; the three-order solves converged (7.4e-12 / 8.6e-12); the
arclength pass traversed the turn (16/16 points; one first point
stall-accepted at 2.6e-10, within the declared 3e-9 stall level; the
maximum residual over all 200 records is 1.0e-9, inside the pipeline's
documented near-fold residual floor). The resolution ladder (m=96/128
cross-checks) never triggered — the pre-registered trigger (arclength
failure AND MS rejection) did not occur.

The one honest failure of the campaign is in **stage C's frozen
certificate box, not in the collocation**: the frozen τ-box
construction (three-order spread ± 1e-8 = [64.4023266408, 64.4023272134],
width 5.7e-7) failed Krawczyk inclusion at every radii rung
(min_gap −7.35e-9 at the base radii, worsening as radii grow). The
diagnostic run (recorded in the solver log and the certificate JSON)
attributes this to the box WIDTH — the frozen construction imported the
m=64-vs-m=96/128 cross-check spread into the certificate box (~25× the
lower fold's box width), inflating the interval-Jacobian variation so
that the v-radius leaks ~6.5e-9 into the w-rows against ry = 2e-9 —
while the nominal point itself is exact (|G| = 1.02e-12) and the
τ-component of K never failed (width 3.4e-14). Both attempts are
recorded: the frozen-box failure is preserved verbatim in
`second_fold_krawczyk_frozenbox.json` / `.log`; the certified run used
the RECORDED DEVIATION (pre-registration §7) of re-centering the τ-box
on the polished m=64 nominal with the same ± 1e-8 pad — the lower-fold
certificate's own structure. The radii ladder, the FD battery, the
certificate requirements, and the three-order agreement criterion were
all unchanged.

## The verdict (the owner's rule, applied verbatim)

> "If a second fold is found and certified, then the current model has
> two folds."

A second fold was found (Moore–Spence m=64/96/128, agreement 5.53e-7)
and certified (interval Krawczyk, unique MS zero, G' nonsingular,
nondegeneracy constants excluding zero). **The current Candidate-A
gated model has two folds**:

- the certified lower fold at \( \tau_f \approx 5.587236198690 \)
  (inherited certificate, untouched), and
- the certified upper fold at \( \tau_{f2} \approx 64.402327203369 \)
  (this campaign).

The upper basin boundary near 148.6–149.5 is now identified as a basin
boundary inside the (mathematically) bistable window
64.4023 < τ < 150.358, not as the stable family's birth: the stable
family is born at the second fold, but is generically unreachable until
the upper window. The fallback statement ("one certified lower fold
… upper basin boundary … unresolved") is superseded; what remains open
is listed below.

## Open items (honest register)

1. The past-turn stable arm beyond τ = 64.438 (its continuation to the
   face-cycle family; the 64.438–148.6 gap; whether it reaches the
   E~Emax face at all). Pre-registered budget stopped at 16 points.
2. The continuum off-grid residual stage and the RFDE lift — open for
   BOTH folds (unchanged scope statements).
3. The exact nature/location of the 148.6–149.5 capture onset as a
   basin boundary (history-dependent, per the campaign's asymmetry
   findings).
4. The m=64 discretization gap at the second fold (5.5e-7 vs the m=96/
   m=128 pair) — inside the frozen 1e-6 criterion, but ~5 orders larger
   than at the lower fold (2.7e-11); a higher-order certificate would
   need the m=96/128 MS systems certified (not pre-registered).
5. The P4 campaign's statement "no periodic-orbit family in the branch
   records on 5.6 < τ < 147.5" is revised by this campaign's records:
   the unstable upper arm exists on 64.4023 < τ < 150.358 (the finite
   basin-search monostability statement is unaffected — the arm is
   unstable and the stable arm has no generic basin there).

## Records inventory

| File | Content |
|---|---|
| `SECOND_FOLD_PREREGISTRATION.md` | the frozen plan (commit a3823c5) |
| `second_fold_search.py`, `second_fold_krawczyk.py` | the executed code (commit 363003b) |
| `second_fold_environment.json` | stage 0: versions, hashes, PAR/equivalence/seed/certificate checks |
| `second_fold_branch.csv` | 200 branch records (switch + 183 natural + 16 arclength) with per-point residual, Nyquist, step, Floquet multipliers |
| `second_fold_orbits.npz` | the converged orbit at every recorded τ |
| `second_fold_ms.npz` | the Moore–Spence solutions (z, ell) at m=64/96/128 |
| `second_fold_krawczyk.json` | the stage-C certificate (with the frozen-box attempt and the recorded deviation) |
| `second_fold_krawczyk_frozenbox.json` / `.log` | the preserved frozen-box failure record |
| `second_fold_basin.csv` | 45 basin runs (grids A and B + dt-halving) |
| `second_fold_status.json`, `second_fold_results.json` | the stage states and the assembled results |
| `second_fold_run.log`, `second_fold_krawczyk.log` | the full solver trails |
