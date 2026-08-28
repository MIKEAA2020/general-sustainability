#!/usr/bin/env python3
"""Scientific row-closure pass for source A004 (uploads/Paper_IV_Phosphorus_Agriculture_Module.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, A016, and A010 passes in the same campaign). The full
source (*Phosphorus, Agriculture, and Catchment Safety: A Multi-Scale
Material-Service-Institution Module*, 94 lines) was read in full; the three
A004 rows are the competing model set of §7 (the identification ladder
H0/H1/H2); the evaluation record ("a strong domain-instantiation template...
valid as a domain module specification and falsification protocol, not yet
as a standalone phosphorus research paper") and the inventory's own
"Unverified components" note (no constitutive flux laws, parameter values,
trade matrices, observation likelihoods, thresholds, theorems, or empirical
tests supplied) are the verification witnesses.

A004-specific findings:

1. NO intake row corruptions; NO destination corrections (the domain
   template rides Paper 3 per the architecture's domain-paper rule: "Until
   then their valid theory/examples belong in Papers 1, 3, and 5").

2. THREE module classifications (A004 unclassified 3 -> 0), all to
   observation_governance_empirics (the H0/H1/H2 competing-model ladder is
   the identification discipline: "The more complex model is supported only
   by improved held-out prediction, calibrated uncertainty, safety-boundary
   relevance, or a demonstrated decision advantage"). THREE mapping
   classifications (UNRESOLVED -> EXACT_SPECIALIZATION: the model-class
   definitions instantiate the canonical comparator-class types).

3. REGISTERED TEMPLATE OBLIGATIONS, not discharged content: the module is a
   falsifiable specification — the moiety condition l_P^T S_P = 0, the
   functional-state/service maps, the safety and action correspondences, the
   compatible-state set, and the falsification protocol are architectural
   objects awaiting calibration; the inventory's corrections recorded (the
   undefined chi component; the overloaded R symbol for the rights/burden
   operator); the identification discipline recorded (process, parameter,
   observation, reporting, structural-discrepancy, trade-leakage, and
   implementation uncertainty distinguished; "A fitted residual may not be
   silently assigned to recovery, erosion, unreported trade, or soil
   immobilization").

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
DSO = 'defined_source_object'

V: dict[int, dict] = {
    1: dict(kind='competing-model-class definition verified in source §7 (H0: the aggregate regional phosphorus balance — the null comparator of the identification ladder; supported over H1/H2 only if the more complex models fail to improve held-out prediction, calibrated uncertainty, safety-boundary relevance, or decision advantage)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (the competing-model ladder is the identification discipline); destination Paper 3 confirmed (the domain template rides Paper 3 per the architecture\'s domain-paper rule); REGISTERED TEMPLATE OBLIGATION — no constitutive content supplied in the source'),
    2: dict(kind='competing-model-class definition verified in source §7 (H1: the multi-compartment regional/catchment model — the typed moiety ledger r_P with the extraction, regional, and catchment layers linked by the trade and land-routing interfaces)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; the displacement discipline recorded (a regional safety claim must check exported phosphorus burden through imports, trade, waste shipment, or feed supply); cite with the A005 physical-hypothesis ladder at the Paper 3 identification seam'),
    3: dict(kind='competing-model-class definition verified in source §7 (H2: the spatial trade-network/catchment model — trade and transport as explicit matrices/correspondences with sign, units, delay, ownership, and boundary status declared at every interface)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; the compositional-certificate conditions recorded (interface assumptions, shared-control compatibility, and nonblocking institutional events); the falsification protocol recorded (the module is falsified as a necessary architecture if simpler models predict held-out outcomes equally well with equal or better calibrated uncertainty — "the architecture must be narrowed")'),
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
        if not row['concordance_id'].startswith('CC-A004-'):
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

        parts = [f'Row-closed {DATE} (A004 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A004 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 320 + 3, f'expected 323 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
