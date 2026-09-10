# E1 — Tier 3 Restructuring Plan (grok's presentation pass)

> **REVISION 2.** Revision 1 was audited against the source and had four defects, one of
> them a missed correctness bug. Corrections are marked **[R2]** throughout and summarised
> in §0b. The headline word-count target in revision 1 was wrong in both operands.

**Baseline:** `paperE1_cod_forecast_ladder_v21.tex` (0 blockers, compiles, 501,159 B).
**Target:** v22. **Nothing in this plan changes a number, a verdict, or a scored result.**
Every item is presentation. Tier 1 and Tier 2 (correctness, completeness) are already
shipped in v20/v21 — see `E1_V20_CHANGELOG.md` and `E1_AUDIT2_JOINT_EVALUATION.md` §J.

grok's framing: *"The paper will still look elementary unless the first page states a plain
question, a plain design, and a plain negative result, and unless the formal apparatus is
pushed out of the reader's way."* That is a desk-rejection risk, not a scientific defect,
which is why it was deferred — and why it should now be done in one deliberate pass.

---

## 0. Measured baseline (all figures computed from v21, not estimated)

| Section | Words (excl. tables) |
|---|---|
| ~~Highlights 533~~ **[R2]** Highlights 63 · **abstract 456** (measured separately) |
| 1. Introduction | 945 |
| 2.1 Data | 225 |
| 2.2 Forecast models | 1,119 |
| 2.3 Evaluation design | 855 |
| 3.1 Primary specification | 951 |
| 3.2 Annual landings / survey | 833 |
| 3.3 Alternative assessment | 594 |
| 3.4 Prey-informed | 466 |
| 3.5 Uncertainty | 998 |
| 3.6 Fitted parameters | 214 |
| **4. Discussion** | **2,511** |
| 5. Conclusions | 119 |
| References | 960 |
| ~~**Total 11,323**~~ **[R2] TRUE BODY (Intro→Conclusions): 9,830** |

**Diagnostics:**
- **Abstract: 458 words.** *Fisheries Research* permits **250**. **Hard violation — 208 over.**
- **Highlights: 5 bullets, longest 105 characters.** The guide permits 3–5 bullets at
  **≤85 characters each**. **Two bullets over (91, 105). Hard violation.**
- **52 sentences of ≥45 words**; longest in body 82w (§2.2), then 79w (§3.2), 77w (§4), 73w and 72w (§2.3).
- **8 numbered formal objects**: Def 2.1, Lem 2.2, Def 2.3, Def 2.4, Def 2.5, Prop 3.1, Obs 3.2, Prop 4.1.
- **Introduction contains fitted results**: r=1.935, K=1032.7, repeller 144, attractor 889 — all before any estimation is described.
- **The negative result first appears at L47** (highlights) and is not stated plainly in the abstract's opening.
- **Coinage counts:** `declared` 26, `non-retention` 10, `frozen` 10, `retention rule` 7, `scored ladder` 6, `rung` 5.
- Discussion is **2.6× the mean section length** and 22% of the body.

The two journal-limit breaches were found while measuring for this plan. They are
independent of grok and are the most urgent items in it.

---

## 0b. [R2] What was wrong with revision 1

Revision 1 was checked against the source before execution. Four defects:

**D1 — The headline metric was wrong in both operands.** "~11,300 → ~9,000 body words" was
doubly incorrect. The 11,323 figure silently included the abstract, highlights, title block
*and* the 960-word reference list; the true body is **9,830**. And the plan's own itemised
cuts (T2–T6) total roughly **−1,960**, landing near **7,900**, not 9,000. So the plan
understated the reduction it was actually proposing by about 1,100 words while overstating
the starting point by 1,500. A reviewer trusting the summary would have been misled about
how aggressive this pass is. **Corrected target: 9,830 → ~7,900 body words (−20%).**

**D2 — The "Highlights: 533 words" row was a measurement artefact.** It bundled the
abstract into the highlights section because I sliced on section markers without excluding
the `abstract` environment. Highlights are **63 words**; the abstract is **456**. The two
have different journal limits and different owners, so conflating them is not cosmetic.
(The 458 vs 456 discrepancy is `\emph{}`-markup tokenisation; either way it is ~200 over.)

**D3 — "Move to SI" appears five times, but no E1 supplement exists.** Searched: there is
no E1 SI file anywhere in the workspace or repo. §4 already references "Section SI-1"
(qwen flagged this in round 2, item C7-adjacent, and it was never resolved). So T3, T4, T5
and T7 all depend on an artefact that must be *created first*. This is a missing
prerequisite, not a detail — without it "move to SI" means "delete".
**Added as T-SI, which now blocks Stage C.**

