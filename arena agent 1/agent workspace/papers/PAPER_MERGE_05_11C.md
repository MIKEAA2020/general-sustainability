# Merging for breadth: paper 5 + paper 11c → exactness is not the limitation

## Why this merge

Both papers are exact-arithmetic papers, and each supplies the thing the other lacks.

- **Part I (paper 5, computation at scale).** Takes the exact discipline into the
  curse-of-dimensionality regime and shows it survives: $1{,}048{,}576$ subset evaluations collapse
  to $496$ sets, and at five parameters $68{,}719{,}476{,}736$ collapse to $1{,}552$.
- **Part II (paper 11c, exact audits).** Applies one exact audit framework to a family of worked
  systems and shows exactness is what produces the counter-intuitive verdicts: a review-timing
  identity that is *non-strict*, a monitoring target on which *no coarsest adequate partition
  exists*, and two middle cells that are simply incomparable.

A method that scales is not thereby shown to produce surprising verdicts, and a collection of
surprising exact examples is not thereby shown to survive dimensionality. Together they close both
objections normally raised against exact methods: that they are confined to toys, and that they are
a stylistic preference rather than a source of results.

## What was produced

`paper05_exact_belief_computation_v15.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 5 (at scale) | 13 | 6,435 |
| paper 11c (audits) | ~8 | 11,123 |
| **merged v15** | **21** | **18,963** |

Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged references
(26 entries); merged declarations. 75 labels, 47 cross-references, 0 dangling.

## Nothing lost

Both Part bodies reproduced in full and verbatim, each opening with its own original abstract.
Word count exceeds the sum of the parts (18,963 vs 17,558).

## The general claim now stated

> Exactness is the instrument, not the limitation.

with the two supports kept separate because they fail independently: *exactness scales* (because
the stored object is an antichain and the argued instrument is a pairwise bound — a change of what
is enumerated, not a constant-factor saving), and *exactness bites* (the verdicts are statements
about boundaries, non-existence and incomparability — exactly the kind a floating-point treatment
smooths into a wrong answer).

Part I also reports where the instrument runs out: at five parameters **the pairwise bound stops
being sufficient**. That is the honest form of a scaling claim.

What is deliberately not claimed is stated plainly: these examples do not constitute a general
taxonomy of viability failures. They supply exact counterexamples, finite censuses and reproducible
benchmarks that separate mechanisms often conflated in qualitative discussion.

The operational output, restated because it is the transferable part: boundary-inclusive reviews;
fibre splits over threshold tuning; certainly-safe reporting under aggregation; structural repair
of bias rather than compensation for it; and protocol design before instrument tuning — **design the
observation before tuning the estimator**, because in both regimes the information structure, not
the estimation quality, determines what is achievable.

## New bug: multiple size-groups in one reference list

The 1+2 merge fixed an unbalanced `{\footnotesize ... }` by stripping the wrapper at the block
ends. That was insufficient here: **paper 5's reference list contains several such groups**, and
the entry splitter cannot break across a delimiter (there is no `". "` to key on), so the opener
and closer stayed glued to whichever entries happened to be first and last in each group. An
alphabetical sort then scattered them, producing `! Too many }'s.`

Fixed by dropping size-group delimiter *lines* (a line that is exactly `{`, `}`, `{\cmd}`, or
`{\cmd`) before splitting entries. This is strictly more general than the block-end strip and
supersedes it.

**A side effect worth noting:** the merged reference count went from 24 to 26. Two entries had been
invisible to the earlier de-duplication because they were glued to brace wrappers and so failed to
normalise to distinct keys. Recovering them is a reminder that a reference-merge bug does not only
break the build — it can silently drop citations.

## Verification

Compiled with tectonic: **21 pages, 0 errors, 0 undefined references.** Content checked by PDF text
extraction for both Part markers, both original abstracts, and each part's signature objects
(1,048,576 → 496; 68,719,476,736; the 16 maximal singletons; the 93-cell grid; "no coarsest";
7 of 15; $Y^{*} = 27/5$).
