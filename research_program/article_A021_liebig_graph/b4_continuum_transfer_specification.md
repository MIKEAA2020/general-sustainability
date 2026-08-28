# B4 Continuum-Transfer Specification — from discrete product bunching to a certified continuum NAIM persistence statement

**Status: SPECIFIED (2026-08-27). No transfer computation is executed by this document.** This is the evaluated execution plan for the B4 continuum transfer, written after the A1 gate closed (Stage 4d: a true periodic solution of the C4 DDE certified within 3e-7) — the event that unlocks the transfer (`batch 2/04_open_problems/OPEN_PROBLEMS_REGISTER.md` B4: "COMPUTED_PARTIAL (discrete only; continuum transfer gated on A1)"). It follows the campaign discipline of the A1 stages: the specification is grounded in already-measured constants; every required machinery element is mapped to its existing, verified implementation; the feasibility margins are computed from the discrete evidence before any stage is executed.

## 1. The object and the gap

The Paper 4 NAIM persistence capstone rests on the generic two-block periodic persistence theorem (`generic_two_block_periodic_persistence_theorem.md`), whose hypothesis **H3 (invariant linear splitting and bunching)** requires, at the continuum level, the product stable-norm inequality

\[
q_n \;=\; M_c \cdot \max\bigl\{\,\|S_x^n\|,\;\|T_y(nP_x)\|\,\bigr\} \;<\; 1 ,
\]

where (C4 scaffold, `product_prefactor_bunching_assessment.md`):

- \(S_x^n\) — the stable-complement evolution of the **binding block** (the gated C4 binding cycle, \(\tau_x = 4.5\)), phase direction removed, history sup-norm;
- \(T_y(nP_x)\) — the semigroup of the **slack block** (the C4 slack equilibrium, \(\tau_y = 10\)), history sup-norm;
- \(M_c \approx 4.55356\) — the phase-tangent history ratio (prefactor);
- \(P_x \approx 370.95\) yr — the binding period.

The discrete evidence (finite discretizations; `NUMERICALLY_VERIFIED_DISCRETE_PRODUCT_BUNCHING_AT_35_PERIODS`; register Part II, COMPUTED_PARTIAL): \(q_{35}^{\rm disc,ext} \approx 0.338 < 1\), robustly (marginal at \(n=30\): 0.9516). The three unsoundness channels recorded in that assessment — discretized binding projections, method-of-lines slack norms, unenclosed discretization-to-continuum operator errors — are exactly what the transfer must close.

**The certified substrate now available (A1 Stage 4d):** a true periodic solution \(y^*\) of the C4 DDE within \(3\times10^{-7}\) (sup-norm, augmented history state) of the committed substrate, at a period within \(3\times10^{-7}\) of \(P\); plus the validated machinery — the outward-rounded interval evaluation (Stage 2), the local Krawczyk systems with the delay coupling enclosed (Stage 3), the block-wrapped affine noise-symbol march (Stage 4b), and the localised kink ladder with the eta-lift (Stage 4d).

## 2. The transfer stages

### Stage T1 — the continuum one-period variational certificate (binding block)

**Input:** the certified orbit \(y^*\) (4d) and its certified radius-3e-7 tube.

**What to certify:** the action of the one-period variational (monodromy) operator of the TRUE DDE along \(y^*\), restricted to the stable complement (the phase direction removed by the certified tangent — already computed in the 4a/4b assembly: \(\|\mathrm{Mon}\,\hat\tau - \hat\tau\|/\|\hat\tau\| = 3.3\times10^{-8}\), tangent \(\xi\)-dominated by the A-state), evaluated in the **history sup-norm**.

