"""Randomized property tests and degenerate-case tests (joint-audit
items: property-based coverage, degenerate systems, independent
feasibility oracle, canonical-JSON cross-process stability).

All randomness is seeded; the run writes nothing and asserts counters.
The feasibility oracle is a third, independent decision method (exact
Cramer/vertex enumeration over all basic subsets) sharing no code with
Fourier-Motzkin elimination or the checker."""
import itertools
import json
import os
import random
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q

from _bootstrap import *  # noqa: F401,F403
from safetransition import (WitnessDatum, belief_backward, certify_polyhedron,
                            witness_state)
from safetransition.operators import E, check_chain
from safetransition.indicators import weight_partition
from safetransition.recursion import failure_certificate

CHECKER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "check_safe_transition_cert.py")
PKG_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def brute_force_feasible(A, b):
    """Independent oracle: a <= system over Q^m is feasible iff some basic
    solution (solver of a square subsystem, or the origin-side homogeneous
    case) satisfies all rows. Exact Cramer with Fraction; exhaustive over
    subsets of rows of size m."""
    m = len(A[0]) if A else 0
    n = len(A)
    if m == 0:
        return all(bi >= 0 for bi in b)
    if n < m:
        subsets = []
    else:
        subsets = itertools.combinations(range(n), m)
    cand = set()
    for sub in subsets:
        M = [list(A[i]) + [b[i]] for i in sub]
        # Gaussian elimination on the square system
        sol = _solve_square([row[:] for row in M], m)
        if sol is not None:
            cand.add(tuple(sol))
    for u in cand:
        if all(sum(A[i][j] * u[j] for j in range(m)) <= b[i] for i in range(n)):
            return True
    return False


def _solve_square(M, m):
    for col in range(m):
        piv = next((r for r in range(col, m) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(m):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[col])]
    return [M[r][m] for r in range(m)]


