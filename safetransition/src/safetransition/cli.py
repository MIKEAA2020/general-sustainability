"""Command-line interface.

Commands
--------
``safetransition verify``   run the twenty-four exact benchmark checks.
``safetransition report``   write the static dashboard for the witness
                            datum (default ``safetransition_dashboard.html``).
``safetransition demo``     both of the above, plus the certificate
                            demonstrations.
"""
import argparse
import sys
from fractions import Fraction as Q

from . import __version__
from .benchmark import run_benchmark
from .certificates import certify_polyhedron, common_action_obstruction
from .indicators import compute
from .rational import fmt


def _certificate_rows():
    rows = []
    res = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(2, 5), Q(-3, 5)])
    rows.append(("Stacked infeasible system u <= 2/5, -u <= -3/5",
                 res.certificate.describe() if res.infeasible else "feasible",
                 res.infeasible and res.certificate.verify()))
    res2 = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(-2, 5), Q(3, 5)])
    rows.append(("Feasible interval system 2/5 <= u <= 3/5",
                 "feasible; no certificate exists (Farkas alternative)",
                 not res2.infeasible))
    obs = common_action_obstruction({"x1": {"a"}, "x2": {"b"}})
    rows.append(("Common-action obstruction, states {x1, x2}, disjoint safe actions",
                 "fires; minimal conflicting subfamily "
                 f"{obs['minimal_conflict']}" if obs["fires"] else "silent",
                 obs["fires"]))
    return rows


def cmd_report(out):
    readings = compute()
    bench = run_benchmark(verbose=False)
    from .dashboard import write
    path = write(readings, out, benchmark=bench, certificates=_certificate_rows())
    print(f"wrote dashboard: {path}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="safetransition",
        description="Exact transition-safety assessment: typed operators, "
                    "recursions, obstruction certificates, dashboard readings.")
    p.add_argument("--version", action="version", version=f"SafeTransition {__version__}")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("verify", help="run the exact benchmark checks")
    rep = sub.add_parser("report", help="write the static dashboard")
    rep.add_argument("--out", default="safetransition_dashboard.html")
    dem = sub.add_parser("demo", help="verify, demonstrate certificates, and write the dashboard")
    dem.add_argument("--out", default="safetransition_dashboard.html")
    args = p.parse_args(argv)
    if args.cmd in (None, "verify"):
        bench = run_benchmark(verbose=True)
        return 0 if bench.all_pass else 1
    if args.cmd == "report":
        return cmd_report(args.out)
    if args.cmd == "demo":
        bench = run_benchmark(verbose=True)
        print("\nCertificate demonstrations (exact):")
        for name, verdict, holds in _certificate_rows():
            print(f"  [{'OK' if holds else 'FAIL'}] {name}: {verdict}")
        r = compute()
        print(f"\nDashboard readings at the witness: rho_1 = {fmt(r.rho1)}, "
              f"rho_2 = {fmt(r.rho2)}, kappa* = {fmt(r.kappa_star)}, "
              f"blindness alarm = {r.blind_alarm}")
        return cmd_report(args.out)
    p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
