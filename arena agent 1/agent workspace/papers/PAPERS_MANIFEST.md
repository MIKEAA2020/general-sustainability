# The eleven papers — assembled 2026-09-29

Partition made on **content and merits only**, with venue, length and submission strategy
excluded as considerations. New versions written to `papers/`; nothing overwritten.

## 1. The eleven

| # | file | words | composition |
|---|---|---|---|
| 1 | paper01_obstruction_calculus_v58.tex | 22,257 | 1 part |
| 2 | paper02_probabilistic_sufficiency_v10.tex | 11,804 | 1 part |
| 3 | paper03_computational_certification_v10.tex | 9,924 | 1 part |
| 4 | paper04_minimax_dual_certificates_v12.tex | 6,107 | 1 part |
| 5 | paper05_exact_belief_computation_v10.tex | 3,420 | 1 part |
| 6 | paper06_assessment_separation_v64.tex | 27,934 | 1 part |
| 7 | paper07_sampled_governance_v48.tex | 18,259 | 1 part |
| 8 | paper08_governance_delay_v42.tex | 27,339 | 1 part |
| 9 | paper09_cod_certification_v30.tex | 22,276 | 2 parts |
| 10 | paper10_depletion_ledgers_v51.tex | 42,982 | 2 parts |
| 11 | paper11_forecasting_baselines_v61.tex | 39,499 | 3 parts |

**Total: 231,801 words** across eleven papers.

## 2. What "assembled" means — stated plainly

Each file is a **new version** carrying a provenance header naming its source and the
partition rationale. What has been done is **structural assembly**. What has **not** been
done is **editorial integration**, and the difference matters:

- Papers 1--8 are single-source. They are the source manuscript with a new header. They are
  substantively complete papers in their own right.
- **Papers 9, 10 and 11 are concatenations, not integrations.** Their parts are placed in
  one file behind `\clearpage` dividers with a comment naming each source. They have not
  been edited into a single argument. Concatenation is a staging step; it is not a merged
  paper.

Specifically outstanding:

1. **Shared-framework de-duplication across papers 1--5.** The overlap test found them
   near-disjoint in *content*, but each still sets up the selector principle, the epistemic
   kernel and the observation structure independently. That setup must be derived once, in
   paper 1, and cited by 2--5 rather than re-derived.
2. **Sibling cross-citation.** None of the eleven currently cites its siblings.
3. **The 6.5-year crossing ownership (papers 7 and 8).** Both report it. Paper 7 computes
   it on the sampled map and should own it; paper 8 must cite paper 7 for it rather than
   re-derive. Until that edit is made, the two papers contain a duplicated result.
4. **Merge editing for 9, 10, 11.** Paper 9 already has a written reconciliation (the E2 /
   ARV paragraph) that should become its connecting prose. Papers 10 and 11 have no bridge
   yet.
5. **Bibliography merging** for 9, 10, 11, which currently carry two or three reference
   lists each.

None of this is hidden. It is listed here because "finish the work" cannot honestly be
claimed for editorial integration that has not happened.

## 3. Root cause analysis

**Why the family was mis-partitioned into three papers.** The earlier inventory was built
by listing the `fam/` directory plus a few known paths. The P2 companions live in
`paper rewrites/latex/` under `paper2_*` names and were never enumerated, so they were
invisible to the plan. Three of the eight venue-assigned papers (`comp`, `ebc`, `psuff`)
were consequently dropped from the inventory altogether, and two (`ebc`, `psuff`) have no
file named after them anywhere. **An inventory built from one directory is not an inventory
of the family.** Any future one must enumerate the whole tree.

**Why the count moved 3 → 8 → 10 → 11.** Each move was an evidence correction, not a
change of taste:

- 3 → 8: the P2 companions were found to exist and to be unabsorbed.
- 8 → 10: a **content** overlap test (shared sentences) replaced a **section-title** test
  and showed the five P2 papers are near-disjoint, which invalidated two merges that had
  been justified by thinness rather than duplication.
- 10 → 11: removing venue and submission considerations left the `P5` / `P4` merge
  unsupported. They differ in mathematics — a hybrid sampled map against a delay
  differential equation — and their result sets are almost disjoint. Two mathematical cores
  in one paper is the signature of two papers.

**The recurring failure mode, named.** Three times this session a conclusion was reached
before the evidence was checked: the prior-art verdict ("the claim does not survive
unqualified"), the drift onto papers outside the named family, and the two merges later
invalidated by the content test. In each case the same thing happened — a plan or summary
was treated as authoritative and the underlying artifact was not read first. The remedy
that worked each time was the same: read the artifact, measure, then conclude.

**One correction I owe.** I twice answered the "have you drifted" question defensively,
explaining that the plan assigned P5 to Paper B, rather than acknowledging that six of the
eight named papers had received no work. That was exculpatory rather than accurate.

## 4. Confidence

- `comp` and `psuff` identification: **high** (stems match the given names).
- `ebc` identification: **moderate** (no file named `ebc*`; `paper2_exact_belief_computation`
  is the only stem whose initials fit). Paper 5 rests on this and should be confirmed first.
- The content-overlap test is **sentence-level on shared strings**; it would miss
  paraphrase. Strong evidence of disjointness, not proof.
- Word counts for papers 9, 10, 11 include all concatenated parts.

---

## 5. Status update — 2026-09-29, editorial pass

Items 2, 3 and 4 of the outstanding list in section 2 are addressed. Items 1 and 5 are not.

- **Cross-citations (item 2): done.** Every one of the eleven files now carries a sibling
  block naming its companion papers, with the directive that the selector principle, the
  epistemic kernel and the observation structure are defined in paper 1 and cited by
  papers 2–5 rather than re-derived.
- **6.5-year ownership (item 3): assigned.** Paper 7 computes it on the sampled map and owns
  it; paper 8 carries an instruction to cite paper 7 and remove any independent
  re-derivation. The instruction is a note, not a text edit — the duplicate passage in
  paper 8 still has to be removed by hand.
- **Merge bridges (item 4): written.** Papers 9, 10 and 11 now open with a
  "How the parts fit together" paragraph, and their parts are promoted to LaTeX part units
  with labels. Paper 9's bridge is the E2/ARV reconciliation, which was already written;
  papers 10 and 11 are new prose.

**Still outstanding, and not mechanically finishable:**

1. **Framework de-duplication across papers 1–5.** The sibling blocks state the rule; the
   actual excision of the repeated setup from papers 2–5 is editorial judgement and has not
   been done. Each of 2–5 still contains its own derivation of the shared framework.
2. **Bibliography merging for papers 9, 10, 11.** Each still carries two or three separate
   reference lists. A diagnostic counted duplicated long lines and found **87** in paper 9,
   **45** in paper 10 and **113** in paper 11. These are the shared preamble and repeated
   reference entries; the lists must be merged by content, not by string match.
3. **The duplicate 6.5-year passage in paper 8** is flagged but not yet removed.

**Two corrections to the previous version of this section, recorded because they were my
errors.** It stated that the duplicate-line diagnostic returned zero for all three merged
papers. It did not: the first run reported zero only because the bridge-insertion regex
failed to match and the script skipped those files before counting. The real counts are the
87 / 45 / 113 above. The earlier wording also survived a bash mangling of back-quoted text
and was garbled on the way to the repository.

**Root cause of the failure this pass corrected:** the divider written into the merged files
used a doubled percent sign inside a Python percent-format string, which collapses to a
single percent, so the bridge-insertion regex silently matched nothing. It was caught only
because the script reported zero words for three files instead of writing them. A silent
no-match is the failure mode to guard against: a script that edits should always report
what it changed.
