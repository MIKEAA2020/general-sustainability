# The corpus restructured: fifteen papers → seven

Every merge is a **new version**. No source file was overwritten; all prior versions remain on disk
(paper01 has 5, paper03 has 6, paper05 has 6, and so on). No content was lost or condensed — each
Part body is reproduced verbatim, **including its original abstract**, and every merged file is
larger than the sum of its parts because the new front matter, table of contents, Part heads and
cross-part conclusion are additive.

## The seven

| # | file | from | pages | words | the general claim it now makes |
|---|---|---|---|---|---|
| 1 | `paper01_obstruction_calculus_v62.tex` | 1 + 2 | 35 | 38,565 | The set-valued and probabilistic readings are **the same object at two resolutions** |
| 2 | `paper03_computational_certification_v15.tex` | 3 + 4 | 24 | 23,411 | **Obstruction certificates are small** — sized by the decision variables, not the uncertainty |
| 3 | `paper05_exact_belief_computation_v15.tex` | 5 + 11c | 21 | 18,963 | **Exactness is the instrument, not the limitation** — it scales, and it bites |
| 4 | `paper06_assessment_separation_v66.tex` | 6 + 10 | 122 | 65,390 | Aggregation is a **representation error with a geometric signature**, not a doctrine |
| 5 | `paper08_governance_delay_v46.tex` | 8 + 7 | 90 | 49,255 | Institutional latency decides stability — and **the representation changes the answer** |
| 6 | `paper09_cod_certification_v32.tex` | 9 + 9b + 10b | 68 | 34,451 | **Certification has a horizon**, set by the fitted map, not by the method |
| 7 | `paper11_forecasting_baselines_v64.tex` | 11 + 11b | 64 | 31,100 | **Process-based models are not self-justifying** |

261,135 words. All seven compile with tectonic at **0 errors, 0 undefined references**.

## Correction to the earlier plan

The eight-way partition proposed earlier was wrong in two ways, both now corrected:

- It listed a **"paper 12" that does not exist**. There are fifteen papers: 1, 2, 3, 4, 5, 6, 7, 8,
  9, 9b, 10, 10b, 11, 11b, 11c.
- It **omitted paper 10b** (Edwards Aquifer viability kernels).

The corrected partition is seven papers, not eight, and — with 10b placed by evidence rather than
by convenience — **no paper in the corpus now draws its conclusion from a single system.**

## How 10b was placed (the one judgement call asked for)

Two options were on the table: join 9+9b, or join 6+10. **It joins 9 + 9b.**

| | 9 + 9b | 6 + 10 | 10b |
|---|---|---|---|
| viability kernels | yes | no | **12 mentions** (66 "kernel") |
| retention protocol frozen before scoring | yes | no | **24 mentions** of "retention" |
| ledger / aggregation theory | no | yes | **0** |

10b is a viability-kernel study under a frozen retention protocol — that is 9b's machinery, not
paper 10's. Placing it with 6+10 would have put a viability-kernel paper inside an
aggregation-theory paper on the strength of both touching groundwater.

The structural reason is stronger. Paper 9b opens: *"The viability machinery ... has been validated
on deliberately small exact instances. This paper applies it to a real assessment record — the
Northern cod stock."* Paper 10b performs **the same move on a different system**. So 9b and 10b are
one operation on two real systems — the two-system replication the audit identified as missing. And
10b names its own limit in its conclusion (*"the scored comparison on one measured system"*);
merging removes that limit rather than leaving it standing.

## Two results that only exist because of the merges

**Certification has a horizon.** Paper 9: the certified layer is finite — six years under the two
harsher floors, seven under the informative one — because the map is expansive at the reference
point. Paper 10b: every positive-pumping certified kernel is empty beyond three years, "an
optimistic bound on a defect the out-of-sample audit exceeds." Two systems, unrelated hydrologies,
the same shape of limitation. Neither paper could state this; together it is the paper's thesis.

**The representation changes the answer.** Paper 7's operator contrast (the exact sample-and-hold
map crosses once near 6.5 yr while one-step approximations report artefact crossings) and paper 8's
discretisation artefact (an apparent 2.3-yr threshold that is not real) are the same phenomenon
seen from two formalisations. Merged, they yield the discipline the field is missing: *a stability
claim about a reviewed resource is not interpretable until the decision clock is declared*, and the
operator axis and the parameter axis are different axes.

## Merge machinery

All merges run through `/home/user/p5/mergelib.py`, with per-merge configs
(`merge_01_02.py`, `merge_03_04.py`, `merge_05_11c.py`, `merge_06_10.py`,
`merge_09_9b_10b.py`) and a compile harness (`build.py`) that stubs the missing figures so tectonic
can run.

Eight distinct failure modes were found and fixed centrally. The one worth carrying forward:

> **Every structural search in this corpus must be comment-aware.** Provenance headers literally
> mention the commands they describe ("It contained 2x \documentclass, 2x \begin{document} ...").
> This bug appeared in **five different forms** across the merges, most recently inside
> `merge_preamble`, where a plain `rfind` matched inside a comment and injected a package block
> mid-comment, turning the comment's continuation lines into live LaTeX.

Others: `\newtheorem` and `\usepackage` must be de-duplicated **by name**, not by literal line
(papers load the same environment or package with different options); declarations blocks carry
`\ref` while defining no `\label`, so namespacing must be given the part's label set explicitly;
reference lists are sometimes wrapped in size groups whose delimiters survive an alphabetical sort
as unbalanced braces — and, notably, a cleanup rule added to fix that silently ate the closing brace
of `\end{document}`.

## What remains

The merges create the room for broader claims; they do not write them. **The claim-closing pass
across all seven is still outstanding.** Per the user, that is the next prompt.

## Records

Per-merge rationale, bug analyses and verification are in `PAPER_MERGE_01_02.md`,
`PAPER_MERGE_03_04.md`, `PAPER_MERGE_05_11C.md`, `PAPER_MERGE_06_10.md`,
`PAPER_MERGE_08_07.md`, `PAPER_MERGE_09_9B_10B.md`, `PAPER_MERGE_11_11b.md`.
