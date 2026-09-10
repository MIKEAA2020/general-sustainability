# E1 v19 — Joint Evaluation of Three Audits (grok / gpt / qwen)

Round 2. Every checkable claim below was verified against `E1_v19.tex` directly.
A scanner hit or an auditor assertion is evidence, not a verdict.

**Verdict counts:** 9 CONFIRMED defects · 4 REJECTED · 6 PARTIAL · rest = style, triaged.

---

## A. CONFIRMED DEFECTS — verified in the source, must fix

### A1. Table 9 row count is wrong: text says 32, table has 28 (gpt §8, qwen §1.3)
**VERIFIED.** Parsed the longtable: exactly **28 data rows** (7 per Spec×horizon block).
L1002 reads "five of the thirty-two rows". Both auditors caught this independently.

### A2. The "five disagreement rows" count is ALSO wrong — it is four (my check, neither auditor)
Both auditors flagged the denominator; **neither checked the numerator.** Programmatic
recount of rows with CI excluding zero *and* |z|<1.96:

| Spec | h | comparison | z | CI |
|---|---|---|---|---|
| A | 1 | M4 vs M3 | 0.99 | [+4.7, +144.7] |
| B | 1 | M3 vs persist | 1.85 | [+1.0, +92.5] |
| B | 5 | M1b vs persist | 1.80 | [+18.2, +250.9] |
| B | 5 | M4 vs M3 | 1.88 | [+20.2, +177.4] |

⇒ **"five of the thirty-two" must become "four of the twenty-eight."** Two errors in one clause.

### A3. The square-root/"different estimands" explanation is mathematically wrong (gpt §1.1)
**VERIFIED ALGEBRAICALLY.** √ā−√b̄ = (ā−b̄)/(√ā+√b̄) with positive denominator, so the two
differences are **sign-identical**; a bootstrap p from tail proportions about zero is
*unchanged* by the square root. Numerically confirmed on random draws.
The manuscript's stated mechanism ("square root compresses the heavy right tail … more
stable") cannot explain the DM/bootstrap disagreement. The *disagreement is real* (A2
lists four genuine rows) — but the explanation offered for it is false and must be deleted.
This is the single most serious defect in the round: a wrong mechanism attached to a
correct observation. **gpt alone found it; qwen explicitly praised the same passage
("now explained as two different estimands") as an improvement.**

### A4. M4 decomposition mixes matched and mixed-origin baselines (qwen §2.1)
**VERIFIED.** L1362 "694 of 713 kt". 713 = 1031 − **318** (Table 6 mixed-origin), but the
matched Spec B h=5 persistence is **300** (Table 9, n=55). The h=1 figure likewise uses 88,
not 84.4. The paper elsewhere makes a point of origin-matching. Recompute on matched
baselines or state the origin set explicitly.

### A5. Abstract uses "negative certificate", body defines only "non-retention" (qwen §1.1)
**VERIFIED.** L90 abstract "supports a negative certificate"; L1331 "M3 and M4 are not
certificates here". Definition 2.5 is titled *Non-retention*. Term undefined in body.
Note this also violates the standing register policy. Replace both with "non-retention".

### A6. K-bound definition inconsistent between §2.2 and §3.6 (qwen §1.5)
**VERIFIED.** L388 "training-window maximum"; L1245 "the maximum is taken over the states
the one-step regression conditions on". These differ: including 2007 (81.10) gives 91.10,
not 50.8. **This is exactly the error I made myself in an earlier round** (see Errors log:
81.1 vs 40.8). §2.2 must adopt the §3.6 wording. High priority — it is the precise
ambiguity that already produced one wrong number in this project.

### A7. Estimation bounds for 𝔰, b, φ never declared (gpt §4, qwen §1.6)
**VERIFIED.** L387 declares bounds for r and K only. Observation 3.2 uses admissible
range [0, min S] = [0, 9.68] which appears nowhere in Methods; φ clipping to [±0.95]
appears in passing; b has no stated bounds. Reproducibility gap. Both auditors agree.

### A8. "K at bound" contradicts "500 is the multi-start initialiser" (qwen §1.9)
**VERIFIED.** L1615 Data availability says "K at bound"; §2.2 and Table 10 insist 500 kt is
an initialiser, not a bound. One-line fix.

