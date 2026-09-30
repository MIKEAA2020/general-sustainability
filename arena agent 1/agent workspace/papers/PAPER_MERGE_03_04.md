# Merging for breadth: paper 3 + paper 4 → obstruction certificates are small

## Why this merge

The two papers are explicitly cross-referenced as reaching **the same finding in different
languages**. Paper 4's conclusion states it directly:

> "A companion paper reaches an analogous conclusion for a different pipeline: there the count is
> the information--time product rather than the input dimension (Abaee, 2026, computational
> certification). The two are the same finding in different languages, and the recurrence is the
> point --- *obstruction certificates are small objects whose size is set by the decision variables,
> not by the uncertainty.*"

That is a general, fundamental claim currently split across two papers, each of which can only
assert its own half and cite the other for the other half. Merged, the recurrence stops being an
observation about a sibling and becomes the paper's own result, evidenced by two independent
pipelines.

- **Part I (paper 3, computational).** An outer moment approximation of all measurable
  information-adapted controls plus an inner adversarial approximation yields a finite LP whose
  optimum is a certified lower bound on the continuous-time safety value; whenever a positive
  certificate exists one can be chosen with at most $r+1$ safety rows, $r$ an information--time rank.
- **Part II (paper 4, duality).** The obstruction is not a failed search but the existence of a
  measure witness, supported on at most $k+1$ points ($k$ the control dimension), tight.

Part I says the certificate **can be computed**; Part II says what it **is**.

## What was produced

`paper03_computational_certification_v15.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 3 (computational) | 13 | 13,626 |
| paper 4 (measure dual) | 8 | 8,566 |
| **merged v15** | **24** | **23,411** |

Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged references
(44 entries, union, de-duplicated); merged declarations. 50 labels, 28 cross-references, 0 dangling.

## Nothing lost

Both Part bodies reproduced in full and verbatim, each opening with its own original abstract.
Word count exceeds the sum of the parts (23,411 vs 22,192) because the new front matter, table of
contents, Part heads and cross-part conclusion are additive.

## The general claim now stated

> Obstruction certificates are small objects whose size is set by the decision variables, not by
> the uncertainty.

with the negative half made explicit, because a bound is only substantive if it can fail: the
natural Helly-type alternative --- at most $m+1$ compatible states suffice to witness nonviability
--- is valid for convex common-action sets in $\mathbb{R}^m$ and **false** for a common blind
control function. For every $q$ there is a system with *scalar* input and $q+1$ indistinguishable
modes in which every proper subbelief is viable while the full belief is not, so every certificate
must involve all $q+1$ modes. The correct dimension counts independent temporal and informational
control decisions, not inputs.

Where the equivalence fails is stated plainly too: the measure characterisation requires
convexity, and a two-action instance exhibits a strict minimax gap in which no measure certifies.

The two recoveries are given as what they are --- Farkas infeasibility certificates and Isaacs
minimax drift conditions are not rival frameworks but specialisations of one duality --- so that
what the unification *licenses* is the transfer of checkability: a certificate verifiable without
re-running the search, whose size is known in advance, and which localises the failure it reports.

## Verification

Compiled with tectonic: **24 pages, 0 errors, 0 undefined references.** Content checked by PDF text
extraction for both Part markers, both original abstracts, and each part's signature objects
(the $r+1$ safety rows, the $q+1$-mode rank instance, the $k+1$ tight measure bound, Farkas and
Isaacs recovery, the minimax gap). The one apparent miss, "Information--time rank", was traced to a
dash-variant artifact (en-dash in the TOC versus em-dash in the probe), not missing content.

## Note on the merge machinery

This merge reused `mergelib.py`, factored out of the 11+11b and 8+7 merges. No new failure modes
appeared, which is the point of factoring it: the three bugs found during the 1+2 merge
(`\newtheorem` collision, declarations-block refs, the `{\footnotesize ... }` reference group) are
now fixed once, centrally.
