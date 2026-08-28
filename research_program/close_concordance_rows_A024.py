#!/usr/bin/env python3
"""Scientific row-closure pass for source A024 (uploads/paper_VII_first_passage.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes (and executed after the A003, A020,
A019, and A013 passes in the same campaign). The full source (*Constructed
Depletion Proxies as First-Passage Times of Observed-Drift Surrogates*, 253
lines) was read in full; every inventoried item was located in the source;
for each of the 9 A024 rows this pass verifies item existence, kind, the
source's own status discipline (two theorems with proofs on the line, one
corollary with proof, one definition, and the source's exemplary seven-item
non-claims list; the brief evaluation record — "Mathematically sound,
carefully scoped note" — is the verification witness), the canonical module,
the primary mapping type per TCS-1.0 §7, and the proof/evidence status.

A024-specific findings:

1. NO intake row corruptions: all 9 rows quote-check cleanly against the
   inventory list.

2. THREE mapping-type corrections, all one principle: items whose load-
   bearing content establishes an interpretation BOUNDARY are
   COUNTEREXAMPLE_OR_LIMIT, not EXACT_SPECIALIZATION (the closure report's
   classification principle; the CC-A013-012 precedent from this campaign).
   (a) CC-A024-005 (the record-relative barrier and boundary-degenerate
   case): the barrier is a path-dependent observational minimum, not an
   independently identified physical failure floor, and the already-at-
   minimum zero is relative to that barrier, not zero physical uncertainty
   or confirmed collapse. (b) CC-A024-008 (the parameter/barrier/observation
   uncertainty cautions): integrating out uncertainty gives mixtures, not a
   single inverse-Gaussian law; no calibrated predictive distribution is
   claimed — pure boundary content. (c) CC-A024-009 (the seven explicit
   non-claims relative to the physical ledger): the source's own §7 boundary
   list. Items carrying a positive record WITH attached restrictions stay
   EXACT (the A011 precedent); items that are ONLY the boundary do not.

3. THREE module classifications (A024 unclassified 3 -> 0), all to
   ledger_diagnostics (the observed-drift surrogate definition, the
   moments/zero-noise/median results, and the barrier discipline are the
   depletion-proxy diagnostic family, joining the already-classified
   inverse-Gaussian and geometric-Brownian theorems and the phosphate
   passage time). THREE mapping classifications (UNRESOLVED -> resolved).

4. TWO evidence kind-corrections: CC-A024-001 (the model-hitting-time vs
   empirical-proxy distinction) source_specific_empirical_status_check_
   required -> defined_source_object (a scoping distinction, not an
   empirical record — the empirical status belongs to the proxy
   applications); CC-A024-003 (the inverse-Gaussian theorem)
   source_specific_empirical_status_check_required ->
   proof_inventory_present_line_check_required (a theorem with its proof on
   the line — the standard Brownian first-passage result applied with the
   substitution; the source-specific empirical status belongs to the
   surrogate APPLICATION, which rides -005's barrier discipline and the
   Paper 3 seam with CC-A013-010/-011).

5. NO destination corrections: the first-passage semantics ride Paper 3
   (the architecture's "depletion horizons and first-passage semantics"
   content, joining the A013 rows at the seam); the proxy-distinction and
   uncertainty-caution rows ride Paper 5 (the observation/identification
   discipline).

6. The source's own status discipline preserved verbatim in every row: the
   surrogates are statistical constructions — not hydrological constitutive
   laws, not mass-conserving, not stochastic completions of the ledger; no
   theorem relates mu-hat to -dot A of the companion cores; T^dep is not
   shown inverse Gaussian; the shorter median/Ito mean is not evidence of
   faster physical depletion; the fisheries calculation is not a stage-
   structured model and the phosphate calculation is not a geological-
   reserve model; public-data inputs retain their existing provenance/
   reproduction obligations.

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

OG = 'observation_governance_empirics'
LD = 'ledger_diagnostics'
EX = 'EXACT_SPECIALIZATION'
CO = 'COUNTEREXAMPLE_OR_LIMIT'
PI = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'
SSE = 'source_specific_empirical_status_check_required'
CRO = 'conditional_or_open'

V: dict[int, dict] = {
    1: dict(kind='scoping distinction verified in source §1 (two objects, not one: the model hitting time T^dep = inf{t > 0 : A(t) <= epsilon A(0)} lives on trajectories of the mass-conserved ledger or a named reduced system and is NOT computed in the empirical tables; the instantaneous diagnostics H^act and H^act,net measure support use and decline and are not identified with empirical regression statistics; the constructed proxies H^win_GW, H_F, and R/P are the public-data objects)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='evidence kind-corrected to defined_source_object (a scoping distinction, not an empirical record); the distinction instantiates the canonical proxy-vs-model discipline exactly; destination Paper 5 confirmed (the observation/identification discipline)'),
    2: dict(kind='definition verified in source §2 (Definition 1: the observed-drift Brownian surrogate A(t) = A_0 + mu t + sigma W_t stopped at first reaching the record-relative barrier A^win_min — "a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of Paper I\'s active-pool equation or Paper II\'s finite-donor primitive system")', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics (the depletion-proxy diagnostic family); destination Paper 3 confirmed; the non-completion non-claim recorded verbatim'),
    3: dict(kind='theorem + proof verified in source §2 (Theorem 1: the inverse-Gaussian groundwater first passage — T_GW ~ IG(nu, lambda) with nu = d/|mu| and lambda = d^2/sigma^2 conditional on treating mu and the barrier as fixed; E[T_GW] = nu = H^win_GW and Var = d sigma^2/|mu|^3; the standard Brownian-drift first-passage result with the substitution)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='evidence kind-corrected to proof_inventory_present_line_check_required (a theorem with its proof on the line; the source-specific empirical status belongs to the surrogate application, which rides -005 and the Paper 3 seam with CC-A013-010)'),
    4: dict(kind='corollary + proofs verified in source §2 (Corollary 1: as sigma -> 0+ the passage time converges to H^win_GW in probability and the deterministic trajectory reaches the barrier exactly there; for every finite sigma > 0 the inverse-Gaussian median m < nu via F_T(nu) = 1/2 + e^{2 lambda/nu} Phi(-2 sqrt(lambda/nu)) > 1/2; the variance scales as sigma^2 and the quantile widths as sigma)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics; the source\'s own reading preserved: conditional distributional statements about the surrogate, not corrections to the tabled years and not evidence of faster physical water-mass depletion'),
    5: dict(kind='barrier discipline verified in source §3 (the barrier A^win_min is selected from the same finite observation window used to estimate mu-hat — a path-dependent, record-relative threshold, not an independently identified hydrological failure floor; future passage below it is a record-breaking stress event under the surrogate; the already-at-minimum case gives T_GW = 0 deterministically for every sigma with IG(0,0) a degenerate boundary limit, not an ordinary inverse Gaussian; an independent physical threshold A# < A^win_min gives the longer conditional mean (A_0 - A#)/|mu| within the surrogate — not a general lower-bound theorem for the physical ledger)', module=(LD, 'classified'), mapping=(CO, 'classified'), evidence=PI, cite=True,
            extra='module classified ledger_diagnostics; mapping classified COUNTEREXAMPLE_OR_LIMIT (the item\'s load-bearing content is the interpretation boundary — the CC-A013-012 precedent: boundary content, not a positive instantiation); the zero-cells discipline recorded (zero relative to the selected observational barrier, not zero physical uncertainty or confirmed collapse)'),
    6: dict(kind='theorem + proof verified in source §5 (Theorem 2: the geometric-Brownian fisheries correction — dB = -hB dt + sigma B dW under Ito gives T_fish ~ IG(nu_F, lambda_F) with nu_F = log(B_0/B_min)/(h + sigma^2/2) and lambda_F = log(B_0/B_min)^2/sigma^2 by Ito\'s lemma on log B; the finite-noise mean is strictly shorter than the deterministic horizon; as sigma -> 0+ it converges to the pure-decay horizon at h = F, B_min = B_lim)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=PI, cite=True,
            extra='the Ito-lemma proof on the line; the source\'s own reading preserved: a property of the chosen surrogate parameterization, NOT a universal claim that environmental variability accelerates physical biomass loss; the fisheries proxy joins CC-A013-012 (the same pure-decay construction\'s classification) and the A014 cod case at the Paper 3/Paper 5 seam'),
    7: dict(kind='application record verified in source §6 (the constant-production phosphate passage time T_phos = (R_0 - R_min)/P with the reserve-life ratio the R_min = 0 special case and a threshold fraction epsilon R_0 giving (1-epsilon) R_0/P; "a conditional reserve-classification proxy under constant production... not a forecast of geological exhaustion without an explicit resource and production model")', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE, cite=True,
            extra='evidence status consistent with CC-A013-011 (the same phosphate content\'s source-specific empirical status); no stochastic phosphate extension is needed for the interpretation in Paper I — the source\'s own scope note; cite together at the Paper 3 seam'),
    8: dict(kind='uncertainty cautions verified in source §6 (the inverse-Gaussian results condition on the drift, barrier, and noise scale; mu-hat is estimated from a finite, potentially autocorrelated record and the barrier selected from the same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks, and common climatic drivers are separate uncertainties; integrating out uncertainty in mu, the barrier, or sigma gives a predictive distribution that is generally a MIXTURE rather than a single inverse-Gaussian law; a residual scale from the same window would not identify process noise; "No calibrated predictive distribution is claimed here")', module=(OG, 'confirmed'), mapping=(CO, 'corrected'), evidence=CRO, cite=True,
            extra='mapping corrected EXACT_SPECIALIZATION → COUNTEREXAMPLE_OR_LIMIT (intake: EXACT_SPECIALIZATION): pure boundary content — the cautions delimit what the distributional statements do NOT provide (the A011 precedent distinguishes records WITH attached restrictions, which stay EXACT, from boundary-only items); destination Paper 5 confirmed (the observation/uncertainty discipline)'),
    9: dict(kind='explicit non-claim list verified in source §7 (all seven: the Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments; no theorem relates mu-hat to -dot A of the companion cores or to the finite-donor primitive system or the three-state delay equation; T^dep is not shown inverse Gaussian; the historical groundwater minimum is not an independently identified physical failure barrier; a shorter surrogate median or Ito mean is not evidence of faster physical depletion; the gross active-pool horizon and its productivity-illusion interpretation are not first-passage results treated here; the fisheries calculation is not a stage-structured fisheries model and the phosphate calculation is not a geological-reserve model)', module=(LD, 'confirmed'), mapping=(CO, 'corrected'), evidence=DSO, cite=True,
            extra='mapping corrected EXACT_SPECIALIZATION → COUNTEREXAMPLE_OR_LIMIT (intake: EXACT_SPECIALIZATION): the source\'s own §7 boundary list — boundary content per the closure report\'s classification principle; the non-claims are the paper\'s exemplary status discipline and ride Paper 3 with the first-passage semantics'),
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
        if not row['concordance_id'].startswith('CC-A024-'):
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

        parts = [f'Row-closed {DATE} (A024 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A024 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 284 + 9, f'expected 293 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
