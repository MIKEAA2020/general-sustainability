# Paper01 v70 — line-level prose review (flaws, gaps, inconsistencies, math–prose alignment)

**2026-10-04 · Task 141.** Line-level read of the shipped v70 line
(`paper01_obstruction_calculus_v70.tex`, 2067 lines + `paper01_obstruction_calculus_v70_supplementary.tex`,
1137 lines; remote tip `fb03e538`+`abffbda6` at review time). No sources were modified; this is a
findings record with locations and suggested fixes. **Overall: the mathematics is in good order — every
theorem statement checked against its hypotheses, and every worked number re-derived exactly — but the
prose layer carries 24 findings: three broken edit-seams (grammar), four cross-reference/numbering
defects (two caused by the v70 demotion renumbering), two notation-section inconsistencies, four
dangling/undefined items, and a tail of minor presentation gaps. One initially-flagged defect class (six
"malformed figure openings") was retracted during the review as a tooling artifact and is documented as
such below.**

## 0. Method and a methodological incident

Method: full sequential read of both files; automated passes (dangling `\ref`/`\label`, duplicate labels,
hardcoded theorem-number mentions vs actual environment order, bibliography-vs-citation diff,
sentence-boundary splice sweeps); hand re-derivation of every displayed computation; byte-level
re-verification of every flagged passage.

**Tooling incident (recorded for future rounds).** During the review, the terminal display of file
contents silently deleted the two-character sequence `[h` (bracket + h) from all outputs. This produced
a convincing but false reading of `\begin{figure}[htbp]` as `\begin{figure}tbp]` at six sites, which was
pursued through a dozen compile experiments before hex-level inspection (`5c…7d 5b 68 74 62 70 5d` =
`\begin{figure}[htbp]`) exposed the artifact: the sources are correct, the compiled PDFs match them,
and the finding is withdrawn. **All findings below were re-verified at byte level with `[h`-safe
display; none is affected by the artifact** (the corpus contains `[h` only inside the six
`\begin{figure}[htbp]` and two `\begin{example}[hidden-mode …]` openings, none in prose).

## 1. Broken edit-seams (grammar) — 3 findings, all the same splice pattern

Inserted sentences that severed an existing sentence, leaving a stranded fragment.

