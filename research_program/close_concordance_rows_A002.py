#!/usr/bin/env python3
"""Scientific row-closure pass for source A002 (uploads/general_theory.txt).

Executed 2026-08-27, following the procedure established by the A001 pass
(research_program/close_concordance_rows_A001.py). The full source article
(*A Typed Flux-Observation-Governance Theory of Sustainability*) was read in
full; every inventoried item was located in the source; for each of the 53
A002 rows this pass verifies item existence, kind, proof presence (the
deferred line check), the canonical module, the primary mapping type per
TCS-1.0 §7, and the proof/evidence status — with special attention to the
source's own claim-status lines (the status{} macro), which self-declare
Theorem vs Conditional theorem and govern the evidence status where the
intake heuristic mis-fired.

A002-specific defect classes found and corrected here (beyond the A001
pattern): the intake keyword heuristic (i) read the substring 'open' inside
'clopen', mis-flagging two PROVED theorems (finite-clopen observation
knowledge kernel; finite-clopen inter-sample-safe knowledge kernel) as
conditional_or_open — both carry complete proofs and Theorem status lines in
the source; (ii) read 'limit' inside 'donor limitation', mis-mapping the
donor-limitation corollary (an exact sufficiency result) as APPROXIMATION;
(iii) flagged a definition (hybrid specialization data) with empirical-check
evidence. The restored repair row CC-A002-053 (the second untitled Remark —
the substitution-section remark on Farkas multipliers) is verified against
its source location.

Same honest boundary as A001: content-level acceptance only; no theorem
status promoted; the §8 interface contract remains open; the paper-time
citation match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-27'

FF = 'formal_foundations'
OG = 'observation_governance_empirics'
ND = 'nonlinear_dynamics'
LD = 'ledger_diagnostics'
AT = 'architecture_transformation_composition'
SE = 'stage_spatial_extension'
EX = 'EXACT_SPECIALIZATION'
CL = 'COUNTEREXAMPLE_OR_LIMIT'
PIC = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'

V: dict[int, dict] = {
    1: dict(kind='definition verified in source §2.1 (the typed physical state and moiety/unit typing)', module=(AT, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    2: dict(kind='definition verified in source §2.1 (hybrid specialization data: mode sets, phase spaces, jump rules, execution rule, observation map)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='evidence corrected to defined_source_object (intake had source_specific_empirical_status_check_required — this is a definition, not an empirical object)'),
    3: dict(kind='definition verified in source §2.1 (the canonical tuple S with its 13 slots)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    4: dict(kind='definition verified in source §2.1 (four uncertainty levels with quantifier discipline)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    5: dict(kind='definition verified in source §2.3 (five diagnostic claim types; the no-transfer rule)', module=(LD, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    6: dict(kind='definition verified in source §2.3 (threshold typing + the intergenerational recursive safety criterion)', module=(AT, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    7: dict(kind='proposition + proof verified in source §2 (unrestricted-compensation counterexample construction + the domain-certificate biconditional)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
            extra='the item is a rejection-within-characterization: the first half is an explicit deficit construction, the second the exact domain-certificate iff; both halves verified'),
    8: dict(kind='theorem + proof verified in source §3 (typed hybrid conservation under L^T S = 0, L^T S^J = 0)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    9: dict(kind='remark verified in source §3 (the moiety-scope note: one balance per moiety; no biomass+money+biodiversity+exergy scalar)', module=(LD, 'classified'), mapping=(EX, 'confirmed'), evidence=None,
            extra='interpretive scope note on the conservation theorem; no proof status to promote; the remark-to-§6-vocabulary crosswalk is a paper-time decision'),
    10: dict(kind='corollary + proof verified in source §3 (closed positive-moiety component bound)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    11: dict(kind='theorem + proof verified in source §3 (non-negative invariance across ordinary, hybrid, and RFDE modes; quasipositivity on C_τ; reset preservation)', module=(FF, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to formal_foundations (intake: nonlinear_dynamics) — the theorem is positive-cone invariance theory (the TCS §2.4 positivity principle); the RFDE case is one of three modes, not the subject'),
    12: dict(kind='corollary + proof verified in source §3 (donor-limited outflows and boundary flows suffice for the tangency condition)', module=(FF, 'corrected'), mapping=(EX, 'corrected'), evidence=None,
             extra='module corrected to formal_foundations (intake: ledger_diagnostics — kept with the invariance theorem, its parent); mapping corrected from APPROXIMATION: the intake keyword read "limit" inside "donor limitation" — the corollary is an EXACT sufficiency result, not an approximation'),
    13: dict(kind='conditional theorem + proof verified in source §3 (BIBS via coercive V, Dini dissipativity, non-expansive resets; the dot-x=u counterexample to weaker premises is in the status note)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    14: dict(kind='definition verified in source §4 (support provenance partition + directional support gap)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    15: dict(kind='theorem + proof verified in source §4 (Farkas linear substitution alternative; dual certificate)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    16: dict(kind='definition verified in source §5 (exact safety certifier)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None, cite=True,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — the certifier definition heads the observation-fibre family (with the criterion theorem and the safety-crossing corollary)'),
    17: dict(kind='theorem + proof verified in source §5 (observation-fibre criterion; the saturation identity)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    18: dict(kind='corollary + proof verified in source §5 (safety-crossing fibres obstruct exact certification; largest certainly-safe set)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — same family as the observation-fibre criterion'),
    19: dict(kind='definition verified in source §6 (three policy questions: actual-policy safety, viability, robust viability with the fixed quantifier order)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    20: dict(kind='definition verified in source §6 (capture basin, recoverability, policy-relative irreversibility — all five indices declared)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    21: dict(kind='theorem + proof verified in source §6.1 (sampled robust-viability kernel; compactness, finite-horizon iff, greatest invariant set)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    22: dict(kind='corollary + proof verified in source §6.1 (monotonicity under policy-set expansion, with the rebound caveat)', module=(OG, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    23: dict(kind='theorem + proof verified in source §6.2 (finite-clopen observation knowledge kernel — parts 1–4 incl. the injective-observation reduction; source status line: "Theorem, finite-clopen sampled observation model")', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PIC,
             extra='evidence corrected to proof_inventory_present_line_check_required (intake had conditional_or_open — the keyword heuristic read "open" inside "clopen"; the source declares a complete theorem with proof on the line)'),
    24: dict(kind='definition verified in source §6.3 (held-control tube predecessor with the exact W_h encoding caveat)', module=(OG, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    25: dict(kind='theorem + proof verified in source §6.3 (inter-sample-safe sampled kernel; source status line: "Theorem, restricted fixed-period full-state model")', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    26: dict(kind='theorem + proof verified in source §6.4 (finite-clopen inter-sample-safe knowledge kernel; source status line: "Theorem, finite-clopen fixed-period held model")', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PIC,
             extra='evidence corrected to proof_inventory_present_line_check_required (intake had conditional_or_open — the same "open"-in-"clopen" keyword false positive; the source declares a complete theorem with proof on the line)'),
    27: dict(kind='theorem + proof verified in source §6.5 (sampled RFDE finite-clopen knowledge kernel on the compact equi-Lipschitz history class; source status line: "Conditional theorem, compact single-delay history model")', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
             extra='conditional_or_open CONFIRMED as the source-declared status: the theorem environment carries a complete proof, but the source\'s own status line demotes it to conditional (the total jointly-continuous held-solution map and the compact history class are substantive hypotheses)'),
    28: dict(kind='conditional theorem + proof verified in source §6.6 (review-synchronised hybrid RFDE knowledge kernel with continuous phase-space reset; source status line: "Conditional theorem, review-clock hybrid RFDE")', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    29: dict(kind='proposition + proof verified in source §6.6 (outer semicontinuity does not close universal tube constraints — the explicit [0,1]-space counterexample at the grazing guard)', module=(FF, 'classified'), mapping=(CL, 'classified'), evidence=None,
             extra='the explicit construction is a counterexample establishing the OSC obstruction; classified COUNTEREXAMPLE_OR_LIMIT (intake: UNRESOLVED)'),
    30: dict(kind='conditional theorem + proof verified in source §6.6 (bounded-jump hybrid ODE kernel with Hausdorff-continuous exact tubes, full-state and finite-clopen versions; source status line: "Conditional theorem, continuous exact hybrid tubes")', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    31: dict(kind='remark verified in source §6.6 (accounting and boundedness on the restricted hybrids — the scope note gating the conservation/BIBS application)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None,
             extra='interpretive scope note riding the hybrid-kernel family; no proof status to promote'),
    32: dict(kind='definition verified in source §6.7 (compact sampled information model with exact latent tubes)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    33: dict(kind='theorem + proof verified in source §6.7 (restricted sampled information-state tube kernel; source status line: "Theorem, restricted compact information model")', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    34: dict(kind='conditional theorem + proof verified in source §7 (finite-time sample-and-hold convergence, O(h) global error; source status line: "Conditional theorem, finite-horizon consistency")', module=(OG, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    35: dict(kind='definition verified in source §8 (four model maps: specialisation, exact projection, approximation, singular reduction)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    36: dict(kind='theorem + proof verified in source §8 (projectability criterion: the Dp·F = G∘p semiconjugacy iff)', module=(FF, 'confirmed'), mapping=('PROJECTABLE_REDUCTION', 'confirmed'), evidence=None),
    37: dict(kind='corollary + proof verified in source §8 (fibre obstruction: unequal Dp·F on a fibre defeats any exact autonomous reduction)', module=(FF, 'classified'), mapping=(CL, 'confirmed'), evidence=None),
    38: dict(kind='theorem + proof verified in source §9 (support-saturated logistic stock limit: O(κ) Gronwall bound; source status line: "Theorem, partial reduction")', module=(LD, 'confirmed'), mapping=('APPROXIMATION', 'confirmed'), evidence=None,
             extra='APPROXIMATION confirmed as correct here — the result is a singular reduction with an explicit error bound, unlike the donor-limitation corollary'),
    39: dict(kind='theorem + proof verified in source §10 (logistic variance correction — an exact identity — plus the general C² curvature bound; source status line: "Theorem, static spatial aggregation")', module=(LD, 'confirmed'), mapping=('APPROXIMATION', 'confirmed'), evidence=None,
             extra='the variance/covariance correction is exact; the curvature bound is an explicit error bound — APPROXIMATION retained for the bound half, noted'),
    40: dict(kind='conditional theorem + proof verified in source §11 (local-horizon bracket under slow rate variation; source status line: "Conditional theorem, local diagnostic")', module=(LD, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    41: dict(kind='conditional theorem + proof verified in source §12 (small-gain delay-independent stability via Halanay; the unique decay rate; source status line: "Conditional theorem, sufficient certificate")', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    42: dict(kind='conjecture with declared missing-proof and disproof route verified in source §13 (periodic-orbit-fold persistence under typed coupling)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    43: dict(kind='conjecture with declared missing-proof and disproof route verified in source §13 (variable-time delayed-hybrid information kernel; two independent gaps documented)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    44: dict(kind='conjecture with declared missing-proof and disproof route verified in source §13 (restricted delay-separation principle)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    45: dict(kind='empirical hypothesis with test requirements verified in source §14 (observation aggregation)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    46: dict(kind='empirical hypothesis with test requirements verified in source §14 (governance phase ordering, with the frequency-domain identification caveat)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    47: dict(kind='empirical hypothesis with test requirements verified in source §14 (substitution certificate)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    48: dict(kind='research programme verified in source §15 (spatial, stage, and polycentric-agent closure — moment closures, agent-specific observation maps, network+delay stability, Erlang cascades)', module=(SE, 'classified'), mapping=(EX, 'classified'), evidence=None,
             extra='module classified stage_spatial_extension (the A022/A023 module this programme proposes to close); the Part VII crosswalk maps research-programme items to OPEN/SPECIFIED via the open-problems register'),
    49: dict(kind='research programme verified in source §15 (exergy, quality grades, and nonsmooth transformation feasibility)', module=(AT, 'confirmed'), mapping=('TRANSFORMATION', 'confirmed'), evidence=None),
    50: dict(kind='research programme verified in source §15 (justice and multiscale viability: group-indexed K, recursive intergenerational criterion, local-global kernel composition)', module=(AT, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to architecture_transformation_composition (intake: formal_foundations) — the programme is the normative/multiscale-composition extension (K\'s justice module + kernel composition), Paper 1 territory'),
    51: dict(kind='research programme verified in source §15 (model selection, minimality, and the limit lattice — commutation proofs or path-dependent counterexamples)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    52: dict(kind='research programme verified in source §15 (structural uncertainty, robustness, and quantitative detection risk)', module=(OG, 'classified'), mapping=('APPROXIMATION', 'confirmed'), evidence=None,
             extra='module classified observation_governance_empirics (the epistemic/robustness channel); the intake APPROXIMATION label is nominal for this prospective object — the substantive content is the module assignment; the Part VII crosswalk maps programme items to OPEN/SPECIFIED'),
    53: dict(kind='remark verified in source §4 (the substitution-section remark: Farkas multipliers are separation certificates, not universal exchange rates) — the 2026-08-26 machine-pass repair row restoring the second untitled Remark', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None,
             extra='the restored collision twin of the conservation remark (CC-A002-009); its identity as the SUBSTITUTION remark (after the Farkas theorem in §4) verified in the source; module classified formal_foundations, riding the substitution-feasibility family'),
}


def module_verdict_str(v: tuple[str, str], intake_module: str) -> str:
    val, verdict = v
    if verdict == 'confirmed':
        return f'module {val} confirmed'
    if verdict == 'classified':
        return f'module {val} classified (intake: unclassified)'
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
        if not row['concordance_id'].startswith('CC-A002-'):
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

        row['canonical_module'] = d['module'][0]
        row['primary_mapping'] = d['mapping'][0]
        row['mapping_status'] = 'accepted_mapping'
        if d.get('evidence'):
            row['proof_evidence_status'] = d['evidence']
        row['review_state'] = 'row_verified'

        parts = [f'Row-closed {DATE} (A002 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A002 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53, f'expected 152 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
