#!/usr/bin/env bash
# Master reproduction script for this deposit. Run from the deposit root:
#     bash run_all.sh
# Steps: environment -> integrity -> exact verification -> SafeTransition suite ->
# figure/graphical-abstract regeneration with byte-level comparison.
set -u
fail=0
export SOURCE_DATE_EPOCH=0   # deterministic timestamps in generated PDFs

echo "=== [1/6] Environment ==="
python3 - <<'PY' || fail=1
import sys
assert sys.version_info >= (3, 9), "Python 3.9+ required"
import numpy, matplotlib, PIL
print("  python", sys.version.split()[0], "| numpy", numpy.__version__,
      "| matplotlib", matplotlib.__version__, "| pillow", PIL.__version__)
PY

echo "=== [2/6] Integrity of deposited files (SHA-256) ==="
sha256sum -c SHA256SUMS --quiet || fail=1
[ $fail -eq 0 ] && echo "  all checksums match"

echo "=== [3/6] Exact-arithmetic verification (25 checks, deterministic) ==="
python3 verification/typed_false_positive_instantiation.py > verification_run.log 2>&1
tail -2 verification_run.log
grep -q "25/25 checks passed" verification_run.log || fail=1

echo "=== [4/6] SafeTransition 1.2.0 suite (tests, benchmark, certificate protocol) ==="
(cd safetransition && sh run_all.sh) || fail=1

echo "=== [5/6] Figure and graphical-abstract regeneration ==="
rm -rf rebuilt && mkdir rebuilt
(cd rebuilt \
  && python3 ../figure_code/make_fig1_v40.py > /dev/null \
  && python3 ../figure_code/make_fig2_v35.py > /dev/null \
  && python3 ../figure_code/make_figures_v31.py > /dev/null \
  && python3 ../figure_code/make_graphical_abstract.py > /dev/null \
  && python3 ../figure_code/make_graphical_abstract_tif.py > /dev/null \
  && python3 ../figure_code/make_benchmark_v44.py > /dev/null)
check() {
  if cmp -s "$1" "$2"; then echo "  identical: $(basename "$1")";
  else echo "  DIFFERS: $(basename "$1") (likely a library-version difference; compare visually)"; fail=1; fi
}
for f in figures/*.png; do check "$f" "rebuilt/$(basename "$f")"; done
check graphical_abstract/graphical_abstract.png rebuilt/graphical_abstract.png
check graphical_abstract/graphical_abstract.tif rebuilt/graphical_abstract.tif
check graphical_abstract/graphical_abstract.pdf rebuilt/graphical_abstract.pdf
rm -rf rebuilt verification_run.log

echo "=== [6/6] Result ==="
if [ $fail -eq 0 ]; then echo "ALL REPRODUCTION CHECKS PASS"; else echo "SOME CHECKS FAILED — see above"; exit 1; fi
