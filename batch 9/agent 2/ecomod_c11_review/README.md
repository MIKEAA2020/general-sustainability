# C11 targeted revision review

This package preserves the original review and adds a version-matched follow-up:

1. [C11 version-matched follow-up](ecomod_c11_review_followup_20261028.md) — dispositions after checking the revised main text, SI, code and build outputs at C11 draft commit `d2b5e2c9e60c6e2a26b04a199dbe34064508251e`.
2. [Original targeted review](C11_TARGETED_REVISION_REVIEW_20261028.md) — historical assessment of the earlier 35-page main PDF. Its findings and context are preserved, not overwritten.

The version-matched C11 main PDF is 36 pages and its SI is 23 pages. Neither PDF is copied into this review package; their SHA-256 hashes, source hashes, verification results and remaining numerical discrepancy are recorded in the follow-up and [`c11_followup_verification_results.json`](c11_followup_verification_results.json). The reviewed manuscript, SI, scripts and checksum manifest are in the C11 draft branch named above.

## Reproduce the original independent audit

```sh
python -m pip install -r requirements.txt
python verify_c11.py /path/to/ecomod_continued_11_revision_draft_20261028.pdf > c11_verification_stdout.txt
```

In the original workspace, the script defaults to the PDF under the adjacent `uploads/` directory. Outputs are written beside the script. Tested with Python 3.13. The reconstruction implements one explicit reading of the PDF's numerical convention. It is not author code and does not establish historical run provenance. It reproduces the `dt=0.1` recovery summary and most printed `A_c`/`B`/`D` refinement statistics; the population-refinement discrepancy is disclosed in both reports.

The follow-up's version-matched source checks, rebuild and numerical reruns refer to the C11 branch commit identified above. The follow-up records Tectonic 0.17.0 as the successful build tool because pdfLaTeX was unavailable in that workspace.

## Contents

- `ecomod_c11_review_followup_20261028.md`: version-matched follow-up and updated finding dispositions.
- `C11_TARGETED_REVISION_REVIEW_20261028.md`: preserved original review.
- `c11_followup_verification_results.json`: machine-readable version, checks, quantitative results and limitations.
- `verify_c11.py`: original PDF extraction, independent numerical reconstruction and counterexamples.
- `c11_verification_results.json`, `c11_verification_stdout.txt`: recorded original-review checks.
- `c11_extracted_text.txt`: original PDF text extraction for locating passages; font/ligature artifacts remain. Consult the source PDF for authoritative wording and mathematics.
- `requirements.txt`: tested dependency versions.
- `artifact_manifest.json`: SHA-256 and byte counts for package files, excluding the manifest itself.

The extraction is supplied as audit context, not as a revised manuscript. No new empirical dataset was downloaded or transformed for this review. Authentication credentials are excluded.
