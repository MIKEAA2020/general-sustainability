"""Operator chain, witnessed separation, and recursion facts on the
witness datum (exact)."""
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition.datum import WitnessDatum, witness_state
from safetransition.operators import E, V, V_weak, check_chain
from safetransition.recursion import one_period_typed_viable, belief_backward
from safetransition.indicators import compute, licensing_thresholds

DATUM = WitnessDatum()
FP_WITNESS = witness_state(Q(1, 2), Q(6, 5), Q(6, 5))
RESCUE_WITNESS = witness_state(Q(3, 2), Q(6, 5), Q(6, 5))


class TestOperators(unittest.TestCase):
    def test_chain_inclusions_at_witnesses(self):
        for z in (FP_WITNESS, RESCUE_WITNESS):
            for incl, holds in check_chain(DATUM, z, (Q(1), Q(1))):
                self.assertTrue(holds, msg=f"{incl} fails at {z}")

    def test_witnessed_separation(self):
        # typed operator empty at the FP witness ...
        self.assertEqual(E(DATUM, FP_WITNESS, mode="typ"), frozenset())
        # ... but the aggregate operator licenses a plan at w = (1, 1)
        self.assertIn("FAST", E(DATUM, FP_WITNESS, mode="w", w=(Q(1), Q(1))))
        # and per-weight licensing covers every positive ratio r = w2/w1
        for w in ((Q(3), Q(1)), (Q(1), Q(1)), (Q(1), Q(3)), (Q(2, 3), Q(1)), (Q(1), Q(3, 2))):
            self.assertTrue(E(DATUM, FP_WITNESS, mode="w", w=w), msg=f"V_w empty at w={w}")

    def test_typed_operator_requires_capacity(self):
        # FAST admissible (typed) iff s1 >= 2; STAGED iff x >= 1; SLOW iff s2 >= 2
        self.assertIn("FAST", E(DATUM, witness_state(Q(1, 2), Q(2), Q(6, 5)), mode="typ"))
        self.assertNotIn("FAST", E(DATUM, witness_state(Q(1, 2), Q(9, 5), Q(6, 5)),
                                    mode="typ"))
        self.assertIn("STAGED", E(DATUM, witness_state(Q(1), Q(6, 5), Q(6, 5)), mode="typ"))
        self.assertNotIn("STAGED", E(DATUM, witness_state(Q(1) - Q(1, 5), Q(6, 5), Q(6, 5)),
                                      mode="typ"))

    def test_endpoint_operator_weakest(self):
        # E_end,typ nonempty at the FP witness while E_typ is empty (paper's photographic reading)
        self.assertTrue(E(DATUM, FP_WITNESS, mode="end_typ"))
        self.assertFalse(E(DATUM, FP_WITNESS, mode="typ"))

    def test_recursion_and_v_weak(self):
        grid = [witness_state(Q(x), Q(s1), Q(s2))
                for x in (Q(1, 2), Q(1), Q(3, 2))
                for s1 in (Q(6, 5), Q(2)) for s2 in (Q(6, 5), Q(2))]
        weights = [(Q(3), Q(1)), (Q(1), Q(1)), (Q(1), Q(3))]
        vtyp = one_period_typed_viable(DATUM, grid)
        vweak = V_weak(DATUM, grid, weights)
        # witnessed separation persists: FP witness outside V_typ, inside V_weak
        self.assertNotIn(FP_WITNESS, vtyp)
        self.assertIn(FP_WITNESS, vweak)
        # any state with s1 >= 2 or s2 >= 2 or x >= 1 is typed-viable
        self.assertIn(witness_state(Q(1), Q(6, 5), Q(6, 5)), vtyp)


class TestIndicators(unittest.TestCase):
    def test_thresholds_exact_and_crosschecked(self):
        self.assertEqual(licensing_thresholds(), (Q(2, 3), Q(3, 2)))
        r = compute()
        self.assertTrue(r.threshold_crosscheck_ok)
        self.assertEqual(r.rho1, Q(2, 3))
        self.assertEqual(r.rho2, Q(3, 2))
        self.assertEqual(r.kappa_star, Q(1, 2))

    def test_blindness_alarm(self):
        r = compute()
        self.assertTrue(r.blind_alarm)
        self.assertEqual(r.index_min, Q(2, 5))
        self.assertEqual(r.floor_min, Q(-4, 5))

    def test_rescue_witness_reading(self):
        # at the rescue witness the typed-safe STAGED plan is financed:
        # no shortfall, no floor breach, no alarm along STAGED
        r = compute(state=RESCUE_WITNESS, plan="STAGED")
        self.assertEqual(r.kappa_star, Q(0))
        self.assertFalse(r.blind_alarm)
        # the composite index along STAGED: floors grow, so the minimum is
        # at t = 0 and equals 2 x 6/5 = 12/5
        self.assertEqual(r.index_min, Q(12, 5))
        # while the licensed FAST plan remains index-blind at w = (1, 1)
        r_fast = compute(state=RESCUE_WITNESS, plan="FAST")
        self.assertTrue(r_fast.blind_alarm)


class TestBeliefRecursion(unittest.TestCase):
    def test_post_observation_recourse_failure(self):
        # three-state instance of the companion obstruction-calculus paper:
        # V = {x1, x2, x4}; x1 -a-> x1, x1 -b-> x4; x2 -a-> x4, x2 -b-> x2;
        # x4 -> x3 (violation) under both actions; observation merges x1, x2.
        F = {"x1": {"a": ["x1"], "b": ["x4"]},
             "x2": {"a": ["x4"], "b": ["x2"]},
             "x4": {"a": ["x3"], "b": ["x3"]},
             "x3": {"a": ["x3"], "b": ["x3"]}}
        gamma = {"x1": "y12", "x2": "y12", "x4": "y4", "x3": "y3"}
        safe = {"x1", "x2", "x4"}
        W, start = belief_backward(F, gamma, safe, prior=["x1", "x2"], horizon=2)
        self.assertEqual(start, frozenset({"y12"}))
        self.assertIn(start, W[1], "root belief must be one-step viable")
        self.assertNotIn(start, W[2], "post-observation recourse failure must surface at k=2")


if __name__ == "__main__":
    unittest.main()