### A9. Prop 4.1 "fixed catch sequence" does not support the autonomous proof (gpt §1.4, qwen §1.8)
**VERIFIED.** L1267 says "fixed catch sequence"; a time-varying prescribed path gives F_t,
not F, so F(S_-)=S_- and forward invariance of the sub-repeller interval do not follow —
yet the text applies the proposition to M2, which uses year-by-year catch. Restrict to
**constant catch (M1, and M1b under its own equilibrium analysis)**; M2 is motivated, not
covered. gpt additionally notes clipping can map a positive state to 0, so the invariant
set should be **[0, S_-)**, not the open interval — correct, and cheap to fix.

Given this project has already withdrawn Prop 4.1 once and Lemma 3.2 once, apply the
standing check: proof conclusion vs statement quantifier, and hypothesis holds where applied.

---

## B. REJECTED — do not act

### B1. gpt: "delete the p column / remove the bootstrap as a test"
**REJECT the deletion.** A3 kills the *explanation*, not the *procedure*. The verified
record (carried from v17) is that DM is bandwidth-fragile while the block bootstrap is
stable across block lengths, and the four A2 rows are genuine. Deleting the bootstrap
column would discard the more reliable of the two inferential summaries because the prose
around it was wrong. Fix the prose; keep the column; drop the word "decisive".

### B2. qwen §1.10 / gpt: "prey modules not identified" is unsupported
**REJECT as stated, ACCEPT the wording fix.** Both are right that no profile diagnostic
exists for the prey variants, so "were not identified" overstates. But qwen frames this as
an internal inconsistency; it is only a wording overreach. Soften to "weakly constrained
by short training windows and missing index years, and they fail the retention score."
Do **not** run new prey diagnostics to justify the strong claim — that is scope creep on a
result that does not depend on it.

### B3. gpt §13.7: "add a regularized AR / local-trend comparator"
**REJECT.** This adds a new model to a frozen scored ladder after the scoring pass. It
violates frozen-spec discipline and would require a specification amendment. The point it
raises ("is it this ladder or any extrapolator?") is legitimate but belongs in Discussion
as a stated limitation, not as a new run.

### B4. grok: "cut companion-paper citations from the intro"; gpt: "move aquifer comparison out"
**REJECT the citation cut.** Companions are DOI-backed and citable under standing policy —
this is precisely the v18 error. *Accept* the narrower point: the Protocol-status paragraph
should not rank its "evidentiary standing" against the aquifer paper (self-commentary, and
it invites "why wasn't this preregistered?"). Cite the companions; drop the comparison.

Also note grok's micro-edit list says to search-and-destroy "in review" — **already done in
v19; zero occurrences.** grok appears to be reading a pre-v19 draft in places.

---

## C. PARTIAL / JUDGEMENT

- **C1. Intro pre-freeze wording (qwen §1.2).** Could not verify: the phrase qwen quotes
  ("coded before the first scoring pass and applied unchanged") returns **no match** in
  v19 — already fixed, or qwen is quoting an earlier draft. Re-check against the intro
  before editing. Same suspicion as B4.
- **C2. Uncited references (qwen §6.6).** VERIFIED: `Abaee 2026c` and `DFO 2024b` appear
  only in the reference list, never in the body (lines 1525, 1546). Cite or cut. Note
  2026c was added by *me* in v19 — my own loose end.
- **C3. DM sentence is unbalanced (qwen §2.2).** Correct: Spec A moves 1.14→2.30, which
  also crosses 1.96. The text singles out Spec B. One-sentence rebalance.
- **C4. "H1 vacuous … turns on H2 alone" (gpt, qwen §4.2).** Correct — H3 (both horizons,
  tie band) still binds. L481. Trivial fix.
- **C5. Origin-matched baselines in Tables 6–8 (gpt §1.5).** Right in principle; overlaps
  A4. Promote matched baselines to the primary tables, demote mixed-origin to an audit
  table. Moderate reformatting, real gain.
- **C6. Missing 𝔰 values in Table 10 (qwen §1.7).** Table 10 claims to collect *every*
  printed fitted value; the two recovery-window 𝔰 (2.1e−23, 9.4e−6) are absent. Add.
- **C7. qwen §5.1–5.2 LaTeX breakage** (`\arraybacksla sh`, bare-paren math) — **extraction
  artifacts.** v19 compiles clean to 488,980 B. No action. qwen hedged correctly.

---

## D. STYLE / PRESENTATION (grok's domain)

