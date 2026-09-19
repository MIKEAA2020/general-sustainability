# Archive manifest — exhibit bundle, v2

Companion to the main text `revision/v7/paper3_material_ledgers_v39.md` (LaTeX twin `.tex`, 55 pp.) and to
`revision/v7/paper3_supplementary_v10.md`, S8 and S9.3. Referenced by the article's Code availability
statement and described in Companion A, `revision/v7/companionA_certification_procedure_v1.md`, Section 8.

This is version 2 of the bundle first shipped at `revision/v5/code/`. **The numbers are unchanged.** Only the
printed loci moved, because the article renumbered between v5 and v39, and a printed label that no longer
resolves is a defect in a reproduction bundle. Nothing in `revision/v5/code/` was modified: the older deposit
still reproduces what it printed.

## The relabelling, in full

| v5 printed | v2 prints | why |
|---|---|---|
| `Section 7.1 exhibit` | `Section 10.1 and supplementary S8 exhibit` | the premium and the concealed-deficit programme are in main-text Section 10.1, with the recipes in the supplementary's S8 |
| `(S8.1)`, `(S8.2)`, `(S8.3)` | `(main text 6.5.1)`, `(main text 6.5.2)`, `(main text 6.5.3)` | the three classified indicators are main-text subsections; the supplementary's S8 is the LP recipes, not the classifications |
| `Section 8.1 exhibit` | `Section 6.5.1 exhibit` | the persistence index moved out of Section 8 (now: domain templates) into Section 6.5 |
| `python3 revision/v5/code/…` | `python3 revision/v7/code/…` | bundle location |

`make_bundle_v2.py` performs the substitution mechanically, re-runs all three scripts, writes `outputs.txt`, and
exits non-zero unless (i) the expected values are present in the fresh output and (ii) no stale loci string
survives in any script. The two checks that matter for a relabelling commit.

## The three scripts

| Script | Produces | Reads | Deterministic? |
|---|---|---|---|
| `persistence_index_simulation.py` | the record-length table behind Proposition 32 (§6.5.1): mean, median and 90th percentile of the persistence index at `n = 10², 10³, 10⁴, 10⁵`, plus the implied stock drop | nothing (simulated inside the declared linear-trend class) | yes, seed 7 |
| `curvature_and_crossover.py` | the `κ` table for Proposition 27, the closed-form check `T = H_loc/(1−κ)`, the reserve-life crossover grid for Proposition 28 on the pinned record, and the three-law illustration of Proposition 26 | nothing (the reserves, production and growth figures are the ones tabulated in §6.5.2 and restated in the script) | yes, pure arithmetic |
| `certification_lp.py` | the compensation premium and the worst-concealed-deficit linear programme (Proposition 30) on a declared two-component box, the event-time witness of Proposition 31, and the certificate vectors of the three classified indicators | nothing | yes |

Run all three from this directory, or one at a time:

```
python3 certification_lp.py
python3 curvature_and_crossover.py
python3 persistence_index_simulation.py
```

**Versions and runtime.** Python 3.13.14, numpy 2.3.5, scipy 1.17.1 (recorded at the head of `outputs.txt`); the
three scripts together run in under ten seconds. `certification_lp.py` falls back to vertex enumeration when no
solver is importable and prints which route produced each line; that fallback is exact and exponential in the
component count, so it is a convenience for small instances, not a solver.

**Outputs.** `outputs.txt` holds the complete stdout of a single run of all three scripts, in the order listed
above. The figures quoted in the main text and in the supplementary's S8 are copied from it.

**Scope limits, stated so they cannot be over-read.** No script obtains data, contacts a network, or re-derives
any published table. The groundwater numbers are simulated series inside the class the article declares for the
anomaly index, not basin data; the phosphate numbers are arithmetic on the vintage pinned in §6.5.2; the LP
exhibit uses a declared box chosen to show computability, not any public indicator's bounds. Nothing here
supports a claim about any aquifer, fishery or deposit. The G3P basin rows discussed in §6.5.2 are quarantined
in the article and their provenance is recorded in the supplementary's S5.4; no script consumes them.
