#!/usr/bin/env python3
"""Scientific row-closure pass for source A014 (uploads/paper1_final.md).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, and A012 passes. The full source (*Northern Cod (NAFO 2J3KL): A
Present-Tense Test of Strong Depensation*, 272 lines) was read in full; every
inventoried item was located in the source; for each of the 15 A014 rows this
pass verifies item existence, kind, the audit status recorded in the
programme evaluation (the A014-L1..L10 defect list is the verification
witness), the canonical module, the primary mapping type per TCS-1.0 §7, and
the proof/evidence status. The committed corrected article
(revised_articles/A014_northern_cod_revised.md) was read alongside: it
implements the scalar-autonomous phase-line obstruction (Proposition 1, with
proof), the conditional extra-loss shift (Proposition 2, with the
existence/production-maximum conditions), the exact SAR table, the governance
timing restraint, and the reproduction-obligations register.

A014-specific findings:

1. NO intake row corruptions: all 15 rows quote-check cleanly against the
   per-claim inventory table (the case-source format: claim/object with
   submitted and audit statuses).

2. THIRTEEN module classifications (A014 unclassified 13 -> 0) and THIRTEEN
   mapping classifications — all to observation_governance_empirics: the
   monograph chapters of every non-docket A014 row already read "Observation,
   governance, and identification", and the architecture lists the corrected
   cod case among Paper 5's sources. The case is kept as ONE canonical unit
   (model + propositions + data + interpretation all in the case module) —
   the A011 empirical-source pattern; no named-delay-system seam exists here
   (the case model is a non-delay scalar ODE), so no nonlinear_dynamics row.

3. TWO mapping-type classifications to COUNTEREXAMPLE_OR_LIMIT (CC-A014-003
   and -004): the fixed-autonomous-scalar incompatibility and the
   replaced-by-theorem trichotomy are failure-boundary results of the case's
   model class (the A001 counterexample-family mapping precedent).

4. NO module, mapping, or destination corrections, and NO intake
   corruptions: the destinations verify row by row (Paper 5 for the case
   content; the conditional docket for the unreproduced/not-established
   items; the negative/counterexample register for the institutional-margins
   row whose formulas/provenance/timing are invalid or absent).

5. The upload's defects are real and the corrections are committed:
   (a) A014-L1 autonomy mismatch — the displayed model contains C(t), so it
   is NOT autonomous when removals vary; the corrected article states the
   obstruction for fixed removals/constant forcing (Proposition 1) and the
   paper's scope line says "fixed removals"; (b) A014-L2 — the trichotomy's
   "should have climbed far" overstates finite-time behavior (convergence can
   be arbitrarily slow near degeneracy; the reliable contradiction is
   repeated direction reversal); the corrected Proposition 1 is the
   stronger-and-narrower replacement ("exact trajectories, not noisy
   estimates or forced systems"); (c) A014-L3 — the threshold-shift lemma
   requires the existence/production-maximum conditions; corrected as
   Proposition 2 (the effective threshold is conditional on the modified
   equilibria existing — an "effective threshold" is not automatically a
   shifted structural parameter); (d) A014-L4 — the M-pulse causal claim is
   demoted to NCAM-formulation attribution; (e) A014-L5/L6 — the Δτ_gov=-1
   timing inference is removed (annual SSB cannot date a within-year
   crossing; fast does not imply adequate); (f) A014-L7 — the constrained-M
   values, C/π₀ ratios, and institutional margins are unreproduced and
   registered as reproduction obligations (hypotheses, not results).

6. The A016 bridge row (CC-A014-014) keeps its Paper 5 destination with the
   bridge obligation recorded (the archived Statistics Canada table query and
   population mapping required before the 43-CSD social values join A016's
   adaptive-capacity material).

Same honest boundary: content-level acceptance only; no claim status promoted
(the "SETTLED/CONFIRMED" author labels are replaced by the audit statuses;
the discriminants stay untested/exploratory; the docket rows stay open); the
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

OG = 'observation_governance_empirics'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
SSE = 'source_specific_empirical_status_check_required'
CRO = 'conditional_or_open'
SCR = 'status_crosswalk_required'
PI = 'proof_inventory_present_line_check_required'

V: dict[int, dict] = {
    1: dict(kind='case constitutive model verified in source §3.0 (the strong-Allee surplus equation dS/dt = rS(1-S/K)(S-s)/(K-s) - C(t) with SSB S, growth r, carrying capacity K, unstable threshold s, removals C; typed claim U1 "constitutive assumption, stands"; U2 records Schaefer as the Allee-factor-1 specialization)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='retained as an illustrative constitutive model, not a fit; the A014-L1 autonomy defect recorded: the displayed model contains C(t) and is NOT autonomous when removals vary — the corrected article states the obstruction class as one-dimensional autonomous with fixed parameters and fixed removals'),
    2: dict(kind='corrected proposition verified in source §3.0 (the extra-loss threshold-shift lemma: if C>0 or M_x>0 the effective threshold s_eff > s)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO,
            extra='conditional per the audit (A014-L3): the shift holds only when the modified positive equilibria exist and the loss lies below the relevant production maximum — larger losses eliminate the positive basin entirely; the corrected article states this as Proposition 2 (the conditional form, with the coalescence/disappearance case and the per-capita analog); an "effective threshold" is not automatically a shifted structural parameter'),
    3: dict(kind='antitheorem/case result verified in source §3.1 (any autonomous fixed-(r,K,s) version is incompatible with the non-monotonic post-moratorium trajectory: the three-row trichotomy table with the rising-and-falling series)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=SSE, cite=True,
            extra='mapping classified COUNTEREXAMPLE_OR_LIMIT — an incompatibility/failure-boundary result of the case model class; retained AFTER the exact-trajectory/autonomy restatement (A014-L1) and the finite-time restatement (A014-L2: convergence toward K can be arbitrarily slow near degeneracy — the reliable contradiction is repeated direction reversal, not failure to reach an unspecified biomass by an unspecified deadline); the obstruction must be separated from rejection under measurement error, process noise, age structure, migration, time-varying mortality, and state-space observation models (A014-L9)'),
    4: dict(kind='corrected proof replacing the source §3.1 trichotomy (the three threshold locations "prove rejection" claim)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=PI,
            extra='the upload\'s finite-time branch is overclaimed; the replacement is the corrected article\'s Proposition 1 (scalar-autonomous phase-line obstruction, WITH PROOF: a nonconstant solution of a locally Lipschitz scalar autonomous ODE is monotone between equilibria and cannot cross an equilibrium in either direction, so an exact path repeatedly rising and falling across a common interval is incompatible with one fixed scalar autonomous model) — "stronger and cleaner than a threshold-location trichotomy, and narrower: exact trajectories, not noisy estimates or forced systems"'),
    5: dict(kind='research task registered from source §3.2 (the resistance-landscape check: the claim that the trichotomy survives surplus-production/Allee, catch-accounting, and delay-difference frames)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='unsupported without explicit alternative models and calculations (the audit verdict on the "CONFIRMED" author label): each alternative frame requires its own displayed model and calculation; registered on the conditional docket as an open robustness obligation, not a completed check'),
    6: dict(kind='empirical table verified in source §4.1 (DFO CSAS SAR 2016/026 Table A2 SSB and M values: 1991-1995 SSB 735/382/101/31/10 kt with M 1.002/2.214/2.575/2.331/0.288 yr^-1; the crash-window M 2.2-2.6 roughly ten times pre-collapse levels)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE, cite=True,
            extra='verified as rounded source values by the evaluation (exact values 381.95/101.05/30.55 kt etc.); the survival column is exp(-M) after rounding — a transformation of the reported instantaneous M estimate, not an independently observed survival series; the corrected article carries the fuller exact-value 1991-2015 table'),
    7: dict(kind='model comparison verified in source §4.1 and §5 (the M-pulse interpretation of the crash: "M-pulse dominates the crash")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='demoted to NCAM-formulation attribution (A014-L4): NCAM M is an estimated unobserved-death component conditional on model structure, and DFO framework proceedings explicitly caution that unreported fishing deaths may enter de-facto M; the corrected statement is "the NCAM M-shift formulation allocates most estimated mortality to M"; the crash interpretation is formulation-dependent (the constrained-M formulation attributes it to unreported catch)'),
    8: dict(kind='case synthesis verified in source §4.4 (the two-window split: the exact data splits the phenomenon into two events — the crash interpretation is formulation-dependent, the non-recovery is unexplained in both formulations)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='retained as a useful descriptive partition; THE POSITIVE RESULT IS THE SPLIT, NOT A NEW MECHANISM (the source\'s own abstract and conclusion); the non-recovery window 1996-2004 remains unexplained (residual catch first-order at low biomass; weak depensation live; predator pit and assessment bias untested)'),
    9: dict(kind='computational object registered from source §5.1 (the constrained-M experiment: crash-window M=0.46, F=1.37 with unreported catch 257.8 kt/yr = 102.5% of mean SSB; non-recovery M=0.43, F=0.25 with 3.7 kt/yr)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='UNREPRODUCED (A014-L7): the constrained-M values, the 257.8 kt/yr estimate, and the 102.5% ratio require equations, source series, code, units, windows, and uncertainty; the corrected article registers them as hypotheses/reproduction targets, not results; the docket obligation is the registered reproduction package'),
    10: dict(kind='background-only content verified in source §5.2 (the Tam & Bundy 2019 ecosystem context: harp seal biomass 49,600 t -> 161,183 t, a 3.2x increase; capelin biomass 13.77 -> 4.97 t/km^2, a 64% decline)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='partially source-consistent, causal use unverified (A014-L8): the values are descriptive mass-balance inputs, not causal tests; "predator pit not supported" and "no capelin correlation" require a defined estimator, interval, lag structure, and uncertainty — kept untested/exploratory until reproduced'),
    11: dict(kind='open hypothesis registered from source §6 (discriminant D3: predator pit rejected — "no capelin correlation")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO,
            extra='NOT ESTABLISHED: the discriminant-table check/cross labels are author statuses; D3 requires the defined estimator and uncertainty analysis before it discriminates anything; docket row — the negative verdict is itself the open obligation'),
    12: dict(kind='open hypothesis registered from source §6 (discriminant D5: weak depensation live — per-capita surplus positive; with D1 residual catch C/pi_0 >= 1 at S=22-30 kt)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO,
            extra='requires a definition and an estimator before the "LIVE" status discriminates; the C/pi_0 ratios are unreproduced (the A014-L7 obligation); docket row'),
    13: dict(kind='negative-register content verified in source §7.1 (the institutional margins table: delta-tau_gov = -1 yr "PERVERSE (fast response)", M_act = +14.9 kt/yr, M_legit = -474 kt, "2 of 3 margins perverse")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='formulas/provenance and timing invalid or absent (A014-L5/L6/L7): the delta-tau_gov=-1 one-year lead cannot be inferred from an annual SSB estimate (removed in the corrected article — no governance lead is inferred); fast response does not establish adequacy; M_act and M_legit are unreproduced; the RETAINED verified facts are the 2 July 1992 moratorium announcement and the 26 June 2024 reopening with TAC 18 kt as decision events for prospective analysis'),
    14: dict(kind='A016 bridge registered from source §7.2 (the B6 data collection: 43 NL fishing-dependent CSDs, Statistics Canada 38-10-0167-01; income from fishing 32.2% in 2016 to 25.6% in 2021; DFO licence/landing data needing a NAFO STATLANT filter)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SCR,
            extra='requires the archived table query and population mapping before the social values join A016\'s adaptive-capacity material; the bridge itself is the registered obligation — kept at Paper 5 with the cross-reference to the A016 row family'),
    15: dict(kind='supplement verified in source Appendix (the minimal-embarrassment test: the four toy simulations — Schaefer growth from 1.2e5, below-threshold decay to 0, above-threshold convergence to K, and the below-threshold monotone/no-pulse check at C=3e3)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE,
            extra='executed successfully per the evaluation (verified item 4) and rerun in the corrected article; confirms only that the selected parameterized toy trajectories behave as expected — does not fit Northern cod and does not validate the constrained-M experiment'),
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
        if not row['concordance_id'].startswith('CC-A014-'):
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

        parts = [f'Row-closed {DATE} (A014 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A014 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53 + 24 + 16 + 14 + 15, f'expected 221 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
