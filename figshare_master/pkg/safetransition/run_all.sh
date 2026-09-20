#!/usr/bin/env sh
# Fresh-environment reproduction for SafeTransition.
# Run from the package root:  sh run_all.sh
set -e
cd "$(dirname "$0")"
export PYTHONPATH=src
echo "== 1/7 unit and integration tests =="
python3 -m unittest discover -s tests
echo "== 2/7 exact benchmark checks =="
python3 -m safetransition.cli verify
echo "== 3/7 certificate protocol: emit + independent check + tamper reject =="
rm -rf certificates
python3 -m safetransition.cli certify --outdir certificates
python3 check_safe_transition_cert.py certificates/*.json
echo "== 4/7 worked examples =="
python3 examples/partial_observation.py
python3 examples/northern_cod_dashboard.py dashboard_repro.html
echo "== 5/7 scaling study (quick sweep; committed full results) =="
python3 benchmarks/scaling_study.py --quick --out /tmp/scaling_repro.json | tail -1
rm -f /tmp/scaling_repro.json
echo "== 6/7 adversarial exactness instance (n = 49 verdict flip) ==="
python3 examples/certificates_demo.py | tail -1
echo "== 7/7 figure regeneration (optional; see requirements-figures.txt) =="
if python3 -c "import matplotlib, PIL" 2>/dev/null; then
  python3 figure_code/make_safetransition_figs.py
  python3 figure_code/make_certificate_chain.py
  python3 figure_code/make_graphical_abstract_tif.py
else
  echo "skipped: matplotlib/Pillow not installed"
fi
echo "ALL REPRODUCTION STEPS PASS"
