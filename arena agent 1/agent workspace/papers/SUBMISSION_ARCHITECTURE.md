# Architecture — coherence-driven, re-derived 2026-09-30

**Target: preprints.org — final, not staging.**

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
> **Never fold to fix a missing prior-art section** — a merged paper still has none. *(The rule
> stands. Note that as of 2026-09-30 it does not describe units 2–5, whose prior-art gaps turned
> out to be a measurement error; see the corrected table under "Prior art".)*

**Target: preprints.org, as the final destination.** Journal submission is a possible secondary
prospect and is recorded nowhere as a constraint. No unit below is constituted, sized or split
for the convenience of a journal, and no column records a venue.

**The venue column is dropped, not provisional.** A provisional column reopens the question
"would this fold more neatly at journal X?" every time the partition is revisited. With the
target settled, that question has no standing.

### What "final target" changes about the bar

This is a real change, not bookkeeping. Under a journal target three functions are discharged
*for* the paper by referees: error detection, scope moderation, prior-art screening. Under
preprints.org as the final destination none of them are.

- **Screening is narrow, so the checking burden is ours alone. The standard is unchanged.**
  Preprints.org screens for "basic scientific content, author background, and compliance with
  ethical standards", in under one business day [2](https://www.preprints.org/about). It will
  not detect a false lemma, a mis-stated interval, or a missing prior-art section. That is a
  statement about **who** checks, not about **how much** checking is owed: the objective remains
  valid, accurate, correct science — no erroneous mathematics, no erroneous prose. Because no one
  else will catch those defects, **we are the only ones who can**, and the passes below are the
  mechanism for doing so.
- **There is no revision round.** Screening is a pass/fail gate, not a referee loop. What is
  posted is what stands.
- **It cannot be taken back.** Authors must acknowledge that "preprints cannot be completely
  removed once online" [5](https://www.preprints.org/blog/post/preprints-young-academics).
  A published defect is permanent and carries a DOI.

So the pending passes are not preparation for a gate that will check them — **they are the only
gate there is.** Phase 0 (soundness), the prior-art novelty test, and the claim audit move from
advisory to load-bearing. And because publication is irreversible, order matters: a unit should
not be posted before it has passed its own passes.

**Upsides worth banking.** Preprints.org assigns a DOI and posts under CC BY 4.0
[1](https://www.preprints.org/blog/post/preprint-benefits)
[3](https://www.preprints.org/blog/post/chances-getting-published), so every unit — and every
supplementary file — is permanently citable and dated. This is what makes the standing
"no content lost" rule satisfiable: material displaced to supplementary is citable, not
orphaned.

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

**Units 1–5 still separate — but not for either reason I gave.** The venue argument is void, and
the prior-art argument (ground 2 below) was **struck on 2026-09-30** when direct measurement
showed every unit already has a substantial prior-art section (709–1,680 w). The separation now
rests on **one** venue-independent ground:

1. **Don't bury independent results.** The five are essentially disjoint: sentence-level overlap
   is 0.0% (obstr↔psuff/comp/ebc), 0.7% (obstr↔minimax), 4.5% (comp↔ebc). Folding removes
   nothing and buries five independent results inside one another. This is a coherence defect
   under any target, and it is sufficient on its own.

2. ~~**Folding cannot produce a prior-art section.**~~ **STRUCK — factually false.** It asserted
   units 2–5 had "stub prior-art sections (0 words)". They have 1,493 / 1,680 / 1,321 / 709 w
   respectively. The *rule* against folding to fix a prior-art gap remains good doctrine; it
   simply no longer describes these units and cannot support their separation. See the corrected
   table under "Prior art" below.

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

**CORRECTED 2026-09-30.** The table previously in this place recorded **0 words** of prior art
for units 2–6. That measurement was **wrong**. Direct measurement of the source heads:

| unit | 1 | 2 | 3 | 4 | 5 | 6 | 7a/7b | 8a/8b/8c | 9 | 10a/10b | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| words | 951 | **1,493** | **1,680** | **1,321** | **709** | **921** | 518/652 | 608/647/590 | 531 | 532/438 | 405 |

Every unit has a real prior-art section. **Two consequences:**

1. **The argument "folding cannot produce a prior-art section" is void as a ground for keeping
   units 1–5 apart.** There was no missing prior-art section to produce. That ground is struck
   from §"What did not change" below; the separation now rests on disjointness alone.
2. **This was never a drafting exercise.** Prior art existed and had not been checked against
   the literature — which is the novelty test as originally specified.

**Prior-art pass result (2026-09-30), recorded in `PRIOR_ART_PASS.md`:**

| unit | verdict | action required |
|---|---|---|
| 2 | **PASSES** | none |
| 3 | **PASSES** | none |
| 4 | **PASSES** | optional: surface the Carathéodory/Helly attribution in the related work |
| 5 | **SURVIVES** | antichain-*algorithms* literature uncited; Harper's theorem uncited; abstract looser than body |
| 6 | **SURVIVES** | Kuhn's theorem unaddressed; Wei & Zhang (2024) uncited |

**No unit was repositioned, combined, or dropped. The attrition budget was not drawn on.**
Units 3 and 4 had already anticipated and conceded the classical results that a search would
surface; unit 5's and unit 6's claims survive but each needs two citations to be safely made.

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

1. **RESOLVED (2026-09-30).** Preprints.org is the **final** target; journals are a possible
   secondary prospect only, and are never allowed to shape the partition. Venue column dropped.

2. **Unit 1's venue is no longer an open item.** The JMCDA concern is void: with preprints as
   the target there is no competing journal submission to conflict with.

3. **NEW — pre-posting checklist.** To be verified against the platform itself before the
   first unit goes up; none of it changes the partition.

   - **AI-use disclosure.** Preprints.org is run by MDPI, whose house policy requires
     generative-AI use to be disclosed in an Acknowledgments statement and described in detail
     in Methods, with grammar and formatting exempt
     [1](https://libguides.iou.edu.gm/c.php?g=1482669&p=11059956)
     [2](https://www.mdpi.com/about/announcements/5687). That policy is documented for MDPI
     *journals*; whether it is applied to the preprint platform has **not** been verified.
     It bears squarely on this family, developed with AI assistance. Verify before posting and
     **default to disclosure if uncertain** — over-disclosure carries no penalty.
   - **Research data must be available** at submission
     [5](https://www.preprints.org/blog/post/preprints-young-academics). Each unit needs a
     data/code availability statement. The Lean-checked units already name their toolchain
     pins, which is most of one.
   - **Consent to the no-withdrawal policy.** Co-authors must agree to CC BY 4.0 posting and
     to the fact that the preprint cannot be removed once online [5]. Sole-authored or not,
     that irreversibility is worth a conscious decision per unit, taken *after* its passes.
