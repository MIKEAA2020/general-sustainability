#!/usr/bin/env python3
"""Scientific row-closure pass for source A001 (uploads/topdown.txt).

Executed 2026-08-27. This is the scientific layer of the concordance
row-closure campaign (the machine layer is reaudit/verify_concordance_rows.py:
quotes, coverage, vocabulary). The full source article A001 was read in
full; every inventoried item was located in the source; for each row this
pass verifies:

  1. item existence, kind, and proof presence in the source (the deferred
     line check);
  2. the canonical_module assignment (classifying intake-unclassified rows;
     correcting mis-classified rows);
  3. the primary_mapping type per TCS-1.0 section 7 semantics;
  4. the proof_evidence_status where the intake heuristic mis-typed the
     item's kind;
  5. the item_type/source_item pair where the intake builder's naive
     pipe-split corrupted the row (Theorems 11.1-11.4 and 16.1; the A001
     inventory lines 72 and 97 were also repaired to the source-faithful
     single-backslash norm notation).

What this pass does NOT do (honest boundary): it promotes no theorem status
(TCS-1.0 section 6 statuses are untouched), proves no interface contract
(the section 8 producer/consumer obligation stays in interface_dependency),
and performs no paper-time citation check (the Part III paper-support
discipline owns that). mapping_status moves to accepted_mapping at the
CONTENT level only: the mapping TYPE and the exact source assumptions are
verified; theorem transfer between modules still requires the section 8
contract.

Idempotent: rows already carrying review_state 'row_verified' are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-27'

FF = 'formal_foundations'
OG = 'observation_governance_empirics'
ND = 'nonlinear_dynamics'
LD = 'ledger_diagnostics'
AT = 'architecture_transformation_composition'
EX = 'EXACT_SPECIALIZATION'
CL = 'COUNTEREXAMPLE_OR_LIMIT'
PIC = 'proof_inventory_present_line_check_required'
DSO = 'defined_source_object'

# ---------------------------------------------------------------------------
# The per-row verification table.
# kind: short description of what was verified in the source.
# module: (final value, verdict) where verdict in
#         {'confirmed', 'classified', 'corrected'}; 'classified' rows were
#         unclassified at intake; 'corrected' rows had a wrong intake value.
# mapping: (final value, verdict) same convention.
# evidence: final value or None to keep the intake value; verdict string.
# repair: (item_type, source_item) or None.
# dest: destination override or None.
# extra: additional note fragment or None.
# ---------------------------------------------------------------------------
V: dict[int, dict] = {
    1: dict(kind='theorem + proof verified in source §2.5', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    2: dict(kind='theorem + proof verified in source §2.5', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    3: dict(kind='theorem + proof verified in source §2.5 (uncoupled product identity; coupling failure cross-references §10.3–10.4)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    4: dict(kind='theorem + proof verified in source §2.5 (Nagumo face/kernel distinction; logistic counterexample inside the proof)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    5: dict(kind='theorem + proof verified in source §2.6', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    6: dict(kind='theorem + proof verified in source §2.6', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    7: dict(kind='proposition + proof verified in source §3.1', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    8: dict(kind='corollary verified in source §3.1 (impossibility/triviality of recovery-resilience definitions on the kernel boundary)', module=(FF, 'confirmed'), mapping=(CL, 'corrected'), evidence=None,
            extra='mapping corrected to COUNTEREXAMPLE_OR_LIMIT: the corollary establishes that recovery-into-the-while-staying-in-V is identically impossible outside the kernel — a boundary result, not a positive specialization'),
    9: dict(kind='definition verified in source §3.2', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    10: dict(kind='definition verified in source §3.3', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    11: dict(kind='definition verified in source §3.4', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    12: dict(kind='definition verified in source §3.4', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=DSO,
            extra='evidence corrected to defined_source_object (intake had source_specific_empirical_status_check_required — this is a definition, not an empirical object)', cite=True),
    13: dict(kind='proposition + proof verified in source §3.4', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    14: dict(kind='definition verified in source §4.1', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    15: dict(kind='definition verified in source §4.2', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    16: dict(kind='definition verified in source §4.3', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    17: dict(kind='theorem + proof verified in source §4.4', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    18: dict(kind='corollary verified in source §4.4 (no separate proof; follows from Theorem 4.1 via the causal inverse)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    19: dict(kind='proposition + proof verified in source §4.4', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    20: dict(kind='theorem + proof verified in source §4.5 (explicit constant-observation construction emptying a nonempty physical kernel)', module=(OG, 'confirmed'), mapping=(CL, 'corrected'), evidence=None,
             extra='mapping corrected to COUNTEREXAMPLE_OR_LIMIT: the theorem is an impossibility witness (EViab = ∅ despite Viab = V ≠ ∅), the canonical epistemic-contraction boundary'),
    21: dict(kind='theorem + proof + numerical check verified in source §4.5 (Hayes characteristic equation; complete delay-margin classification)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    22: dict(kind='theorem + proof verified in source §4.6 (six hypotheses; observer convergence absorbing Lipschitz error)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — the observer/estimation channel is the assessment operator of the canonical execution chain, same family as Prop 4.1'),
    23: dict(kind='theorem + proof verified in source §4.7 (regulation map; measurable selection; discriminating-kernel converse)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    24: dict(kind='theorem + proof verified in source §4.8 (finite-horizon induction + Knaster–Tarski greatest fixed point)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    25: dict(kind='definition verified in source §4.8', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None, cite=True,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — belief-size reduction through actions is the information channel'),
    26: dict(kind='theorem verified in source §4.9 (no separate proof block; the argument is inline and Example 4.1 is the witness)', module=(OG, 'confirmed'), mapping=(CL, 'confirmed'), evidence=None),
    27: dict(kind='explicit example verified in source §4.9 (hidden-mode conflict: two individually viable states, no common safe action)', module=(OG, 'confirmed'), mapping=(CL, 'corrected'), evidence=None,
             extra='mapping corrected to COUNTEREXAMPLE_OR_LIMIT: the example is an impossibility witness for common-action viability, not a positive specialization'),
    28: dict(kind='theorem + proof verified in source §4.9 (Dini-inequality exit bound before the next informative observation)', module=(OG, 'corrected'), mapping=(CL, 'confirmed'), evidence=None, dest='Paper 5',
             extra='module corrected to observation_governance_empirics (intake: nonlinear_dynamics) and destination corrected Paper 4 → Paper 5: the delay here is the observation interval T_obs (information timing — Paper 5\'s review-interval spectrum), not an RFDE; the source itself calls it "information may be accurate but arrive too late"'),
    29: dict(kind='theorem + proof verified in source §4.10 (strict barrier margins absorbing observer error)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — output-feedback/observer-error family, consistent with Theorem 4.4 and Prop 4.1'),
    30: dict(kind='proposition + proof verified in source §4.10 (conditional tubular erosion — the corrected Operator-I erosion record governs this row)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    31: dict(kind='definition verified in source §5.1', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    32: dict(kind='theorem + proof verified in source §5.2', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    33: dict(kind='theorem + proof verified in source §5.3 (finite-time exit certificate; the engine behind the §5.6 harvest-floor obstruction)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    34: dict(kind='definition verified in source §5.4', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    35: dict(kind='proposition + proof verified in source §6.1', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    36: dict(kind='theorem + proof verified in source §6.2 (Gronwall comparison + order-upper-set equivalence)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    37: dict(kind='theorem + proof verified in source §6.3 (necessity of (i)–(iv), sufficiency, maximality; the central scalar kernel theorem)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    38: dict(kind='corollary + inline derivation verified in source §6.3 (constrained-MSY formula with the floor-above-MSY correction and the exact overstatement identity)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    39: dict(kind='theorem + proof verified in source §6.4', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    40: dict(kind='theorem + proof verified in source §6.5', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    41: dict(kind='theorem + proof verified in source §6.5', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    42: dict(kind='proposition + proof verified in source §6.6 (four-stock mass balance under the declared closure)', module=(LD, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    43: dict(kind='theorem + proof verified in source §6.7 (Kamke comparison dominance; frozen-slice inner bound; curve frontier where g_K < 0)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    44: dict(kind='theorem + proof verified in source §7.2', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    45: dict(kind='lemma + proof verified in source §7.2 (scalar concave capital kernel)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    46: dict(kind='definition verified in source §7.3', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    47: dict(kind='theorem + proof verified in source §7.3', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    48: dict(kind='theorem + proof verified in source §7.4 (distributional floors raising the effective harvest floor; restricted sharing as control-set restriction)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    49: dict(kind='theorem + five-case proof verified in source §8.2 (dimensionally correct CES net-surplus classification)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    50: dict(kind='corollary + proof verified in source §8.2 (σ = 1 essentiality and unbounded-substitution thresholds)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    51: dict(kind='theorem + proof verified in source §9 (cumulative-extraction budget identity)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    52: dict(kind='corollary verified in source §9 (strong-sustainability budget; Hartwick contrast — follows from Theorem 9.1 by direct integration)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    53: dict(kind='theorem + proof verified in source §10.1 (Kamke comparison; upper-set structure for cooperative minimal-harvest fields)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    54: dict(kind='theorem + proof verified in source §10.2 (planar equilibrium criterion via strong monotonicity + Poincaré–Bendixson)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    55: dict(kind='explicit counterexample verified in source §10.3 (emptiness despite factorwise viability at MSY)', module=(FF, 'confirmed'), mapping=(CL, 'confirmed'), evidence=None),
    56: dict(kind='explicit example verified in source §10.4 (coupling creates viability absent in a factor; equilibrium-defined floors)', module=(AT, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    57: dict(kind='proposition + proof verified in source §10.5 (genericity via proper algebraic hypersurfaces; transversality/nondegenerarity conditions stated)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
            extra='the intake conditional_or_open flag reflects the genericity qualification, retained: the proposition is proved for an open dense parameter set, not universally'),
    58: dict(kind='explicit example verified in source §10.5 (identical-patch orbital barrier; Cauchy problem for the frontier with a numerical bracket Γ(0.12) ∈ (0.25, 0.38))', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None,
            extra='the numerical bracket is a source-stated sample check, not a validated computation — no artifact status is created'),
    59: dict(kind='theorem + proof verified in source §10.6 (quartic equilibrium criterion; Sturm decidability)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    60: dict(kind='theorem + proof verified in source §10.7 (corner Nagumo condition)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    61: dict(kind='theorem + proof verified in source §11.2 (finite cascade termination)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=PIC,
            repair=('Theorem 11.1.', 'For finite $V$, monotone loads, irreversible failures: the cascade terminates in at most $\\|V\\| - \\|F_0\\|$ strict rounds.'),
            extra='item_type/source_item REPAIRED — the intake builder\'s naive pipe-split corrupted this row to the fragments "F_0\\ / $ strict rounds."; the true label and description restored from the source §11.2'),
    62: dict(kind='theorem + proof verified in source §11.3 (k-redundancy containment)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=PIC,
            repair=('Theorem 11.2 ($k$-redundancy).', 'If every node is $k$-redundant and $\\|F_0\\| \\leq k$: $F_\\infty = F_0$.'),
            extra='item_type/source_item REPAIRED — same intake pipe-split corruption; true label and description restored from the source §11.3'),
    63: dict(kind='theorem + proof verified in source §11.3 (row-sum containment)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=PIC,
            repair=('Theorem 11.3 (Row-sum containment).', 'If $\\|M\\|_\\infty < 1$ with $M_{ij} = a_{ji}/\\theta_i$: $F_\\infty = F_0$ for every seed.'),
            extra='item_type/source_item REPAIRED — same intake pipe-split corruption; true label and description restored from the source §11.3 (inventory line 72 also repaired to the source-faithful single-backslash norm notation)'),
    64: dict(kind='theorem + proof verified in source §11.4 (nilpotent-chain construction refuting finite spectral-radius bounds)', module=(FF, 'classified'), mapping=(CL, 'confirmed'), evidence=PIC,
            repair=('Theorem 11.4.', 'There is no finite uniform bound on $\\|F_\\infty \\setminus F_0\\|$ in terms of $\\rho(M) < 1$ alone.'),
            extra='item_type/source_item REPAIRED — same intake pipe-split corruption; true label and description restored from the source §11.4; the refutation role (abstract: "a nilpotent-chain construction refutes spectral-radius cascade bounds") makes COUNTEREXAMPLE_OR_LIMIT the correct mapping type'),
    65: dict(kind='theorem + proof verified in source §11.5 (dynamic cascade safety under a protection set)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    66: dict(kind='definition verified in source §12.1', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    67: dict(kind='lemma + proof verified in source §12.1 (Rosen diagonal strict concavity; negative-definite Hessian computation)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    68: dict(kind='theorem + proof verified in source §12.2 (Nash over-extraction with the strictness and corner cases; the decoupled-equality caveat is in the source)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    69: dict(kind='theorem + proof verified in source §12.3 (commons obstruction via the Theorem 5.2 mechanism)', module=(AT, 'confirmed'), mapping=(CL, 'confirmed'), evidence=None),
    70: dict(kind='corollary + proof verified in source §12.4 (quota rescue via sanctions and Theorem 6.2)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — quotas and sanctions are institutional implementation operators (§13 family)'),
    71: dict(kind='theorem + proof verified in source §13.2 (institutional equivalence through induced objects)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    72: dict(kind='definition verified in source §13.3', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    73: dict(kind='theorem + proof verified in source §13.3 (institutionally robust safe prescriptions)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    74: dict(kind='theorem + proof verified in source §13.4 (sanction sufficiency)', module=(OG, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    75: dict(kind='theorem + proof verified in source §13.5 (Ostrom sufficiency: eight translations + Theorem 6.2 conditions ⇒ nonempty kernel)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — the Ostrom principles are mechanisms on the institutional implementation operator'),
    76: dict(kind='theorem + proof verified in source §13.5 (eight constructions, one per principle, each emptying the kernel)', module=(OG, 'corrected'), mapping=(CL, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — same Ostrom family as Theorem 13.5'),
    77: dict(kind='definition verified in source §13.6 (primitive constructors)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=DSO, cite=True,
            extra='evidence corrected to defined_source_object (intake had source_specific_empirical_status_check_required — this is a definition, not an empirical object); module classified architecture_transformation_composition (the constructor algebra operates on the architecture tuple)'),
    78: dict(kind='definition verified in source §13.6 (implementation lattices)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    79: dict(kind='proposition + proof verified in source §13.6 (downward closure; InvLat ⊆ Inst)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    80: dict(kind='theorem + proof verified in source §13.6 (invariance under irrelevant structure)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    81: dict(kind='corollary + proof verified in source §13.6 (management vocabularies as constructor rewrites — the formal completion rule)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=PIC, cite=True,
            extra='module classified architecture_transformation_composition; evidence corrected to proof_inventory_present_line_check_required (intake had conditional_or_open — the corollary carries a proof on the line in §13.6)'),
    82: dict(kind='definition verified in source §14.1', module=(AT, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    83: dict(kind='theorem verified in source §14.1 (immediate equivalence when V^(k) ≡ V; no separate proof)', module=(AT, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    84: dict(kind='theorem + proof verified in source §14.2 (nested-empty-intersection impossibility under compactness)', module=(AT, 'confirmed'), mapping=(CL, 'corrected'), evidence=None,
             extra='mapping corrected to COUNTEREXAMPLE_OR_LIMIT: the theorem establishes nonexistence of intergenerationally viable paths — an impossibility result; the compactness hypothesis is essential and stated'),
    85: dict(kind='theorem + proof verified in source §14.3 (explicit discount-rate threshold preferring an exiting pulse)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    86: dict(kind='definition verified in source §15.1', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    87: dict(kind='definition verified in source §15.2', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    88: dict(kind='theorem + proof verified in source §16 (input-tolerance compositional viability — the small-gain-style composition theorem)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=PIC,
            repair=('Theorem 16.1 (Compositional viability).', 'Suppose each subsystem has an input tolerance $\\bar z_i$ such that $\\|z_i\\| \\leq \\bar z_i$ implies $\\exists\\, u_i : D^+ b_i(x_i) \\geq 0$ on $\\partial Q_i$. If'),
            extra='item_type/source_item REPAIRED — the intake pipe-split corrupted this row to the fragments "z_i\\\\ / \\leq \\bar z_i$ implies ..."; true label and description restored from the source §16 (inventory line 97 also repaired to the source-faithful norm notation); module classified architecture_transformation_composition — this is THE composition theorem of the source'),
    89: dict(kind='definition verified in source §17', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    90: dict(kind='definition verified in source §17', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None, cite=True),
    91: dict(kind='theorem + proof verified in source §17 (stopping-time localization; Markov bound; Remark 17.1\'s horizon split governs the reading)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    92: dict(kind='conjecture + falsification criterion verified in source §17 (competitive OLG; the myopic common-property special case is Remark 17.2)', module=(AT, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    93: dict(kind='conjecture + falsification criterion verified in source §17 — the source itself DEMOTED the infinite-horizon claim (Remark 17.1: only the finite-horizon part stands, as Theorem 17.1); the row title already carries the corrected finite-horizon-only form', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    94: dict(kind='conjecture + falsification criterion verified in source §17 (adaptive management beyond high gain)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — adaptive observers/parameter learning are the assessment channel'),
    95: dict(kind='open problem verified in source §18 (hybrid kernel off the Theorem 11.5 protection set)', module=(FF, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    96: dict(kind='open problem verified in source §18 (binary-sensor threshold discretization)', module=(OG, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    97: dict(kind='conjecture + falsification criterion verified in source §18 (n-patch super-equilibrium equivalence; cooperative scope with competitive failure noted in the source)', module=(ND, 'confirmed'), mapping=(EX, 'confirmed'), evidence=None),
    98: dict(kind='conjecture + falsification criterion verified in source §18 (multi-resource Hartwick)', module=(FF, 'classified'), mapping=(EX, 'confirmed'), evidence=None),
    99: dict(kind='conjecture + falsification criterion verified in source §18 (Ostrom individual necessity)', module=(OG, 'corrected'), mapping=(EX, 'confirmed'), evidence=None,
             extra='module corrected to observation_governance_empirics (intake: formal_foundations) — same Ostrom family as Theorems 13.5–13.6'),
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
    return f'mapping {val} corrected (intake: {intake_mapping})'


def main() -> None:
    with open(CC, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    n_closed = n_skipped = 0
    for row in rows:
        if not row['concordance_id'].startswith('CC-A001-'):
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

        # --- repairs
        if d.get('repair'):
            row['item_type'], row['source_item'] = d['repair']
        if d.get('dest'):
            row['destination_paper'] = d['dest']

        # --- classification acceptance
        row['canonical_module'] = d['module'][0]
        row['primary_mapping'] = d['mapping'][0]
        row['mapping_status'] = 'accepted_mapping'
        if d.get('evidence'):
            row['proof_evidence_status'] = d['evidence']
        row['review_state'] = 'row_verified'

        parts = [f'Row-closed {DATE} (A001 scientific pass; source read in full): {d["kind"]}; '
                 f'{module_verdict_str(d["module"], intake_module)}; {mapping_verdict_str(d["mapping"], intake_mapping)}.']
        ev = d.get('evidence')
        if ev is not None:
            parts.append(f'Evidence status now {ev} (see extra note where corrected).')
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
    print(f'A001 scientific row-closure: {n_closed} rows closed, {n_skipped} skipped (already closed).')
    print(f'Concordance review states now: {dict(rev)}')
    assert rev['row_verified'] == 99, f'expected 99 closed A001 rows, got {rev["row_verified"]}'


if __name__ == '__main__':
    main()
