#!/usr/bin/env python3
"""lean_README_v14.md -> lean_README_v15.md

v39: prop:deadline built (EBC closes); build 59 -> 60 jobs,
53 -> 54 modules. Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v14.md"
DST = "/home/user/lean_README_v15.md"

DEADLINE_SECTION = """

### `prop:deadline` — status (v39)

**Built.** paper2_exact_belief_computation_v10, ll. 365–392: hold for
`T` steps (drift `−1/2`), the parameter revealed exactly at `T`, then
matched forever (drift `+3/10` on every branch). Viability holds exactly
when `z₀ ≥ 1 + T/2`.

**Why this needs no delayed-instance machinery.** The delay lives
entirely in the *shape of the action sequence*, not in the state. For
branch `θ` the realized sequence is `hold^T ++ (matched θ)^n`, and
`survivesTo I θ us z0` is already a branchwise predicate taking an
arbitrary action list, so adaptivity after revelation costs nothing:
each branch supplies its own list, and `matched` is `θ`-dependent by
construction. No state expansion, no belief or filter, no new transition
structure. The revelation event itself is never modelled, because the
claim concerns the realized trajectory — which is how the paper's own
proof proceeds: *"under the hold every cell drifts −1/2 … after
revelation the matched action rises at +3/10 on every branch"*, and
*"the direct branchwise argument needs no scalar-additivity
hypothesis"*.

The paper's two numbers were already in the layer: hold scores
`ipi = 0` (`hold_action_zero`) so drifts `−1/2`; matched scores
`ipi = m` (`ipi_matched`) so at `m = 4` drifts `−1/2 + 4/5 = +3/10`,
which the layer carries as `matched_scale_m4` (`10·d = 3`).

| fact | theorem |
|---|---|
| the deadline policy | `EBC_Deadline.deadlineSeq` |
| hold drifts `−1/2` | `holdAct_drift` |
| matched drift `≥ 0` at `m = 4` | `matched_drift_nonneg` |
| `t` holds accumulate `t·(−1/2)` | `totalDrift_holdRep` |
| survival to revelation forces `z₀ ≥ 1 + T/2` | `deadline_necessity` |
| the converse for the hold phase | `holdRep_survives` |
| `z ≥ 1` plus nonnegative drift survives any tail | `matchedRep_survives` |
| survival across a concatenation | `survivesTo_append` |
| `z₀ ≥ 1 + T/2` gives survival at every horizon | `deadline_sufficiency` |
| **the law** | `deadline_law` |
| the policy uses only the paper's 17 actions | `deadlineSeq_inAlphabet` |

Two notes on the formalization:

* Sufficiency needs only `d ≥ 0`, not the exact `3/10` — once `z ≥ 1` a
  nonnegative drift keeps every later state at or above the floor. That
  keeps the `4/5 − 1/2 = 3/10` identity off the critical path; the value
  itself is already in the layer.
* `T` is left symbolic. The paper states `T = 0,…,4`, but nothing in the
  argument uses the restriction.

**EBC is closed.** `prop:bands` (all four clauses), `prop:ladder`
(complete on the EBC side, bridge recorded as structural), and
`prop:deadline` are done. What remains of EBC — `prop:pbvi`,
`prop:census`, the 5,219-policy / 60-step search, the 84 pairings, the
65,536 subsets — is instance-level and belongs to the Python verifier
rather than to Lean.
"""

PATCHES = [
    ("### v14 — result-level index",
     "### v15 — result-level index",
     "title v14 -> v15"),
    ("`lake build` → **rc = 0, 59 jobs** (53 imported modules). Zero `sorry`.",
     "`lake build` → **rc = 0, 60 jobs** (54 imported modules). Zero `sorry`.",
     "build state 59 -> 60 jobs"),
    ("`EBC_Ladder`, `EBC_Ladder_v2` (v37) |",
     "`EBC_Ladder`, `EBC_Ladder_v2` (v37); `EBC_Deadline` (v39) |",
     "ebc slot row"),
    ("Build went 57 → 59 jobs, 51 → 53 modules.",
     "Build went 57 → 59 jobs (v38) → 60 jobs, 54 modules (v39).",
     "v39 addendum note"),
]

def main():
    s = io.open(SRC, encoding="utf-8").read()
    for old, new, label in PATCHES:
        if old in s:
            s = s.replace(old, new, 1)
            print(f"ok   {label}")
        else:
            print(f"MISS {label}")
    s = s.rstrip("\n") + "\n" + DEADLINE_SECTION
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
