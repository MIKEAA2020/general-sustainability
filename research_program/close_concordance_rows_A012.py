#!/usr/bin/env python3
"""Scientific row-closure pass for source A012 (uploads/paper2_dynamics.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, and A006 passes. The full source article (*Delay-Amplified Extractive
Mobilisation Under Stock Decline: A Registered Family of Renewable-Resource
Models*, 581 lines) was read in full; every inventoried item was located in
the source; for each of the 14 A012 rows this pass verifies item existence,
kind, the source's own four-status evidentiary discipline (identity/theorem,
numerical result, inferred numerical classification, conjecture — declared in
§1 of the source), the canonical module, the primary mapping type per
TCS-1.0 §7, and the proof/evidence status, with the programme evaluation
record as the verification witness for the targeted corrections.

A012-specific findings:

1. NO intake row corruptions: all 14 rows quote-check cleanly against the
   per-result inventory table.

2. The analytical core verifies line by line: the five-face tangent-cone +
   method-of-steps invariance proof (with the tau=0 ODE fallback), the
   variation-of-constants boundedness/global-continuation proof, the
   determinant-expansion characteristic quasi-polynomial proof, and the
   squared-modulus + unit-modulus-ratio cubic Hopf-frequency theorem (with
   the source's own simplicity/transversality caveat before any crossing
   classification).

3. The source's TARGETED DEFECTS are real in the upload and REPAIRED in the
   committed corrected article (revised_articles/A012_delay_dynamics_corrected.tex):
   (a) the extinction face additionally carries the gate-created boundary
   equilibrium (0, delta, E_max) — repaired at line 173 (the branch exchange
   at r=qE* involves the interior-effort branch only); (b) the fixed-demand
   stock-culling experiment is not donor-limited at N=0 (C_stock = D > 0
   points through the boundary) — repaired at line 446 (first-hitting-time
   stopping rule / explicit donor limiter; the reported time-to-zero retained
   as a first-hitting-time result); (c) the omega_A/kappa_A notation mismatch
   (model equation omega_A vs reported threshold kappa_A) — harmonized to
   omega_A at line 464; (d) the MPF active-material admissibility obligation
   (X+U <= M invariance) — DISCHARGED by the NEW MPF simplex forward-
   invariance theorem at lines 483-487 (d/dt(X+U) = -qEX - gamma_U U <= 0 on
   the boundary, with g(X,0)=0 and m(0)=0). Each defect is recorded in its
   row with both facts (upload defect + committed repair); at paper time the
   corrected statements are the citable ones.

4. FIVE module classifications (A012 unclassified 5 -> 0: the invariance
   theorem, the boundedness corollary, the M3-LC local equivalence, and the
   M3-LC/M4-A numerical families -> nonlinear_dynamics) and FIVE mapping
   classifications (the same rows, UNRESOLVED -> EXACT_SPECIALIZATION —
   registered-model specializations of the canonical machinery).

5. ONE destination correction: CC-A012-006 (interior equilibrium and stock
   branch) Paper 3 -> Paper 4 — the architecture lists A012 exclusively
   among Paper 4's sources, Paper 4's content explicitly includes
   "equilibrium and characteristic equations", and the linearization of
   CC-A012-003/-004 is evaluated at exactly this equilibrium: routing the
   equilibrium algebra to Paper 3 would split the local-bifurcation analysis
   across papers (the A001 Thm 4.8 seam precedent). The standalone identity
   rows stay at Paper 3: the decline-pressure diagnostic identity
   (CC-A012-005) is a componentwise-deficit object and the support-saturated
   logistic limit (CC-A012-008) is primitive-flux-ledger content.

6. Evidence-status harmonization for the numerical families: CC-A012-010
   and -011 carried conditional_or_open at intake; the evaluation record
   accepts ALL numerical families at the source's asserted status on the
   user's instruction (numerical result / inferred numerical classification),
   with the reproducibility archive a publication obligation — the accurate
   evidence status for all five family rows (-010..-014) is
   source_status_accepted_artifact_pending (accepted at source status;
   artifact archive pending), which the A011 pass established for exactly
   this situation.

7. The shared bibliography dependency (\\input{../shared/references.tex},
   source line 581) is declared but NOT committed (no uploads/shared/) —
   registered in the closure report as a paper-time citation obligation
   (the CC-A011-024 precedent; no inventory row exists for it).

Same honest boundary: content-level acceptance only; no theorem status
promoted (the inferred criticalities stay inferred; the SNPO classifications
stay conjectural; the numerical families stay numerical); the §8 interface
contract remains open; the paper-time citation match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-28'

ND = 'nonlinear_dynamics'
LD = 'ledger_diagnostics'
AC = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
AP = 'APPROXIMATION'
TR = 'TRANSFORMATION'
PI = 'proof_inventory_present_line_check_required'
SSA = 'source_status_accepted_artifact_pending'

V: dict[int, dict] = {
    1: dict(kind='theorem + proof verified in source §2.2 (forward invariance of the M3-B box D = {0<=N<=K, Z>=0, 0<=E<=E_max}: five boundary-face tangent-cone calculations with the delayed history non-negative on each step, method-of-steps induction over [n*tau,(n+1)*tau], and the tau=0 ODE fallback; cited standard RFDE invariance machinery)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='the evaluation confirms the theorem correct; the admissible-history clarification recorded (every history value lies in the box, not only the endpoint); the multiplicative gate is load-bearing (a hard saturation architecture, not a generic effort law)'),
    2: dict(kind='corollary + proof verified in source §2.2 (boundedness and global continuation: variation of constants in the Z equation with the monotone bounded input nu <= Phi_k(q E_max K) gives Z-bar, then bounded-set local Lipschitz continuation for all t>=0)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI,
            extra='the evaluation confirms the corollary correct; the extinction-face remark of the same section (Z relaxes to delta; the baseline source sustains commanded effort at zero realised harvest; E is an institutional deployment intensity, not a conserved stock — no closed-effort-energetics claim) rides this row'),
    3: dict(kind='proposition + proof verified in source §3.2 (characteristic quasi-polynomial P(lambda) - C_Z L(lambda) e^{-lambda tau} = 0 by determinant expansion of the 3x3 modal system; the gate factor (1-E*/E_max) distinguishes M3-B from M3-U)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the evaluation confirms the factorisation correct; the linear coefficients are evaluated at the interior equilibrium of CC-A012-006 — the two rows form one local-bifurcation analysis (the destination seam noted there)'),
    4: dict(kind='theorem + proof verified in source §3.3 (cubic modulus condition and phase branches: squared moduli give the cubic H(x) in x=omega^2; conversely each positive root gives the unit-modulus ratio R=P(i omega)/(C_Z L(i omega)) and phase branches tau_k=(-arg R+2 pi k)/omega)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the source\'s own discipline preserved: candidates qualify as Hopf crossings only after separately verified simplicity and transversality; the cubic bounds distinct positive frequency families by three and determines neither criticality nor global folds; the first Lyapunov coefficients remain undone (the source\'s open-question list, item 2)'),
    5: dict(kind='identity verified in source §2.1 Eq. (4) (decline pressure Lambda(t)=max{0,qEN-S(N)}=max{0,-Ndot}: the memory input is a smoothed stock-decline rate, exactly the positive part of the decline)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='exact per the evaluation; not a stock-level scarcity measure, unmet-consumption measure, or independently observed service deficit; qEN-S(N)=O(N) as N->0 so the raw decline input vanishes near extinction while the baseline source can sustain commanded effort (the incremental-vs-baseline distinction of the same section)'),
    6: dict(kind='algebra verified in source §3.1 (interior equilibrium: Z*=Phi_k(0)=delta; the effort bracket gives a quadratic with exactly one positive root; admissibility 0<E*<min{E_max,r/q}; N*=K(1-qE*/r); equilibrium independent of tau and k)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, dest='Paper 4',
            extra='destination corrected Paper 3 → Paper 4: the architecture lists A012 exclusively among Paper 4\'s sources and Paper 4\'s content explicitly includes "equilibrium and characteristic equations"; the linearization of CC-A012-003/-004 is evaluated at exactly this equilibrium, so routing the equilibrium algebra to Paper 3 would split the local-bifurcation analysis across papers (the A001 Thm 4.8 seam precedent); the extinction-face defect in the upload (the gate also creates the boundary equilibrium (0,delta,E_max)) is repaired in revised_articles/A012_delay_dynamics_corrected.tex line 173 (the r=qE* branch exchange involves the interior-effort branch only; the boundary branch classified separately)'),
    7: dict(kind='identity verified in source §5.3 (M3-LC equals M3-U whenever the recruitment floor is inactive: the two-channel law reduces exactly to Ndot=S(N)-qEN, so the equilibrium and local characteristic equation are independent of psi and kappa)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='the source\'s own scope preserved: local equality does not imply excursion equality (the floor truncates recruitment on large excursions; the fixed-demand and tau=115 transient experiments of the same section demonstrate the divergence); the two-channel law is a phenomenological stock equation, not a closed mass ledger (C_recruit is demographic suppression, not a material transfer)'),
    8: dict(kind='identity verified in source §5.5 (MPF support-saturated logistic stock limit: for fixed interior A>0, K_A->0 gives Xdot=(mu-d)X-cX^2-qEX = rX(1-X/K)-qEX with r=mu-d, K=(mu-d)/c, requiring mu>d, c>0; direct substitution)', module=(LD, 'confirmed'), mapping=(AP, 'confirmed'), evidence=PI, cite=True,
            extra='mapping APPROXIMATION confirmed as a genuine limit result: pointwise on the interior support region, NOT uniform through the depleted-pool boundary (A/(K_A+A)=0 at A=0 for every K_A>0); the scope restriction preserved — the identity does not eliminate U, make A constant near its boundary, transform the memory or effort laws, or transfer Hopf/fold thresholds ("an ecological stock-equation identity, not a full-core reduction"); the MPF active-material admissibility obligation (X+U<=M invariance) is DISCHARGED in the corrected article by the NEW MPF simplex forward-invariance theorem (d/dt(X+U)=-qEX-gamma_U U<=0 on the boundary, with g(X,0)=0, m(0)=0) — the paper-time companion theorem'),
    9: dict(kind='identifiability result verified in source §6 (effort-scale transformation: E\'=aE, E\'_max=aE_max, q\'=q/a, delta_0\'=a delta_0 with correspondingly scaled effort histories leaves the (N,Z) trajectory unchanged)', module=(AC, 'confirmed'), mapping=(TR, 'confirmed'), evidence=PI, cite=True,
            extra='structural non-identifiability of the separate effort scale, q, E_max, and delta_0 from (N,Z) observations alone — direct effort observations in a calibrated unit, a scale normalization, or additional deployment measurements required before separate empirical interpretation; the paper wave should cite this row at the Paper 5 empirical-identification seam even though its primary home is the Paper 1 transformation-operator family'),
    10: dict(kind='numerical proposition family verified in source §5.1 (M3-U thresholds, cycles, folds, basins: Candidate A crossings tau-=6.8814, tau+=132.3749 yr; Candidate B 6.2136/76.2906 yr; persistence boundaries ~7.355/131.24 yr; bistability windows ~0.47/1.1 yr; basin-dependent capture at tau=131.8; unstable small orbit below the lower Hopf; eta and r sweeps bounding the two-crossing window)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA,
             extra='accepted as verified numerical work at the source\'s asserted status per the evaluation record (the user instruction), with the reproducibility archive a publication obligation; the SNPO classification of either persistence boundary remains conjectural (branch collision and nondegeneracy not demonstrated); basin statements restricted to the histories actually tested; the sensitivity sweeps are model sensitivity results, not empirical calibration'),
    11: dict(kind='numerical proposition family verified in source §5.2 (M3-B thresholds, folds, Floquet, basins: Candidate A crossings tau-=3.67, tau+=150.36 yr; Candidate B 5.5128/80.4245 yr; distinct lower periodic-orbit folds near 5.574-5.575 (stable large-cycle branch) and 5.587 yr (small unstable branch; real multiplier 1.0514 at tau=5.584 to 0.998983 at 5.587); upper persistence boundary 148.3 yr bracketed [148.125,148.438] with open classification)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA,
             extra='the inferred subcritical signatures (amplitude exponent 0.47; surrogate cubic coefficient ~3.9e-6) are inferred numerical classifications, NOT first Lyapunov coefficients from a DDE centre-manifold calculation (the source\'s own status discipline); the two lower folds belong to distinct periodic-orbit families, so a single square-root collision law is inapplicable; the gate\'s threshold relocation (~47% lower, ~14% upper for Candidate A) shows thresholds cannot be transported between variants; finite searches support but cannot prove interior monostability; k-independence is local only'),
    12: dict(kind='numerical proposition family verified in source §5.3 (M3-LC persistence and fixed-demand experiments: upper persistence boundary ~132.0 yr at psi=1 vs ~132.5 yr at psi=0 with the ~0.8-yr inter-locator discrepancy treated as localisation uncertainty; tau=115 transients of order 1e4-1e5 yr with minimum N~33 (psi=1) vs N~10 (psi=0); fixed-demand D=0.7 experiment: stock culling reaches zero near time 158, recruitment suppression N<1 near time 430)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA,
             extra='the fixed-demand culling boundary flaw REMAINS in the upload (C_stock=D>0 points through the non-negative boundary; the post-hit model not physically admissible as written) — the correction IS implemented in the corrected article (first-hitting-time stopping rule / explicit donor limiter, line 446; the reported time-to-zero retained as a first-hitting-time result); the defensible conclusion is an order-of-one-year shift, not an exact percentage; local equivalence does not imply excursion equivalence; assigning psi to a field system requires age-, stage-, or replenishment-specific evidence'),
    13: dict(kind='numerical proposition family verified in source §5.4 (M4-A thresholds and turnover boundary: ungated Candidate-A equilibrium (89.5256, 397.8665, 2.0896) with crossings 6.982022/132.272044 yr and persistence boundaries ~7.374/130.77 yr; gated counterpart crossings ~3.7849/150.12 yr with 360-380 and 150-160 yr cycle periods; the tau=0 turnover stability boundary at ~0.001316298 (gated ~0.001330) with 1798-point sweep, 60 sub-threshold simulations, 60 continuation points)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA,
             extra='the omega_A/kappa_A notation mismatch REMAINS in the upload (the model equation uses omega_A; the numerical boundary is reported as kappa_A) — harmonized to omega_A in the corrected article line 464 before any threshold citation; the open-relaxation caveat preserved (a reduced open-pool model, not a closed ledger, not a proved Tikhonov reduction); the finite sweeps support delay-independent sub-threshold stability, not a theorem for all parameter values; freezing A is not a justified fast-variable elimination at the baseline omega_A=1e-3'),
    14: dict(kind='numerical proposition family verified in source §5.5-§5.6 (MPF Hopf/transient/basin/sweep results: the illustrative baseline (X*,U*,E*)~(16.68,10.23,0.435) has no local Hopf crossing for 0<=tau<=500; the apparent onset near tau=33.4-33.6 reclassified as a long-lived decaying transient (return within ~2e4 units over the tested 33.4-34.8 interval); basin-selective global dynamics for tau>=35; parametric Hopf onset at eta_crit~2.337 with interleaving crossing pairs over eta in (2.337,3]; supercritical-consistent onset (exponent 0.59, inferred); the 300-parameterisation sigmoid-gate negative screen)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA,
             extra='the active-material boundary check obligation is DISCHARGED in the corrected article (the MPF simplex forward-invariance theorem — see the CC-A012-008 note); the negative screen is a numerical negative result over the sampled domain, not a structural impossibility theorem; the baseline regime is neither the M3-B regime nor a transfer of its threshold values'),
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
        if not row['concordance_id'].startswith('CC-A012-'):
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

        parts = [f'Row-closed {DATE} (A012 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A012 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53 + 24 + 16 + 14, f'expected 206 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
