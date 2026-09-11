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
| **B1** | Misspecified-truth DGP | **Correction to an earlier draft of this synthesis, which said §2b already covered this. It does not.** §2b declares only `T = 71`, `σ = 0` and `𝔰 ∈ {5, 30}` — all still members of the ladder's class. A truth *outside* the class is a new design element and requires an amendment to `SPECIFICATION_v4.md`, dated and committed before execution. A feasibility test also shows the obvious candidate needs care: a regime switch from the collapse to the recovery parameterisation drives the series to the numerical floor within four steps, so it would measure floor behaviour rather than power. A misspecified DGP must be calibrated to stay inside the observed biomass range. |
| **B2** | `T = 71` extension | Covered by §2b; execution and a recorded replicate count only. |
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

---

## Part 3 — Revisiting this synthesis: what it got wrong and how it improves

Re-examined against v43. Two defects in the synthesis itself, and four structural
improvements.

### 3.1 Errors found on re-reading

**E-1. Tier A was reported as "done now"; three of its five items were not implemented.**
Checking v42 directly rather than trusting the plan: A1 (rule comparison) and A5 (pre-check
as open problem) were in; **A2 (power map), A3 (algorithm box) and A4 (reporting template)
were not.** A plan that marks a tier complete when 40% of it shipped is a plan that will
lose items. All three are now implemented in v43.

**E-2. B1 was wrongly described as already pre-registered.** The synthesis said a
misspecified-truth DGP "needs no new sheet — already declared in §2b". It is not: §2b
declares `T = 71`, `σ = 0` and `𝔰 ∈ {5, 30}`, every one of which is still a member of the
ladder's class. A truth outside the class is a **new design element** and needs a dated
amendment before execution. Corrected in §2.3 above.

A feasibility test made the point sharper. The obvious misspecified candidate — a regime
switch from collapse to recovery parameters — drives the series to the numerical floor
within four steps (900 → 888 → … → 305 → 77 → 0). It would measure floor behaviour, not
power. Any misspecified DGP must be calibrated to remain inside the observed biomass
range, which is design work, not just execution.

### 3.2 How the synthesis improves as an instrument

**I-1. Verify tier completion against the artefact, not the plan.** E-1 arose because I
checked my own record rather than the manuscript. The rule already adopted for audit items
after round 5 — verify by grep against the compiled source — applies to plans as well.

**I-2. Distinguish "declared" from "declared *and covering this case*".** E-2 arose from
matching on the word "deferred" rather than reading what was deferred. A pre-registration
is only a defence for the elements it actually names.

**I-3. Feasibility-test Tier B items before ranking them.** The misspecified DGP was ranked
"highest value, low effort" by the reviewer and carried into my plan at that rating. Five
minutes of simulation showed the naive version is degenerate. Effort estimates for
unexecuted work should be checked with a smoke test before they enter a plan.

**I-4. The plan needs an explicit stopping condition.** Nine rounds have each produced a
new tier. Absent a stated endpoint this continues indefinitely. The endpoint implied by
the whole sequence, and now stated: **E1 is complete as a case study with a pre-registered,
validated decision rule.** Everything remaining — misspecified truth, `T = 71`, the Edwards
coordination, retitling — belongs to a *successor* framework paper, not to E1. The
appropriate next action on E1 itself is submission, not another tier.

### 3.3 Current state of the plan

| Tier | Item | Status |
|---|---|---|
| A1 | Rule comparison from archived replicates | **v42 partial, completed v44** — see §3.4 |
| A2 | Power map figure | **done, v43** |
| A3 | Algorithm box | **done, v43** |
| A4 | Table 2b proposed as a reporting template | **done, v43** |
| A5 | Pre-check stated as an open problem | **done, v42** |
| B1 | Misspecified-truth DGP | **blocked**: needs a v4 amendment and a non-degenerate design |
| B2 | `T = 71` | ready; covered by §2b |
| B3 | Tie-band / horizon sensitivity | **absorbed into A1** |
| C1 | Edwards coordination | open; the real gate on retitling |
| C2 | Retitle | not before B1, B2, C1 |

**Tier A is now genuinely complete.** Tier B and C belong to the successor paper.


### 3.4 A third error, found on the same re-check

**E-3. A1 shipped two of the four comparators it promised.** The plan specified "AIC-based
selection, MASE alone, a bare beat-persistence rule, and 0%/10% tie-band variants". v42
delivered the tie-band variants and beat-persistence; **the AIC and MASE comparators were
never computed.** A grep for "MASE" appeared to pass only because the term occurs in the
introduction's literature discussion — a false positive from checking the whole document
rather than the table.

Both are now computed on the same archived replicates and added in v44:

| rule | power | specificity |
|---|---|---|
| adopted retention rule | 0.376 | 0.978 |
| MASE < 1 against the naive benchmark | 0.651 | **0.675** |
| information criterion, `n·log MSE + 2k` | **0.509** | **0.992** |

**This is the most consequential finding of the whole comparison, and it is unfavourable
to the paper's own rule.** An information criterion penalising free parameters dominates
the adopted rule on *both* axes — more power and better specificity. MASE alone buys power
by surrendering specificity, retaining structure in a third of persistence-true replicates.

The manuscript now states this plainly: the comparison does not vindicate the rule used
here, and a reader selecting an instrument for new work should prefer the parameter-
penalising criterion. The rule stands as the pre-registered instrument that produced the
empirical result, not as a recommendation.

**Method lesson (extends I-1).** Verifying by grep over the *document* is not the same as
verifying over the *object that was supposed to change*. E-3 survived a check that E-1 was
designed to catch, because the search space was too wide. Checks must be scoped to the
table, section or figure the item promised to alter.
