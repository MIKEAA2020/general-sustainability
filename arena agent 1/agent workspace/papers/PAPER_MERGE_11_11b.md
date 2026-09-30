# Merging for breadth: paper 11 + paper 11b → one two-system paper

## Why this merge

The bar is *broad conclusions and fundamental understanding*. Nine of the fifteen papers drew
their conclusions from a single system each, which caps how broad any of them can be. Papers 11
(Northern cod) and 11b (Edwards Aquifer) were the strongest candidate for a fix, on evidence:

- **Structurally parallel.** Identical LaTeX preamble, and the same section architecture ---
  Introduction, Related work, Data/Specification, Forecast Models, Evaluation Design, Results,
  Discussion, Conclusions --- differing only in the system.
- **One method, two systems.** Both score deliberately simple process-based models against naive
  benchmarks under a retention rule frozen before any score was computed.
- **11b already claimed the replication.** Its "Transferable lesson" paragraph stated that the
  finding "replicates in the companion Northern cod forecast study". Merging makes that
  replication *internal* to the paper rather than a citation to a sibling.

Vocabulary overlap between the two is 33.0% — unremarkable, and not the deciding criterion.
The deciding criterion is that **together they support a claim neither supports alone**: a
finding on one system is a demonstration; the same finding on two systems from different
domains is a replication.

## What was produced

`paper11_forecasting_baselines_v64.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 11 (cod) | 41 | 20,764 |
| paper 11b (Edwards) | 22 | 9,637 |
| **merged v64** | **64** | **31,100** |

Structure: combined title and abstract stating the two-system design and the general claim;
Part I (full Northern cod study); Part II (full Edwards study); a cross-system conclusion;
merged references (36 entries, union, de-duplicated); merged declarations.

## Nothing lost

- Both Part bodies are reproduced **in full**, uncondensed.
- **Both original abstracts are preserved.** An early version of the merge script stripped them
  as duplicate front matter; that was caught by checking the rendered PDF for the phrase "Five
  surplus-production modules", which had vanished. The script was corrected so each Part opens
  with its own original abstract, with the combined abstract at the head of the document.
- Page count is the sum of the parts (41 + 22, plus the table of contents and cross-system
  conclusion), which is the arithmetic check that nothing was dropped.

## The general claim now stated by the paper

> A model that persists a near-white driver has no claim to beat persistence, whatever its
> mechanistic fidelity.

with two general consequences: a negative result is informative only against a protocol fixed in
advance; and the failure is **diagnostic**, locating the defect in the driver's spectrum rather
than only reporting a loss. The two systems supply different mechanisms (a weakly autocorrelated
surplus in the fishery; a near-white annual recharge, r = 0.17, in the aquifer) against the same
test — and that invariance is the point.

## Bugs hit during the merge (and the lesson)

1. **`\end{document}` × 3.** Each source body carried its own; the declarations block did too.
2. **Duplicate titles/abstracts.** Both bodies contained `\title`/`\author`/`\maketitle`.
3. **The comment bug, again.** Paper 11's provenance header *mentions* `\documentclass` and
   `\begin{document}` ("v61 was THREE complete LaTeX documents concatenated (3x \documentclass,
   3x \begin{document})"). A naive `s.find()` split **inside that comment**, putting the real
   preamble into the body and producing `LaTeX Error: Environment abstract undefined`. Fixed with
   a comment-aware `find_real()` that skips matches preceded by `%` on the same line.
   This is the third time this class of bug has appeared in this corpus; it must be assumed
   present in any structural operation on these files.
4. **Namespace collisions.** The two papers shared 8 labels (`conclusions`, `discussion`,
   `evaluation-design`, `forecast-models`, `introduction`, `priorart`, `references`, `results`).
   Resolved by prefixing Part I labels with `cod-` and Part II labels with `edw-`, rewriting both
   `\label` and `\ref`/`\eqref` consistently.
5. **`re.sub` replacement escaping.** `'\eqref{...}'` in a replacement string raises
   `bad escape \e`; replacements must be passed as lambdas.

## Verification

Compiled with tectonic: **64 pages, 0 errors, 0 undefined references.** Rendered content checked
by PDF text extraction for both Part markers, both systems' signature quantities (884.6 kt, r =
0.17, 16.80 vs 21.11, 97% power), both original abstracts, and the cross-system conclusion.
