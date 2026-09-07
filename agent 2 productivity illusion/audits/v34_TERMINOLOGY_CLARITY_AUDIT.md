# v34 Terminology & Line-Level Clarity Audit

Audit record for the three-part directive applied to `manuscript_ECOMOD_v34.tex`
and `supplementary/SUPPLEMENTARY_information_v2.md`. Companion to
`v33_vs_v34_CONTENT_LOSS_AUDIT.md` (diff audit, complete, no loss) and the prior
terminology-semantics audit (terms correctly distinguished).

---

## (1) Abstract self-contained — CONFIRMED CLEAN

Read the `abstract` environment in full. It contains **none** of
`\cite`, `\ref`, `\label`, `\S`, "et al.", a Figure/Table/Eq. pointer, or a "see
paper/§" construction. "National Footprint and Biocapacity Accounts (world, 2025)"
is inline data attribution (a data source named in prose), not a citation-style
reference, so it is compatible with the self-contained requirement.

No edits applied (already compliant).

---

## (2) Term elegance + cross-reference — DECISION APPLIED

**Constraint.** Any rename must not collide with the manuscript's established
"aggregation" machinery (8 occurrences, all in distinct, already-defined senses:
"aggregation face of the composition effect" L45; "aggregation theorem (Prop 1)"
L324; "no-nonnegative-weighting aggregation obstruction" L324/L466; "aggregation
relative to the typed floor" L408; "compensatory-aggregation gap" L415;
"aggregation face of the masking result" L513/L640).

**Literature check.** No established term was found. "Composition effect" in
environmental economics refers to the *mix of goods in the economy's output* (a
different, established sense); "composite index" is a methodology term. So
"composition illusion" is a coinage. "Aggregation bias", "negative footprint
illusion", and "ecological fallacy" were ruled out (collision / wrong phenomenon).

**Decision (user).** Retain **"composition illusion"** as headline, and add a
one-line gloss at first body use. Rationale: it bridges the companion paper3's
"productivity illusion" (the yield-inflation sense, per L474–475), and keeps
coherence with the manuscript's own ~90-occurrence "composition *" mechanism
family (composition effect / mechanism / condition / diagnostic / step / window /
mask), which a headline rename would otherwise orphan.

