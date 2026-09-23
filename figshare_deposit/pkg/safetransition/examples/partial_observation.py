"""Partial-observation demonstrations (exact).

1. The three-state post-observation recourse failure: the root belief is
   one-step viable, yet exits at the second step under every observation-
   based policy — witnessed only by the belief-space recursion.
2. The observation-fibre criterion on the same system.
3. The Farkas certificate for a stacked infeasible control window.
4. The pooled-kernel identity of the deposited double-integrator
   instance: weights lam = (3/8, 5/16, 5/16) with sum lam_j n_j = 0.
"""
import sys
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from safetransition.certificates import certify_polyhedron, fibre_criterion
from safetransition.recursion import belief_backward

# 1 -------------------------------------------------------------------
F = {"x1": {"a": ["x1"], "b": ["x4"]},
     "x2": {"a": ["x4"], "b": ["x2"]},
     "x4": {"a": ["x3"], "b": ["x3"]},
     "x3": {"a": ["x3"], "b": ["x3"]}}
gamma = {"x1": "y12", "x2": "y12", "x4": "y4", "x3": "y3"}
safe = {"x1", "x2", "x4"}
W, start = belief_backward(F, gamma, safe, prior=["x1", "x2"], horizon=2)
assert start == frozenset({"y12"})
assert start in W[1] and start not in W[2]
print("[OK] root belief {y12}: one-step viable, exits at step 2 (recourse failure)")

# 2 -------------------------------------------------------------------
exists, fibre = fibre_criterion(["x1", "x2", "x4"],
                                lambda s: s != "x2", gamma)
assert exists is False and fibre["label"] == "y12"
print("[OK] fibre criterion: no exact observation-only certifier; "
      "violating fibre y12 = {x1, x2}")

# 3 -------------------------------------------------------------------
res = certify_polyhedron([[Q(1)], [Q(-1)]], [Q(2, 5), Q(-3, 5)])
assert res.infeasible and res.certificate.verify()
assert res.certificate.lam == (Q(1, 2), Q(1, 2))
print("[OK] Farkas:", res.certificate.describe())

# 4 -------------------------------------------------------------------
n = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
lam = [Q(3, 8), Q(5, 16), Q(5, 16)]
assert sum(lam) == Q(1)
assert all(sum(lam[j] * n[j][d] for j in range(3)) == 0 for d in range(2))
print("[OK] pooled kernel: sum lam = 1 and sum lam_j n_j = 0 (exact)")
