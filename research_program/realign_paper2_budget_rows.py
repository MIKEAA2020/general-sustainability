#!/usr/bin/env python3
"""Realign paper2_retained_row_budget.csv to the closure-corrected concordance IDs.

Background (2026-08-28): the retained-row budget was produced by the source-
selection pass BEFORE the 2026-08-26 machine repair that restored the second
untitled A002 Remark as concordance row CC-A002-053. In the pre-repair
numbering, the A002 block from row 16 onward shifted every later environment
down by one (the collided remark occupied position 16). The A002 scientific
closure pass (2026-08-27, close_concordance_rows_A002.py) verified all 53
rows in the CORRECTED numbering. This script realigns the budget so that the
budget, the concordance, and the Paper 2 manuscript
(papers/paper2_theorem_atlas/manuscript.md) reference the same rows.

Mapping (A002 block only; A001 rows unchanged):
  TM-A002-001..015  ->  CC-A002-001..015   (unchanged)
  TM-A002-016       ->  CC-A002-053        (the collided/restored remark)
  TM-A002-017..053  ->  CC-A002-016..052   (shift by one, INCLUDING row 053,
                                            the fifth research programme)

The tier/family/selection columns are NOT touched: the selection decisions
were made on content (family-level), and the closure pass confirmed the
family assignments against the corrected row identities. The original
map_id column is preserved verbatim (the historical selection-pass ID); the
authoritative current row is recorded in the new concordance_id column, with
a dated realignment flag.

Idempotent: rows already carrying a concordance_id column are skipped.
"""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUDGET = REPO / 'research_program' / 'paper2_retained_row_budget.csv'
CC = REPO / 'research_program' / 'canonical_concordance_A001_A025.csv'
DATE = '2026-08-28'


def budget_to_cc(map_id: str) -> str:
    src, num = map_id.rsplit('-', 1)
    n = int(num)
    if src == 'TM-A002' and n == 16:
        return 'CC-A002-053'
    if src == 'TM-A002' and 17 <= n <= 53:
        return f'CC-A002-{n - 1:03d}'
    return map_id.replace('TM-', 'CC-', 1)


def main() -> None:
    rows = list(csv.DictReader(open(BUDGET)))
    fields = list(rows[0].keys())
    if 'concordance_id' in fields:
        print('already realigned; nothing to do')
        return
    cc = {r['concordance_id']: r for r in csv.DictReader(open(CC))}
    fields += ['concordance_id', 'realigned_2026_08_28']

    shifted = 0
    seen: set[str] = set()
    for r in rows:
        cid = budget_to_cc(r['map_id'])
        if cid not in cc:
            raise SystemExit(f'unknown concordance row {cid} for {r["map_id"]}')
        if cid in seen:
            raise SystemExit(f'collision: {cid} mapped twice (last from {r["map_id"]})')
        seen.add(cid)
        r['concordance_id'] = cid
        naive = r['map_id'].replace('TM-', 'CC-', 1)
        realigned = cid != naive
        r['realigned_2026_08_28'] = 'yes' if realigned else 'no'
        shifted += int(realigned)

    assert len(seen) == len(rows) == 152, (len(seen), len(rows))
    with open(BUDGET, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f'realigned {shifted} A002 rows (17..53 shift + remark 053); '
          f'{len(rows)} rows total; concordance_id + realigned columns added')


if __name__ == '__main__':
    main()
