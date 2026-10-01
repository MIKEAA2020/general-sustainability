#!/usr/bin/env python3
"""Source-bound prose check for the paper07 v49 sensitivity addition and its copy.

Run at ADDITION time before copying/merging this section, not as a speculative
fatal rule for unrelated papers. Re-executes p7/sensitivity.py (~10 seconds),
then checks the live manuscript tables, qualifying prose and computation note.
Historical v49 is deliberately not checked: it is the immutable origin witness.
"""
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/home/user')
source = ROOT / 'p7/sensitivity.py'
run = subprocess.run([sys.executable, str(source)], check=True,
                     capture_output=True, text=True, timeout=180).stdout
assert 'largest finite crossing shift under +/-2%' in run
assert 'worst 1% swing' not in run
matches = re.findall(r'^\s*(\w+)\s+worst finite 2% swing:\s+[\d.]+ yr\s+' +
                     r'\(\s*([\d.]+)% of baseline\)', run, flags=re.M)
computed = {name: float(pct) for name, pct in matches}
symbols = {
    'K': r'\(K\)', 'q': r'\(q\)', 'Emax': r'\(E_{\max}\)',
    'eta': r'\(\eta\)', 'r': r'\(r\)', 'dref': r'\(d_{\rm ref}\)',
    'tm': r'\(t_m\)', 'd0': r'\(d_0\)', 'Zref': r'\(Z_{\rm ref}\)',
}
assert computed.keys() == symbols.keys(), computed
assert min(computed[a] for a in ('K', 'q', 'Emax')) > 50
baseline = float(re.search(r'BASELINE CROSSING = ([\d.]+) yr', run).group(1))
assert abs(baseline - 6.5013) < .0001
annual = float(re.search(r'mobilising exact\s+rho\(1\) = ([\d.]+)', run).group(1))
assert abs((annual - 1) - .00035) < 1e-8
# Max protective rho from the independently rerun crossing campaign.
campaign = (ROOT / 'content_audit/p7_campaign_recheck.log').read_text()
assert 'protective exact max rho on [0.2,200] = 0.9967' in campaign
assert abs((1 - .9967) - .0033) < 1e-8

for path in (ROOT / 'papers/paper07_sampled_governance_v50.tex',
             ROOT / 'papers/paper08_governance_delay_v46.tex'):
    text = path.read_text()
    table_start = text.index('\\caption{Sensitivity of the exact-update mobilising crossing')
    table = text[table_start:text.index('\\end{table}', table_start)]
    assert 'worst 2\\%' in table and 'worst 1\\%' not in table, path
    assert 'largest\nfinite crossing shift among the \\(\\pm2\\%\\) endpoints' in table, path
    assert 'a non-crossing endpoint is excluded from that percentage' in table, path
    for name, symbol in symbols.items():
        rows = [line for line in table.splitlines() if line.startswith(symbol + ' ')]
        assert len(rows) == 1, (path, name, rows)
        m = re.search(r'&\s*(\d+\.\d+)\\%\\\\\s*$', rows[0])
        assert m, (path, name, rows[0])
        assert abs(float(m.group(1)) - computed[name]) < .051, (path, name, m.group(1), computed[name])
    assert r'under a \(2\%\) change in \(K\), \(q\) or \(E_{\max}\)' in text, path
    assert r'under a \(1\%\) change in \(K\), \(q\) or \(E_{\max}\)' not in text, path
    assert 'margin three orders of magnitude larger' not in text, path
    assert r'minimum stability margin' not in table  # the two sections are independent
    assert r'its smallest stability margin on that grid is approximately \(0.0033\)' in text, path
    assert r'\(0.00035\) (\(1.00035-1\))' in text, path
    print('checked', path.name, 'table/prose against fresh one-axis source run and campaign margins')

note = (ROOT / 'papers/PAPER07_SENSITIVITY.md').read_text()
assert 'worst finite 2% swing' in note
assert 'dref | 10.78 | 8.89 | 2.35 | none | 65.7%' in note
assert 'minimum tested-grid stability margin about 0.0033' in note
print('checked computation note; historical v49 retained as origin witness')
