# Content-Loss / Condensation Audit — v33 → v34

**Scope:** line-level, normalized (whitespace-insensitive) diff of the manuscript as it
transitioned from `manuscript_ECOMOD_v33.tex` (prior, complete) to
`manuscript_ECOMOD_v34.tex` (editorially cleaned). Verdict: **NO accidental content loss.**
The only content that was removed or condensed is the change-log / self-referential /
informal-chat language that the editorial task (Task A) was explicitly instructed to strip.

## 1. Structural facts

| Metric | v33 | v34 | Δ |
|---|---|---|---|
| Lines | 702 | 702 | 0 |
| Word tokens | 12,634 | 12,497 | −137 (−1.1 %) |
| Characters | 98,152 | 97,139 | −1,013 (−1.0 %) |
| Whole lines deleted (diff opcode `delete`) | — | 0 | — |
| Whole lines inserted (diff opcode `insert`) | — | 0 | — |
| Sequence-similarity ratio (word-level) | — | — | 0.9744 |

Every one of the 24 changes is a **`replace` on an equal-length span** — no line, equation,
citation, label, or paragraph was wholly deleted or added. The −1.0 % character delta
corresponds exactly to the removed change-log phrases.

## 2. Loss-free invariants (identical occurrence counts v33 vs v34)

Automated cross-check confirmed the following appear the **same number of times** in both
files (no silent deletion anywhere):

- `\cite{...}` — 0 / 0 (no inline citations in source; references are a BibTeX/`\bibitem` block)
- `\label{...}` — 5 / 5  (tab:regime, tab:conv, tab:basin, tab:neg, tab:ladder)
- `\ref{...}` — 5 / 5  (all 5 table labels referenced)
- `\S` cross-references — 7 / 7
- math `\frac{...}{...}` — 16 / 16
- `\tau_{\mathrm{conv}}` — 12 / 12
- `b_{c,\mathrm{eff}}` — 21 / 21
- `\Delta b_{\mathrm{conv}}` — 23 / 23
- `A_c^{\min}` — 13 / 13
- `q_{\max}/2` — 5 / 5

Distinctive numeric quantities checked and present in v34: `0.758, 1.138, 0.0537, 0.8333,
0.016, 0.32, 1.110, 0.626, 0.385, 0.143, 0.070, 2.41, 2.98, 3.14, 1.21, 5.39, 0.414, 0.784,
0.79, 0.54, 0.52, 0.50`.

## 3. The 24 changes, categorized

All changes are either (a) pure editorial removals of change-log / self-referential /
self-praise / informal-chat language, or (b) 1:1 rewrites to present-tense, formal phrasing
with **no loss of scientific substance.**

### 3a. Comment-only / metadata (1)
- v33 lines 5–6: removed "Follows v32 preamble (error-free).", "Scope-A revision: two-land
  conversion model. Minimal-edit path (v32 section map)." → "Two-land conversion model."

### 3b. Pure change-log / self-commentary removed (substance retained or restated)
- **L64** (intro conclusions): "not an accident of parameter choice" → "not an artefact of one
  parameter set"; "The message is therefore cautionary, but it names the levers precisely" →
  "The model distinguishes what is structural from what is conditional"; "The paper remains"
  → "It is". Scope statement (stylised illustration, not calibrated forecast) **retained**.
- **L152** (two conventions): "The consequence for honesty is explicit" → "The consequence is
  that"; "This is deliberately minimal" → "This is deliberate".
- **L181** (conversion-rate bullet): removed "(A previous version omitted the time constant and
  thereby put a ha stock into a ha·yr⁻¹ equation directly; that incoherence is removed here.)".
  The correct rate and its time constant remain fully specified.
- **L244** (no-conversion face): "which the old (no-maintenance) formulation could not support"
  → "supported by the maintenance term"; "This corrects both the deferred one-stock result and
  the old two-land ... pathology" → "are properties of a single-stock comparator ... neither
  holds under the quality-based two-land model". All mathematical content retained.
- **L250** (equilibria): "(the old two-branch merge did not survive the corrected operator)"
  → removed; "absent under the corrected operator" → "absent". Verified saddle-node absence
  and critical-slowing content retained.
- **L287** (collapse transition bullet): "Under the corrected model" → "The"; "old 'critical
  slowing at the fold' does not survive the corrected operator" → removed (claim restated
  directly).
- **L306** (prediction 3): "under the corrected operator" → removed (claim restated directly).
- **L334–336** (numerics): "With corrected model" → "For"; "larger than the old claim (which had
  P₀≲1.10)" → "raising these thresholds"; "The no-CSD negative result is confirmed. Under the
  corrected operator" → "The no-CSD negative result. The"; "the 'one-stock no CSD / no τ_g
  cliff' result transfers ... only in the sense that CSD is also absent here" → "Critical
  slowing down is also absent under a single-stock comparator, but the two results are
  established independently; the two-land model is not a reduction of the one-stock case."
  All eigenvalue values (−0.0537 yr⁻¹, −0.08) and definitions retained; the single-stock
  comparison is actually restated more precisely.
