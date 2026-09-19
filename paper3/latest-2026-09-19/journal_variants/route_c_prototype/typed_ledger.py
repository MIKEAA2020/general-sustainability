"""Small, dependency-free reference implementation of the typed-ledger core.

This is the route-C prototype accompanying the journal-cut drafts. It deliberately implements
only declarations, incidence construction, balance residuals, componentwise barrier checks and the
non-compensation witness. It does not claim to be the complete solver or a validated software
package. That boundary is part of the prototype's API documentation.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class Compartment:
    name: str
    type_name: str
    unit: str


@dataclass(frozen=True)
class Flux:
    name: str
    source: str
    sink: str
    kind: str = "transfer"              # transfer or conversion
    coefficient: float = 1.0             # source consumption per unit output


class LedgerError(ValueError):
    """A declaration cannot be interpreted as the typed ledger says it should be."""


class TypedLedger:
    def __init__(self, compartments: Iterable[Compartment], fluxes: Iterable[Flux]):
        self.compartments = tuple(compartments)
        self.fluxes = tuple(fluxes)
        self._index = {c.name: i for i, c in enumerate(self.compartments)}
        if len(self._index) != len(self.compartments):
            raise LedgerError("compartment names must be unique")

    def validate(self) -> tuple[str, ...]:
        """Return declaration failures; an empty tuple means the core declaration is valid."""
        failures: list[str] = []
        for f in self.fluxes:
            if f.source not in self._index or f.sink not in self._index:
                failures.append(f"{f.name}: source and sink must be declared compartments")
                continue
            if f.kind not in {"transfer", "conversion"}:
                failures.append(f"{f.name}: kind must be transfer or conversion")
            if f.coefficient <= 0:
                failures.append(f"{f.name}: conversion coefficient must be positive")
            src, dst = self.compartment(f.source), self.compartment(f.sink)
            if f.kind == "transfer":
                if src.type_name != dst.type_name or src.unit != dst.unit:
                    failures.append(f"{f.name}: transfer crosses type or unit boundary")
            elif f.kind == "conversion" and src.type_name == dst.type_name:
                failures.append(f"{f.name}: conversion must name distinct types")
        return tuple(failures)

    def compartment(self, name: str) -> Compartment:
        try:
            return self.compartments[self._index[name]]
        except KeyError as exc:
            raise LedgerError(f"unknown compartment: {name}") from exc

    def incidence(self) -> tuple[tuple[float, ...], ...]:
        """Return rows=compartments, columns=fluxes; source is negative, sink positive."""
        failures = self.validate()
        if failures:
            raise LedgerError("; ".join(failures))
        rows = [[0.0 for _ in self.fluxes] for _ in self.compartments]
        for j, f in enumerate(self.fluxes):
            rows[self._index[f.source]][j] = -f.coefficient if f.kind == "conversion" else -1.0
            rows[self._index[f.sink]][j] = 1.0
        return tuple(tuple(r) for r in rows)

    def balance_residual(
        self,
        state_dot: Sequence[float],
        rates: Sequence[float],
        boundary: Sequence[float] | None = None,
    ) -> tuple[float, ...]:
        """Return ``state_dot - (S v + boundary)`` for one declared observation."""
        if len(state_dot) != len(self.compartments):
            raise LedgerError("state_dot length does not match compartments")
        if len(rates) != len(self.fluxes):
            raise LedgerError("rates length does not match fluxes")
        boundary = tuple(boundary or (0.0 for _ in self.compartments))
        if len(boundary) != len(self.compartments):
            raise LedgerError("boundary length does not match compartments")
        S = self.incidence()
        return tuple(
            float(state_dot[i]) - (sum(S[i][j] * rates[j] for j in range(len(self.fluxes))) + boundary[i])
            for i in range(len(self.compartments))
        )

    @staticmethod
    def barriers_ok(
        trajectory: Iterable[Sequence[float]],
        lower: Sequence[float],
        upper: Sequence[float],
        *,
        tolerance: float = 1e-12,
    ) -> bool:
        lower, upper = tuple(lower), tuple(upper)
        if len(lower) != len(upper):
            raise LedgerError("barrier vectors must have equal length")
        for state in trajectory:
            if len(state) != len(lower):
                raise LedgerError("trajectory state and barrier lengths differ")
            if any(x < lo - tolerance or x > hi + tolerance for x, lo, hi in zip(state, lower, upper)):
                return False
        return True

    @staticmethod
    def residual_ok(residual: Sequence[float], *, tolerance: float = 1e-9) -> bool:
        return all(isclose(float(x), 0.0, abs_tol=tolerance) for x in residual)


def compensating_witness(weight: Sequence[float], deficit_index: int = 0) -> tuple[float, ...]:
    """Return a simple balance vector with positive aggregate and one negative component."""
    w = tuple(float(x) for x in weight)
    if not w or any(x < 0 for x in w) or all(x == 0 for x in w):
        raise LedgerError("weight must be nonnegative and nonzero")
    if not 0 <= deficit_index < len(w):
        raise LedgerError("deficit index outside weight vector")
    if w[deficit_index] == 0:
        deficit = -1.0
    else:
        deficit = -1.0
    b = [0.0] * len(w)
    b[deficit_index] = deficit
    j = next((i for i, x in enumerate(w) if i != deficit_index and x > 0), None)
    if j is None:
        raise LedgerError("need a second positively weighted component for this finite witness")
    b[j] = (1.0 - sum(w[i] * b[i] for i in range(len(w)) if i != j)) / w[j]
    return tuple(b)


def aggregate(weight: Sequence[float], balance: Sequence[float]) -> float:
    if len(weight) != len(balance):
        raise LedgerError("weight and balance lengths differ")
    return sum(float(w) * float(b) for w, b in zip(weight, balance))
