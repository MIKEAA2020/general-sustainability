"""Scaling study for SafeTransition's exact pipeline (external-audit item
"parameterized benchmark family with known answers").

Families, each with the answer known by construction and asserted:

A. FM chain    - stacked chain with planted infeasibility; chain length k
                 varies; known answer: infeasible with a verified Farkas
                 certificate; margin positive with denominator dividing the
                 planted gap.
B. Bit growth  - dyadic chain: exact margin c * 2^-t certified for
                 denominator exponent t up to 320 (binary floating point
                 loses the margin early); known answer: the certificate
                 margin's denominator is exactly 2^t.
C. Typed rec.  - layered state graphs, all states safe and
                 destination-maintainable; known answer: every state stays
                 viable at every horizon.
D. Action menu - witness-datum menu cloned to j identical-behaviour
                 actions; known answer: all j admissible in all five modes.
E. Beliefs     - m independent labels with removal dynamics; known answer:
                 exactly 2^m reachable beliefs; the default enumeration
                 bound (4,096) is hit exactly at m = 12 and exceeded at
                 m = 13, where the call must raise with no partial results.

Recorded per instance: wall-clock runtime, peak traced memory, eliminator
rows generated / peak working rows, certificate JSON size, maximal
numerator/denominator bit length, reachable-belief counts, and the
independent checker's runtime. Results are written to
benchmarks/scaling_results.json. Timings are wall-clock on one core of the
running machine (record in the JSON's meta); growth rates, not absolute
times, are the result.

Run from the repository root:
    PYTHONPATH=src python3 benchmarks/scaling_study.py            # full
    PYTHONPATH=src python3 benchmarks/scaling_study.py --quick    # CI-size
"""
import json
import os
import subprocess
import sys
import tempfile
import time
import tracemalloc
from fractions import Fraction as Q

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "..", "src")))
from safetransition import belief_backward, certify_polyhedron, typed_backward  # noqa: E402

CHECKER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",
                                       "check_safe_transition_cert.py"))
QUICK = "--quick" in sys.argv
RESULTS = {"meta": {"python": sys.version.split()[0],
                    "mode": "quick" if QUICK else "full"}}


def out_path():
    """Result destination: --out PATH overrides; a quick sweep without
    --out writes a disposable repro file so the committed full-run
    results are never clobbered by a reproduction."""
    if "--out" in sys.argv:
        return sys.argv[sys.argv.index("--out") + 1]
    name = ("scaling_results_repro_quick.json" if QUICK
            else "scaling_results.json")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)


def max_bits(cert):
    def bl(v):
        f = Q(v)
        return max(abs(f.numerator).bit_length(), abs(f.denominator).bit_length())
    return max([bl(v) for row in cert["A"] for v in row]
               + [bl(v) for v in cert["b"]]
               + [bl(v) for v in cert["lam"]])


def run_checker(cert):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(cert, fh)
        path = fh.name
    t0 = time.perf_counter()
    res = subprocess.run([sys.executable, CHECKER, path],
                         capture_output=True, text=True)
    dt = time.perf_counter() - t0
    os.unlink(path)
    assert res.returncode == 0, res.stdout + res.stderr
    return dt


def chain_system(k):
    """k variables, k+1 rows: -u_0 <= -3/5 (u_0 >= 3/5); u_i - u_{i+1} <= gap;
    u_{k-1} <= 2/5. The chain propagates the lower bound upward, so
    feasibility requires 3/5 - (k-1)*gap <= 2/5: infeasible by construction
    for gap = 1/4096 and every k >= 2."""
    A = [[Q(-1)] + [Q(0)] * (k - 1)]
    for i in range(k - 1):
        row = [Q(0)] * k
        row[i], row[i + 1] = Q(1), Q(-1)
        A.append(row)
    A.append([Q(0)] * (k - 1) + [Q(1)])
    return A