grok's contribution is almost entirely presentational, and on that axis it is the most
useful of the three: lead with the result, get fitted numbers out of §1, demote
Definitions 2.3/2.5 and Prop 3.1 from theorem environments, split the 80+ word sentences
in §3.2/§3.5, compress §3.5 to one paragraph + table. All consistent with standing register
policy. grok's proposed abstract and gpt's §11 intro are both usable drafts; grok's is
tighter, gpt's is better grounded on the predictand ("assessment-derived SSB, not measured").

**Note both propose deleting the de-jargoning targets already on the (m)(1) list** —
"scored ladder", "retention rule" as lead concept, "machine layer", "freeze". Converging
independent evidence that the coinage cluster is the top presentational blocker.

gpt's "you still need a literature-grounded gap statement, do not invent one" is correct
and is the one item here that cannot be executed by editing — it needs real sources.

---

## E. WHERE THE AUDITS DISAGREE

1. **The bootstrap.** qwen *praises* the "different estimands" explanation; gpt proves it
   false. **gpt is right** (A3). qwen accepted a plausible-sounding rationale without
   checking the algebra — the same failure mode as accepting a scanner hit without context.
2. **Prop 4.1.** qwen calls the scoping fixed; gpt finds the residual catch/autonomy gap
   and the clipping/invariance flaw. **gpt is deeper.**
3. **Formalism.** grok says cut the theorem environments; qwen says fix them in place.
   **grok is right for a journal audience**; the content survives as prose either way.
4. **Table 9.** Both spotted the denominator; **neither spotted the numerator** (A2).

**Reliability ranking this round: gpt > qwen > grok on correctness; grok > gpt > qwen on
presentation.** gpt is the only one that verified anything mathematically. grok is
partly auditing a stale draft (B4, "in review").

---

## F. RECOMMENDED FIX ORDER FOR v20

**Tier 1 — correctness (all verified, all cheap):**
1. A3 delete the square-root explanation + "decisive"; keep the bootstrap column
2. A2+A1 "four of the twenty-eight"
3. A4 recompute M4 decomposition on matched baselines
4. A6 K-bound wording → conditioning states
5. A9 Prop 4.1 → constant catch, interval [0, S_-), M2 excluded
6. A5 "negative certificate" → "non-retention" (also register policy)
7. A8 "K at bound" → "at the 500-kt multi-start initialiser"

**Tier 2 — completeness:** A7 bounds for 𝔰/b/φ · C6 Table 10 𝔰 rows · C2 cite-or-cut ·
C4 H2+H3 · C3 DM rebalance · B2 soften prey wording

**Tier 3 — presentation:** grok's §1 rewrite + abstract · demote Def 2.3/2.5, Prop 3.1 ·
C5 matched-baseline tables · sentence splitting · B4 drop aquifer standing comparison

Tier 1 + 2 are all confined to prose and two recomputations; none touches the frozen
scoring core, and **none changes the retention verdict** — persistence still wins
everywhere. Tier 3 is the desk-rejection risk.

---
---

# ADDENDUM — Items Not Adjudicated in the First Pass

The first pass resolved the high-severity cluster and swept grok's and gpt's line-level
material into "Tier 3 / style". That was too coarse: several of those items are
**correctness** issues, not presentation. Each is verified against `E1_v19.tex` below.
Numbering continues from the main document.

## G. NEWLY CONFIRMED DEFECTS

### G1. "Most annual increments are positive" is false — it is 7 of 12 (gpt §6)
**VERIFIED, and this is a real error.** Computed from the V2 series (1995–2007):
`[+6.37, +4.52, +7.68, +6.34, −0.17, −4.92, −5.63, −1.80, −2.00, +5.11, +15.65, +40.27]`
⇒ **7 positive, 5 negative.** "Most" is defensible only in the barest 7/12 sense, and the
window contains **five consecutive declines** (1999–2004) — the very feature the sentence
is used to wave away when arguing the Allee term should be weakly constrained. gpt told me
to "verify the exact count before making this statement." I did; the rhetoric outruns it.
Replace with the explicit count and acknowledge the consecutive-decline run.
**Missed by grok and qwen; missed by me in the first pass.**

