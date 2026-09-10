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
