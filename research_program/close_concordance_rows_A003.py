#!/usr/bin/env python3
"""Scientific row-closure pass for source A003 (uploads/Paper_V_Institutional_Feedback_and_Nonlinear_Transitions.txt).

Executed 2026-08-28, following the procedure established by the A001, A002,
A011, A006, A012, A014, and A018 passes. The full source (*Scarcity-Amplifying
Institutional Feedback, Sampled Governance, and Safety-Relevant Nonlinear
Transitions*, 114 lines) was read in full; every inventoried item was located
in the source; for each of the 15 A003 rows this pass verifies item existence,
kind, the source's own status discipline (policy hypotheses, mechanism
taxonomy, and a variant registry — the source's abstract itself declares the
non-claims; the evaluation record's §10 verdict is the verification witness),
the canonical module, the primary mapping type per TCS-1.0 §7, and the
proof/evidence status.

A003-specific findings:

1. NO intake row corruptions: all 15 rows quote-check cleanly against the
   inventory list (the policy hypotheses, the three physical mechanism types,
   and the nine numerical-programme objects).

2. NO destination corrections. The split routing of the three taxonomies is
   verified row by row and CONFIRMED as the architecture's intent: the H1/H2
   hypotheses ride Paper 4 because their named instantiations ARE Paper 4's
   registered families (A012's delay-amplified extractive mobilisation = H1;
   A020's protective channel = H2); H3 (inertia/capture — no named
   instantiation in any source) is stated as the response-class taxonomy entry
   in the atlas's institutional-implementation family, joining the A001 quota/
   Ostrom implementation-operator rows; the culling/recruitment-suppression/
   weak-coupling mechanism types ride the papers owning each mechanism's
   treatment (P3 ledger outflow typing; P4 named-core recruitment channel;
   P1-or-monograph weak-coupling composition result, the A018 precedent); the
   nine variant-registry entries ride Paper 4's variant registry supplement
   (the evaluation record's preferred destination), except the sampled-review
   variant which rides Paper 5's sampled-governance content.

3. ONE module correction: CC-A003-003 (H3 inertia/capture/state-dependent
   response) formal_foundations -> observation_governance_empirics — the same
   A001-closure precedent that moved the institutional implementation-operator
   family (quota rescue, Ostrom sufficiency/obstruction/necessity) from
   formal_foundations to observation_governance_empirics: a response law of
   the implementation/deployment operator, not a viability-kernel result.
   TWELVE module classifications (A003 unclassified 12 -> 0): the H1/H2
   response-sign hypotheses -> observation_governance_empirics (the response
   taxonomy types the deployment operator; the evaluation record's §1.4 and
   §8 identify A002's command-deployment distinction as the bridge); the
   recruitment-suppression mechanism type -> ledger_diagnostics (the
   evaluation record's §3 typed-flux reading: it modifies/diverts a
   recruitment flux, one incidence family with culling); the seven P4 variant
   registry entries -> nonlinear_dynamics (the archived stress-test variant
   family of the named delay dynamics); the mapping classifications
   (UNRESOLVED -> resolved) on all twelve.

4. REGISTERED OBLIGATIONS, not discharged artifacts: the nine variant rows
   (CC-A003-007..-015) close as what they are in the source — registry
   entries in §7's variant registry whose equations, parameter files, code,
   and outputs were NOT included in the submitted source (the inventory's own
   closing line; the evaluation record's §6: "Their results cannot be
   verified from this file"). No artifact status is created by closure; each
   row records the reproduction obligation (source equations, parameters,
   scripts/settings, outputs in the research-program registry) at exactly
   that status. Evidence status defined_source_object: the rows' verifiable
   content is the registry entry itself.

5. The source's own status discipline is preserved verbatim in every row:
   the abstract's non-claims (no generalization from H1 to H2/H3; no default
   continuous-delay representation of governance; no universal policy
   threshold), §1's "No result for H1 is generalized to H2 or H3", §3's
   "phenomenological stress-test family unless derived from a domain
   module", the E-interpretation discipline (industry effort / quota
   utilization / institutional control are not interchangeable), §6's
   bifurcation-is-not-sustainability-transition discipline, and §9's
   policy-scope disclaimer.

Same honest boundary: content-level acceptance only; no theorem status
promoted (the structured-persistence conjecture is registered conjecture
content riding the intake rows of other sources — its A003 statement is the
scope frame); no artifact obligation discharged; the §8 interface contract
remains open; the paper-time citation match rides Part III.

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
ND = 'nonlinear_dynamics'
AC = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
DSO = 'defined_source_object'

V: dict[int, dict] = {
    1: dict(kind='policy hypothesis (response-sign taxonomy) verified in source §1 (H1: scarcity-amplifying extraction — the sign condition dG_H1/dZ > 0 over the relevant range; the abstract\'s own non-claim "does not claim that institutions generally behave this way")', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (the response taxonomy types the implementation/deployment operator; A002\'s command-deployment distinction is the bridge per the evaluation record §1.4/§8); destination Paper 4 confirmed — H1\'s named instantiation is A012\'s registered delay-amplified extractive mobilisation family (Paper 4\'s named content); §1\'s non-transfer discipline preserved verbatim: "No result for H1 is generalized to H2 or H3"; the E-interpretation discipline (endogenous industry response / legal quota-utilization state / actual institutional control are not interchangeable) rides §3'),
    2: dict(kind='policy hypothesis (response-sign taxonomy) verified in source §1 (H2: protective restraint/restoration — the reversed or restoration-including effect on extraction)', module=(OG, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified observation_governance_empirics (same response-operator family as H1); destination Paper 4 confirmed — H2\'s named instantiation is A020\'s protective channel (Paper 4\'s two-delay identity content); the source\'s three-hypothesis comparison frame is the interpretive context for both named families'),
    3: dict(kind='policy hypothesis (response-sign taxonomy) verified in source §1 (H3: inertia, capture, or state-dependent response)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module corrected formal_foundations → observation_governance_empirics (the A001-closure precedent: the institutional implementation-operator family — quota rescue, Ostrom sufficiency/obstruction/necessity — is observation_governance_empirics, not a viability-kernel result; a state-dependent response law of the implementation operator); destination Paper 2 confirmed — H3 has NO named instantiation in any source, so it is stated as the response-class taxonomy entry in the atlas\'s institutional-implementation family, joining the A001 implementation-operator rows; the taxonomy split (H1/H2 to P4 with their named families, H3 to the atlas) is recorded as the architecture\'s intent, not an accident'),
    4: dict(kind='physical mechanism type (typed-flux incidence taxonomy) verified in source §2 (standing-stock culling: present extraction removes reproductive stock directly; "A diagnostic label such as "unsustainable portion" never determines physical destination. Material routing is determined by the typed physical module")', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module ledger_diagnostics confirmed (the evaluation record §3 typed-flux reading: culling enters as an outflow from the standing-stock compartment); destination Paper 3 confirmed (the ledger outflow typing is Paper 3\'s primitive-flux content); the diagnostic-threshold-is-not-material-routing discipline preserved verbatim'),
    5: dict(kind='physical mechanism type (typed-flux incidence taxonomy) verified in source §2 (recruitment suppression: present use prevents future recruits without immediate adult removal)', module=(LD, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified ledger_diagnostics (the evaluation record §3: recruitment suppression modifies or diverts a recruitment flux — one typed-flux incidence family with culling and weak coupling); destination Paper 4 confirmed (the mechanism\'s named treatment is the recruitment channel of the P4 cores — A018\'s four-state support-pool recruitment suppression; the three-way distinction as one conceptual object is stated in the source §2 and cross-cited at the seam)'),
    6: dict(kind='physical mechanism type (typed-flux incidence taxonomy) verified in source §2 (weak viability coupling: use has limited or indirect effect on reproduction)', module=(AC, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module architecture_transformation_composition confirmed (the weak-coupling concept is the composition-interface family — the A018 weak-coupling theorem precedent); destination Paper 1 or monograph introduction confirmed (matches the A018 closure\'s weak-coupling composition-result routing); the source\'s §5 alternative-mechanism discipline (an institutional mechanism must be compared with these alternatives rather than identified from periodicity alone) recorded'),
    7: dict(kind='variant registry entry verified in source §7 (ungated variant — one of the nine archived numerical-programme objects; no equations, parameter files, code, or outputs included in the submitted source)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics (the archived stress-test variant family of the named delay dynamics); REGISTERED OBLIGATION, not a discharged artifact: the inventory\'s own closing line and the evaluation record §6 ("Their results cannot be verified from this file") — each variant requires source equations, parameters, scripts or software settings, and outputs in the research-program registry before any numerical claim; the §7 tabulation discipline (governing equations, units/identifiability, equilibrium/boundary conditions, method/mesh/horizon, branch identity, six-status label) is the reproduction obligation\'s content'),
    8: dict(kind='variant registry entry verified in source §7 (gated variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status as the ungated variant); the §3 non-negativity/effort-bounds discipline applies ("Gating, damping, or saturation is not accepted merely because it preserves a desired bifurcation; it must have a constitutive interpretation")'),
    9: dict(kind='variant registry entry verified in source §7 (hybrid-effort variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status)'),
    10: dict(kind='variant registry entry verified in source §7 (four-state support-pool variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status); the named four-state treatment that IS verified lives in the A018 rows (closed) — this row is the registry entry, not a duplicate of A018\'s content; the §3 frozen-A discipline ("a frozen A is a formal limiting case, not a default physical assertion") recorded'),
    11: dict(kind='variant registry entry verified in source §7 (two-channel liquidation variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status); the verified two-channel treatment lives in the A020 rows — this row is the registry entry; cite together at the Paper 4 two-channel section'),
    12: dict(kind='variant registry entry verified in source §7 (stage-structured variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status); the stage-structured THEOREM content is A022/A023\'s Paper 7 conditional rows — this row is the A003 registry entry riding Paper 4\'s variant registry; cite at the seam if Paper 7 is triggered'),
    13: dict(kind='variant registry entry verified in source §7 (sampled-review variant; same no-artifact status)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='module observation_governance_empirics confirmed (the sampled-review variant instantiates §4\'s sampled-governance representation — the primary institutional representation per the source); destination Paper 5 confirmed; REGISTERED OBLIGATION (same §7 no-artifact status); §4\'s bridge discipline recorded: a continuous-delay approximation to the effort equation is admissible only after specifying the review interval, hold rule, implementation lag, and approximation error, and a sampled map can exhibit flip, Neimark-Sacker, or border-collision behavior not captured by continuous-delay Hopf terminology'),
    14: dict(kind='variant registry entry verified in source §7 (thermodynamic-tether variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status)'),
    15: dict(kind='variant registry entry verified in source §7 (unified-core variant; same no-artifact status)', module=(ND, 'classified'), mapping=(EX, 'classified'), evidence=DSO, cite=True,
            extra='module classified nonlinear_dynamics; REGISTERED OBLIGATION (same §7 status); the verified unified-core treatments live in the A018 rows — this row is the registry entry; the §6 safety-relevance ladder (bifurcation existence / persistence under coupling / safety relevance via attractor-basin-tube intersection with the unsafe set) and the structured-persistence conjecture\'s fold caution (transverse normal hyperbolicity does not imply normal hyperbolicity of the fold orbit itself) are the interpretive frame for every variant row'),
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
        if not row['concordance_id'].startswith('CC-A003-'):
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

        parts = [f'Row-closed {DATE} (A003 scientific pass; source read in full): {d["kind"]}; '
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
    print(f'A003 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 239 + 15, f'expected 254 closed rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
