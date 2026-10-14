# Paper 1 — CHANGELOG v62/v63 → v64

**Edition note.** The repository carries a `paper1_assessment_separation_v63.tex` on branches `e2-v3-source-year` and `lean-audit-v4` (not on `main`). It differs from v62 by a single added paragraph stating that the appendix proofs are formalised in a Lean 4 layer (no axioms, no admitted gaps, no computer-algebra oracle; ordered-field interface; produced independently of the appendices and agreeing with them). This rewrite was built from v62 and is therefore numbered **v64**; the content of the v63 paragraph is carried in Section 4.7 (Verification), item (c), and in SI Table S2 (result map with Lean references). Everything below that says "v62" applies equally to v63.


**Source:** `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v62.tex` (198 KB, ~29.7k words, 10 tables, 4 figures, 13 named results numbered in citation order) + `paper1_supplementary_v12.md`.
**Output:** `manuscript_paper1_v64.tex/.pdf` (40 pp. elsarticle preprint 11pt; ~9.9k words of body text + appendix proofs) and `manuscript_paper1_v64_supplementary.tex/.pdf` (30 pp.).
**Rule followed:** no theorem, number, proof or verified quantity was changed. Everything is either carried over from v62/SI v12 or re-derived from it; the only new computations are the two new figures, whose values were cross-checked against the v62 tables (see "Figures").

## 1. Title, abstract, framing

* New title states the result: *Every weighting licenses a plan, no plan satisfies the floors: a quantifier-order separation between compensatory and noncompensatory transition assessment* (v62: *Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility*).
* Abstract cut from 1,954 characters / ~320 words to 267 words; it now states the finite-menu characterisation, the rescue split, blend vs. time-sharing, the CES ladder (with the exact critical floors) and the common-shock survival. If the journal enforces 250 words, drop the sentence "A fishery transition anchored to a regulated biomass limit realises the datum."
* Introduction rewritten as a research-article introduction: §1.1 compensability as an acceptance question (MCDA framing first, sustainability doctrines second); §1.2 the two semantics + protocol table + a one-paragraph concrete instance; §1.3 five contributions (v62 had thirteen) + "what is not claimed"; §1.4 position in the literature (one paragraph; v62 §5.2 and SI S10 condensed; per-literature notes moved to SI S8). Adds the explicit link to the companion obstruction calculus' fibre criterion (Lemma 2 = exactness at a fixed trajectory; Theorem 2 = failure under the quantifier over plans).

## 2. Structure (v62/v63 → v64)

| v62 | v64 |
|---|---|
| §1 Intro (1.1–1.3, 13 contributions) | §1 Intro (1.1–1.4, 5 contributions) |
| §2 Typed framework (typing, datum, quantifier discipline, notation list) | §2 Setting (2.1 data & exact-tube semantics; 2.2 operators + Table 2; 2.3 accepted sets, central inclusion, notation **table**) |
| §3 Operators (five operators; accepted-state operators) | merged into §2 (typed-endpoint operator moved to §6.3 / SI S6.5) |
| §4 Results: Rem 1, Rem 2, Prop 3, Prop 4, Thm 6, datum, Thm 5, figures, Rem 7, Thm 8, machine verification, Thm 9, Prop 10 | §3 General results (Lemmas 1–2, Props 1–2, **Theorem 1** finite-menu + new Fig. 1) and §4 Witness (datum, **Theorem 2**, Table 5, Figs 2–3, Prop 3 persistence/erasure, Thm 3 blend, Prop 4 time-sharing, Prop 5 rescue + instruments table, **Thm 4 ladder** + Table 7 + new Fig. 4, **Prop 6 common shock**, §4.7 verification incl. Lean) |
| §5 Interpretation (5.1–5.9, ~12k words) | §6 Discussion (6.1 scope; 6.2 MCDA acceptance semantics; 6.3 four design tests; 6.4 limitations) — 5.3 translation table, 5.4 disturbance table, 5.5 checklist, 5.6 minimum report/data requirements, 5.7 institutional forms, 5.8 CES spectrum (landscape, Thm G, fixed-sum, continuum closure, LPI caveats, relevance chain), 5.9 common shock (M4, CT, single-event, δ-family) → SI S3–S6 |
| §6 Discussion (negative certificates; 13 limitations; §6.3 benchmark ~2,200 words + Fig. 4 + Table) | negative certificates folded into the reading after Theorem 2; limitations cut to 8; benchmark condensed to §5 (~750 words + Fig. 5); full benchmark, fisheries table, data anchor → SI S5 |
| §7 Conclusions; abbreviations; App. A–C; manual reference list; SI pointer; declarations | §7 Conclusions; App. A (general proofs), App. B (witness proofs); natbib-style bibliography (57 entries, all cited); declarations; SI contents list |

