#!/usr/bin/env python3
"""Scientific row-closure pass for source A011 (uploads/paper3_empirical.txt).

Executed 2026-08-27, following the procedure established by the A001 and A002
passes (research_program/close_concordance_rows_A001.py, _A002.py). The full
source article (*Periodic Review and Resource Governance: Sampled-Data
Models, Spectral Screens, and Case Evidence*, 296 lines) was read in full;
every inventoried item was located in the source; for each of the 24 A011
rows this pass verifies item existence, kind, status discipline, the
canonical module, the primary mapping type per TCS-1.0 §7, and the
proof/evidence status — with special attention to the source's own status
declarations (the SD-E-DR records are exploratory pending complete stage
registration; the computational record is declared incomplete; the spectral
null carries a three-way restriction; the zero-count case search cannot
serve as independent disconfirmation).

A011-specific findings (beyond the A001/A002 patterns):

1. NO intake row corruptions (unlike A001's pipe-split fragments and A002's
   keyword false-positives): all 24 rows quote-check cleanly against the
   inventory.

2. TWO module corrections (CC-A011-012, CC-A011-020: ledger_diagnostics ->
   observation_governance_empirics) and TWO destination corrections (the
   same rows: Paper 3 -> Paper 5): the 42-stock RAM annual-review cohort and
   its eligibility table are the spectral screen's INPUT layer, defined by
   the annual-review eligibility criterion — an analysis-side cohort
   criterion per the source itself, not a RAM classification and not a
   worked ledger example. Fragmenting the screen's inputs (Paper 3) from
   its analysis (rows -013/-021, Paper 5) would split one analysis across
   papers; Paper 3's fisheries examples are the worked ledger cases
   (A013/A014), not the screen cohort.

3. INVENTORY-LEVEL OMISSIONS flagged (not repaired here, per the A001
   unnumbered-remarks precedent — creating rows would change the registered
   409-row base): the source's ONLY complete formal result — the
   forward-invariance proposition of §3.2 (with proof; verified after
   adding tau_m>0 and resolving held-vs-interpolated effort wording per the
   article evaluation record) — has NO concordance row; likewise the
   rapid-review consistency remark of §3.3 (theorem-tier coverage rides
   CC-A002-034, A002 §7), the governance-time ontology of §2, the
   prospective identification designs of §6, the closed-loop MSE design of
   §7, and the falsification criteria of §8. The A011 inventory records
   these in prose ("Formal result" / "Conditional result" / "Prospective
   design" sections) rather than as inventoried entries — an inventory-
   format outlier versus the A012/A013 per-result tables. Flagged in the
   closure report as paper-wave non-loss obligations; if the paper wave
   needs them as rows, that is a deliberate intake-extension decision with
   its own register entry.

4. The shared bibliography dependency (CC-A011-024) is declared in the
   source (\\input{../shared/references.tex}) but NOT committed in the
   repository (no uploads/shared/ directory) — registered here as a
   paper-time citation obligation.

Same honest boundary as A001/A002: content-level acceptance only; no
theorem status promoted; the §8 interface contract remains open; the
paper-time citation match rides Part III.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-27'

OG = 'observation_governance_empirics'
ND = 'nonlinear_dynamics'
EX = 'EXACT_SPECIALIZATION'
SSE = 'source_specific_empirical_status_check_required'
SSA = 'source_status_accepted_artifact_pending'
DSO = 'defined_source_object'

V: dict[int, dict] = {
    1: dict(kind='model definition verified in source §3.1 (Eq. 1: the between-review logistic resource process with held effort E_n)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True),
    2: dict(kind='model definition verified in source §3.1 (Eq. 2: the filtered nonnegative deficit signal Z with the nonnegative signal map Phi and memory timescale tau_m)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True),
    3: dict(kind='model definition verified in source §3.2 (Eq. 4: the projected explicit effort update — the review map with projection onto [0, E_max])', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True),
    4: dict(kind='named model object verified in source §3.2 (SD-E-B3: Eqs. 1–4 with the shifted floored softplus Phi_k — the sample-and-hold counterpart of the M3-B extractive mobilisation law; the source itself declares it "an explicit controller discretisation, not a generic harvest-control rule")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True),
    5: dict(kind='comparator class definitions verified in source §3.2 (SD-P protective, SD-F fixed multi-year plan, SD-H hybrid with change caps/emergency triggers/legal overrides)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='the source\'s own status discipline preserved: SD-P, SD-F, SD-H are declared comparators for the prospective MSE, not completed numerical experiments in this article'),
    6: dict(kind='computational response record verified in source §5.2 (SD-E-DR-AN: persistent tail oscillation near T_r = 3–4 yr, weak response at 2 yr; annual-review convergence over the tested grids)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
            extra='exploratory finite-grid trajectory-classified response region pending complete stage registration; not attributed to SD-E-B3; no Poincaré-map multiplier classification claimed (the source\'s own restriction); not a reproducible numerical proposition until the computational record is complete'),
    7: dict(kind='computational response record verified in source §5.2 (SD-E-DR-SP: persistent tail oscillation near T_r = 6–12 yr)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
            extra='same exploratory trajectory-classified status as CC-A011-006; the SD-E-DR labels separate these records from SD-E-B3 and do not by themselves complete a model registration (§5.1)'),
    8: dict(kind='computational response record verified in source §5.2 (SD-E-DR-CO: trajectories converge to equilibrium for every tested T_r in [1, 20] yr although the corresponding continuous-delay calculation has an oscillatory interval)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
            extra='a convergence-over-tested-grid record, not a stability theorem for every history; same exploratory status discipline'),
    9: dict(kind='computational response record verified in source §5.2 (SD-E-DR-SL: oscillation over part of the tested grid below ~20–30 yr, convergence at longer review intervals, transition brackets ~30–50 yr depending on r)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
            extra='the source\'s own note preserved: the one-sided slow-r pattern does not contradict rapid-review consistency — the continuous no-delay M3-B target is itself unstable over part of the slow-r regime, so small-T_r trajectories may approximate an unstable target on finite horizons; not a general claim that slower review stabilises governance'),
    10: dict(kind='robustness summary verified in source §5.2 (multiplicative assessment-error experiments retain the anchovy-class trajectory region through 30% error; no noise-induced persistent tail oscillation at annual review in the tested ensemble)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
             extra='robustness summary for the declared multiplicative perturbation only, not a guarantee under arbitrary observation error (the source\'s own restriction)'),
    11: dict(kind='diagnostic spectral record verified in source §5.2 (observable-specific dominant peaks: ~4 yr anchovy-class biomass / 12 yr effort; ~8 yr sprat-class biomass / 60 yr effort)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=None, cite=True,
             extra='retained only as observable-specific dominant peaks over the analysed windows; the source\'s own caveat preserved — components of one stationary periodic orbit cannot have different fundamental periods (harmonics, subharmonics, modulation, or transient spectral content unresolved; no decomposition established)'),
    12: dict(kind='empirical cohort definition verified in source §5.3 (the frozen 42-stock RAM Legacy v4.66 annual-review cohort selected by the separate eligibility screen)', module=(OG, 'corrected'), mapping=(EX, 'classified'), evidence=SSE, dest='Paper 5',
             extra='module corrected to observation_governance_empirics (intake: ledger_diagnostics) and destination corrected Paper 3 → Paper 5: the cohort is the spectral screen\'s input layer, defined by the annual-review eligibility criterion — an analysis-side cohort criterion per the source itself, not a RAM classification and not a worked ledger example; fragmenting the screen\'s inputs (Paper 3) from its analysis (rows -013/-021, Paper 5) would split one analysis across papers; Paper 3\'s fisheries examples are the worked ledger cases (A013/A014), not the screen cohort'),
    13: dict(kind='empirical screen result verified in source §5.3 (the multiplicity-controlled Lomb–Scargle spectral null: no stock has a peak in the 4–8 yr biomass or 12–60 yr effort band meeting all robustness criteria; per-series AR(1) red-noise null; familywise control across stocks, observables, bands)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSE,
             extra='the source\'s own three-way restriction preserved: a spectral null for the selected annual-review cohort — not proof of absence, not a controller-sign comparison (SD-E vs SD-P), not causal evidence for annual review'),
    14: dict(kind='power-analysis record verified in source §5.4 (injected-signal power: sprat-class 1.0 at sigma = 0.1 and ~0.24–0.58 at 0.3; anchovy-class ~0.02–0.14 over tested horizons and noise levels, on 100–200 yr synthetic records)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSE,
             extra='conditional simulations only: no minimum-power guarantee per empirical stock; the 100–200 yr horizons exceed many eligible series; the anchovy-class null is consequently weakly informative and the sprat-class result informative only in favourable noise and record-length regimes (the source\'s own reading)'),
    15: dict(kind='structured case-search record verified in source §5.5 (more than 30 systems across fisheries, aquaculture, groundwater, surface water, rangeland, wildlife harvest, forestry, and produced-capital markets; four eligibility criteria; zero eligible count after primary-source and station-level review)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=None,
             extra='the source\'s own restriction preserved: the stringent criteria (responsive feedback, independently dateable lag, no major competing driver, individual-resource data) prevent the zero count from serving as independent disconfirmation; Bangkok and La Mancha Oriental are the closest cases on the stabilising side; the produced-capital delay oscillators lack the autonomously regenerating stock'),
    16: dict(kind='case-calculation record verified in source §5.5 (author calculations from registered input series, not source-reported values: Sheridan-6 precipitation R^2 ~ 0.47; Icelandic cod post-rule CV 0.387 with 10–15 yr fluctuation and ~0.2–0.3 yr implementation lag — a lag that is not a review interval; Icelandic haddock CV 0.143; La Mancha Oriental 2019–2023 average ~312 hm^3/yr; Peruvian anchoveta robust period ~3.7 yr with |r| ~ 0.31 ENSO leading catch)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=None,
             extra='the anchoveta correlation is retained as exploratory pending exact ENSO product identification (the source\'s own provenance note); the subannual review regime lies below the SD-E-DR-AN response region but controller nonclassification prevents that comparison from testing the mechanism'),
    17: dict(kind='registration-requirement object verified in source §5.1 (the delayed-recruitment equations and complete parameter vectors: reproduction requires a companion registration stating the complete equations, state dimension, class-specific vectors, effort gate, Phi, initial history, flow/update order, and tail-classification conventions)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=SSA,
             extra='the source itself declares the complete stage registration NOT present in the main-text model record — the SD-E-DR values are retained as exploratory computational summaries and are not attributed to SD-E-B3; the SD-E-B3 Candidate-A/B vectors live in the companion model registry (uploads/MODEL_REGISTRY.md); destination Paper 4 kept: the DDE registration object rides the named-delay-systems seam while its response-region outputs (rows -006..-009) are Paper 5 — the A018 seam precedent (equations vs outputs)'),
    18: dict(kind='registration-requirement object verified in source §5.1 and the Data and code availability section (initial histories and solver configuration: one-step flow-then-update convention, contemporaneous exact assessment, tau_dec = tau_dep = 0, no queue; multiplicative assessment error only in the designated robustness experiment)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSA,
             extra='registration requirement declared by the source; not discharged — the solver configuration and histories are not attached'),
    19: dict(kind='reproducibility-artifact obligation verified in the Data and code availability section (code and machine outputs: the source declares the computational record incomplete — "Until the computational record is complete, the stage-output values have the exploratory status defined above rather than the status of reproducible numerical propositions")', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
             extra='the code and machine outputs are NOT committed; the retrospective computational/data results remain unreproduced (the source registry\'s verification status); this row registers the obligation, not a discharged artifact'),
    20: dict(kind='registration-requirement object verified in source §5.3 and the Data and code availability section (RAM stock IDs and the annual-review eligibility table)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=SSA, dest='Paper 5',
             extra='module corrected to observation_governance_empirics (intake: ledger_diagnostics) and destination corrected Paper 3 → Paper 5 — the same screen-input seam as CC-A011-012: the eligibility table is the spectral screen\'s selection layer, not a worked ledger example; the annual-review designation is an analysis-side cohort criterion, not a RAM classification'),
    21: dict(kind='registration-requirement object verified in source §5.3 and the Data and code availability section (processed series and spectral routines: detrending rule, Lomb–Scargle periodogram, band-power integration, AR(1) red-noise null, multiplicity adjustment, detrending/endpoint sensitivity)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=None, cite=True,
             extra='registration requirement; the screen\'s analysis-side artifacts are not attached'),
    22: dict(kind='registration-requirement object verified in source §5.4 and the Data and code availability section (power simulation code and seeds for the injected-signal experiments)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
             extra='registration requirement not discharged'),
    23: dict(kind='registration-requirement object verified in source §5.5 and the Data and code availability section (case-screening table and query log; the case-level primary sources are identified in the screening table per the source)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=None,
             extra='registration requirement not discharged'),
    24: dict(kind='declared file dependency verified in the source (the shared bibliography file: \\input{../shared/references.tex})', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=SSA,
             extra='the shared bibliography dependency is declared in the source but NOT committed in the repository (no uploads/shared/ directory) — registered here as a paper-time citation obligation: the bibliography must be reconstructed from the cited works at paper time'),
}


def module_verdict_str(v: tuple[str, str], intake_module: str) -> str:
    val, verdict = v
    if verdict == 'confirmed':
        return f'module {val} confirmed'
    if verdict == 'classified':
        return f'module {val} classified (intake: unclassified)'
    return f'module {val} corrected (intake: {intake_module})'


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
        if not row['concordance_id'].startswith('CC-A011-'):
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

        parts = [f'Row-closed {DATE} (A011 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A011 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99 + 53 + 24, f'expected 176 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
