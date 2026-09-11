Verification protocol for corrected_manuscript.tex

This directory extends this project’s existing integrity-checking
practice (/home/user/check_integrity.py, which guards against accidental
content pruning) with a second, complementary check that guards against
a different failure mode: mathematical/physical inconsistency introduced
when a later edit changes an assumption an earlier formula depended on,
without that earlier formula being re-derived.

Why this exists (root cause, not just a description)

An external audit and a subsequent internal root-cause investigation
(this session) found six confirmed correctness bugs in Sections 2–6 of
the manuscript (the general vector-accounting framework), all traceable
to one underlying pattern: a formula or symbol was correct at the moment
it was introduced, verified against the specific sub-problem it solved,
and then silently invalidated by a later addition elsewhere in the
manuscript that changed what correctness required — without the earlier
item being re-checked.

Critically, Sections 7–9 (the reduced 3-state and 4-state numeric cores)
underwent at least as many revisions and never accumulated this failure
mode. The reason: every claim there is verified by executing code
(direct substitution into the governing equations, plus RK4/DDE
simulation) before being asserted in prose — a discipline stated and
applied dozens of times throughout those sections. Sections 2–6, by
contrast, were historically verified only by prose argument, never by
execution — which is exactly how all six bugs entered, and exactly how
all six were found in this session (by writing and running symbolic
algebra scripts, not by re-reading prose).

verify_flux_ledger.py generalizes that ad hoc, one-off verification into
a permanent, re-runnable artifact, extending the executable-verification
discipline already governing Sections 7–9 to Sections 2–6.

Files

-   verify_flux_ledger.py — the permanent check. Symbolically re-derives
    the mass-conservation identity (dM_tot/dt = 0) from the current flux
    equations of Sections 2–6, and separately verifies the unified
    A^{act,eq} formula and the split chi_rec/chi_decay conservation
    constraints. If a future edit changes any flux term without updating
    its matching counterpart elsewhere, this script’s assertion fails
    immediately rather than silently shipping a new instance of the same
    bug pattern.
-   verify_macro_stability.py — confirms the
    fast-macroeconomic-subsystem Jacobian is not block-triangular (K, L,
    A_TFP couple through the shared output Q), but that the fast
    subsystem is nonetheless stable at its own fixed point, verified
    numerically across a sweep of the deficit-forcing term, replacing an
    earlier false structural claim with a checked numerical one.
-   verify_macro_scaling.py — confirms two further corrections found
    during the same root-cause sweep: (a) the savings rate varsigma must
    not be scaled by 1/epsilon in the Tikhonov boundary-layer analysis,
    since (unlike the other scaled rate constants) it is a bounded
    fraction in [0,1] and the old scaling drove it past that bound; the
    fix rescales capital’s whole equation of motion instead, leaving
    varsigma physical.
    (b) The saturated price transform tilde_p introduced to keep the
        economic deficit Delta^econ bounded must be used consistently
        everywhere Delta^econ is defined; an earlier revision introduced
        the fix in one place (sec:deficit-definitions) but left the
        original, unsaturated formula in Layer 2’s separate restatement
        of the same quantity.
-   verify_unified_ledger.py — verifies the algebraic/structural claims
    of the “Toward a Unified Core” section: the primitive-flux ledger’s
    structural immunity to double-compensation, the ell = -Xdot
    identity, forward invariance of both candidate unified-core effort
    laws, their closed-form equilibria, and the opposite sign-dependence
    of each law’s delay-coupling coefficient on equilibrium effort (the
    original sigma-gated proposal’s coupling weakens with effort; the
    repaired hybrid form’s strengthens with effort). The more expensive
    empirical search that confirms the consequence of the sigma-gated
    form’s weakening coupling (no Hopf-like crossing found for it across
    300+ randomized trials) is documented separately in
    upgrade5_search/CONSOLIDATED_FINDINGS.md and its accompanying
    scripts. Important caveat, corrected in a later session: the
    repaired hybrid form’s strengthening coupling does NOT by itself
    imply a local Hopf bifurcation exists — see
    verify_unified_characteristic.py below, which shows no local Hopf
    actually exists at the manuscript’s illustrative parameterisation
    despite this coupling strengthening; the large-amplitude cycle for
    the repaired form is a global attractor-birth/ fold-like event, not
    a Hopf crossing.
