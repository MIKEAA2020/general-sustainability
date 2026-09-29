#!/usr/bin/env python3
"""lean_README_v12.md -> lean_README_v13.md

v37: prop:bands is now closed in all four clauses (the z0 >= 1.1
"nothing larger" half landed as far_pair_horizon_bound), and prop:ladder
is analysed and scoped. Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v12.md"
DST = "/home/user/lean_README_v13.md"

TITLE_OLD = "### v12 — result-level index"
TITLE_NEW = "### v13 — result-level index"

V13_NOTE = """
>
> **v37 addendum.** `prop:bands` is now **closed in all four clauses**.
> The `z₀ ≥ 1.1` half of "nothing larger" landed: `cor_hamming_m4` is
> stated at `z₀ = 1` and does not transfer to a higher start, so the
> pair-sum bound was re-derived with `z₀` as a parameter
> (`EBC_Classification_v2`), giving `|us| ≤ 10·(z₀ − 1)` after the
> arithmetic reduction (`EBC_Classification_v3`). At `z₀ = 1.1` a pair
> at Hamming distance `≥ 2` survives at most **one step**, so no such
> pair appears in any set that survives at every horizon. The counts 16
> and 32 remain instance-level, with the verifier.
>
> `prop:ladder` is analysed and scoped but **not yet started** — see the
> note in the EBC section. Build went 55 → 57 jobs, 49 → 51 modules."""

BUILD_OLD = "`lake build` → **rc = 0, 55 jobs** (49 imported modules). Zero `sorry`."
BUILD_NEW = "`lake build` → **rc = 0, 57 jobs** (51 imported modules). Zero `sorry`."

EBC_SLOT_OLD = "`EBC_Classification` (v36) |"
EBC_SLOT_NEW = "`EBC_Classification`, `EBC_Classification_v2`, `EBC_Classification_v3` (v36) |"

OPEN_ROW_OLD = "| — | `prop:bands` (iii) — nothing larger, at `z₀ ≥ 1.1` | **open** | Needs the `z₀`-indexed pair-sum bound; `cor_hamming_m4` is stated at `z₀ = 1` and does not transfer. See `lean_audit_v36.md` §3 for the derivation |"
OPEN_ROW_NEW = "| — | `prop:bands` (iii) — nothing larger, at `z₀ ≥ 1.1` | **result clause** | `EBC_Classification_v3.far_pair_horizon_bound`: `\\|us\\| ≤ 10·(z₀ − 1)`, from `far_pair_sum_bound` (`EBC_Classification_v2`) — at `z₀ = 1.1` a distance-`≥2` pair survives at most one step |"

LADDER = """

### EBC — `prop:ladder` (analysed, not started)

`prop:ladder` (geometric ladder) states that the maximal conditional
kernel mass doubles with each probe:

```
z₀ = 1.0  :  1/16 → 1/8 → 1/4 → 1/2 → 1
z₀ ≥ 1.1  :  1/8  → 1/4 → 1/2 → 1   → 1
```

for zero through four probes. Its proof decomposes into three inputs:

1. **The antichain value formula** (companion P3 theory): the kernel
   value of a prior is the maximal survivable-set mass it charges, and
   survivability is hereditary downward, so for the uniform prior on a
   support `S` the value is `max{|A| : A ⊆ S, A survivable} / |S|`.
   Proved in the P3 slot — `P3_FreezeValue.VfamAdm_prune_eq` (v35) is
   the value-as-max-over-maximal-sets form on the corrected family.
2. **Heredity**: **proved here** in EBC terms —
   `EBC_Classification.survivesSet_mono`.
3. **`prop:bands`**: **proved** — the survivable subsets are singletons
   at the floor and Hamming-adjacent pairs above the edge.

With those, a `2^j`-cell subcube has value `1/2^j` at the edge and
`2/2^j` above it (capped at `1` when `j = 0`), which is the ladder.

**What is instance-level and therefore stays with the verifier:** the ten
numbers themselves, the 16 cells, the `2^j` subcube sizes, and the claim
that supports after `0…4` probes are subcubes with `j = 4,3,2,1,0`. The
paper itself says "the script recomputes all ten values by exhaustive
survivable-subset enumeration within each support".

**What remains to be formalized**, and it is a cross-paper bridge rather
than a new idea: connect the P3 value functional to EBC survivability
(the two slots currently use different notions of "survivable set" —
P3's is the class-restricted `SfamAdm` family, EBC's is the drift/floor
`survivesTo`), and model a probe as a restriction of the index set. That
bridge is the work; the mathematics on the EBC side is done.
"""

def patch(s, old, new, label):
    if old in s:
        s = s.replace(old, new, 1)
        print(f"ok   {label}")
    else:
        print(f"MISS {label}")
    return s

def main():
    s = io.open(SRC, encoding="utf-8").read()
    s = patch(s, TITLE_OLD, TITLE_NEW, "title v12 -> v13")
    s = patch(s, "Build went 48 → 55 jobs, 43 → 49 imported modules.",
              "Build went 48 → 55 jobs, 43 → 49 imported modules." + V13_NOTE,
              "v37 addendum note")
    s = patch(s, BUILD_OLD, BUILD_NEW, "build state 55 -> 57 jobs")
    s = patch(s, EBC_SLOT_OLD, EBC_SLOT_NEW, "ebc slot row")
    s = patch(s, OPEN_ROW_OLD, OPEN_ROW_NEW, "prop:bands (iii) open -> proved")
    s = s.rstrip("\n") + "\n" + LADDER
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