class TestPropertyRandom(unittest.TestCase):
    SEED = 20260920

    def test_operator_chain_inclusion_random(self):
        rng = random.Random(self.SEED)
        datum = WitnessDatum()
        n_checked = 0
        for _ in range(60):
            z = witness_state(Q(rng.randint(0, 3), rng.randint(1, 4)),
                              Q(rng.randint(1, 8), rng.randint(1, 4)),
                              Q(rng.randint(1, 8), rng.randint(1, 4)))
            w = (Q(rng.randint(1, 9), rng.randint(1, 5)),
                 Q(rng.randint(1, 9), rng.randint(1, 5)))
            sets = {m: E(datum, z, mode=m, w=w)
                    for m in ("typ", "w", "tube_phys", "end", "end_typ")}
            self.assertTrue(sets["typ"] <= sets["w"] <= sets["tube_phys"]
                            <= sets["end"])
            self.assertTrue(sets["typ"] <= sets["end_typ"] <= sets["end"])
            n_checked += 1
        self.assertEqual(n_checked, 60)

    def test_farkas_validity_and_oracle_crosscheck_random(self):
        # The vertex-enumeration oracle requires full column rank; the
        # generator enforces it (regenerating rank-deficient draws).
        rng = random.Random(self.SEED + 1)

        def rank(M):
            M = [row[:] for row in M]
            r, cols = 0, len(M[0]) if M else 0
            for c in range(cols):
                piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
                if piv is None:
                    continue
                M[r], M[piv] = M[piv], M[r]
                pv = M[r][c]
                M[r] = [v / pv for v in M[r]]
                for i in range(len(M)):
                    if i != r and M[i][c] != 0:
                        f = M[i][c]
                        M[i] = [a - f * b for a, b in zip(M[i], M[r])]
                r += 1
            return r

        for trial in range(60):
            m = rng.randint(1, 3)          # variables
            n = rng.randint(m + 1, m + 4)  # rows
            A = [[Q(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(m)]
                 for _ in range(n)]
            if rank(A) < m:
                continue
            style = trial % 2
            if style == 0:   # planted infeasible: u_j bounds crossing
                A[0] = [Q(1)] + [Q(0)] * (m - 1)
                A[1] = [-Q(1)] + [Q(0)] * (m - 1)
                b = [Q(2, 5)] + [Q(-3, 5)] + [Q(rng.randint(-2, 4), rng.randint(1, 3))
                                              for _ in range(n - 2)]
            else:            # planted feasible: u = 0 works
                b = [Q(rng.randint(0, 4), rng.randint(1, 3)) for _ in range(n)]
            res = certify_polyhedron(A, b)
            oracle = brute_force_feasible(A, b)
            self.assertEqual(res.infeasible, not oracle,
                             (A, b, res.infeasible, oracle))
            if res.infeasible:
                self.assertTrue(res.certificate.verify())

    def test_belief_monotonicity_random(self):
        rng = random.Random(self.SEED + 2)
        for _ in range(25):
            n_states = rng.randint(3, 6)
            states = [f"x{i}" for i in range(n_states)]
            labels = [f"y{i}" for i in range(rng.randint(2, n_states))]
            gamma = {s: rng.choice(labels) for s in states}
            safe = set(s for s in states if rng.random() < 0.8) or {states[0]}
            # uniform action menu (the recursion's documented domain):
            # every state offers the same actions, each single-valued
            names = [f"a{k}" for k in range(rng.randint(1, 2))]
            targets = {nm: rng.choice(states) for nm in names}
            F = {s: {nm: [targets[nm]] for nm in names} for s in states}
            prior = [rng.choice(states)]
            try:
                W, _ = belief_backward(F, gamma, safe, prior, 3,
                                       max_beliefs=2000)
            except RuntimeError:
                continue
            for k in range(2, 4):
                self.assertTrue(W[k] <= W[k - 1], (k, F, gamma, safe))

    def test_weight_partition_coverage_random(self):
        rng = random.Random(self.SEED + 3)
        from fractions import Fraction as QF
        for _ in range(20):
            s1 = QF(rng.randint(1, 12), rng.randint(4, 10))
            s2 = QF(rng.randint(1, 12), rng.randint(4, 10))
            dip = QF(rng.randint(6, 16), rng.randint(2, 4))
            if not (0 < s1 < dip and 0 < s2 < dip):
                continue
            part = weight_partition(state=(0, QF(1), s1, s2), dip=dip)
            rho1, rho2 = QF(part["thresholds"]["rho1"]), QF(part["thresholds"]["rho2"])
            for _ in range(5):
                r = QF(rng.randint(1, 300), rng.randint(1, 20))
                lic = set()
                if r >= rho1:
                    lic.add("FAST")
                if r <= rho2:
                    lic.add("SLOW")
                if QF(part["state"]["x"]) >= 1:
                    lic.add("STAGED")
                got = None
                for rg in part["regions"]:
                    lo = QF(rg["range"]["lo"])
                    hi = rg["range"]["hi"]
                    ok = (r >= lo) and (hi == "inf" or r <= QF(hi)) and \
                         not (r == lo and not rg["range"]["lo_inc"]) and \
                         not (hi != "inf" and r == QF(hi) and not rg["range"]["hi_inc"])
                    if ok:
                        got = set(rg["licensed"])
                self.assertIsNotNone(got, (r, part))
                self.assertEqual(got, lic, (r, s1, s2, dip))

    def test_canonical_json_cross_process_hashseed(self):
        cert = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()
        digests = set()
        for seed in ("0", "1", "12345"):
            code = (
                "import json, hashlib, sys\n"
                f"cert = json.loads({json.dumps(json.dumps(cert))})\n"
                "ser = json.dumps(cert, sort_keys=True, separators=(',', ':'))\n"
                "print(hashlib.sha256(ser.encode('utf-8')).hexdigest())\n"
            )
            env = dict(os.environ, PYTHONHASHSEED=seed)
            r = subprocess.run([sys.executable, "-c", code],
                               capture_output=True, text=True, env=env)
            self.assertEqual(r.returncode, 0, r.stderr)
            digests.add(r.stdout.strip())
        self.assertEqual(len(digests), 1)

    def test_tamper_fuzz_rejected(self):
        # multiplier and matrix mutations break the defining identities,
        # so the checker must reject every one; bound mutations are the
        # documented algebra/semantics boundary: a bound change that
        # leaves the system infeasible with the same multiplier vector is
        # an algebraically valid certificate for the TAMPERED system and
        # verifies (the checker checks the certificate against the
        # supplied system, not the system against the intended datum).
        rng = random.Random(self.SEED + 5)
        base = certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()
        rejected = 0
        for _ in range(30):
            c = json.loads(json.dumps(base))
            field = rng.choice(["lam0", "lam1", "A00", "A10"])
            delta = Q(rng.choice([1, -1]))
            if field == "lam0":
                c["lam"][0] = str(Q(c["lam"][0]) + Q(1, 3))
            elif field == "lam1":
                c["lam"][1] = str(Q(c["lam"][1]) + Q(1, 3))
            elif field == "A00":
                c["A"][0][0] = str(Q(c["A"][0][0]) + delta)
            elif field == "A10":
                c["A"][1][0] = str(Q(c["A"][1][0]) + delta)
            with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
                json.dump(c, fh); path = fh.name
            res = subprocess.run([sys.executable, CHECKER, path],
                                 capture_output=True, text=True)
            os.unlink(path)
            if res.returncode != 0:
                rejected += 1
        self.assertEqual(rejected, 30)

    def test_bound_mutation_semantics_boundary(self):
        # +1 on the upper bound makes the system feasible: the certificate
        # no longer proves anything, and the checker rejects it.
        c = json.loads(json.dumps(
            certify_polyhedron([[1], [-1]], ["2/5", "-3/5"]).certificate.to_dict()))
        c["b"][0] = str(Q(c["b"][0]) + 1)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(c, fh); path = fh.name
        res = subprocess.run([sys.executable, CHECKER, path],
                             capture_output=True, text=True)
        os.unlink(path)
        self.assertNotEqual(res.returncode, 0)
        # -1 keeps the system infeasible with the same lam: the tampered
        # certificate is algebraically valid for the tampered system and
        # verifies -- exactly the checker's documented scope (algebraic
        # validity relative to the supplied system).
        c["b"][0] = str(Q(c["b"][0]) - 2)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(c, fh); path = fh.name
        res = subprocess.run([sys.executable, CHECKER, path],
                             capture_output=True, text=True)
        os.unlink(path)
        self.assertEqual(res.returncode, 0, res.stdout)


class TestDegenerateCases(unittest.TestCase):
    def test_empty_and_zero_row_systems(self):
        self.assertFalse(certify_polyhedron([[1]], [-1]).infeasible is True or False)
        # zero-variable contradiction: 0 <= -1 expressed as all-zero row
        res = certify_polyhedron([[0]], [-1])
        self.assertTrue(res.infeasible)
        self.assertTrue(res.certificate.verify())
        # all-zero row with nonnegative rhs: feasible
        res = certify_polyhedron([[0]], [Q(0)])
        self.assertFalse(res.infeasible)

    def test_duplicate_redundant_constraints(self):
        A = [[1], [1], [1], [-1]]
        b = [Q(2, 5), Q(4, 5), Q(1), Q(-3, 5)]
        res = certify_polyhedron(A, b)
        self.assertTrue(res.infeasible)
        self.assertTrue(res.certificate.verify())
        A = [[1], [1], [-1]]
        b = [Q(1), Q(2), Q(0)]
        self.assertFalse(certify_polyhedron(A, b).infeasible)

    def test_single_variable_and_coincident_thresholds(self):
        self.assertTrue(certify_polyhedron([[1], [-1]], [Q(1), Q(-1)]).infeasible is False)
        part = weight_partition(state=(0, Q(1), Q(1), Q(1)), dip=Q(2))
        self.assertEqual(part["regime"], "rho1 = rho2")
        with self.assertRaises(ValueError):
            weight_partition(state=(0, Q(1), Q(2), Q(6, 5)), dip=Q(2))  # s1 = dip
        with self.assertRaises(ValueError):
            weight_partition(state=(0, Q(1), Q(3, 2), Q(2)), dip=Q(2))  # s2 = dip

    def test_belief_no_actions_and_empty_fibre(self):
        F = {"x1": {}, "x2": {"a": ["x1"]}}
        gamma = {"x1": "y1", "x2": "y2"}
        W, start = belief_backward(F, gamma, {"x1", "x2"}, ["x2"], 2,
                                   max_beliefs=100)
        # x1 has no actions: not 1-step viable; x2 can reach it
        self.assertNotIn(frozenset({"y1"}), W[1])
        self.assertIn(start, W[1])

    def test_failure_certificate_roundtrip_and_tamper(self):
        F = {"x1": {"a": ["x1"], "b": ["x4"]}, "x2": {"a": ["x4"], "b": ["x2"]},
             "x4": {"a": ["x3"], "b": ["x3"]}, "x3": {"a": ["x3"], "b": ["x3"]}}
        gamma = {"x1": "y12", "x2": "y12", "x4": "y4", "x3": "y3"}
        cert = failure_certificate(F, gamma, {"x1", "x2", "x4"}, ["x1", "x2"], 2)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(cert, fh); path = fh.name
        res = subprocess.run([sys.executable, CHECKER, path],
                             capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        os.unlink(path)
        cert["failure"]["actions"]["a"]["reason"] = "violation en route"
        cert["failure"]["actions"]["a"]["states"] = []
        cert["failure"]["actions"]["b"]["reason"] = "post-belief not 1-step viable"
        cert["failure"]["actions"]["b"]["post_belief"] = ["y12"]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(cert, fh); path = fh.name
        res = subprocess.run([sys.executable, CHECKER, path],
                             capture_output=True, text=True)
        self.assertNotEqual(res.returncode, 0)
        os.unlink(path)


if __name__ == "__main__":
    unittest.main()