Result numbering is now sequential in presentation order (v62 carried a "presentation note" apologising for Theorem 6 preceding Theorem 5). Map (also SI Table S2):
Rem 1→Lemma 1; Rem 2→Lemma 2; Prop 3→Prop 1; Prop 4→Prop 2; Thm 6→Thm 1; Thm 5→Thm 2; Rem 7+Thm 8→Prop 3; Thm 9→Thm 3; Prop 10→Prop 4; Prop 11→Prop 5; Lemma A/B + Thm S1/S2→Thm 4 (Lemmas A/B are Lemmas S1/S2 in SI); Thm M1/M2/M3→Prop 6; Thm G→SI Thm S3; Thm M4/CT→SI Thms S6/S7.

## 3. Content moved to the Supplementary Information (new LaTeX SI, 30 pp.)

S1 abbreviations + result map · S2 remaining proofs (persistence; erasure datum; ladder: handshake, collapse convention, master equation/averaging argument, Theorem 4 (i)–(iii); common-shock sketches) · S3 substitutability spectrum in full (σ* landscape table, off-diagonal criterion Theorem S3, residual cells, fixed-sum regimes R1–R4, anchor decision 707/250, continuum slice closure with t*, a*, b*, harmonic circle, flip-total ladder, LPI caveats, relevance chain, verification) · S4 common-shock variant in full (variant, handshake, coupled regime Theorem S6, replace-reading collapse Theorem S7, single-event sub-case, δ-family, relevance chain, verification, disturbance-regime table) · S5 benchmark in full (system, schedule, dashboard, fisheries translation table, Northern-cod data anchor, institutional forms) · S6 practitioner material (terminology map, 10-point checklist, minimum report, 5 data requirements, typed-endpoint operator, Figure S1 weight intervals) · S7 verification record (grid verifier, 25-check enumeration, the six check lists, Lean module contents) · S8 positioning notes · S9 framework extensions at partial status (summary of SI v12 S1–S6; the full v12 text stays in the deposit).

## 4. Content added

* **Figure 1 (new):** the finite-menu geometry — conv(D)+R²₊ vs. ∪(d_a+R²₊) for a three-plan menu and for the witness menu {(2,0),(0,2)}; computed with the dual criterion of Theorem 1(ii) (`work/make_fig_geometry.py`).
* **Figure 4 (new):** the substitutability ladder — critical floor s*(θ) vs. σ with the exact rungs 1, 5/4, √2, φ, √3, and σ*(s) on the diagonal with the v62 brackets overlaid (`work/make_fig_ladder.py`). Numerical cross-check against v62: s*(1/2)=1.25, s*(0)=1.41421…, s*(−1)=1.61803…, s*(−2)=1.73205…; σ*(6/5)=2.64∈(2,3), σ*(5/4)=2.000, σ*(13/10)=1.58∈(1,2), σ*(3/2)=0.74∈(1/2,1), σ*(13/8)=0.488∈(1/3,1/2), σ*(9/5)=0.2498∈(1/5,1/4), σ*(39/20)=0.0689∈(1/17,1/13). All consistent.
* **Lean 4 formalisation** now reported in the paper (§4.7, SI S7): v62 omitted it although the cover letter cites it (`lean/Formalizations/P1_AssessmentSeparation.lean`, 199 theorems, no `sorry`, no added axioms).
* Theorem 4 now states the CES results as a main-text theorem (nesting; pointwise; uniform) and Proposition 6 the common-shock verdict, so the two standard objections ("artefact of linearity", "artefact of the action-indexed convention") are answered in the main text rather than in labelled extensions.
* Notation table (Table 3) replaces the v62 bullet list.

## 5. Content removed from the main text (not from the deliverables)

Terminology table; disturbance-regime table; 10-point checklist; minimum report; data requirements; institutional forms; error-bound-modulus remark (kept as one sentence after Prop 5); relaxed-control terminology paragraph (kept as one sentence); cross-reference paragraphs to companions (kept as one sentence each); the "presentation note"; the duplicate limitations on the σ/common-shock extensions; the abbreviations list (SI S1); the second (redundant) weight-interval figure (SI Figure S1).

## 6. Notation and wording changes

* Schaefer surplus renamed ς(B) (v62: σ(B)) to avoid the clash with the elasticity σ.
* "actions" → "plans" throughout the prose (symbols unchanged: menu 𝒜, plan a); "doctrine" retained only in §6.1.
* British spelling harmonised (characterisation, formalise, …).
* Declarations: "Authors' contributions" singular; availability statement now lists the six check lists and the Lean module.

## 7. Items to confirm before submission

1. JMCDA abstract limit (250 vs. 267 words) — see §1.
2. The Lean count "199 theorems" is the count of `theorem`/`lemma` declarations in the P1 module at the repository head on 2026-10-14; the README's "395 theorems" is the ten-module total.
3. The deposited verifier files and the Lean module comments use the v62 result numbers; SI Table S2 gives the map. Consider adding the map to the deposit's README.
4. Cover letter v3 (`COVER_LETTER_paper1_v64_JMCDA.md`) updated for the new title and result numbers.
