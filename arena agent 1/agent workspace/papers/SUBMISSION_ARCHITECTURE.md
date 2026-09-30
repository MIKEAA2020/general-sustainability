# Architecture — coherence-driven, re-derived 2026-09-30

**Status: RATIFIED, then RE-DERIVED.** The partition was first derived from the recorded venue
strategy and grouped by *submission unit*. That derivation was **wrong in its reasoning**: the
case for separating units 2–5 rested on "folding surrenders four venues", and with
preprints.org as the primary target **no submission is lost by folding**. That argument is void.

This document re-derives the same partition with **coherence as the sole driver**, as directed.

## The driver

> **Fold** when the member shares a *result, record, system or question* with the host, or is
> too thin to be a coherent standalone piece of work.
>
> **Separate** when the member poses its own question, carries its own result, and is coherent
> on its own terms.
>
> **Never fold to fix a missing prior-art section** — a merged paper still has no prior art.

**Venue is informational only.** It records an intended eventual destination and is not the
reason any unit is constituted. Nothing below changes if a venue is retargeted.

**The cost-of-folding column is withdrawn.** It measured venue loss, which is not a cost under
the actual goal.

---

## The partition

| # | Unit | Papers | The single claim it makes | Words | Thm | Coherence basis |
|---|---|---|---|---|---|---|
| 1 | Obstruction calculus | `paper01` | No observation-based policy can keep a system viable, and there is a finite, checkable, exact certificate that proves it | 23,428 | 21 | Own question; 21 results; 951 w of real prior art |
| 2 | Probabilistic sufficiency | `paper02` | The calculus carries to belief states with no loss of exactness: value-one level ≡ viable-set recursion; α-vectors are an antichain | 13,632 | 18 | Own question, 18 results. **Disjoint from unit 1 (0.0% overlap)** |
| 3 | Computational certification | `paper03` | Nonviability is certifiable by a finite LP covering every measurable information-adapted control, with a certified two-sided bound | 13,629 | 7 | Own question; comparator now explicit (Saint-Pierre 1994; Helly bound shown false) |
| 4 | Minimax dual certificates | `paper04` | The common-action obstruction is dual to an adversarial measure on ≤ k+1 points (tight); Farkas and Isaacs are specialisations | 8,566 | 13 | Own question, 13 results — a complete argument at this length |
| 5 | Exact belief computation | `paper05` | The exact discipline survives the curse of dimensionality: antichain + pairwise bound collapse 68.7 bn evaluations to 1,552, and the bound's failure at m=5 is the sharper news | 6,435 | 9 | Own question, 9 results, complete m=5 classification |
| 6 | Quantifier-order separation | `paper06` | Compensatory and noncompensatory feasibility are related by a quantifier commutation that fails on an **open region** | 29,071 | 0 | Own question; own applied sections |
| 7 | The decision clock | `paper07`+`paper08` | Institutional latency — not ecology — decides whether governance stabilises or destabilises a resource, **and how that latency is represented changes the computed answer** | 47,923 | 16 | **Shares a result**: both report the 6.5-yr crossing |
| 8 | Certification on real records | `paper09`+`paper09b`+`paper10b` | Reference points can be defended by certification rather than simulation, **and that certification has a horizon set by the map, not the method** | 33,092 | 14 | **Shares machinery and question**; two systems (cod, Edwards) |
| 9 | Depletion arithmetic | `paper10` | Depletion time is three mutually non-interchangeable quantities; what a typed ledger can certify is delimited by its typing | 35,012 | 0 | Own theory **and** own application — see note |
| 10 | Forecasting baselines and the null | `paper11`+`paper11b` | Process-based models are not self-justifying: at the annual origin they do not beat persistence, and the failure is diagnostic of the driver's spectrum | 30,401 | 0 | **Shares a rule and a question**; two systems (cod, Edwards) |
| 11 | Exact audits of worked systems | `paper11c` | Each mechanism of the obstruction calculus acquires a count, a witness and a boundary on worked systems | 11,123 | 14 | Own question, 14 results, 405 w real prior art |

**Eleven units.** One change from the venue-driven draft: **`paper10b` moves from unit 9 to
unit 8.** Everything else is unchanged.

---

## What changed, and why

### The one structural change: `paper10b` → unit 8

Under the recorded venue strategy, `paper10b` (E4, Edwards viability kernels) sat with
`paper10` (P3, ledgers) at *Ecological Economics*. Under coherence it belongs with unit 8.

- **Its central result is unit 8's claim.** `paper10b` reports that *"every positive-pumping
  certified kernel is empty beyond three years — an optimistic bound on a defect the
  out-of-sample audit exceeds."* That is the horizon result, on a second system. Unit 8's
  claim is precisely that certification has a horizon set by the map.
- **Its machinery is unit 8's machinery.** It computes robust viability kernels under a
  retention protocol frozen before any score — exactly `paper09b`'s (ARV) apparatus. With
  `paper10` it shares only a *domain* (groundwater), not a method or a question.
