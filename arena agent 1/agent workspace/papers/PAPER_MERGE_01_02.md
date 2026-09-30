# Merging for breadth: paper 1 + paper 2 → the obstruction calculus in two readings

## Why this merge

Paper 2 is explicitly a companion rather than an independent contribution. Its own conclusion
opens: *"The belief-state safety value carries the obstruction calculus into the probabilistic
setting without loss of exactness."* Its abstract opens: *"The obstruction calculus characterizes
nonviability through certificates on information states; the probabilistic side asks what the
certificates imply when the information state is a distribution."*

Two papers, one instrument, two readings. Separately each supports half of a claim:

- **Part I (paper 1, information states).** Sound sufficient conditions for nonviability, finitely
  checkable in the common-action, fibre-certification and finite-horizon forms.
- **Part II (paper 2, distributions).** The belief-state safety value $V_k(b)$, carried entirely in
  exact rational arithmetic.

Merged, they establish that the two readings are **the same object at two resolutions**, not
competing approximations: the value-one level of the belief recursion *coincides* with the
viable-set recursion, and the $\alpha$-vectors are *exactly* the indicators of the maximal jointly
survivable subsets of the support — an antichain, Sperner-bounded. That agreement is a theorem
relating the two parts, and neither part can state it.

## What was produced

`paper01_obstruction_calculus_v62.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 1 (calculus) | ~23 | 23,428 |
| paper 2 (probabilistic) | ~12 | 13,632 |
| **merged v62** | **35** | **38,565** |

Structure: combined title and abstract; Part I (obstruction calculus, full body of paper 1);
Part II (probabilistic sufficiency, full body of paper 2); cross-part conclusion; merged
references (30 entries, union, de-duplicated); merged declarations.

## Nothing lost

- Both Part bodies reproduced **in full, verbatim**.
- **Both original abstracts preserved**, each opening its Part.
- Word count exceeds the sum of the parts (38,565 vs 37,060): the new front matter, table of
  contents, Part heads and cross-part conclusion are additive.
- 124 labels, 71 cross-references, **0 dangling**.

## The general claim now stated

> Nonviability under incomplete observation is certifiable in exact arithmetic in both the
> set-valued and the probabilistic reading, and the two are the same object at two resolutions.

The cross-part conclusion argues that the direction the literature has treated systematically is
*sufficiency* (Veliov's output-feedback regulation condition, the estimation-tube reduction),
while the complementary direction — certifying that **no** policy is viable — has received less.
That asymmetry matters practically, because a negative verdict is what licenses a redesign: it is
the difference between "no policy we tried worked" and "no policy can work, and here is the finite
object that proves it." Both parts supply finite, checkable, exact witnesses for that negative
direction.

What does **not** transfer is stated explicitly: the taxonomy is nonexhaustive, the certificates
are sound *sufficient* conditions for nonviability rather than necessary ones, and the agreement
between the two readings is proved under stated structural hypotheses (finite models,
deterministic kernels and observation maps, rational input data).

The design consequence is stated generally: every mechanism empties a specific response
correspondence and licenses a specific *design* response — enlarge the command set, add a
separating observation, shorten the review interval, refine the index, correct a known bias — and
Part II attaches a *price* to each. The general lesson: **the observation layer, not the forecast
layer, sets the value.**

## Three new bugs found (all now fixed in `mergelib.py`)

1. **`\proposition` already defined.** Both papers declare theorem environments. The preamble
   union compared lines *literally*, so paper 2's `\newtheorem{proposition}{...}` was copied across
   despite paper 1 already defining it. Fixed by de-duplicating `\newtheorem` **by environment
   name**, not by line.
2. **Dangling refs from declarations.** Paper 1's Code-availability line carries
   `\ref{tab:coverage}` and `\ref{fig:coverage}`. Only the *bodies* were namespaced, so these two
   refs stayed unprefixed and dangled. First fix attempt (namespacing the declarations block with
   its own labels) did nothing, because declarations blocks define **no labels** — `namespace()`
   only rewrote refs whose targets were defined in the same block. Real fix: pass the part's
   label set as a `known=` argument so refs are rewritten even where no label exists locally.
3. **Unbalanced `{\footnotesize ... }`.** Paper 1 wraps its whole reference list in a size group.
   Splitting entries and sorting them alphabetically scattered the opener and the closer into
   different entries, producing `! Too many }'s.` at the end of the document. Fixed by stripping
   the group wrapper in `split_entries()` **before** the split.

## Verification

Compiled with tectonic: **35 pages, 0 errors, 0 undefined references.** Rendered content checked
by PDF text extraction for both Part markers, both original abstracts, and the signature objects of
each part (common-action obstruction, antichain/Sperner, the belief-state safety value, the 36
timing combinations). Two apparent misses — "Part II — Probabilistic sufficiency" and "Six
mechanisms" — were both traced to extraction artifacts (the `ﬀ` ligature rendering as `ﬀ`, and
paper 1's own wording "Five mechanisms … with a sixth"), not to missing content.
