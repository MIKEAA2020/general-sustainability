#!/usr/bin/env python3
"""Scientific row-closure pass for source A016 (uploads/paper3_final.md).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, and A024 passes in the same campaign). The full source (*Who
Holds Adaptive Capacity*, 206 lines) was read in full; every inventoried
item was located in the source; for each of the 12 A016 rows this pass
verifies item existence, kind, the source's own status discipline (the typed
claim registry N1/N2/D1/D2/M1/E1/E2/C1 and U1-U7 graph; the evaluation
record's verified-items list and A016-L1..L9 correction register are the
verification witness), the canonical module, the primary mapping type per
TCS-1.0 §7, and the proof/evidence status.

A016-specific findings:

1. NO intake row corruptions: all 12 rows quote-check cleanly against the
   inventory table.

2. NO destination corrections: the two tagged-normative-premise rows
   (-001, -010) ride Paper 1 or monograph introduction exactly as the Paper 1
   manuscript's status ledger already states them (at their open status, no
   promotion); the distributive-module, measurement-bridge, and bridge rows
   ride Paper 5 (the architecture's "distributive/adaptive constraints where
   reproducible"); the antitheorem rides the negative register; the
   correct-before-use instrument and the two unreproduced data pipelines
   ride the open-problem docket.

3. ELEVEN module classifications (A016 unclassified 11 -> 0): the B6 typed
   normative premise -> architecture_transformation_composition (the
   normative-typing discipline is architecture-level, joining the -010
   intergenerational-nondegeneracy floors the same way the Paper 1 ledger
   groups the tagged normative premises); the constituency, floor,
   instrument-vintage, MPI-bridge, data-pipeline, conjecture-bridge, and
   residue rows -> observation_governance_empirics (the measurement/
   identification discipline); the exact-conjunction method rule and the
   smooth-barrier antitheorem -> formal_foundations (the noncompensation
   family — CC-A018-001/CC-A013-001 precedent). ELEVEN mapping
   classifications (UNRESOLVED -> resolved).

4. ONE mapping classification to COUNTEREXAMPLE_OR_LIMIT: CC-A016-012 (the
   anti-domination residue) — boundary-only content (the part every
   income-and-amenities box misses, which must NOT be filled with a 0-1
   agency score), per the closure report's boundary principle; the typed
   floors and registry rows stay EXACT_SPECIALIZATION (they instantiate the
   canonical typed-norm objects, at their open/unoperationalized status).

5. The evaluation record's corrections preserved verbatim in every row:
   A016-L1 (the poverty-line vintage: the current primary line is $3.00/day
   2021 PPP; $2.15/2017 PPP only for historically vintage-consistent
   analysis); A016-L2 (the population mismatch: the declared G is registered
   inshore harvesters/licence holders, the displayed data are all-resident
   CSD employment income including aquaculture and processing — the CSD
   table is not a licence-holder panel); A016-L3 (the geography mismatch:
   NL fishing-dependent CSDs are not automatically the 2J3KL impact
   population); A016-L4 (the unarchived extraction: 43 CSDs, the 32.2%/25.6%
   means, and the top-ten values are plausible but not verified from the
   article alone); A016-L5 (the internal contradiction between the displayed
   table and the limitations list); A016-L6 (non-decline is a normative
   rule, not an empirically justified floor); A016-L7 (finite LogSumExp is a
   conservative inner certificate with a quantified approximation gap, not
   simply "compensation reintroduced"); A016-L8 (coincidence is not causal
   effect — comparison populations, confounders, migration, shellfish
   substitution, transfers, policy timing, and a causal or explicitly
   descriptive design required); A016-L9 (terminology and publication
   style).

Same honest boundary: content-level acceptance only; no normative premise
promoted to a theorem or operationalized; the unreproduced tables stay
unreproduced (the docket rows carry the extraction obligations); the §8
interface contract remains open; the paper-time citation match rides Part
III.

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
AC = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSE = 'source_specific_empirical_status_check_required'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='typed normative premise verified in source §2 and §8 (N1: no relevant population may be pushed below a stated social minimum and the capacity of future generations must not be irreversibly degraded — a normative commitment, "a value premise, not a physical law and not a control theorem"; N2: adaptive capacity is held by someone, used against someone, paid for by someone — anti-domination; U1 records both as tagged value premises)', module=(AC, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified architecture_transformation_composition (the normative-typing discipline is architecture-level, joining the -010 intergenerational floors as the tagged normative premises — the Paper 1 status ledger already states both rows at their open status); destination Paper 1 or monograph introduction confirmed; NO PROMOTION: the premise stays a tagged norm'),
    2: dict(kind='definition verified in source §2 (D1: the worst-off relevant population is a modelling choice — a named constituency G_t; for the program\'s own case §5.2 names G = registered inshore harvesters / licence holders in 2J3KL)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='A016-L2 recorded (the population mismatch: the displayed CSD data are all-resident employment income including aquaculture and processing — redefine G as CSD populations or obtain licence-holder micro/administrative data; do not treat the CSD table as a licence-holder panel); A016-L3 recorded (the geography crosswalk from CSDs to 2J3KL dependence)'),
    3: dict(kind='definition verified in source §2 (D2: a measured floor is a pair (I_k, c_k) — instrument I_k and cutoff c_k; the floor is a measurement object, distinct from the norm that motivates it)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (the measurement-bridge definition); A016-L6 recorded (non-decline is a normative rule, not automatically an empirically justified floor — baseline, cohort, inflation/PPP treatment, uncertainty, attrition, acceptable variation, authority, and structural diversification all require declaration)'),
    4: dict(kind='methodological rule verified in source §2 and §3 (M1: if several floors are in force the arrangement fails as soon as ANY measured margin m_k(G,t) = I_k(G,t) - c_k is negative — report the vector m(G,t); the conjunction is exact, no compensatory master scalar)', module=(FF, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified formal_foundations (the noncompensation family — the measurement-level twin of CC-A018-001/CC-A013-001); the evaluation record confirms componentwise margins rather than a compensatory master score as the accepted redesign; destination Paper 5 confirmed (the distributive-measurement context)'),
    5: dict(kind='antitheorem verified in source §3 (the discarded draft\'s smooth barrier encoding of the intersection {a_k >= c_k}: the iff is a definition plus a standard limit; at finite rho compensation is reintroduced; at rho -> infinity the function is unnecessary — with the A016-L7 correction: finite LogSumExp is a CONSERVATIVE INNER CERTIFICATE with a quantified approximation gap, not simply "compensation reintroduced"; the exact conjunction is the minimum/essential infimum, and smoothness may be useful when conservatism is declared)', module=(FF, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified formal_foundations (the noncompensation/smoothness critique); mapping classified COUNTEREXAMPLE_OR_LIMIT (the antitheorem — the wrong-object critique); destination negative/counterexample register confirmed; the corrected reading (conservative, not exact) recorded per the audit status "Modify: finite smooth form is conservative, not exact"'),
    6: dict(kind='empirical instrument record verified in source §4.1 (the PIP lock: the $2.15/day 2017 PPP line with welfare aggregate, PPP year, population, and vintage locked — per A016-L1 now HISTORICAL ONLY: the current primary international poverty line is $3.00/day 2021 PPP; the 2017-PPP line remains available only for historically vintage-consistent analysis)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True,
            extra='module classified observation_governance_empirics; CORRECT BEFORE USE status retained (the audit\'s own instruction): either use $3.00/2021 PPP or explicitly freeze a historical 2017-PPP query and explain why; destination conditional docket confirmed (the open correction obligation)'),
    7: dict(kind='measurement bridge verified in source §4.2 (the global MPI as a multidimensional deprivation instrument — Alkire-Foster / OPHI / UNDP; U5: MPI is not N2 — neither PIP nor MPI exhausts the normative B6 object; both are world-hooks for deprivation, retained with release/vintage locks)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics; the evaluation record\'s verified item 3 recorded (PIP and MPI are legitimate external instruments that do not exhaust B6); destination Paper 5 confirmed'),
    8: dict(kind='empirical data-pipeline record verified in source §5.2 (the 43 NL fishing-dependent CSDs identified from Statistics Canada Tables 38-10-0167-01 (2016) and 38-10-0168-01 (2021); the mean income from fishing 32.2% (2016) -> 25.6% (2021))', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='module classified observation_governance_empirics; UNREPRODUCED status retained (the audit\'s own verdict): plausible but not verified from the article alone — the locked query, CSV extract, filters, missing-value rules, geography crosswalk, and reproduction code are required (A016-L4); the Statistics Canada method facts verified by the evaluation record (top-2% CSD definition; fishing thresholds 25.1% in 2016 and 21.4% in 2021); destination conditional docket confirmed'),
    9: dict(kind='empirical data-pipeline record verified in source §5.2 (the top-ten CSD table: Bay de Verde 71.7% -> 50.7%; Belleoram 58.9% -> 56.7%; Fermeuse 57.9% (2016 only); Hant\'s Harbour 53.2% -> 30.0%; Anchor Point 51.6% -> 33.3%; Old Perlican 50.0% -> 41.7%; Comfort Cove-Newstead and Greenspond 45.7% -> 37.8%; Hermitage-Sandyville 45.5% -> 56.5%; Charlottetown (Labrador) 43.9% -> 38.5%)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='module classified observation_governance_empirics; UNREPRODUCED and NOT-LICENCE-HOLDER-POPULATION status retained (the audit\'s own verdict): A016-L2 (the population mismatch) and A016-L4 (the unarchived extraction) apply to every displayed value; A016-L5 recorded (the internal contradiction with the limitations list\'s "No Newfoundland income or licence table is computed" — the displayed CSD-income extraction must be distinguished from the missing licence/participation/recruitment panel); destination conditional docket confirmed'),
    10: dict(kind='normative research-programme record verified in source §5.3 (the proposed floors m2 participation non-decline and m3 recruitment-of-people non-decline, with m1 income/transfers pre-declared — normative and unoperationalized: U7 records that B6 is not operationalized by this paper)', module=(AC, 'confirmed'), mapping=(EX, 'confirmed'), evidence=CRO, cite=True,
            extra='the intergenerational-nondegeneracy family (the future-persons clause of N1 checked on present irreversible commitments, §4.3); UNOPERATIONALIZED status retained — no promotion; destination Paper 1 or monograph introduction confirmed (the Paper 1 status ledger states this row at its open status)'),
    11: dict(kind='conjecture verified in source §2 and §5.4 (C1: a biomass-only success story can coincide with a declining inshore G — the discriminants: biomass pulses up while locked human margins stay negative supports C1; human margins recovering with or before biomass defeats it; if the human series cannot be assembled, B6 is NOT operationalized and that is published)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True,
            extra='module classified observation_governance_empirics (the A014/A011 bridge: the cod case\'s social-ecological conjecture); OPEN conjecture status retained; A016-L8 recorded (coincidence is not causal effect — comparison populations, confounders, migration, shellfish substitution, transfers, policy timing, and a causal or explicitly descriptive design required); cite together with the A014 rows at the Paper 5 cod seam'),
    12: dict(kind='normative limitation record verified in source §6 (the anti-domination residue that must not be filled: who pays for persistence, who may use remaining variety, whose knowledge counts, future persons — "the part every income-and-amenities box misses"; N2 is not filled with a 0-1 "agency" score; §9\'s limits preserve the residue: no household vector constructed, no far-from-equilibrium thermodynamics computed, non-Western obligation systems not consulted, future persons not assigned a fake income)', module=(OG, 'classified'), mapping=(CO, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (the measurement-limitation discipline); mapping classified COUNTEREXAMPLE_OR_LIMIT (boundary-only content: what the instruments cannot capture — the "must not be filled" boundary); the responsible-engagement obligation retained (the audit\'s own instruction — the Liboiron/Whyte citations mark the engagement surface, not its discharge); destination Paper 5 confirmed'),
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
        if not row['concordance_id'].startswith('CC-A016-'):
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

        parts = [f'Row-closed {DATE} (A016 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A016 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 293 + 12, f'expected 305 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