**D4 — Renumbering hazard was unassessed.** Deleting Def 2.5 and demoting Def 2.3/Lem 2.2
shifts every subsequent label. Measured cross-reference counts: **Def 2.1 ×5, Def 2.4 ×4
(three of them remote — L1063, L1255, L1596), Def 2.3 ×2**, the rest ×1. Def 2.4's remote
references are load-bearing (they carry the protocol-status disclosure). Renumbering must
therefore be mechanical and verified, not incidental.
**Added to the verification gate as a hard check.**

### And one thing the plan should never have contained: a correctness bug

While auditing T3 I found a **live self-contradiction still in v21**:

- **L839 (§3.2):** Regular et al.'s *M* ≈ 2.5 peak "is **not the same object** as this
  scalar residual, though the two point in the same direction."
- **L971 (§3.3):** "That split **is the same as** the surplus residual after subtracting
  official *C_t*."

These cannot both be true. gpt raised exactly this in round 2 ("Final sentence equating
*M* and the residual … **directly contradicts** your correction in Section 3.2 … Delete
it", audit line 1100). **It never entered my joint evaluation** — I confirmed the §3.2
half in v20 and silently dropped the §3.3 half. `grep` of the evaluation for "equating"
returns nothing, so this was an omission in my audit, not a deferred decision.

This is a **Tier 1 correctness item, not Tier 3.** It is now **T-FIX**, ahead of all
presentation work, and it means my round-2 evaluation was not exhaustive — a caveat that
should attach to any claim that "all surviving Tier 1/2 points are implemented."

---

## Item T-FIX — Resolve the *M*-vs-residual contradiction *(Tier 1, not Tier 3)* **[R2]**

**Priority 0. Do before any presentation work.**

Delete the L971 sentence ("That split is the same as the surplus residual after
subtracting official *C_t*"). §3.2's L839 statement is the correct one and already
survives v20's overclaim pass; the §3.3 sentence is the residual remnant that contradicts it.
Deleting is right — the two objects genuinely differ (an age-structured *M* estimate
informed by tagging and a predictor vs. a scalar one-step residual), and §3.2 already
says so with the appropriate hedge.

**Do not** "reconcile" them by softening §3.2 — that would undo a completed Tier 1 fix.
**Risk:** none, it is a deletion of a false equivalence. **Effort:** one edit.

## Item T-SI — Create the supplement *(prerequisite, blocks Stage C)* **[R2]**

Four items in this plan (T3, T4, T5, T7) move material "to SI", and §4 already cites
"Section SI-1", but **no E1 supplement exists**. Create `E1_SUPPLEMENTARY.md` first, with
the sections the main text will point at:

- **SI-1** pass order (already cited at L1600 — currently a dangling reference)
- **SI-2** Lemma 2.2 statement and proof (from T3)
- **SI-3** HAC grid, block-length grid, the four named DM/bootstrap disagreement rows, script names (from T5)
- **SI-4** floor-binding counts, the 1956 catch-source discrepancy, the 3.6→3.2 kt origin-mix arithmetic (from T4/T7)

Until this exists, "move to SI" is indistinguishable from deletion, and the standing
no-fabrication rule means content cannot simply vanish.
**Risk:** low. **Effort:** 1 pass, but it gates Stage C.

## Item T0 — Abstract to ≤250 words *(NEW — hard journal limit)*

**Priority 1. Blocks submission regardless of anything else.**

Current abstract is 458 words and buries the finding behind protocol description. Cut to
≤250 with this order: question → design → **result in sentence 3** → scope caveat.
grok supplied a usable draft (~200 words); it needs the v20/v21 corrections folded in —
"non-retention" not "negative certificate", the environment-qualified reproducibility
clause, and the H1/H2 distinction (M3 beats M2; M1b sometimes beats M1).

**Retained verbatim:** the 98 vs 115–206 kt and 84 vs 120 kt origin-matched figures, the
1898 kt collapse figure, and the two-series scope sentence.
**Risk:** low. **Effort:** 1 pass.

## Item T1 — Highlights to ≤85 characters *(NEW — hard journal limit)*

Bullets 1 (91) and 4 (105) exceed the limit. Rewrite all five to the ≤85 form, dropping
`scored ladder` and `five-module ladder` per T6. grok's proposed set is already compliant
and is the natural basis.
**Risk:** none. **Effort:** minutes.

## Item T2 — Lead with the result; move fitted numbers out of §1

grok: *"An editor currently has to reach Section 3.1 / Table 4 to learn that persistence
wins."* Confirmed: Table 4 is at L760 of 1,700.

1. State the negative result in the **first 150 words** of §1.
2. **Delete the equilibrium paragraph from the Introduction** (r=1.935, K=1032.7, repeller
   144, attractor 889). These are Results/Discussion objects and Prop 4.1 already carries
   them at L1362. This is grok's ¶4 item and gpt's independently.
3. Keep the scope sentence — grok calls it "one of the best sentences in the paper" —
   and move it directly after the result.
4. Keep the new literature-grounded gap statement from v21 (Hyndman & Koehler; Kell 2016,
   2021; Kokkalis 2024). It is what makes the opening a *contribution* claim rather than
   an assertion, and it postdates grok's review.

**Risk:** medium — §1 is the most-edited region; must not disturb the gap statement or the
locked title/thanks block. **Effort:** 1 focused pass.

## Item T3 — Demote formal apparatus

8 numbered objects is heavy for an empirical forecast comparison. Both grok and gpt
converge here.

| Object | Action | Rationale |
|---|---|---|
| Def 2.1 (map) | **Keep** | grok: "necessary" |
| Lem 2.2 (Schaefer ≠ 𝔰→0) | → one sentence + SI | both auditors; "pedantic for this audience" |
| Def 2.3 (scored ladder) | → prose sentence | replaced by Table 2 |
| Def 2.4 (retention rule) | → prose, keep the rule verbatim | the rule is load-bearing; the *environment* is not |
| Def 2.5 (non-retention) | **Delete** | "not retained" is ordinary English |
| Prop 3.1 | → one sentence, no proof env | both: "true but trivial" |
| Obs 3.2 + profile | **Keep** | grok: "the right level"; carries the v20 G2 reframing |
| Prop 4.1 | Keep claim, **drop proof environment** | keep the v20 A9 scoping (constant catch, [0,S_-), M2 excluded) |

**Constraint:** Def 2.4's actual criteria (H1/H2/H3, 5% band, comparator map) must survive
word-for-word in prose. Demoting the *presentation* must not weaken the *rule*.
**Risk:** medium-high — this is where an over-zealous cut could damage a real commitment.
**Effort:** 2 passes with a diff review.

## Item T4 — Discussion 2,511 → ~1,500

Largest single win. Keep: Prop 4.1 claim, the catch-drop paragraph, the H1/H2 distinction,
the delay decomposition **with its matched-origin numbers and caveats in the same
paragraph** (v20 A4/G5), Rose 2026 corroboration, attribution-vs-forecast-module point,
the protocol disclosure (once, short).
Compress to a single limitations paragraph: predictand, persistence-as-benchmark,
recreational catch, log-floor, sample size. Floor-binding counts (15/25, 17/25, 19/21) → SI.
**Risk:** low-medium. **Effort:** 2 passes.

## Item T5 — §3.5 to one paragraph + Table 9

998 words for uncertainty is "a paper inside the paper" (grok). Main text keeps: Spec A
within noise (n=25/21); Spec B intervals exclude zero; DM bandwidth-fragile both ways
(v21 C3) so the reading rests on the bootstrap; no comparator change flips a verdict;
Spec A rows are the annual-landings pass.
To SI: the HAC grid, the block-length grid, the script name, and the four named
disagreement rows (keep the **corrected** "four of the twenty-eight" count — v20 A1/A2).
**Keep verbatim:** *"Read 'within noise' as 'this analysis does not resolve the
difference', not as evidence that the models are equivalent."* Both grok and I flag this
as one of the best sentences in the paper.
**Risk:** low. **Effort:** 1 pass.

## Item T6 — Coinage reduction

Not a blanket purge — the scanner already enforces the register rules, and `non-retention`
is now a *defined* term doing real work (v20 A5 removed "negative certificate" in its
favour). Targets, in order:
- `declared` (26) — the worst offender; most uses are filler. Cut to ≤8.
- `scored ladder` (6) / `rung` (5) → "the models tested", "the comparison set". Define once.
- `frozen` (10) — keep where it names the real frozen-spec commitment; cut decorative uses.
- `non-retention` (10) — **keep**; defined and load-bearing. Reduce repetition only.
- `protocol status` (2) — keep as a heading, it is an honest disclosure.

**Risk:** low, but must not touch frozen-spec language that encodes a real commitment.
**Effort:** 1 pass + scanner re-run.

## Item T7 — Sentence splitting

52 sentences ≥45 words. Do **not** mechanically split all 52. Target the 18 at ≥59 words,
concentrated in §2.2 (L282, L288, L366), §2.3 (L469, L480, L533, L541), §3.2 (L702, L757),
§3.4 (L880, L892), §4 (L1178, L1198, L1209, L1235).
Note L366 (82w) and L288 (64w) are the **new** G4/A7 bounds-and-recursion sentences from
v20 — dense by necessity, but they should be broken into a short list.
The 123-word "sentence" at L32 is the highlights block, handled by T1.
**Risk:** low. **Effort:** 1 pass.

## Item T8 — Matched baselines into the primary tables

gpt §1.5, overlapping grok §3.4. v21 already fixed the Table 8 caption so bold marks the
matched comparison. Remaining: promote origin-matched persistence into Tables 6–8 as the
primary column and demote all-origin baselines to an audit table.
**Risk:** medium — touches numbers' *placement*. Every value must be reproduced from
`rolling_forecasts.csv` / `xte_rolling_forecasts.csv`, not retyped.
**Effort:** 2 passes with recomputation.

---

## Sequencing **[R2 — revised]**

**Stage 0 — correctness + prerequisite:** **T-FIX**, then **T-SI**.
T-FIX is a Tier 1 bug and must not ride along inside a presentation diff. T-SI must exist
before anything is "moved" to it.

**Stage A — journal compliance (independently shippable):** T0, T1.
Fixes two hard violations. Small, self-contained.

**Stage B — first-page rewrite:** T2, then T6 (coinages are densest in §1–§2).

**Stage C — apparatus and bulk:** T3, T4, T5. **Blocked by T-SI.**

**Stage D — line level and tables:** T7, T8.

Each stage = one new version file (v22…v25), never edited in place, each compiled and
scanned before the next. Rationale: T3 and T4 are where an over-aggressive cut could
delete a real commitment, so they should land on top of a stable, already-verified base
rather than being mixed into the same diff as the abstract rewrite.

## Verification gate (every stage)

1. `manuscript_style_scan.py` → **0 blockers**.
2. Tectonic compile from `paper rewrites/` (**not** `latex/` — figures resolve against source).
3. Locks: title, `\thanks{Data vintages...}` author block, no `\citep{}`, no "in review",
   no "negative certificate".
4. **Numeric invariance:** every RMSE, p-value, count and parameter identical to v21.
   Diff the extracted number set; a Tier 3 pass that changes a digit has failed.
   *(Exception: T-FIX deletes a sentence containing no numerals; T8 relocates values and
   must recompute them from the archived CSVs rather than retyping.)*
5. Retention verdict unchanged: persistence wins both specifications, both horizons.
6. **[R2] Cross-reference integrity.** After any renumbering, every `Definition N.M`,
   `Lemma`, `Proposition`, `Observation` and `Section SI-N` string must resolve to an
   object that exists. Baseline counts to preserve: Def 2.1 ×5, Def 2.4 ×4 (three remote:
   L1063, L1255, L1596), Def 2.3 ×2, others ×1. Script this check; do not eyeball it.
7. **[R2] No content evaporation.** Anything the diff removes from the main text must be
   present in `E1_SUPPLEMENTARY.md`. Verify by string search, not by intention.

## Explicitly out of scope

- **gpt's new-comparator proposal** (regularized AR / local-trend) — new rung on a frozen
  ladder; needs a `SPECIFICATION_v3.md`, not an editing pass.
- **Re-running any scoring.** Tier 3 is text only. The one exception is T8, which
  *relocates* already-archived numbers and must recompute rather than retype them.
- **grok's advice to restore "in review"** — contradicts standing policy; companions are
  cited by DOI.
- Anything in the audit's rejected set (H1–H4, B1–B4).

## Expected outcome **[R2 — corrected]**

**Body 9,830 → ~7,900 words (−20%)**, not the "11,300 → 9,000" claimed in revision 1.
Abstract 456 → ≤250. Highlights ≤85 characters each. 8 numbered objects → 3. Longest
sentence <45 words. Result visible in the first 150 words. Plus one Tier 1 correctness
fix (T-FIX) and one new artefact (`E1_SUPPLEMENTARY.md`).

No scientific content removed — the apparatus moves to SI, the numbers stay put.

**Honest caveat:** −20% of the body is a substantial rewrite, not a copy-edit. Stage C in
particular rewrites the two longest sections. The staged sequencing exists so that each
step is separately verifiable and revertible; if the Discussion cut starts to bite into
substance rather than repetition, stopping after Stage B still leaves the paper
submission-compliant and materially better than v21.
