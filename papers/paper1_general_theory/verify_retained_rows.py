#!/usr/bin/env python3
"""Manuscript self-check for Paper 1 (papers/paper1_general_theory/manuscript.md).

Run from the repository root:

    python3 papers/paper1_general_theory/verify_retained_rows.py

Checks (idempotent, stdlib only):
  1. Extracts the retained set from the canonical concordance
     (destinations 'Paper 1 or monograph introduction' and
     'Paper 1 if independent-result gate; otherwise Paper 2' — the
     independent-result gate closed in favour of Paper 1).
  2. Parses manuscript.md for every CC-A0XX-YYY identifier.
  3. Checks every cited ID resolves in the concordance.
  4. Checks the cited set equals the retained set plus exactly the declared
     cross-references (each declared with a one-phrase reason and its owning
     destination verified not to be Paper 1).
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
MANUSCRIPT = REPO / 'papers' / 'paper1_general_theory' / 'manuscript.md'

MAIN_DESTS = ('Paper 1 or monograph introduction',
              'Paper 1 if independent-result gate; otherwise Paper 2')
EXPECTED_RETAINED = 21  # 18 routed rows + 3 independent-result-gate rows

# Declared cross-references: concordance rows cited in the manuscript that are
# owned by other papers of the architecture, with a one-phrase reason.
DECLARED_CROSS_REFERENCES: dict[str, str] = {
    'CC-A002-007': 'Paper 2 owner: domain-qualified noncompensation proposition invoked at the typed-framework statement',
}

ID_RE = re.compile(r'CC-A\d{3}-\d{3}')


def load_concordance() -> dict[str, dict[str, str]]:
    with open(CC_CSV, newline='', encoding='utf-8') as f:
        return {r['concordance_id']: r for r in csv.DictReader(f)}


def retained_set(rows: dict[str, dict[str, str]]) -> set[str]:
    return {i for i, r in rows.items() if r['destination_paper'] in MAIN_DESTS}


def main() -> int:
    failures: list[str] = []

    # Check 1: extract the retained set.
    rows = load_concordance()
    retained = retained_set(rows)
    print(f'Check 1 (extract retained set): {len(retained)} rows routed to Paper 1')
    if len(retained) != EXPECTED_RETAINED:
        failures.append(f'Check 1 FAIL: expected {EXPECTED_RETAINED} retained rows, '
                        f'got {len(retained)}')
    else:
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

    # Check 4: cited set == retained set + declared cross-references.
    allowed = retained | set(DECLARED_CROSS_REFERENCES)
    extra = sorted(cited - allowed)
    missing = sorted(retained - cited)
    undeclared = sorted(cited - retained - set(DECLARED_CROSS_REFERENCES))
    bad_owner = sorted(
        i for i in DECLARED_CROSS_REFERENCES
        if i in rows and rows[i]['destination_paper'] in MAIN_DESTS
    )
    unused_decl = sorted(set(DECLARED_CROSS_REFERENCES) - cited)
    if extra or missing or undeclared or bad_owner or unused_decl:
        if extra:
            failures.append(f'Check 4 FAIL: cited but not retained/declared: {extra}')
        if missing:
            failures.append(f'Check 4 FAIL: retained rows never cited in manuscript: {missing}')
        if undeclared:
            failures.append(f'Check 4 FAIL: cited cross-references not declared: {undeclared}')
        if bad_owner:
            failures.append(f'Check 4 FAIL: declared cross-references routed to Paper 1: {bad_owner}')
        if unused_decl:
            failures.append(f'Check 4 FAIL: declared cross-references never cited: {unused_decl}')
    else:
        print(f'Check 4 (cited set == retained + {len(DECLARED_CROSS_REFERENCES)} declared '
              f'cross-references): PASS')

    # Check 5: the status ledger table contains every retained row exactly once.
    m = re.search(r'^## 11 Status ledger\s*$(.*?)(?=^## )', text, flags=re.M | re.S)
    if m is None:
        failures.append('Check 5 FAIL: status ledger section (## 11) not found')
    else:
        ledger_text = m.group(1)
        ledger_ids: list[str] = []
        for line in ledger_text.splitlines():
            if not line.startswith('|'):
                continue
            cells = [c.strip() for c in line.split('|')]
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