def family_fm_chain():
    out = []
    gap = Q(1, 4096)
    for k in ([2, 8, 32] if QUICK else [2, 8, 32, 128, 256]):
        A = chain_system(k)
        b = [Q(-3, 5)] + [gap] * (k - 1) + [Q(2, 5)]
        t0 = time.perf_counter()
        tracemalloc.start()
        res = certify_polyhedron(A, b)
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        dt = time.perf_counter() - t0
        assert res.infeasible and res.certificate.verify(), "known answer violated"
        cert = res.certificate.to_dict()
        check_t = run_checker(cert)
        # closed form: raw gap 1/5 - (k-1)*gap split across the k+1 unit rows
        expected = (Q(1, 5) - (k - 1) * gap) / (k + 1)
        assert res.certificate.margin == expected, \
            (res.certificate.margin, expected)
        out.append({"k_vars": k, "rows_in": k + 1,
                    "eliminations": res.eliminations,
                    "rows_generated": res.rows_generated,
                    "peak_rows": res.peak_rows,
                    "cert_bytes": len(json.dumps(cert)),
                    "cert_bits": max_bits(cert),
                    "margin": str(res.certificate.margin),
                    "time_s": round(dt, 4),
                    "checker_s": round(check_t, 4),
                    "peak_mem_bytes": peak})
    RESULTS["fm_chain"] = out


def family_bit_growth():
    """u_0 <= 1 - 2^-t; u_{i+1} - u_i <= 0; u_L >= 1: infeasible with raw
    gap exactly 2^-t, certified margin 2^-t / (L + 2) after normalization.
    Binary floating point cannot represent the bound 1 - 2^-t once t exceeds
    the mantissa width, and rounds the gap away entirely."""
    out = []
    L = 3 if QUICK else 5
    k = L + 1
    A = [[Q(1)] + [Q(0)] * (k - 1)]
    for i in range(k - 1):
        row = [Q(0)] * k
        row[i + 1], row[i] = Q(1), Q(-1)      # u_{i+1} - u_i <= 0
        A.append(row)
    A.append([Q(0)] * (k - 1) + [Q(-1)])
    for t in ([10, 20, 40] if QUICK else [10, 20, 40, 80, 160, 320]):
        eps = Q(1, 2 ** t)
        b = [Q(1) - eps] + [Q(0)] * (k - 1) + [Q(-1)]
        t0 = time.perf_counter()
        res = certify_polyhedron(A, b)
        dt = time.perf_counter() - t0
        assert res.infeasible and res.certificate.verify()
        expected = eps / (k + 1)
        assert res.certificate.margin == expected, \
            (res.certificate.margin, expected)
        cert = res.certificate.to_dict()
        out.append({"bits_t": t,
                    "margin": str(res.certificate.margin),
                    "rows_in": k + 1,
                    "rows_generated": res.rows_generated,
                    "cert_bits": max_bits(cert),
                    "cert_bytes": len(json.dumps(cert)),
                    "time_s": round(dt, 5)})
    RESULTS["bit_growth"] = out


def family_typed_recursion():
    out = []
    grid = ([(10, 10), (10, 100)] if QUICK else
            [(5, 10), (10, 10), (10, 30), (10, 100), (10, 300), (10, 1000),
             (20, 1000)])
    for horizon, width in grid:
        states = [(l, i) for l in range(horizon + 1) for i in range(width)]

        def actions_fn(z):
            return ["stay", "left"]

        def visited_fn(z, a):
            return [z]

        def safe_fn(z):
            return True

        t0 = time.perf_counter()
        tracemalloc.start()
        viable = typed_backward(states, actions_fn, visited_fn, safe_fn, horizon)
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        dt = time.perf_counter() - t0
        assert len(viable) == len(states), "known answer violated"
        out.append({"states": len(states), "horizon": horizon,
                    "time_s": round(dt, 4), "peak_mem_bytes": peak})
    RESULTS["typed_recursion"] = out


