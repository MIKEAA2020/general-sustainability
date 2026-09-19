# Archive manifest — v5 exhibit code

Companion to `supplementary_v5_additions.md` §S-E. Referenced by the article's Code availability
statement.

| Script | Produces | Reads | Deterministic? |
|---|---|---|---|
| `persistence_index_simulation.py` | the record-length table behind Proposition 32 (§8.1): mean, median and 90th percentile of the persistence index at `n = 10², 10³, 10⁴, 10⁵`, plus the implied stock drop | nothing (simulated inside the declared linear-trend class) | yes, seed 7 |
| `curvature_and_crossover.py` | the `κ` table for Proposition 27, the closed-form check `T = H_loc/(1−κ)`, the reserve-life crossover grid for Proposition 28 on the pinned record, and the three-law illustration of Proposition 26 | nothing (the reserves, production and growth figures are the ones tabulated in §8.2 and restated in the script) | yes, pure arithmetic |
| `certification_lp.py` | the compensation premium and the worst-concealed-deficit linear programme (Proposition 30) on a declared two-component box, the event-time witness of Proposition 31, and the certificate vectors of the three classified indicators | nothing | yes |

**Versions.** `python3 -V`, `numpy`, `scipy` as recorded at the head of `outputs.txt`.
`certification_lp.py` falls back to vertex enumeration if `scipy` is unavailable, and reports which
solver it used on each line.

**Outputs.** `outputs.txt` holds the complete stdout of a single run of all three scripts; the
figures quoted in `supplementary_v5_additions.md` §S-C are copied from it.

**Scope limits, stated so they cannot be over-read.** No script obtains data, contacts a network, or
re-derives any published table. The groundwater numbers are simulated series inside the class the
article declares for the anomaly index, not basin data; the phosphate numbers are arithmetic on the
vintage pinned in §8.2; the LP exhibit uses a declared box chosen to show computability, not any
public indicator's bounds. Nothing here supports a claim about any aquifer, fishery or deposit.
