# reaudit — Reproducible checks for the batch-4 audits and repairs

The audit documents in `batch 4/` (PROOF_REAUDIT.md, WAVE_E_RERUN.md,
CROSS_DOCUMENT_CONSISTENCY.md) and the repair dossiers (`batch 4/*_REPAIRED.md`,
`batch 4/PROOF_ELEVATION.md`) cite these suites. Every script reads the
repository and writes nothing; every script exits 0 on success.

| suite | assertions | covers |
|---|---|---|
| `verify_findings.py` | 34 | the original audit: A3/B6/E4 refutations |
| `verify_wave_e.py` | 56 | Wave E reproduction (hashes, scores, retention) |
| `verify_consistency.py` | 43 | cross-document consistency (incl. the manifest-vocabulary grep that catches C3-type defects) |
| `verify_a3_repair.py` | 18 | `A3_THM1_REPAIRED.md` |
| `verify_b6_repair.py` | 31 | `B6_THM1_REPAIRED.md` |
| `verify_e4_repair.py` | 58 | `E4_REPAIRED.md` |
| `verify_e7_repair.py` | 40 | `E7_REPAIRED.md` |
| `verify_b1_repair.py` | 28 | `B1_THM1_REPAIRED.md` |
| `verify_b10_repair.py` | 30 | `B10_THM1_REPAIRED.md` |
| `verify_e2b1a_b9_repair.py` | 28 | `E2_B1A_REPAIRED.md`, `B9_THM1_REPAIRED.md` |
| `verify_e2b2a_a4_repair.py` | 28 | `E2_B2A_REPAIRED.md`, `A4_THM1_REPAIRED.md` |
| `verify_a3thm2_cathm3_repair.py` | 26 | `A3_THM2_REPAIRED.md`, `CA_THM3_REPAIRED.md` |
| `verify_e3cfb7_repair.py` | 24 | `E3_C63_REPAIRED.md`, `CF_REPAIRED.md`, `B7_THM1_REPAIRED.md` |
| `verify_joint_disputes.py` | 8 | **the joint-assessment adjudications** (`PROOF_ELEVATION.md` §I.3): (1) B9 split-completeness refuted by A1's y1/y2 witness — exhaustive split search; (2) B10 pessimistic non-attainment witness — ψ is lsc, not usc (also corrects the audit's own "continuous by Berge" parenthetical) |

Note on `verify_b9`/`verify_b10`-adjacent suites: the A2 attempt's own
verification of its B9 clause (c) and B10 pessimistic existence passed
because those claims are false only on models outside their test fixtures;
`verify_joint_disputes.py` supplies the refuting fixtures. The errata at
the head of the root `batch 4/B9_THM1_REPAIRED.md` and `B10_THM1_REPAIRED.md`
record this.

**Reading the suites after the repairs landed (post-2026-08-26).** The
audit documents describe the *pre-repair* state, so Section B of
`verify_consistency.py` asserts the *presence* of the defects it documents:
after the repair commits, a `[FAIL]` on a defect check means the defect is
**gone** (fixed), and `[OK]` means either the discipline still holds
(Section A) or the defect remains. Expected post-repair failures: C1 (both),
C2, C3, C4 (manifest + B_TIER + WAVE_E_UPDATE), C5, C6 (both) — exactly the
bucket-B/C4 repairs. The two C4 `[OK]`s that remain (PUBLICATION_STRATEGY's
"closes R02.Cor6's bridge" phrase-match, and WAVE_E_UPDATE's §1 row if the
pattern is re-run) are phrase-level matches on text that now carries the
two-depth bookkeeping qualifier — the four-way disagreement itself is
resolved (all four documents now assert the closure at the two-depth form
with the same bookkeeping).

To run everything (from the repository root):

```bash
for s in reaudit/verify_*.py; do python3 "$s" > "reaudit/$(basename "$s" .py)_output.txt" 2>&1 || echo "FAILED: $s"; done
```

Saved output: `joint_disputes_output.txt` (the adjudication run of
2026-08-26). The A2 attempt's own saved outputs were not uploaded with the
attempt; re-run the suites to regenerate them.
