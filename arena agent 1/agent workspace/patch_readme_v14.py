#!/usr/bin/env python3
"""lean_README_v13.md -> lean_README_v14.md

v38: prop:ladder completed by substitution; the DetMDP instantiation
question resolved by the paper's wording; build 57 -> 59 jobs,
51 -> 53 modules. Targeted substitutions; each prints ok/MISS.
"""
import io, os

SRC = "/home/user/lean_README_v13.md"
DST = "/home/user/lean_README_v14.md"

TITLE_OLD = "### v13 — result-level index"
TITLE_NEW = "### v14 — result-level index"

BUILD_OLD = "`lake build` → **rc = 0, 57 jobs** (51 imported modules). Zero `sorry`."
BUILD_NEW = "`lake build` → **rc = 0, 59 jobs** (53 imported modules). Zero `sorry`."

NOTE_ANCHOR = "Build went 55 → 57 jobs, 49 → 51 modules."
NOTE_NEW = NOTE_ANCHOR + """

> **v38 addendum.** `prop:ladder` is complete on the EBC side, and the
> `DetMDP` question is settled by the paper's own wording rather than
> left open. Two corrections to earlier statements in this index:
>
> * `prop:bands` **closed at `2bf7d4b`** — all four clauses. It is not
>   an open item, and the shared arithmetic helper (`RatArith`) that made
>   its clauses cheap was built several pushes earlier.
> * The `prop:ladder` section below, headed "analysed, not started", is
>   now out of date: the EBC half landed in `EBC_Ladder` and
>   `EBC_Ladder_v2`.
>
> Build went 57 → 59 jobs, 51 → 53 modules."""

EBC_SLOT_OLD = "`EBC_Classification_v3` (v36) |"
EBC_SLOT_NEW = "`EBC_Classification_v3` (v36); `EBC_Ladder`, `EBC_Ladder_v2` (v37) |"

LADDER_STATUS = """

### `prop:ladder` — status (v38)

**Complete on the EBC side.** `EBC_Ladder` fixed the shape — set
survivability as `survivesSetAt`, one in-alphabet policy of `L` actions
keeping every member at or above the floor, which is P3's
`SurvivableAdm M S k` verbatim — and `EBC_Ladder_v2` completed the
cardinality facts the value formula consumes:

| fact | theorem |
|---|---|
| heredity of survivability | `EBC_Ladder.survivesSetAt_mono` |
| at the floor, all members agree on `I`, so `M = 1` | `EBC_Ladder.floor_survivable_all_agree` |
| above the edge, every pair is Hamming-adjacent, so `M ≤ 2` | `EBC_Ladder.pairs_adjacent_above` |
| no three pairwise-distinct survivors above the edge | `EBC_Ladder_v2.no_three_distinct_above` |
| a surviving subset is a singleton or an adjacent pair | `EBC_Ladder_v2.survivor_is_singleton_or_adjacent_pair` |
| `M = 2` is attained | `EBC_Ladder.adjacent_pair_survives` |
| a subcube with a free coordinate contains an adjacent pair | `EBC_Ladder.subcube_adjacent_pair` |
| a probe, modelled as a restriction of the index set | `EBC_Ladder.inSubcube`, `flip` |

With the value `= M/|S|`, that is `1/|S|` at the edge and
`min(1, 2/|S|)` above it — the paper's two rows, `|S|` symbolic.

**The `DetMDP` instantiation is not being done, and here is why.** The
decision rule is the paper's claim: type-identity ("is an instance of")
would require it, shape-equivalence ("has the same value form") would
not. `prop:ladder`'s proof reads *"The companion theory's antichain
formula **makes** the kernel value of a prior the maximal survivable-set
mass it charges…"* — it **applies** the companion formula, and never
asserts the ladder *is* an instance of `VfamAdm`. So the formalization
target is shape-equivalence, and building a `DetMDP` over the sixteen
cells whose `survK` is EBC's `survivesTo` would add mechanism without
adding a theorem. The bridge is recorded as **structural**. If a future
edition of the paper claims type-identity, revisit this.
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
    s = patch(s, TITLE_OLD, TITLE_NEW, "title v13 -> v14")
    s = patch(s, BUILD_OLD, BUILD_NEW, "build state 57 -> 59 jobs")
    s = patch(s, NOTE_ANCHOR, NOTE_NEW, "v38 addendum + corrections")
    s = patch(s, EBC_SLOT_OLD, EBC_SLOT_NEW, "ebc slot row")
    s = s.rstrip("\n") + "\n" + LADDER_STATUS
    io.open(DST, "w", encoding="utf-8").write(s)
    print(f"wrote {DST}: {len(s.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
