# Paper 3 v3 — change summary (v2 and v1 preserved unchanged)

## New: Supplementary Material (paper3_supplementary_v1.md)

The manuscript merits supplementary at EMS: the main paper stays at the
software-description length while the verification depth (check
enumeration, worked derivations, search protocol) is deposited separately.

Contents S1–S8, fully aligned with the v3 main paper:

- S1 operator table (Section 2.1); S2 both recursions (Section 2.2);
- S3 certificate family with the worked Fourier–Motzkin derivation of the
  stacked menu window (lambda = (1/2, 1/2), margin 1/10 — matches
  Section 4.3 and Table 2);
- S4 complete 24-check enumeration (Section 4.1);
- S5 artifact tree + `run_all.sh` reproduction procedure + pinned figure
  environment (Sections 3, 6);
- S6 related-software search records (Section 5) — six queries with
  verbatim result records deposited in the package's `novelty_searches/`
  directory (the analogue of the master deposit's novelty searches);
- S7 notation; S8 citations.

## Main paper v3 = v2 + one supplementary cross-reference

Section 6 (test-suite paragraph) now points to S1–S8. 9 pp (was 8);
0 `??`; overfull baseline only; abstract and all other content unchanged.

## Package 1.1.1 (v1.1.0 untouched; new zip alongside)

- `novelty_searches/`: 6 query files (verbatim records, 2026-09-20,
  agent-mediated web search) + method/mapping README; the Section 5 gap
  statement is made against these records.
- Version bumped in `__init__.py` / `pyproject.toml` / `CITATION.cff`;
  CHANGELOG entry; SHA256SUMS regenerated (40 entries);
  `SafeTransition_v1.1.1.zip`.

## Version ledger

v1 (8 pp, restored original), v2 (8 pp, author corrections), v3 (9 pp,
supplementary pointer) — all three tex/PDF pairs in the repository;
nothing overwritten.
