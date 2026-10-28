# C11 targeted revision review

Start with [the review](C11_TARGETED_REVISION_REVIEW_20261028.md).

This package checks the newly uploaded 35-page C11 PDF against the recorded C10 audit findings. It does not modify the manuscript or existing C10 audit package. The PDF itself is not copied into this audit package; its SHA-256 is recorded in the report/results.

## Reproduce

```sh
python -m pip install -r requirements.txt
python verify_c11.py /path/to/ecomod_continued_11_revision_draft_20261028.pdf > c11_verification_stdout.txt
```

In the original workspace, the script defaults to the PDF under the adjacent `uploads/` directory. Outputs are written beside the script. Tested with Python 3.13.

The independent reconstruction implements one explicit reading of the PDF's numerical convention. It is not author code and does not establish historical run provenance. It reproduces the dt=0.1 recovery summary and most printed Ac/B/D refinement statistics. The P refinement numbers differ slightly; the report discloses that difference. Revised SI and versioned author code were not supplied.

## Contents

- `C11_TARGETED_REVISION_REVIEW_20261028.md`: findings, resolution matrix and next steps.
- `verify_c11.py`: PDF extraction, independent numerical reconstruction and counterexamples.
- `c11_verification_results.json`, `c11_verification_stdout.txt`: recorded numerical checks.
- `c11_extracted_text.txt`: PDF text extraction for locating passages; font/ligature artifacts remain. Consult the original PDF for authoritative wording and mathematics.
- `requirements.txt`: tested dependency versions.
- `artifact_manifest.json`: SHA-256 and byte counts, excluding the manifest itself.

The extraction is supplied as audit context, not as a revised manuscript. No new empirical dataset was downloaded or transformed for this review. Authentication credentials are excluded.
