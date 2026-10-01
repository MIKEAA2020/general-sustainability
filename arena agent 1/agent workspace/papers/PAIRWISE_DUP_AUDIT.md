# Cross-paper duplication audit — all 55 pairs of the eleven units (2026-10-01)

**Author's instruction:** mild, conservative de-duplication; remove only what is
obviously duplication; show the text when in doubt.

**Outcome: no substantive duplication exists between any pair of papers.** Every
shared passage is material each paper must carry on its own. No edits made.

---

## Why this scan was run

The framework audit (`FRAMEWORK_DEDUP_AUDIT.md`) compared **paper 1 against
papers 2–5 only**. That left papers 6–11, and the merged concatenations (units 8,
10, 11), entirely untested — which is where duplication was most likely, since
those files were assembled from several sources. This scan covers all 55 pairs.

Method: shared contiguous word-10-grams, reported as runs of ≥45 words so that
boilerplate phrases and formula fragments do not register.

## Result: 18 shared passages, all in three categories

| category | pairs | verdict |
|---|---|---|
| Shared bibliography entries | u1↔u2, u1↔u4, u1↔u5, u1↔u11, u2↔u4, u2↔u5, u2↔u11, u4↔u5, u4↔u11, u6↔u9 (×2), u8↔u10 (×2) | retain |
| Declarations back-matter | u1↔u2 (129 words) | retain |
| Lean verification provenance | u1↔u4, u1↔u5, u4↔u5 (111–139 words) | retain |

**Not one shared passage is body content.** No shared derivation, no repeated
theorem, no duplicated argument, no repeated results section.

### Bibliographic entries

The largest group: sibling citations such as

> `abaee a 2026 an obstruction calculus for viability under incomplete
> observation submitted abaee a 2026 robust viability of the 2j3kl limit
> reference point under a surplus production map policy scoring expansion and
> when catch cannot help zenodo https doi org 10 5281 zenodo 22552060`

shared by papers 1, 2, 4, 5 and 11c; Baez 2023 and Fischer-Kowalski 2011 shared
by papers 6 and 10; the Edwards Aquifer Authority and Water Data for Texas
entries shared by papers 9 and 11.

Each paper needs its own reference list. A reader of paper 4 alone cannot be sent
to paper 1 for a citation. Not duplication in any removable sense.

### Declarations back-matter (papers 1 and 2)

> `declarations funding none competing interests none data availability no
> external data were used code availability the verification script paper2
> probabilistic sufficiency v14 verification py which chains the per system
> scripts…`

Verified by inspection: paper01 lines 2117–2131 and paper02 lines 1795–1806 are
each file's own `\section*{Declarations}` block. Both must exist.

### Lean verification provenance (papers 1, 4, 5)

> `verification provenance the project is pinned to lean 4 in lean toolchain
> currently v4 34 1 the mechanized checks reported in this section were run under
> v4 14 0 on 2026 09 30 the source level invariants were re verified…`

Previously considered in the framework audit for papers 4 and 5 and retained; the
scan shows paper 1 carries the same paragraph. Same reasoning applies and is
strengthened: three papers independently make mechanization claims, and each
reader needs the provenance statement in the paper they are reading. It also
carries a caveat ("the build has not been re-run since the toolchain pin moved"),
which would be lost to two of the three papers if it were centralised.

## Consolidated position on de-duplication

Across all three audits there is now a complete picture:

1. **Framework setup (papers 1–5)** — not duplicated. Papers 2–5 contain zero
   occurrences of "selector principle" and "epistemic kernel" and cite paper 1.
   Closed with zero edits.
2. **Cross-paper body content (all 55 pairs)** — not duplicated. Closed with zero
   edits (this audit).
3. **Within-paper duplicate bibliography entries** — 19 found, 18 removed keeping
   the fuller copy; 1 left (Brown 2012 in paper08 has Carpenter 2011 glued to it).
4. **Within-paper duplicate blocks** — paper11's duplicated CRediT statement under
   the Funding heading removed; paper10's flagged "duplicate" equation was a false
   positive (φ and ψ, the lower and upper envelope integrands).
5. **paper09's three AI declarations** — recommended for retention. They sit in
   three declarations blocks whose other content differs (different data- and
   code-availability statements citing different scripts), so each belongs to its
   source paper. Awaiting the author's decision.

## Limitation

As with the framework audit, this tests **verbatim** overlap. A paraphrased
restatement would not be detected. Detecting that would require reading the
papers against one another in full — a much larger and far more invasive task, and
not one warranted under "de-duplicate only what is obviously duplication."

Method: `pairwise_dup.py`. No paper was modified by this audit.