-   verify_unified_characteristic.py — derives and verifies, entirely
    independently (not by copying the manuscript’s claims), the exact
    4x4 linearized characteristic determinant of the repaired
    unified-core-v2 system and confirms it reduces to a closed-form
    quasi-polynomial
    Q(lambda) - K*lambda*(lambda+gamma_U)*exp(-lambda*tau) = 0. Verifies
    K > 0 for any interior equilibrium plus five limiting-case checks
    (q->0, eta->0, Delta_ref->infinity, E*->Emax, X*->0 all correctly
    send K->0), and the Hopf-locus modulus/argument identities. Central
    finding: at the manuscript’s own illustrative parameterisation,
    direct minimisation of the Hopf-modulus residual finds no root, and
    an argument-principle (winding-number) root count — first validated
    against the manuscript’s own published Candidate A thresholds —
    finds zero unstable roots for every delay in [0,500] years. Both
    methods agree: the interior equilibrium of unified core v2 is
    locally stable throughout this range, so the large-amplitude
    oscillation documented for it is a global attractor-birth/fold-like
    event, not a local Hopf bifurcation. This corrects an earlier
    manuscript claim (and an earlier version of this README) that
    described the same oscillation as a “genuine Hopf mechanism.”
-   verify_exact_cubic.py — verifies the new “Exact Algebraic Reduction”
    subsection (sec:exact-cubic) added to Section sec:hopf-verified for
    the three-state core. Confirms, entirely symbolically, that the 3x3
    characteristic determinant of Eq. char-eq-corrected factors exactly
    as P(lambda) - C_Z*L(lambda)*e^{-lambda*tau}, that the Hopf-modulus
    condition reduces exactly to a real cubic H(x), x=omega^2, and that
    H is a genuine cubic (hence has at most 3 real roots, certifying an
    upper bound on the number of distinct Hopf-frequency families for
    this system, algebraically rather than by search coverage). Solving
    this cubic independently (no eigenvalue root-tracking) exactly
    reproduces this manuscript’s own published tau_-, tau_+ thresholds
    for both Candidate A and Candidate B, finds no additional crossing
    below tau=300yr for either, and a sweep of eta across the full
    literature-anchored range [0.5,3.0] confirms the cubic always has
    exactly 0 or 2 positive roots — never 1 or 3 — certifying the
    two-Hopf-point picture used throughout this manuscript’s core
    analysis.
-   verify_abiotic_nonnegativity.py — verifies a real, previously
    unflagged non-negativity gap found in the general framework’s
    active- abiotic-pool equation (sec:abiotic, Eq. abiotic) and its
    fix. The original gross-uptake term B_i = R_i + kappa_A,i*N_i had a
    turnover component (kappa_A,i*N_i) that, unlike the co-located
    regeneration term R_i, did not vanish as A^act_i -> 0; direct
    simulation from an admissible initial condition (small A^act(0),
    undeveloped detritus pool) confirms this drives A^act strictly
    negative, not merely as a theoretical edge case. The fix multiplies
    the turnover term by the same donor-limiting factor A^act/(A^act+A0)
    already used by R_i (and applies the identical factor to the
    matching detritus source term, Eq. detritus, for mass-balance
    consistency); this script proves forward invariance of A^act >= 0
    symbolically, confirms the frozen-A limit is exactly unchanged,
    re-derives the manuscript’s own “Resolving D_ret” mass-conservation
    cancellation from scratch and confirms it still holds for any
    N, A^act (not only at N=K), and quantifies the resulting equilibrium
    shift for the four-state core’s Candidate A (N* shifts ~0.0008%,
    A^act* shifts ~2.9%) — explicitly flagging that this shift has not
    yet been propagated through that section’s downstream Hopf/SNPO
    numerical pipeline.
-   verify_general_feedback.py — verifies a unification (not a new
    variant) between two of this manuscript’s already-published local
    bifurcation results. Section sec:exact-cubic (three-state core) and
    Section sec:unified-characteristic (unified core v2) each derive a
    local characteristic equation independently, in different notation,
    from different governing equations. This script confirms both are
    exact special cases of one general feedback characteristic equation,
    lambda - C_E - C_Z*e^{-lambda*tau}*[-g*lambda*c^T(lambda*I-J)^{-1}*b_E]   /(1+tau_m*lambda) = 0,
    by re-deriving each manuscript equation from the general form
    directly (not copying either target equation’s own derivation
    steps): the three-state reduction (1D ecological block, gain g=1/2
    from the shifted softplus’s own derivative) reproduces
    char-eq-corrected exactly, verified both symbolically (zero
    residual) and numerically at both Candidate A and B parameter sets;
    the unified-core-v2 reduction (2D (X,U) ecological block, g=1 since
    ell=-Xdot needs no regularisation) reproduces unified-char-eq
    exactly, with the coupling constant K=-J_E*C_Z emerging
    automatically from the resolvent’s own structure. This is explicitly
    not a claim that either core is a parameter limit of the other — the
    adjacent “No reduction link” finding is unaffected and remains open
    — it is a unification of the two cores’ local bifurcation algebra:
    both cores’ Hopf onset is governed by the same ecological-resolvent
    / institutional-gain / delay-phase decomposition, differing only in
    which (J, b_E, c, g) each core supplies.
