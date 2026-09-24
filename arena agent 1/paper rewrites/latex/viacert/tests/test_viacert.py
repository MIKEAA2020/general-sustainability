"""Audited-identity test suite (mirrors the CLI selftest; unittest style)."""
import unittest
from fractions import Fraction as Q
from viacert.systems import audit_system, benchmark_caps, ce_laws, timing_grid
from viacert.recursion import verdict, kernel, witness
from viacert.monitoring import (partition_census, maximal_common_action_sets,
                                delay_identity, ce_drift_report, sigma_star)


class AuditedIdentities(unittest.TestCase):
    def setUp(self):
        self.sysm = audit_system()
        self.pairs = self.sysm.pairs()
        self.agg = lambda x: x[0] + x[1]
        self.full = lambda x: x

    def test_pair_family_and_corner(self):
        self.assertEqual(len(self.pairs), 36)
        self.assertFalse(verdict(self.sysm, frozenset({(1, 1)}), self.full))

    def test_four_cell_concordance(self):
        k_agg = kernel(self.sysm, self.agg, self.pairs)
        k_full = kernel(self.sysm, self.full, self.pairs)
        k_agg_alt = kernel(self.sysm, self.agg, self.pairs, alt=True)
        k_full_alt = kernel(self.sysm, self.full, self.pairs, alt=True)
        self.assertEqual((len(k_agg_alt), len(k_agg),
                          len(k_full_alt), len(k_full)), (24, 26, 25, 28))
        self.assertEqual(k_agg & k_full_alt, k_agg_alt)

    def test_partitions(self):
        total, adm, minsz = partition_census(
            self.sysm, [(1, 2), (2, 1), (2, 2), (3, 1)])
        self.assertEqual((total, len(adm), minsz), (15, 7, 2))
        mx = maximal_common_action_sets(
            self.sysm, [(1, 2), (2, 1), (2, 2), (3, 1)])
        self.assertTrue(any(a & b == {(2, 2)}
                            for i, a in enumerate(mx) for b in mx[i + 1:]))

    def test_benchmark(self):
        cap1, cap2, Ystar = benchmark_caps()
        self.assertEqual(Ystar, Q(27, 5))
        self.assertEqual(cap1(Ystar) + cap2(Ystar), 2)

    def test_ce_drift(self):
        d_u, d_c = ce_drift_report(ce_laws())
        self.assertGreaterEqual(d_u, Q(21, 100))
        self.assertEqual(d_c, 0)

    def test_delay_identity(self):
        g = timing_grid()
        self.assertEqual(delay_identity(g), [])
        self.assertEqual(delay_identity(g, strict=True), [(Q(2), 1)])
        self.assertEqual(sigma_star(Q(2)), 1)

    def test_witness(self):
        w = witness(self.sysm, frozenset({(2, 2), (2, 1)}), self.agg, 3)
        self.assertIsNotNone(w)
        self.assertTrue(all(u in (1, 2) for _, u in w))


if __name__ == "__main__":
    unittest.main()
