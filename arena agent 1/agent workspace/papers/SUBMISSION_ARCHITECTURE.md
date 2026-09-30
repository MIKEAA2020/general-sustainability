# Submission architecture — RATIFIED 2026-09-30

**Status: RATIFIED.** Eleven units. Derived, not invented: venues from
`FAMILY_CONSOLIDATION_PLAN.md` §1.1 and `FAMILY_PAPER_COUNT.md`'s revised ten; grouping by
**claim**, not content affinity and not paper count.

**Venue is secondary.** The target is preprints.org, with one preprint mapping to one eventual
journal submission. The venue column records the intended destination; it is not the reason any
unit is constituted. The partition stands on the claim structure and the fold rule, both of
which are venue-independent. Nothing below changes if a venue is retargeted.

**Two amendments made at ratification:** unit 11 stands alone at Systems & Control Letters
(eleven units, not ten); and the bar verdicts on units 2–5 were re-verified rather than
inferred — see §"Verification of the prior-art inference".
 Derived, not invented: the venues come from
`FAMILY_CONSOLIDATION_PLAN.md` §1.1 (the eight venue-assigned papers) and
`FAMILY_PAPER_COUNT.md` §"the revised ten". The grouping is by **claim**, as directed, not by
content affinity and not by paper count.

**This draft supersedes my seven-way merge partition.** Six of my seven merges were wrong,
and the reason is diagnostic: I grouped by *content affinity* ("do these support a broader
claim together?") when the driver should have been *submission unit* ("which papers constitute
one journal submission?"). The recorded strategy already answers that question, and it answers
it differently.

---

## The draft

| # | Unit | Papers (source) | The single claim it makes | Venue | Words | Thm | Cost of folding |
|---|---|---|---|---|---|---|---|
| 1 | Obstruction calculus | `paper01` | No observation-based policy can keep a system viable, and there is a finite, checkable, exact certificate that proves it | **Automatica**, Regular | 23,428 | 21 | — (anchor) |
| 2 | Probabilistic sufficiency | `paper02` | The calculus carries to belief states with no loss of exactness: value-one level ≡ viable-set recursion; α-vectors are exactly the indicators of maximal jointly survivable subsets, an antichain | **IEEE TAC**, Full | 13,632 | 18 | **loses a TAC submission** |
| 3 | Computational certification | `paper03` | Nonviability is certifiable by a finite LP covering every measurable information-adapted control, with a certified two-sided bound | **SIAM J. Optimization** | 13,629 | 7 | **loses a SIOPT submission** |
| 4 | Minimax dual certificates | `paper04` | The common-action obstruction is dual to an adversarial measure on ≤ k+1 points (tight); Farkas and Isaacs are specialisations | **Mathematics of OR** | 8,566 | 13 | **loses a MoOR submission** |
| 5 | Exact belief computation | `paper05` | The exact discipline survives the curse of dimensionality: antichain + pairwise bound collapse 68.7 bn evaluations to 1,552 — and the bound's failure at m=5 is the sharper news | **Automatica**, Tech. Communiqué | 6,435 | 9 | **loses a Tech. Communiqué** |
| 6 | Quantifier-order separation | `paper06` | Compensatory and noncompensatory feasibility are related by a quantifier commutation that fails on an **open region**; the acceptance gap is the part of the convex hull no single plan dominates | **Math. OR / SIOPT** | 29,071 | 0 | **loses a venue** |
| 7 | The decision clock | `paper07` + `paper08` | Institutional latency — not ecology — decides whether governance stabilises or destabilises a resource, **and how that latency is represented changes the computed answer** | preprints first | 47,923 | 16 | negative — **the one merge the evidence supports** |
| 8 | Certified horizons on a real record | `paper09` + `paper09b` | Reference points can be defended by certification rather than simulation, and that certification has a horizon set by the map, not the method | **CJFAS** | 23,766 | 14 | ARV is thin alone (7,056 w) — folding is right |
| 9 | What depletion numbers can certify | `paper10` + `paper10b` | Depletion time is three mutually non-interchangeable quantities; what a typed ledger can certify is delimited by its typing | **Ecological Economics** | 44,338 | 0 | E4 is thin alone (9,326 w) — folding is right |
| 10 | Forecasting baselines and the null | `paper11` + `paper11b` | Process-based models are not self-justifying: at the annual origin they do not beat persistence, and the failure is diagnostic of the driver's spectrum | **Int. J. Forecasting** | 30,401 | 0 | E3 is thin alone (9,637 w) — folding is right |
| 11 | Exact audits of worked systems | `paper11c` | Each mechanism of the obstruction calculus acquires a count, a witness and a boundary on worked systems | **Systems & Control Letters** (see dispute below) | 11,123 | 14 | **contested — see below** |

**Eleven units, not ten.** Unit 11 is the one addition, for a reason given below.

---

## Fold-or-separate, per case

### Units 1–5: separate. All five.

This reverses my `1+2` and `3+4` merges, and it reverses the plan's §3 disposition of
`minimax → obstr` and `ebc → comp`.

**The dispositive evidence already exists** (`FAMILY_PAPER_COUNT.md` §0). A sentence-level
overlap test across the five P2 manuscripts found them essentially disjoint:

| pair | shared sentences | overlap of smaller |
|---|---|---|
| obstr ↔ psuff / comp / ebc | 0 | **0.0%** |
| obstr ↔ minimax | 1 | 0.7% |
| psuff ↔ comp / ebc | 4 / 3 | 1.9% / 3.4% |
| comp ↔ ebc | 4 | 4.5% |

*With no duplication to remove, folding removes nothing and buries an independent result.*
Unit 4 at 8,566 w with 13 theorems is a legitimate MoOR research article. Unit 5 at 6,435 w
with 9 theorems is right for the short format it was already assigned.

**The "below bar" verdicts on 2, 3, 4 and 5 are prior-art verdicts, and folding cannot fix
them.** This is the crux. The bar assessment calls them "blocked" or "below bar" — but the
stated reason in every case is that they state no prior-art position. I measured it:

| unit | prior-art section | words of prior art |
|---|---|---|
| 1 | real prose | 951 |
| **2** | **stub** | — |
| **3** | **stub** | — |
| **4** | **stub** | — |
| **5** | **stub** | — |
| 6 | stub | — |
| 7a/7b | real prose | 518 / 652 |
| 8a/8b | real prose | 608 / 647 |
| 9a/9b | real prose | 531 / 590 |
| 10a/10b/10c | real prose | 532 / 438 / 405 |

**This is the argument that settles the question.** Folding `paper02` into `paper01` produces a
larger paper that *still has no prior-art section*. Folding is not merely costly — it is the
wrong instrument for the defect that is actually present. The block is removable by writing,
at a cost of roughly 600–950 words per paper, which is what units 1 and 7–10 already have.

**Recommendation: separate 1–5; write four prior-art sections.** Cost of folding would be four
venues surrendered to purchase nothing.

### Unit 6: separate — but its prior art is a research task, not a writing task

The bar assessment flags unit 6 as the **highest novelty risk**: the separation result *sits
close to known robust-optimisation and MCDM separation results*, and the plan records that it
"either carries an aggressive prior-art paragraph or it does not go in". Units 2–5 need a
writing job; unit 6 needs the literature searched first. Same recommendation (separate),
different work, and it should be scheduled as research rather than drafting.

My `6+10` merge was wrong on two counts: it buried a 29,071-word standalone result inside a
ledger paper, and it separated `paper10` from `paper10b`, which share a question.

### Unit 7: merge. This is the one the evidence supports.

`P5` and `P4` share an actual **result** — both report the 6.5-year crossing. Splitting would
make each cite the other for the same number. The recorded strategy says this explicitly:
*"This is the one merge the evidence supports."* It is the only one of my seven that survives.

### Units 8, 9, 10: merge — thin member, shared system or question

Each folds a member that is too thin to stand alone into a host it shares a **record, system or
question** with: ARV is a second direction on the same cod record; E4 is a second withdrawal
system under the same depletion question; E3 is a second system under the same retention rule.
This is folding for the right reason — not thinness alone, but thinness plus shared object.

My errors here: I folded `paper10b` (E4) into the cod unit instead of the depletion unit, and I
left `paper11c` out of the forecasting unit entirely while folding it into `paper05`.

### Unit 11: contested. The recorded strategy contradicts itself.

This is the one case where I am not able to derive an answer, because the two recorded
statements disagree:

- `FAMILY_CONSOLIDATION_PLAN.md` §1.1 assigns `ws` to **Systems & Control Letters**.
- `FAMILY_PAPER_COUNT.md`'s revised ten folds `ws` into unit 10 at **Int. J. Forecasting**.

The content favours S&CL decisively. `paper11c` is *"Exact Audits of Worked Systems for the
**Obstruction Calculus**"* — 14 theorems about the calculus's own mechanisms, with 405 words of
real prior art. It shares its framework with units 1–5, not with forecasting, and at 11,123
words with 14 theorems it is not thin. Folding it into a forecasting paper would put
obstruction-calculus machinery in front of *Int. J. Forecasting* referees.

**Recommendation: unit 11 stands alone at Systems & Control Letters.** That makes eleven.
If ratification prefers the revised ten, it folds into unit 10 and the venue mismatch should
be addressed explicitly rather than by silence.

---

## What my seven-way partition cost

| my merge | verdict | what it cost |
|---|---|---|
| `1 + 2` | **wrong** | a TAC submission; did not fix the prior-art gap it was meant to fix |
| `3 + 4` | **wrong** | a MoOR submission; same |
| `5 + 11c` | **wrong** | a Tech Communiqué; misplaced `11c` out of the forecasting unit |
| `6 + 10` | **wrong** | buried a standalone 29k-word result; separated `10` from `10b` |
| `8 + 7` | **correct** | — |
| `9 + 9b + 10b` | **wrong** | misplaced `10b` (E4) into the cod unit |
| `11 + 11b` | **incomplete** | should also take `11c` |

Four venues surrendered, three papers misplaced, and — the substance of the error — **the
folding was aimed at a prior-art gap that folding is structurally incapable of closing.**

---

## The fold rule this yields

> **Fold** when the member shares a *result, record, system or question* with the host, or is
> too thin to stand alone at any venue it was assigned.
>
> **Separate** when the member poses its own question, carries its own result, and is at a
> legitimate length for a venue it was assigned.
>
> **Never fold to fix a missing prior-art section.** A merged paper still has no prior art.
> This is the case that units 2–5 present, and it is why separating them is right even though
> the bar assessment currently calls them blocked.

---

## Also done in this pass

**`phase0_scan.py` now context-checks before reporting.** A string match is a candidate, not a
finding. Each stale-provenance signature carries an excusing context; if the paper states the
current value *and* the caveat beside the stale one, the hit is reclassified as a disclosed
caveat and reported as a **positive** signal. Self-disclosure is now detected and reported
(`build has not been re-run`, `should be re-confirmed before submission`).

Effect on the 15 source heads: **10 hits reclassified as disclosed, 4 remaining actionable.**
The scanner now also catches a real asymmetry that the raw match missed — unit 3's provenance
sentence stated the run pin but not the current pin, unlike its siblings.

**`paper03` v16 (new version, source untouched).** Completes that sentence to
*"pinned to Lean~4 in `lean-toolchain` (currently `v4.34.1`); the checks were run under
`v4.14.0`"*, making it consistent with units 1, 4 and 5. 13 pp, 0 errors.

**`paper10` v53.** The one genuine finding from the first sweep: it imported the 6.5-year
crossing from the companion without its sensitivity band, at the single site where it reasons
from that number. The qualification is now inherited with the number.

---

## Verification of the prior-art inference (directed before ratification)

The partition rested on an *inference*: that the bar assessment's "blocked" / "below bar"
verdicts on units 2–5 are **prior-art-only**, so that writing the prior art is sufficient and
folding is unnecessary. That inference was checked against the bar assessment's actual wording
rather than assumed. **It was right on 2 of 4 — and the other 2 had their additional gaps
closed by work done after the assessment.**

| unit | bar assessment's stated gap(s) | beyond prior art? | status of that gap now |
|---|---|---|---|
| 2 `psuff` | "none states a prior-art position" | **no** | prior-art stub only |
| 4 `minimax` | "none states a prior-art position" | **no** | prior-art stub only |
| 3 `comp` | prior art **+** "five formal results for a computational paper, **with no comparator for its complexity claims**" | **yes** | **closed.** Saint-Pierre (1994) is now engaged in the body (L1416), and the rank result supplies a genuine comparator: a Helly-type "at most m+1 states suffice" bound is valid for convex common-action sets but *false* for a common blind control function, the correct dimension being information–time rank. Grew 10,077→13,629 w, 5→7 theorems. |
| 5 `ebc` | prior art **+** "against *substantial methodological development* this does not clear **at this length**" — requires "a scope decision: expand beyond the cube instance, or fold into paper 3" | **yes** | **the scope decision was taken.** Task 58 expanded m=4→m=5: census 16×2³² = 68,719,476,736 → 1,552, with raw growth 65,536× against stored growth 3.13×. Grew 3,578→6,435 w, 9 theorems. Remaining question is whether 6,435 w clears for a *Technical Communiqué* — the thinnest of the five. |

**Consequence.** The separate-and-write-prior-art recommendation survives, because the
decisive argument was never venue-count but this: *folding cannot produce a prior-art
section.* That argument is untouched. But the ratification carries one correction — **the
prior art for units 2–5 must be treated as a novelty test, not a drafting exercise.** No one
has checked whether these results survive the literature, because until now there was no
prior-art section to check them against. Attrition must be budgeted for.

**Attrition plan.** If a unit's result does not survive its novelty test, the options in
order are: reposition the claim to what the evidence supports; combine with a sibling *for the
new reason* (a collapsed novelty claim genuinely changes the fold calculus — the earlier
ruling only excluded folding **to fix a prior-art gap**, not folding for any other reason); or
drop. Unit 5 is the most likely casualty, being thinnest; unit 3 the least likely, its
comparator now being explicit.

---

## Open item: unit 1's venue, and a possible live submission

Ratification flagged that a **JMCDA special-issue submission for Paper 1** may exist from
earlier in the project, which would conflict with the Automatica assignment.

**Checked: no trace.** `JMCDA`, `special issue` and `Special Issue` return **zero** matches
across every `.md` in the workspace and across `paper01_obstruction_calculus_v61.tex`. Either
the submission predates the workspace record, was recorded only in conversation, or does not
exist as a live artifact.

Under the ratification's own rule — *the live submission's venue takes priority over the
architecture's assignment* — this needs a human answer before unit 1's row is locked. It is
the only unresolved item in the architecture.

---

## Ratification notes

The partition above is a proposal. Two points are genuinely open and I would rather you decide
than guess:

1. **Unit 11** — stand alone at S&CL (eleven units), or fold into unit 10 per the revised ten?
   The recorded strategy says both.
2. **Units 2–5** — my recommendation is separate-and-write-prior-art. That is four prior-art
   sections to write, and it is the cheaper path, but it does commit to four more submissions.
   If the strategic preference is fewer, stronger papers, folding is coherent — it just has to
   be paired with writing the prior art anyway, or the merged paper inherits the gap.