-   verify_proposition1_scalar_aggregation.py — verifies the
    constructive proof of Proposition 1 (Section
    sec:why-frameworks-fail, informally motivated by the “productivity
    illusion” narrative of Section sec:productivity-illusion-narrative):
    for any dimension n>=2, any fixed positive weight vector w, any
    target component k, and any threshold M>0, there exists a deficit
    vector b with b_k <= -M (an arbitrarily severe single-component
    deficit) while the scalar aggregate sigma(b) = w^T b > 0 (an
    arbitrarily positive aggregate reading), and symmetrically a b' with
    b'_k >= M while sigma(b') < 0. This shows no positively-weighted
    scalar index can ever certify componentwise sustainability, for any
    choice of weights — the “productivity illusion” is the generic
    behaviour of scalar aggregation, not a special or unlucky case. The
    script checks the two-point construction exactly via Python’s
    fractions.Fraction (no floating-point rounding) across 280
    (n, j, k, M) combinations with n up to 6 and M up to 1e12,
    stress-tests the sign pattern over 5,000 random floating-point
    instances with n up to 8, and separately confirms sigma(b) stays
    pinned at its target value while b_k is swept continuously across 9
    orders of magnitude toward -infinity. This is a
    foundational/motivational result, not a new dynamical finding — it
    formalises, as a citable boxed proposition, a claim the manuscript’s
    own prose already asserted informally.
-   regression_self_test.py — demonstrates that verify_flux_ledger.py’s
    checks are real regression guards, not tautologies: it substitutes
    the original, unfixed formulas back in and confirms the checks
    correctly fail against them.

Directory: upgrade5_search/

Contains the full, escalating-rigor numerical investigation that
established (a) the original sigma-gated unified-core proposal does not
exhibit a genuine delay-induced Hopf bifurcation across an extensive
randomized search, and (b) a repaired hybrid form does, confirmed via
direct nonlinear simulation. See
upgrade5_search/CONSOLIDATED_FINDINGS.md for the full write-up,
including the honest scope limitation that the repaired form’s precise
tau_- threshold has only been bracketed, not pinned down to the same
precision as Candidates A and B.

-   verify_new_effort_law_audit_proposal.py — evaluates (and REJECTS as
    a direct drop-in replacement) an external audit’s proposed
    alternative effort law
    Edot = eta*E*(1-E/Emax)*Z_tau/Delta_ref + delta0*(1-E/Emax) -   mu_E*E,
    offered as an improvement on eq:effort-core-corrected’s boundary
    behaviour. Confirms the audit’s boundary claim is TRUE (both E=0 and
    E=E_max point strictly inward, vs. the published law’s weakly-
    invariant E=E_max) and that E* remains a closed-form quadratic. But
    an extensive parameter search (joint grid + 3000-point random
    log-uniform search over eta, mu_E, E_max) finds no parameter
    combination giving both a comparable working equilibrium (N* in a
    plausible interior range) and a genuine Hopf bifurcation for any
    delay tau – i.e., adopting this law as literally proposed would
    silence the manuscript’s central delay-induced-instability
    mechanism. Root cause (verified symbolically): the new law’s
    baseline-panic term delta0*(1-E/Emax) has no Z_tau-dependence, so
    (unlike the published law) it contributes nothing to the
    institutional feedback gain C_Z, which then comes entirely from the
    eta term alone and is too weak at every stable working equilibrium
    tested. Reported as a permanent negative finding: the manuscript
    retains eq:effort-core-corrected rather than adopting this
    alternative.

