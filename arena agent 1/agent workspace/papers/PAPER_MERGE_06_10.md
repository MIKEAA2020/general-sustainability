# Merging for breadth: paper 6 + paper 10 → aggregation is a claim, not a presentation

## Why this merge

Both papers close on **the same general claim**, reached from different directions:

> **6:** "...not of either tradition ... an index can be sound at the level of accounting and still
> over-certify at the level of assessment ... per-floor reporting is not a presentation preference
> but a detection requirement."
>
> **10:** "For ecological-economics measurement, that is the closing statement: **not rival
> doctrines but two readings of one ledger, and the vector reading is what carries the
> certificate.**"

As with papers 7 and 8, two papers asserting one sweeping conclusion from one direction each. The
directions are genuinely complementary rather than redundant:

- **Part I (paper 6)** gives the **geometric** reason: the compensatory and noncompensatory
  readings are related by a *quantifier commutation that can fail on an open region of state
  space*; for any finite menu, the acceptance gap is exactly the part of the convex hull of the
  required margins that **no single plan dominates**.
- **Part II (paper 10)** gives the **conservation** reason: in a typed stock--flow ledger the
  moieties are not commensurable, conservation is proved from the incidence structure rather than
  assumed, and substitution is located *within* the ledger as either a recycled flux or a drawdown
  on a second compartment — different entries with different statuses.

Part I says the gap is real and geometric; Part II says the coordinate-wise reading is the one that
carries the certificate.

## What was produced

`paper06_assessment_separation_v66.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 6 (assessment separation) | 60 | 29,071 |
| paper 10 (typed ledgers) | 62 | 34,903 |
| **merged v66** | **122** | **65,390** |

Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged references
(153 entries, union, de-duplicated); merged declarations. 129 labels, 0 dangling. Compiled with
tectonic: **122 pages, 0 errors, 0 LaTeX undefined-reference warnings.**

## Nothing lost

Both Part bodies reproduced in full and verbatim, each opening with its own original abstract.
Word count exceeds the sum of the parts (65,390 vs 63,974) because the new front matter, table of
contents, Part heads and cross-part conclusion are additive. Page count is the sum of the parts
plus the new front matter.

## The general claim now stated

> Aggregating incommensurable quantities is not a doctrine to be weighed against its alternative
> but a **representation error with a geometric signature**, and the error is structural rather
> than a knife-edge.

Three points are made explicitly in the cross-part conclusion, because each is easy to overstate:

1. **Not a normative position.** Part I's theorem establishes *no ranking of doctrines*: the
   structural character of the separation is a property of the finite deterministic menu, not of
   either the weak- or the strong-sustainability tradition. Neither part claims aggregation is
   never permissible; the claim is that where separately-binding floors matter, the aggregate
   cannot be the instrument that detects their violation.
2. **The gap has interior.** The commutation fails on an *open region*, and on the explicit
   rational datum every nonnegative weighting licenses some transition, no transition is licensed
   by all, and no transition satisfies the floors path-wise. This is the difference between a
   caution and a theorem, and it is why per-floor reporting is a *detection requirement*.
3. **The mechanism is identified, not assumed.** It is *not* scalarization blindness — at fixed
   trajectories the full-cone aggregate is lossless. It is the **policy dependence** of the
   aggregate-feasible transition: the aggregate says *there exists a weight*, the floors say *for
   all coordinates*, and the quantifiers do not commute once the plan may depend on the weight.

The implication for composite indices is stated as one about *use* rather than construction: the
arithmetic can be impeccable and the inference drawn from it unsupported. Part II makes the same
point from the other side by unpacking "depletion time" into three mutually non-interchangeable
quantities and classifying three widely cited public-data indicators at their exact status.

## Two new bugs (both fixed in `mergelib.py`)

1. **`\end{document}` inside the references block.** Paper 10 has no Declarations-style heading
   after its References — its declarations sit *before* them — so `split_body()` returned no
   declarations block and the whole tail, including `\end{document}`, became "references". It was
   then split into entries and sorted into the middle of the merged bibliography. Fixed by
   stripping `\end{document}` from the references blocks before merging.
2. **The trailing-`}` strip ate a command's closing brace.** My per-entry cleanup removes a
   trailing `}` (to clean up size-group wrappers). Applied to an entry ending in `\end{document}`
   it produced the malformed `\end{document`, giving
   `! Paragraph ended before \end was complete.` Fixed by not stripping a trailing `}` that closes
   a `\begin{...}`/`\end{...}` command.

This second bug is the interesting one: **a cleanup rule introduced to fix one problem silently
corrupted an unrelated command.** The fix is a guard, not a broader strip.

## Verification

Compiled with tectonic: **122 pages, 0 errors, 0 LaTeX undefined-reference warnings.** Content
checked by PDF text extraction for both Part markers, both original abstracts, and each part's
signature objects (the compensatory/noncompensatory formulation, the depletion-indicator framing,
"no single plan dominates", "three mutually non-interchangeable", and the new "detection
requirement" formulation). The `undef=21` figure reported by the harness is the *word* "undefined"
occurring in prose (e.g. "undefined output functional"), not a dangling reference: the log contains
**zero** LaTeX `Reference/Citation ... undefined` warnings.
