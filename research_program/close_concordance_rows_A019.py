#!/usr/bin/env python3
"""Scientific row-closure pass for source A019 (uploads/paper_II_closed_ledger.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003 and A020
passes in the same campaign). The full source (*Finite-Donor Primitive Fluxes
and the Nonexistence of a Closed Rest Point*, 193 lines) was read in full;
every inventoried item was located in the source; for each of the 9 A019 rows
this pass verifies item existence, kind, the source's own status discipline
(four theorems with proofs on the line, one rejection statement, two
completion-distinction statements; the brief evaluation record's correction
list is the verification witness), the canonical module, the primary mapping
type per TCS-1.0 §7, and the proof/evidence status. The committed corrected
article (revised_articles/A019_closed_ledger_corrected.tex) was read
alongside: it implements the little-o-to-order/budget-bound replacement
(line 165's transient-length claim), the autonomy fix (the extended system
with G(t) as a state is an autonomous RFDE, not nonautonomous), and the
Hopf-detuning demotion to hypothesis.

A019-specific findings:

1. NO intake row corruptions: all 9 rows quote-check cleanly against the
   inventory list.

2. ONE mapping-type correction: CC-A019-001 (the primitive donor-limited
   exchange and mining laws) APPROXIMATION -> EXACT_SPECIALIZATION. The four
   primitives (e_GA, e_AG, C^{A,lim}, gamma_U U) are the exact typed-flux
   objects of the closed ledger — the CC-A002-008 typed-hybrid-conservation
   family precedent maps exact flux identities as EXACT_SPECIALIZATION. The
   approximation content belongs to the frozen-donor SPECIALIZATION's scope
   statements (-008/-009), not to the primitive laws themselves.

3. ONE destination correction: CC-A019-004 (the no-interior-positive-effort-
   rest theorem) Paper 2 -> Paper 3, with the module corrected
   formal_foundations -> ledger_diagnostics. The theorem is a CLOSED-LEDGER
   rest-point nonexistence result — the A018 ledger-to-dynamics interface
   contract is explicit that "Paper 3 owns the closed ledger and conservation
   proofs", and the theorem constrains exactly that closed primitive ledger
   (it is the source's title result). Routing it to Paper 2 would split the
   closed-ledger object across papers (the A012-006 destination-correction
   precedent: the object joins the paper that owns its full treatment).

4. SIX module classifications (A019 unclassified 6 -> 0): the orthant-
   invariance theorem and the extinction-geochemical rest set ->
   ledger_diagnostics (the A018-003 precedent: the closed ledger's positivity
   family; the rest set is the closed ledger's rest-point structure); the
   cross-completion tracking rejection -> ledger_diagnostics (the seam-object
   family of the A018 interface contract); the extraction-integrability
   theorem -> ledger_diagnostics (the finite-budget consequence of the mass
   identity — Paper 3's depletion-horizon semantics); the long-time finite-
   budget interpretation -> nonlinear_dynamics (the frozen-donor cycle's
   persistence interpretation — the tau_+ delay object); the frozen-donor
   limit distinction's intake ledger_diagnostics confirmed. SIX mapping
   classifications (UNRESOLVED -> resolved).

5. The source's own correction status preserved verbatim in every row: the
   three evaluation-record corrections are implemented in the corrected
   article (the transient-length claim now an order/budget bound; the
   extended system autonomous with the donor as a state; the local-Hopf
   slow-detuning statement a hypothesis, not a consequence of the mass
   budget); the source's own non-claims stand (no finite-time tracking of
   the companion working core; epsilon_G is a donor-draw diagnostic of the
   derived-target completion, not a tracking error bound; the G_0->infinity
   scaling is not a regular perturbation of the working field and Hopf
   persistence under it is not claimed).

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

LD = 'ledger_diagnostics'
ND = 'nonlinear_dynamics'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
AP = 'APPROXIMATION'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='model definition verified in source §2 (the four donor-involving primitives: e_GA = omega_A [A^eq,intrinsic]_+ sigma with recharge unable to run backward — zero at A^geo = 0 and at a nonpositive intrinsic target; e_AG = omega_A A^act; C^{A,lim} = C^A sigma — mining donor-limited the same way extraction is; gamma_U U = detritus return; no derived target appears)', module=(LD, 'confirmed'), mapping=(EX, 'corrected'), evidence=DSO, cite=True,
            extra='mapping corrected APPROXIMATION → EXACT_SPECIALIZATION (intake: APPROXIMATION): the primitives are the exact typed-flux objects of the closed ledger — the CC-A002-008 family precedent; the approximation content belongs to the frozen-donor specialization\'s scope statements (rows -008/-009), not to the primitive laws'),
    2: dict(kind='theorem + proof verified in source §3 (Theorem 1: the natural-block mass identity d/dt(N + A^act + A^geo + U) = -qEN along every absolutely continuous solution; with the companion\'s donor-limited routing restored, the seven-compartment sum N+A^act+A^geo+U+P+W+I is constant — the cancellation proof R - B + T = 0 with B = R + T)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the closed natural block loses mass exactly at the extraction and mining rates; destination Paper 3 confirmed (the architecture names "conservation/nonnegativity" as Paper 3 content and the A018 interface contract assigns the closed ledger to Paper 3)'),
    3: dict(kind='theorem + proof verified in source §3 (Theorem 2: forward invariance of the nonnegative orthant in (N, A^act, A^geo, U, Z, E) — the face-by-face Nagumo argument: at A^geo = 0, e_GA = 0 and dot A^geo = e_AG >= 0; at A^act = 0, R = B = T = e_AG = 0 and dot A^act = e_GA + gamma_U U >= 0; at N = 0 extraction and uptake vanish; the Michaelis-Menten factors C-infinity on the closed orthant)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the CC-A018-003 precedent: the closed ledger\'s positivity family); destination Paper 3 confirmed'),
    4: dict(kind='theorem + proof verified in source §4 (Theorem 3: no interior rest at positive effort — a rest point of the closed natural block with constant E = E_* > 0 forces R = 0, hence N = 0 or N = K or A^act = 0, each incompatible with E_* > 0 and N_* > 0; the companion working point (N*, A^act*) = (89.526, 397.87) is not a rest point at E = E* ~= 2.090 since R* = qE*N* ~= 0.187 > 0)', module=(LD, 'corrected'), mapping=(EX, 'confirmed'), evidence=PI, cite=True, dest='Paper 3',
            extra='module corrected formal_foundations → ledger_diagnostics and destination corrected Paper 2 → Paper 3: the theorem is a closed-ledger rest-point nonexistence result — the A018 interface contract is explicit that Paper 3 owns the closed ledger and conservation proofs, and this is the source\'s title result; routing it to Paper 2 would split the closed-ledger object across papers (the CC-A012-006 destination precedent: the object joins the paper that owns its full treatment)'),
    5: dict(kind='theorem + proof verified in source §4 (Theorem 4: the extinction-geochemical rest set — N = 0, U = 0, E arbitrary, A^act = A^eq,intrinsic sigma; if A_g0 = 0 and sigma = 1 for A^geo > 0, the ray A^act = A^eq,intrinsic, A^geo >= 0; institutional memory yields E -> E* at N = 0 with extraction vanishing identically — consistent with the rest set, not an interior rest)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the closed ledger\'s rest-point structure); destination Paper 3 confirmed; "the only rest points with vanishing extraction are extinction plus geochemical equilibrium" — the abstract\'s own scope statement'),
    6: dict(kind='negative result verified in source §5 (the rejection of the cross-completion tracking claim: the primitive and working A^act fields differ by an O(1) term at the working point even when sigma ~= 1; epsilon_G(T) = G_0^{-1} integral |e_GA - e_AG| dt quantifies cumulative donor draw in the derived-target completion but is NOT a tracking error bound between the primitive system and the working core; a finite-time comparison requires a separate continuous-dependence estimate — "no such estimate is asserted here")', module=(LD, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the seam-object family of the A018 ledger-to-dynamics interface contract — the tracking rejection IS the interface contract\'s no-false-reduction discipline instantiated); mapping classified COUNTEREXAMPLE_OR_LIMIT (a boundary result: the O(1) field difference refutes the claimed estimate family); destination negative/counterexample register confirmed — cite at the Paper 3/Paper 4 seam alongside the A018 interface contract'),
    7: dict(kind='theorem + proof verified in source §6 (Theorem 5: extraction integrability — M(t) = M(0) - integral qE N ds >= 0 by the mass identity and orthant invariance, so qEN in L^1(0, inf) with integral <= M(0); no trajectory maintains extraction at the companion working value qE*N* ~= 0.187 for all time)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics (the finite-budget consequence of the mass identity — Paper 3\'s depletion-horizon semantics); destination Paper 3 confirmed'),
    8: dict(kind='completion distinction verified in source §7 (the frozen-donor limit and its scope: rescaling G = G_0 g, the limit G_0 -> infinity freezes g but does NOT restore the companion\'s derived target — the limiting recharge field uses A^eq,intrinsic, not A^eq,W; the scaling is not a regular perturbation of the working four-state vector field; local Hopf persistence under the primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated)', module=(LD, 'confirmed'), mapping=(AP, 'confirmed'), evidence=PI, cite=True,
            extra='the frozen-donor specialization\'s approximation scope stated exactly: what the approximation is (the frozen-donor limit of the closed ledger) and what it is not (the working completion\'s field); the corrected article\'s autonomy fix recorded at the -009 row'),
    9: dict(kind='finite-budget interpretation verified in source §6 and §8 (the companion\'s tau_+ ~= 150 yr upper cycle is a frozen-donor object; on the closed system it can persist only as a transient on the finite donor budget; the local Hopf mechanism is not cancelled by closing the donor — per the correction, that slow-detuning statement is a HYPOTHESIS, not a consequence of the mass budget, and the transient-length claim is an order/budget bound, not a little-o estimate)', module=(ND, 'classified'), mapping=(AP, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics (the frozen-donor cycle\'s persistence interpretation — the tau_+ delay object); the three evaluation-record corrections implemented in the corrected article recorded verbatim: (a) the unsupported little-o transient length replaced by an order/budget bound; (b) the extended system with G(t) as a state is an AUTONOMOUS RFDE with a slow donor coordinate, not nonautonomous; (c) the Hopf-detuning claim demoted to hypothesis; the precise transient duration and any attractor continuation in (G_0, tau) require a separate computation — registered open, not promoted'),
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
        if not row['concordance_id'].startswith('CC-A019-'):
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

        parts = [f'Row-closed {DATE} (A019 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A019 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 263 + 9, f'expected 272 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
