#!/usr/bin/env python3
"""Report-only corpus/false-negative trials before changing the CI gate."""
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parent
checker = root / 'check_whitelisted_footprints.py'
allow = root / 'allowed_native_axioms_v4341.txt'
text = (root / 'ci_runs/36946730855/all_footprints.log').read_text()

def check(sample, gate, expected_code, expected_phrase):
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / 'all.log'; p.write_text(sample)
        cmd = [sys.executable, str(checker), str(p), str(allow)] + (['--gate'] if gate else [])
        r = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert r.returncode == expected_code and expected_phrase in r.stdout, (r.returncode, r.stdout[-500:])
        print('POLICY_TEST_PASS', 'gate' if gate else 'report-only', expected_phrase)

check(text, False, 0, 'OBSERVED_ALLOWED=9 UNKNOWN=0 STALE=0')
check(text, True, 0, 'EXACT AXIOM ALLOWLIST PASS')
changed = text.replace('native_decide.ax_4\n', 'native_decide.ax_44\n', 1)
assert changed != text
check(changed, False, 0, 'UNKNOWN=1')
check(changed, True, 2, 'AXIOM ALLOWLIST BLOCKED')
changed = text.replace('native_decide.ax_4\n', 'sorryAx\n', 1)
assert changed != text
check(changed, True, 2, 'AXIOM ALLOWLIST BLOCKED')
changed = text.replace('native_decide.ax_4\n', 'Formalizations.P3.NewExplicitAxiom\n', 1)
assert changed != text
check(changed, True, 2, 'AXIOM ALLOWLIST BLOCKED')
changed = text.replace('FOOTPRINT_TOTAL 1972 UNEXPECTED_REFERENCES 90', 'FOOTPRINT_TOTAL 1972 UNEXPECTED_REFERENCES 89')
assert changed != text
r = subprocess.run([sys.executable, str(checker), '/dev/stdin', str(allow), '--gate'], input=changed, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
assert r.returncode != 0 and 'Incomplete unexpected-axiom inventory' in r.stdout
print('POLICY_TEST_PASS malformed log rejected')
