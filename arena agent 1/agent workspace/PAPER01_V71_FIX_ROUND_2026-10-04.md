# Paper01 v71 fix round — application of the Task 141 prose-layer findings

**2026-10-04 · Task 143.** v71 seeded from v70 (`paper01_obstruction_calculus_v70.tex` + supplementary, at `839f70e7`); all 24 prose-layer findings of
`PAPER01_V70_LINE_LEVEL_PROSE_REVIEW_2026-10-04.md` applied as local edits; standard diff-audit + tectonic rebuild protocol executed. No theorem, hypothesis,
proof step, table number, or figure content was altered; the four-gates language is untouched. The mathematical layer of v70 was verified sound in Task 141
and is carried over verbatim.

## Findings → fixes (all 24 applied)

**Edit-seams (1–3).**
(1) Main, Theorem 3's proof: stranded "so some \(t<t_1\)…" clause restarted as "**Hence** some \(t<t_1<T_{\mathrm{obs}}\) has…" (matches the supplement's
parallel one-sentence form). (2) Main, Theorem 4's proof sketch: the lead-in now reads "the robust inequality is **as follows.** Set \(\zeta_{j,r,k,t}=\dots\)",
and the redundant spelled-out copy of the support constants in the following sentence is replaced by the defined symbol
(\(h_{W_j}(\zeta_{j,r,k,t})\) precomputed). (3) Supplement, Theorem 4's complete proof: the two inserted clarifying sentences (row-index vs disturbance-time;
coupled paths) moved **after** the "where \(h_{W_j}\) is the support function…" sentence, re-attaching the where-clause to its display.

**Cross-references (4–7).**
(4) Both stale "Proposition 4 of the main article" sites (sparse-witness proof header; the §3.4 finite-witness sentence) corrected to **Proposition 3**
(v70 demotion renumbering; the witness is Prop 3, emptiness is Prop 4 — verified against the environment order). (5) The duplicated "of the main article of the
main text" collapsed to "of the main text". (6) The class-declaration clause-(iv) attribution corrected from "(Section 10)" to **"(Section 3.3)"** — clause (iv)
belongs to Theorem 4 (LP instantiation) in §3.3; the two neighboring "(Section 10)" attributions (chance-constrained and deterministic-kernel propositions)
were verified correct and left alone. (7) Helly 1923 entry added to the supplement's reference list (Helly, E.: Über Mengen konvexer Körper mit
gemeinschaftlichen Punkten. Jahresber. Dtsch. Math.-Ver. **32**, 175–176 (1923)), matching the list's Springer style; the body's "(Helly, 1923)" citation now
resolves.

**Notation section (8–9).**
(8) The orphaned adverse-selection correspondences entry deleted outright: \(D_{\varepsilon}(x,u)\) and \(D_{\eta}(x)\) each occurred exactly once in the
corpus (in the entry itself); byte-level re-verification confirmed 2 occurrences, both in the deleted passage, and none remain. (9) The λ site lists harmonized
**to all four real sites** in both the prose list and the companion table: Farkas multiplier of Theorem 2's checkability certificate **or Theorem 4's LP adjoint
rows**, recourse pooling weight in Proposition 5, observer decay rate of Section 5(c). (The two lists had disagreed: prose kept the common-action use only; the
v70 table edit had kept Theorem 4 + recourse only.)

**Dangling items (10–13).**
(10) The undefined "(R3)" label dropped from the sensor-regularity paragraph. (11) The ten uncited second-block bibliography entries **wired into the body**
rather than deleted, with one neutral positioning sentence each (see below), and the block dissolved: all entries converted to the first block's Springer style
and merged into the single alphabetical list — the two-style defect is gone. (12) The natural source for the uncited "qualitative finite-POMDP safety"
parenthetical (§1.3) wired in: "(including qualitative finite-POMDP safety, Chatterjee, Doyen, and Henzinger, 2009)". (13) **IRViab formally defined** in §2.1
at its first appearance, mirroring the ERViab treatment: "the robust epistemic kernel of Definition 1 with the observation structure \(\mathcal I\) replaced by
the observations the institution \(\mathcal J\) is permitted to receive and the admissible actions restricted to those it may command (its governance reading is
Section 6.4)"; the §2.4 notation pointer now cites Section 2.1, and §6.4's back-pointer is no longer circular.

**Wiring of the ten formerly-uncited entries (finding 11), one sentence each, no new claims:**
- Åström-adjacent cluster in §10's opening: computational bounds and complexity (Lovejoy, 1991; Papadimitriou and Tsitsiklis, 1987) and distributionally robust
  variants (Nakao, Jiang, and Shen, 2021) added to the existing "partially observable literature" citation sentence.
- Alshiekh et al., 2018 (shielding): one sentence in §1.3's verification paragraph — "for finite stochastic models, shield-based runtime enforcement restricts
  an arbitrary policy's actions to precomputed safe choices".
- Bertsekas and Shreve, 1978: §6.5(i)'s measurable-selection sentence — "the classical discrete-time apparatus is Bertsekas and Shreve, 1978" (cited as what
  the paper does *not* rely on; consistent with the four-gates program).
- Witsenhausen, 1968: cited at the ce-trap's own "No signalling or nonclassical-information analogy … is needed" sentence (the entry was already in the first
  block; only the body citation was missing).
