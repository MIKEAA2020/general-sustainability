"""Certificate-protocol tests: independent checking, tamper rejection,
import hygiene, exactness discipline, and the adversarial exact-vs-float
verdict flip."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition import (FarkasCertificate, certify_polyhedron,
                            benchmark_certificate, tube_certificate,
                            weight_partition, licensing_thresholds,
                            explain_belief_failure, TubeStatus,
                            WitnessDatum, witness_state)
from safetransition.operators import admissible

CHECKER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "check_safe_transition_cert.py")
PKG_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def run_checker(*paths):
    return subprocess.run([sys.executable, CHECKER, *paths],
                          capture_output=True, text=True)


class TestCertificateProtocol(unittest.TestCase):
    def test_farkas_produce_check_roundtrip(self):
        cert = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate
        d = cert.to_dict()
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(d, fh); path = fh.name
        res = run_checker(path)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("margin = 1/10", res.stdout)
        self.assertTrue(FarkasCertificate.from_dict(d).verify())
        os.unlink(path)

    def test_tampered_certificates_rejected(self):
        base = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()
        for mutate in (lambda c: c["b"].__setitem__(0, "3/5"),      # bound tampered
                       lambda c: c["lam"].__setitem__(0, "3/5"),    # multipliers tampered
                       lambda c: c["A"][1].__setitem__(0, "1")):    # system tampered
            c = json.loads(json.dumps(base))
            mutate(c)
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
                json.dump(c, fh); path = fh.name
            res = run_checker(path)
            self.assertNotEqual(res.returncode, 0,
                                "tampered certificate accepted: " + res.stdout)
            os.unlink(path)

    def test_weight_partition_certificate_checked(self):
        for s, dip in ((Q(6, 5), Q(2)), (Q(3, 2), Q(2)), (Q(7, 4), Q(2)),
                       (Q(6, 5), Q(5, 2)), (Q(9, 5), Q(2))):
            d = weight_partition(state=(0, Q(3, 2), s, s), dip=dip)
            # closed-form family: rho1 = (dip - s)/s, rho2 = s/(dip - s)
            self.assertEqual(d["thresholds"]["rho1"], fmt := str((dip - s) / s))
            self.assertEqual(d["thresholds"]["rho2"], str(s / (dip - s)))
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
                json.dump(d, fh); path = fh.name
            res = run_checker(path)
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            os.unlink(path)

    def test_weight_partition_rescue_witness(self):
        d = weight_partition(state=(0, Q(3, 2), Q(6, 5), Q(6, 5)))
        self.assertTrue(d["staged_financed"])
        self.assertTrue(d["typed_safe_any_weight"])
        for rg in d["regions"]:
            self.assertIn("STAGED", rg["licensed"])

    def test_benchmark_and_tube_certificates_checked(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(benchmark_certificate(), fh); path = fh.name
        res = run_checker(path)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("11 values re-derived", res.stdout)
        os.unlink(path)
        self.assertEqual(tube_certificate()["realization"]["status"],
                         TubeStatus.CONSERVATIVE.value)
        self.assertEqual(tube_certificate()["declared_paths"]["status"],
                         TubeStatus.EXACT.value)


class TestExactnessDiscipline(unittest.TestCase):
    def test_float_inputs_rejected(self):
        from safetransition import frac
        with self.assertRaises(TypeError):
            frac(0.5)
        with self.assertRaises(TypeError):
            witness_state(0.5, Q(6, 5), Q(6, 5))

    def test_import_graph_hygiene(self):
        src = os.path.join(PKG_ROOT, "src", "safetransition")
        banned = ("matplotlib", "PIL", "numpy", "scipy")
        for fn in os.listdir(src):
            if fn.endswith(".py"):
                with open(os.path.join(src, fn), encoding="utf-8") as fh:
                    text = fh.read()
                for line in text.splitlines():
                    stripped = line.strip()
                    if stripped.startswith(("import ", "from ")):
                        for b in banned:
                            self.assertNotIn(b, stripped.split()[1].split(".")[0],
                                             f"{fn} imports {b}")

    def test_core_runs_without_figure_stack(self):
        code = (
            "import sys\n"
            "class Block:\n"
            "    def find_spec(self, name, path=None, target=None):\n"
            "        if name.split('.')[0] in ('matplotlib', 'PIL', 'numpy'):\n"
            "            raise ImportError(name + ' blocked for core test')\n"
            "sys.meta_path.insert(0, Block())\n"
            "sys.path.insert(0, <<SRC>>)\n"
            "import safetransition as st\n"
            "r = st.run_benchmark()\n"
            "assert r.all_pass\n"
            "assert st.weight_partition()['thresholds']['rho1'] == '2/3'\n"
            "print('core-ok')\n"
        ).replace("<<SRC>>", repr(os.path.join(PKG_ROOT, "src")))
        res = subprocess.run([sys.executable, "-c", code],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("core-ok", res.stdout)


class TestExactVersusFloat(unittest.TestCase):
    def test_adversarial_verdict_flip(self):
        # 49 * (1/49) - 1: exactly zero (floor exactly met -> licensed);
        # binary floating point: -1.11e-16 (falsely unlicensed)
        self.assertEqual(Q(49) * Q(1, 49) - Q(1), Q(0))
        self.assertLess(49 * (1 / 49) - 1, 0)

    def test_adversarial_flip_on_library_admissibility(self):
        # a minimal custom datum (the documented extension path): s1 flat at
        # 1/49, s2 dipping to -1, successor maintained by the hold policy.
        from safetransition.datum import Action, Disturbance
        zero = (Q(0), Q(0), Q(0))

        class BoundaryDatum(WitnessDatum):
            def actions(self, z):
                return {"DIP2": Action("DIP2", {"x": zero,
                                                "s1": zero,
                                                "s2": (Q(0), Q(-1), Q(0))},
                                       Disturbance())}

            def successor(self, z, name):
                return (1, z[1], z[2], z[3])

        datum = BoundaryDatum()
        z = witness_state(Q(1), Q(1, 49), Q(0))
        w = (Q(49), Q(1))
        self.assertTrue(admissible(datum, z, "DIP2", mode="w", w=w))
        self.assertEqual(Q(49) * Q(1, 49) + Q(1) * Q(-1), Q(0))


class TestBeliefWitness(unittest.TestCase):
    DEMO = dict(
        F={"x1": {"a": ["x1"], "b": ["x4"]},
           "x2": {"a": ["x4"], "b": ["x2"]},
           "x4": {"a": ["x3"], "b": ["x3"]},
           "x3": {"a": ["x3"], "b": ["x3"]}},
        gamma={"x1": "y12", "x2": "y12", "x4": "y4", "x3": "y3"},
        safe={"x1", "x2", "x4"})

    def test_explainer_returns_counterexample(self):
        ex = explain_belief_failure(prior=["x1", "x2"], horizon=2, **self.DEMO)
        self.assertEqual(ex["horizon"], 2)
        self.assertEqual(ex["belief"], ["y12"])
        for a in ("a", "b"):
            self.assertEqual(ex["actions"][a]["reason"], "post-belief not 1-step viable")
            self.assertEqual(sorted(ex["actions"][a]["post_belief"]), ["y12", "y4"])

    def test_bound_raises_no_partial_results(self):
        from safetransition import belief_backward
        with self.assertRaises(RuntimeError):
            belief_backward(prior=["x1", "x2"], horizon=2, max_beliefs=1,
                            **self.DEMO)


if __name__ == "__main__":
    unittest.main()
