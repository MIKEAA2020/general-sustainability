#!/usr/bin/env python3
"""Scientific row-closure pass for source A006 (uploads/Paper_II_Robust_Epistemic_Viability_V2.txt).

Executed 2026-08-28, following the procedure established by the A001, A002, and
A011 passes (research_program/close_concordance_rows_A001.py, _A002.py,
_A011.py). The full source article (*Robust and Epistemic Viability for
Hybrid Material-Institution Systems*, 228 lines) was read in full; every
inventoried item was located in the source; for each of the 16 A006 rows this
pass verifies item existence, kind, the source's own claim-status discipline
(the source carries an explicit claim-status summary table in its final
sections), the canonical module, the primary mapping type per TCS-1.0 §7, and
the proof/evidence status, with the programme evaluation record
(research_program/article_006_robust_epistemic/evaluation_and_verification.md)
as the verification witness for the one critical defect.

A006-specific findings (beyond the A001/A002/A011 patterns):

1. NO intake row corruptions: all 16 rows quote-check cleanly against the
   inventory (which is a per-result table, the A012/A013 format).

2. THE CRITICAL DEFECT IS REAL AND ITS REPAIR IS COMMITTED: CC-A006-006
   (Conditional sampled epistemic-institutional viability) is NOT verified as
   written in the upload — the finite-horizon recursion
   K_{n+1} = K_n ∩ Pre_I(K_n) and the Tarski operator T(Q) = S ∩ Pre_I(Q)
   are not the same operator, so the countable/transfinite fixed-point claim
   does not follow from the displayed recursion (evaluation record §6.2).
   The repair IS implemented in the committed corrected article
   revised_articles/A006_robust_epistemic_corrected.tex (the safe-base form:
   K_{n+1} = T(K_n) := S ∩ Pre_I(K_n), with the deflationary-orbit equivalence
   remark). The row records both facts; at paper time the corrected statement
   is the citable one. Evidence status stays conditional_or_open.

3. FIVE module corrections, all by cross-source family consistency with the
   already-closed rows: -002 (hybrid history-cone invariance /
   nonnegativity) nonlinear_dynamics -> formal_foundations (the A002-011
   nonnegative-invariance family for ordinary/hybrid/RFDE modes is
   formal_foundations); -004 (stability/safety independence counterexample
   lemma) nonlinear_dynamics -> formal_foundations (the A001-008
   viability-concept counterexample family); -008 (common-action obstruction)
   formal_foundations -> observation_governance_empirics (the A001-026
   instantaneous common-action obstruction family); -009 (observer-to-safety
   transfer) formal_foundations -> observation_governance_empirics (the
   A001-030 observer/eroded-set transfer family); -014 (safe-learning
   template) formal_foundations -> observation_governance_empirics (the
   A001-006 information-contraction and A001-094 adaptive-learning families).

4. TWO destination corrections, both closing seams that split one object or
   one family across papers: -004 Paper 4 -> Paper 2 (the lemma is not
   delay-specific — it is an explicit failure boundary of viability theory,
   the A001-008 family's destination; the architecture lists repaired A006
   fragments among Paper 2's sources); -006 Paper 5 -> Paper 2 (the sampled
   epistemic-institutional kernel definition -005 is already Paper 2 and the
   whole A002 sampled-kernel family -021/-025/-026/-033 is Paper 2; routing
   the kernel's fixed-point theorem to Paper 5 would split the kernel object
   across papers — the A011 seam pattern; the architecture's Paper 2 content
   explicitly includes 'robust/epistemic kernels ... sampled/hybrid
   restrictions').

5. Supersession discipline preserved verbatim: the evaluation record's table
   (stronger sources for every duplicated theorem family) is carried into the
   row notes as paper-time canonical-source-selection obligations — A002-008
   (typed hybrid conservation) over the moiety balance; A002-011 over the
   history-cone invariance; A001-023-family over the full-information
   benchmark; A001's information-refinement theorem; A001-026-family common
   action; A001-030 observer transfer; A001 Theorem 16.1 + A002 contract
   framework over compositional safety. The source's unique preserved object
   is the joint institutional information state (B,h) with prescription
   authority Gamma and implementation correspondence E and the lower-game
   quantifier order (evaluation §14, §5).

Same honest boundary as A001/A002/A011: content-level acceptance only; no
theorem status promoted (the -006 defect is recorded, not repaired in the
source); the §8 interface contract remains open; the paper-time citation
match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-28'

FF = 'formal_foundations'
OG = 'observation_governance_empirics'
ND = 'nonlinear_dynamics'
LD = 'ledger_diagnostics'
AC = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
DO = 'defined_source_object'
CRO = 'conditional_or_open'
SCR = 'status_crosswalk_required'

V: dict[int, dict] = {
    1: dict(kind='theorem + proof verified in source §2 (conditional hybrid moiety balance; integrate between locally finite events and telescope the left/right jump differences)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='jump-interpretation clarification recorded: an internal-transformation jump requires L^T(r+−r−)=0 or a jump incidence factorization with left-kernel conservation, a boundary-crossing jump is a boundary impulse; the yield-routing obligation of the same section rides this theorem; superseded-but-preserved versus CC-A002-008 (typed hybrid conservation) — canonical source selection at paper time'),
    2: dict(kind='theorem + proof verified in source §2 (conditional hybrid history-cone invariance: quasipositivity at zero material components + reset positivity + induction over the locally finite event sequence)', module=(FF, 'corrected'), mapping=(EX, 'confirmed'), evidence=PI,
            extra='module corrected to formal_foundations (intake: nonlinear_dynamics) by cross-source family consistency: the same nonnegative-invariance family for ordinary/hybrid/RFDE modes is classified formal_foundations (CC-A002-011); destination Paper 4 unchanged, matching CC-A002-011; the interval-of-existence limitation and the positivity-only scope (the source\'s own remark: positivity, boundedness, persistence, and viability are distinct) preserved; superseded-but-preserved versus CC-A002-011'),
    3: dict(kind='proposition verified in source §3 (conditional full-information viability benchmark — a conditional invocation of established controlled-invariance theory; no proof on the line)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO,
            extra='the source\'s own claim-status table: "conditional benchmark / finite-dimensional ODE" and the source\'s own remark: "an ideal ODE benchmark. It is not a theorem for delayed, sampled, partially observed institutions"; the canonical theorem of the invoked family is CC-A001-023 (formal_foundations, Paper 2) — at paper time the benchmark is cited as the ideal limit of the sampled-governance comparison, with the A001 robust-tangency family as the formal source'),
    4: dict(kind='lemma + proof verified in source §3 (stability and safety are independent: xdot=−(x+1) with safe set [0,∞) for the first statement; a nominally safe stable system with a disturbance class driving the state outside the set for the second)', module=(FF, 'corrected'), mapping=(CO, 'confirmed'), evidence=PI, dest='Paper 2',
            extra='module corrected to formal_foundations (intake: nonlinear_dynamics) and destination corrected Paper 4 → Paper 2: the lemma is not delay-specific — it is an explicit failure boundary of viability theory, the CC-A001-008 counterexample family\'s module and destination; the architecture lists repaired A006 fragments among Paper 2\'s sources; the second counterexample remains verbal in both the upload and the corrected article — the evaluation record supplies the explicit example (xdot=−x+w, w∈[−2,2], C=[−1,1]) as a paper-time obligation'),
    5: dict(kind='definition verified in source §5 (finite-horizon epistemic-institutional kernel: K_0=S, K_{n+1}=K_n ∩ Pre_I(K_n))', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DO, cite=True,
            extra='module confirmed by the CC-A002-032 compact-sampled-information-model precedent; the institutional information state Z=(B,h) with prescription authority Gamma and implementation correspondence E is the source\'s unique preserved architectural object (evaluation §14)'),
    6: dict(kind='theorem + proof verified in source §5 (conditional sampled epistemic-institutional viability) — NOT VERIFIED AS WRITTEN: the critical operator mismatch is real (the recursion K_{n+1}=K_n∩Pre_I(K_n) and the Tarski operator T(Q)=S∩Pre_I(Q) are not the same operator, so the fixed-point claim does not follow from the displayed recursion; evaluation record §6.2)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO, dest='Paper 2',
            extra='destination corrected Paper 5 → Paper 2: the kernel definition CC-A006-005 is already Paper 2 and the whole A002 sampled-kernel family (CC-A002-021/-025/-026/-033) is Paper 2; routing the kernel\'s fixed-point theorem to Paper 5 would split the kernel object across papers (the A011 seam pattern); the architecture\'s Paper 2 content explicitly includes "robust/epistemic kernels ... sampled/hybrid restrictions"; the repair IS committed in revised_articles/A006_robust_epistemic_corrected.tex (safe-base form: K_{n+1}=T(K_n):=S∩Pre_I(K_n) with the deflationary-orbit equivalence remark) — the corrected statement is the citable one at paper time; the ω-continuity-from-above condition for the countable limit and the transfinite fallback preserved; abstract-characterization status preserved (no nonemptiness, tractability, or calibration claim)'),
    7: dict(kind='theorem + proof verified in source §6 (information-refinement monotonicity: a controller with finer information can ignore it and implement a coarser-information strategy)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI,
            extra='common-space/projection clarification recorded: the inclusion IViab^{I2}_T ⊆ IViab^{I1}_T requires the two kernels represented in a common physical initial-state space or a declared map between belief-state spaces; A001\'s fuller information-refinement theorem is the canonical source at paper time'),
    8: dict(kind='proposition + proof verified in source §6 (common-action obstruction: output feedback must choose one action/prescription before the uncertainty within B is resolved; no such action is robustly safe for all compatible states)', module=(OG, 'corrected'), mapping=(CO, 'confirmed'), evidence=PI,
            extra='module corrected to observation_governance_empirics (intake: formal_foundations) by cross-source family consistency: the instantaneous common-action obstruction family is CC-A001-026 (observation_governance_empirics, Paper 2); prescription-level reformulation recorded: the robust object is A_com(B,h)={a∈Γ(B,h): E(x,h,a)⊆U_safe(x) ∀x∈B} — an empty raw-action intersection does not preclude a common prescription under state-dependent implementation; A001\'s common-action and hidden-mode results are the stronger sources'),
    9: dict(kind='proposition + proof verified in source §6 (conditional observer-to-safety transfer: full-state inward margin η_i preserved whenever L_i·||X̂−X|| ≤ η_i)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=PI,
            extra='module corrected to observation_governance_empirics (intake: formal_foundations) by cross-source family consistency: the observer/eroded-set transfer family is CC-A001-030 (observation_governance_empirics, Paper 2); dot-product notation and region/admissibility conditions recorded as required corrections; local sufficient condition only — eroded-set motivation without observer existence or estimator bounds; CC-A001-030 is the stronger source'),
    10: dict(kind='proposition verified in source §6 (conditional compositional safety — stated WITHOUT proof on the line; the source\'s own remark: "conditional on the interface contracts; separate subsystem certificates alone do not imply network safety")', module=(AC, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO,
            extra='nearly all substantive work is in the hypotheses (consistently signed and routed interfaces, subsystem-assumption satisfaction, joint shared-control feasibility, nonblocking hybrid event composition); the paper-time formal sources are A001 Theorem 16.1 (restricted composition) and the A002 contract framework'),
    11: dict(kind='proposition verified in source §8 (no sign-free delay conclusion: the scalar systems xdot=−ax−bx(t−τ) and xdot=−ax+bx(t−τ), a,b>0, have different feedback signs and different stability properties)', module=(ND, 'confirmed'), mapping=(CO, 'confirmed'), evidence=SCR,
            extra='valid non-universality statement; no proof environment — the two sign-contrast systems are named in the statement; explicit parameter examples desirable (the evaluation\'s note); non-universality only — not an analysis of a particular sampled institution, distributed delay, non-minimum-phase plant, or ecological system (the source\'s own remark)'),
    12: dict(kind='remark/template verified in source §7 (robust information value V_T^I = sup inf min q under well-posedness; the refinement difference is a safety-margin value of information)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SCR,
            extra='attainment/closure caveat preserved: a nonnegative value is equivalent to finite-horizon robust safety only when the supremum is attained or the relevant viability closure is used; safety-margin value of information, not an entropy metric'),
    13: dict(kind='remark/template verified in source §7 (informational recovery: a strategy keeps the trajectory in the emergency envelope E_X until T and reaches (B_T,h_T) ∈ K_∞)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SCR,
            extra='physical recoverability does not imply institutional recoverability (the viable-information-state requirement) — the template\'s preserved content; destination Paper 5 consistent with the CC-A001-013 information-monotonicity-of-recovery precedent'),
    14: dict(kind='remark/template verified in source §7 (safe learning: an action is safely informative only if tube-safe and contracting a declared belief-size functional for every compatible observation branch)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=CRO,
            extra='module corrected to observation_governance_empirics (intake: formal_foundations) by cross-source family consistency: belief/learning objects are the CC-A001-006 information-contraction and CC-A001-094 adaptive-learning families (observation_governance_empirics); a domain-specific dual-control problem — learning is not presumed harmless; destination Paper 2 unchanged'),
    15: dict(kind='remark verified in source §7 (normative monotonicity: C_X(λ1)⊆C_X(λ2) and A(·;λ1)⊆A(·;λ2) give nested viability kernels in the same direction under aligned dynamics/information/uncertainty)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SCR,
            extra='valid monotonicity result; exposes feasibility consequences of normative choices without purporting to derive or justify them (the source\'s own scope discipline)'),
    16: dict(kind='conjecture verified in source §8 (unnumbered paragraph: persistence of a reduced hybrid/RFDE nonlinear transition requires well-posed semiflow, fast difference-operator contractivity, spectral separation, center-manifold reduction, transverse Poincaré-map conditions, regular coupling, and preservation of material feasibility and safety)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO,
            extra='merge with the A002–A003 conjecture programme with class-specific conditions (the evaluation\'s instruction); fast difference-operator contractivity applies to particular neutral/difference formulations and is not a universal RFDE condition; the fold-orbit normal-hyperbolicity caveat (transversely but not on the fold orbit itself) preserved; module/destination consistent with the A002 conjecture rows CC-A002-042/-043/-044 (nonlinear_dynamics, Paper 4)'),
}


def module_verdict_str(v: tuple[str, str], intake_module: str) -> str:
    val, verdict = v
    if verdict == 'confirmed':
        return f'module {val} confirmed'
    return f'module {val} corrected (intake: {intake_module})'


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
        if not row['concordance_id'].startswith('CC-A006-'):
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

        parts = [f'Row-closed {DATE} (A006 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A006 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53 + 24 + 16, f'expected 192 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
