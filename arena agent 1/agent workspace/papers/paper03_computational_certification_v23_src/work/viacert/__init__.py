"""viacert — viability certificates on finite systems, exact arithmetic.

The programme's library MVP (flagship P2's artifact). It implements,
verbatim and exactly, the two machine-verified cores of the obstruction
programme:

  1. the finite-horizon recursively viable selector (the recursion of the
     calculus's Theorem 1; the concordance's `win`/`verd`, with the
     no-repeat codex threaded as a parameter — never a global);
  2. the fibre/partition criteria of the monitoring companion (the
     partition-form adequacy converse, maximal common-action sets, the
     review-timing identity, and the certainty-equivalence drift audit).

Scope and discipline: exact integer/rational arithmetic; standard library
only; deterministic. The audited systems (the three-coordinate audit
system, the continuous benchmark, the CE laws) ship as default instances;
new systems plug in through `viacert.systems.FiniteSystem`.

Nothing here is a new theorem: every identity is a pointer to a source
edition and its verification script (see README.md). AI declaration: GLM
(Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and
iterative review. The author reviewed and edited outputs and takes
responsibility for the final work.
"""
from .systems import FiniteSystem, audit_system, benchmark_caps, ce_laws, timing_grid
from .recursion import viable, verdict, kernel, witness
from .monitoring import (
    safe_actions, common_safe, fibre_partition, adequate, maximal_common_action_sets,
    partition_census, sigma_star, delay_identity, ce_drift_report,
)

__all__ = [
    "FiniteSystem", "audit_system", "benchmark_caps", "ce_laws", "timing_grid",
    "viable", "verdict", "kernel", "witness",
    "safe_actions", "common_safe", "fibre_partition", "adequate",
    "maximal_common_action_sets", "partition_census",
    "sigma_star", "delay_identity", "ce_drift_report",
]
__version__ = "0.1.0"
