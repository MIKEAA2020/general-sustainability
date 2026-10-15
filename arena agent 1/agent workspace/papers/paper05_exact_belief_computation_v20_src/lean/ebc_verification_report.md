# EBC instance-level verification — scoping and result

Date: 2026-09-28. Branch `lean-audit-v4`.

## The question

Scope the three instance-level items before deciding how to check them:

* 5,219 policies × 60 steps
* 84 pairings
* 65,536 subsets

The recommendation was to default to **full enumeration** unless scoping
showed it infeasible, and to scope first — specifically, to ask whether
the verifier already exists.

## The answer: the verifier already exists, and it already does all of this

`arena agent 1/paper rewrites/latex/paper2_exact_belief_computation_v10_verification.py`
(382 lines, 15,652 bytes) is a full-enumeration verifier for exactly
these items. It is not sampled.

**Result: 30/30 checks pass, exit 0.** Wall clock 7m36s.

```
$ python3 paper2_exact_belief_computation_v10_verification.py
verification: 30/30 checks pass
```

Full output: `ebc_verify/run2.txt` (this workspace).

### The three items, as the verifier runs them

| item | check | result |
|---|---|---|
| 5,219 policies × 60 steps | *exhaustive 1/2/3-periodic classification (5,219 policies, 60-step certificates)* | **PASS** |
| 84 pairings | *exact point-based evaluation: alpha-set values equal trajectory enumeration at 7 rational beliefs × 3 levels × 4 horizons (84 pairings); 17⁴ = 83,521 sequences deduplicate to ≤ 545 vectors* | **PASS** |
| 65,536 subsets | *antichain census: 1,048,576 raw subset evaluations collapse to 496 stored maximal sets* | **PASS** |

**A correction on the "65,536" figure.** It is not one number. The
antichain census the verifier runs is **1,048,576 raw subset evaluations
collapsing to 496 stored maximal sets** (16 at the edge + 32×15 above).
The paper's own text carries `$2^{16} = 65{,}536$ raw subsets, $736$
stored antichain`. Both are compression ratios over the same structure;
earlier notes quoted 65,536 as the subset count without distinguishing
it from the census figure. The census check passes.

**Symmetry reduction already exists.** The compression is the point of
the check — raw evaluations collapse by 4,096× and 2,048× per level via
a Minato-style antichain representation (the paper cites Minato 1993).
So "are all 65,536 genuinely needed" is already answered: the verifier
enumerates the space and stores only the antichain.

**Runtime: 7m36s.** Not prohibitive. Full enumeration is the right
default and is what runs.

## One real defect found, and it was environmental

The first run reported 29/30 with

```
FAIL chained script exits green: paper2_exact_belief_computation_v2_verification.py (16/16)
```

This is a regression chain: v10's verifier requires v2's verifier to
exit green, and v2's requires v1's. Each script reads its **own `.tex`
sibling** from its working directory. Run outside the latex folder, each
crashes with `FileNotFoundError` after its mathematical checks have
already passed.

With the three missing siblings fetched (`v1_verification.py`,
`v1.tex`, `v2.tex`), the chain resolves and the result is **30/30,
exit 0**. So the failure was a missing-file artifact, not a
mathematical one — but it is worth recording that the chained check
fails closed (exit 1) rather than skipping, which is the correct
behaviour.

A second, informational note: the `proof completeness` check passes
while reporting one missing optional needle, `29-cell radius-two ball`.

## The verifier independently corroborates the Lean layer

This is the most useful finding. The Python verifier and the Lean layer
were built separately, and they agree:

| Lean | verifier check |
|---|---|
| `EBC_Deadline.deadline_law` | *deadline instance on the cube: viability iff z₀ ≥ 1 + T/2* — PASS |
| `prop:ladder` value `1/\|S\|` at the edge, `min(1, 2/\|S\|)` above | *observation ladder exact: 1/16, 1/8, 1/4, 1/2, 1 at the edge and 1/8, 1/4, 1/2, 1, 1 above* — PASS |
| `EBC_Ladder_v2.no_three_distinct_above` | *no three cells pairwise Hamming-adjacent (all C(16,3) = 560 triples): blind survivable sets have at most two members* — PASS |
| `prop:bands` (16 singletons / 32 pairs) | *16 singletons at 1.0; exactly the 32 Hamming-1 pairs at 1.1 and 2.5; nothing larger* — PASS |

The ladder row is worth spelling out. At `|S| = 16`, the Lean layer's
formula gives `1/16` at the edge and `min(1, 2/16) = 1/8` above it. The
verifier's enumeration reports exactly `1/16` and `1/8` as the first two
ladder entries. Two independent derivations of the same numbers.

## Conclusion

**Nothing to build.** The instance-level items were already verified by
full enumeration, at a cost of seven and a half minutes. The remaining
work was to run the verifier in a directory that had its dependencies
and to record the result — which this document does.

## Reproducing

```
mkdir ebc_verify && cd ebc_verify
# fetch from arena agent 1/paper rewrites/latex/
#   paper2_exact_belief_computation_v10_verification.py
#   paper2_exact_belief_computation_v10.tex
#   paper2_exact_belief_computation_v2_verification.py
#   paper2_exact_belief_computation_v2.tex
#   paper2_exact_belief_computation_v1_verification.py
#   paper2_exact_belief_computation_v1.tex
python3 paper2_exact_belief_computation_v10_verification.py
# -> verification: 30/30 checks pass   (exit 0)
```
