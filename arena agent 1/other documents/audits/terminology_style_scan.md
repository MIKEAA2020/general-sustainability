# Terminology, Style, and Syntax Scan (Turn 52)

**Scope.** All nine papers checked for (a) spelling-variant consistency, (b) terminology consistency (the same object under one name), (c) stylistic/syntax conventions (units, dashes, figure-caption style). Fixes issued as new versioned files only.

## Spelling findings and fixes

| Paper | Finding | Fix |
|---|---|---|
| P1 | "specialisation" (1×) amid US "-ization" convention (characterization 3×, specialization 2×, formalization) | **P1 v8**: "specialization" |
| P2 | consistent US ("-ize") throughout | none |
| P3 | "analyzed" (2×) amid British "analysed" (9×) | **P3 v8**: "analysed" ×2 |
| P4 | "hypothesized" (1×) amid British "-ise" convention (characterisation, discretisation, linearisation, destabilising, restabilising — 100+ instances) | **P4 v9**: "hypothesised" |
| P5 | "stabilization" (1×) amid British convention (stabilisation, destabilise, discretisation, factorisation, generalised) | **P5 v9**: "stabilisation" |
| E1, E2, E3, E4 | consistent US ("-ize") | none |

Word-level verification was used throughout (regex counts of "-ise/-ize" word families were checked word by word, since blanket counts conflate nouns like "expertise", "otherwise" with verb endings).

## Terminology consistency

- **P4/P5** use one name per object throughout: "mobilising/protective channel", "hold map"/"review map", "exact held-assessment update"/"exact held-measurement update" (P5/P4 respectively — each paper is internally uniform; the cross-paper difference in the same comparator's name is recorded and deliberate, each paper defining its own object), "Candidate A", "$\tau_-$/$\tau_+$", "$T_r$". No competing spellings found.
- **E2/E4** share the "flat-90%", "UC-min/UC-q05/UC-q10", "LRP", "BAU" vocabulary and use it identically in both papers; E3/E4 share "J-17", "twenty-column analysis panel", "1934–1990 training window" with matching values (verified in the turn-52 conversion pass).
- **P1/P2** share the viability vocabulary (kernel, safe-control correspondence, tube) with P5's E-notation kept distinct — no silent transfer of terms.
- En-dash compounds ("stock–flow", "Neimark–Sacker", "Lomb–Scargle") are used consistently within each paper; no hyphen/en-dash alternation for the same compound was found.

## Syntax and style checks

- **Units**: P4/P5 use "yr" and "yr⁻¹" consistently; E1–E4 use "ft", "kt", "acre-ft" consistently; no mixed unit spellings found.
- **Figure captions**: after the E2 v10 fix, all papers with figures use the same convention — image embed + bold "Figure N." caption, no filenames inside caption text (E1, E2, E3, E4, P1, P5 uniform).
- **Abstract format**: all nine now carry venue-compliant abstracts; E3/E4 use the Groundwater structured four-headed form with an Article Impact Statement (v7/v8).
- **Punctuation artifacts**: the trailing "--" residues found in P5 (fixed turn 51) and E3 (fixed turn 52, v7) were the only editing residues in the corpus; the sweep found no other stray markers, no TODO/XXX/lorem, no double spaces in prose lines.
- **Mixed straight/curly quotes**: no curly quotes or non-breaking hyphens remain in any of the nine manuscripts (the conversion drafts' typographic characters were normalized to ASCII on insertion).

## Deferred (not defects)

- American vs British spelling differences *across* papers (P3/P4/P5 British; P1/P2/E1–E4 American) are venue-consistent choices, not inconsistencies — each paper is internally uniform after this pass.
- "$\dot\xi$" vs "$\dot{x}$" variational-state notation differs between P4 and P5; each paper defines its own letter and uses it uniformly.
