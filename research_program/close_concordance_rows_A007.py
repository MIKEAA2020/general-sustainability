#!/usr/bin/env python3
"""Scientific row-closure pass for source A007 (uploads/Paper_I_Hybrid_Sustainability_Architecture_V4.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, A016, A010, A004, A005, and A025 passes in the same
campaign). The full source (*A Hybrid Sustainability-Systems Architecture*,
170 lines) was read in full; the two A007 rows are the two static lemmas of
§7 (the compensatory reporting limit and the static diagnostic aliasing);
the evaluation record's verified-structure list (the architecture's
separations and admission standard) and its two critical state-space
inconsistencies (which do not touch the two static lemmas) are the
verification witnesses.

A007-specific findings:

1. NO intake row corruptions; NO destination corrections (both lemmas ride
   Paper 2's atlas families: the noncompensation family and the
   observation-limits family).

2. ONE mapping-type correction: CC-A007-001 (the compensatory reporting
   limit) APPROXIMATION -> COUNTEREXAMPLE_OR_LIMIT. The lemma is the
   two-coordinate witness-construction family — the same logical content as
   CC-A018-001 / CC-A013-001 / CC-A016-004 (the noncompensation family),
   classified COUNTEREXAMPLE_OR_LIMIT by the A018 and A013 passes this
   campaign and before. ONE module classification on the same row ->
   formal_foundations. ONE module + mapping classification on CC-A007-002
   (the static diagnostic aliasing) -> observation_governance_empirics /
   COUNTEREXAMPLE_OR_LIMIT: the aliasing lemma is the memoryless-classifier
   impossibility twin of the observation-fibre certification family
   (CC-A010-001), and boundary content.

3. The source's own status discipline preserved: the aliasing lemma's
   remark ("The latter lemma does not establish dynamic unobservability.
   Observer/filter/set-membership claims require dynamic observability/
   detectability, error, and structural-discrepancy conditions") rides the
   row; the noncompensatory-form discipline ("a scalar certificate may be
   used only in noncompensatory form, e.g. q(X,u) = min_i m_i(X,u); weighted
   summaries may report preferences but do not certify componentwise safety
   without a restricted-domain proof") rides the -001 note; the evaluation
   record's supersession status recorded (A007 is the concise predecessor
   of A002's architecture; the two lemmas survive in the atlas's families).

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
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'

V: dict[int, dict] = {
    1: dict(kind='lemma verified in source §7 (the compensatory reporting limit: for unrestricted margins b in R^n, n >= 2, and w in R_{++}^n, w^T b > 0 does not imply b in R_+^n — the two-coordinate witness-construction family; §4\'s noncompensatory margin discipline: safety requires m in R_+^{q+p}, a scalar certificate only in noncompensatory form min_i m_i, weighted summaries report preferences but do not certify without a restricted-domain proof)', module=(FF, 'classified'), mapping=(CO, 'corrected'), evidence=PI, cite=True,
            extra='mapping corrected APPROXIMATION → COUNTEREXAMPLE_OR_LIMIT (intake: APPROXIMATION): the witness-construction family — the same logical content as CC-A018-001 / CC-A013-001 / CC-A016-004, all classified COUNTEREXAMPLE_OR_LIMIT; module classified formal_foundations (the noncompensation family); destination Paper 2 confirmed (the atlas\'s noncompensation family); cite the A018/A013 twins at the seam'),
    2: dict(kind='lemma verified in source §7 (the static diagnostic aliasing: if a safe and an unsafe point state have the same instantaneous observation, no memoryless deterministic classifier of that observation correctly classifies both; the remark preserves the scope — "The latter lemma does not establish dynamic unobservability. Observer/filter/set-membership claims require dynamic observability/detectability, error, and structural-discrepancy conditions")', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified observation_governance_empirics (the observation-limits family); mapping classified COUNTEREXAMPLE_OR_LIMIT (the memoryless-classifier impossibility — boundary content; the twin of the observation-fibre certification family CC-A010-001, which carries the positive iff characterization); destination Paper 2 confirmed (the atlas\'s observation and epistemic viability family); the dynamic-observability scope remark preserved verbatim'),
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
        if not row['concordance_id'].startswith('CC-A007-'):
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

        parts = [f'Row-closed {DATE} (A007 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A007 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 342 + 2, f'expected 344 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
