# Merging for breadth: paper 9 + 9b + 10b → certification on two real systems

## The placement decision, and why (asked to judge on merits)

Two options were on the table for paper 10b (Edwards Aquifer): join 9+9b, or join 6+10.

**It joins 9 + 9b.** The evidence is textual and decisive:

| | 9 + 9b | 6 + 10 | 10b |
|---|---|---|---|
| viability kernels | yes | no | **12 mentions (66 "kernel")** |
| retention protocol frozen before scoring | yes | no | **24 mentions of "retention"** |
| ledger / aggregation theory | no | yes | **0** |

10b is a viability-kernel study under a frozen retention protocol — that is 9b's machinery, not
paper 10's. Placing it with 6+10 would have put a viability-kernel paper inside an
aggregation-theory paper on the strength of both being about groundwater accounting.

The stronger reason is structural. Paper 9b opens:

> "The viability machinery of the obstruction calculus has been developed and validated on
> deliberately small exact instances. This paper applies it to a real assessment record — the
> Northern cod stock."

Paper 10b performs **the same move on a different system**: robust viability kernels of the Edwards
Aquifer J-17 record. So 9b and 10b are one operation on two different real systems — which is
exactly the two-system replication the task-59 audit identified as missing across the corpus.

Paper 10b also names its own limitation in its conclusion: *"the scored comparison on one measured
system."* Merging removes that limitation rather than leaving it standing.

## The unifying finding

The three parts certify rather than simulate, on two real assessment records with no hydrology, no
biology and no institutional history in common. The finding they establish jointly and none
establishes alone:

> **Certification has a horizon, and the horizon is set by the fitted map, not by the method.**

- **Part I (paper 9).** The map is expansive at the reference point for every admissible carrying
  capacity $K \ge 2K^*$, so the certified layer has a finite horizon — six years under the two
  harsher floors, seven under the informative one.
- **Part III (paper 10b).** Every positive-pumping certified kernel is empty beyond three years,
  "an optimistic bound on a defect the out-of-sample audit exceeds."

The two numbers differ by a factor of two and come from unrelated systems, which is why the
recurrence is a finding rather than a property of one fit. *A certified verdict is valid over a
stated horizon, and quoting it without that horizon is quoting a different claim* — a discipline
simulation does not impose, since a simulation shows a trajectory of some length and leaves the
reader to supply the horizon.

## What was produced

`paper09_cod_certification_v32.tex` — a new version. No source was modified.

| | pages | words |
|---|---|---|
| paper 9 (harvest–protection budget) | 29 | 16,710 |
| paper 9b (regime viability, cod) | ~14 | 7,056 |
| paper 10b (Edwards viability kernels) | ~20 | 9,326 |
| **merged v32** | **68** | **34,451** |

Structure: combined title and abstract; Part I (harvest–protection budget); Part II (regime
viability); Part III (Edwards governance operators); cross-system conclusion; merged references
(50 entries); merged declarations. 83 labels, 0 dangling.

Compiled with tectonic: **68 pages, 0 errors, 0 undefined references.**

## Nothing lost

All three Part bodies reproduced in full and verbatim, each opening with its own original abstract.
Word count exceeds the sum of the parts (34,451 vs 33,092) because the new front matter, table of
contents, Part heads and cross-system conclusion are additive. Page count is the sum of the parts
plus the new front matter.

## The general claim now stated

> Reference points and management rules are usually defended by simulation; here the defence is
> certification — and the difference is not stylistic.

A simulation shows what happened on the runs that were tried; a certification states *why*, locates
the verdict in a constant, and makes explicit the horizon over which the verdict holds.

Three supporting claims, each stated because each is easy to overstate:

1. **The verdict becomes structural.** Paper 9's no-dominance verdict is structural, not empirical:
   because $C^* = g(\mathrm{LRP}) - |e| = 91.59$ kt and any rule's protection margin is exactly
   $C^*$ minus its catch there, harvest and protection are *one budget*, so a reactive rule cannot
   out-supply a flat cap it matches in protection.
2. **The protocol is what makes a negative result informative.** All three parts fix the criterion
   before any score and all three report negative results. Part III reports its reactive rules as
   retained only *nominally*, together with the reason (the hybrid criterion's wet-year margin is
   exactly what the robust class excludes); Part II reports which steps do *not* certify.
3. **Two design consequences generalise.** Where a threshold is protected by the weather rather
   than by policy, no rule in the scored family can be credited with protecting it (the 660-ft line
   is protected by wet years — a geometric property of scoring triggers against their own level);
   and a positive attractor-to-threshold margin defeats every non-negative pumping rule.

Scope is stated once: each part names its own resolution limit (Part III cannot resolve the marginal
caps, $P = 0.41$–$0.65$; Part II certifies some steps and not others). The general claim is not that
certification resolves more than simulation, but that **certification states what it resolves and
over what horizon**.

## Two new bugs (both fixed in `mergelib.py`)

1. **The comment bug, fifth appearance, in `merge_preamble`.** This function located the insertion
   point with a plain `rfind('\\begin{document}')`, which is *not* comment-aware. Paper 9's
   provenance header literally says *"It contained 2x \documentclass, 2x \begin{document} ..."*, so
   the search matched **inside the comment** and injected the package block mid-comment — turning
   the comment's continuation lines into live LaTeX and producing two spurious
   `\begin{document}`. Fixed by using the comment-aware `find_real()`, with an append-at-end
   fallback for the normal case (where `split_body()` has already removed the real one).
   This is the same root cause as the original bug in the 11+11b merge, now found in five forms:
   provenance headers mention the structural commands they describe, and *every* structural search
   in this corpus must be comment-aware.
2. **`Option clash for package geometry`.** Paper 9 and paper 10b both load `geometry` with
   *different options*, so the literal-line comparison did not treat them as duplicates and both
   were included. Fixed by de-duplicating `\usepackage` **by package name** (skipping a line only
   when every package it loads is already present, so multi-package lines with a new member survive)
   — the same principle already applied to `\newtheorem`.

## Verification

Compiled with tectonic: **68 pages, 0 errors, 0 undefined references.** Content checked by PDF text
extraction for all three Part markers, all three original abstracts, and the signature quantities of
each part (91.59 kt, 215.2 kt, 615.72 ft, the 660-ft threshold).
