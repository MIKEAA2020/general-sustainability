#!/usr/bin/env python3
"""Manuscript self-check for Paper 3 (papers/paper3_material_ledgers/manuscript.md).

Run from the repository root:

    python3 papers/paper3_material_ledgers/verify_retained_rows.py

Checks (idempotent, stdlib only):
  1. Extracts the retained set from the canonical concordance
     (destination 'Paper 3').
  2. Parses manuscript.md for every CC-A0XX-YYY identifier.
  3. Checks every cited ID resolves in the concordance.
  4. Checks the cited set equals the retained set plus exactly the declared
     cross-references (each declared with a one-phrase reason and its owning
     destination verified not to be Paper 3).
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
MANUSCRIPT = REPO / 'papers' / 'paper3_material_ledgers' / 'manuscript.md'

MAIN_DEST = 'Paper 3'

# Declared cross-references: concordance rows cited in the manuscript that are
# owned by other papers of the architecture, with a one-phrase reason.
DECLARED_CROSS_REFERENCES: dict[str, str] = {
    'CC-A002-005': 'Paper 1 owner: diagnostic types and the no-transfer rule invoked as architecture context',
    'CC-A002-011': 'Paper 2 owner (atlas Thm 4.3; destination Paper 4): parent nonnegative-invariance theorem behind the retained donor-limitation corollary',
    'CC-A002-036': 'Paper 2 owner: projectability criterion (the family of the retained triangular projection)',
    'CC-A002-040': 'Paper 2 owner: canonical local-horizon bracket (the retained A010 row is the predecessor statement)',
    'CC-A003-001': 'Paper 4 owner: H1 scarcity-amplifying statement named at the groundwater template ladder (row-note citation directive)',
    'CC-A003-002': 'Paper 4 owner: H2 protective statement named at the groundwater template ladder (row-note citation directive)',
    'CC-A013-001': 'Paper 2 owner: compensatory witness construction behind the accounting-side rejection',
    'CC-A018-001': 'Paper 2 owner: no-scalar proposition (twin witness of the same rejection)',
    'CC-A018-007': 'Paper 4 owner: working/QSS closures owning the open-projection approximation content separated from the retained conservation theorem',
    'CC-A024-001': 'Paper 5 owner: model-hitting-time versus constructed-proxy scoping distinction',
    'CC-A024-008': 'Paper 5 owner: parameter and observation uncertainty cautions of the first-passage surrogates',
}

ID_RE = re.compile(r'CC-A\d{3}-\d{3}')


def load_concordance() -> dict[str, dict[str, str]]:
    with open(CC_CSV, newline='', encoding='utf-8') as f:
        return {r['concordance_id']: r for r in csv.DictReader(f)}


def retained_set(rows: dict[str, dict[str, str]]) -> set[str]:
    return {i for i, r in rows.items() if r['destination_paper'] == MAIN_DEST}


def main() -> int:
    failures: list[str] = []

    # Check 1: extract the retained set.
    rows = load_concordance()
    retained = retained_set(rows)
    print(f'Check 1 (extract retained set): {len(retained)} rows routed to {MAIN_DEST}')
    if len(retained) != 52:
        failures.append(f'Check 1 FAIL: expected 52 retained rows, got {len(retained)}')
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
        if i in rows and rows[i]['destination_paper'] == MAIN_DEST
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
            failures.append(f'Check 4 FAIL: declared cross-references routed to Paper 3: {bad_owner}')
        if unused_decl:
            failures.append(f'Check 4 FAIL: declared cross-references never cited: {unused_decl}')
    else:
        print(f'Check 4 (cited set == retained + {len(DECLARED_CROSS_REFERENCES)} declared '
              f'cross-references): PASS')

    # Check 5: the status ledger table contains every retained row exactly once.
    m = re.search(r'^## 10 Status ledger\s*$(.*?)(?=^## )', text, flags=re.M | re.S)
    if m is None:
        failures.append('Check 5 FAIL: status ledger section (## 10) not found')
    else:
        ledger_text = m.group(1)
        # Count identifiers in the ID column (first cell) of each ledger table row.
        ledger_ids: list[str] = []
        for line in ledger_text.splitlines():
            if not line.startswith('|'):
                continue
            first_cell = line.split('|')[1].strip()
            i = ID_RE.fullmatch(first_cell)
            if i:
                ledger_ids.append(i.group(0))
        counts: dict[str, int] = {}
        for i in ledger_ids:
            counts[i] = counts.get(i, 0) + 1
        dupes = sorted(i for i, c in counts.items() if c > 1)
        absent = sorted(retained - set(counts))
        foreign = sorted(set(counts) - retained)
        if dupes or absent or foreign:
            if dupes:
                failures.append(f'Check 5 FAIL: retained rows appearing more than once in the ledger: {dupes}')
            if absent:
                failures.append(f'Check 5 FAIL: retained rows missing from the ledger: {absent}')
            if foreign:
                failures.append(f'Check 5 FAIL: non-retained concordance rows in the ledger: {foreign}')
        else:
            native_rows = len(re.findall(r'^\|\s*MS-Native-\d+\s*\|', ledger_text, flags=re.M))
            print(f'Check 5 (ledger contains every retained row exactly once; '
                  f'{len(counts)} concordance rows + {native_rows} manuscript-native rows): PASS')

    # Check 6: summary.
    print()
    if failures:
        for f_ in failures:
            print(f_)
        print('RESULT: FAIL')
        return 1
    print('All checks passed.')
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
