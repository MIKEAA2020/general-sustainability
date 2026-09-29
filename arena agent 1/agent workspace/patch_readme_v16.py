#!/usr/bin/env python3
"""lean_README_v15.md -> lean_README_v16.md

v40: the instance-level items were already verified by full enumeration.
Adds the instance-level section and corrects the "EBC is closed"
paragraph, which described the remaining work as outstanding.
Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v15.md"
DST = "/home/user/lean_README_v16.md"

OLD_CLOSE = """**EBC is closed.** `prop:bands` (all four clauses), `prop:ladder`
(complete on the EBC side, bridge recorded as structural), and
`prop:deadline` are done. What remains of EBC — `prop:pbvi`,
`prop:census`, the 5,219-policy / 60-step search, the 84 pairings, the
65,536 subsets — is instance-level and belongs to the Python verifier
rather than to Lean."""

NEW_CLOSE = """**EBC is closed.** `prop:bands` (all four clauses), `prop:ladder`
(complete on the EBC side, bridge recorded as structural), and
`prop:deadline` are done. The remaining EBC items — `prop:pbvi`,
`prop:census`, the 5,219-policy / 60-step search, the 84 pairings, the
subset census — are instance-level, and **were already verified by full
enumeration**: see the `prop:instance` section below."""

INSTANCE_SECTION = """

### `prop:instance` — status (v40)

**Verified by full enumeration. 30/30 checks pass, exit 0.**

The instance-level items were scoped before any decision was taken about
how to check them, and scoping found the verifier **already exists**:
`paper2_exact_belief_computation_v10_verification.py` in the latex
folder. It enumerates; it does not sample.

| item | check | result |
|---|---|---|
| 5,219 policies × 60 steps | *exhaustive 1/2/3-periodic classification (5,219 policies, 60-step certificates)* | **PASS** |
| 84 pairings | *exact point-based evaluation … 7 rational beliefs × 3 levels × 4 horizons (84 pairings); 17⁴ = 83,521 sequences deduplicate to ≤ 545 vectors* | **PASS** |
| the subset census | *antichain census: 1,048,576 raw subset evaluations collapse to 496 stored maximal sets* | **PASS** |

Runtime 7m36s. Not prohibitive; full enumeration is what runs.

**A correction on the "65,536" figure.** It is not one number. The
antichain census is **1,048,576 raw subset evaluations collapsing to 496
stored maximal sets** (16 at the edge + 32×15 above); the paper's text
carries `$2^{16} = 65{,}536$ raw subsets, $736$ stored antichain`. Both
are compression ratios over the same structure; earlier notes quoted
65,536 as *the* subset count without distinguishing it from the census
figure.

**Symmetry reduction already exists** — it is what the check measures:
raw evaluations collapse by 4,096× and 2,048× per level via a
Minato-style antichain representation (the paper cites Minato 1993).

**One defect found, and it was environmental.** The first run reported
29/30:

```
FAIL chained script exits green: paper2_exact_belief_computation_v2_verification.py (16/16)
```

The verifiers form a regression chain (v10 → v2 → v1), and each script
reads its **own `.tex` sibling** from its working directory; run outside
the latex folder each crashes with `FileNotFoundError` *after* its
mathematical checks have already passed. With the three missing siblings
fetched, the chain resolves: **30/30, exit 0**. Worth recording that the
chained check fails closed (exit 1) rather than skipping, which is
correct behaviour. Separately, the `proof completeness` check passes
while reporting one missing *optional* needle, `29-cell radius-two ball`.

**The verifier independently corroborates the Lean layer.** The two were
built separately and agree:

| Lean | verifier check |
|---|---|
| `EBC_Deadline.deadline_law` | *deadline instance on the cube: viability iff z₀ ≥ 1 + T/2* — PASS |
| `prop:ladder`, value `1/\|S\|` at the edge, `min(1, 2/\|S\|)` above | *observation ladder exact: 1/16, 1/8, 1/4, 1/2, 1 at the edge and 1/8, 1/4, 1/2, 1, 1 above* — PASS |
| `EBC_Ladder_v2.no_three_distinct_above` | *no three cells pairwise Hamming-adjacent (all C(16,3) = 560 triples)* — PASS |
| `prop:bands`, 16 singletons / 32 pairs | *16 singletons at 1.0; exactly the 32 Hamming-1 pairs at 1.1 and 2.5; nothing larger* — PASS |

The ladder row is the sharpest case. At `|S| = 16` the Lean layer's
formula gives `1/16` at the edge and `min(1, 2/16) = 1/8` above it; the
verifier's enumeration reports exactly `1/16` and `1/8` as its first two
ladder entries. Two independent derivations of the same numbers.

Full output and reproduction steps: `ebc_verification_report.md`.
"""

PATCHES = [
    ("### v15 — result-level index",
     "### v16 — result-level index",
     "title v15 -> v16"),
    (OLD_CLOSE, NEW_CLOSE, "EBC-closed paragraph -> points at prop:instance"),
]

def main():
    s = io.open(SRC, encoding="utf-8").read()
    for old, new, label in PATCHES:
        if old in s:
            s = s.replace(old, new, 1)
            print(f"ok   {label}")
        else:
            print(f"MISS {label}")
    s = s.rstrip("\n") + "\n" + INSTANCE_SECTION
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
