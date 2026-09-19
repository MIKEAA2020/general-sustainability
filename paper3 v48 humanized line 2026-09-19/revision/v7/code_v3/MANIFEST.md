# Exhibit bundle

Scripts that generate every computed figure in "Typed Flux Ledgers and Depletion Arithmetic" and in its
supplementary, and the record of one run of them. Referenced by the article's Code availability
statement and described in Section 8 of the companion certification procedure.

## Running it

```
python3 code/certification_lp.py
python3 code/curvature_and_crossover.py
python3 code/persistence_index_simulation.py
```

from the top of the deposit, with the `code/` directory present. No script takes an argument, reads a
file, opens a network connection or writes anything. `outputs.txt` is the complete stdout of one run of
all three, in that order, under Python 3.13.14 with numpy 2.3.5 and scipy 1.17.1.

## Files

| file | size | sha256 |
|---|---|---|
| `certification_lp.py` | 5,048 B | `50ab318c6ebd65020e5eca251d93ebe0db9a046b51e2142b9941f4a4f4b32a63` |
| `curvature_and_crossover.py` | 3,281 B | `440b61c0fa0a939d8c4481801c80a67751e152025ed523ec8199b098f326395a` |
| `persistence_index_simulation.py` | 2,225 B | `8e3b5d873df79f399939a2a499b04ef6d5bf456ec5b1a27c94d3fb1e85ad95ed` |
| `outputs.txt` | 5,388 B | `a9dd0cf70019d409e0e2c366272ebfcd0cfd690b94f60e435f0d59ff2ca0e130` |

## What each script does, and what it reads

| script | exhibits it produces | inputs | external data |
|---|---|---|---|
| `certification_lp.py` | the compensation premium and the worst-concealed-deficit linear programme (Section 10.1, supplementary S8), and the certificate vector of Section 3.1 for the three indicators classified in Section 8 | the bounds and splits declared in the article and the supplementary | none, arithmetic on declared figures |
| `curvature_and_crossover.py` | the curvature table for Proposition 27, the closed-form check `T = H_loc/(1−κ)`, the reserve-life crossover grid for Proposition 28 on the pinned record, and the three-law illustration of Proposition 26 | the reserves, production and growth figures tabulated in Section 6.5.2 and restated in the script | none |
| `persistence_index_simulation.py` | the boundedness of the persistence index on the declared linear-trend class (Section 6.5.1) | the class declared in the article, with the seed printed in the record | none, the series are simulated |

## Scope limits, stated so they cannot be over-read

No script obtains data, contacts a network, or re-derives any published statistic. The G3P basin rows
whose provenance is recorded in the supplementary (S5.4) are quarantined and no script consumes them, so
nothing in these exhibits depends on them. Figures quoted from the article are inputs here, not
outputs: a script recomputes what the article computes from those inputs and prints the comparison.
The recomputation of the aggregate overshoot date, which does read downloaded tables, is held apart in
the analysis record `analysis/nfa_tau/` for exactly that reason; its manifest states its own limits.

## Licence

The scripts are released under the CC BY 4.0 licence of the article they accompany. Attribution: as the
article's citation. No third-party data is included in this directory.