**Applied.**
- Added a one-line definitional back-link at the §4.4 opening (subsec. "The
  composition illusion and the macro-ratio safe operating space"), which both
  back-references the Introduction's general "productivity illusion" and glosses
  the special term: *"This is the special two-land sense of the productivity
  illusion introduced in the Introduction: here the aggregate rises because
  converting ecological capital into provisioning land inflates current
  accounting capacity (the yield-inflation sense) — a rising aggregate index
  built on a shrinking ecological base — rather than because the orchard is
  healthier."* (L277)
- No forward-link at the Introduction was added (user chose back-link at §4.4
  only).
- The general "productivity illusion" definition at L58 is unchanged.

---

## (3) Deep line-level scan — FINDINGS + FIXES

Meta-commentary / internal-dialogue scan: **clean.** No change-log, "old
operator", "earlier/previous claim", "note that / as discussed / we now", or
self-commentary anywhere in the body. Only two legitimate technical headings
("Residual caveat", "share caveat"). Six legitimate "illustrative" modelling-scope
statements retained.

### (3a) §Presentation — genuine redundancy — FIXED

The "Feedback diagram" bullet (L319) gave the conversion chain
`A_c↓→A_f↑→B↑(if b_f>b_c,eff)→K↑→P↑→S↑→A_c↓`; the following "Two positive-feedback
loops" bullet restated the identical chain as "Loop 1 (conversion/stock-
liquidation)". **Fix applied:** the second bullet now names Loop 1 by reference
(the feedback-diagram loop) and presents only Loop 2 (debt-erosion of the flow
yield, `D↑→b_f↓→B↓→deficit↑→D↑`) as new content, while preserving the "distinct /
can reinforce" point and the reason the mask is bounded.

### (3b) Recovery-metric notation clash — FIXED (manuscript) + UNIFIED (SI)

Manuscript used `\mathcal{R}_c` for the recovery metric (L461, 4×) but also wrote
`R_c=1` in the same sentence for the **same** quantity, and the SI §S5.4 (and the
manuscript's SI pointer L685) used plain `R_c`. The symbol table had no row for
either form (unlike `R_rc`/`R_fc`/`R_B`/`R_A`).

**Applied (per user decision: unify to `\mathcal{R}_c` everywhere).**
- `\mathcal{R}_c` is preferred over plain `R_c` because it stays distinct from the
  restoration flows `R_rc` and `R_fc`, and from `R_B`/`R_A`.
- L461: `$R_c=1$ recovery` → `$\mathcal{R}_c=1$ recovery` (removed the
  intra-sentence contradiction).
- Symbol table (Variables & units): added row
  `$\mathcal{R}_c$ | capital-land recovery metric =(A_c(T)-A_c^deg)/(A_c^init-A_c^deg) | dimensionless | derived`,
  placed with the `R`-family rows.
- L685 SI pointer: `recovery metric $R_c(T)$` → `$\mathcal{R}_c(T)$`.
- SI §S5.4: replaced all 15 occurrences of `R_c` with `\mathcal{R}_c` (using the
  SI's established backtick-monospace symbol convention; no `$...$` math delimiters
  introduced elsewhere in the file).

**Post-edit verification.** Manuscript: `\mathcal{R}_c` 8×, 0 bare `R_c`. SI:
0 bare `R_c`, 15× `\mathcal{R}_c`. LaTeX environment balance: no unbalanced
environment. (No LaTeX engine is installed in the workspace, so compilation was
not run; structural checks passed.)

### (3c) Other sections (§§2–6)

No other genuine redundancy or remnant found. Repeated emphasis of the
"not a universal +0.62", `≈−0.0537 yr⁻¹`, and the
`d ln B = d ln(B/P) + d ln P` split across Abstract/§Discussion/§Conclusions is
intentional abstract-vs-body restatement, not accidental duplication. §4.4,
§Results, §Falsifiable predictions, §Model scope, §Discussion, §Limitations and
§Conclusions read cleanly.

---

## Terminology map (unchanged, re-confirmed)

productivity illusion 2× (general/folk) · composition illusion (special, two-land
= headline) · composition effect 4× (observable phenomenon) · composition
mechanism 10× (causal loop) · composition diagnostic 11× (Δb_conv) · composition
condition 2× · composition step 6× · composition window 2× · composition mask vs
liquidation mask (distinguished) · masking signal 1× · aggregate mask 2× ·
compensatory-aggregation gap 1×. No single term carries two concepts; no concept
has two names.

---

## Round 2 — first-appearance definitions, cross-section alignment, title

### Task 2: terms defined/explained on first appearance
- Core quantities are defined in the Introduction at first appearance: carrying
  capacity, biocapacity, global hectare (gha), natural capital, land-use
  conversion, "productivity illusion" (L58), and "composition of biocapacity"
  (explicit em-dash gloss, L60).
- Coinages that first appear in the abstract/Intro (composition effect,
  aggregation face, typed floor, floor collision, gate sign, composition-loop
  gain) are standard, explained by immediate contrast (floor collision ↔
  saddle-node), or defined at first body use (typed floor in Assumptions #10;
  gate sign in §Recovery dynamics; composition diagnostic in §4.3).
- Headline "composition illusion" is first glossed/defined at §4.4 (its first
  body use) via the Round-1 back-link sentence. Title/keywords use is a label.
- **Verdict:** adequate; no further definition edits required.

### Task 3: do Abstract / Introduction / Discussion / Conclusions fully align?
- **Substantively consistent on every number and claim:** biocapacity +≈23% ↔
  +23.0%; per-capita −364%, population +464% of d ln B; overshoot onset 1971;
  E_ceil≈1.138; leading eigenvalue ≈−0.0537 yr⁻¹; floor collision (not fold);
  no critical slowing down; demand-driven drawdown; recovery gate-sign;
  identifiability; "real, bounded, demand-driven … separated from a
  non-identifiable single-stock reading."
- **FIX APPLIED:** abstract now reads "the *aggregation* face of the **masking
  result**" (was "of the **composition effect**"), matching Discussion and
  Conclusions, which explicitly separate the per-capita/population split from
  the two-land composition illusion. "composition effect" remains once in the
  abstract as the correct closing summary.
- **Optional nit:** abstract leaves "composition-loop gain", "typed floor",
  "gate sign" unglossed — acceptable for abstract brevity.

### Task 4: does the title merit improvement?
- **Current:** "Emergent Carrying Capacity, the Biocapacity Ratio, and the
  Composition Illusion: Two-Land Conversion and the Identifiability of Collapse"
- **Strengths:** names the central novel concepts (emergent carrying capacity,
  composition illusion) and two contributions (two-land conversion, identifiability
  of collapse); "Composition Illusion" is a memorable headline.
- **Weaknesses:** list-heavy (3 main + 2 subtitle = five claims); "the Biocapacity
  Ratio" (R_B) is the weakest element — a defined monitoring quantity, not a
  conceptual headline; subtitle "Two-Land Conversion" overlaps the composition-
  illusion theme.
- **Options:** (A) drop "the Biocapacity Ratio" → "Emergent Carrying Capacity and
  the Composition Illusion: Two-Land Conversion and the Identifiability of
  Collapse"; (B) front-load the hook → "The Composition Illusion: Emergent
  Carrying Capacity, Two-Land Conversion, and the Identifiability of Collapse";
  (C) retain as-is.
- **Ripple if changed:** manuscript `\title`, `\hypersetup{pdftitle=…}`, the SI
  header line, and the comment header — no body use of the title string.
- **Verdict:** competent and consistent; only a light tightening worth doing if
  desired; not wrong as-is.

---

## Git sync (Round 2)

Pushed to `MIKEAA2020/general-sustainability` `main` (subdir `agent 2
productivity illusion`):
- `84a39ef` — "ECOMOD v33->v34: terminology & clarity pass, plus prior-round
  artifacts" (added v33/v34, SI v2, latest audits/, model_sims/, data/nfa/).
- `89b7e9a` — "v34: align abstract with Discussion/Conclusions" (abstract
  "aggregation face" → masking result).

Token read from `.github_pat` (never printed); used via `http.extraHeader` for
push, then scrubbed from the clone config; the clone lives in `/tmp` (outside the
workspace snapshot).