- The self-deposit (An Obstruction Calculus…, Zenodo + figshare): the title-page banner now records "Deposited at Zenodo and figshare (Abaee, 2026)."
- The 2J3KL companion: appended to §1.3's sustainability-domain sentence — "a companion robust-viability application to the 2J3KL limit reference point is
  Abaee (2026)."
- The minimax-dual-certificate manuscript: one sentence at §8's opening — "The minimax-dual development of these witnesses is the subject of a companion
  manuscript (Abaee, 2026)."

**Minor gaps (14–24).**
(14) Supplement figure numbering unified: `\renewcommand{\thefigure}{S\arabic{figure}}` moved to the preamble (the per-S4 `\setcounter` deleted), so the four
figures are now **S1** (fibre, within S1), **S2** (ladder), **S3** (obstruction tree), **S4** (ce-trap); all four cross-document references updated (supp ×2,
main ×2), and the header now reads "four S-numbered figures (Figure S1 appears within S1; Figures S2–S4 are collected in S4)". Verified in the compiled PDF:
S1–S4 captions and references consistent both documents. (15) Table 1's delayed-information row now carries the class subscript:
\(\sigma^*_{\Pi}(B_0)<T_{\mathrm{obs}}\) (the form the threshold remark actually defines). (16) All three main/supp statement drifts mirrored: the supp selector
principle restatement regains the "*post-observation information cell*" qualifier; supp (H3.2) reads "Fix the **policy** class being certified"; the supp exit
theorem closes "**This theorem** is independent of an observation argument…" (no article-Theorem-4 collision). (17) §3.9 aligned to the recorded-provenance
form: "The project's recorded build passes all 60 jobs." (18) The recourse-proof header reads "with the display **stated** in the support-function form"
(no change-log meta-language). (19) "with a slack timing bound" disambiguated to "when the timing bound is violated with slack". (20) Both v28-era "exhibit"
over-claims softened to the hardened semantics: "one **conditional on** an enforcement selection" (§1.1) and "each **carry** the violating constraint…" (§1.2).
(21) The missing §2.1↔(H5.2) bridge added at (H5.2): the standing solution-existence conditions give a Carathéodory solution for each *fixed* selection pair
and do not discharge the hypothesis's fixed-point requirement of a drift-consistent adversarial selection coupled to the declared policy class. (22) Remark 5
(the ce-trap): \(g\) now "**continuous and** strictly increasing" in both the hypothesis and the compactness step (the inference was unsound for discontinuous
monotone g). (23) The §9 instance's inherited admissibility condition stated explicitly: "\(\bar u\ge(2.1)^2=4.41\)". (24) The three-branch pair-viability
rationals now carry an exact-rational derivation trace (blind controls identified: the edge point \((-\tfrac25,\mp\tfrac45)\) for the pairs containing branch 1,
the vertex \(n_1\) for \(\{2,3\}\), then per-branch braking; peaks \(s(\tau)+\tfrac12\dot s(\tau)^2\) with \((s,\dot s)=(\tfrac{1940}{1250},\tfrac{23}{25})\) and
\((\tfrac{1935}{1250},\tfrac{22}{25})\) — the reviewer re-derived both numbers independently before writing the trace).

## Diff-audit and rebuild verification

- **Diff-audit:** 33 hunks (main) + 14 hunks (supplement) vs v70, every hunk mapped to exactly one finding above; zero collateral changes. Byte-level reads for
  every site (the `[h`-eating terminal artifact of Task 141 is still active in this environment; all verification used the file-read path, and the artifact
  was confirmed to affect only terminal display, never the files).
- **Rebuild:** tectonic 0.15.0, both files compile with exit 0 — main 22 pages (v70: 22), supplement 20 pages (v70: 20). Zero unresolved `??` in either compiled
  text layer; zero dangling `\ref`, zero duplicate labels; the undefined-reference warnings in the build log are first-pass artifacts resolved by tectonic's
  rerun (same pattern as v70).
- **Compiled-text spot checks:** "Hence some \(t<t_1\)" ✓; "as follows. Set \(\zeta\)" ✓; \(h_{W_j}(\zeta_{j,r,k,t})\) ✓; σ\*_Π in Table 1 ✓; "Proposition 3 of
  the main article/text" ×2 ✓; "(Section 3.3)" ✓; "This theorem is independent" ✓; "policy class" ✓; post-observation information cell ✓; Helly bibliography
  entry ✓; where-clause reattached ✓; Figure S1–S4 captions and all four cross-references ✓; single alphabetical Springer-style reference block with all
  entries cited in the body ✓; "(R3)" and the \(D_\varepsilon/D_\eta\) passage gone ✓; the IRViab definition, the (H5.2) bridge, "continuous and strictly
  increasing" ×2, "violated with slack", \(\bar u\ge4.41\), "recorded build passes", the pair-maxima trace, and all ten citation wirings render as intended ✓.
- **Status quo confirmed unchanged (by design, not flagged by the review):** the supplement's body cites fewer works than its reference list carries (identical
  v70/v71 counts for every affected name); the versioned `coverage_v70.py` runner and `fig_p2_coverage_v70.png` references remain factually correct (they name
  existing versioned artifacts).

## Line of record

v70 remains the reviewed line; v71 is the prose-fixed line of record going forward. Artifacts: `paper01_obstruction_calculus_v71.tex` (177,257 bytes),
`paper01_obstruction_calculus_v71.pdf`, `paper01_obstruction_calculus_v71.log`, and the three supplementary counterparts, alongside the v63–v70 sets.