**Machinery mapping:** the 4b block-wrapped affine noise-symbol march applied to the VARIATIONAL equation (the existing operator-column march already propagates the linearized dynamics — the 895 signed basis columns of Stage 4b are the variational march; what changes is the object assembled from it: the stable-complement projector at the certified solution rather than the Krawczyk resolvent). The augmented-state sup-norm → history sup-norm conversion uses the already-computed interpolation-error functionals (the exact Peano constants \(|w'|_{\max} = 0.125\), \(k_d[2] = 6.47\times10^{-2}\), \(k_d[9] = 8.10\times10^{-7}\) of Stage 4c/4d) and the localised kink ladder (the 4d per-patch chains, eps_read \(2.07\times10^{-12}\) worst patch).

**Known obstruction and its treatment:** the interval width-growth rate 1.00264/step is paid once per 500-step block (16 blocks/period) by block-wrapping — the same engineering as 4b. The dichotomy constant \(K_0 = \sup_j\|P_j\|_\infty = 731.6\) (4a) governs the nonnormal transient; the phase-projection norm converges 141.99 → 163.15 → 170.16 across resolutions and must be enclosed on the continuum side.

**Honest feasibility note:** the one-period stable-complement norm is **greater than 1** (the discrete n-period norms are 17.36 at n=10 → the one-period norm is at least \(17.36^{1/10} \approx 1.333\)); no one-period shortcut exists. The certificate must target the n-period product directly (T2).

### Stage T2 — the n-period product march (binding block)

**What to certify:** \(\|S_x^{35}\|\) in the history sup-norm, by marching the stable-complement variational system **35 periods** (560 blocks; each block pays the \(1.00264^{500}\) in-block pessimism once, then block-wraps into the coordinate symbols — the 4b pattern). Checkpointed/resumable exactly as the 4c partials were.

**Feasibility margin (from the discrete evidence):** the discrete \(\|S_x^{35}\| \approx 1.5\times10^{-3}\); the binding channel contributes to \(q_{35}\) a factor \(M_c \times 1.5\times10^{-3} \approx 6.8\times10^{-3}\) — **more than two orders of margin** against the binding side of the inequality. Even a 100× enclosure pessimism (far beyond what the 4d experience suggests: 12.3× at the honest floor) leaves the binding channel below 0.7. The binding side is not the binding constraint of the transfer.

### Stage T3 — the slack-block semigroup certificate

**What to certify:** \(\|T_y(35P_x)\|\) for the CONSTANT-COEFFICIENT linear DDE at the slack equilibrium — a far more tractable object than the binding block (no orbit, no phase). Two admissible routes; the specification does not preclude either:

1. **Spectral:** enclose the rightmost characteristic roots of the slack equation by interval argument principle (outward-rounded), certify the spectral bound \(s^* < -c\) with \(c > 0\), and bound the transient constant \(C\) by the resolvent/conditioning bound along a contour to the right of \(s^*\) — then \(\|T_y(T)\| \le C e^{-cT}\) with \(T = 35P_x \approx 12983\) yr.
2. **Direct:** the upwind method-of-lines march (the discrete evidence's own generator) with the discretization error enclosed by the tail/eigenvalue decay — the observed convergence is linear in \(1/m\) (25→400 intervals: 0.0575 → ~0.0741 at n=35), so the enclosure must carry the extrapolation error explicitly.

**Feasibility margin:** the discrete \(q_{35}\) is **dominated by the slack channel** (\(M_c \times 0.0741 \approx 0.337\) vs the binding's 0.0068). The observed transient is \(C \approx 9\) (n=10 norm 9.0) with decay \(\approx e^{-0.175/\mathrm{period}}\); a certified \(c\) within a factor of 2 of the observed decay and a certified \(C\) within a factor of 3 of the observed transient keep \(M_c C e^{-cT} < 1\) — **roughly one order of combined slack**, tighter than the binding side and the true risk concentrator of the transfer. The specification flags T3 as the stage most likely to need the extra refinement passes (contour optimization; two-sided transient constants).

### Stage T4 — the prefactor certificate

**What to certify:** \(M_c\), the phase-tangent history ratio, from the certified orbit's tangent data (the 4a/4b tangent machinery; the discrete value 4.55356 with the phase-projection norm convergence as the convergence check). Small relative to T1–T3; a bounded-interval enclosure suffices (a 10% enclosure moves \(q_{35}\) by less than the T3 slack).

### Stage T5 — assembly and the persistence statement

**What to certify:** \(q_{35}^{\rm cont} = M_c \cdot \max\{\|S_x^{35}\|, \|T_y(35P_x)\|\} < 1\) in outward-rounded interval arithmetic; then H3 of the generic two-block persistence theorem is instantiated on the C4 scaffold. **The theorem's remaining hypotheses must be discharged alongside**, per its own status note ("Application to the C4 scaffold remains conditional on CAP and perturbation bounds"):

- **H1** (regularity/localization): the \(C^2\) regularity of the certified orbit and the \(\delta_\varepsilon\) perturbation bound — the smoothness certificates already exist in embryo (the 4c/4d bootstrap bounds the solution's \(z^{(9)}\); the true solution is \(C^\infty\) wherever \(f\) is, the patch-boundary kinks being representation artifacts — the eta-lift's cascade analysis);
- **H2** (split tubular coordinates): the stable bundle and the tubular chart — constructible from the T1 projector data at the certified radius;
- **the A2 coupling class** \(G, f, g\) — **DECLARED, awaiting the author decision** (`OPEN_PROBLEMS_REGISTER.md` A2; `remaining_obstacles` obstacle 3). The transfer does not require it, but the Paper 4 capstone statement does: without a declared coupling, what T5 certifies is the two-block scaffold's persistence, not the coupled system's.

**Register consequences if T1–T5 close:** Part II B4-bunching row COMPUTED_PARTIAL → COMPUTED (continuum); Part III "Paper 4: NAIM persistence capstone" candidate support gains the continuum product certificate (the row remains NOT CONFIRMED until the paper-claim-level match); Paper 6's gate (A021 continuum periodic-NAIM) substantially advanced. If any stage fails to close, the honest outcome is the A1-4c pattern: the machinery verified, the obstruction scoped, and the Paper 4 capstone published at the discrete level with the declared coupling (as currently scoped in Part III).

## 3. Campaign cost estimate and ordering

- **T3 first** (the risk concentrator; constant-coefficient; no dependence on the certified orbit; the cheapest stage per unit of information — it decides whether the transfer is viable at all);
- **then T1 + T2** (the heavy marches; T2 ≈ 35 × the 4b Phase-A cost per run, checkpointed; the 4d localised ladder is already in place for the history-norm conversion);
- **T4 and T5 last** (cheap; assembly).
- Estimated multi-session (the A1 campaign's 4a–4d arc is the calibration: each march stage ≈ one session with resumability engineering; T2's 560-block march is the single longest computation, comparable to 35 concatenated 4b Phase-A runs).

## 4. What this document does NOT do

It executes no computation, changes no status, and certifies nothing. The B4 bunching row remains COMPUTED_PARTIAL (discrete only); the Paper 4 capstone row remains NOT CONFIRMED; Paper 6's gate remains closed. The document's own claim is exhausted by: the machinery mapping above is faithful to the committed A1 artifacts (each cited constant is register-pinned), and the feasibility margins are computed from the committed discrete evidence.

## 5. Execution record (appended 2026-08-28)

The transfer is EXECUTED. The stages, their levels, and the assembly:

- **T3 (the slack channel) — CERTIFIED at the continuum level in outward-rounded interval arithmetic**: the rightmost characteristic roots of the slack characteristic equation enclosed in disks with certified winding numbers (existence, location, simplicity), with rectangle counts 0 roots at Re ≥ −0.0005 (the pair globally rightmost) and exactly 3 at Re ≥ −0.05; the semigroup norm via the residue-functional decomposition with the rigorous contour remainder: ‖T_y(35 P̂)‖ ≤ 8.9916e−2 (requirement 1/M_c = 0.2196; 2.44× margin) and ‖T_y(40 P̂)‖ ≤ 3.3885e−2 (the 0.25/M_c target = 0.0549; 1.62× margin). Runner `../validated_computations/a021_c4/b4_t3_slack_semigroup_certificate.py`; record `b4_t3_slack_semigroup_certificate.md`.
- **T2 (the binding channel) — CERTIFIED at the collocation level in the Stage-4b affine noise-symbol arithmetic**: the deflated (Mon·D)^n march for n = 1..40 with signed within-period propagation, block-wrapped magnitude accumulation, and period-boundary signed deflation + collapse of the noise zonotope; ‖S_x^35‖ ≤ 5.8923e−3 and ‖S_x^40‖ ≤ 3.6820e−3. The float part matches the direct matrix products to 1e−11; the one-period noise extent reproduces the committed 4b eval value 4.820e−3 exactly. The operator-level continuum lift (the true-DDE variational monodromy vs the collocation monodromy) is NOT enclosed — this is the transfer's remaining open item on the binding side (the committed 4d certificate lifts the solution, not the variational operator).
- **T4 (the prefactor) — CERTIFIED**: M_c ≤ 4.590009620 from the committed Fourier substrate with the 4d tube + phase-drift + evaluation-noise budget (0.80% above the committed discrete value; the specification's 10% budget respected).
- **T5 (the assembly) — CLOSED at both horizons**: q_35 ≤ 0.41272 < 1 (2.42× margin; slack-dominated) and q_40 ≤ 0.15553 < 1/4 (1.61× margin; the persistence theorem's own application target).

Record: `b4_transfer_execution_record.md`. Register consequences: the two-block scaffold's bunching inequality closes with the channel levels as stated; the B4 row carries the executed-partial status (the full COMPUTED (continuum) promotion awaits the binding channel's operator-level continuum lift, the H2 tubular chart, and the A2 coupling declaration); the Paper 4 capstone row is not promoted; Paper 6's gate is substantially advanced, not passed. No theorem status is promoted anywhere by this execution.
