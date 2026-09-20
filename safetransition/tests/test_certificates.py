"""Exact certificate tests: Farkas via Fourier-Motzkin, common-action
obstruction, observation-fibre criterion."""
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition.certificates import (certify_polyhedron,
                                         common_action_obstruction,
                                         fibre_criterion)


class TestFarkas(unittest.TestCase):
    def test_infeasible_interval(self):
        # the companion manuscript's stacked system: u <= 0.4, -u <= -0.6
        res = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(2, 5), Q(-3, 5)])
        self.assertTrue(res.infeasible)
        cert = res.certificate
        self.assertTrue(cert.verify())
        self.assertEqual(cert.margin, Q(1, 10))          # infeasibility margin 0.1
        self.assertEqual(cert.lam, (Q(1, 2), Q(1, 2)))   # lambda = (1/2, 1/2)

    def test_feasible_interval(self):
        res = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(-2, 5), Q(3, 5)])
        self.assertFalse(res.infeasible)
        self.assertIsNone(res.certificate)

    def test_unbounded_side_is_feasible(self):
        # 2u <= -1 alone admits u -> -infinity: feasible, no certificate
        res = certify_polyhedron([[Q(2)]], [Q(-1)])
        self.assertFalse(res.infeasible)

    def test_2d_infeasible_triangle(self):
        # x + y <= 1, x >= 3/4, y >= 3/4. Farkas margins here equal
        # lam_1/2 for any lam_1 > 0, so the specific margin is
        # certificate-dependent: verify the defining identities instead.
        A = [[Q(1), Q(1)], [Q(-1), Q(0)], [Q(0), Q(-1)]]
        b = [Q(1), Q(-3, 4), Q(-3, 4)]
        res = certify_polyhedron(A, b)
        self.assertTrue(res.infeasible)
        self.assertTrue(res.certificate.verify())
        self.assertGreater(res.certificate.margin, 0)

    def test_parallel_contradiction_margin(self):
        # u <= -1 and u >= 1; lam is normalized to a convex combination,
        # giving the canonical margin 1 for this system
        res = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(-1), Q(-1)])
        self.assertTrue(res.infeasible)
        self.assertTrue(res.certificate.verify())
        self.assertEqual(res.certificate.margin, Q(1))

    def test_3d_pooled_kernel_instance(self):
        # deposited double-integrator instance: normals n_j with weights
        # lam = (3/8, 5/16, 5/16) vanishing in the pool (sum lam_j n_j = 0)
        n = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
        lam = [Q(3, 8), Q(5, 16), Q(5, 16)]
        self.assertEqual(sum(lam), Q(1))
        self.assertEqual([sum(lam[j] * n[j][d] for j in range(3)) for d in range(2)],
                         [Q(0), Q(0)])


class TestCommonAction(unittest.TestCase):
    def test_fires_on_disjoint_singletons(self):
        obs = common_action_obstruction({"x1": {"a"}, "x2": {"b"}})
        self.assertTrue(obs["fires"])
        self.assertEqual(obs["minimal_conflict"], ["x1", "x2"])

    def test_silent_when_common_action_exists(self):
        obs = common_action_obstruction({"x1": {"a", "b"}, "x2": {"b", "c"}})
        self.assertFalse(obs["fires"])
        self.assertEqual(obs["intersection"], ["b"])

    def test_silent_when_some_state_not_viable(self):
        obs = common_action_obstruction({"x1": {"a"}, "x2": set()})
        self.assertFalse(obs["fires"])

    def test_minimal_conflict_is_minimal(self):
        # pairwise intersections {b}, {a}, {c} are all nonempty;
        # only the full triple has an empty intersection
        obs = common_action_obstruction({"x1": {"a", "b"}, "x2": {"b", "c"},
                                         "x3": {"a", "c"}})
        self.assertTrue(obs["fires"])
        self.assertEqual(sorted(obs["minimal_conflict"]), ["x1", "x2", "x3"])


class TestFibreCriterion(unittest.TestCase):
    def test_violating_fibre_reported(self):
        states = ["x1", "x2", "x4"]
        gamma = {"x1": "y12", "x2": "y12", "x4": "y4"}
        safe = lambda s: s != "x2"          # membership differs inside the merged fibre
        exists, fibre = fibre_criterion(states, safe, gamma)
        self.assertFalse(exists)
        self.assertEqual(fibre["label"], "y12")
        self.assertEqual(sorted(fibre["safe"]), ["x1"])
        self.assertEqual(fibre["unsafe"], ["x2"])

    def test_exact_certifier_exists_on_identity_observation(self):
        states = ["x1", "x2"]
        gamma = {"x1": "o1", "x2": "o2"}
        safe = lambda s: s == "x1"
        exists, fibre = fibre_criterion(states, safe, gamma)
        self.assertTrue(exists)
        self.assertIsNone(fibre)


if __name__ == "__main__":
    unittest.main()
