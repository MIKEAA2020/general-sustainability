#!/usr/bin/env python3
"""Scientific row-closure pass for source A020 (uploads/paper_III_two_channels.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003 pass in
the same campaign). The full source (*Protective Delay is a Different Loop:
Two Institutional Channels*, 262 lines) was read in full; every inventoried
item was located in the source; for each of the 9 A020 rows this pass verifies
item existence, kind, the source's own status discipline (definition /
theorem / proposition / corollary / numerical-result environments with proofs
on the line; the brief evaluation record's correction list is the verification
witness), the canonical module, the primary mapping type per TCS-1.0 §7, and
the proof/evidence status. The committed corrected article
(revised_articles/A020_two_channels_corrected.tex) was read alongside: it
implements the zero-root and characteristic-continuity requirements on the
all-delay stability argument, the downgraded statement of the numerically
located unique loop-gain maximum, and the continuity/common-equilibrium/
gain-margin hypotheses on the mobilising-weight corollary.

A020-specific findings:

1. NO intake row corruptions: all 9 rows quote-check cleanly against the
   inventory list.

2. ONE mapping-type correction: CC-A020-003 (the no-positive-Hopf-frequency
   cubic result) COUNTEREXAMPLE_OR_LIMIT -> EXACT_SPECIALIZATION. The theorem
   is an exact application of the companion's loop-gain exclusion machinery
   at protective gains — the CC-A018-016 family precedent (the loop-gain
   exclusion theorem is EXACT_SPECIALIZATION, not a witness construction
   refuting a claimed possibility). The channel-separation READING ("destabil-
   isation by short delay is confined to the mobilising summand") is the
   theorem's interpretation, carried in the row note, not the mapping type.

3. SIX module classifications (A020 unclassified 6 -> 0), all to
   nonlinear_dynamics (the named three-state core's delay/characteristic-
   equation content — the protective channel, its linear coefficients, the
   iso-gain flip, the weighted small-gain theorem, the conditional mobilising
   weight, and the pacing synthesis); the three intake ND classifications
   (-003, -005, -008) confirmed. SIX mapping classifications (UNRESOLVED ->
   resolved as EXACT_SPECIALIZATION).

4. NO destination corrections: all nine rows are Paper 4's named content (the
   architecture's Paper 4 content list names "protective channel and
   two-delay identity" explicitly).

5. The source's own correction status preserved verbatim: the no-Hopf theorem
   and weighted small-gain theorem are RETAINED with the added zero-root and
   characteristic-continuity requirements (implemented in the corrected
   article); the loop-gain maximum 0.08011 is a numerically located maximum
   stated at its downgraded status; the mobilising-weight corollary is
   conditional on the continuity/common-equilibrium/denominator-nonvanishing/
   strict-gain-margin hypotheses (the corrected article's line 211); the
   sampled crossing T_r=2.306 is an Euler-discretisation crossing (1+T_r C_E
   with C_E=-0.850), explicitly NOT a Hopf of the protective DDE; the
   sampled numerical values are accepted as externally verified at exact
   source-stated status by user attestation, with archive action P-A020-01
   (publication-artifact documentation) remaining open.

Same honest boundary: content-level acceptance only; no theorem status
promoted; the §8 interface contract remains open; the paper-time citation
match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-28'

ND = 'nonlinear_dynamics'
EX = 'EXACT_SPECIALIZATION'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSE = 'source_specific_empirical_status_check_required'
SSA = 'source_status_accepted_artifact_pending'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='model definition verified in source §2 (Definition 1: the quota-tracking protective effort law dE/dt = (1-E/E_max) eta_p (E_cap(Z(t-tau_p)) - E) with E_cap C^2, positive, strictly decreasing; the calibration E_cap(Z)=E_0 Z_ref/(Z_ref+Z) placing the unique interior rest at the companion\'s Candidate A point (N*,Z*,E*)=(89.55188, delta, 2.08962), so the stock-memory block is identical and only the effort law changes)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics (the named three-state core\'s response-channel content); the E-interpretation discipline (A003\'s non-interchangeability of industry effort / quota utilization / institutional control) applies at the seam; destination Paper 4 confirmed'),
    2: dict(kind='calibrated linear coefficients verified in source §2 (C_E = -(1-E*/E_max) eta_p = -0.850336 and C_Z = (1-E*/E_max) eta_p E_cap\'(delta) = -1.661702 at eta_p = eta_A = 0.914 — "Both signs are those of a restoring quota, not of scarcity mobilisation")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSE, cite=True,
            extra='module classified nonlinear_dynamics; the coefficient values are calibration arithmetic from the source-stated formulas at the Candidate A point — accepted at source-stated numerical status; the sign discipline (C_Z < 0 is the protective channel; C_Z = +1.785 the mobilising one at gated Candidate A) is the channel-separation object'),
    3: dict(kind='theorem + proof verified in source §3 (Theorem 1: at the Candidate A stock-memory linearisation and the protective gains, the monic cubic H has no positive root — c_2=0.76339, c_1=0.028946, c_0=9.278e-6 all positive and c_2 c_1 - c_0 = 0.02209 > 0, Descartes\' rule of signs plus Routh-Hurwitz; equivalently the loop gain Gamma(omega) attains its maximum 0.08011 at omega ~= 0.0583 — a numerically located maximum at its downgraded status; the companion\'s loop-gain theorem then excludes every delay-induced Hopf for all tau_p >= 0)', module=(ND, 'confirmed'), mapping=(EX, 'corrected'), evidence=PI, cite=True,
            extra='mapping corrected COUNTEREXAMPLE_OR_LIMIT → EXACT_SPECIALIZATION (intake: COUNTEREXAMPLE_OR_LIMIT): an exact application of the companion\'s loop-gain exclusion machinery at protective gains — the CC-A018-016 family precedent; the channel-separation reading (destabilisation by short delay is confined to the mobilising summand) is the theorem\'s interpretation, carried here; the corrected article adds the zero-root and characteristic-continuity requirements to the all-delay stability argument — retained, not demoted'),
    4: dict(kind='proposition + proof verified in source §4 (Proposition 1: replacing C_Z by -C_Z at fixed modulus leaves H unchanged and shifts the fundamental delays by pi/omega — tau_- = 128.374, tau_+ = 70.697 years, the companion values shifted on each family; both crossings remain local Hopfs; the reversed-gain linearisation has loop gain 1.016 > 1 and retains the eta E*/Delta_ref factor, so it is NOT the quota law — "Definition 1 changes the modulus as well as the sign")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; the iso-gain discipline recorded: a pure sign flip is not a protective institution — the genuine protective law changes the modulus as well (the false-reversal identification hazard); destination Paper 4 confirmed'),
    5: dict(kind='theorem + proof verified in source §5 (Theorem 2: the two-delay characteristic identity P(lambda) - L(lambda)(C_m e^{-lambda tau_m} + C_p e^{-lambda tau_p}) = 0 with P and L the companion polynomials, proved by expanding the variational system\'s characteristic determinant along the third row)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the exact algebraic identity the architecture\'s Paper 4 content list names ("two-delay identity"); C_m = chi_m C_Z^mob, C_p = chi_p C_Z^prot, C_E the sum of the two gate-adjusted E-derivatives at the common interior rest where both brackets vanish separately'),
    6: dict(kind='theorem + proof verified in source §5 (Theorem 3: if sup_omega>0 (|C_m|+|C_p|) |L(i omega)| / |(i omega - A_N)(i omega + d)(i omega - C_E)| < 1 then the two-delay characteristic equation has no imaginary-axis root for any tau_m, tau_p >= 0 — the triangle-inequality small-gain proof using |e^{-i omega tau}| = 1)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; the weighted small-gain theorem is retained in the corrected article (with the zero-root and continuity requirements carried by the -003 row\'s correction note); destination Paper 4 confirmed'),
    7: dict(kind='corollary verified in source §5 (Corollary 1: at Candidate A the pure mobilising loop gain exceeds 1 and the pure protective loop gain is 0.080, so under the interpolation hypotheses there exists chi_m* in (0,1) such that every interpolation with chi_m < chi_m* satisfies the weighted small-gain theorem — a Hopf of the interpolated system requires a sufficiently large mobilising weight and cannot be produced by decreasing tau_p alone)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; CONDITIONAL status retained and strengthened by the correction: the corrected article adds the common-equilibrium, continuity-in-chi_m, denominator-nonvanishing, and strict-protective-gain-margin hypotheses (its line 211) — the corollary stands exactly under those hypotheses; no promotion'),
    8: dict(kind='proposition + proof verified in source §6 (Proposition 2: the protective sample-and-hold monodromy M_p(T_r) = shear(C_E, C_Z) exp(A_hold T_r); rho(M_p(1)) = 0.9838 < 1 — annual review of the quota-tracking channel is linearly stable at Candidate A; the same Euler hold map crosses rho = 1 at T_r = 2.306, which is a discretisation of the explicit Euler factor 1 + T_r C_E with C_E = -0.850, explicitly NOT a Hopf of the protective DDE)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA, cite=True,
            extra='the sampled crossing and search are accepted as externally verified at exact source-stated numerical status by explicit user attestation; archive action P-A020-01 (publication-artifact documentation) remains open; the operator-specific scope recorded (the mobilising hold map is unstable at T_r = 1 because the undelayed mobilising Jacobian is already unstable — the protective map does not inherit that instability)'),
    9: dict(kind='theorem + proof verified in source §7 (Theorem 4: for the mobilising bracket the equilibrium is linearly unstable for 0 < tau < tau_-; for the protective law at Candidate A linearly stable for every tau_p >= 0; for the two-channel system any delay-induced instability lies in a region of (tau_m, chi_m) and is independent of tau_p wherever the weighted small-gain theorem applies — the proof cites Theorem 1 and Corollary 1)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; the pacing synthesis inherits Corollary 1\'s interpolation hypotheses wherever its interpolation clause applies (recorded, not promoted); the channel-specific pacing interpretation is the Paper 4 policy-scope discipline instantiated: faster protective governance is not the hazard — the mobilising sign is'),
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
        if not row['concordance_id'].startswith('CC-A020-'):
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

        parts = [f'Row-closed {DATE} (A020 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A020 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 254 + 9, f'expected 263 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