-   verify_snpo_unstable_orbit.py — partial progress on this
    manuscript’s own flagged open question: “the existence of the
    intervening unstable periodic orbit that a true SNPO requires … has
    not been independently confirmed” (Section
    sec:numerical-continuation-corrected). Re-uses a pre-computed
    Fourier spectral-collocation periodic-orbit continuation branch
    (unstable_branch_up_ckpt.npz, effort-saturation- corrected core,
    Candidate A) already in this project’s history. At tau=3.700 (just
    above tau_-=3.666), the converged orbit (collocation residual ~1e-7,
    i.e. an essentially exact solution) is confirmed unstable by direct
    long-horizon (2-3 million simulated years) forward integration from
    its own state with no added perturbation: floating-point roundoff
    alone eventually displaces the trajectory onto the large-amplitude
    cycle (amplitude ~55.8, matching the coexisting stable orbit’s own
    amplitude at that tau), confirming the orbit sits exactly on the
    basin boundary — the defining signature of a genuine unstable
    periodic orbit. Confirmed dt-independent (0.01, 0.02, 0.04) and
    confirmed not to occur at nearby tau values further from the Hopf
    point (3.92, 4.11, 4.59, 4.91) within the same horizon, ruling out a
    generic simulation-instability artifact. Honest scope: this is a
    real, verified partial answer — it does not establish that the
    orbit’s amplitude vanishes as tau -> tau_- (checked directly; it
    does not shrink to zero in the range tested, itself an open puzzle,
    not a confirmed textbook Hopf-emanating picture), and does not
    establish the SNPO collision itself (a continuous meeting of this
    unstable branch with the stable branch at tau_SNPO,L or tau_SNPO,R
    with sqrt(tau-tau_SNPO) scaling) — that remains future work. A
    direct Floquet-multiplier computation via monodromy-matrix
    propagation (floquet_corrected.py, already in this project) was
    attempted on this orbit but did not cleanly resolve the
    theoretically-required trivial +1 multiplier at the discretisation
    resolutions tested; recorded as attempted-but-inconclusive, not
    suppressed.

-   verify_snpo_fold_refinement.py — extends
    verify_snpo_unstable_orbit.py with two further, genuinely new pieces
    of evidence for the effort-saturation-corrected core (Candidate
    A). (1) Refined fold location: direct 10^6-simulated-year bisection
    of the stable large-amplitude orbit’s own persistence refines
    tau_SNPO,L to [5.56999, 5.57001] (5 significant figures) — distinct
    from the previously reported 5.63-5.64 (obtained from a
    shorter-horizon search).

    (2) A verified negative result narrowing the SNPO-partner search:
        continuing the small-amplitude unstable orbit (confirmed
        genuinely unstable in verify_snpo_unstable_orbit.py) via
        Newton-corrected Fourier collocation from tau=3.700 through
        tau=5.700 (past the refined fold) shows its amplitude varies
        smoothly by less than 0.1 total and never approaches the stable
        branch’s own amplitude (25.4372 immediately before the fold) —
        ruling out that specific orbit as the colliding SNPO partner at
        tau_SNPO,L. A second, independently-converged unstable orbit
        (amplitude ~13-17) is confirmed to exist nearby and is confirmed
        unstable by the same roundoff-escape method, but has not yet
        been continuously tracked to the fold to test whether it is the
        true SNPO partner — flagged as the concrete next step, not
        claimed here.

    CORRECTION (see verify_snpo_fold_correction.py below): Check (2)’s
    claim above — that the small orbit’s amplitude “varies smoothly by
    less than 0.1 total” and stays near its Hopf-point value — is FALSE.
    It was contradicted by the project’s own previously-saved
    continuation checkpoint (unstable_clean_ckpt.npz, already in the
    workspace at the time this false claim was written) and by an
    independent, from-scratch re-continuation. This script
    (verify_snpo_fold_refinement.py) and its retracted Check 2 are kept
    unmodified in the repository as a transparent record of the error;
    do not treat its amplitude-range claim as valid. Check (1) (the
    refined tau_SNPO,L=[5.56999,5.57001] persistence-loss boundary) and
    Check (3) (existence of the second unstable orbit) are unaffected
    and remain valid.

-   verify_snpo_fold_correction.py — corrects the false claim above and
    reports a newly-found genuine fold. Four checks, all executed live
    (no hardcoded/cached amplitude tables): (1) the project’s own saved
    checkpoint already contradicts the old flat-amplitude claim, growing
    from 1.05 (tau=3.700) to 17.42 (tau=5.679); (2) a fresh from-scratch
    M=257 natural-parameter continuation (Newton/Levenberg-Marquardt,
    residual <1e-9 throughout) reproduces and extends this growth to
    amp=15.0 at tau=5.40; (3) an independent M=129 (half-resolution)
    continuation confirms the same growth trend, ruling out an
    M=257-specific artifact; (4) pseudo-arclength continuation (treating
    tau as a free unknown) pushes through the point where
    natural-parameter continuation stalls and finds a genuine fold: tau
    reaches a local maximum of 5.468331 (amplitude ~19.57) and then
    decreases as the branch is followed further — the defining
    topological signature of a saddle-node of periodic orbits, not a
    numerical stall. Continuing past this turning point, direct forward
    simulation from several points on the post-fold branch settles
    (within 3-6 periods) onto amplitudes matching independently-computed
    points on the known large-amplitude stable cycle to 4+ significant
    figures (e.g. 54.5625 at tau=3.89), consistent with — though not a
    formal Floquet-multiplier proof of — this being the genuine SNPO
    collision. Honestly-reported open discrepancy: this fold’s location
    (tau=5.468331) does not exactly coincide with the
    independently-reproducible persistence-loss boundary
    (tau_SNPO,L=[5.56999,5.57001]) from Check (1) of
    verify_snpo_fold_refinement.py above (itself re-confirmed and still
    valid). A reconciliation attempt (continuing a separately-seeded,
    generic-initial-condition orbit down from tau=5.50) produced a
    third, only loosely-converged amplitude value at tau=5.40 matching
    neither branch — flagged as a genuine, unresolved puzzle (possible
    multiple coexisting large-amplitude branches, or
    critical-slowing-down bias in the finite-horizon persistence
    bisection) rather than smoothed over. A crude perturbation-based
    Floquet proxy was attempted and found unreliable (it reported
    “unstable” even for a known-stable control orbit), so it is reported
    as attempted-but-inconclusive and not used to support any stability
    claim in the manuscript.

