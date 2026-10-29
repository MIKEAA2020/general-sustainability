# Empirical follow-up F09 — source-grounded uncertainty and validation interpretation

- [Main manuscript F09](followup_F09_main.pdf) · [LaTeX](followup_F09_main.tex)
- [Supplementary Information F09](followup_F09_SI.pdf) · [LaTeX](followup_F09_SI.tex)
- [Companion-document review](SOURCE_REVIEW_F09.md) · [22-finding evidence matrix](EVIDENCE_MATRIX_F09.csv)
- [Exact revision/preservation account](metadata/revision_record_F09.md)
- [Current source links and access scope](INPUT_LINKS_F09.md)
- [Remaining empirical work](REMAINING_EMPIRICAL_WORK_F09.md)
- [Unchanged eight-country admission table](data/support/physical_admission_F08.csv)

## What F09 does

Integrates the completed ATBD review R01 and targeted E3UB/PVIR/PVP/ADPC review into a new scientific main/SI. It acknowledges current independent v7 **stock** validation and existing within-stack/spatial covariance propagation, while distinguishing them from validated **local paired forest change**, final-map cross-year covariance, mixed-cell allocation and calibrated coverage. The external review records two visually confirmed printed-equation inconsistencies without claiming a verified provider-code defect or silently implementing a correction.

The compiled main manuscript and SI are **11 pages each**. No original numerical result is changed. Both local allocation-difference sets still contain zero; these remain conditional identification sets, not confidence intervals. All eight country admissions remain on hold. The ORCID, seven keywords and exact approved AI sentence are preserved. F08 and previous packages are unchanged.

## Reproduce technical checks

```bash
python -m pip install -r requirements_F09.txt
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
bash src/build_F09.sh
python src/finalize_checks_F09.py
```

Compilation requires latexmk and the standard LaTeX recommended/extra/font packages. The scripts do not fetch new ecological data during these tests. The source-identity check is separate:

```bash
python src/verify_companion_sources_F09.py --cache ../.cache/cci_companion_R02
# Explicit, optional retrieval if the excluded cache is absent:
python src/verify_companion_sources_F09.py --download --cache ../.cache/cci_companion_R02
```

The source downloader pins final media URL, ETag, length and full SHA-256 under an unchanged 25 MB per-document transfer guard. It does not redistribute source documents or verify the provider implementation. Tests and analytic checks are not ecological validation.

## Inheritance and current records

Unchanged F04–F08 data, algorithms, configurations and history retain their filenames and historical claims. `README_inherited_F08.md`, `INPUT_LINKS_F08.md`, older revision/test records and the inherited `configs/study_design.json` are **historical**; the F08 access statement that ATBD was unread is not F09's current status. Current scope is recorded in `configs/revision_scope_F09.json`, this README, current review and current QA files. The scientific study design itself is unchanged.

Current compilation/tests and preservation checks are in `metadata/verification_F09.json` and versioned test logs. The artifact manifest excludes caches and itself. Raw source PDFs, full extracted text, source-page images, compiler caches and credentials are not publication artifacts. No earlier local package was deleted during this revision.
