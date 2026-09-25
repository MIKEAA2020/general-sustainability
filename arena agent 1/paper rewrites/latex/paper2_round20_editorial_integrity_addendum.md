# Round 20 — Editorial-Integrity Sweep: Reference Policy, Register, Over-Hedging, Content Audit

**Date:** 2026-09-26. **Base:** `121d83d` (round 19 final). **Scope:** four directives — (D1) reference policy (companions citable; superseded versions never referenced); (D2) no change-log/diary/audit narration or editorial self-commentary; (D3) over-hedging scan (metaphor apologies out, legitimate scope statements kept); (D4) content-loss audit of earlier versions against the final editions.

## D1 — Superseded-version references removed

- **ebc v5** (the one paper still narrating its own series): the introduction no longer opens on "the series' first paper … on a two-parameter instance of 48 augmented cells, where hand analysis had failed three times and enumeration was the arbiter" — it now states the two working disciplines directly and cites the companion theory (Abaee, 2026b). The reference entry "Abaee, A. *Exact belief-state computation at scale* … Preprint" (a citation of this paper's own superseded edition) is **removed**; the remaining two entries carry years (2026a calculus, submitted; 2026b theory, preprint). Both "executes the series' first/second verification script" narrations are gone from the methods and code-availability sections.
- **E1 v54**: the body sentence "…on the annual-landings pass, which earlier editions used…" is now "The layer is unchanged when recomputed on the annual-landings pass." (the robustness statement kept, the edition history dropped); the build-provenance comment referencing the superseded markdown and pipeline is stripped.
- **minimax v5**: "the companion note's Edition 2 record" parenthetical removed.
- Companion references (published-to-be) are retained and where needed made explicit with author-year keys — per policy.

## D2 — Change-log, audit narration, and editorial self-commentary removed

- **minimax v5** (the main rewrite): the introduction no longer recounts provenance ("formulation was proposed in the source audit; … repairs two steps of the proposed argument; … replaces its worked benchmark — whose evaluation switched control sets…"); it now states the paper's contributions as its own (measure dual verified exactly; sparsity by the finite-reduction route; singleton caveat; convexity boundary by counterexample; separation axiom; single-fixed-control-set benchmark solved in closed form; dynamic layer formulated and analyzed). The dynamic-envelope section is retitled "The dynamic envelope"; the rejected-proposal narrative is reframed as mathematical analysis of "a natural candidate formulation" that fails for three reasons (the reasons and their mathematics are **retained in full** — they have methodological value and shape the corrected object); "Root causes" → "Three obstructions to the candidate"; "A category error in the clothing" → "A Bellman object posed as a pointwise Hamiltonian"; "the correction replaces" → "the formulation developed below replaces"; conjecture retitled "the open residue in continuous time"; "finite-space shadow of the martingale-transport flavour" → "finite-space form of the martingale-transport structure"; "consolidates … under one roof" → "unifies"; "requirement whose absence sank the original proposal" → "… makes a backward recursion ill-posed".
- **Editorial "honest" removed everywhere** (self-commentary): P3 v8 ("the honest general behaviour" → "the general behaviour"; "the honest complexity statement" → "the exact complexity statement"), comp v12 ("the honest one" → "the conservative one"; "the honest bound" → "the certified bound"), ws v12 ("the honest report" → "the sound report"), minimax v5 ("honest residue" → "residue").
- **Navigation phrasing**: P1 v53 "The certificates so far fire…" → "The certificates of the preceding subsections fire…"; minimax v5 "one review deep so far" → "one review deep"; "the instance's proof was the template" → "the two-window instance is the K = 2 case".
- **ebc v5 informal register**: "with a surprise" and "a different animal" → "the structure changes" / "a different regime".
- **supp v51**: "This edition adds three complete proofs…" → the supplement's section map stated timelessly.
- **ARV v3**: "has so far been developed" → "has been developed" (temporal-project narrative removed; the companion-positioning and scope retained).

## D3 — Over-hedging scan

Pattern battery: metaphor apology, "map is not the territory", "not an empirical claim", "goes without saying", "strictly speaking", "it should be noted", "should not be read as", "we emphasize that". **No naive over-hedging found in any of the nine manuscripts** — the only hits on the loose patterns are legitimate methodology, kept: E1's "a threshold recovered from an M1 fit should not be read as a biological one" (statistical-interpretation guard), "a negative result is only as informative as the instrument that produced it" (methodological motivation for the instrument audit), and P1's "an oracle failure is only a sufficient condition for real failure" (mathematical fact). Legitimate scope statements (Delimitations sections, "What else is not claimed", the sign-convention and semantics scoping) are untouched.

## D4 — Content-loss audit (earlier versions vs final editions)

**Mechanically verified present (no loss):**
- All seven delegated discussion blocks and all three complete proofs in supp v51 (7/7, 3/3 probes).
- ARV v3 carries the full proposition set of v1/v2 (8/8 themes: windows, moratorium, breach, marginal decade, covariate alarm, outcome years, delimitations, verification methods).
- minimax v5 retains all 16 environments and 9 proofs, including the three obstructions (the mathematics of the former "root causes" — nonlocality, coupling consistency, selection — kept verbatim in substance), the general finite-sequence theorem, the review-sequence instance, and "What else is not claimed".
- ebc v5 structure identical to v4 (10 sections, 8 environments).
- Word-level editions (P3 v8, comp v12, ws v12, ARV v3, P1 v53) differ from their predecessors by exactly the targeted lines (2–8 lines each, unified-diff verified) plus self-pointer renames.

**Deletion ledger (all directed, none scientific):** the parity sentences (round 16; the bar itself enforced by verifier checks); ebc's edition-history sentences (round 20; provenance only); minimax's audit-narration (round 20; the mathematical content retained, provenance stripped); E1's "earlier editions" clause and pipeline comment (round 20; robustness statement retained); supp's "This edition adds" map (round 20; content retained in timeless form). **Conclusion: no scientific, pedagogical, or expository content from earlier LaTeX-era editions is missing from the final versions; every removed sentence was either relocated (verified) or was provenance/diary text.**

## Editions shipped this round (all NEW files; nothing overwritten)

| Artifact | Edition | Change | Checks | Pages | Overfull |
|---|---|---|---|---|---|
| minimax dual certificates | v5 | de-audited intro + envelope section, formal register | 23/23 (chained 20/24/8) | 5 | 0 |
| ebc exact belief computation | v5 | self-history removed; refs rekeyed 2026a/b; self-entry dropped | 19/19 | 4 | 0 |
| P1 main | v53 | navigation phrase | probe (build gate) | 18 | 0 |
| P1 supplementary | v51 | timeless section map | probe (build gate) | 20 | 0 |
| P3 probabilistic sufficiency | v8 | "honest" ×2 | 30/30 | 10 | 0 |
| comp computational certification | v12 | "honest" ×2 | 39/39 | 10 | 0 |
| ws worked systems | v12 | "honest report" → "sound report" | 46/46 | 9 | 0 |
| ARV applied regime viability | v3 | "so far" removed | 61/61 | 4 | 0 |
| E1 cod forecast ladder | v54 | "earlier editions" clause; provenance comment | 47/47 | 35 | 0 |

All builds: exit 0, halt 0, no "??". Residual-marker battery across all nine: **0 hits**.
