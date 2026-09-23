"""The twenty-four exact benchmark checks must pass, unchanged."""
import unittest

from _bootstrap import *  # noqa: F401,F403
from safetransition.benchmark import run_benchmark


class TestBenchmark(unittest.TestCase):
    def setUp(self):
        self.res = run_benchmark(verbose=False)

    def test_all_checks_pass(self):
        failed = [l for l, c in self.res.checks if not c]
        self.assertTrue(self.res.all_pass,
                        msg="failed: " + ("; ".join(failed) or "count mismatch"))

    def test_check_count(self):
        self.assertEqual(self.res.total, 24)

    def test_ground_truth_values(self):
        from safetransition.benchmark import RHO1, RHO2, sigma
        from fractions import Fraction as Q
        self.assertEqual((RHO1, RHO2), (Q(2, 3), Q(3, 2)))
        self.assertEqual(sigma(Q(16, 5)), Q(1088, 125))


if __name__ == "__main__":
    unittest.main()