### G2. The profile statistic is a Gaussian likelihood construct that the paper never declares (gpt §1.3)
**VERIFIED NUMERICALLY — and it implicates my own diagnostic.** gpt conjectures the
statistic is Λ(𝔰) = n·log{SSE(𝔰)/SSE(𝔰̂)}. Testing that against my reported numbers:
- coarse: 12·log(135.04/126.50) = **0.784** → paper prints 0.78 ✓
- annual: 12·log(126.50/122.90) = **0.346** → paper prints 0.35 ✓

Exact reproduction. So the paper fits by **least squares** but reports a **likelihood-ratio**
statistic against **χ²₁**, without ever stating the Gaussian-iid-homoskedastic assumptions
that licence the conversion. gpt's four objections to the χ²₁ reference are all individually
true of this fit: 𝔰̂ is **at the boundary** (2.1e−23), **r is also at its bound** (2.000),
n = 12, and the "observations" are reconstructed states, not measurements. Boundary cases
alone break the χ²₁ null.

**This does not overturn the conclusion** — the profile is flat and 𝔰 is unidentified; that
survives as a *descriptive* result and is corroborated by the r–K compensation path.
**It does overturn the phrasing.** Drop "settles the identification question directly",
drop "confidence set = whole admissible interval", and report it as a descriptive profile:
objective increase plus compensation path. Also declare that `[0, min S_t]` is an
**estimation bound**, not a mathematical admissibility region (gpt is right that negative
production above min S is not inadmissible; my own note already flags the s∈[0,40] grid as
leaving the region — that was a *bound*, not a law).

Standing lesson reinforced: *constants reproducing is not validation.* The number was right;
the inferential frame around it was not.

### G3. "Except in M3, which carries the fitted residual forward as a state." (gpt §4, qwen §5.3)
**VERIFIED at L293** — sentence fragment, and it **omits M4**, which inherits M3's residual
mechanism. Both auditors independently flagged it. Merge into the preceding sentence and
name M3 *and* M4.

### G4. M3/M4 residual recursion is never written down (gpt §4)
**VERIFIED: zero matches** for any φ^k recursion in the source. Table 2 alone does not let a
reader reproduce M3 or M4. Unspecified: whether the AR regression has an intercept; which
residual is available at issuance; whether residuals are computed pre- or post-clipping;
how M4 initialises the residual state. This is a **reproducibility defect**, not a style
point, and it compounds A7 (undeclared bounds). Write the recursion out — but read it off
`run_ladder.py`, do **not** adopt gpt's guessed indexing, which it explicitly says to check.

### G5. M4 may be a stale-start experiment, not a delayed-information one (gpt §4)
**Substantively correct and unresolved in the text.** Memory confirms M4 differs from M3
*only* by `start_idx = i_tr[-1] − delay`; the fitted parameters are M3's. So M4's parameters
still see S_t through training even though its trajectory starts at S_{t−1}. That makes it
**stale initialisation**, not a genuinely delayed information set. The paper's §4 delay
decomposition leans on it. Relabel accurately — this is cheap and honest — and note that a
true delayed-information variant would require truncating training too. **Do not build that
variant**: new ladder rung, frozen spec, same objection as B3.

### G6. "byte for byte" claimed without environment qualification (gpt §5, qwen §6.2)
**VERIFIED at L99 (abstract), L516, L1602.** Data availability elsewhere concedes a fixed
interpreter/library stack and an environment-sensitive M1b row (±17 kt). The abstract's
unqualified claim contradicts the paper's own caveat. Add "within the pinned environment".
Both auditors agree; trivial.

### G7. Direction-score definition is ambiguous (gpt §5)
Scores of 0.25 and 0.57 imply 4 and 7 comparisons on 5- and 8-year windows, i.e. the first
origin-to-test transition is excluded. That is never stated. Also unstated: whether 5-year
RMSE is endpoint or trajectory-average, the log base and floor, and the fixed-window RMSE
year set. Small, but these are score definitions in a scoring paper.

### G8. Brier is a misclassification rate under 0/1 forecasts (gpt §5)
Correct. With hard 0/1 forecasts the Brier score is numerically the misclassification rate;
calling it a Brier score implies probability forecasts that do not exist here. Rename
"threshold misclassification rate (equivalently, Brier for deterministic binary forecasts)".
This *strengthens* the existing degeneracy disclosure rather than weakening it.

### G9. Persistence direction score printed as 0 should be NA (gpt §5)
If persistence is excluded from the direction score by construction, printing 0.00 reads as
an observed 0% hit rate. Print NA.