-   verify_hybrid_effort_law.py — follows up on the rejection in
    verify_new_effort_law_audit_proposal.py with a genuine repair,
    additive to (not a replacement for) eq:effort-core-corrected: adding
    a single term -mu_E*E outside the existing (1-E/E_max)-gated bracket
    (rather than restructuring the bracket itself, as the rejected
    proposal did) makes the E=E_max boundary strictly inward while
    leaving the bracket — and therefore the delay-dependent
    institutional gain C_Z the rejected law lost — completely untouched.
    Confirmed symbolically (dC_Z/d(delta_0) != 0, the exact root-cause
    fix) and by direct nonlinear DDE simulation: a genuine Hopf pair
    (tau_-, tau_+) persists at both Candidate A and Candidate B, at an
    equilibrium within 0.005 of the already-published one for each
    candidate, with E(t) confirmed to stay strictly within [0, E_max]
    throughout the large-amplitude cycle at every tau tested. This is an
    additive, further-improved variant — the new parameter mu_E has no
    independent empirical calibration, and the full fold/SNPO analysis
    has not been repeated for it — offered alongside, not replacing,
    eq:effort-core-corrected.

When to run this

When to run this

When to run this

When to run this

Run python3 verify_flux_ledger.py before and after any edit to the flux
equations of Sections 2–6 (natural capital, product, waste, inert,
active-abiotic-pool, geological-reservoir, or detritus dynamics), in the
same way check_integrity.py is already run before/after any edit to the
manuscript generally. Report its pass/fail result alongside the edit.

If a future revision adds a new compartment or flux term, add the
corresponding row to build_ledger() in verify_flux_ledger.py and confirm
the ledger still balances to zero before adding that term to the
manuscript itself — do not add a new flux to the paper without a
corresponding update here.

Relationship to check_integrity.py

  --------------------------------------------------------------------------
                          check_integrity.py      verify_flux_ledger.py
  ----------------------- ----------------------- --------------------------
  Guards against          Accidental              Mathematical/physical
                          deletion/pruning of     inconsistency from
                          content                 uncoordinated accretion

  Method                  Structural fingerprint  Symbolic re-derivation of
                          diff (labels, refs,     conservation/equilibrium
                          cites, equations)       identities from current
                          against a baseline      equations

  Scope                   Whole manuscript        Sections 2–6 (general
                                                  vector framework)
                                                  specifically
  --------------------------------------------------------------------------

Both should be treated as required, not optional, steps in this
project’s editing workflow.

