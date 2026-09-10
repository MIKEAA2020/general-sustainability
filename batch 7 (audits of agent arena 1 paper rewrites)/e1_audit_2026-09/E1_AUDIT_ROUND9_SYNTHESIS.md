# E1 — Round-9 evaluation (deepseek retitling review) and joint synthesis

**Source:** `uploads/e1_audit_round9_retitling.txt` (94 lines)
**Basis:** v41, Ω_sim results, `E1_METHODS_FRAMING_ASSESSMENT.md`
**Date:** 10 Sep 2026

---

## Part 1 — Evaluation of the review

### 1.1 Verdict: agrees with my independent assessment, and adds three items I missed

The review and my own assessment (written before seeing it) reach the **same conclusion by
the same route**: retitling is "defensible but not yet warranted", the simulation is
"necessary, not sufficient", and the Edwards application is the missing second leg. That
convergence is worth stating, but it is not evidence — two analyses can share a blind spot.
What matters is where the review goes further.

| # | Review item | My prior assessment | Verdict |
|---|---|---|---|
| 1 | Simulation too narrow (T, σ, truth class) | same, in detail | **ACCEPT** |
| 2 | **No comparison to alternative rules** | **not raised** | **ACCEPT — genuine gap** |
| 3 | No second application | same | **ACCEPT** |
| 4 | **No identifiability pre-check** | **not raised** | **ACCEPT the aim, see §1.3** |
| 5 | Simulation reported as diagnostic, not integrated | implicit | **ACCEPT** |
| 6 | Formalise as algorithm/pseudocode | not raised | **ACCEPT — low cost** |
| 7 | "How to report" checklist | partially (Table 2b) | **ACCEPT as extension** |
| 8 | Power map as a figure | not raised | **ACCEPT — low cost** |

**Item 2 is the sharpest.** The paper never asks how its rule compares with AIC, BIC, MASE
alone, or a bare "beat persistence" rule. Without that, a reader cannot tell whether the
retention rule is a contribution or one arbitrary choice among many. Ω_sim already
generates everything needed to answer it — the per-replicate RMSE table is archived, so
alternative rules can be applied post hoc **with no refitting**. This is the single
cheapest high-value item in the review.

### 1.2 One correction to the review

The review says the information-set table "is a reporting template that other hindcast
evaluations could adopt" and lists a reporting checklist as a separate item 7. These are
the same item: Table 2b **is** the template, and what is missing is only the sentence
proposing it as one. Minor, but it inflates the apparent work remaining.

### 1.3 The identifiability pre-check: I tested it, and it does not work as proposed

The review calls this "the single highest-value addition" — turning the simulation's
finding into a protocol: *check identifiability first, apply the rule only where it has
power.* I agree that would be the strongest possible contribution, so I tried to build it.

**Candidate A — dispersion of module scores.** If the five modules score alike, the data
cannot distinguish them. Median coefficient of variation across modules, per cell, against
true-module power: **Spearman ρ = 0.524**. Too weak to license a protocol.

**Candidate B — margin of the best-scoring module over persistence.** Relative margin,
median per cell, against power: **Spearman ρ = 0.881, Pearson r = 0.942**. Strongly
predictive.

But Candidate B **fails as a pre-check on two independent grounds**:

1. **It is circular.** The margin is computed from the same out-of-sample scores the
   retention rule consumes. It cannot be evaluated *before* deciding whether to apply the
   rule, so it is a post-scoring interpretive statistic, not a gate.
2. **It misclassifies.** Applying a 5%-margin threshold as an APPLY / DO-NOT-APPLY rule:

| cell | margin | pre-check says | actual power |
|---|---|---|---|
| D1 σ=11.8 | +0.421 | APPLY | 0.965 ✓ |
| D1 σ=33.8 | +0.414 | APPLY | 0.985 ✓ |
| D2 σ=11.8 | +0.408 | APPLY | 0.710 ✓ |
| D2 σ=33.8 | +0.022 | DO NOT APPLY | 0.130 ✓ |
| **D3 σ=11.8** | **+0.126** | **APPLY** | **0.090 ✗** |
| **D3 σ=33.8** | **+0.187** | **APPLY** | **0.110 ✗** |
| D4 σ=11.8 | +0.019 | DO NOT APPLY | 0.005 ✓ |
| D4 σ=33.8 | −0.013 | DO NOT APPLY | 0.015 ✓ |

