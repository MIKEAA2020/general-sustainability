#!/usr/bin/env python3
"""Scientific row-closure pass for source A010 (uploads/paper4_perspective.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, and A016 passes in the same campaign). The full source
(*A Research Architecture for Sustainability: Typed Fluxes, Governance, and
Robust Viability*, 534 lines) was read in full; every inventoried item was
located in the source; for each of the 15 A010 rows this pass verifies item
existence, kind, the source's own status discipline (the inventory's own
status column — Verified / Correct architecture-level identity / Requires
correction / Model-specific only / Not a proposition — is the verification
witness; the evaluation record confirms the two theorems and the ten-state
audit and records the substantial supersession by A002, which contains the
same observation-fibre and local-horizon results), the canonical module, the
primary mapping type per TCS-1.0 §7, and the proof/evidence status.

A010-specific findings:

1. NO intake row corruptions: all 15 rows quote-check cleanly against the
   inventory table.

2. ONE destination correction: CC-A010-007 (the exergy-gated suppression
   conjecture) Paper 2 -> Paper 4. The conjecture is a LOOP-GAIN theorem
   target ("sufficiently low deployable exergy reduces the loop gain below
   every admissible Hopf-frequency modulus condition") — the CC-A018-016 /
   CC-A020-006 loop-gain family is Paper 4's named content, and the
   audit's "Model-specific only" status bars it from the architecture-level
   exergy programme (which rides Paper 1 via the A002 exergy rows — a
   different object, cited at the seam).

3. TEN module classifications (A010 unclassified 10 -> 0): the local
   threshold-horizon bound -> ledger_diagnostics (the depletion-horizon
   family, joining the A013/A024 rows); the logistic variance identity and
   the C2 curvature bound -> formal_foundations (the projectability/
   coarse-graining family — the CC-A002-036 precedent); the geological
   noninvariance -> ledger_diagnostics (the donor-limit ledger discipline);
   the variance-unclosure and output-Q closure failures -> nonlinear_dynamics
   (the ten-state template's moment and capital dynamics); the stage-
   structured equilibrium formula -> nonlinear_dynamics (the A022 stage
   family); the effort sensitivity coefficients and interior effort bound ->
   nonlinear_dynamics (the template's effort-law linearisation). TEN mapping
   classifications (UNRESOLVED -> resolved); the two closure-failure rows
   and the noninvariance classified COUNTEREXAMPLE_OR_LIMIT (witness
   content per the closure report's boundary principle).

4. THREE evidence kind-corrections: CC-A010-006 (the fold-persistence
   conjecture) source_status_accepted_artifact_pending ->
   conditional_or_open (a conjecture requiring the fold-specific spectral/
   nondegenerability correction, not an accepted numerical result);
   CC-A010-008 (the six-state cancellation) status_crosswalk_required ->
   proof_inventory_present_line_check_required (the identity is displayed
   arithmetic on the line); CC-A010-015 (the delay-crossing record)
   proof_inventory_present_line_check_required -> conditional_or_open (the
   source's own verdict: "not numerical propositions of this article ...
   retained only as reproduction targets pending recovery and registration
   of the constitutive closures actually used").

5. The source's own status discipline preserved verbatim in every row: the
   ten-state template is an admissibility STRESS TEST, not a realization
   (no observation/assessment operator, no command-deployment separation,
   no protective channel, no disturbance strategy, no computed kernel); the
   formal cancellation does not prove forward invariance; the geological
   exchange is not donor limited (must be replaced by separate
   non-negative donor-limited fluxes); the variance dynamics are unclosed
   and not realizable; Q is undefined so the ten equations do not determine
   a unique autonomous DDE; the crossing near tau* ~= 43 with period ~263
   carries the status-qualified reproduction record (Table
   tab:scaf-reproduction: the elevated-forcing cod class eta=5, varsigma=0.8,
   K_0=0.03, q=0.01; the sign d(Re lambda)/d tau < 0 is a STABILIZING local
   crossing — "cannot support language asserting that increasing delay
   creates oscillatory instability"); the supersession map (A002 contains
   the same observation-fibre and local-horizon results, richer kernels,
   projectability, and coarse-graining — A010 is the predecessor statement,
   preserved as the model-audit record).

Same honest boundary: content-level acceptance only; no theorem status
promoted; no spectral proposition created for the unclosed template; the
§8 interface contract remains open; the paper-time citation match rides
Part III.

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
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='theorem + proof verified in source §8 (the observation-fibre certification criterion: a deterministic observation-only certificate c: Y -> {0,1} with c(O(z)) = 1_K(z) for every z in D exists iff membership in K is constant on every observation fibre — the two-line double-inclusion proof); the scope note preserved (it concerns CURRENT latent-state membership certification only; it does not imply observation-based robust control is impossible — distinct states in a fibre may admit a common safe action, and a dynamic impossibility theorem must show incompatibility of every admissible causal policy over observationally indistinguishable histories)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='destination Paper 5 confirmed (the certification limit grounds the identification and falsification design — §10\'s hypotheses 2 and 7 reference observation fibres); the SUPERSESSION MAP recorded: A002 contains the same observation-fibre result (the evaluation record\'s finding) — A010 is the predecessor statement, cite at the seam'),
    2: dict(kind='theorem + proof verified in source §8 (the local threshold-horizon bound: for absolutely continuous A with A(0) > A_min, v_0 > 0, 0 < epsilon < 1, and (1-epsilon)v_0 <= -A_dot <= (1+epsilon)v_0 a.e. while above A_min, the first crossing time H exists no later than H_0/(1-epsilon) and satisfies H_0/(1+epsilon) <= H <= H_0/(1-epsilon) with |H - H_0| <= epsilon H_0/(1-epsilon) — the absolute-continuity integration proof); the scope note preserved (a local diagnostic only: it fails when depletion reverses, the rate approaches zero, or feedback moves the trajectory outside the declared rate bounds)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the depletion-horizon family — joins the A013 hitting-time and A024 first-passage rows at the Paper 3 seam); destination Paper 3 confirmed; the supersession map recorded (A002 contains the same local-horizon result)'),
    3: dict(kind='identity verified in source §3.1 (typed conservation under the left-kernel condition: if L^T S_T = 0 for the typed incidence operator, one conservation law per conserved moiety and boundary follows; "It does not create a scalar sustainability mass across incommensurable systems")', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the CC-A002-008 typed-hybrid-conservation family precedent; the evaluation record\'s clarifications recorded (d_x must be typed — physical disturbance vs structural discrepancy; S_T can contain signed entries though v >= 0; boundary notation harmonized with the master architecture); destination Paper 3 confirmed'),
    4: dict(kind='identity verified in source §5.2 (the logistic variance correction: E[R(X)] = r mu_X (1 - mu_X/K) - (r/K) Var(X) for the logistic R — the quadratic identity; "neither closes the dynamics of the variance"; exact dynamic moment closure occurs only for special functional forms or distributions)', module=(FF, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified formal_foundations (the projectability/coarse-graining family — the CC-A002-036 precedent); destination Paper 2 confirmed (the theorem-programme table\'s "Spatial coarse-graining: quadratic identity and C2 bound above" row)'),
    5: dict(kind='bound verified in source §5.2 (the general C2 curvature bound: |E[f(X)] - f(E[X])| <= (1/2) ||f\'\'||_{inf,I} Var(X) for f in C^2(I) and X supported in I — Taylor\'s theorem; the heterogeneous-harvest covariance term -q Cov(E,X) noted)', module=(FF, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified formal_foundations (same projectability family); destination Paper 2 confirmed'),
    6: dict(kind='conjecture verified in source §8 (Conjecture 1, periodic-orbit-fold persistence: a transverse fold of periodic orbits in a registered scalar DDE persists under sufficiently small typed vector coupling and compatible additional fixed delays IF normal hyperbolicity, a spectral gap, and regularity of the Poincare map hold; "The open work is not satisfied by citing Fenichel theory alone: the hypotheses must be verified for the actual infinite-dimensional system, and the baseline fold must first be established by periodic-branch continuation")', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO, cite=True,
            extra='evidence kind-corrected to conditional_or_open (a conjecture, not an accepted numerical result): the audit status "Requires fold-specific spectral/nondegenerability correction" governs; the A003 structured-persistence conjecture is the same family — the evaluation record directs they be merged rather than maintained as two independent conjectures; destination Paper 4 confirmed'),
    7: dict(kind='conjecture verified in source §8 (Conjecture 2, exergy-gated suppression: for a declared class of autocatalytic extractive controllers, sufficiently low deployable exergy reduces the loop gain below every admissible Hopf-frequency modulus condition; "This is not universal: depletion of institutional capacity may also disable protective action or create hysteresis")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True, dest='Paper 4',
            extra='module classified nonlinear_dynamics; destination corrected Paper 2 → Paper 4: the conjecture is a LOOP-GAIN theorem target — the CC-A018-016 / CC-A020-006 loop-gain family is Paper 4\'s named content, and the audit\'s "Model-specific only" status bars it from the architecture-level exergy programme (which rides Paper 1 via the A002 exergy rows — a different object, cited at the seam); CONJECTURE status retained — no promotion'),
    8: dict(kind='identity verified in source §9.2 (the six-state material cancellation: d/dt(X_A + X_J + P + U + A + G) = 0 by summing the six material equations — "This is an algebraic cancellation only. It does not prove forward invariance of the six material states or physical admissibility of every term"; the ghost-sink check: the same g_B enters dot X_J and dot A with opposite signs, so material not transferred to juveniles remains in A)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='evidence kind-corrected to proof_inventory_present_line_check_required (the displayed arithmetic is on the line); destination Paper 3 confirmed (the cancellation joins the closed-ledger conservation family at the audit seam)'),
    9: dict(kind='boundary test verified in source §9.2 (the geological/support-pool noninvariance: Eq. scaf-G is not donor limited — at G = 0 and A < A^eq it gives dot G < 0; "A physically admissible formulation must replace the fixed-target exchange by separate non-negative donor-limited fluxes e_GA(G,A) and e_AG(A,G) satisfying e_GA(0,A) = 0 and e_AG(0,G) = 0")', module=(LD, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the donor-limit ledger discipline); mapping classified COUNTEREXAMPLE_OR_LIMIT (the noninvariance witness); destination Paper 2 confirmed (the atlas\'s positivity-family boundary example); the A019 primitive-flux ledger is the REPAIR of exactly this defect — cite at the Paper 3 seam (the A019 rows closed this campaign)'),
    10: dict(kind='closure test verified in source §9.2 (the variance equation is unclosed and potentially negative at zero: dot V_N at V_N = 0 equals -2 q X_A Cov(E, X_A), which can be negative; the covariance is not determined by the ten displayed states; "the variance dynamics are both unclosed and not guaranteed to be realizable by a non-negative spatial distribution")', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics (the ten-state template\'s moment dynamics); mapping classified COUNTEREXAMPLE_OR_LIMIT (the closure-failure witness); destination negative/counterexample register confirmed — the ten-state audit\'s headline negative content'),
    11: dict(kind='closure test verified in source §9.2 (the output Q is undefined: Eq. scaf-K contains output Q without a displayed state equation or constitutive closure; the broader production function cannot silently supply the omission; a prescribed path gives a non-autonomous problem, constant or state-dependent closures give different autonomous systems — "the ten equations therefore do not determine a unique autonomous DDE or characteristic quasi-polynomial")', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics (the template\'s capital/production dynamics); mapping classified COUNTEREXAMPLE_OR_LIMIT (the closure-failure witness); destination negative/counterexample register confirmed'),
    12: dict(kind='algebraic result verified in source §9.1 (the stage-structured equilibrium formula X_A* = N_c log[P_0 A^eq/(A^eq + A_0) / Theta(E*)] with Theta(E) = d_A(1 + g d_J) + qE(1 + psi g d_J), subject to P_0 A^eq/(A^eq + A_0) > Theta(E*); the stage distinction preserved: at fixed E, recruitment suppression (psi = 0) contributes qE to the equilibrium drag while adult-selective removal (psi = 1) contributes qE(1 + g d_J) — "an algebraic interpretation within the displayed stage balance, not evidence that the two pressure channels are empirically interchangeable")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics (the A022 stage family); destination Paper 7 conditional confirmed (joins the stage-structured rows if the gate opens); VERIFIED UNDER INTERIOR ASSUMPTIONS status retained; the juvenile compartment\'s methodological role recorded (it separates recruitment, juvenile mortality, maturation, adult mortality, and adult-selective removal — without making the template dynamically complete)'),
    13: dict(kind='algebraic result verified in source §9.1 (the effort sensitivity coefficients C_Z = h_0 g_0 eta E*/Delta_ref and C_K = mu_E E* (1 - g_0)/(K_0 g_0); C_Z is the local sensitivity of effort growth to the delayed decline signal multiplied by the deployable-capital gate g_0; C_K becomes a damping pathway only through its coupling to the separate K_C dynamics; the 1/g_0 factor cannot be extrapolated to g_0 = 0)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; VERIFIED FOR 0 < g_0 < 1 status retained (conditional on a regular interior equilibrium); destination Paper 2 confirmed (the template-conditional algebra rides the atlas\'s diagnostics/certificate family as the model-audit record — the architecture\'s A010 role: technical supplement/model audit; the registered cores\' C_Z values are the A012/A018/A020 rows, a different object)'),
    14: dict(kind='algebraic result verified in source §9.1 (the interior effort upper bound: an interior equilibrium with Z* = 0 and E* > 0 must satisfy h_0 g_0 (delta_0 - eta (E*)^2/E_max) = mu_E E* > 0, hence E* < sqrt(delta_0 E_max/eta) ~= 0.573 at delta_0 = 0.3, E_max = 1, eta = 0.914; "not a failure of boundary invariance ... a restrictive equilibrium consequence of placing the linear loss outside the multiplicative gate; moving loss terms would define a different model")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; the boundary-invariance check recorded (dot E = delta_0(1 - e^{-K_C/K_0}) >= 0 at E = 0 and dot E = -mu_E E_max < 0 at E = E_max); destination Paper 2 confirmed (same audit-record routing as -013)'),
    15: dict(kind='status-qualified reproduction record verified in source §9.3 (the elevated-forcing cod-class calculation: a simple crossing recorded near tau* ~= 43 with period ~263 time units and d(Re lambda)/d tau < 0 at eta = 5, varsigma = 0.8, K_0 = 0.03, q = 0.01; the source\'s own verdict: "not numerical propositions of this article ... retained only as reproduction targets pending recovery and registration of the constitutive closures actually used"; the life-history anchoring and broader-crossing-search rows of Table tab:scaf-reproduction carry the same status)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO, cite=True,
            extra='evidence kind-corrected to conditional_or_open (the source\'s own "Not a proposition" verdict — closures and provenance incomplete: the closure convention, remaining parameters, root count, active nonsmooth branch, residual values, tolerances, and full search domain remain to be recovered); the sign discipline recorded verbatim (d(Re lambda)/d tau < 0 at a simple crossing is a STABILIZING local crossing — the equilibrium locally unstable just below and stable just above; "Such a result cannot support language asserting that increasing delay creates oscillatory instability"); destination Paper 4 confirmed (the reproduction targets ride the reproducibility and certification hierarchy)'),
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
        if not row['concordance_id'].startswith('CC-A010-'):
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

        parts = [f'Row-closed {DATE} (A010 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A010 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 305 + 15, f'expected 320 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