-   verify_corrected_core_folds.py — independent from-scratch re-verification
    (numba RK4-DDE written directly from Eqs. stock-core / Z-core /
    effort-core-corrected, validated by reproducing tau_- = 3.666 and
    tau_+ ~ 150.36 from the exact linearized characteristic equation, the
    lower fold to <0.1% ([5.5738,5.5756] vs the published
    [5.56999,5.57001], amplitude 24.9 vs 25.4372), and the original ungated
    core's upper fold ~131.24) of the corrected core's global fold
    structure, with two corrections and one quantification:
      (1) UPPER FOLD CORRECTED: no large-amplitude attractor at
          tau in [64.39,140] (8 ICs, 6e5-yr horizons); upper fold at
          tau_SNPO,R in [148.125,148.438], i.e. a narrow upper bistable
          window (~148.3,150.36), not the previously reported 86-yr window
          (64.39,150.36). The old value is traced to a finite-horizon
          ghost-transient artifact: far-from-equilibrium trajectories in the
          monostable interior oscillate with near-cycle amplitude for
          ~1e4-1e5 yr before collapsing, so a 6e4-yr persistence protocol
          reports "cycle" on BOTH sides of the claimed 64.38994/64.39004
          bracket.
      (2) k-SENSITIVITY QUANTIFIED: with delta fixed, the equilibrium and
          local Hopf thresholds are exactly k-independent
          (softplus'_k(0)=1/2), but the global fold is strongly
          k-dependent: lower fold ~5.0 (k=5), 5.574 (k=10), and no
          stable-cycle/equilibrium coexistence above tau_- (k=20).
      (3) CANDIDATE B FOLDS CORRECTED: the lower Hopf is supercritical
          (cycle amplitude -> 0 as tau -> tau_-, no lower fold or bistable
          window; the earlier tau_SNPO,L~6.15-6.18 was this small cycle),
          and the upper fold is tau_SNPO,R in [76.0725,76.077], just below
          tau_+ = 76.29 (narrow bistable window), not 76.60 (which lay
          above tau_+). All six checks pass (exit 0).

CROSS-CONFIRMATION ADDENDUM (after the project's original stack was restored to the
workspace): the upper-fold correction in verify_corrected_core_folds.py is now
confirmed by the project's OWN simulation code (corrected_core_common.simulate,
an entirely separate implementation from the script's from-scratch RK4). Running
corrected_core_common.simulate at 1.2e5-yr horizons gives: tau=64.39/100/140/146
-> collapse to the equilibrium (tail amplitude 0), tau=148.4/150 -> persistent
large-amplitude cycle (tail amplitude 55.5/42.9). Two independent implementations
therefore agree that the corrected core's upper fold is ~148.3 (bracket
[148.125,148.438]), NOT the manuscript's previously reported 64.39. Additionally,
verify_snpo_fold_correction.py (the project's own script) passes all 4 checks with
the restored unstable_clean_ckpt.npz (exit 0): the unstable branch grows 1.05 ->
17.4 (tau 3.7 -> 5.68) and PALC finds the fold at tau=5.46833. The checkpoint's
branch extends to tau=118.5 (amplitude ~8), consistent with the unstable orbit
persisting through the monostable window without creating bistability.
Also verified with the restored stack: the tau=115 yr "bistable window" figure
captions (Sec. two-channel) were wrong - tau=115 lies in the monostable safe
range of the original ungated core (7.36,131.24); a 4e5-yr run from far-from-
equilibrium collapses within ~50 kyr (tail amplitude 0), matching the ghost-
transient class documented above. Captions corrected to describe the excursion
as a long-lived transient.

-   verify_hopf_nature.py — determines the nature of the corrected core's two
    Hopf bifurcation points (Candidate A) and the periodicity of its
    upper-window large-amplitude attractor. Checks (all pass, exit 0):
      (1) sigma(tau) = Re(lambda_rightmost) is linear near tau_- with
          dsigma/dtau = -9.4e-5 yr^-2 (equilibrium stable above tau_-);
      (2) first Lyapunov coefficient at tau_-: branch amplitude scales as
          a^2 ~ kappa*(tau-tau_-), kappa~24, fitted exponent 0.47 (Hopf: 1/2);
          l1 = -(dsigma/dtau)/kappa = +3.9e-6 (peak-to-peak N convention;
          +1.6e-5 half-amplitude). l1 > 0: SUBCRITICAL.
      (3) tau_+ = 150.36 (sigma crosses zero), dsigma/dtau = +5.5e-6 yr^-2
          (destabilisation ~17x slower than at tau_-: severe critical slowing
          down near tau_+);
      (4) dynamical tests: near-equilibrium histories below tau_- and above
          tau_+ grow without intermediate saturation to the LARGE cycle
          (amplitude ~57 and ~43 respectively) — no small stable cycle exists
          on either unstable side;
      (5) Poincare sections at tau = 148.4, 150, 152: settled section spread
          < 5e-4 and decreasing with dt (5.5e-4 @0.1, 1.5e-4 @0.05, 2.4e-5
          @0.02) — the upper-window attractor is a PERIOD-1 limit cycle, not
          a torus (a torus would show a finite dt-independent spread); the
          power spectrum shows the fundamental (period ~157 yr) plus its
          second harmonic only. Partially resolves, for the corrected core,
          the manuscript's flagged periodicity question.
      (6) Floquet multipliers of the small orbit at tau=3.7 via
          segment-discretized monodromy (dim 225): max |multiplier| = 1.00075
          > 1 (unstable), consistent with exp(-2 sigma T) = 1.00160 from the
          normal form; the trivial +1 and the radial mode are too close to
          separate at this discretization (reported honestly).
    Both Hopf points are subcritical, consistent with the bistable windows and
    SNPO-fold topology reported in the manuscript.

    ADDENDUM (ungated core): check 7 establishes that the UNGATED core's
    upper-window large-amplitude attractor at tau=131.8 is a period-1 limit
    cycle: the N-envelope (successive maxima) is constant to <=0.001 (dt=0.02)
    and <=0.004 (dt=0.01) over 1.5-2e6-yr records, and the power spectrum is
    harmonic-only (fundamental ~135.6 yr). This does NOT reproduce the ~0.08
    amplitude modulation previously reported for this attractor from an
    adaptive-tolerance integrator; the discrepancy is reported honestly in the
    manuscript and treated as unresolved pending replication of that integrator.

-   verify_ungated_floquet.py — resolves two open items for the UNGATED core
    (Candidate A). (1) Floquet multipliers via shooting fixed-point + FD
    Jacobian of the discrete segment map: the tau=131.8 upper-window
    attractor is a STABLE period-1 limit cycle (all multipliers < 1; phase
    recovered ~0.99; no second unit-circle multiplier -> NOT a torus), and
    the small unstable orbit at tau=7.1 has dominant multiplier ~1.018 > 1
    (normal form exp(-2 sigma T) ~ 1.012) — the subcritical SNPO partner.
    (2) A correct method-of-steps adaptive RK45 (scipy solve_ivp, rtol=1e-9)
    at tau=131.8 gives an N-envelope flat to ~0.005 over 2e4 yr, so the
    earlier ~0.08 amplitude modulation (from an adaptive-tolerance
    integrator) is NOT reproduced by fixed-step RK4, by adaptive RK45, or by
    the Floquet spectrum — it is an integrator artifact; the attractor is a
    stable limit cycle. All three checks pass (exit 0).

    CORRECTION ADDENDUM (corrected-core small orbit): the earlier Floquet
    attempt on the corrected-core small orbit at tau=3.7 (segment-discretized
    monodromy, max|mult| = 1.00075, reported inconclusive) is superseded by a
    validated shooting/FD computation (corrected_shooting.py): the orbit from
    unstable_clean_ckpt.npz is advanced by the exact-floor discrete RK4 map,
    and the central-difference Jacobian's eigenvalues give a radial multiplier
    converging monotonically to exp(-2 sigma T) = 1.0016 (1.0008, 1.0011,
    1.0013 at dt=0.05, 0.025, 0.0125) with the phase multiplier converging to
    1 (0.998, 0.999, 1.000). The orbit is UNSTABLE -- the subcritical SNPO
    partner -- resolving the previously-inconclusive note.

-   verify_fourstate_pipeline.py — recomputes the four-state core's full
    numerical pipeline at the DONOR-LIMITED equilibrium (manuscript item
    #17, previously flagged as not propagated). Validates the pre-correction
    values exactly (OLD equilibrium to 1e-12; tau=0 eigenvalues to 8
    significant figures; tau_- = 6.985285 and tau_+ = 132.268712 to 6
    significant figures; kappa_A threshold 0.0038945 to 1e-8), then reports
    the recomputed values: Candidate A tau_- = 6.982022 (-0.05%),
    tau_+ = 132.272044 (+0.003%), SNPO_L ~ 7.374, SNPO_R ~ 130.77 (the
    manuscript's 118.900 is a ghost-transient artifact — no cycle at
    tau in [118.9,130] at any horizon to 1.5e6 yr; carry-continuation places
    the true fold in [130.770,130.771]), kappa_A threshold 0.0013163 (-66%);
    Candidate B tau_- = 6.25115, tau_+ = 99.79060, supercritical lower Hopf
    (no lower fold), SNPO_R ~ 76.98 (ordering SNPO_R < tau_+ holds with a
    ~23 yr gap, not 10.2). All 7 checks pass (exit 0).

-   verify_branch_structure.py — maps the corrected core's lower-fold branch
    structure and tests the sqrt(tau-tau_SNPO) collision scaling an SNPO
    requires. Findings (all checks pass): (1) the earlier-reported "genuine
    fold at tau=5.468331 (amp 19.57)" is a floor-smoothing artifact of the
    collocation's soft_floor(200); with an essentially-exact floor (sharpness
    10000) the small-unstable branch is monotone through tau=5.468 and folds
    at tau~5.587 (amp ~21.7). (2) The stable large-amplitude cycle terminates
    at tau~5.574-5.575 (amp ~25.0; collocation at 5.574, 12-Myr simulation at
    5.576 collapses). (3) The two folds are DISTINCT (stable ~5.575 amp 25 vs
    small-unstable ~5.587 amp 21.7); at the stable branch's end the small
    orbit has amp ~20.5, so it does NOT collide with the stable cycle — it is
    not the SNPO partner. (4) Honest negative: the sqrt(tau-tau_SNPO)
    collision scaling of a single SNPO is not cleanly demonstrable (a forced
    gap-fit gives exponent ~0.46, but the two arms terminate at different
    tau, so no single fold gives a clean sqrt law). The lower boundary is a
    tight cluster of two nearby folds, not a single confirmed SNPO.

    FOLD-SIGNATURE ADDENDUM (resolves the two open branch-structure items):
    verify_branch_folds.py documents the Floquet-multiplier signatures that
    resolve Q1 and Q2 from verify_branch_structure.py. (1) The small-unstable
    branch GENUINELY folds at tau~5.587: shooting Floquet of the
    collocation-converged orbit gives a real multiplier 1.0514 at tau=5.584
    decreasing to 0.998983 at tau=5.587 -- a real multiplier crossing +1, the
    defining fold-of-periodic-orbits signature. (2) The stable large-amplitude
    branch GENUINELY folds at tau~5.574-5.575, not a hard end: its dominant
    complex Floquet pair has modulus 0.947, 0.957, 0.967 at tau=5.555, 5.565,
    5.574 with Re->1 and Im->0 as tau->5.575 (coalescing at +1). (3) The two
    folds are DISTINCT events of different periodic-orbit families (periods
    ~322.9 vs ~314.3 yr at their respective folds), so the lower boundary is a
    tight pair of individually-genuine folds, and the single-SNPO
    sqrt(tau-tau_SNPO) collision scaling is not applicable. (4) The earlier
    "fold at 5.468331" is corrected to a continuation artifact: the Z-floor is
    INACTIVE on both branches (the baseline shift delta=ln2/k makes the floored
    quantity the softplus itself, nonnegative identically), so floor sharpness
    cannot be the cause.

GAP-CLOSURE ADDENDUM (numerical gaps closed in this round):
- verify_kappaA_sweep.py: four-state kappa_A gap. Validates tau=0 eigenvalues
  and Hopf pair at kappa_A=0.05 exactly; continuous tau=0 stability sweep over
  [0,0.5] (1798 physical-branch equilibria) with the unique stability threshold
  bisected to kappa_A=0.001316298 (manuscript ~0.0013163); below-threshold
  delay-independent stability verified on a 10 x 6 (kappa_A, tau) grid by
  direct simulation (0 unstable); continuous Hopf loci over [0.0014,0.5]
  (tau_-: 17.5->6.9 yr, tau_+: 280->132.4 yr); plus high-delay crossings
  beyond tau_+ (270.2, 274.5, 416.6, ... yr) with the marginal-crossing note.
- verify_fourstate_fold_tracking.py: continuous fold tracking vs kappa_A.
  Both folds tracked at 19 kappa_A points in [0.0015,0.5] (multi-seed
  carry-continuation bisection, 8e5-yr horizons): SNPO,L 11.4->7.3 yr,
  SNPO,R 148.5->130.8-131.1 yr, windows collapse at the threshold.
- verify_hybrid_folds.py: hybrid effort law (Eq. effort-core-hybrid) fold/Hopf
  analysis. E*=2.086113 (A), tau_-=3.5953 (A) / 5.5085 (B); lower fold
  SNPO,L~5.53, upper fold SNPO,R~143.5, quiet middle; equilibrium locally
  stable throughout tau_-<tau<tau_+ by the characteristic-equation root count.
  Basin caveat: near the upper fold the large cycle's basin extends into the
  nominal safe range for histories with Z0~delta or N0>K (also true of the
  corrected core).
- verify_unified_eta_sweep.py: unified core v2 eta sweep over (2.337,3.0].
  Reproduces eta=10 (17.568, 18.362) and eta=2.5's multi-crossing (0.6, 54.2,
  92.9, 113.1); reveals TWO local-Hopf pairs (large-delay pair born at
  eta_crit~2.337 at tau~71; small-delay pair born at eta~2.454 with tau_->0);
  the local-Hopf regime does not connect continuously to the baseline's
  global-fold regime (tau~33.4-33.6).
- verify_fourstate_sensitivity.py: omega_A / A0 / A^{act,eq,intrinsic} sweeps
  over their full literature ranges. Thresholds shift only mildly
  (tau_- in [6.89,7.42], tau_+ in [131.8,132.4], folds within [7.3,7.65] and
  [130.3,131.1] yr); tau=0 stable throughout.