def family_action_menu():
    from safetransition import WitnessDatum, witness_state
    from safetransition.datum import Action, Disturbance
    from safetransition.operators import E, MODES
    zero = (Q(0), Q(0), Q(0))

    def make(menu_size):
        class MenuDatum(WitnessDatum):
            n_actions = menu_size

            def actions(self, z):
                return {f"A{i}": Action(f"A{i}", {"x": zero, "s1": zero,
                                                  "s2": zero}, Disturbance())
                        for i in range(self.n_actions)}

            def successor(self, z, action_name):
                return (1, z[1], z[2], z[3])
        return MenuDatum()

    out = []
    for j in ([2, 8, 32] if QUICK else [2, 8, 32, 128, 512]):
        datum = make(j)
        z = witness_state(1, 2, 2)
        t0 = time.perf_counter()
        counts = {m: len(E(datum, z, mode=m, w=(Q(1), Q(1)))) for m in MODES}
        dt = time.perf_counter() - t0
        assert all(c == j for c in counts.values()), counts
        out.append({"actions": j, "all_modes_s": round(dt, 4)})
    RESULTS["action_menu"] = out


def subset_belief_system(m):
    """m removable labels: reachable beliefs are exactly {y_0} u S for
    S subset of {y_1..y_m}: 2^m beliefs."""
    labels = [f"y{i}" for i in range(m + 1)]
    states = [f"x{i}" for i in range(1, m + 1)] + ["t"]
    gamma = {**{f"x{i}": f"y{i}" for i in range(1, m + 1)}, "t": "y0"}
    F = {}
    for i in range(1, m + 1):
        acts = {"hold": [f"x{i}"]}
        for j in range(1, m + 1):
            acts[f"a{j}"] = ["t"] if j == i else [f"x{i}"]
        F[f"x{i}"] = acts
    F["t"] = {f"a{j}": ["t"] for j in range(1, m + 1)}
    F["t"]["hold"] = ["t"]
    return F, gamma, set(states), [f"x{i}" for i in range(1, m + 1)]


def family_beliefs():
    out = []
    for m in ([2, 4, 6] if QUICK else [2, 4, 6, 8, 10]):
        F, gamma, safe, prior = subset_belief_system(m)
        t0 = time.perf_counter()
        tracemalloc.start()
        W, start = belief_backward(F, gamma, safe, prior, 2, max_beliefs=100000)
        peak = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        dt = time.perf_counter() - t0
        reachable = set().union(*W.values()) | {start}
        assert len(reachable) == 2 ** m, (len(reachable), 2 ** m)
        out.append({"labels": m, "reachable_beliefs": len(reachable),
                    "expected": 2 ** m, "time_s": round(dt, 4),
                    "peak_mem_bytes": peak})
    RESULTS["beliefs"] = out
    # enumeration bound: default 4,096 hit exactly at m = 12, exceeded at 13
    bound = {}
    for m, expect_raise in ((12, False), (13, True)):
        F, gamma, safe, prior = subset_belief_system(m)
        raised = False
        try:
            belief_backward(F, gamma, safe, prior, 2)
        except RuntimeError:
            raised = True
        assert raised == expect_raise, (m, raised)
        bound[str(m)] = {"raised": raised}
    RESULTS["beliefs_bound"] = {"default_max_beliefs": 4096, **bound,
                                "note": "m = 12 reaches the bound exactly; "
                                        "m = 13 raises with no partial results"}


if __name__ == "__main__":
    t0 = time.perf_counter()
    family_fm_chain()
    family_bit_growth()
    family_typed_recursion()
    family_action_menu()
    family_beliefs()
    RESULTS["total_s"] = round(time.perf_counter() - t0, 2)
    path = out_path()
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(RESULTS, fh, indent=1)
    print(json.dumps(RESULTS, indent=1))
    print(f"\nwrote {path}")
