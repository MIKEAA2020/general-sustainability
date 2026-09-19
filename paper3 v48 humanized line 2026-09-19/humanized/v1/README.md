# `paper3` humanized — v1 (hybrid, de-jargoned for a broad audience)

**Built:** 2026-09-14 · **Source of truth:** `uploads/paper3_material_ledgers_v32.pdf` → `work/paper3.txt` (137,046 chars, 40 pp) · **Nothing in `work/` or `uploads/` was modified.** This is a new version, kept separate from every earlier file.

## What this version is

A complete plain-language rendering of **all eleven sections plus front matter, back matter and the reference list**, produced by the hybrid recipe agreed in `review/joint_evaluation_v1.md` §6, with the emphasis you set: clarity and accessibility for a broad human audience, de-jargoned into everyday words.

| Part | Covers |
|---|---|
| `part_01_front_matter_and_s1.md` | title/author block, reading guide + status legend, abstract (plain **and** author's own text), §1.1–1.3 |
| `part_02_s2_typed_ledger.md` | notation table, §2.1–2.6 (eqs. (1)–(2), both incidence matrices, the three recharge laws, ψ assignments, Theorem 1 + Remark 2) |
| `part_03_s3_certification.md` | §3.1–3.6 (numbering note, Props. 1–2, safety set, Lemma 3, Prop. 4, Theorem 5 + corollary + worked envelope, Prop. 6, counterexample, "Depletion is compartmental") |
| `part_04_s4_s5.md` | §4.1–4.9 (Theorems 7–15 incl. both proofs in full, the 7×10 incidence, "cancellation is cheap", closed-ledger portrait) and §5.1–5.4 (Defs. 1–2, Remark 16, decline pressure) |
| `part_05_s6_depletion_arithmetic.md` | §6.1–6.5.4 (Defs. 3–5, Prop. 17, exit times/maintainability, robust semantics, classification matrix, all three applied tables incl. the quarantine note, Non-example 1, fisheries disclosures) |
| `part_06_s7_first_passage.md` | §7.1–7.8 (Defs. 6, Props. 18/20 + Cor. 19 with proofs, record-relative barrier, three boundary facts, seven non-claims, uncertainty) |
| `part_07_s8_s9_interface.md` | §8.1–8.3 and §9 in full (interface contract, shared object, hand-off projection, five non-reduction reasons, non-reduction theorem, frozen-donor limit, long-time budget) |
| `part_08_s10_s11_and_backmatter.md` | §10.1–10.4 (both no-certification results **with proofs**), §11, supplementary pointer, Declarations |
| `part_09_references.md` | reference list carried unchanged + the 7 DOI links + the two back-matter items the author must settle |

Assembly order is the table order. To make one file: `cat part_0{1..9}*.md > paper3_humanized_v1_full.md`.

## The rules the rendering obeyed

1. **Status-bearing sentences are copied in substance, never re-framed.** Registered / illustrative / quarantined / established / non-example / banned, and the guard clauses ("declared, not computed", "must not be reused", "must not be taken at face value", "routing is never determined by diagnostic labels", "Banned unless donor-limited", "the tax moves the economic equilibrium, but it does not move the physical floor") survive verbatim in meaning and mostly verbatim in wording.
2. **Jargon is translated, not deleted.** Every term gets an everyday gloss at first use ("moiety = the conserved substance class a conservation law attaches to"; "support pool = a stock that receives the current draw and is not renewed as fast"; "donor-limited = a flow can only take out what its source holds"; "barrier = a declared line the reading must stay between").
3. **Nothing is added to the author's claims.** Two `[Editor's note — flagged for the author, not their claim]` blockquotes exist (abstract↔Lemma 3 direction; the transposed-`Sᵀ` notation hazard elsewhere handled by writing `S^{\top}` throughout) and both are marked. No new numbers are derived: Non-example 1 stops at `0.130 yr⁻¹`, and its reciprocal is explicitly *not* turned into a horizon — the mistake the Gemini version made.
4. **Every number, table and proof is carried.** The 40-page extraction's three tables, both incidence matrices, and all 12 proof environments appear, not summarized.
5. **Sentences were split mechanically.** Mean prose sentence length is now **22.5 words** (source: 32.7), p90 39 (63), sentences over 60 words 25 (67), counted on math-free prose so theorem statements don't distort it. Per part: 19.1 / 23.5 / 19.8 / 24.4 / 25.9 / 23.0 / 27.9 / 24.7.
6. **The chatbot residue is gone**: no `gemini:` prefix, no second abstract, no "People keep treating…", no duplicate §1. The article's own voice is kept impersonal where the source is impersonal — the we/our count is *not* padded in §§2–9 to hit a style metric, because that would invent authorial claims.

## Verification run over these nine files

* 27 discipline phrases checked → all present (three initially "missing" were false negatives from bold markup inside the phrase; confirmed by direct grep).
* 60 must-keep numeric tokens checked → all present, including 89.526 / 397.87 / 2.090 / 4.652133 / 0.535 / 5.000 / 4.47 / 0.348 / 0.187, 4.44 / 415 / 2.57 / 4.66 / 454 / 2.9 / 1.79, ψ = 0.85 / 0.25 / 0.70 / 0.20, 150 yr, 2×10⁶ yr, 8.6×10⁴ yr, 5,050, 0.130, the whole phosphate and G3P tables.
* The eight known Gemini failures re-tested for presence here: `τ_aggregate`, "metabolic balance", "resolves both failures", "satellite-derived masks", "artificially thresholded", routing-by-label, "USGS MCS 2026 Vintage", "engineered to capture" → **0 hits each.**
* `humanize/style_audit.py` runs clean on every part; the 25 long sentences are almost entirely blockquote/list joins and math-adjacent prose, not paragraphs needing another split.

## Deliberate deviations, and what still needs the author

* **No boxes.** Rendered as blockquotes and "In plain words" openers, because the venue/template decision is still open (`humanizing.txt` rule 1). Swapping to journal `\begin{tcolorbox}` later is mechanical.
* **Markdown, not LaTeX.** Equations use `$$ … $$` for legibility here; the LaTeX pass must convert tables to floats — note that the article itself numbers **no** figures or tables (0 callouts of the form "Figure N"/"Table N" in the source), so the three tables in this rendering also need numbering decisions.
* **Open actions unchanged:** the ε label on the resources row; the abstract↔Lemma 3 direction; the five "in review" placeholders (three works) — mapping them to the three Abaee (2026) Zenodo records is visible in the source but is the author's call; completing the MCS-2026 per-country re-pin; no AI-declaration wording changes.
