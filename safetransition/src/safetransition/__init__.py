"""SafeTransition: exact rational certification of transition safety.

Typed assessment operators, backward recursions, Farkas obstruction
certificates, and dashboard readings for sustainability transitions.
The mathematical basis is the companion pair of manuscripts by
A. Abaee — *Aggregate Indices and Transition Safety* and *An Obstruction
Calculus for Viability under Incomplete Observation* — with all quoted
benchmark values verified in the companion deposit,
DOI 10.6084/m9.figshare.33764023.
"""
from .rational import Q, frac, fmt, fmtf
from .datum import (Action, Disturbance, TransitionDatum, WitnessDatum,
                    witness_state, describe_state, TubeStatus)
from .operators import E, V, V_weak, admissible, check_chain, MODES
from .recursion import (typed_backward, one_period_typed_viable, belief_backward,
                        explain_belief_failure)
from .certificates import (FarkasCertificate, CertifyResult, certify_polyhedron,
                           common_action_obstruction, fibre_criterion)
from .indicators import Readings, compute, licensing_thresholds, weight_partition
from .benchmark import (run_benchmark, schedule_data, BenchmarkResult,
                        benchmark_certificate, tube_certificate)

__version__ = "1.2.0"

__all__ = [
    "Q", "frac", "fmt", "fmtf",
    "Action", "Disturbance", "TransitionDatum", "WitnessDatum",
    "witness_state", "describe_state", "TubeStatus",
    "E", "V", "V_weak", "admissible", "check_chain", "MODES",
    "typed_backward", "one_period_typed_viable", "belief_backward",
    "explain_belief_failure",
    "FarkasCertificate", "CertifyResult", "certify_polyhedron",
    "common_action_obstruction", "fibre_criterion",
    "Readings", "compute", "licensing_thresholds", "weight_partition",
    "run_benchmark", "schedule_data", "BenchmarkResult",
    "benchmark_certificate", "tube_certificate",
    "__version__",
]
