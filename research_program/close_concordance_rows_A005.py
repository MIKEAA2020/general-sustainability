#!/usr/bin/env python3
"""Scientific row-closure pass for source A005 (uploads/Paper_III_Groundwater_Module.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, A016, A010, and A004 passes in the same campaign). The
full source (*Groundwater Governability under Partial Observation: A Typed
Hybrid Material-Institution Module*, 117 lines) was read in full; the six
A005 rows are the competing physical hypotheses (H0/H1/H2) and the competing
institutional hypotheses of the identification programme; the evaluation
record ("a sound groundwater-domain architecture... not a calibrated basin
model and contains no theorem, numerical result, viability kernel, or
empirical validation") and the inventory's own "Unverified components" note
are the verification witnesses.

A005-specific findings:

1. NO intake row corruptions; NO destination corrections (the domain
   template rides Paper 3 per the architecture's domain-paper rule; the
   institutional-hypothesis H3 twin rides Paper 2 with CC-A003-003).

2. FIVE module classifications (A005 unclassified 5 -> 0), all to
   observation_governance_empirics (the physical and institutional
   hypothesis ladders are the identification discipline — "The two-pool
   hypothesis is supported only if it improves held-out state/service/safety
   prediction or gives demonstrably better calibrated uncertainty"; "No
   generic delay parameter is interpreted as an institutional lag without
   dated evidence of observation, assessment, authorization, implementation,
   and enforcement").

3. ONE module correction: CC-A005-003 (the H2 distributed/higher-
   dimensional groundwater model) ledger_diagnostics ->
   observation_governance_empirics — the competing-model ladder is ONE
   identification object (the same H0/H1/H2 family as -001/-002 and the
   A004 ladder); splitting its modules would split the ladder. ONE evidence
   kind-correction on the same row: source_specific_empirical_status_
   check_required -> defined_source_object (a hypothesis-class definition,
   not an empirical record — the intake had typed only this row of the
   ladder as empirical).

4. ONE module correction on CC-A005-006 (the inertia/capture/state-dependent
   institutional hypothesis): formal_foundations -> observation_governance_
   empirics — the same A001-closure precedent applied to CC-A003-003 this
   campaign (the implementation-operator response family is the governance
   chain, not a viability-kernel result); its Paper 2 destination is
   CONFIRMED (the H3 twin joins CC-A003-003 in the atlas's institutional-
   implementation family).

5. REGISTERED TEMPLATE OBLIGATIONS, not discharged content: the source is a
   falsifiable specification (no named basin, data, parameters, thresholds,
   constitutive recharge/leakage/solute functions, observation likelihood,
   policy class, kernel, or numerical result supplied); the evaluation
   record's corrections recorded (donor-limited leakage, compartment-
   specific solute accounting, the unused release control, compatible-state
   topology, structural discrepancy in material coordinates, storage as a
   constitutive function of head rather than a duplicate state); the
   governability thesis recorded ("a basin may improve physically yet
   remain outside an implementable viability kernel because state
   uncertainty, authority, compliance, or review constraints prevent a safe
   policy").

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
    1: dict(kind='competing-physical-hypothesis definition verified in source §7 (H0: one-pool storage — the null comparator of the physical identification ladder)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (the hypothesis ladder is the identification discipline); destination Paper 3 confirmed (the domain template rides Paper 3); REGISTERED TEMPLATE OBLIGATION — no constitutive content supplied'),
    2: dict(kind='competing-physical-hypothesis definition verified in source §7 (H1: fast/slow two-pool storage with bidirectional leakage — "a falsifiable competing physical hypothesis, not a universal ontology"; supported only by improved held-out state/service/safety prediction or demonstrably better calibrated uncertainty)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; the two-pool logic joins the A018 diagnostics at the Paper 3 seam; cite with the A004 physical-hypothesis ladder'),
    3: dict(kind='competing-physical-hypothesis definition verified in source §7 (H2: a justified distributed or higher-dimensional groundwater model)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module corrected ledger_diagnostics → observation_governance_empirics (the competing-model ladder is ONE identification object — the same H0/H1/H2 family as -001/-002 and the A004 ladder; splitting its modules would split the ladder); evidence kind-corrected to defined_source_object (a hypothesis-class definition, not an empirical record); destination Paper 3 confirmed'),
    4: dict(kind='competing-institutional-hypothesis definition verified in source §7 (scarcity-amplifying extraction — the groundwater-module restatement of the A003 H1 response-sign taxonomy; "No generic delay parameter is interpreted as an institutional lag without dated evidence of observation, assessment, authorization, implementation, and enforcement")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; destination Paper 3 confirmed (the domain template\'s institutional ladder); cite with CC-A003-001 (the H1 statement whose named instantiation rides Paper 4) at the seam'),
    5: dict(kind='competing-institutional-hypothesis definition verified in source §7 (protective restraint/restoration — the groundwater-module restatement of the A003 H2 response-sign taxonomy)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; destination Paper 3 confirmed; cite with CC-A003-002 at the seam'),
    6: dict(kind='competing-institutional-hypothesis definition verified in source §7 (inertia/capture/state-dependent action — the groundwater-module restatement of the A003 H3 response-sign taxonomy)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module corrected formal_foundations → observation_governance_empirics (the same A001-closure precedent applied to CC-A003-003 this campaign: the implementation-operator response family is the governance chain, not a viability-kernel result); destination Paper 2 CONFIRMED (the H3 twin joins CC-A003-003 in the atlas\'s institutional-implementation family); cite at the seam'),
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
        if not row['concordance_id'].startswith('CC-A005-'):
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

        parts = [f'Row-closed {DATE} (A005 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A005 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 323 + 6, f'expected 329 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
