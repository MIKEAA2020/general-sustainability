# viacert — viability certificates on finite systems (library MVP)

The programme's library artifact (flagship P2). Exact integer/rational
arithmetic; standard library only; deterministic. Implements the two
machine-verified cores of the obstruction programme and nothing else:

- **The recursively viable selector** (`viacert.recursion`): the
  finite-horizon read-then-act winning recursion of the calculus's
  Theorem 1 — viability verdicts, kernels, and step-1 witness
  extraction — with the institutional no-repeat codex threaded as a
  parameter (never a global).
- **The fibre/partition criteria** (`viacert.monitoring`): safe-action
  and common-safe sets, the partition-form adequacy converse, maximal
  common-action sets, the partition census, the review-timing identity
  (non-strict, boundary included) with its sigma-star convention, and
  the certainty-equivalence drift audit.

New systems plug in through `viacert.systems.FiniteSystem` (states,
actions, safe set, transition, null action). The programme's shared
three-coordinate audit system, the continuous benchmark caps, the CE
law pair, and the 48-cell review grid ship as audited default instances.

## Run

    cd viacert
    python3 -m viacert selftest        # 12 audited identities
    python3 -m unittest discover -s tests -v

## Provenance

Every audited identity is a pointer to a source edition and its
verification script — selector concordance v1 (C1–C8), minimax dual
certificates v1, monitoring design v3 (E1–E9), and the consolidated
worked-systems flagship `paper2_worked_systems_v1` whose master script
chains all seven lineage scripts (57 checks). The library reimplements
none of the claims; it packages the verified primitives for reuse and
plugs new systems into the same exactness discipline.

Repository: https://github.com/MIKEAA2020/general-sustainability
(folder `arena agent 1/paper rewrites/latex/viacert`).

AI declaration: GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI
assisted with drafting and iterative review, under the programme's
verification discipline.