1. **Main L804** (Theorem 3's proof): "…The theorem need not detect a failure caused only by a
   non-minimizer branch. **so some** \(t<t_1<T_{\mathrm{obs}}\) has \(q(x(t))<0\), contrary to safety."
   The final clause is stranded after a period (the original sentence was "…continues through first
   contact by (H3.2), so some \(t<\dots\) has…", into which the two hedge sentences were inserted).
   The supplement's parallel proof (supp L187) retains the correct one-sentence form. *Fix:* "…by a
   non-minimizer branch. Hence some \(t<t_1<T_{\mathrm{obs}}\) has \(q(x(t))<0\), contrary to safety."
2. **Main L874–875** (Theorem 4's proof sketch): "\(\emph{Proof sketch.}\) For branch \(j\), horizon
   step \(k\), floor row \(r\), and independent disturbances \(w_{j,t}\in W_j\), **the robust inequality
   is** / **Set** \(\zeta_{j,r,k,t}=\dots\). Then the robust row is [display]". The lead-in "the robust
   inequality is" has no object; the v70 ζ-display edit replaced the display and its preamble but left
   the old lead-in. *Fix:* "…the robust inequality is as follows. Set \(\zeta_{j,r,k,t}=\dots\); then
   the robust row is [display]" (and drop the redundant spelled-out copy of the same support constants
   at L883).
3. **Supp L750–751** (complete proof of Theorem 4): "…must be replaced by the support of the joint
   admissible path set. / **where** \(h_{W_{j}}\) is the support function of \(W_{j}\); each support
   value is itself a linear program…". The "where"-clause originally continued the display-introduction
   sentence ("…is equivalent to [display], where \(h_{W_j}\) is…"); the two inserted clarifying
   sentences (row-index vs disturbance-time; coupled paths) were spliced between the display and its
   "where", orphaning it after a period. *Fix:* move the two sentences after the "where…" sentence, or
   restart it as "Here \(h_{W_{j}}\) is…".

A corpus-wide sweep for this pattern (lowercase connective after a period, at line start and mid-line)
confirms these three are the complete set.

## 2. Cross-reference and numbering defects — 4 findings

4. **Supp L357 and L527 — stale "Proposition 4 of the main article" (×2).** Both refer to the sparse
   common-action witness. The v70 demotion of the uniform-margin proposition shifted every main-article
   proposition numbered ≥3 down by one: the witness is **Proposition 3** in v70 (Proposition 4 is now
   the emptiness construction). The supplement's concordance header was updated for the shift
   (ladder→2, recourse→5, decomposition→8) but these two hardcoded references were missed.
5. **Supp L527 — duplicated phrase:** "the Helly-type witness of Proposition 4 **of the main article of
   the main text** (Section 3.4)" — a splice duplication predating v70 (present in v69).
6. **Supp L649 — wrong section for the class-declaration theorem:** "as in clause (iv) of the
   class-declaration theorem of the main text **(Section 10)**" — clause (iv) ("the declaration is
   load-bearing…") belongs to Theorem 4, the LP instantiation, in **Section 3.3**. The other two
   "(Section 10)" references on L642/L644 are correct (the chance-constrained and deterministic-kernel
   propositions do live in §10); only the class-declaration attribution is wrong.
7. **Supp L381 — dangling citation "(Helly, 1923)":** cited in the sparse-witness proof ("By Helly's
   theorem in \(\mathbb{R}^{m}\) (Helly, 1923)") but the supplement's reference list contains no Helly
   entry. The main text says "Helly-type" without citation and also has no entry. Add the entry (Helly,
   E.: Über Mengen konvexer Körper mit gemeinschaftlichen Punkten. Jahresber. Dtsch. Math.-Ver. 32,
   175–176 (1923)) or cite via a standard textbook.

## 3. Notation-section inconsistencies — 2 findings

8. **Main L466–471 — orphaned "adverse-selection correspondences."** The notation section declares
   \(D_{\varepsilon}(x,u)\) (attributed to Theorem 5) and \(D_{\eta}(x)\) with the \(\eta/2\) margin
   (attributed to "Theorem 2's proof, local"). **Each appears exactly once in the entire corpus** — in
   this notation entry itself. No theorem statement or proof (main or supplement) uses either symbol:
   the exit theorem states its drift condition directly as (4); the common-action proof no longer
   constructs a \(D_\eta\) selection (that machinery was withdrawn by the v67–v70 hardening and the
   uniform-margin demotion). The entry also misdescribes both as "of the exit certificates". *Fix:*
   delete the entry, or redefine it to the objects actually used ((4)'s sup-inf form and (H2.3)'s
   adverse-path premise).
9. **Main L496–498 vs L523 — λ attributed to different sites in prose and table.** The prose list says
   λ is "the Farkas multiplier of Theorem 2's checkability certificate and the observer decay rate of
   Section 5(c)"; the companion table says "a Farkas multiplier of Theorem 4's LP certificate or a
   recourse weight in Proposition 5; the observer decay rate in Section 5(c)". Both are incomplete and
   they disagree (the v70 table edit fixed the old "Theorem 3" misattribution but dropped the
   common-action use, while the unedited prose kept it). The real sites are four: §3.2's common-action
   Farkas pair, Theorem 4's adjoint rows, §3.7's recourse pooling weights, and §5(c)'s observer decay.
   *Fix:* harmonize both lists to all four (or point to a single consolidated remark).

## 4. Dangling / undefined items — 4 findings

10. **Main L1507 — undefined condition label "(R3)".** "A proposed sensor regularity condition (R3)
    is model-specific…" — (R3) occurs exactly once in the corpus and is never defined (no R1/R2/R3
    anywhere; evidently a leftover from a review-response round). Either define the condition inline or
    drop the label.
11. **Main reference list — ten uncited entries in a second, differently-formatted block.** Alshiekh
    et al. (2018); Chatterjee–Doyen–Henzinger (2009); Nakao et al. (2021); Papadimitriou–Tsitsiklis
    (1987); Lovejoy (1991); Bertsekas–Shreve (1978); Witsenhausen (1968); and three Abaee (2026)
    companion preprints (the Zenodo self-deposit, the 2J3KL paper, the minimax-dual-certificate paper)
    appear in the bibliography but are cited nowhere in the main or supplement bodies. The block also
    switches citation style (author-year vs the Springer style of the first block) with no separator.
    *Fix:* wire the citations in (see finding 12) or remove the block; unify the style.
12. **Main L251 — uncited parenthetical with an available citation:** "(including qualitative
    finite-POMDP safety)" in the re-scoped §1.3 HJ paragraph. The natural source —
    Chatterjee–Doyen–Henzinger (2009) — sits uncited in the bibliography (finding 11). One-line wiring
    fix.
13. **IRViab is used but never defined.** It appears in the §2.1 hierarchy display (L335) and is then
    deferred to §6.4 (L339; again L484 in §2.4), while §6.4 (L1529) defers back to §2.1 — circular
    pointers, no formal definition anywhere (only the informal gloss "an institution restricted in
    what it may observe and in what it may command"). *Fix:* add a one-line definition in §2.1 (even
    as a contrast-class remark mirroring the EViab treatment) or in §6.4, and point both cross-references at it.

## 5. Minor presentation and consistency gaps — 11 findings

14. **Supp figure-numbering split.** The fibre figure (inside S1's complete-discussion block, supp
    L619) compiles as **"Figure 1"** (plain), because the `\renewcommand{\thefigure}{S\arabic{figure}}`
    (L880) precedes only the S4 figures ("S1"–"S3"). The main text's "(S1, Figure~S1)" then reads as if
    Figure S1 lived in section S1 (it is in S4). Move the `\renewcommand` before the first figure
    (making it "Figure S1"…"Figure S4" with renumbered cross-references), or annotate the header's
    "three additional figures (S4)".
15. **σ\* syntax drifts across four forms:** \(\sigma^{*}_{\Pi}(B_0)\) (Remark 2), \(\sigma^{*}(B_0;\Pi_B)\)
    (Theorem 4), \(\sigma^{*}_{\mathrm{hold}}(B_0)\) (§3.3 checkability, §8, §9), and bare
    \(\sigma^{*}(B_0)\) in the Table 1 delayed-information row — the last silently drops the class
    subscript that the v70 class-relativity hardening made load-bearing. *Fix:* keep the subscripted
    forms; write \(\sigma^{*}_{\Pi}(B_0)\) in the table row.
16. **Main/supp statement drift (three spots):** (a) the supplement's restatement of the selector
    principle (supp L942) drops the main's "\emph{post-observation information cell}" qualifier
    (main L548) — the qualifier is the v67+-era fix and should be mirrored; (b) supp (H3.2) opens "Fix
    the class being certified" vs main's "Fix the policy class being certified"; (c) the supp exit
    theorem closes "Theorem 4 is independent of an observation argument…" — self-referential in
    supplement numbering while its hypotheses use article numbering (readable, but "This theorem"
    would avoid the article-Theorem-4 collision).
17. **§3.9 tense mismatch:** L1240 "The project builds cleanly: all 60 build jobs pass" (present
    tense) vs the same subsection's v70-softened provenance paragraph L1272 "The pinned Lean~4 build
    previously recorded 60/60… no fresh Lean rebuild is claimed here." Align the first to the recorded
    form ("its recorded build passes all 60 jobs").
18. **Supp L400 — editorial meta-language:** the recourse-proof header reads "…with the display
    **corrected** to the support-function form" — change-log narration inside the paper; rephrase
    ("stated in the support-function form").
19. **Main L1467 — "with a slack timing bound":** ambiguous (intended: the bound is violated with
    slack, i.e. \(T_{\mathrm{obs}}\) comfortably exceeds \(\inf q/\varepsilon\)); easily misread as the
    bound being loose. Suggest "when the timing bound is violated with slack".
20. **"Exhibit" language vs hardened statements (L130, L214).** §1.1: the drift certificates are
    described as "one **exhibiting an enforcement selection**"; §1.2: "Theorem 5 and Theorem 3 each
    **exhibit** the violating constraint, an admissible disturbance, and the quantitative bound".
    Post-hardening, these theorems do not exhibit a disturbance — they hypothesize its existence
    ((H5.2), (H3.2)) and prove failure conditional on it; the v28-era construction language survives
    only here. Suggest "carry"/"are conditional on".
21. **Missing bridge between §2.1's standing conditions and (H5.2).** §2.1 (L296–301) declares "every
    selection pair admits a Carathéodory solution" as a standing condition; (H5.2) (L1024) insists
    path existence "is not a consequence of ambient lower semicontinuity or closed graph of \(D\)
    alone". There is no contradiction (the standing condition gives a solution for a *fixed* pair;
    (H5.2) needs a drift-consistent *adversarial selection* compatible with the policy class — a
    fixed-point coupling the standing condition does not supply), but the one-sentence bridge saying
    so is absent, and a careful reader will stumble on the apparent tension.
