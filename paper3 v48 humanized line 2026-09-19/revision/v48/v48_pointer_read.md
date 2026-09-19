# The seven, and the pointers: the read

`v48_pointers_v1.py` writes `v48_pointers.{md,csv,json}`; this is what I made of it, plus the seven sentences read
end to end against the deposit. Both were asked for before the build, and the build note carries the consequences.

## The pointers: 100 of them, and how each was tested

79 of the 290 reused sentences point at something in the document: a section, a numbered theorem, a table, or a
count. Two tests per pointer, because a single test is not a check:

| test | result |
|---|---|
| does the target exist in the deposited article | 100/100 exist. Three `§9` flags were my heading parser: the deposit writes `## 9. The Interface…`, number followed by a full stop, and my pattern demanded whitespace. Fixed, and the flags went away |
| does the *deposit* cite that same target in the passage behind the sentence | 96/100 do. Those are the paper's own pointers, carried, not asserted |
| the 4 the draft cites on its own authority | all four land on the right object (below) |

- **D0159** `*(definitions; §2)*` → §2 "The Typed Primitive Ledger" — the definitions are there. Right.
- **D0354** `Proposition 6 (Finite exhaustion under uniform negative drift)` — the deposit gives Proposition 6 that
  exact title. Right; it is a self-label, which is why the aligned passage did not repeat it.
- **D0545** `incommensurable objects under the typing of §2.1` → §2.1 "Typed stocks, primitive fluxes, and the
  incidence discipline". Right target, **weaker source**: the deposit's own sentence routes this claim to
  *Definition 47* ("types, units and conversion coefficients are declared with the ledger"), where the draft points
  at the section instead. A section pointer is not false, but a reader who wants the definition is now one hop
  further. Note, not a regeneration.
- **D0655** `Theorem 14` → "Integrable extraction", cited by a sentence about cumulative drawdown bounds. Right.

The counts in the reuse set are the deposit's counts, verified against its text: `eight zero entries` (1),
`three certification` layers (2), `seven explicit non-claims` (2), `five mathematical reasons` (1),
`35 stocks` (2), `43 assessed` (1), `six-compartment` (7), `empty-kernel` (2). No reused sentence miscounts anything.

## The seven least-aligned sentences, read

Three of the seven no longer need this reading: **D0195, D0594, D0597** were in the 16 the overrule sends to the
deposit, and that is exactly where they belong — D0195 is the sentence that renames the stoichiometric operator
`S^{\top}` in the very line that *defines* it, and D0594/D0597 carry the `\mathcal A`, `\mathcal B` and
`\mathbb E` decorations the article does not use. Their low ratios were not the problem; their notation was.

**D0653** (ratio 0.207 — the furthest of all) — kept. Read against the deposit's passage it is near-verbatim:
"…whose signed difference is …; the difference is $U$-dependent because the working field omits the detritus return
$\gamma_UU$ that the closed field carries — the $U$-handling split is part of this obstruction". The low ratio is
the row *merging* two of the deposit's numbered items, not drift. Its figure `4.652133\ldots` is the deposit's
(1 in each file) and `Theorem 12` is cited by the deposit in the same passage.

**D0544** — kept. "**Non-example 1 — a deliberate boundary of aggregation, not a score of the framework.**" is the
deposit's own wording, and the row ends at "world phosphate reserves," because the next thing in both documents is a
`$$` display: the splitter cut a sentence that the document renders across a display. Harmless for reuse — the
display is carried, not rewritten — but it is why the ratio looks bad.

**D0530** — **a real flaw, and the only one in the seven.** The draft's version drops the locator the deposit
supplies. Deposit: "…the archived pull, *designated* the headline cohort under the data-vintage rule **recorded in
S5**…". Draft: "…the archived pull, kept in place as the headline cohort by the recorded data-vintage decision…".
Every number in it is the deposit's (`43`, `eight`, `≈ 1.8 yr`); what is lost is the route to the evidence.
This is the visible instance of a systemic pattern: the deposited article routes the reader to **13 distinct
supplementary locators** (S2, S2.1, S5, S5.4, S6, S7, S8, S9, S10, S11, S14, S16, S17); the draft carries **2**
(S5, S6). Within the reuse set, four sentences drop a locator their own aligned deposit sentence had —
**D0309** (S6), **D0530** (S5), **D0618** and **D0620** (S2, S14). The build therefore carries a locator check as a
gate item, so the severance cannot exceed those four sentences, and this file is the disclosure where it does.
I did not move them to the regenerate set: the partition is 290/268 as instructed, and each of the four is one line
in `v48_overrules.csv` (`D0309,regenerate` etc.) if the author wants them gone instead of disclosed.

**D0162** — kept, and the ratio is explained: its first sentence, "Every one-way transfer is donor-limited…", is the
deposit's own (1 instance in each file), and "Three certification layers, separated and proved." is verbatim from
the deposit. The register swaps are "distinct predicates with distinct proof obligations" → "different predicates
with different proof obligations", and the draft's `*(theorems; §3)*` where the deposit writes "are proved in full
(Section 3)" — same claim, same pointer, shorter breath.

## What this changes for the build, and what it does not

It adds one gate item (locators) and two disclosures: the four reused sentences that lose an `S`-reference, and the
fact that the reused sentences are subject to the two document conventions the plumbing enforces — `in review` →
`under review`, and `this article` → `this paper`. Both touch verbatim text, so the build log counts the rows they
touch instead of pretending the copy was untouched.

It does not change the partition: **290 reused, 268 regenerated**, the 16-row notation overrule applied, the
breakdown in `v48_reuse_split.md` now summing on both sides (260 + 30 reused; 188 + 64 + 16 regenerated) after the
counts were re-derived from final membership rather than from the pre-overrule piles.
