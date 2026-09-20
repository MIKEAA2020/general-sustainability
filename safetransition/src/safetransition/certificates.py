"""Obstruction and infeasibility certificates (exact).

Implements the finitely checkable certificate family of the companion
manuscript *An Obstruction Calculus for Viability under Incomplete
Observation*:

* :func:`certify_polyhedron` — exact rational Fourier-Motzkin elimination
  with multiplier tracking; infeasibility is returned as a Farkas
  certificate ``lam >= 0`` with ``lam^T A = 0`` and ``lam^T b < 0``,
  together with the infeasibility margin ``-lam^T b > 0``.

* :func:`common_action_obstruction` — finite form of the common-action
  obstruction: if the safe-action sets of a family of compatible states
  intersect emptily, no observation-based policy is viable, even though
  every state is individually viable under full information. A minimal
  conflicting subfamily is reported (the sparse-witness bound is
  ``m + 1`` states for ``m`` stacked constraints in the polyhedral form).

* :func:`fibre_criterion` — the observation-fibre criterion: an exact
  observation-only certifier exists iff safe-set membership is constant
  on observation fibres; a violating fibre is reported otherwise.

All verdicts are exact; no floating-point enters any check.
"""
from dataclasses import dataclass, field
from fractions import Fraction as Q
from itertools import combinations

from .rational import frac, fmt


@dataclass(frozen=True)
class FarkasCertificate:
    """A Farkas infeasibility certificate for ``A u <= b``:
    ``lam >= 0``, ``lam^T A = 0``, ``lam^T b < 0``."""

    A: tuple
    b: tuple
    lam: tuple

    def verify(self):
        """Exact re-verification of the three defining identities."""
        m = len(self.A)
        if any(l < 0 for l in self.lam):
            return False
        n = len(self.A[0]) if m else 0
        for j in range(n):
            if sum(self.lam[i] * self.A[i][j] for i in range(m)) != 0:
                return False
        return sum(self.lam[i] * self.b[i] for i in range(m)) < 0

    @property
    def margin(self):
        """Infeasibility margin ``-lam^T b > 0`` (exact)."""
        m = len(self.A)
        return -sum(self.lam[i] * self.b[i] for i in range(m))

    def to_dict(self):
        """Canonical JSON-ready dictionary (rationals as strings)."""
        return {
            "type": "farkas",
            "A": [[str(v) for v in row] for row in self.A],
            "b": [str(v) for v in self.b],
            "lam": [str(v) for v in self.lam],
        }

    @classmethod
    def from_dict(cls, d):
        """Rebuild from a dictionary as produced by :meth:`to_dict`."""
        assert d.get("type") == "farkas", "not a farkas certificate"
        return cls(A=tuple(tuple(frac(v) for v in row) for row in d["A"]),
                   b=tuple(frac(v) for v in d["b"]),
                   lam=tuple(frac(v) for v in d["lam"]))

    def describe(self):
        return ("Farkas certificate: lam = (" + ", ".join(fmt(l) for l in self.lam)
                + "); lam.A = 0; -lam.b = " + fmt(self.margin) + " > 0")


@dataclass
class CertifyResult:
    status: str                      # "feasible" | "infeasible"
    certificate: FarkasCertificate = None
    eliminations: int = 0

    @property
    def infeasible(self):
        return self.status == "infeasible"


def certify_polyhedron(A, b):
    """Exact feasibility verdict for ``A u <= b`` via Fourier-Motzkin
    elimination with provenance tracking. On infeasibility, the returned
    certificate's multiplier vector is the provenance of a derived
    contradiction ``0 <= c, c < 0``, re-verified exactly."""
    A = [tuple(frac(v) for v in row) for row in A]
    b = [frac(v) for v in b]
    m, n = len(A), len(A[0]) if A else 0
    # rows: (coeffs, rhs, provenance vector over original rows)
    rows = [(A[i], b[i], tuple(Q(1) if k == i else Q(0) for k in range(m)))
            for i in range(m)]
    elims = 0
    for var in range(n):
        pos = [r for r in rows if r[0][var] > 0]
        neg = [r for r in rows if r[0][var] < 0]
        zer = [r for r in rows if r[0][var] == 0]
        new = list(zer)
        for p in pos:
            cp = p[0][var]
            for q in neg:
                cn = q[0][var]          # negative
                coeffs = tuple((Q(0) - cn) * p[0][j] + cp * q[0][j] for j in range(n))
                rhs = (Q(0) - cn) * p[1] + cp * q[1]
                prov = tuple((Q(0) - cn) * p[2][k] + cp * q[2][k] for k in range(m))
                if all(c == 0 for c in coeffs):
                    if rhs < 0:
                        s = sum(prov)
                        lam = tuple(l / s for l in prov)
                        cert = FarkasCertificate(A=tuple(A), b=tuple(b), lam=lam)
                        assert cert.verify(), "internal: derived certificate failed verification"
                        return CertifyResult("infeasible", cert, elims)
                else:
                    new.append((coeffs, rhs, prov))
        rows = new
        elims += 1
    # any remaining all-zero row with negative rhs is a contradiction
    for coeffs, rhs, prov in rows:
        if all(c == 0 for c in coeffs) and rhs < 0:
            s = sum(prov)
            lam = tuple(l / s for l in prov)
            cert = FarkasCertificate(A=tuple(A), b=tuple(b), lam=lam)
            assert cert.verify(), "internal: derived certificate failed verification"
            return CertifyResult("infeasible", cert, elims)
    return CertifyResult("feasible", None, elims)


def common_action_obstruction(safe_sets):
    """Finite common-action obstruction.

    ``safe_sets`` maps each state of a compatible family to its safe
    action set. The obstruction fires iff the intersection is empty
    while each individual set is nonempty (every state individually
    viable under full information). Returns a dict with keys ``fires``,
    ``minimal_conflict`` (a minimal subfamily of states with empty
    intersection, minimum-cardinality: found by exhaustive search in nondecreasing size, so every strictly smaller subfamily is certified to intersect),
    ``intersection`` and ``sizes``.
    """
    states = list(safe_sets)
    sets = {s: frozenset(safe_sets[s]) for s in states}
    full = frozenset.intersection(*sets.values()) if states else frozenset()
    result = {
        "fires": len(states) > 0 and len(full) == 0
        and all(len(v) > 0 for v in sets.values()),
        "minimal_conflict": None,
        "intersection": sorted(full),
        "sizes": {s: len(sets[s]) for s in states},
    }
    if result["fires"]:
        for r in range(2, len(states) + 1):
            for sub in combinations(states, r):
                if not frozenset.intersection(*(sets[s] for s in sub)):
                    result["minimal_conflict"] = list(sub)
                    return result
    return result


def fibre_criterion(states, safe_fn, gamma):
    """Observation-fibre criterion for exact observation-only certification.

    An exact certifier exists iff safe-set membership (the boolean
    ``safe_fn``) is constant on every observation fibre of ``gamma``.
    Returns ``(exists, violating_fibre)``: ``violating_fibre`` is a dict
    ``{"label": ..., "states": [...], "safe": [...], "unsafe": [...]}``
    or ``None``."""
    fibres = {}
    for x in states:
        fibres.setdefault(gamma[x], []).append(x)
    for label, members in fibres.items():
        safe = [x for x in members if safe_fn(x)]
        unsafe = [x for x in members if not safe_fn(x)]
        if safe and unsafe:
            return False, {"label": label, "states": members,
                           "safe": safe, "unsafe": unsafe}
    return True, None