22. **Remark 5's compactness step needs g continuous.** "since \(g\) is strictly increasing on the
    compact interval, \(\dot S\) is bounded below by a positive constant there" — compactness gives
    this for *continuous* strictly increasing g (or via a monotone-striding argument); "strictly
    increasing" alone does not. The regeneration-function reading implies continuity; add the word.
23. **§9's certainty-equivalence instance (L~1698 region) omits \(\bar u\):** with \(g(S)=S^{2}\) on
    \([1,2.1]\) the admissibility range condition needs \(\bar u \ge (2.1)^{2}=4.41\); the instance
    inherits Remark 5's setup without restating it.
24. **The three-branch pair-viability rationals (main L1153):** \(\tfrac{2469}{1250}=1.9752\) and
    \(\tfrac{2419}{1250}=1.9352\) are asserted with exact-rational precision but no derivation,
    verification note, or supplementary pointer — unlike the paper's own verification pattern
    (§3.8's "recomputed independently in exact rational arithmetic"; the supplement's
    "machine-verified… twelve computations"). Given that the "six of seven priors viable" claim rests
    on them, add a derivation or a script pointer.

## 6. What was checked and stands sound (math–prose alignment)

- **Every theorem statement against its hypotheses and proof:** finite-horizon (Thm 1), common-action
  (Thm 2) with the (H2.2)↔(H2.3) gradient-to-path step, delayed (Thm 3) including the \(m=0\)
  boundary-contact case and the \(h=a\) upward-crossing exclusion, LP instantiation (Thm 4) including
  the bisection count \(\lceil\log_2 K\rceil+1\), exit (Thm 5) with the strip-integration argument,
  one-step completeness (Thm 6), static-observation reduction (Thm 7) with the \([0,2]\)
  counterexample, belief-state value (Thm 8), and all eleven propositions (selector, ladder, sparse
  witness + both scope blocks, emptiness + construction isolation, recourse + attainment variant,
  fibre, certainly-safe, monotone, decomposition, window-nogo, chance, degenerate). The ladder's
  inclusions and the demoted held-action consequence re-checked under their stated (H2.3) premise.
