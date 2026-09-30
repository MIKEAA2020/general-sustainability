# Framework de-duplication across papers 1–5 — audit (2026-10-01)

**Author's instruction:** de-duplicate only minimally, only what is clear
duplication; when in doubt, retain and change as little as possible.

**Outcome: no changes made.** The duplication this item describes is not present
at the level of verbatim text, and what overlap does exist is material each paper
legitimately carries on its own. Under the stated rule the correct action is to
retain everything.

---

## 1. What the manifest claims

`PAPERS_MANIFEST.md` §2 item 1 and §5 item 1:

> The overlap test found them near-disjoint in *content*, but each still sets up
> the selector principle, the epistemic kernel and the observation structure
> independently. That setup must be derived once, in paper 1, and cited by 2–5
> rather than re-derived.

> Each of 2–5 still contains its own derivation of the shared framework.

Both statements were tested directly. Neither holds.

## 2. Verbatim overlap with paper 1 is negligible

Shared word 12-grams between paper 1 (23,158 words) and each of papers 2–5:

| paper | words | shared 12-grams | % of that paper |
|---|---|---|---|
| 2 | 13,327 | 365 | 2.76% |
| 3 | 13,015 | 93 | 0.72% |
| 4 | 8,192 | 223 | 2.74% |
| 5 | 8,099 | 147 | 1.83% |

The percentages are low, but the more important fact is **what** the shared
passages are. Every contiguous shared run of 40 words or more is one of:

- **Bibliography entries** — paper 2 shares reference lines with paper 1. Each
  paper needs its own reference list; these are not duplication in any sense that
  could be removed.
- **Declarations boilerplate** — funding, competing interests, data availability.
  Each paper must carry its own.
- **The Lean verification-provenance paragraph** — shared by papers 4 and 5,
  111 words, identical.

Not one shared run is framework setup.

## 3. The named concepts do not appear in papers 2–5

Occurrences in live text (comments stripped):

| concept | p1 | p2 | p3 | p4 | p5 |
|---|---|---|---|---|---|
| "selector principle" | 7 | **0** | **0** | **0** | **0** |
| "epistemic kernel" | 17 | **0** | **0** | **0** | **0** |
| "observation structure" | 15 | **0** | 1 | **0** | **0** |
| "obstruction calculus" | 17 | 8 | 12 | 16 | 6 |

Papers 2–5 do not set up the selector principle or the epistemic kernel at all —
not independently, not in any form. The single "observation structure" mention in
paper 3 is inside a shared-symbols table, not a derivation.

The manifest's premise — that each of 2–5 "still contains its own derivation of
the shared framework" — is therefore false as stated.

## 4. The one candidate, checked by hand: paper 2's selector

Paper 2 has 12 "selector" mentions, the only paper besides paper 1 with more than
one, so it is the only plausible candidate for re-derivation. It was read in full
(§`model`, L243–302). It does not re-derive:

> "**In the selector framework** this is the distributional counterpart of the
> recursive correspondence…"

and it cites paper 1 explicitly:

- L86 title: *Probabilistic Sufficiency for **the Obstruction Calculus***
- L165: "(Abaee, 2026, An obstruction calculus)"
- L175: "Abaee (2026, An obstruction calculus): the calculus there is set-valued,
  and the present theory…"
- L180: "the companion papers (the calculus, its…)"

Paper 2 builds the **distributional counterpart** of the framework — new content
on top of paper 1, not a restatement of it.

Papers 3, 4 and 5 cite paper 1 the same way:

- paper 3 L150: "information state (Abaee, 2026, An obstruction calculus)"; L265:
  a "Shared symbols across the companion papers" table
- paper 4 L91: "(Abaee, 2026, An obstruction calculus, Section 3.2)"; L126:
  "(… Theorem 2; … Worked systems for the obstruction calculus)"
- paper 5 L75: title binds it to the obstruction calculus; L131 notes its notation
  is deliberately disjoint from the companions'

The manifest asks that the setup "be derived once, in paper 1, and cited by 2–5
rather than re-derived." **That is already what the papers do.**

## 5. The one genuinely identical passage, and why it is retained

Papers 4 and 5 carry a byte-identical 111-word "Verification provenance"
paragraph (Lean 4 pinning, `v4.34.1` / `v4.14.0`, the 2026-09-30 re-verification,
and the caveat that the build has not been re-run since the toolchain pin moved).

This is the only true verbatim duplication of *body* text found. It is retained,
because:

- it is a factual provenance statement, not an argument, and each paper must
  stand on its own for a reader who has not fetched the sibling;
- each paper continues with a **different** Scope paragraph (paper 4: the
  dual-certificate core over an ordered-field interface; paper 5: the discrete
  combinatorial core), so the shared text is a common preamble to distinct
  content, in the same way a shared bibliography entry is;
- removing it from one paper would leave that paper's mechanization claims
  unattributed in its own text.

Under "when in doubt, err towards retaining," this stays.

## 6. Conclusion

Item 1 closes with **zero edits to papers 1–5**. The de-duplication it calls for
is not needed: the framework is defined once in paper 1 and cited by papers 2–5,
which is the outcome the item was written to achieve.

Two caveats on this conclusion, stated so it is not over-read:

- **This tests verbatim text and named concepts, not conceptual redundancy.** A
  paper could restate the framework in different words and this method would not
  see it. Given the instruction to change as little as possible, the low verbatim
  overlap plus explicit cross-citation was taken as sufficient; a conceptual
  review would be a separate and much more invasive task.
- **The manifest's §5 item 1 wording is now known to be wrong** and should be
  corrected at the next edit of that file, so a later reader does not act on it.

Method: `framework_overlap.py` (shared 12-grams, contiguous runs) plus direct
reading of every candidate passage. No paper was modified.
