# ECOMOD series audit — best prose, and what was altered against itself (2026-11-13)

Scope: all 36 unique ECOMOD `.tex` blobs on `main` and 7 other branches (`ecomod-v45-*`, `post-agent-mistake`,
`workspace-recovery-2026-10-24`, `archive/ecomod-companion-restorations-2026-10-26`,
`agent/p06-ecomod-c11-local-draft-20261028`). Saved in `series_audit/files/` with `index.json`.
Versions cover v30–v44, `ecomod_continued_2–10`, C14–C20, and the v45 recovered artifacts.

---

## 1. Best prose

**v41 and v42 are the two best-written manuscripts in the series, and they are good in different ways.**

| Candidate | What it is | Why it is the best |
|---|---|---|
| **v41** | 16-section technical manuscript, 124,430 B, 1,953-word introduction | The fullest and clearest *explanation*. The orchard is built in three concrete steps (two kinds of ground → the arithmetic of a productive stock → the hen). The elevator is attributed and makes a two-sided judgement: "judged by what it delivers the elevator still runs; judged by its reserve it is already failing." No hedging scaffold. |
| **v42** | 6-section research article, 81,103 B, 898-word introduction | The clearest *argument*. Introduction asks Q1–Q3 explicitly, states one contribution with three parts, and closes each claim with what would falsify it. Abstract is the most legible in the series (Flesch 20.4, ASL 26.4, 0 apologies). |

Readability of the introduction (computed, not impression):

| Version | Words | Avg sentence | Flesch | Apologies/1k words |
|---|---|---|---|---|
| v30 | 1,100 | 24.4 | 32.8 | 0.20 |
| v33 | 1,122 | 21.6 | **34.7** | 0.16 |
| v35/v41 | 1,925 / 1,953 | 25.0 / 25.4 | 30.5 / 30.4 | 0.13 / 0.12 |
| **v42** | 898 | 26.4 | 20.4 | **0.00** |
| v44 | 928 | 26.5 | **17.4** | 0.00 |
| **C20 (in submission)** | 789 | 19.7 | **18.6** | **0.34** |

The last row is the finding that matters: **the version going to EM is the least readable introduction in
the series by Flesch, and carries the highest apology rate** — 2.8× v42/v44 and 3× v30 — while being the
*shortest*. It lost words, lost the pictures, and gained disclaimers.

## 2. The one clearly perverse directive: C-series line-editing

`ecomod_continued_4` is generated from `.../S. Ghosh/agent/...` — a line-edit pass. From C10 onward
($\rightarrow$ C17 $\rightarrow$ C18 $\rightarrow$ C19 $\rightarrow$ C20) the lineage is a
line-edited chain, not an authorial one. Effects, measured:

| | v41/v42/v44 | C17–C20 | Change |
|---|---|---|---|
| Hedges / 1,000 words | 0.3–0.5 | **1.1** | **×2–3 worse** |
| "not an empirical claim / does not assert / not evidence that" | 0–1 | **3–4 per document** | **introduced** |
| Abstract 4-decimal numbers | 0 | **2** (`0.547925`, `0.231310`) | **introduced** |
| Abstract: "composition" | present | **absent** | **dropped** |
| Abstract: "identifiability" | v35–v42 present | **absent** | **dropped** |
| Introduction: Q1/Q2/Q3 | present (v42) | **removed** | **dropped** |

### (a) Numbers raised into the abstract
The abstract now reads *"conversion contributes 0.547925 gha, while the net account increase is 0.231310 gha."*
Six significant figures in an abstract, for a decomposition of a representative simulation. No version
before the C-series does this; v41/v42/v44 abstracts contain **zero** 4-decimal tokens. This is precision
inflation: it makes a conditional illustration look like a measurement, which is the opposite of what the
paper's own epistemic stance asks for.