- **Every worked number re-derived exactly:** the §3.4 Farkas pair (\(\lambda=(1/2,1/2)\),
  \(\lambda^{\top}A=0\), margin \(1/10\)) and the nonconvex scope example; the §3.7 three-branch
  instance end-to-end (\(\beta_j=-9/25-\tau\), pooled window kernel \(0\), post-reveal pairing
  \(1/2\), \(\Gamma_h(\tau)=7/50-\tau\), exact threshold \(7/50\), \(\Gamma_h(1/5)=-3/50\)); the §3.8
  aggregate LP (cap sum \(67/25-(Y-2)/5\), \(Y^{*}=27/5\), margins \(3/50\) and witness
  \(u=(6/5,4/5)\) at \(Y=5\), \(47/25\) at \(Y=6\)); the ζ-display's support algebra; the decaying
  duality (\(z_0\ge(10/9)^{K}\), boundary control \(u\equiv0\)); the §9 fibre/aggregation thresholds
  (certainly-safe \(=\{\text{high}\}\), \(I\ge1.4\)), the timing identity
  \(T_{\mathrm{obs}}\le\lfloor z_0-1\rfloor\), the coverage grid partition \(42=30+12\) cell by cell,
  the two-patch fibres/verdicts/cycle witness and the \(y\ge4\) vs \(y\ge5\) split; the supplement's
  belief-value table (all nine rows against the closed-form \(V^{\mathrm{hold}}\) formulas), the
  two-floor POMDP instance (\(V_k=1/2\)), A.1 (h-margins 0.31/0.10, equilibrium check), A.2 (the
  \(\varphi_i=-(r_i/C_i)(S_i-C_i/2)^2\) identity, the \(p^{*}\) drift \(\kappa(C_2-C_1)/2\), the
  ω-limit argument), and A.3's recursion verdicts.
- **Concordance:** article↔supplement numbering verified at every stated point (article Thms 1/2/3/5 ↔
  supp Thms 1/2/3/4; article Thm 4's LP proof in S2; ladder ↔ supp Prop 1; recourse = article Prop 5;
  decomposition = article Prop 8; "Theorem 4's LP certificate" in the notation table ✓; "Theorem 1's
  finite-system recursion" in §8 ✓).
- **Automated integrity:** zero dangling `\ref`/`\label`, zero duplicate labels, every prose-cited
  work present in the bibliography (except the supp-side Helly entry, finding 7), the four-gates
  language intact everywhere it must be (§1.2, §2.1–2.3, §3.5, §3.9, §6.5, §7, §8, Open Problem 1,
  the unrefereed-preprint banner, and the supplement header's non-certification note).

## 7. Retracted finding (tooling artifact)

"Six malformed `\begin{figure}tbp]` openings" — withdrawn. Byte-level inspection shows all six sites
read `\begin{figure}[htbp]` (and both example openings read `\begin{example}[hidden-mode conflict]`);
the terminal display ate the `[h` sequence from every output. The shipped PDFs match their sources
(a full tectonic rebuild of the main file reproduces the shipped PDF's text layer exactly, modulo the
date). No action needed; recorded so future rounds use `[h`-safe display (the corpus census confirms
`[h` occurs only in those eight environment openings).

## 8. Recommendation

All 24 findings are prose-layer; **none touches a theorem statement, hypothesis, proof step, table
number, or figure content.** Findings 1–7 are the clear fix batch (three splices, two stale
proposition numbers, one wrong section, one missing reference entry — roughly fifteen edited lines);
findings 8–13 are small consistency repairs; 14–24 are optional polish. If a v71 is cut for them, seed
from v70; the fixes are local and carry no gate implications. Per the paper's own convention, any edit
round should re-run the diff-audit (exactly the intended hunks) and rebuild both files.