- **L394–396** (basin caption): "Note the thresholds are larger than the old (superseded)
  values, because the ... buffer the shortfall; the direction — lower capital has less headroom
  — is unchanged" → "The ... buffer the shortfall, so these thresholds exceed those of a model
  without a maintenance term." Direction of the monotonicity retained (also stated in the text).
- **L555**: "again, as a proxy" → "as a proxy".
- **L618**: "The strongest honest empirical claim." → "The empirical claim."
- **L620–622**: "We do not claim the proxies solve ...; we claim they turn ... into" →
  "The proxies do not solve ...; they make ...". Scope of the identification claim retained.

### 3c. Change-log → live formulation-contrast rewrites (substance fully retained)
- **L210** (capacity max scope): "re-derived below" → "derived directly"; "corrected operator"
  → "quality-based formulation".
- **L218** (capacity maximum): "(Under the old area-based operator, G_c was a function of A_c
  and the 'capacity maximum' A_c* and the condition b_G,c ρ_c > b_c were properties of that
  A_c-shaped read; in the corrected model the corresponding Y_c'(A_c)=0 statement has no
  analogue, because Y_c is linear in A_c at fixed q.)" → "(Under an area-based formulation in
  which G_c is a function of A_c, the per-hectare value would be quadratic in area and the
  condition b_G,c ρ_c > b_c would define an 'area capacity maximum' A_c*; under the
  quality-based formulation adopted here Y_c is linear in A_c at fixed q, so the corresponding
  Y_c'(A_c)=0 statement has no analogue.)" — mathematically identical; only the "was a property
  of that old read" framing became a "would be / is" formulation contrast.
- **L233–238** (tab:regime caption): "under the corrected model" → "under the quality-based
  model"; "the old b_G,c ρ_c vs. b_c shape-regime split ... is superseded" → "the shape-regime
  split of an area-based form ... does not arise, because"; "The demand ceiling and its
  structure are re-derived" → "derived". Same content, present-tense.
- **L258** (conversion-loop subsection): "the honest replacement for a universal stability
  index" → "a state- and parameter-dependent stability contrast".
- **L340**: "(the honest replacement for a universal index)" → removed.
- **L363, L391** (two captions): "under the corrected model" → "in the quality-based model".

### 3d. Conclusion and terminology (substance retained, warts tightened)
- **L640** (conclusions): "a sharp, policy-relevant conclusion ... in three ways" → "a
  conclusion ... in three respects"; "The productivity illusion" → "The composition illusion"
  (aligns with the paper title); "In one sentence:" removed; and the trailing rhetorical clause
  "so the question is not whether the index rises, but whether the trees are still standing"
  removed. The **orchard metaphor itself is fully retained** (now as plain text, not \emph):
  "A modern economy can run for decades on a harvest that looks healthy while the orchard behind
  it quietly shrinks, because the unit in which capacity is measured already mixes the fruit
  with the trees." v34 adds a clarifying "and" ("real, bounded, and demand-driven").

## 4. Terminology discipline (concept → term mapping)

Applied rule: **identical concepts take one consistent term; slightly different concepts, or
general-vs-special, take distinguished terms.** The manuscript v34 satisfies this:

| Concept | Role | Term | Count |
|---|---|---|---|
| General folk misreading (a rising/steady capacity implies health) | general class | productivity illusion | 2 |
| Special result: two-book conversion makes `B` rise while `A_c` falls | named/special | composition illusion | 6 (+ title, keywords) |
| The observable pattern (aggregate rises, component falls) | phenomenon | composition effect | 4 |
| The causal process (`Δb_conv > 0` conversion loop) | mechanism | composition mechanism | 10 |
| The concealing device (vs. liquidation mask) | device | composition mask | 1 (defined) |

- **productivity illusion vs composition illusion are general vs special and MUST stay
  distinguished.** They are; the manuscript states this explicitly (L474–475: "The term is
  deliberately *composition* illusion here … which paper3 frames as the yield-inflation sense
  of its 'productivity illusion.'"). **Do not merge.**
- "effect" (phenomenon), "mechanism" (process), "illusion" (named result), and "mask" (device)
  are four genuinely distinct concepts and are each used consistently for their own concept —
  they should not be collapsed into one term either.
- **Fix applied:** SI v2 §S4.2 (one-stock comparator regime table) used bare "illusion small /
  illusion more visible". A one-stock comparator has **no composition** and cannot produce the
  *composition* illusion. The manuscript consistently calls the one-stock concealment a
  "mask" (e.g. L684 `5.4 yr mask`), reserving "illusion" for the two-land composition case.
  The SI cells were changed to "masking weak / masking more visible".

## 5. Notes / items to be aware of (not defects)

- No whole-line deletions and no numeric/citation/label loss. All five table labels remain
  referenced. The v34 file structure (sections/equations) is untouched apart from these edits.

**Conclusion:** the −1.0 % word/character reduction is entirely attributable to the removal of
change-log, self-referential, self-praise, and informal-chat phrasing. No legitimate
scientific or expository content was lost or condensed. Terminology satisfies the
identical-concept/distinct-concept rule; the only cross-concept leak found (SI one-stock
"illusion") was corrected to "masking".
