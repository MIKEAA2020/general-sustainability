#!/usr/bin/env python3
"""Repair only the inherited v49 sensitivity wording in the two reviewed heads.

Historical paper07 v49 remains unchanged as a provenance witness. Apply this to
v50 or its v46 paper08 copy; the exact-match preconditions refuse unrelated text.
The numerical rows are unchanged except d_ref: its finite -2% endpoint is 65.7%,
whereas the +2% endpoint has no crossing (and is not assigned a finite shift).
"""
import sys
from pathlib import Path

ROOT = Path('/home/user/papers')
TARGETS = {
    '07': ROOT / 'paper07_sampled_governance_v50.tex',
    '08': ROOT / 'paper08_governance_delay_v46.tex',
}

REPLACEMENTS = [
    (
        r'under a \(1\%\) change in \(K\), \(q\) or \(E_{\max}\).',
        r'under a \(2\%\) change in \(K\), \(q\) or \(E_{\max}\).',
    ),
    (
        r'& worst 1\%\\',
        r'& worst 2\%\\',
    ),
    (
        'perturbation. Baseline crossing \\(6.501\\)~yr. ``none\'\' indicates that no unit-circle\n'
        'crossing occurs anywhere on \\([0.2,200]\\)~yr: the loop is stable at every tested interval.}',
        'perturbation. Baseline crossing \\(6.501\\)~yr. The last column is the largest\n'
        'finite crossing shift among the \\(\\pm2\\%\\) endpoints, as a percentage of baseline;\n'
        'a non-crossing endpoint is excluded from that percentage. ``none\'\' indicates that\n'
        'no unit-circle crossing occurs on \\([0.2,200]\\)~yr at the tested grid resolution.}',
    ),
    (
        r'& 10.78 & 8.89 & 2.35 & none  & ---\\',
        r'& 10.78 & 8.89 & 2.35 & none  & 65.7\%\\',
    ),
    (
        'and that verdict has a margin three orders of magnitude larger than the mobilising\n'
        "channel's. (iii) The multiplicity-controlled screen",
        'and its smallest stability margin on that grid is approximately \\(0.0033\\)\n'
        '(\\(1-0.9967\\)). At annual review the mobilising instability excess is approximately\n'
        '\\(0.00035\\) (\\(1.00035-1\\)); these two margins refer to different interval sets.\n'
        '(iii) The multiplicity-controlled screen',
    ),
]


def main(which):
    p = TARGETS[which]
    text = p.read_text()
    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f'{p.name}: expected exactly one source match, found {n}: {old[:65]!r}')
        text = text.replace(old, new, 1)
    p.write_text(text)
    print(f'repaired inherited v49 sensitivity passage in {p}')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in TARGETS:
        raise SystemExit('usage: fix_p7_sensitivity_addition.py 07|08')
    main(sys.argv[1])
