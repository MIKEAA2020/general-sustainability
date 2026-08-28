#!/usr/bin/env python3
"""Scientific row-closure pass for source A018 (uploads/manuscript.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, and A014 passes. The full source (*Scarcity-Driven Capital
Liquidation and Delay-Amplified Instability: A Vector-Valued Flow-Balance
Framework for Sustainability*, 1573 lines) was read in full; every inventoried
item was located in the source; for each of the 18 A018 rows this pass
verifies item existence, kind, the source's own status discipline (theorem/
conjecture/numerical-result environments; the A018-L1..L7 line-level audit is
the verification witness), the canonical module, the primary mapping type per
TCS-1.0 §7, and the proof/evidence status. The committed corrected article
(revised_articles/A018_capital_liquidation_corrected.tex) was read alongside:
it implements the donor-fraction sign fix (A018-L1, "strictly increasing"),
the CES elasticity reparameterization (A018-L2, sigma_Q with the correct
Cobb-Douglas/Leontief limits), the Euclidean-norm specification for the cone
distance (A018-L3), the Tikhonov demotion theorem-to-conjecture (A018-L4),
and the fold-language conformance to A025's non-certificate status (A018-L5).

A018-specific findings:

1. NO intake row corruptions: all 18 rows quote-check cleanly against the
   inventory list.

2. ONE mapping-type correction: CC-A018-002 (the donor-limited vector
   material ledger and conservation theorem) APPROXIMATION ->
   EXACT_SPECIALIZATION. The theorem is exact under the unit-sum routing
   constraints (dM_tot/dt = 0 with the incidence-matrix proof); the
   A002-008 typed-hybrid-conservation family precedent maps exact
   conservation identities as EXACT_SPECIALIZATION. The approximation
   content belongs to the open-projection COROLLARY (the reduced cores are
   not mass-closed), which is carried by rows -007/-008, not by this row.
   This is the A002 substring-false-positive defect class surfacing at
   intake.

3. SEVEN module classifications (A018 unclassified 7 -> 0), each matching
   the intake monograph chapter: the nonnegative-orthant theorem, the
   deficit identity, and the exact triangular projection -> ledger_diagnostics
   (the ledger's positivity, its diagnostic identity, and the ledger-to-
   dynamics seam object of the A018 interface contract); the working/QSS
   closures, the frozen-active-pool approximation, the four-state numerical
   results, and the stoichiometric feedback/loop-gain content ->
   nonlinear_dynamics. FIVE mapping classifications (UNRESOLVED -> resolved).

4. NO destination corrections: the destinations verify row by row against
   the architecture (P2 for the scalar-certification obstruction and the
   demoted macro reduction; P3 for the ledger, its positivity, the deficit
   identity, the exact seam projection, and the ADH diagnostics; P4 for the
   named-core dynamics and numerics; P5 for the identifiability groups and
   the empirical screen; Paper 1 or monograph for the weak-coupling
   composition result) and against the A018 ledger-to-dynamics interface
   contract (Paper 3 owns the closed ledger; Paper 4 states the named RFDEs
   locally).

5. The upload's defects are real and the corrections are committed:
   (a) A018-L1 donor-fraction monotonicity sign — corrected to "strictly
   increasing" (the sigma_geo remark); (b) A018-L2 CES parameterization —
   reparameterized with sigma_Q and the correct limits (Cobb-Douglas as
   sigma_Q->1, Leontief as sigma_Q->0+); (c) A018-L3 cone distance — the
   Euclidean norm specified; (d) A018-L4 the delayed-Tikhonov theorem is
   internally overstatused with an inconsistent error term — DEMOTED to
   Conjecture in the corrected article (conditional on the Hurwitz
   hypothesis, which the finite-difference sweep supports but does not
   replace); CC-A018-010 (Hopf persistence) inherits the conditionality
   because it assumes that theorem; (e) A018-L5 fold language — conformed
   to A025's explicit non-certificate status everywhere ("numerical
   continuation, multiplier, basin, or turning-region results; no Moore-
   Spence/Krawczyk/nondegeneracy certificate or continuous-DDE fold proof
   is claimed"); (f) A018-L6 — all computational claims accepted at exact
   source-stated status by user attestation, with the Candidate-A local
   Hopf interval certificates INDEPENDENTLY REPRODUCED from committed code
   (byte-identical a025_interval_hopf.json, recorded in the corrected
   article).

6. Evidence-status harmonization: five rows carrying status_crosswalk_
   required or source_status_accepted_artifact_pending at intake are rows
   whose formal content carries its proof on the line (the working/QSS
   closures, the weak-coupling theorem, the sample-and-hold monodromy, the
   identifiability theorem, and the Hopf cubic theorem) — set to
   proof_inventory_present_line_check_required, with the numerical families
   (-014, -015, -018, -017) keeping their accepted/empirical statuses.

Same honest boundary: content-level acceptance only; no theorem status
promoted (the Tikhonov demotion is recorded, not reversed; the turning-region
results stay non-certificates; the frozen-donor quasi-equilibrium stays a
quasi-equilibrium); the §8 interface contract remains open; the paper-time
citation match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-28'

FF = 'formal_foundations'
LD = 'ledger_diagnostics'
ND = 'nonlinear_dynamics'
OG = 'observation_governance_empirics'
AC = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
AP = 'APPROXIMATION'
PR = 'PROJECTABLE_REDUCTION'
PI = 'proof_inventory_present_line_check_required'
SSA = 'source_status_accepted_artifact_pending'
SSE = 'source_specific_empirical_status_check_required'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='proposition + proof verified in source §2 (no scalar weighting certifies componentwise sustainability: for every positive weight vector w and every index k, b_k <= -M with sigma(b)>0 and b_k\' >= M with sigma(b\')<0; the two-coordinate construction b_k=-M, b_j=(w_k M+1)/w_j)', module=(FF, 'confirmed'), mapping=(CO, 'confirmed'), evidence=PI, cite=True,
            extra='the source\'s own bounded-set caveat preserved (a conservative scalar threshold on a bounded admissible set can exclude the most extreme single-component deficits but still cannot identify which component fails — the certification failure is generic); non-compensatory scalars (min margin, violation magnitude, cone distance) DO certify componentwise non-negativity; the Euclidean-norm specification (A018-L3) is implemented in the corrected article; the exact-rational-arithmetic stress test rides the proposition'),
    2: dict(kind='theorem + proof verified in source §3.3 (stoichiometric conservation of the full ledger: under the unit-sum routing constraints and 0<=alpha<=1, Xdot = I F(X) with 1^T I = 0, hence dM_tot/dt = 0; the incidence-matrix proof)', module=(LD, 'confirmed'), mapping=(EX, 'corrected'), evidence=PI, cite=True,
            extra='mapping corrected APPROXIMATION → EXACT_SPECIALIZATION (intake: APPROXIMATION): the theorem is an EXACT conservation identity under the routing constraints — the A002-008 typed-hybrid-conservation family precedent; the approximation content belongs to the open-projection corollary (the reduced cores are not mass-closed; the frozen-A^geo mass error is the recorded integral), which rides rows -007/-008; the donor-fraction monotonicity sign defect (A018-L1: increasing, not decreasing) is corrected in the corrected article\'s sigma_geo remark — the A_g0>0 assumption makes sigma_geo smooth and strictly increasing in the donor level'),
    3: dict(kind='theorem + proof verified in source §6 (forward invariance of the mass orthant: Omega = {N, A^act, U, P, W, I, A^geo, Z >= 0, 0 <= E <= E_max} on the specialised system and the five-, four-, and three-state cores; the face-by-face Nagumo argument)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (matching the intake monograph chapter "Material ledgers and diagnostics" and the architecture\'s Paper 3 content "conservation/nonnegativity"); destination Paper 3 confirmed; the gated-law scope note (the E<=E_max bound fails for the ungated comparison rows; the stoichiometric core\'s signed memory is OUTSIDE the Z>=0 scope) preserved'),
    4: dict(kind='lemma + proof verified in source §6 (exact deficit identity: qEN - R(N,A) = -Ndot on every trajectory of the specialised system and every reduced core; the collapse Lambda = [qEN-R]_+ = [-Ndot]_+ holds only under the S=R identification of the specialisation)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='the ledger family precedent: CC-A012-005 (the decline-pressure identity, ledger_diagnostics/Paper 3); the source\'s own scope discipline preserved — the collapse is a property of the specialisation, not a definition of liquidation on the unreduced ledger (the general diagnostic is C - M^T S, not equal to -Ndot unless waste-product feedback vanishes and the service is identified with regeneration)'),
    5: dict(kind='theorem + proof verified in source §6 (exact triangular projection: under the institutional-failure specialisation the macroeconomic block, prices, and demand do not appear in (Ndot, Adot, Udot, Zdot, Edot); the ecological-institutional subsystem is an exact closed projection for every eps>0, no singular limit required)', module=(LD, 'classified'), mapping=(PR, 'classified'), evidence=PI, cite=True,
            extra='mapping classified PROJECTABLE_REDUCTION — the A002-036 projectability-criterion family (one of two PROJECTABLE_REDUCTION rows in the concordance); destination Paper 3 confirmed: the projection is the ledger-to-dynamics seam object of the A018 interface contract (Paper 3 owns the closed ledger and states this hand-off; Paper 4 states the named RFDEs locally); module ledger_diagnostics per the intake monograph chapter and the seam role'),
    6: dict(kind='conjecture (demoted from theorem in the corrected article) verified in source §6 (finite-time reduction to the five-state core when macroeconomic feedback remains: the O(eps + omega_A T) sup-norm bound and the slow-manifold tracking bound, conditional on Hypotheses scale/hurwitz/lipschitz)', module=(FF, 'confirmed'), mapping=(AP, 'confirmed'), evidence=CRO,
            extra='mapping APPROXIMATION confirmed as a genuine error-bound result (the finite-time O(eps) estimate); A018-L4 implemented: the delayed-Tikhonov theorem was internally overstatused with an error term inconsistent with its proof — the corrected article DEMOTES it to Conjecture, conditional on the Hurwitz hypothesis (the finite-difference sweep over Delta~ in [0,5] supports but does not replace it); the classical Tikhonov/Fenichel theorems are ODE statements — the infinite-dimensional Fenichel-type theorems apply only subject to unverified spectral-gap/compactness conditions; the geological-freezing budget is the cumulative donor change eps_G(T), not omega_A T alone; the CES reparameterization (A018-L2: sigma_Q with Cobb-Douglas as the sigma_Q->1 limit, Leontief as sigma_Q->0+) rides the same macroeconomic layer'),
    7: dict(kind='theorems + proofs verified in source §6 (working and QSS four-state closures: Theorem working-proj — the dynamic derived target makes omega_A(A^eq - A) + gamma_U U = omega_A(A^eq,intrinsic - A) + kappa_A K identically in the sigma_geo=1 limit, so (N,A,Z,E) satisfies the working core exactly with U a driven auxiliary; Theorem detritus — the O(eps_U) slaving under the fixed intrinsic target)', module=(ND, 'classified'), mapping=(AP, 'confirmed'), evidence=PI,
            extra='module classified nonlinear_dynamics (matching the intake monograph chapter "Delay and nonlinear transitions"); mapping APPROXIMATION confirmed (the QSS closure is an O(eps_U) estimate; the working core is exact only at sigma_geo=1 and perturbed O(1-sigma_geo) for finite reservoir); the baseline caveat preserved: gamma_U/r = 10, so eps_U is NOT small — the QSS theorem is a finite-time estimate that does not control global periodic orbits; the QSS core\'s low-A equilibrium (23.85, 0.159) is not dynamically connected to the high-A working equilibrium used for the reported tau_pm'),
    8: dict(kind='theorem + proof verified in source §6 (frozen-active-pool finite-time approximation: sup |four-state - three-state| <= C_T(A_0/A_min + V_A T); an O(eta_A) inner approximation on [0,T], NOT a Tikhonov reduction)', module=(ND, 'classified'), mapping=(AP, 'classified'), evidence=PI,
            extra='module classified nonlinear_dynamics; mapping APPROXIMATION classified (a genuine finite-time error bound); the baseline scope preserved: 1/omega_A ~ 10^3 yr versus 250-390 yr oscillation periods — the theorem justifies the three-state core for local near-equilibrium questions on institutional timescales (the 3.2% tau_- shift is inside the bound) but NOT the large-amplitude cycle or its period'),
    9: dict(kind='lemma + theorem + proofs verified in source §6 (the soft-minimum gap bound pi_j <= w_min^{-1} e^{-rho Delta_y} and the decoupling at the Liebig limit: ||X - X^k|| <= C_T eps_c with eps_c = C e^{-rho Delta_y} + eps_phys)', module=(AC, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the terminal Liebig-limit phase versus the compensatory phase near yield parity preserved (the cross-derivatives are not exponentially small near Delta_y -> 0; Layers 2-4 and the scalar obstruction are the compensatory phase); the physical-remainder-only case (no gap needed) included; the stage/spectral-separation gates for the fuller persistence claim live in the A021 row family'),
    10: dict(kind='theorem + proof verified in source §6 (local Hopf persistence: under the strict specialisation the core spectrum is a literal factor of the full characteristic function so the Hopf points persist exactly; under residual macroeconomic feedback of size eps the shift is O(eps) (+ O(1-sigma_geo) for the finite reservoir), via the Schur-complement/Rouche argument)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO,
            extra='conditional on repaired bridges — the source\'s own assumption list (Theorems tikhonov and working-proj, the simple-pair/transversality/no-other-imaginary-eigenvalues conditions, and the uniformly Hurwitz fast Jacobian): with the Tikhonov theorem DEMOTED to Conjecture in the corrected article (A018-L4), this persistence theorem is conditional on that conjecture — evidence stays conditional_or_open; the global fold events are explicitly outside its hypotheses'),
    11: dict(kind='theorem + proof verified in source §6 (sample-and-hold monodromy: the variational system between reviews is the ODE with A_hold; the monodromy M(T_r) = shear * exp(A_hold T_r); sampled stability iff all eigenvalues of M inside the unit disc; the T_r->0 singular limit recovers the continuous undelayed Jacobian)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the statement is about THIS sample-and-hold/Euler review scheme, not the continuous-delay DDE (the source\'s own scope); on the gated Candidate A hold map annual review is unstable (rho(M(1))=1.00055 — the undelayed linearisation is already unstable) and the sampled equilibrium restabilises by a Neimark-Sacker pair at T_r^NS=47.536 yr with a period-doubling multiplier at T_r^{(-1)}=79.143 yr; the T_r ~ 3-4 yr (anchovy) and 6-12 yr (sprat) windows are zeros of the stage-structured review map — a different operator'),
    12: dict(kind='theorem + proof verified in source §6 (dimensionless identifiability: e* = (a + sqrt(a^2+4b))/2, N*/K = 1 - varrho e*, and after scaling time by r^{-1} the local Hopf delays r*tau_pm depend on (varrho, lambda_F, a, b, Z_ref/delta, eta/r, r*tau_m) and sp_k\'(0)=1/2; the four combinations (qE*, E*/E_max, eta E*/Delta_ref, delta_0/eta) do NOT determine H)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='Candidates A and B are two points in (eta/r, varrho), not one class; the family tie recorded: this theorem is complementary to CC-A012-009 (the effort-scale non-identifiability transformation) — A012-009 shows the separate effort scale is not identifiable from (N,Z) alone, this theorem charts the dimensionless groups that DO fix N*/K and r*tau_pm once effort is scaled by E_max; the paper wave should cite the pair together at the Paper 5 identification seam; the k-invariance qualifications (invariance at fixed delta, not fixed delta/k; criticality NOT k-invariant through sp_k\'\'(0)=k/4) ride the parameters section'),
    13: dict(kind='theorem + proof verified in source §8 (complete local Hopf spectrum: lambda = i*omega is a characteristic root iff x = omega^2 is a positive root of the cubic H and tau = (-arg(P/(C_Z L)) + 2 pi k)/omega > 0; at most three frequency families) + the interval-Newton certificates (Numerical Result interval-hopf: tau_- in [3.6661490142739, 3.6661490142743], tau_+ in [150.3584773101408, 150.3584773101421] yr for gated Candidate A)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the even-pairs algebra (B_N = -(1/2 tau_m) A_N and B_E = -(1/2 tau_m) A_E make the cross term vanish identically, so positive roots occur zero or two at a time); the Candidate A local Hopf interval certificates are INDEPENDENTLY REPRODUCED from committed code (byte-identical a025_interval_hopf.json, recorded in the corrected article and batch 4/VALIDATED_COMPUTATIONS_RERUN.md); this certifies the local spectrum of H — NOT an interval certificate of any global fold'),
    14: dict(kind='numerical results verified in source §8 and Appendix methods (the source-stated Lyapunov, continuation, Floquet, fold, and basin results: l_1(tau_-^A,gated)=+5.75e-5 and l_1(tau_+^A,gated)=+3.55e-4 — both subcritical; l_1(tau_-^B,ungated)=-9.84e-5 — supercritical; the two-family lower boundary with the large-cycle termination in [5.574,5.576] and the small-branch turning region near 5.587; the upper boundary 148.3 with the distinct-families collocation; the five-regime sequence; basin statements for tested histories)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA,
             extra='accepted at exact source-stated status by user attestation (A018-L6) with the publication archive pending; the A018-L5 fold-language correction IS implemented: the events near 5.574-5.576, 5.587, 64.4, and 148.3 are "numerical continuation, multiplier, basin, or turning-region results" — no Moore-Spence/Krawczyk/nondegeneracy certificate or continuous-DDE fold proof is claimed (conforming to A025\'s explicit non-certificate status); fixed-initial-condition bisection mislocates folds by more than 20 yr under critical slowing and is not used for the table'),
    15: dict(kind='numerical results verified in source §9 (the four-state working-core results: the Hopf pair tau_- ~ 3.78, tau_+ ~ 150.1 yr characteristic-pinned; the gated four-state fold events at ~5.63 and ~64.4 yr with the saddle-node classification open; the kappa_A* ~ 0.001316 turnover boundary via sixty (kappa_A, tau) pairs and three methods; the frozen-donor quasi-equilibrium (N*, A*) = (89.526, 397.87) sustained by geological support ~4.652 stock units/yr — NOT a rest point of the closed mass ledger; the eps_G(T) geological-error table)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA,
             extra='module classified nonlinear_dynamics; mapping classified EXACT_SPECIALIZATION; accepted at source-stated status with the archive pending; the frozen-donor quasi-equilibrium discipline preserved (incompatible with the formal QSS target; the working-core thresholds are sigma_geo=1 properties); the period range 250-390 yr essentially independent of tau (frequency pinned by r and tau_m)'),
    16: dict(kind='identity + theorems + proofs verified in source §10 (the stoichiometric feedback identity l = h - (g - m) = -Xdot; the general feedback equation lambda - C_E - C_Z e^{-lambda tau} G(lambda) = 0 unifying the cores\' linearisations at two memory gains g=1/2 vs g=1; the loop-gain exclusion theorem — sup |C_Z G(i omega)|/|i omega - C_E| < 1 excludes delay-induced Hopf for every tau; the Nyquist criterion; the logistic identification theorem with the O(K_A/A) remainder)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
             extra='module classified nonlinear_dynamics; the signed-memory scope (Z* = 0, no Phi_k floor — outside the Z >= 0 invariance statement); the saturating-gate negative screen (more than 300 randomised parameterisations, no genuine Hopf on the searched domain — a numerical nonexistence report, not an analytic exclusion); eta_crit ~ 2.337 with the two Hopf pairs and their interleaving; K_A -> 0 WITHOUT the mortality identification does NOT yield logistic — the identification requires mu - d = r and c = r/K; the linearised-feedback-identity scope (shared linearisation, not shared nonlinear dynamics)'),
    17: dict(kind='empirical diagnostics verified in source §5 (the groundwater/phosphate/fisheries ADH tables: G3P v1.12 basin trends with trend-to-window-minimum horizons; USGS phosphate reserve-life ratios with the reserves/resources split; the RAM pure-decay proxy with median ~1.8 yr across 43 stocks)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE, cite=True,
             extra='the source\'s own scope discipline preserved: none of the reported numbers is a computed instance of the model\'s own first-hitting time — the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted (its caption states it is not an abiotic horizon); descriptive component-resolved diagnostics in the two-pool logic, not dynamical predictions; the equal-weight inverse-horizon score is a ranking device, not a componentwise certificate (Proposition no-scalar)'),
    18: dict(kind='empirical screen and prospective hypotheses verified in source §11 (the 30+ candidate case search with zero eligible systems under the four criteria; the three groundwater near-misses at station resolution; Icelandic cod cohort resonance 15-25x shorter than predicted; the anchoveta confound gate failure via the 3.7 yr ENSO peak; the two structural reasons for the null; the stage-structured review-map windows T_r ~ 3-4 yr (anchovy) and 6-12 yr (sprat) robust to 30% multiplicative assessment error)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE, cite=True,
             extra='the prospective review-interval test is an intervention test (no responsive 3-4 yr review is currently operated — the prediction is untested, not falsified); the institutional signal is carried by effort and quota utilisation (80-240% of E*), not biomass (1-2% of N*); the sampled-governance windows are zeros of the stage-structured review map, a different operator from the Candidate A hold map (annual review unstable there, restabilising only at T_r^NS=47.54 yr) — both statements are det(M - e^{i theta} I) = 0 on the map to which they refer'),
}


def module_verdict_str(v: tuple[str, str], intake_module: str) -> str:
    val, verdict = v
    if verdict == 'confirmed':
        return f'module {val} confirmed'
    return f'module {val} classified (intake: {intake_module})' if intake_module == 'unclassified_canonical_review' else f'module {val} corrected (intake: {intake_module})'


def mapping_verdict_str(v: tuple[str, str], intake_mapping: str) -> str:
    val, verdict = v
    if verdict == 'confirmed':
        return f'mapping {val} confirmed'
    return f'mapping {val} classified (intake: {intake_mapping})' if intake_mapping == 'UNRESOLVED' else f'mapping {val} corrected (intake: {intake_mapping})'


def main() -> None:
    with open(CC, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    n_closed = n_skipped = 0
    for row in rows:
        if not row['concordance_id'].startswith('CC-A018-'):
            continue
        if row['review_state'] == 'row_verified':
            n_skipped += 1
            continue
        suf = int(row['concordance_id'].rsplit('-', 1)[1])
        if suf not in V:
            raise SystemExit(f'no verification decision for {row["concordance_id"]}')
        d = V[suf]
        intake_module = row['canonical_module']
        intake_mapping = row['primary_mapping']

        if d.get('dest'):
            row['destination_paper'] = d['dest']
        row['canonical_module'] = d['module'][0]
        row['primary_mapping'] = d['mapping'][0]
        row['mapping_status'] = 'accepted_mapping'
        if d.get('evidence'):
            row['proof_evidence_status'] = d['evidence']
        row['review_state'] = 'row_verified'

        parts = [f'Row-closed {DATE} (A018 scientific pass; source read in full): {d["kind"]}; '
                 f'{module_verdict_str(d["module"], intake_module)}; {mapping_verdict_str(d["mapping"], intake_mapping)}.']
        ev = d.get('evidence')
        if ev is not None:
            parts.append(f'Evidence status now {ev}.')
        parts.append('Content-level acceptance only: the TCS-1.0 §7 mapping type and the exact source assumptions are verified; the §8 interface contract for cross-module theorem transfer and all theorem statuses remain unchanged.')
        if d.get('cite'):
            parts.append('Citation anchor locked at the source section named above; the paper-time citation match rides the Part III paper-support discipline.')
        if d.get('extra'):
            parts.append(d['extra'])
        row['notes'] = ' '.join(parts)
        n_closed += 1

    with open(CC, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    rev = Counter(r['review_state'] for r in rows)
    print(f'A018 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53 + 24 + 16 + 14 + 15 + 18, f'expected 239 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
