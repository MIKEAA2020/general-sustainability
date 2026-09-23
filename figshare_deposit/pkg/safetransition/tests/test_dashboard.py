"""Dashboard: self-contained HTML, correct tokens, no external resources."""
import re
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition.indicators import compute
from safetransition.benchmark import run_benchmark
from safetransition.dashboard import render

EXTERNAL_SRC = re.compile(r'<(script|link|img)[^>]+(src|href)="(https?:)?//', re.I)


class TestDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bench = run_benchmark(verbose=False)
        cls.html = render(compute(), benchmark=cls.bench,
                          certificates=[("demo", "Farkas certificate: lam = (1/2, 1/2)", True)])

    def test_external_free(self):
        self.assertIsNone(EXTERNAL_SRC.search(self.html),
                          "dashboard must not reference external resources")

    def test_key_tokens(self):
        for token in ("SafeTransition", "EXACT RATIONAL ARITHMETIC",
                      "BENCHMARK 24/24", "INDEX-BLINDNESS ALARM",
                      "rho", "kappa", "10.6084/m9.figshare.33764023",
                      "<svg", "2/5", "-4/5", "2/3", "3/2"):
            self.assertIn(token, self.html, msg=f"missing token: {token}")

    def test_exact_rendering_not_float_mangled(self):
        self.assertIn("1088/125", self.html)   # sustained yield, exact form
        self.assertIn("1463/125", self.html)   # FAST quota peak, exact form


if __name__ == "__main__":
    unittest.main()
