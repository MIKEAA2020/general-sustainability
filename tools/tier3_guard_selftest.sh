#!/bin/bash
# Regression suite for tier3_guard.py. Run before trusting the guard on a real pass.
set -u
G="python3 /home/user/tools/tier3_guard.py"
BASE=/home/user/E1_v22.tex
SI=/tmp/reloc_si.md
pass=0; fail=0
chk(){ # name expected_exit cmd...
  local n="$1" e="$2"; shift 2
  "$@" >/dev/null 2>&1; local a=$?
  if [ "$a" -eq "$e" ]; then echo "  PASS  $n"; pass=$((pass+1));
  else echo "  FAIL  $n (exit $a, expected $e)"; fail=$((fail+1)); fi
}
echo "tier3_guard self-test"
chk "T1 identity (base vs base)"        0 $G "$BASE" "$BASE" --si "$SI" --quiet
chk "T2 results paragraph deleted"      1 $G "$BASE" /tmp/sabotage1.tex --si "$SI" --quiet
chk "T3 legitimate SI relocation"       0 $G "$BASE" /tmp/reloc.tex --si "$SI" --quiet
chk "T4 claim silently unscoped"        1 $G "$BASE" /tmp/sabotage2.tex --si "$SI" --quiet
chk "T5 no SI supplied, SI-1 cited"     1 $G "$BASE" "$BASE" --quiet
echo "  ---- $pass passed, $fail failed"
[ "$fail" -eq 0 ]
