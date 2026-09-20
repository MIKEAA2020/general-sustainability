"""Render the SafeTransition dashboard for the resource-transition
benchmark (Schaefer realization of the witness datum).

Usage:  python examples/northern_cod_dashboard.py [output.html]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from safetransition.benchmark import run_benchmark
from safetransition.certificates import certify_polyhedron, common_action_obstruction
from safetransition.dashboard import write
from safetransition.indicators import compute

out = sys.argv[1] if len(sys.argv) > 1 else "dashboard.html"

bench = run_benchmark(verbose=True)
readings = compute()
certs = [
    ("Stacked quota constraints u <= 2/5, -u <= -3/5 (infeasible menu window)",
     certify_polyhedron([[1], [-1]], [(2, 5), (-3, 5)]).certificate.describe(), True),
]
obs = common_action_obstruction({"FAST": {"pulse"}, "SLOW": {"hold"}})
certs.append(("Common-action obstruction on disjoint plan sets {pulse} vs {hold}",
              "fires; minimal conflicting subfamily " + str(obs["minimal_conflict"]),
              obs["fires"]))
path = write(readings, out, benchmark=bench, certificates=certs)
print(f"\nwrote {path}")
