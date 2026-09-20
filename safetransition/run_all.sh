#!/usr/bin/env sh
# Fresh-environment reproduction for SafeTransition.
# Run from the package root:  sh run_all.sh
set -e
cd "$(dirname "$0")"
export PYTHONPATH=src
echo "== 1/4 unit and integration tests =="
python3 -m unittest discover -s tests
echo "== 2/4 exact benchmark checks =="
python3 -m safetransition.cli verify
echo "== 3/4 worked examples =="
python3 examples/partial_observation.py
python3 examples/northern_cod_dashboard.py dashboard_repro.html
echo "== 4/4 figure regeneration (optional; see requirements-figures.txt) =="
if python3 -c "import matplotlib, PIL" 2>/dev/null; then
  python3 figure_code/make_safetransition_figs.py
  python3 figure_code/make_graphical_abstract_tif.py
else
  echo "skipped: matplotlib/Pillow not installed"
fi
echo "ALL REPRODUCTION STEPS PASS"
