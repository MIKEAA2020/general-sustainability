#!/usr/bin/env python3
"""Scientific row-closure pass for source A013 (uploads/paper1_accounting.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
and A019 passes in the same campaign). The full source (*Componentwise
Sustainability Accounting: Typed Stock-Flow Ledgers and Depletion
Diagnostics*, 465 lines) was read in full; every inventoried item was located
in the source; for each of the 12 A013 rows this pass verifies item
existence, kind, the source's own status discipline (the inventory's own
Verified/Valid/accepted-by-user-instruction status column is the verification
witness; the evaluation record's qualification list — the support-gap
closedness caveat, the notation consideration, the supplement-pending
status of the application values — is read alongside), the canonical module,
the primary mapping type per TCS-1.0 §7, and the proof/evidence status.

A013-specific findings:

1. NO intake row corruptions: all 12 rows quote-check cleanly against the
   inventory table.

2. ONE mapping-type correction: CC-A013-001 (the positive-weighted-scalar
   non-certification observation) EXACT_SPECIALIZATION ->
   COUNTEREXAMPLE_OR_LIMIT. The item is the explicit witness construction
   (b_k = -L, b_j = (w_k L + 1)/w_j with w^T b = 1 > 0 despite b_k < 0) —
   the same logical content as CC-A018-001, which the A018 pass classified
   COUNTEREXAMPLE_OR_LIMIT; the cross-source family-consistency precedent
   (the A006 pass's five corrections "per A002-011" et al.) applies. The
   source's own humility is preserved: "This familiar fact is recorded here
   only to fix the certification boundary, not as a new mathematical
   result."

3. NINE module classifications (A013 unclassified 9 -> 0), all to
   ledger_diagnostics (the balance-domain and support-gap definitions, the
   incidence identity, the forward-invariance theorem, the three
   depletion-diagnostic definitions, the G3P anomaly indices, and the
   fisheries removals-only scale are all the ledger/diagnostic family —
   the CC-A018-017 precedent classified the same application tables
   ledger_diagnostics). The three intake LD classifications (-005, -008,
   -011) confirmed. TEN mapping classifications (UNRESOLVED -> resolved).

4. NO destination corrections: -001 to Paper 2 with CC-A018-001 (the
   noncompensation family in the atlas — the identical proposition's
   verified destination); the other eleven rows to Paper 3 (the ledger,
   positivity, diagnostic taxonomy, and the three classified applications
   are exactly the architecture's Paper 3 content list).

5. The source's own status discipline preserved verbatim in every row: the
   domain-qualified scope of the noncompensation observation (an
   unrestricted compensatory certificate is ruled out; a restricted-domain
   implication must be proved from the restrictions; the non-compensatory
   scalar encodings min_i b_i, ||[-b]_+||, and max_i [-b_i]_+/s_i^ref DO
   certify absence of a component deficit when reference scales are
   declared); the support-gap closedness qualification ("Valid; attainment
   requires closedness" — if Gamma_reg is not closed the supremum may not
   be attained); the service-readout discipline (internal transfers are not
   services; the O-notation consideration is recorded for the canonical
   bridge); the three-quantity taxonomy (gross turnover measures dependency,
   not decline — g > 0 does NOT imply dot A < 0; the local ratio freezes
   the current net rate; the hitting time is scenario-conditioned with a
   distribution or robust interval, not a single universal date); the
   application classifications (the G3P index is a statistical anomaly
   index, not the physical H_A^loc; the reserve-life ratio is internally
   consistent arithmetic, not an exhaustion forecast; Theta_F is a
   removals-only pressure time scale classified OUTSIDE the
   J/H/T hierarchy — "SSB is not an abiotic support pool"); and the
   ledger-to-viability boundary (the safe-set construction links to
   viability but "does not identify their certification statements").

Same honest boundary: content-level acceptance only; no theorem status
promoted; the G3P/phosphate application values stay at their accepted-
by-user-instruction status with the submission-stage supplement pending;
the §8 interface contract remains open; the paper-time citation match
rides Part III.

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
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSE = 'source_specific_empirical_status_check_required'
SSA = 'source_status_accepted_artifact_pending'

V: dict[int, dict] = {
    1: dict(kind='logical observation + explicit witness construction verified in source §2.3 (for any n >= 2, any component k, any deficit L > 0 and any j != k: b_k = -L, b_j = (w_k L + 1)/w_j, b_i = 0 otherwise, gives w^T b = 1 > 0 despite b_k < 0 — a positive half-space contains vectors outside the nonnegative orthant; on a restricted feasible domain the certificate requires the separately proved implication b in B, w^T b >= 0 => b in R_+^n, which fails exactly when the domain contains a compensating counterexample of the displayed kind)', module=(FF, 'confirmed'), mapping=(CO, 'corrected'), evidence=PI, cite=True,
            extra='mapping corrected EXACT_SPECIALIZATION → COUNTEREXAMPLE_OR_LIMIT (intake: EXACT_SPECIALIZATION): the item is the explicit witness construction — the same logical content as CC-A018-001, classified COUNTEREXAMPLE_OR_LIMIT by the A018 pass (cross-source family consistency); the source\'s own humility preserved ("recorded here only to fix the certification boundary, not as a new mathematical result"); the non-compensatory scalar encodings (min_i b_i, ||[-b]_+||, max_i [-b_i]_+/s_i^ref) DO certify absence of a component deficit when reference scales are declared — recorded with the certification boundary; destination Paper 2 confirmed with CC-A018-001 (the atlas\'s noncompensation family)'),
    2: dict(kind='definition verified in source §2.1 (the state-dependent feasible balance domain B(x,t) = {O(x,u,theta) - d : u in U(x,t), d in D(t)} — the geometry is state dependent and inherited partly from the stock-flow model; "the unrestricted argument below cannot replace an application-specific analysis of B(x,t)")', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics (the balance-domain definition is the ledger/service-readout diagnostic object); the notation consideration recorded (the evaluation record reserves O for measurement; a canonical service map Gamma_s, Qv, or S at the canonical bridge); destination Paper 3 confirmed'),
    3: dict(kind='definition verified in source §2.2 (the directional regenerative-support fraction alpha_reg(s_bar; x,t) = sup{alpha in [0,1] : alpha s_bar in Gamma_reg(x,t)} and the support gap (1 - alpha_reg) s_bar in the same service units; a realized service in Gamma_all \\ Gamma_reg is support-dependent even when s >= d)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics; the inventory\'s own status preserved verbatim ("Valid; attainment requires closedness"): if Gamma_reg is not closed the supremum may not be attained — the gap is relative to a supremal fraction, not necessarily an achievable boundary service; the non-interpretation discipline recorded (the statement neither subtracts raw material from service nor proves a stock is declining; net depletion still requires a negative stock balance or a trajectory argument)'),
    4: dict(kind='identity verified in source §3.2 (the six-compartment incidence matrix S(alpha, rho) with 1^T S = 0 — the routing splits alpha (harvest to U) and rho (retirement to U vs W) displayed explicitly with the eight nonnegative primitive fluxes g, m, h, d_U, e_GA, e_AG, c_G, r_P)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics; the constitutive-choices discipline recorded (the constant splits, the compartment set, and the absorbing-sink convention are features of this example, not properties of every typed ledger; the monomaterial projection caveat; the quality-grade split obligation if recovery claims are made); destination Paper 3 confirmed'),
    5: dict(kind='theorem + proof verified in source §3.3 (mass conservation: d/dt M = 0 for M = X+U+A+G+P+W along every classical solution — the pairwise cancellation proof with -h + alpha h + (1-alpha)h = 0 and rho r_P - r_P + (1-rho) r_P = 0)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the conservation argument applies to the expanded typed incidence system when quality grades are split — not automatically to an undifferentiated quality-neutral loop (the source\'s own scope note); the open-systems remark recorded (imports/exports become dot M = I_partial - O_partial)'),
    6: dict(kind='theorem + proof verified in source §3.3 (forward invariance of the nonnegative cone R_+^6 under the donor boundary assumptions — the face-by-face tangent-cone argument: at X = 0, g = m = h = 0 so dot X = 0; at U = 0, dot U = m + alpha h + rho r_P >= 0; at A = 0, dot A = d_U + e_GA >= 0; at G = 0, dot G = e_AG >= 0; at P = 0, dot P >= 0; at W = 0, dot W >= 0; the Aubin tangent-cone invariance theorem cited)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the CC-A018-003/CC-A019-003 precedent: the closed ledger\'s positivity family); conservation and boundary admissibility are SEPARATE obligations (the source\'s own emphasis); the finite-donor condition discipline recorded (a target-relaxation law e_GA = omega(A^eq - A) does not satisfy it unless limited by G — the open-system declaration requirement)'),
    7: dict(kind='definition + false-implication record verified in source §4.1 (the gross turnover intensity J_A^gross = g/A and gross support-coverage ratio H_A^gross = (A - A_min)/g; the implication g > 0 => dot A < 0 is FALSE in general — at an interior steady state g can be positive while decomposition and geological transfer balance it exactly)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics; the source\'s own discipline preserved verbatim ("Gross uptake measures throughput or dependency; net depletion is a balance property"); destination Paper 3 confirmed'),
    8: dict(kind='definition verified in source §4.2 (the local net-depletion ratio H_A^loc = (A - A_min)/[-dot A]_+ with the extended-real convention +infinity when dot A >= 0 — "correctly reports no current net decline at a stationary or replenishing state"; still not a trajectory forecast: it freezes the current net rate)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='the middle rung of the three-quantity taxonomy (J/H gross = dependency; H^loc = frozen-rate ratio; T_A = scenario-conditioned) — the three answer different questions and must not share one depletion-horizon label'),
    9: dict(kind='definition verified in source §4.3 (the scenario-conditioned hitting time T_A(x_0; pi, d) = inf{t >= 0 : A^{pi,d}(t; x_0) <= A_min} with T_A = +infinity if never reached; under parameter, observation, and scenario uncertainty the appropriate output is a distribution or robust interval, not a single universal date)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics; destination Paper 3 confirmed; the first-passage semantics join the A024 first-passage rows at the Paper 3 diagnostics seam'),
    10: dict(kind='application record verified in source §5.1 (the G3P v1.12 Linear-Trend Anomaly Persistence Index L_hist^anom = (a_latest - a_hist,min)/[-a_dot]_+ and the four-basin table: Indo-Gangetic -49.7 cm/yr / ~2.7 yr; North China Plain -18.6 / ~7.9; Central Valley -16.1 / ~9.5; La Mancha -3.2 / ~21.4 over the April 2002-September 2023 window)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=SSA, cite=True,
            extra='module classified ledger_diagnostics (the CC-A018-017 precedent: the same application tables classified ledger_diagnostics); the values accepted as verified by explicit user instruction with the submission-stage supplement pending (processing files, source extracts, shared references not in the workspace); the source\'s own classification preserved verbatim: a statistical anomaly index with units of time, NOT the physical H_A^loc and not a forecast of aquifer exhaustion — a physical H_A^loc requires an absolute stock estimate and a net stock derivative; cite together with CC-A018-017 (the A018 statement of the same tables) at the Paper 3 seam'),
    11: dict(kind='application record verified in source §5.2 (the phosphate reserve-life ratio T_reserve = G_reserve/C_G ~= 309 yr at ~74,000 Mt world reserves and ~240,000 kt/yr production; the resource-threshold variant T_{resource,10%} = 0.9 G_resource/C_G answers a different question and must not share a column without an explicit convention label)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE, cite=True,
            extra='the arithmetic internally consistent as a reserve-life ratio to zero; NOT a physical exhaustion forecast (reserve classification changes with prices, technology, exploration, regulation); the source vintage to be supplied at submission (the inventory\'s own status); the reserves/resources split discipline recorded'),
    12: dict(kind='application record + classification boundary verified in source §5.3 (the Fisheries-Only Time-to-Reference Theta_F = R_B/F_now with R_B = log(SSB_now/B_lim): the crossing time of the deliberately incomplete comparison process dot B = -F_now B; the genuinely local biomass-decline ratio H_B^loc = (B - B_lim)/[-dot B]_+ would require a compatible net dot B estimate, and a demographic hitting time a fully specified population model — "RAM Legacy SSB and F data do not by themselves supply these quantities or models")', module=(LD, 'classified'), mapping=(CO, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics; mapping classified COUNTEREXAMPLE_OR_LIMIT (the item\'s load-bearing content is the classification boundary: the construction is retained specifically to show why an isolated gross-removal time scale must NOT be promoted to a net depletion diagnostic — outside the J/H/T hierarchy; "Spawning biomass is not an abiotic support pool"); the A014 cod case is the worked fisheries instance of exactly this discipline'),
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
        if not row['concordance_id'].startswith('CC-A013-'):
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

        parts = [f'Row-closed {DATE} (A013 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A013 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 272 + 12, f'expected 284 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