- **`paper10` does not need it.** The standing direction on P3 was that *"the four applied
  sections are the ingredient that lifts it from typology to measurable consequence"* — P3
  carries its own application (three public-data indicators classified at their exact status,
  plus the registered domain templates). It does not need E4 to make that lift.
- **Unit 8 gains breadth it otherwise lacks.** As `{09, 09b}` it is cod-only. With `paper10b`
  it is exact viability certification on **two** real systems with no hydrology, biology or
  institutional history in common.

| | unit 8 | unit 9 |
|---|---|---|
| Option A (recorded) | 23,766 w — cod only | 44,338 w |
| **Option B (coherence)** | **33,092 w — cod + Edwards** | **35,012 w** |

### What did not change, and why the reasons had to be replaced

**Units 1–5 still separate — but not for the reason I gave.** The venue argument is void, so
the separation now rests on two venue-independent grounds:

1. **Don't bury independent results.** The five are essentially disjoint: sentence-level overlap
   is 0.0% (obstr↔psuff/comp/ebc), 0.7% (obstr↔minimax), 4.5% (comp↔ebc). Folding removes
   nothing and buries five independent results inside one another. This is a coherence defect
   under any target.
2. **Folding cannot produce a prior-art section.** Units 2, 3, 4 and 5 have stub prior-art
   sections (0 words) against 405–951 words for the others. A merged paper still has none. This
   is the argument that survives the change of driver intact.

**Units 7, 8, 10 still fold**, on shared *result* (7: the 6.5-yr crossing), shared *machinery
and question* (8), and shared *rule and question* (10) — with a thin member in each case
(9,637 w and 9,326 w respectively). None of this depended on venue.

### Guarding against folding drift

Removing venue pressure removes the main argument *against* folding, so the drift risk is real
and is worth naming explicitly. Three checks hold the line:

- **Disjointness blocks the big fold.** The obvious temptation is one large obstruction-programme
  paper from units 1–5. The overlap test forbids it: there is no duplication for a merge to
  remove, so the only effect would be to bury four independent results.
- **Thinness is not alone sufficient.** Units 4 (8,566 w) and 5 (6,435 w) are the thinnest, but
  each poses and answers one question completely. Thinness justifies folding only when the
  member also shares a result, record, system or question with a host — neither does.
- **A buried result is a defect under any target.** Unit 6 at 29,071 w was folded into unit 9 in
  my earlier seven-way partition. That buried a standalone result with its own claim inside a
  paper about ledgers. It is wrong whether the output is a preprint or a journal article.

---

## Prior art: still the live defect, and now the gating task

Measured prior-art sections across the fifteen sources:

| unit | 1 | **2** | **3** | **4** | **5** | **6** | 7a/7b | 8a/8b/**8c** | 9 | 10a/10b | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| words | 951 | **0** | **0** | **0** | **0** | **0** | 518/652 | 608/647/590 | 531 | 532/438 | 405 |

Five units have no prior-art section at all. This is a defect under any target — a preprint
without prior art is incomplete scholarship whether or not it is peer-reviewed.

**It must be treated as a novelty test, not a drafting exercise.** No one has checked whether
these results survive the literature, because until now there was no prior-art section to check
them against. Attrition is to be budgeted for.

**Attrition plan.** If a unit's result does not survive: (i) reposition the claim to what the
evidence supports; (ii) combine with a sibling — permissible here, since the prohibition is
specifically on folding *to fix a prior-art gap*, not on folding for a new reason; or (iii)
drop. Unit 5 is the likeliest casualty (thinnest, 6,435 w); unit 3 the least likely (its
comparator is now explicit).

---

## Verified before ratification

The prior-art inference was checked against the bar assessment's actual wording rather than
assumed. **It held on 2 of 4.** Units 2 and 4 are cited for prior art only. Units 3 and 5
carried additional gaps, both since closed:

- **Unit 3** — *"no comparator for its complexity claims."* Now closed: Saint-Pierre (1994) is
  engaged in the body, and the rank result supplies a real comparator (a Helly-type "at most
  m+1 states suffice" bound holds for convex common-action sets and is **false** for a common
  blind control function, the correct dimension being information–time rank).
- **Unit 5** — *"does not clear at this length"*, requiring a scope decision. Now taken: m=4→m=5,
  census 16×2³² = 68,719,476,736 → 1,552, raw growth 65,536× against stored growth 3.13×.

---

## Open questions

1. **Is preprints.org the final target or the first step?** The record
   (`FAMILY_PAPER_COUNT.md` §0) treats it as *staging*, with one preprint mapping to one
   eventual journal submission; the current direction treats it as primary. These are
   compatible if the reading is "primary near-term target, journals later." The answer
   determines only whether the venue column is retained as provisional or dropped entirely.
   **The partition is the same either way**, since it is now coherence-driven.

2. **Unit 1's venue is no longer an open item.** The JMCDA concern is void: with preprints as
   the target there is no competing journal submission to conflict with.
