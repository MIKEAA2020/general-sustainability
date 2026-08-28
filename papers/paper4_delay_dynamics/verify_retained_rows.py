#!/usr/bin/env python3
"""Manuscript self-check for Paper 4 (papers/paper4_delay_dynamics/manuscript.md).

Run from the repository root:

    python3 papers/paper4_delay_dynamics/verify_retained_rows.py

Checks (idempotent, stdlib only):
  1. Extracts the retained sets from the canonical concordance
     (main 'Paper 4' + appendix 'Paper 4 appendix or compendium').
  2. Parses manuscript.md for every CC-A0XX-YYY identifier.
  3. Checks every cited ID resolves in the concordance.
  4. Checks the cited set equals the retained set plus exactly the declared
     cross-references (each declared with a one-phrase reason and its owning
     destination verified to be another paper).
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
MANUSCRIPT = REPO / 'papers' / 'paper4_delay_dynamics' / 'manuscript.md'

MAIN_DEST = 'Paper 4'
APPENDIX_DEST = 'Paper 4 appendix or compendium'

# Declared cross-references: concordance rows cited in the manuscript that are
# owned by other papers of the architecture, with a one-phrase reason.
DECLARED_CROSS_REFERENCES: dict[str, str] = {
    'CC-A002-036': 'Paper 2 owner: projectability criterion (the registry no-transfer obligation)',
    'CC-A003-003': 'Paper 2 owner: H3 rides the atlas institutional-implementation family',
    'CC-A003-004': 'Paper 3 owner: standing-stock-culling mechanism type',
    'CC-A003-006': 'Paper 1 owner: weak-coupling mechanism type',
    'CC-A012-008': 'Paper 3 owner: support-saturated logistic stock limit',
    'CC-A012-009': 'Paper 1 owner: effort-scale invariance (identification pair)',
    'CC-A018-002': 'Paper 3 owner: closed donor-limited ledger and conservation theorem (seam)',
    'CC-A018-003': 'Paper 3 owner: nonnegative-orthant theorem (seam)',
    'CC-A018-004': 'Paper 3 owner: deficit-identity row mirrored by the seam restatement',
    'CC-A018-005': 'Paper 3 owner: exact triangular projection (seam hand-off)',
    'CC-A018-006': 'Paper 2 owner: demoted macro-reduction (Tikhonov) conjecture',
    'CC-A018-012': 'Paper 5 owner: dimensionless identifiability groups',
    'CC-A019-004': 'Paper 3 owner: no-interior-rest theorem (non-reduction boundary)',
}

ID_RE = re.compile(r'CC-A\d{3}-\d{3}')


def load_concordance() -> dict[str, dict[str, str]]:
    with open(CC_CSV, newline='', encoding='utf-8') as f:
        return {r['concordance_id']: r for r in csv.DictReader(f)}


def retained_sets(rows: dict[str, dict[str, str]]) -> tuple[set[str], set[str]]:
    main = {i for i, r in rows.items() if r['destination_paper'] == MAIN_DEST}
    appendix = {i for i, r in rows.items() if r['destination_paper'] == APPENDIX_DEST}
    return main, appendix


def main() -> int:
    failures: list[str] = []

    # Check 1: extract both retained sets.
    rows = load_concordance()
    main_set, appendix_set = retained_sets(rows)
    retained = main_set | appendix_set
    print(f'Check 1 (extract retained sets): main={len(main_set)} appendix={len(appendix_set)} '
          f'total={len(retained)}')
    if len(main_set) != 55 or len(appendix_set) != 13:
        failures.append(f'Check 1 FAIL: expected 55 main + 13 appendix rows, '
                        f'got {len(main_set)} + {len(appendix_set)}')
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
        if i in rows and rows[i]['destination_paper'] in (MAIN_DEST, APPENDIX_DEST)
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
            failures.append(f'Check 4 FAIL: declared cross-references routed to Paper 4: {bad_owner}')
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
