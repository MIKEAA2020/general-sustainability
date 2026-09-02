# P4 five-regime continuation campaign — pre-registered plan (frozen 2026-09-03, before any run)

**Status.** This plan is the pre-registration for the recomputation of the
P4 five-regime attractor/basin topology of the gated three-state DDE
(M3-B, Candidate A). It was written and dated before any run of the campaign
was executed, following the discipline of
`stage_reconstruction_preregistration.md` (2026-09-01). Parameter values,
the tested delay grid, the history classes, the acceptance criteria, and the
comparison criteria below are frozen; code bugs may be fixed freely at
execution time, but no parameter or criterion may be changed after the first
complete run without recording the change as a deviation. No part of the
campaign has been executed as of this date.

**Why a recomputation.** The original five-regime records are not in the
repository — this is the definitive negative of the wave-7 registry (full
GitHub tree scan AND full-history filename scan: no five-regime
attractor/basin record, present or historical; provenance-corrected to the
original A018 authoring, commits `6ef8299`/`68f4eee`). The corpus's own
fold-status discipline names the missing objects as *the publication-artifact
archives (branch, Floquet, history, solver, and environment artifacts)* and
*the sampled-numerics documentation action* — a declared-open obligation of
the original authoring. Writing code that claims to reproduce the original
objects without a pre-registered plan would carry the fabrication risk the
registry already records; this plan therefore declares a **new, fully
documented campaign** whose output will be the first committed five-regime
record of any kind. A match with the inherited numbers is a consistency
statement for them, not a validation; a mismatch is reported as such and
adjudicates nothing about numbers whose generating objects remain
unavailable.

**Independence discipline.** (1) The declared object is the committed model
file, unchanged: `research_program/validated_computations/a025_fold/
a025_model.py` (gated three-state (N, Z, E) DDE, Candidate A, the `PAR`
dict). No parameter is chosen with reference to the legacy topology. (2) The
methods are the committed pipeline's own (Fourier collocation, Hopf branch
switching, natural-parameter and pseudo-arclength continuation, Moore–Spence
fold solves, variational Floquet tracking, method-of-steps RK4 with a
circular delay buffer) — the same machinery already certified for the
small-branch fold. (3) No boundary or criterion below may be adjusted to
make a legacy number appear. (4) The comparison criteria are fixed in §5,
before the run.

**Already-certified inputs this campaign inherits (not recomputed).** The
Hopf pair is interval-certified on the repo (tau- in
[3.6661490142739, 3.6661490142743] yr, tau+ in
[150.3584773101408, 150.3584773101421] yr; `a025_interval_hopf.json`), and
the small-branch fold is now interval-certified by the committed
`a025_fold_krawczyk.py` (2026-09-03): unique Moore–Spence zero with
tau_f in [5.587236198689, 5.587236198691] yr inside the lost-artifact box
[5.587236197890, 5.587236199490], G' nonsingular throughout (simple
nondegenerate fold of the m=64 collocation system), and both
nondegeneracy constants excluding zero (psi^T F_tau in
[0.313266, 0.314822]; psi^T D2F[v,v] in [5.6923e-5, 5.8943e-5]). These are
cited as fixed inputs; the campaign does not recompute them.

---

## 1. The declared object (committed, unchanged)

The gated effort-saturation-corrected three-state DDE of a single binding
resource at Candidate A, exactly as committed in
`research_program/validated_computations/a025_fold/a025_model.py`
(N' = rN(1-N/K) - qEN; Z' = (mem(N,E) - Z)/tau_m with the softplus deficit
memory; E' = (1-E/Emax)(eta E (Z(t-tau)/Dref - E/Emax) + delta0 Z(t-tau)/
(Zref + Z(t-tau))); PAR as committed: r=0.02, K=100, q=0.001, eta=0.914,
Emax=30, delta0=0.01, Dref=1, taum=5, k=10, delta=ln2/10, Zref=1). The
admissible domain is the declared one: N >= 0, Z >= 0, 0 <= E <= Emax, with
the E = Emax face invariant. The analysis parameter is the institutional
delay tau in the declared fundamental range 0 < tau <= 160 yr (before the
first recurrent branch of the lower frequency family, ~253 yr).

## 2. Records to be computed (the publication-artifact archives)

1. **Branch archive (CSV per family).** Fourier collocation (m = 64 primary,
   96/128 resolution cross-checks) with the committed pipeline discipline
   (Nyquist-projected Hopf branch switch; unprojected continuation with the
   declared stall-acceptance criterion; checkerboard rejection by relative
   Nyquist content < 1%):
   - the equilibrium Hopf small branch from tau- to its fold and, where the
     budget allows, along [130, 150.30];
   - the large-amplitude cycle family over the lower termination region
     (tau in [1, 6]) and the upper region (tau in [147.5, 160]);
   - a pseudo-arclength pass through each turn where natural-parameter
     continuation fails (the committed failure mode near the folds).
   Per point: tau, period T, N peak-to-peak amplitude, Z and E extrema,
   collocation residual, continuation budget used.
2. **Floquet archive (columns of the branch CSVs).** Variational collocation
   Floquet tracking along every branch record: the dominant multiplier
   (modulus and real/imaginary parts) at every continuation point, with the
   real-crossing signature explicit (imaginary part reported; the +1
   crossing bracketed to <= 1e-3 yr in tau where it occurs).
