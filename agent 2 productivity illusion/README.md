# scan_revision — Master → Revision gap scan (`agent 2 productivity illusion`)

Implements the augmentation blueprint in `uploads/scan augmentation.txt` as an
installable, repeatable, auditable pipeline that cross-checks a **master** plan
(the authoritative joint assessment, `data/MASTER_joint_assessment_and_implementation_plan.md`)
against a **revision** (the implemented paper, `data/IMPLEMENTED_revision_ECOMOD.md`),
verifying coverage, numerics, internal consistency, and risk.

```
scan_revision scan   --master <master.md> --revision <revision.md>
                     [--config config.yaml] [--report-dir reports]
                     [--skip-numeric] [--skip-consistency]
scan_revision review --report reports/scan_report.json      # rubric multi-pass peer review
scan_revision diff   --old v1.json --new v2.json            # semantic diff of structured statements
scan_revision eval   [-m <master.md> -r <revision.md>]      # matcher eval vs labelled gold set
                     [-o eval/results.json] [--thresholds 0.2,0.3,0.55,0.75]
                     [--embedding-model allenai/specter]    # OPT-IN domain embeddings
```

## The 10 blueprint items → where they live

| # | Blueprint item | Implementation |
|---|---|---|
| 1 | Semantic matching + confidence scores | `scan/matcher.py` (**hybrid: 0.6 cosine [TF-IDF or sentence-transformers] + 0.4 BM25**, keyword bonus, section similarity; confidence [0,1]) |
| 2 | Hyperlinked, status-inferred traceability matrix (CSV/HTML) | `scan/report.py` (covered / partial / superseded / missing / ambiguous) |
| 3 | Rule-based + optional BERT classifier, separate pipelines | `scan/classifier.py`; `pipeline="execute"` (actionable, needs evidence) vs `"presence"` (informational) in `scan/models.py`/`risk.py` |
| 4 | Automated numerical claim verification | `model_sims/numeric_claims.py` (`VERIFIERS` + `run_numeric`, tol=0.02) + `scan/numeric.py` |
| 5 | Property-based / parameter-sweep regression tests | `tests/test_sweep.py` (det. grid sweep + optional `hypothesis`) |
| 6 | Contradiction detection via NLI (fallback rule-based) | `scan/consistency.py` (high-precision, both-sides-contrastive rule; optional `transformers` NLI hook) |
| 7 | Scored, prioritised risk register | `scan/risk.py` (`threshold` filter + `ci_failure_ids` gate) |
| 8 | Semantic diff of structured statements | `scan/semantic_diff.py` + `scan_revision diff` |
| 9 | Automated LLM peer review with structured rubric | `scan/review.py` (multi-pass; `reviewer_fn` hook or deterministic scoring) + `scan_revision review` |
| 10 | Machine-readable, replayable scan log with provenance | `reports/scan_log.json` (params, per-claim provenance, replay command) |

### Refinements (from the refined critique)

- **Supersession is decided after numeric verification, never by low score** — `scan/status.py`
  (`apply_superseded`) sets `superseded` only for a numeric `SUPERSEDED` verdict or an explicit
  supersession marker in the text. Matching (`scan/matcher.py`) only ever yields
  covered/partial/missing/ambiguous.
- **Model-provenance column** — each row carries a `Model` value (`original` / `corrected (1‴)`),
  so original-model numerics are never mistaken for corrected-model results.
- **Discrepancy section** — auto-vs-curated disagreements are listed separately
  (non-blocking; the CI only blocks on critical *actionable* missing/partial items).
- **Numeric third status** — verifiers that return a verdict show **`superseded`** (not `n/a`),
  coloured differently in the HTML.
- **Audit summary** — `reports/audit_summary.md` is the one-page, author-facing summary
  (coverage table, key re-verified numerics, discrepancies, open items, provenance caveat).
- **CI is decision support** — `.github/workflows/scan.yml` runs pytest + the scan + `scan_revision eval`
  (non-blocking), uploads the report, and **fails only on critical actionable missing/partial items**
  (never on discrepancies).
- **Two-tier confidence (ranked score ≠ probability)** — because the hybrid score's F1 peaks near ~0.15
  (Gold mean ~0.39), a single threshold can't do both. The pipeline separates `retrieval_threshold`
  (0.20, "show to a human") from `auto_covered_threshold` (0.60, high precision, "auto-mark covered");
  every row carries an `auto_tier` of `auto-covered` vs `candidate`. Curated verdicts stay authoritative.
- **Curated human decisions are recorded** — `scan/curated.py` holds `CURATED_DECISIONS` (the reasoning
  for 12B.6 / 12G.7, where the auto marker is contextual) and `NOT_SUPERSEDED` (IDs whose matched
  paragraph merely *discusses* supersession and must not be auto-flipped). This keeps future scans
  consistent and lets a reviewer see the decision was made.

Authoritative human verdicts are layered on top of the auto scores via
`scan/curated.py` — the auto detector is kept as evidence (`auto_status`/`auto_note`)
so any auto-vs-curated disagreement is surfaced for re-check rather than hidden.

## Caveat (from the blueprint)
Automation reduces manual effort and surfaces issues; it does **not** replace human
sign-off. The reports (`reports/traceability.html`, `scan_report.json`,
`traceability.csv`, `scan_log.json`, `review_report.json`) are decision support for a
domain expert, not a verdict in themselves.