Six of eight correct, but **both D3 cells are false positives** — the diagnostic says
"apply" precisely where the true module wins less often than chance. That is the failure
mode a pre-check exists to catch, and it is the one it misses.

**Ruling: ACCEPT the objective, REJECT the claim that it is low-effort.** A working
pre-check must use training-window information only and must separate D3 from D1. Neither
of my two candidates does. The honest position is that Ω_sim has *identified* the
conditional-power problem without yet *solving* it, and the paper should say so rather
than propose a diagnostic that fails on its own simulation.

This is worth recording precisely because the review is right that it would be the highest
value item. It is high value *and* high difficulty, which is not what the review claims.

---

## Part 2 — Joint synthesis and plan

### 2.1 Where the three assessments converge

Round 8 (reframing), my methods-framing assessment, and round 9 all agree:

- The title should stay locked **for now**.
- The simulation is necessary but not sufficient.
- The Edwards companion is the decisive missing piece.
- The paper as it stands is honest and publishable as a case study with a pre-registered
  validation of its decision rule.

I take that as settled and will not relitigate it.

### 2.2 What each adds that the others do not

| Source | Unique contribution |
|---|---|
| Round 8 | The supplied-catch inversion (implemented, v38) |
| My assessment | Edwards runs the **same rule**, and its M1 case shows the tie band deciding a real retention (implemented, v41) |
| Round 9 | **Rule comparison** (item 2) and the **pre-check** aim (item 4) |

### 2.3 Plan, ordered by value per unit risk

**Tier A — implement now, no new simulation, no spec change**

| | Action | Basis |
|---|---|---|
| **A1** | **Rule comparison from archived output.** Apply AIC-style, MASE-only, bare "beat persistence", and 0%/10% tie-band variants to the existing per-replicate table. Report power and specificity for each against the retention rule. No refitting: the RMSE table is archived. | round 9 item 2 |
| **A2** | **Power map figure.** Heatmap of power by DGP × σ with the pre-declared thresholds marked. | round 9 item 8 |
| **A3** | **Algorithm box.** Pseudocode for the rule, including the H1/H2/H3 gates and the tie band. | round 9 item 6 |
| **A4** | **One sentence** proposing Table 2b as a reporting template. | round 9 items 5, 7 |
| **A5** | **State the pre-check as an open problem**, with the two failed candidates and the D3 counterexample, rather than proposing a diagnostic that does not work. | §1.3 above |

**Tier B — requires new computation under the existing pre-registration**

| | Action | Note |
|---|---|---|
| **B1** | Misspecified-truth DGP | Already declared in `SPECIFICATION_v4.md` §2b as a deferred extension, so it needs no new sheet — only execution and a recorded replicate count. |
| **B2** | `T = 71` extension | Same. |
| **B3** | Tie-band and horizon sensitivity | Cheap: no refitting, applied post hoc to the archived table. Fold into A1. |

**Tier C — the actual gate on retitling**

| | Action |
|---|---|
| **C1** | Coordinate the Edwards application into a shared framework statement. |
| **C2** | Only after A, B and C1: reconsider the title, with two applications, a two-sided power bound, and a rule comparison behind it. |

### 2.4 What I recommend against

- **Retitling before Tier B.** Three independent reviews now say the same thing.
- **Proposing the margin diagnostic as a pre-check.** It fails on D3 (§1.3). Publishing it
  would be exactly the pattern this project has corrected repeatedly: asserting a result
  the evidence does not support.
- **Merging E1 and E3.** Both are complete with Zenodo DOIs; the cross-system contribution
  belongs in a third paper citing both.

### 2.5 Immediate next step

Tier A in one pass: A1 is the highest-value item in the entire round and costs no new
simulation, because every rule variant can be evaluated on the archived per-replicate
scores. A5 converts a failed attempt into a stated open problem, which is a contribution in
a methods context and an honest disclosure in any context.
