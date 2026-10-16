# Merging for breadth: paper 8 + paper 7 → one two-regime paper on governance latency

## Why this merge

Neither paper could make the claim it was making. Both close with the same sweeping sentence:

> 7: "What decides whether management stabilises or destabilises a renewable resource is
> therefore not biology alone but the **decision clock**."
> 8: "**Institutional form and timing**, not ecological lag, decide whether governance
> stabilises or destabilises the stock."

Two papers, one general claim, one delay regime each. The original partition note separated them
deliberately --- *"separated from Paper 7 because the mathematics differs"* --- which is a real
reason, but it is a reason to keep two **treatments**, not two papers. Merged, they support a claim
neither supports alone:

- **Part I (continuous channel, paper 8).** Delay as a lag in the control loop. Establishes that
  the effect of latency is *rule-signed and non-monotone*: intermediate delay stabilises under the
  mobilising rule (two subcritical Hopf crossings), and is stable at every delay under the
  protective rule (no-Hopf theorem). "Delay destabilises" is false as a generality.
- **Part II (sampled channel, paper 7).** Delay as a review clock. Establishes that the *operator*
  is not innocent: the exact sample-and-hold map crosses once near 6.5 yr while one-step
  approximations report artefact crossings, and the protective channel is stable at every interval.

Together these separate the **phenomenon** (latency in the institutional loop matters, and
rule-dependently) from the **representation** (whose choice changes the computed answer). That
separation is the general result, and neither part can state it.

## Evidence the entanglement was real

| | paper 7 | paper 8 |
|---|---|---|
| words | 19,333 | 27,377 |
| labels | 38 | 78 |
| **colliding labels** | **6** (`conclusion`, `discussion`, `introduction`, `limitations`, `references`, `related`) |

Paper 8 cites paper 7's Section 3.5 in **live text** (3 non-comment lines) for the identifiability
band; paper 7 does not cite back. The 6.5-yr number appears **36 times in paper 7 and 22 times in
paper 8** --- the same result, computed in one paper and quoted in the other. That cross-paper
dependency is now internal to the document.

## What was produced

`paper08_governance_delay_v46.tex` — a new version. Neither source was modified.

| | pages | words |
|---|---|---|
| paper 8 (continuous) | 46 | 27,377 |
| paper 7 (sampled) | 41 | 19,333 |
| **merged v46** | **90** | **49,255** |

Structure: combined title and abstract; Part I (continuous channel, full body of paper 8);
Part II (sampled channel, full body of paper 7); cross-regime conclusion; merged references
(85 entries, union, de-duplicated); merged declarations.

## Nothing lost

- Both Part bodies reproduced **in full, verbatim, uncondensed**.
- **Both original abstracts preserved**, each opening its own Part. (Same defect was caught and
  fixed in the 11+11b merge; the fix was carried forward here from the start.)
- Word count *exceeds* the sum of the parts (49,255 vs 46,710) because the new front matter,
  table of contents, Part heads and cross-regime conclusion are additive.
- The cross-citation "(Abaee, 2026, Sampled Governance, Section 3.5)" is **left verbatim** in
  Part I. It now points at a sibling that is also Part II of the same document. This is a known
  cosmetic artifact, left deliberately: rewriting it would alter source content, and no content
  may be lost or changed by a merge.

## The general claim now stated

> Whether management stabilises or destabilises a renewable resource is decided by the latency of
> the institution, not the ecology alone --- and jointly by how long the institution takes and in
> what form that delay is represented.

with what does **not** transfer stated first, because it is the more useful result: a stability
claim about a reviewed resource is **not interpretable until the decision clock is declared**, and
the operator axis and the parameter axis are different axes --- stability across discretisation
schemes (6.50–6.73 yr) says nothing about identifiability in the parameters (0.87–10.67 yr,
vanishing in 20 of 64 corners).

Three things do transfer: rule sign governs the effect of latency; faster assessment is not always
safer; periodicity alone cannot diagnose governance feedback (42-stock screen, 32-system search).

## Bug hit: nested braces in `\author`

`strip_front` removed `\author{...}` with the regex `\{[^\}]*\}`, which is **not** brace-balanced.
Paper 8's author block contains nested braces (`\textsuperscript{1}`, `\href{..}{..}`), so the
match terminated at the first `}` and left the affiliation tail as stray markup --- producing
`! LaTeX Error: There's no line here to end.` on a bare `\\[0.35em]` at line 148. Fixed with
`strip_cmd()` / `_match_brace()`, which do balanced-brace matching and skip matches inside
comments. **This is the same non-nesting-class trap that produced the comment bug; the corpus has
nested braces in front matter and any structural operation must assume so.**

## Verification

Compiled with tectonic: **90 pages, 0 errors, 0 undefined references.** Rendered content checked by
PDF text extraction for both Part markers, both original abstracts, both systems' signature
quantities (3.7 yr, 148.6–149.5, 6.5013, 0.87–10.67, the 42-stock screen and 32-system search),
the section 3.5 sensitivity heading, and the cross-regime conclusion.