3. **History/basin archive (CSV).** Method-of-steps RK4 (circular delay
   buffer, dt = 0.02 yr, horizon 4x10^4 yr, tail = last 1800 yr — the
   A018-declared conventions) at the fixed tau-grid of §3 with the three
   fixed history classes:
   - H1 large stock / low effort: N(t)=90 for t <= 0, Z(t)=Z* (equilibrium),
     E(0)=0.5 E*;
   - H2 depleted: N(t)=5 for t <= 0, Z(t)=Z*, E(0)=0.5 Emax;
   - H3 near-equilibrium: N(t)=N*, Z(t)=Z*, E(0)=E*, histories perturbed by
     +1% on all components.
   Per run: tau, history class, classification (captured by cycle / settles
   to equilibrium / other), tail N-extremes, tail relative standard
   deviation, max E, gate-floor activity flag (max(0,.) binding anywhere).
4. **Solver archive (log).** The per-run console and gate log: residual
   floors, stall acceptances, failed seeds, continuation step sequences —
   the documentation action the paper names.
5. **Environment archive (JSON).** Python/numpy/mpmath versions, machine,
   date, committed-code file hashes, random seeds (none used; the campaign
   is deterministic).

## 3. The fixed tau-grid for the basin archive

tau in {1.0, 3.0, 3.5, 3.65, 3.68, 4.0, 5.0, 5.5, 5.573, 5.575, 5.577, 5.6,
6.0, 8.0, 20.0, 50.0, 100.0, 130.0, 147.0, 148.0, 148.3, 148.6, 149.5,
150.0, 150.4, 151.0, 155.0} (27 values x 3 history classes = 81 runs).
Boundary-adjacent values are dense at the two lower boundaries (5.574-5.576
legacy bracket; 5.587 fold) and the upper bracket [148.125, 148.438].

## 4. Acceptance criteria (fixed before the run)

- Collocation branch records: residual <= 1e-11 inf-norm, or the declared
  stall-acceptance level (3e-9) recorded per point; m=64 primary with the
  m=96/128 cross-check required at every fold location (the three orders
  must agree in tau to <= 1e-6).
- Fold events: each reported fold is either (a) interval-certified by the
  committed `a025_fold_krawczyk.py` (the small-branch fold already is), or
  (b) located by nominal Moore-Spence solves at all three orders with the
  classification stated as provisional.
- Multiplier crossings: the +1 crossing of the dominant real multiplier
  bracketed to <= 1e-3 yr; a complex-pair crossing, if found, reported as
  such (it would contradict the legacy real-multiplier reading and be
  reported as a MISMATCH, not suppressed).
- Basin runs: dt-halving check at two grid points (5.575, 148.3) requiring
  unchanged classification; classification thresholds: captured = tail
  relative standard deviation of N >= 2%; settles = < 0.1%; intermediate
  reported as its own class.
- The five-regime boundary table is produced only from these records, with
  every boundary a bracket (never a point), and the interior monostability
  statement reported as the finite-search result it is.

## 5. Comparison criteria against the inherited A018 §6 rows (fixed)

Legacy values (paper4 v9 §9.2 / A018 §6 rows): lower basin-collapse bracket
[5.574, 5.576]; small-branch fold ~5.587 (multiplier 1.0514 at 5.584 ->
0.99898 at 5.587); large-branch multiplier track 0.240 (tau=4.0) -> 0.964
(tau=5.5815); two families distinct at the lower boundary (amplitudes ~25
vs ~21.7; periods ~322.9 vs ~314.3 yr); upper boundary bracket [148.125,
148.438] with the small branch on [130, 150.30] (amplitude 0.11-1.87) and
the interior large family on [147.5, 160] (amplitude 15.9-19.5) distinct
there; five-regime classification with the H1/H2 basin-capture asymmetry
(large-stock captured, depleted not) inside the bistable windows.

A criterion MATCHES if: the campaign's bracket overlaps the legacy bracket
(boundaries); the multiplier track agrees within 0.02 absolute; amplitudes
and periods agree within 15%; the family-separation statement agrees
(amplitude gap >= 2 and period gap >= 5 yr at the lower boundary); the
basin classification agrees at every shared grid point. The verdict is
reported per criterion as MATCH / MISMATCH / NOT-TESTED, once, with no
re-run after the parameters are frozen. Interior monostability and the
upper-boundary fold type are NOT match criteria (the legacy itself declares
them open).

## 6. Figure-ungating rule (fixed)

The P4 topology figure (judged MERITED but data-gated by the visual-aids
assessment) may be drawn ONLY from this campaign's committed branch and
basin CSVs, with every displayed feature traceable to a committed record.
Until the campaign is executed and its records committed, the figure stays
gated. No legacy number may be drawn.

## 7. Provenance statement (to be printed with the results)

"The original five-regime records are not in the repository (registry
verified negative, 2026-09). The records below are the output of the
pre-registered campaign of 2026-09-03: the committed gated three-state
model continued, tracked, and basin-tested by the committed pipeline
machinery, with all parameters, grids, criteria, and comparison rules fixed
before the run. The inherited A018 §6 numbers keep their exploratory status;
a match is a consistency statement for the inherited record, and a mismatch
adjudicates nothing about numbers whose generating objects remain
unavailable. The small-branch fold and the Hopf pair are interval-certified
inputs; all other records are nominal with the declared acceptance
criteria."

## 8. Scope limits (fixed)

- The campaign produces records for the DISCRETIZED continuations and
  finite-horizon simulations; only the already-certified pieces (Hopf pair,
  small-branch fold) carry interval certificates. No new interval
  certificates are promised by this plan.
- The upper-boundary fold type (saddle-node vs other) is not classified by
  this campaign unless the multiplier track resolves it; the provisional
  status stands otherwise.
- Nothing here touches the gated four-state working core, Candidate B, the
  MPF core, or the sampled-governance paper's objects.
- Execution is a separate future task; this document is the frozen plan.
