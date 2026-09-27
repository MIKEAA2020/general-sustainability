# Lean audit v35 — the `E1` slot: decision record

**Branch:** `lean-audit-v4` (additive). **Toolchain:** `v4.34.1`.
**Build at time of writing:** rc = 0, **46 jobs**, 42 imported modules.

## The question

Item (4) of four. v14 found `E1_ForecastLadder` carries failure modes
**A** (alias) and **C** (vacuous target: *"the paper contains no numbered
environments at all, so the index entry refers to nothing"*). I said a
decision was needed because there is nothing numbered to formalize
against. This record settles what the decision actually is — **the
situation is worse than mode C, and that changes the options.**

---

## 1. Confirmed: no numbered environments

```
grep -c 'begin{\(proposition\|lemma\|theorem\|corollary\)}'
  paperE1_cod_forecast_ladder_v59.tex   →   0
```

## 2. New finding: the module's paper references are invented

The paper is an **empirical forecasting study**:

> "The instrument is a forward-ordered ladder of surplus-production models
> (not a strict nesting for M2 and M4) evaluated against two naive
> baselines. It runs output-only, stock-and-flow, residual, then lagged
> initialisation" (l.182–185)

— a ladder of *statistical models scored on NAFO 2J3KL cod data*, not a
mathematical object with an identity to prove.

`E1_ForecastLadder.lean` (93 lines, 5 theorems) claims otherwise:

| Theorem | Body | Its "Paper reference" |
|---|---|---|
| `ladder_telescope` | `sumRange_telescope f N` — **one-line alias** | "the level margins of the calibrated ladder telescope to the total change; **every level of the paper's construction instantiates this identity**" |
| `ladder_bound_upper` | `sumRange_le_sumRange' …` — **one-line alias** | "Per-level bounds aggregate" |
| `ladder_bound_lower` | `sumRange_le_sumRange' …` — **one-line alias** | "Per-level floors aggregate" |
| `ladder_bracket` | `⟨ladder_bound_lower …, ladder_bound_upper …⟩` | "the ladder's **calibrated-margin bracketing**, the bookkeeping identity behind the record's **margin accounting**" |
| `ladder_ascent` | **the only real proof** (3-line induction) | "the **calibrated-margin monotonicity** the applied readings consume" |

The objects named in those references do not exist in the paper:

```
grep -ci 'telescope'      paperE1_cod_forecast_ladder_v59.tex  →  0
grep -ci 'level margin'   paperE1_cod_forecast_ladder_v59.tex  →  0
grep -ci 'forward margin' paperE1_cod_forecast_ladder_v59.tex  →  0
```

So the slot is not "machinery aimed at a paper with no numbered results"
— it is **generic finite-sum lemmas wearing a fabricated paper
reference**, four of the five being one-line aliases of `Prelude`
lemmas that already existed. This is the third instance of a docstring
outrunning its theorem (v34 found v18's `prop_freeze_drop_count`
claiming `2^{|supp b|}` while proving `2^{|univX|}`), and the first where
the *paper reference itself* is the fabrication.

## 3. The decision, and the options

Waiting for the paper to acquire numbered environments is **not** a real
option: it is an empirical scoring paper and will not grow a theorem.

| Option | What it does | Cost |
|---|---|---|
| **A. Relabel and keep** | Index the slot as *"machinery: 5 generic `sumRange` lemmas, 4 aliases, 1 induction; **no target — the paper has zero numbered environments and the stated paper references do not exist**"*. Code untouched. | ~0 |
| **B. Relocate the one genuine lemma** | `ladder_ascent` is the only theorem with content. Move it (and only it) under an honest name into `Prelude`'s sums section; leave the four aliases in place as deprecated. | small, touches `Prelude` |
| **C. Dissolve the slot** | Drop `E1_ForecastLadder` from `Formalizations.lean`, leaving it as unimported legacy like the ~325 KB of `P1_AssessmentSeparation`. The index entry becomes "`E1`: no formalizable target." | small, removes 4 aliases |
| **D. Retarget** | Find a formalizable claim in the paper's prose and build against it. | **not recommended** — with no numbered environments this means inventing a target, which is how the current defect arose |

**Recommendation: A now, then B.** A costs nothing and stops the index
from asserting a coverage relation that does not exist. B preserves the
one thing of value (`ladder_ascent`) under a name that does not claim a
paper connection. C is defensible but destroys a working import for
cosmetic gain.

## 4. What this does not affect

- `E1_ForecastLadder` builds green and is imported; nothing in this
  record breaks the build.
- The finding is about **provenance and labelling**, not correctness: all
  five theorems are true.
- No other slot is implicated. The other eight slots were checked against
  their papers' numbered environments; E1 is the only one with none.

## 5. Files

Read, not modified: `paperE1_cod_forecast_ladder_v59.tex`;
`lean/Formalizations/E1_ForecastLadder.lean` (93 lines).
