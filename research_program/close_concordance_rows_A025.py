#!/usr/bin/env python3
"""Scientific row-closure pass for source A025 (uploads/paper_VIII_interval_folds.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, A013, A024, A016, A010, A004, and A005 passes in the same campaign).
The full source (*Interval Hopf Enclosures and Numerical Evidence for the
Inner Small-Branch Turning Point*, 165 lines) was read in full; every
inventied item was located in the source; the verification witnesses are
(1) the source's own exemplary two-level evidentiary discipline (certified
local Hopf vs non-certified numerical fold evidence — "these computations
support---but do not interval-certify---a small-branch turning point"), (2)
the evaluation record's verified-structure list and six required corrections,
and (3) THIS REPOSITORY'S OWN INDEPENDENT REPRODUCTIONS: the Candidate-A
Hopf interval certificates are reproduced byte-identically from committed
code (validated_computations/a025_interval_hopf.py — the outward-rounded
coefficient-and-phase pipeline the source declares conditional, including
the branch-safe interval atan2 and the simple-root and transversality
sign checks; rerun-verified in reaudit/), and the fold pipeline is rebuilt
nominally (m=64/96/128 all inside the lost certificate interval; the
interval Krawczyk stage remains unimplemented — consistent with the
source's non-certificate status).

A025-specific findings:

1. NO intake row corruptions; NO destination corrections (all thirteen rows
   are the technical/computational supplement to the unified applied
   article — the "Paper 4 appendix or compendium" routing).

2. TWELVE module classifications (A025 unclassified 12 -> 0), all to
   nonlinear_dynamics (the Hopf cubic, the certificates, the collocation
   machinery, the fold protocol, the fold-certificate gap components, and
   the scope statement are all the named three-state DDE's dynamics
   content). ONE module correction: CC-A025-012 (the model-scope row)
   ledger_diagnostics -> nonlinear_dynamics — the no-transfer scope
   statement rides the fold/branch results it delimits. TWELVE mapping
   classifications (UNRESOLVED -> resolved).

3. Mapping semantics per the closure report's boundary principle: the six
   fold-certificate gap rows (-008, -009, -010, -011, -013, and the scope
   row -012) are COUNTEREXAMPLE_OR_LIMIT (boundary content: what is NOT
   certified and does NOT transfer); the positive records (the cubic
   algebra, the interval certificates, the collocation map, the
   continuation, the residual diagnostics, the Moore-Spence formulation)
   are EXACT_SPECIALIZATION.

4. ONE evidence kind-correction: CC-A025-002 (the Candidate-A interval
   root/delay values) conditional_or_open -> source_status_accepted_
   artifact_pending. The source's own condition ("the certificate claim is
   therefore conditional on that pipeline being supplied or independently
   verified") is DISCHARGED AT THE REPOSITORY LEVEL: the outward-rounded
   coefficient-and-phase pipeline is committed and reproduces the
   displayed intervals exactly (tau_- in [3.6661490142739, 3.6661490142743],
   tau_+ in [150.3584773101408, 150.3584773101421]), byte-identical on
   rerun; the publication-archive obligation remains open (the audit's own
   status). The five fold-gap rows close at conditional_or_open (not
   obtained / not started / not completed / not implemented — exactly the
   source's and the repository's status).

5. The source's own status discipline preserved verbatim in every row: the
   delay is the interval evaluation of the phase relation at a certified
   root, not a root of the argument formula; the certificate is conditional
   on the stated pipeline including the argument-branch handling; the
   collocation residual is a finite-dimensional statement (no
   continuous-DDE truncation bound implied); the solver failure at
   tau = 5.590 is a solver-success/failure bracket, NOT a nonexistence
   result; the Floquet multipliers (1.0514 -> 0.99898) are supporting
   external evidence, not enclosed here; the preliminary fixed-tau
   Krawczyk construction does not provide a contracting free-tau enclosure
   ("a limitation of that formulation, not an exclusion of the fold"); the
   fold statement is numerical evidence, not a validated fold theorem; the
   amplitude/period parameter-mismatch caution (5.58667 vs 5.587).

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
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSA = 'source_status_accepted_artifact_pending'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='exact algebra verified in source §1 (the explicit inner-three-state Hopf cubic H(x) = (x + A_N^2)(x + d^2)(x + C_E^2) - C_Z^2 [B_E^2 x + (A_E B_N - A_N B_E)^2], reduced at the interior equilibrium by the filter identity A_E B_N - A_N B_E = 0 to H(x) = (x + A_N^2)(x + d^2)(x + C_E^2) - C_Z^2 B_E^2 x — algebra inherited from A018\'s loop-gain identity family with the derivative identity cross-checked)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified nonlinear_dynamics; destination Paper 4 appendix or compendium confirmed; the phase relation discipline recorded (the delay is the interval evaluation of the phase formula at a certified positive root of H, not a root of the argument formula)'),
    2: dict(kind='interval certificate record verified in source §1 (Numerical result 1: interval Newton applied to the interval-enclosed coefficient representation certifies simple positive roots in x = omega^2, and branch-safe interval evaluation of the phase relation gives tau_- in [3.6661490142739, 3.6661490142743] and tau_+ in [150.3584773101408, 150.3584773101421] for gated Candidate A, upper-interval width of order 1e-12 yr)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA, cite=True,
            extra='evidence kind-corrected to source_status_accepted_artifact_pending: the source\'s own condition (the claim is "conditional on that pipeline being supplied or independently verified") is DISCHARGED AT THE REPOSITORY LEVEL — validated_computations/a025_interval_hop.py implements the outward-rounded coefficient/equilibrium/phase pipeline (nextafter float64 outward rounding, mpmath-iv transcendentals, branch-safe interval atan2, simple-root and transversality sign checks) and reproduces the displayed intervals exactly, byte-identical on rerun; the publication-archive obligation remains open; the A018 corrected article records the same independent reproduction'),
    3: dict(kind='formulation definition verified in source §2 (the 193-dimensional phase-fixed collocation map F: R^192 x R -> R^193 with the phase equation among the 193 equations — the integral phase condition or the first-sine-coefficient convention; "the phase equation is part of F and removes the time-translation degeneracy"; the schematic discretized map with the spectral time-derivative and delay operators)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; correctly dimensioned per the evaluation record\'s verified structure (192 orbit coordinates plus period, 193 equations with the phase condition); the evaluation record\'s correction 1 recorded (state the exact first-sine phase value and verify transversality to time translation)'),
    4: dict(kind='numerical continuation record verified in source §2 (Numerical result 2: the Newton-LM solver initialized from the Hopf normal-form predictor at tau = tau_- + 0.05 and continued with the sqrt(tau - tau_-) predictor finds one approximate periodic-orbit solution at each sampled tau in [3.716, 5.58667] with discretized residual ||F||_2 <= 6e-14; peak-to-peak amplitude of N from 1.10 to 21.80 and period from 250.0 to 313.76 yr; the solver fails at tau = 5.590 under the stated LM budget with residual 2.8e-6 — "a solver-success/failure bracket, not a nonexistence result")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA, cite=True,
            extra='module classified nonlinear_dynamics; high-accuracy finite-map result — the repository\'s rebuilt fold pipeline (m=64/96/128, all resolutions inside the lost certificate interval) is the same evidentiary class and is rerun hash-identical; no continuous-DDE truncation bound is implied by the residual'),
    5: dict(kind='numerical diagnostic record verified in source §2 (Numerical result 3: at tau = 5.586666666666667 the computed collocation orbit satisfies ||F||_2 = 5.43e-14, ||J^{-1}F||_2 = 5.69e-12, with sigma_min(J) = 4.54e-7 and cond_2(J) = 1.25e7; the effort gate and filter floor inactive — E = 7.93 << E_max and N >= 72.2)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=SSA, cite=True,
            extra='module classified nonlinear_dynamics; the scope preserved verbatim ("||J^{-1}F||_2 is the norm of a linearized Newton correction for the finite-dimensional collocation map; it is not a rigorous error bound for the continuous DDE or for the fold location"); the non-uniqueness caveat recorded (the data do not establish uniqueness of the collocation zero at each tau, and solver failure at 5.590 does not exclude another zero or family there)'),
    6: dict(kind='supporting evidence record verified in source §2 (the independent shooting/Floquet calculations of the companion paper: a real nontrivial multiplier changing from approximately 1.0514 at tau = 5.584 to 0.99898 at tau = 5.587 on the corresponding small branch — consistent with a candidate simple turning point; "It is not an interval certificate, and the present note does not independently recompute or enclose those multipliers"; the parameter-mismatch caution: 5.58667 vs the fold-quoted 5.587 are not the same parameter)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; NOT ENCLOSED HERE status retained — supporting external/source evidence only; cite together with the companion A018 four-state Floquet rows at the Paper 4 seam'),
    7: dict(kind='formulation/protocol definition verified in source §3 (the 387-dimensional Moore-Spence system M(Y, T, tau, v) = (F, J v, l^T v - 1) = 0 — 387 unknowns and equations after adding the 193-vector nullvector and the delay; the nondegeneracy conditions w^T F_tau not containing 0 and w^T D^2 F[v,v] not containing 0 with the phase condition regular; the pseudo-arclength alternative that "does not by itself certify fold nondegeneracy")', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; correct formulation/protocol per the evaluation record\'s verified structure (the Moore-Spence count is 387 after adding the 193-vector nullvector and delay); the protocol is the certification standard the fold-certificate gap rows are measured against'),
    8: dict(kind='fold-certificate gap component verified in source §3 (the converged Moore-Spence zero: NOT OBTAINED — "The present paper does not construct [the Moore-Spence system] or an interval enclosure of [the nondegeneracy conditions]"; the preliminary fixed-tau Krawczyk construction based on an inverse of J does not provide a contracting free-tau enclosure near the ill-conditioned turning region — "a limitation of that formulation, not an exclusion of the fold")', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; mapping classified COUNTEREXAMPLE_OR_LIMIT (boundary content: what is not certified); NOT OBTAINED status retained — no promotion; the repository\'s nominal fold rebuild does not alter this status (three resolutions inside the lost certificate interval, no certificate)'),
    9: dict(kind='fold-certificate gap component verified in source §3 (the discrete Krawczyk inclusion: NOT STARTED/COMPLETED — "A validated Krawczyk or interval-Newton inclusion for [the Moore-Spence system] would establish a unique fold of the m=64 collocation equations inside the resulting box"; not constructed)', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; NOT STARTED/COMPLETED status retained; the repository\'s post-v1.0 fold work records the same gap ("the interval Krawczyk stage remains unimplemented") — the two records agree'),
    10: dict(kind='fold-certificate gap component verified in source §3 (the interval transversality and curvature conditions: NOT COMPLETED — the left-nullvector enclosure and the nondegeneracy conditions w^T F_tau and w^T D^2 F[v,v] not containing zero, with the phase condition regular)', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; NOT COMPLETED status retained'),
    11: dict(kind='fold-certificate gap component verified in source §3 and §5 (the continuous-DDE bordered radii-polynomial lift: NOT IMPLEMENTED — "A validated Moore-Spence or pseudo-arclength fold computation, followed by a Fourier-tail or function-space error bound, would be required to certify a fold of the continuous DDE"; the discrete/continuous separation is stated throughout)', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; NOT IMPLEMENTED status retained; the discrete collocation proof and the continuous-RFDE proof are correctly separated per the evaluation record\'s verified structure'),
    12: dict(kind='model-scope boundary statement verified in source §4 (all fold and branch statements concern the gated inner three-state DDE and its m=64 collocation discretization ONLY — no transfer to the turnover-corrected working four-state core, the finite-donor primitive system of Paper II, the vector Liebig system of Paper IV, the stage-structured fisheries models of Paper V, or the spatial DDE-PDE of Paper VI; the lower termination of the attracting large-cycle family and the upper-window periodic families are not analyzed here)', module=(ND, 'corrected'), mapping=(CO, 'corrected'), evidence=DSO, cite=True,
            extra='module corrected ledger_diagnostics → nonlinear_dynamics (the no-transfer scope statement rides the fold/branch results it delimits); mapping corrected EXACT_SPECIALIZATION → COUNTEREXAMPLE_OR_LIMIT (boundary content: the explicit no-transfer declaration); this is the A002 no-transfer rule instantiated at the named-dynamics level — cite at the Paper 4 seam with the A018 interface-contract discipline'),
    13: dict(kind='fold-certificate headline status verified in source abstract, §3, and §6 (the fold certificate: NOT OBTAINED — "A Moore-Spence or pseudo-arclength bordered validation of the fold is not constructed here"; "these computations support---but do not interval-certify---a small-branch turning point near tau ~= 5.587"; "The fold statement is therefore numerical evidence, not a validated fold theorem")', module=(ND, 'classified'), mapping=(CO, 'classified'), evidence=CRO, cite=True,
            extra='module classified nonlinear_dynamics; mapping classified COUNTEREXAMPLE_OR_LIMIT (the headline non-certificate); NOT OBTAINED status retained — the entire fold-certificate gap family (-008 through -011 and this row) closes at exactly the source\'s and the repository\'s agreed status; the A018 closure\'s fold-language conformance ("no Moore-Spence/Krawczyk/nondegeneracy certificate or continuous-DDE fold proof is claimed") cites this row\'s discipline'),
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
        if not row['concordance_id'].startswith('CC-A025-'):
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

        parts = [f'Row-closed {DATE} (A025 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A025 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 329 + 13, f'expected 342 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
