"""Scaling-study and audit-provenance tests: closed-form FM growth on small
instances, closed-form dyadic margins, linear-growth families, dashboard
provenance determinism, exact schedule-to-figure equality, and the formal
obstruction-to-Farkas row mapping."""
import json
import os
import re
import subprocess
import sys
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition import (WitnessDatum, belief_backward, certify_polyhedron,
                            witness_state)
from safetransition.benchmark import schedule_data
from safetransition.certificates import common_action_obstruction
from safetransition.dashboard import default_provenance, render

PKG_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
STUDY = os.path.join(PKG_ROOT, "benchmarks", "scaling_study.py")
FIGS = os.path.join(PKG_ROOT, "figs_p3")


class TestScalingClosedForms(unittest.TestCase):
    def test_fm_chain_margin_closed_form_small_k(self):
        gap = Q(1, 4096)
        for k in (2, 5, 8):
            A = [[Q(-1)] + [Q(0)] * (k - 1)]
            for i in range(k - 1):
                row = [Q(0)] * k
                row[i], row[i + 1] = Q(1), Q(-1)
                A.append(row)
            A.append([Q(0)] * (k - 1) + [Q(1)])
            b = [Q(-3, 5)] + [gap] * (k - 1) + [Q(2, 5)]
            res = certify_polyhedron(A, b)
            self.assertTrue(res.infeasible)
            self.assertTrue(res.certificate.verify())
            expected = (Q(1, 5) - (k - 1) * gap) / (k + 1)
            self.assertEqual(res.certificate.margin, expected)
            # row growth bounded: elimination terminates at the planted
            # contradiction, so between one round and the full pair count
            self.assertGreaterEqual(res.rows_generated, res.eliminations)
            self.assertLessEqual(res.rows_generated, k * (k - 1) // 2 + 1)

    def test_dyadic_margin_closed_form(self):
        t, L = 12, 3
        k = L + 1
        A = [[Q(1)] + [Q(0)] * (k - 1)]
        for i in range(k - 1):
            row = [Q(0)] * k
            row[i + 1], row[i] = Q(1), Q(-1)
            A.append(row)
        A.append([Q(0)] * (k - 1) + [Q(-1)])
        eps = Q(1, 2 ** t)
        res = certify_polyhedron(A, [Q(1) - eps] + [Q(0)] * (k - 1) + [Q(-1)])
        self.assertTrue(res.infeasible)
        self.assertEqual(res.certificate.margin, eps / (k + 1))

    def test_linear_growth_families(self):
        # menu: time grows linearly in menu size; beliefs: 2^m reachable
        from safetransition.datum import Action, Disturbance
        from safetransition.operators import E
        zero = (Q(0), Q(0), Q(0))

        class MenuDatum(WitnessDatum):
            def actions(self, z):
                return {f"A{i}": Action(f"A{i}", {"x": zero, "s1": zero,
                                                  "s2": zero}, Disturbance())
                        for i in range(24)}

            def successor(self, z, action_name):
                return (1, z[1], z[2], z[3])

        datum = MenuDatum()
        z = witness_state(1, 2, 2)
        for m in ("typ", "w", "end"):
            self.assertEqual(len(E(datum, z, mode=m, w=(Q(1), Q(1)))), 24)
        labels = [f"y{i}" for i in range(5)]
        states = [f"x{i}" for i in range(1, 5)] + ["t"]
        gamma = {**{f"x{i}": f"y{i}" for i in range(1, 5)}, "t": "y0"}
        F = {}
        for i in range(1, 5):
            acts = {"hold": [f"x{i}"]}
            for j in range(1, 5):
                acts[f"a{j}"] = ["t"] if j == i else [f"x{i}"]
            F[f"x{i}"] = acts
        F["t"] = {**{f"a{j}": ["t"] for j in range(1, 5)}, "hold": ["t"]}
        W, start = belief_backward(F, gamma, set(states),
                                   ["x1", "x2", "x3", "x4"], 2, max_beliefs=10 ** 6)
        self.assertEqual(len(set().union(*W.values()) | {start}), 16)

    def test_quick_study_script_runs(self):
        res = subprocess.run([sys.executable, STUDY, "--quick"],
                             capture_output=True, text=True,
                             cwd=os.path.join(PKG_ROOT))
        self.assertEqual(res.returncode, 0, res.stdout[-800:] + res.stderr[-800:])
        data = json.load(open(os.path.join(PKG_ROOT, "benchmarks",
                                           "scaling_results.json")))
        self.assertGreaterEqual(len(data["fm_chain"]), 3)
        self.assertEqual(data["beliefs_bound"]["13"]["raised"], True)


class TestFigureProvenance(unittest.TestCase):
    def test_figure_values_equal_library_values(self):
        d = schedule_data()
        src = open(os.path.join(PKG_ROOT, "figure_code",
                                "make_benchmark_v45.py"), encoding="utf-8").read()
        self.assertIn("schedule_data", src)
        self.assertNotIn("fig_benchmark_v44", src)
        # the deposited v44 values equal the library's, at float tolerance
        pairs = [(d["H_fast"][0], 11.704), (d["H_fast"][1], 8.644),
                 (d["H_sy"], 8.704), (d["H_staged"][0], 8.204),
                 (d["fund"][0], 1.5)]
        for exact, approx in pairs:
            self.assertAlmostEqual(float(exact), approx, places=3)

    def test_dashboard_provenance_deterministic(self):
        cert = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()
        from safetransition.indicators import compute
        prov = default_provenance(certificates_json=[("farkas", cert)])
        h1 = render(compute(), provenance=prov)
        h2 = render(compute(), provenance=prov)
        self.assertEqual(h1, h2)
        digest = __import__("hashlib").sha256(
            json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.assertIn(digest, h1)
        self.assertIn("re-run", h1)
        self.assertIn("1.2.1", h1)


class TestObstructionFarkasMapping(unittest.TestCase):
    def test_row_mapping_on_paper_instance(self):
        # the paper's stacked window: row [1] u <= 2/5 is x1's menu cap;
        # row [-1] u <= -3/5 is x2's floor requirement. The obstruction is
        # the empty intersection of the states' safe menus; the Farkas
        # certificate weights the two states' rows equally.
        obs = common_action_obstruction({"x1": {"a"}, "x2": {"b"}})
        self.assertTrue(obs["fires"])
        res = certify_polyhedron([[1], [-1]], [Q(2, 5), Q(-3, 5)])
        self.assertTrue(res.infeasible)
        lam = res.certificate.lam
        self.assertEqual(lam, (Q(1, 2), Q(1, 2)))
        self.assertEqual(res.certificate.margin, Q(1, 10))
        # the certificate carries the full system, so each row is
        # traceable to its state restriction
        self.assertEqual(len(res.certificate.A), 2)


if __name__ == "__main__":
    unittest.main()
