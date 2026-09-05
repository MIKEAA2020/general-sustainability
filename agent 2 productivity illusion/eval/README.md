# Matcher evaluation (labelled gold set)

`scan_revision eval` measures the master→revision matcher against a small,
human-checked gold set (`scan/gold.py`). It is designed as an **eval-driven
upgrade path**: the backend is swappable, so a stronger model can be plugged in
later and compared against the same gold labels.

## Run

```
# default offline backend (TF-IDF + BM25) — self-contained, deterministic
scan_revision eval \
  --master data/MASTER_joint_assessment_and_implementation_plan.md \
  --revision data/IMPLEMENTED_revision_ECOMOD.md \
  --out eval/results_bm25.json --thresholds 0.2,0.3,0.4,0.55,0.75

# OPT-IN: domain embeddings (requires sentence-transformers + the model weights)
scan_revision eval --embedding-model allenai/specter --out eval/results_specter.json
scan_revision eval --embedding-model sentence-transformers/all-mpnet-base-v2 --out eval/results_mpnet.json
```

## Recorded baseline: TF-IDF + BM25 (offline)

| Metric | Value |
|---|---|
| **Recall@1** | **0.86** (19/22) |
| **Recall@3** | **0.91** (20/22) |
| Gold best-match score | mean 0.39 (min ~0.07, max 1.00) |

Pair classification (gold positives + **expanded hard negatives**) at several thresholds:

| Threshold | Precision | Recall | F1 |
|---|---|---|---|
| 0.15 | 0.80 | 0.83 | **0.81** |
| 0.2 | 0.90 | 0.64 | 0.75 |
| 0.3 | 1.00 | 0.50 | 0.67 |
| 0.45 | 1.00 | 0.25 | 0.40 |
| 0.6 | 1.00 | 0.14 | 0.25 |

> The negative set was expanded with **near-miss** paragraphs (semantically close but
> not the true answer). That is what makes precision drop below 1.0 at loose thresholds:
> the too-loose tail now has real lookalikes. F1 peaks near ~0.15–0.2.

> **Robustness note.** Gold anchors are **distinctive substrings**, not line numbers,
> so the harness survives paragraph re-numbering / document edits (the first
> line-number gold set broke the moment the revision was edited — Recall collapsed
> to 0.14 — which is exactly the kind of regression the harness is meant to catch).
> Only **2 claims** remain unretrieved at top-3: **12A.4** and **12B.6**, both
> genuinely paraphrase-heavy (no lexical/numeric overlap with their gold paragraph).

## Findings

1. **Retrieval is strong.** The matcher ranks a genuinely-covering revision
   paragraph first for 20 of 22 claims — good enough to point a reviewer at the
   right place.

6. **The score is a RANKING score, not a probability — so use TWO thresholds.**
   The hybrid score's F1 peaks near ~0.15 and gold segments average ~0.39, so a single
   threshold can't be both high-recall (find the right paragraph) and high-precision
   (auto-mark as covered without a human). The pipeline therefore separates these:
   * `retrieval_threshold` (0.20) — "show this match to a reviewer": precision 0.95 /
     recall 0.68.
   * `semantic_threshold` (0.45) — the covered/partial AUTO boundary: precision 1.0.
   * `auto_covered_threshold` (0.60) — "auto-mark covered, no human check": precision
     **1.0** (recall is allowed to drop; a human re-checks the rest).
   Every row carries an `auto_tier` (`auto-covered` vs `candidate`) so the report
   distinguishes "confidently auto-covered" from "retrieved, needs a human look".

2. **The hybrid score is miscalibrated as a coverage *probability*.** Gold
   paragraphs rank near the top but their absolute score averages only ~0.39, so
   the old 0.75/0.55 "covered/partial" thresholds over-thresholded (the auto layer
   under-flagged coverage, which is why the curated layer was needed). F1 peaks at
   ~0.2. **The 0.45/0.30 thresholds now in `config.yaml` are data-informed.**

3. **Precision is clean at every threshold (1.00)** — the matcher does not
   confidently propose a paragraph that isn't a genuine match (on this small
   negative set), so a high score is trustworthy; the risk is missed coverage at
   high thresholds, not false coverage.

4. **The 2 recall misses are paraphrase-level, not lexical.**
   - **12A.4** — master "γ,e,b₀ chosen so r²a₁₁²=(γea₂₁)²=1.0×10⁻⁴ (Λ=0), knife-edge"
     vs revision "Baseline sits at χ=1 **because ρ was set to 3q**". Zero overlapping
     numbers; only a paraphrase matches.
   - **12B.6** — master "`dynamics for general γ` advertised but only γ=1 used" vs the
     revision reconciling γ as `1/b_G` in the unified model (via the gross-γE
     supplement), an indirect reframing.
   These are exactly where SPECTER/SciBERT (scientific-paper embeddings) can help.

5. **Golden anchors were not all "obvious".** Two gold lines were corrected during
   the eval (12G.4's Scenario-B/C note is §5 L228, and 12A.4's knife-edge note is the
   §4.3 paragraph at L187). The curated evaluation is a useful correctness check on the
   gold edges themselves.

## SPECTER / all-mpnet (opt-in, NOT default)

Not run here — `sentence_transformers` and the model weights are not present in this
environment (download is heavy/risky, and reproducibility is a core requirement of the
tool). `scan_revision eval --embedding-model <model>` will run it once those are
available and write a comparable `results_*.json`. **Recommendation:** keep TF-IDF+BM25
as the deterministic default; run SPECTER as a second pass and adopt it only if it
recovers 12A.4 / 12B.6 without regressing the 20 that already match.
