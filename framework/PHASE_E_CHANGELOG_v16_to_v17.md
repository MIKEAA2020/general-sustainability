# Phase E changelog — v16 → v17 (2026-09-13)

Phase E = journal formalization, per user directives:

1. **New version only** — v17 is a new file; v16 (and the v13–v15 lineage) stay frozen.
2. **No reference to superseded manuscript states** — all changelog/diary/meta commentary
   stripped: run dates, "rerun", "first execution", "updated", "post-hoc rows disclosed",
   "not executed as full simulation", "the earlier benchmarks understate…", provenance
   notes about which file failed to reproduce, "corrected here against the archived row
   count". Earlier manuscript versions are never referenced. Companion papers remain
   formally cited (Abaee 2026a/b).
3. **Formal register** — informal/chat terms removed ("coin-flip", "protocol kink",
   "from apology into strengthening", "dissolves", "imported unmodified", "— labelled",
   telegraphic fragments repaired), duplicated sentences removed (Section 3 audit
   sentence; Section 5.1 near-tie sentence), garbled fragments rebuilt into formal prose
   (Section 7 Licensed paragraph, Section 5.2 precipitation sentence, Section 1
   scaled-error sentence).
4. **Naive over-hedging removed, legitimate scope kept** — no metaphor apologies were
   present in the lineage (scan below); scope statements ("not proof of it", "no general
   claim", "limitation") retained.
5. **Single authoritative number set** — every operating characteristic now comes from the
   pinned-seed campaign of Phase C (200/100/30/10 replicates per cell, Section 4.2), with
   the archived replicate table retained only as the stated source of the Section 4.5
   alternative-rule rows. Consequently: D1 0.955/0.960; D2 0.780/0.060; D3 0.110/0.100;
   D4 0.010/0.010; D5 specificity 0.995/0.950; D6 0.633/0.733; D7 0.933/0.867; T=71
   0.900/1.000 and 0.000/0.000; wrong-module 0.034; null per-module-replicate 0.0055;
   LR table recomputed; identification 61%/37%/18%/1%/11%; gate removal 72%/93%;
   mean power 0.373; the information-criterion comparison cites 0.373/0.973 with a
   Section 4.5 cross-reference (archived table row 0.376/0.978 noted as statistically
   indistinguishable). All qualitative verdicts unchanged.
6. **Automated guards** — two new scanners, run on every future version:
   `framework/journal_formalization_scan.py` (diary/changelog, naive-hedging,
   informal-register, navigation/self-description, manuscript-state references;
   v17 → 0 flags) and `framework/content_coverage_scan.py` (every numeric claim of the
   original upload v0 and the frozen v13 covered exactly or via recorded updates; all
   30 domain terms present; v17 → clean). `journal_style_automated_scan.py` also passes
   (0 blockers).

Applied as `framework/apply_phaseE_v16_to_v17.py` — **75 asserted replacement rules**
(E01–E75, each verified to occur the expected number of times before replacement),
idempotent (byte-identical on re-apply). v17 = 69,282 chars, 455 lines.

## Coverage audit (user question: content lost from earlier versions?)

Scanner result: **no scientific, pedagogical, or expository content lost.** Every numeric
claim in the original upload (v0) and in the frozen v13 is present in v17, either exactly
or through a recorded update (the pinned-seed values, the AD1 K-bound correction
950.8/50.8 kt, the qwen-2.4 0.0359 value, precision roundings). The only removed material
is process bookkeeping (cost arithmetic, benchmark seconds, provenance notes), replaced
by a formal computing-cost and reproducibility statement in Data availability.
