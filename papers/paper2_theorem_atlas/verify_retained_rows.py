#!/usr/bin/env python3
"""Manuscript self-check for Paper 2 (papers/paper2_theorem_atlas/manuscript.md).

Run from the repository root:

    python3 papers/paper2_theorem_atlas/verify_retained_rows.py

Checks (idempotent, stdlib only):
  1. Extracts the retained set: the Paper-2 budget rows (tier 'main' or
     'bounded_appendix' in research_program/paper2_retained_row_budget.csv)
     plus the nineteen closure-campaign seam rows restored into the atlas
     (RESTORED_SEAM_ROWS below), each verified against the concordance.
  2. Parses manuscript.md for every CC-A0XX-YYY identifier.
  3. Checks every cited ID resolves in the concordance.
  4. Checks the cited set equals the retained set exactly (the atlas cites
     no undeclared cross-references: every cited row is retained here).
  5. Checks the status ledger table contains every retained row exactly once
     (and no non-retained concordance rows).
  6. Prints PASS/FAIL per check; exits nonzero on any failure.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
CC_CSV = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
BUDGET_CSV = REPO / 'research_program' / 'paper2_retained_row_budget.csv'
MANUSCRIPT = REPO / 'papers' / 'paper2_theorem_atlas' / 'manuscript.md'

MAIN_DEST = 'Paper 2'
EXPECTED_BUDGET_RETAINED = 70  # 63 main + 7 bounded_appendix

# The closure-campaign seam rows: routed to Paper 2 by the 2026-08-28
# destination passes and seam closures over the seven further closed sources
# (A003, A005, A006, A007, A010, A013, A018) and stated in the manuscript at
# exactly their verified statuses. Each carries the manuscript location.
RESTORED_SEAM_ROWS: dict[str, str] = {
    'CC-A006-004': 'Lemma 3.5 — stability and safety are independent',
    'CC-A010-009': 'Proposition 4.6 — geological/support-pool noninvariance',
    'CC-A007-001': 'Lemma 5.6 — compensatory reporting limit',
    'CC-A013-001': 'Proposition 5.7 — witness construction (seam: Paper 3 §9.1)',
    'CC-A018-001': 'Proposition 5.8 — no scalar weighting (seam: Paper 3 §9.1)',
    'CC-A006-008': 'Proposition 6.12 — common-action obstruction, output feedback',
    'CC-A006-009': 'Proposition 6.13 — conditional observer-to-safety transfer',
    'CC-A007-002': 'Lemma 6.14 — static diagnostic aliasing',
    'CC-A006-014': 'Template 6.15 — safe learning',
    'CC-A010-004': 'Section 9 restatement record — logistic variance correction',
    'CC-A010-005': 'Section 9 restatement record — general C2 curvature bound',
    'CC-A018-006': 'Conjecture 9.6 — finite-time five-state reduction (seam: Paper 4 §4.3)',
    'CC-A010-013': 'Proposition 10.3 — effort sensitivity coefficients',
    'CC-A010-014': 'Proposition 10.4 — interior effort upper bound',
    'CC-A003-003': 'Hypothesis object 12.3 — H3 response-sign hypothesis (seam: Paper 4 §8.1)',
    'CC-A005-006': 'Hypothesis object 12.3 — groundwater institutional-hypothesis restatement',
    'CC-A006-005': 'Definition 12.4 — finite-horizon epistemic-institutional kernel (seam: Paper 5 §4.4)',
    'CC-A006-006': 'Conditional Theorem 12.5 — sampled epistemic-institutional viability (seam: Paper 5 §4.4)',
    'CC-A002-050': 'Programme 13.3 — justice and multiscale viability',
}

ID_RE = re.compile(r'CC-A\d{3}-\d{3}')


def load_concordance() -> dict[str, dict[str, str]]:
    with open(CC_CSV, newline='', encoding='utf-8') as f:
        return {r['concordance_id']: r for r in csv.DictReader(f)}


def budget_retained() -> set[str]:
    with open(BUDGET_CSV, newline='', encoding='utf-8') as f:
        return {r['concordance_id'] for r in csv.DictReader(f)
                if r['retention_tier'] in ('main', 'bounded_appendix')}


def main() -> int:
    failures: list[str] = []

    # Check 1: extract the retained set (budget + restored seam rows).
    rows = load_concordance()
    budget = budget_retained()
    retained = budget | set(RESTORED_SEAM_ROWS)
    print(f'Check 1 (extract retained set): budget={len(budget)} '
          f'restored-seam={len(RESTORED_SEAM_ROWS)} total={len(retained)}')
    if len(budget) != EXPECTED_BUDGET_RETAINED:
        failures.append(f'Check 1 FAIL: expected {EXPECTED_BUDGET_RETAINED} budget rows, '
                        f'got {len(budget)}')
    unresolved_seam = sorted(set(RESTORED_SEAM_ROWS) - set(rows))
    if unresolved_seam:
        failures.append(f'Check 1 FAIL: seam rows not in concordance: {unresolved_seam}')
    misrouted = sorted(i for i in RESTORED_SEAM_ROWS
                       if i in rows and rows[i]['destination_paper'] != MAIN_DEST)
    if misrouted:
        failures.append(f'Check 1 FAIL: seam rows not routed to Paper 2: {misrouted}')
    if not failures:
        print('Check 1: PASS')

    # Check 2: parse the manuscript for every cited CC identifier.
    text = MANUSCRIPT.read_text(encoding='utf-8')
    cited = set(ID_RE.findall(text))
    print(f'Check 2 (parse cited identifiers): {len(cited)} distinct CC IDs cited')

    # Check 3: every cited ID resolves in the concordance.
    unresolved = sorted(cited - set(rows))
    if unresolved:
        failures.append(f'Check 3 FAIL: cited IDs not in concordance: {unresolved}')
    else:
        print('Check 3 (cited IDs resolve): PASS')

    # Check 4: cited set == retained set (no undeclared cross-references).
    extra = sorted(cited - retained)
    missing = sorted(retained - cited)
    if extra or missing:
        if extra:
            failures.append(f'Check 4 FAIL: cited but not retained: {extra}')
        if missing:
            failures.append(f'Check 4 FAIL: retained rows never cited in manuscript: {missing}')
    else:
        print('Check 4 (cited set == retained set exactly): PASS')

    # Check 5: the status ledger table contains every retained row exactly once.
    m = re.search(r'^## 14 Status ledger\s*$(.*?)(?=^## )', text, flags=re.M | re.S)
    if m is None:
        failures.append('Check 5 FAIL: status ledger section (## 14) not found')
    else:
        ledger_text = m.group(1)
        ledger_ids: list[str] = []
        for line in ledger_text.splitlines():
            if not line.startswith('|'):
                continue
            cells = [c.strip() for c in line.split('|')]
            # The P column carries the concordance ID (cells: | # | P | ...).
            for c in cells:
                if ID_RE.fullmatch(c):
                    ledger_ids.append(c)
                    break
        dup = sorted({i for i in ledger_ids if ledger_ids.count(i) > 1})
        not_retained_in_ledger = sorted(set(ledger_ids) - retained)
        missing_from_ledger = sorted(retained - set(ledger_ids))
        if dup or not_retained_in_ledger or missing_from_ledger:
            if dup:
                failures.append(f'Check 5 FAIL: ledger duplicates: {dup}')
            if not_retained_in_ledger:
                failures.append(f'Check 5 FAIL: ledger rows not in retained set: '
                                f'{not_retained_in_ledger}')
            if missing_from_ledger:
                failures.append(f'Check 5 FAIL: retained rows absent from ledger: '
                                f'{missing_from_ledger}')
        else:
            print(f'Check 5 (ledger contains every retained row exactly once; '
                  f'{len(ledger_ids)} concordance rows): PASS')

    print()
    if failures:
        for f_ in failures:
            print(f_)

    print('RESULT: ' + ('PASS' if not failures else 'FAIL'))
    return 0 if not failures else 1


if __name__ == '__main__':
    sys.exit(main())