## H. NEWLY REJECTED

### H1. gpt §1.2: "prose and Table 10 reverse the catch-treatment labels" — **FALSE**
**REFUTED at L774–780.** The prose reads: *"r = 0.458 with K resting at the multi-start
initialiser of 500.0 kt … against r = 0.370 with K at its upper bound, 5000.0 kt"*, in a
sentence whose subject is the coarse→annual contrast, and *"K = 105.8 against 129.8"* in the
same order. Table 10 (L1206–1217) assigns coarse→{0.458, 500.0}, {105.8}; annual→{0.370,
5000.0}, {129.8}. **They agree.** gpt ranked this its #1 resubmission blocker and hedged
correctly ("only if Table 10 is confirmed") — it is not a defect. My own profile run
independently associates ~106 kt with coarse and 129.8 with annual, which gpt itself noted
agrees with Table 10.

**No action.** Worth recording because acting on it would have *introduced* an error — the
same failure the v18 companion-reference incident produced.

### H2. gpt §6: "34% / above the new LRP mixes years and versions" — **already correct**
L551 states 2015 SSB = 33.8% of the 2016 LRP (matching the advisory 34%); L819 gives
2024/LRP = 1.24 for xteNCAM. Dates and reconstructions are attached. Optional tightening at
L823 only.

### H3. grok: "say 'in review' once in references" — **contradicts standing policy**
grok recommends retaining "in review" for Rose (2026) / Abaee (2026a,b). v19 has **zero**
occurrences and all companions carry Zenodo DOIs. Further confirmation grok is reading a
pre-v19 draft. **Ignore.**

### H4. gpt §3: "a retention outcome cannot transfer because the LRP differs" is a must-fix
gpt is right that the LRP does not enter primary RMSE, so it cannot drive non-transfer.
But the paper's no-pooling rule is a **frozen-spec commitment**, not an inference from the
LRP. Fix the *stated reason* (trajectories, formulation, coverage, catch spec differ; LRP
touches only the secondary diagnostic) — do **not** weaken the no-pooling rule itself.

## I. ADDITIONAL CONFIRMATIONS OF EXISTING ITEMS

- **gpt §5 and §8 independently reach A1** ("five of the thirty-two"). Neither gpt nor qwen
  rechecked the numerator; A2 stands as the only source for "four".
- **gpt §5 reaches C4** (H2 alone → H2 and H3) independently of qwen §4.2.
- **gpt §9 "held in the archive rather than invented"**: phrase **not present** in v19 —
  already removed. Stale-draft artifact, like H3.
- **gpt §6 "driven hard against the upper bound"**, **"evidence against a catch-regime
  reading"**, **"which is what the scored comparison then confirms"**, **"that the optimiser
  does not move K is itself a measure"** (verified present at L777–778): all four are
  overclaim-by-verb, all fold into the Tier-3 register pass. The optimiser one is the
  strongest — a stationary iterate is not a measurement of flatness; the *profile* is.
- **gpt §10 "Slack near zero by construction"**: correct that a mean-based threshold forces
  the *mean* deviation to zero, not the annual ones. Wording fix.
- **gpt §8 "block-length sensitivity shown for M1 only"**: correct; the robustness claim
  should be scoped to the M1 comparison actually tested.
- **gpt §8 "rerun and archive the coarse-regime per-origin files"**: legitimate and the
  cleanest resolution of the Table 9 Spec A footnote — the scoring stack is deterministic,
  so regeneration should be feasible. Flag as optional but valuable; if regeneration does
  not reproduce Table 4, that must be resolved before submission.

## J. REVISED FIX ORDER

**Tier 1 (correctness) — add:** G2 profile-likelihood reframing · G1 the 7-of-12 count
**Tier 2 (completeness) — add:** G4 M3/M4 recursions · G5 relabel M4 · G3 fragment+M4 ·
G6 environment qualifier · G7 score definitions · G8 Brier rename · G9 NA · H4 restate
no-pooling reason
**Tier 3 — add:** gpt's four overclaim verbs · slack wording · block-length scoping

**Do not act on:** H1 (false), H2 (already correct), H3 (policy violation), B1–B4, and any
grok item quoting text absent from v19.

Still no change to the retention verdict. G2 is the only addendum item that touches a
*result* — and it changes how the Allee finding is licensed, not what it says.
