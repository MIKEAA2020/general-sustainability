# Phase J changelog — v20 → v21_restructured + Supplement S1 (2026-09-13)

Phase J = the journal-fit structural pass (owner decision NEW-2, option 1: after
the text passes; distinguishing filename; continuous version count). V9-A/H/C
applied in one coordinated pass; no verdict, number, or frozen element changed.
v20 and the v13–v20 lineage remain frozen.

## New structure (V9-H: demonstration before simulation)

| Old (v20) | New (v21) |
|---|---|
| §4 Operating characteristics | §6 Operating characteristics (6.1–6.5) |
| §4.7 Prospective registration | §8 Prospective registration |
| §5.1/5.2 Applications | §4 Edwards, §5 Northern cod (worked examples first) |
| §6 Cross-application | §7 Two domains, one rule |
| §7/§8 Extracts/Conclusions | §9 Scope and conclusions |

The standard / demonstration / simulation layers are now separated: Sections 2–3
state the standard, 4–5 demonstrate it, 6 measures the rule itself.

## Supplement S1 (V9-A vehicle)

- **S1.1** Uncertainty-robust variants (full sensitivity detail; main §6.5 keeps
  a summary: specificity strengthens, retained set empties, the confidence set
  never eliminates persistence).
- **S1.2** Open problem — pre-check diagnostic (both candidate analyses; main §6
  keeps a one-sentence pointer).
- **S1.3** Verification appendix (moved whole).

## Verification

- **Line-completeness audit:** every v20 line appears verbatim in the main text
  or supplement, except the deliberate renumberings/rewrites (headers, section
  cross-references, the §1 operating-characteristic sentence, the two replaced
  paragraphs now summarised in main and archived in full in S1) — 0 unaccounted
  lines. Nothing lost, only moved.
- Scanners: formalization 0 · redundancy 0 · style PASS on main; formalization 0
  on supplement; content coverage (main+supplement) vs v0 and v13 clean.
- `content_coverage_scan.py` refined: baseline header lines are not numeric
  claims; the v13 cross-reference token 5.2 recorded as updated to Section 4.
  Regression check on v20 unchanged (2/2 clean).

## Word count (disclosed)

Main text 10,695 words; supplement 913. V9-A's 8–10k target is not fully met;
the remaining compression is recorded as O16 in the merged plan (optional,
owner-gated) — the structural goals (order, layering, supplement vehicle) are
complete.
