#!/usr/bin/env python3
"""Scientific row-closure pass for source A017 (uploads/paper4_final.md).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, A016, A010, A004, A005, A025, and A007 passes in the same
campaign). The full source (*The Institutional Solvency Index Does Not Work:
A Negative Result*, 111 lines) was read in full; every inventoried item was
located in the source; the verification witness is the inventory's own audit
status column (Retain / Retain subject to archived recalculation / Reject /
Unreproduced / Not merited) — this is a NEGATIVE-RESULT source, so closure
verifies each item AT ITS AUDITED STATUS, including the two rows whose
claims the audit itself REJECTS (-005 the universal margin failure, -006
the biological-collapse causal claim).

A017-specific findings:

1. NO intake row corruptions; NO destination corrections (all ten rows are
   the negative/counterexample register — the rejection record of A008's
   solvency index and of the institutional-margins replacement).

2. EIGHT module classifications (A017 unclassified 8 -> 0), all to
   observation_governance_empirics (the institutional-metric rejection
   content: the dimensional contradiction, the arithmetic audit, the
   dollars-not-exergy antitheorem, the two rejected overclaims, the NCAM
   values, and the constrained-M table are all the institutional-
   performance-metric family); the two intake OG classifications (-004,
   -009) confirmed. EIGHT mapping classifications (UNRESOLVED -> resolved;
   the rejection/witness rows COUNTEREXAMPLE_OR_LIMIT, the values records
   EXACT_SPECIALIZATION).

3. The rejection discipline is the content: the solvency index alpha =
   Omega_c * tau_d fails on its own terms (dimensionally contradictory,
   arithmetically wrong by 1000x in 5 of 7 rows, conceptually confused —
   dollars labeled as exergy with no joule appearing — and structurally
   perverse: the collapsed Northern cod fishery scores as most "solvent");
   the replacement institutional margins also fail (2 of 3 perverse: dtau_gov
   = -1 yr and M_act = +14.9 kt/yr for the collapsed case; only M_legit =
   -474 kt consistent); the universal-failure claim and the biological-
   collapse causal claim are REJECTED at exactly their audited scope; the
   surviving components (B6 as tagged value premise, non-aggregation logic,
   locked PIP income, the acknowledged gap) are the A016 bridge; and the
   closing lesson recorded verbatim ("The exact data did not replace a bad
   institutional theory with a good biological theory. They split the
   phenomenon and demoted every master variable the program has proposed.
   That split IS the positive result.").

4. REGISTERED OBLIGATIONS retained: the arithmetic-error audit is subject
   to archived recalculation (-002); the constrained-M table is
   unreproduced (-008, the A014 computational queue); the crash
   interpretation is formulation-dependent (-007: NCAM M-shift vs
   constrained-M, dtau_gov = -1 yr, M_act = +14.9 kt/yr, unreported catch
   257.8 kt/yr = 102.5% of mean SSB under constrained M — the ecosystem
   context: harp seal biomass 3.2x, capelin -64%).

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
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSE = 'source_specific_empirical_status_check_required'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='rejection record verified in source §1 (the dimensional contradiction in the A008 solvency index alpha = Omega_c * tau_d: declared both "dimensionless" AND "units of time")', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified observation_governance_empirics (the institutional-metric rejection family); the A008 rejection record — cite together with the A008 adjudicated-rejected rows; destination negative/counterexample register confirmed'),
    2: dict(kind='arithmetic audit record verified in source §1 (the original arithmetic errors: 5 of 7 rows off by 1000x — NW Atlantic cod formula alpha = 200 yr vs reported 0.20 yr; NOAA Fisheries 1.2 yr vs 0.001; DFO Canada 1.6 yr vs 0.0016; IBAMA 0.35 yr vs 0.00035)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=SSE, cite=True,
            extra='module classified observation_governance_empirics; RETAIN SUBJECT TO ARCHIVED RECALCULATION status preserved (the audit supplement obligation — the recalculation archive pending, per the source registry\'s own status); destination negative/counterexample register confirmed'),
    3: dict(kind='antitheorem verified in source §1 (dollars are not exergy: the A008 index labels dollar values as exergy with no joule appearing — the typed-units violation)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified observation_governance_empirics; the antitheorem joins the A016 U3 identity ("PIP dollars are not exergy") and the A010/A002 exergy-programme typing discipline at the units seam; destination negative/counterexample register confirmed'),
    4: dict(kind='construct-validity counterexample verified in source §1 (the perverse case ordering: the collapsed Northern cod fishery scores as the MOST "solvent" under the index — the structural perversity that alone defeats the construct)', module=(OG, 'confirmed'), mapping=(CO, 'confirmed'), evidence=PI, cite=True,
            extra='the construct-validity counterexample is the rejection\'s load-bearing evidence; cite together with the A014 cod rows (the same case) at the negative-register seam'),
    5: dict(kind='scoped rejection verified in source §2.1 (the replacement institutional margins: exact CSAS SAR 2016/026 Table A2 data give dtau_gov = -1 yr PERVERSE, M_act = +14.9 kt/yr PERVERSE, M_legit = -474 kt CONSISTENT — 2 of 3 margins perverse; the audit REJECTS the universal claim: only the tested signs/case may fail)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=SSE, cite=True,
            extra='module classified observation_governance_empirics; the REJECT-UNIVERSAL/RETAIN-CASED discipline is the row\'s content — the margins fail for the tested collapsed case, and no universal failure claim is admitted; destination negative/counterexample register confirmed'),
    6: dict(kind='causal-overclaim rejection verified in source §2.2 and §3.3 (the "The Collapse Was Biological" claim REJECTED AS CAUSAL OVERCLAIM per the audit: the crash interpretation is formulation-dependent — the two-window split of the A014 case governs; "The exact data did not replace a bad institutional theory with a good biological theory. They split the phenomenon and demoted every master variable the program has proposed. That split IS the positive result.")', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified observation_governance_empirics; the rejection recorded at its audited scope — the collapse-interpretation claim stays formulation-dependent (the A014 two-window split rows carry the governing discipline); destination negative/counterexample register confirmed'),
    7: dict(kind='model-comparison values record verified in source §2.2 and §3.1 (the NCAM values: the crash-window Table A2 M values 2.214/2.575/2.331 for 1992-1994 — M roughly 10x higher during the collapse than before or after; the two-window NCAM vs constrained-M comparison: crash M = 1.68, F = 0.14 vs constrained M = 0.46, F = 1.37; non-recovery M = 0.56, F = 0.11 vs M = 0.43, F = 0.25)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True,
            extra='module classified observation_governance_empirics; SOURCE VALUES PARTLY VERIFIED, INTERPRETATION CONDITIONAL status preserved — cite together with the A014 model-comparison rows (the same case\'s governing record) at the seam; destination negative/counterexample register confirmed'),
    8: dict(kind='computational record verified in source §3.1 and §3.3 (the constrained-M table: the constrained-M model requires implausible unreported catch 257.8 kt/yr = 102.5% of mean SSB in the crash window vs 3.7 kt/yr in the non-recovery window; the ecosystem context: harp seal biomass 49,600 t -> 161,183 t (3.2x) and capelin 13.77 -> 4.97 t/km^2 (-64%) between 1985-87 and 2013-15)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='module classified observation_governance_empirics; UNREPRODUCED status preserved (the A014 computational queue — the reproduction obligation rides the A014 case record); destination negative/counterexample register confirmed'),
    9: dict(kind='redesign decision record verified in source §5 (no corrected master scalar: "Do not replace with a corrected scalar — the program unanimously rejected master scalars"; the surviving components — B6 as tagged value premise, non-aggregation logic with component margins, locked World Bank PIP income queries, the acknowledged gap as research queue not to be filled with 0-1 scores)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='the no-master-scalar decision instantiates the typed redesign rule exactly; the surviving components are the A016 bridge (cite CC-A016-001/-004/-012 at the seam); destination negative/counterexample register confirmed'),
    10: dict(kind='publication-decision record verified in source §1 and the inventory (the standalone negative paper NOT MERITED PRESENTLY: the record rides the archive/flagship lesson — the A008/A017 negative material belongs to the negative register and the flagship\'s negative-results section, not a separate paper)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; the minimum-paper rule applied to the negative record itself; destination negative/counterexample register confirmed'),
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
        if not row['concordance_id'].startswith('CC-A017-'):
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

        parts = [f'Row-closed {DATE} (A017 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A017 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 344 + 10, f'expected 354 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