### (b) The paper's own finding deleted from its abstract
Every v35–v42 abstract names the result: *"the aggregate does not identify its own composition"* and
*"these results establish an identifiability property."* **C17 and C20 say neither.** The abstract now
describes the model's mechanics (39 %, ≈46 %, 51.72 %, budgets) and never states the identifiability
result the title's thesis rests on. The composition claim survives only as "aggregate annual account",
which is inert.

### (c) The questions demoted
v42's introduction is built on (Q1)(Q2)(Q3). C-series replaced this with an "Objectives" paragraph and the
nested `\paragraph{...}` register — the research questions survive as prose, not as questions.

## 3. Two further renamings (judgement calls, not corruption)

- **Title**: v35–v44 = *"How aggregation can conceal composition: aggregate biocapacity and the
  identifiability of modelled ecological-capital drawdown"*. C-series = *"A rising biocapacity total can
  mask ecological-capital land drawdown: a two-land model."* The C-title is shorter and more readable but
  drops **"identifiability"**, which is the paper's actual contribution. The change was deliberate
  (`revision_audit_20261029`), and it is arguable — but it is a *loss of claim*, not a gain.
- **Keywords**: v30–v41 carried *"critical slowing down"*; the C-series does not. That is arguably correct
  (the CSD result is a negative structural statement, so advertising it as a keyword invites
  misreading) — recorded as a judgement, not a defect.

## 4. What was *not* perverted — checked, negative results

Worth stating so the audit is not read as "everything degraded":

- **The closing orchard callback survived intact.** "A harvest total is not a census of the orchard" is
  present in C10, C17, C18, C19, C20 — in fact **it is better in C20 than in v41**, where the closing
  paragraph is missing entirely.
- **The exact 46.16 % figure survived.** C10 carries it 3×, C17 2×, C20 1× (in §3.1; the abstract's
  "approximately 46 %" is a separate, older occurrence).
- **The negative-result structure held.** C17/C20 Discussion keeps the "What is not claimed" discipline —
  the one-stock comparator, the no-fold result, the exclusion of the Hopf classification from two-land
  claims. v41 has the same in table form. This is the hardest thing to preserve across rewrites and it
  was preserved.
- **No paraphrase-apology inflation**: the phrase "not an empirical claim" appears **0** times in any
  version; the apologies are of the "does not assert / not evidence that" family and are confined to the
  C-series introduction and discussion.

## 5. Where the readable prose is, ranked

1. **v42** — best *argument*: questions first, one contribution, falsification built in. Best abstract.
2. **v41** — best *explanation*: the orchard/hen/elevator sequence, in full, in your voice. Best §1 prose.
3. **v44** — tightest abstract (221 words, no flab), but its introduction has already compressed the
   orchard to one paragraph and lost the hen.
4. **v33** — highest raw Flesch, but the elevator and the base-arithmetic paragraph were already cut there;
   readable is not the same as complete.
5. **C20** — the weakest introduction in the series by every measure taken here.

## 6. Recommendation

The paper in submission is not the best text the programme produced, and the regression is traceable to
one mechanism: a C-series line-edit that (i) added hedging, (ii) hoisted six-figure decimals into the
abstract, and (iii) deleted the identifiability result and the questions from the front matter.

Minimum-fix list, in order of defensibility, none of which touches a number, a claim, or the layout:

1. **Restore the identifiability sentence to the abstract.** One clause. It is the paper's own result and
   it is currently absent from the abstract in every C-version.
2. **Drop the six-decimal figures from the abstract**, keeping them in §3.6 where the budget lives
   ("about 0.548 gha" is sufficient).
3. **Restore v41's orchard/hen/elevator paragraphs** to §1 (as recommended earlier).
4. **Restore (Q1)(Q2)(Q3)** as the questions register, if you want the v42 argumentative shape.

Items 1–2 are abstract edits, so they collide with the "do not touch content" rule — which is exactly why
they are listed as proposals and not applied. Your call on all four.
