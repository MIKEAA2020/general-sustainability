# Paper06 v76 — independent audit package

This directory contains the audit reports, follow-up verification, executable audit checks, results, and retrieved reference materials produced during review of Paper06 v76.

## Start here

1. [Main manuscript audit](manuscript_audit_v76.md)
2. [Supplementary audit](supplementary_audit_v76.md)
3. [Verification addendum](verification_addendum_v76.md) — resolves the historical 884.6 kt DFO anchor and records later qualifications.

The original reports are retained unchanged. Read them with the addendum, which explicitly supersedes the original unresolved DFO-number qualification.

## Reproduce the audit checks

The main check script uses the Python standard library:

```sh
python audit_materials/independent_checks.py
```

The supplementary script additionally requires `mpmath` (tested with 1.3.0):

```sh
python -m pip install mpmath==1.3.0
python audit_materials/supplement_independent_checks.py
```

Each script prints results and writes its adjacent JSON result file. These checks are not the manuscript author's verifier suite. Finite grid/probe checks do not establish continuum theorems, and arbitrary-precision tangency calculations are not global interval certificates.

## Contents and provenance

- `manuscript_audit_v76.md`: main-article report.
- `supplementary_audit_v76.md`: supplement report.
- `verification_addendum_v76.md`: later verification and qualifications.
- `audit_materials/independent_checks.py` and `independent_checks_results.json`: main audit checks/results.
- `audit_materials/supplement_independent_checks.py` and `supplement_independent_checks_results.json`: supplementary audit checks/results.
- `audit_materials/P1_AssessmentSeparation.lean`: retrieved reference source, not an audit-created formalisation and not rebuilt during this review. Source: https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/6f626ee48b2a3a59282b5df5adda76c8d5993fdc/lean/Formalizations/P1_AssessmentSeparation.lean
- `audit_materials/v75_supplementary.tex`: retrieved historical comparison source, not the submitted v76 supplement. Source: https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/0208f8b1523446a32ef48cbfe50415fe7ec78947/companion_restorations_20261026/Paper06_v75/paper06_assessment_separation_v75_supplementary.tex
- `audit_materials/DFO_2016_026.pdf`: primary DFO reference downloaded from https://waves-vagues.dfo-mpo.gc.ca/Library/365622.pdf ; Table A2 is on PDF/printed page 16. Government of Canada source and attribution are retained in the PDF.

The main audit contains workspace-specific links/paths from the review environment. Relative links in this README are the repository entry points.

## Audited input identification

The supplied input sources were not edited. Their SHA-256 hashes are:

| Input | SHA-256 |
|---|---|
| `paper06_assessment_separation_v76.txt` | `c57e4ebe39fe970f0ac9f78fad3cbcbc9ad12ad3a5aa3bf50f4e00a497c8e0d1` |
| `paper06_assessment_separation_v76_supplementary.txt` | `5ebcfaa789d02fa6912c5437472000c3315b4b36530f4c72c5fbbcc97fc04d3b` |

The supplied manuscript inputs and authentication credentials are not part of this audit-created package. No original manuscript, PDF, or figure revisions were made. No Lean build or independent v76 PDF build was performed. Prior successful PDF builds were reported, not reproduced.
