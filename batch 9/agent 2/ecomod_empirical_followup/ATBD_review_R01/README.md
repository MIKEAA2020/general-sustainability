# ATBD review R01 for the empirical follow-up

- **[Scientific review and recommendations](ATBD_EMPIRICAL_REVIEW_R01.md)**
- [Proposed article paragraphs — not applied](PROPOSED_ARTICLE_TEXT_R01.md)
- [Page-addressed evidence matrix](EVIDENCE_MATRIX_R01.csv)
- [Source identity and complete chunk inventory](metadata/source_registry.json)
- [Actual review scope and unchanged F08 baseline](metadata/review_scope.json)

All 138 ATBD pages are available. The nine uploads were supplemented by the three release assets covering 106–120. Every chunk matches the author's release SHA-256 digest. A bounded original-PDF comparison matches all 138 whitespace-normalized extracted page texts, while recording parser warnings and the range guard; it is not whole-file/image verification. Full source text, source PDFs and rendered source pages are not redistributed.

This is a targeted source/methods review, not a manuscript revision, new biomass computation, independent validation or changed sample admission. F08's 174 distributed files remain unchanged. All eight national physical admissions remain on hold.

## Reproduce source checks

Install `requirements.txt`. Use the author's release PDFs or their hash-matched uploaded copies:

```sh
python src/prepare_sources.py --cache /external/review-cache --uploads /your/upload-folder --release metadata/release_assets.json
# Optional strict HTTP-range text comparison; not a full original-PDF download:
python src/verify_official_text.py --cache /external/review-cache
python -m unittest discover -s tests -v
```

Raw chunks and extracted text stay in the external cache. Each missing release asset is bounded at 25 MB; known digests and lengths reject drift. The original-PDF reader accepts only pinned-ETag HTTP 206 ranges and bounds distinct source bytes at 25 MB. Its optional object reads can hit that guard; the report distinguishes text-comparison results from complete document-object access. No existing raster/native limit changes.

The official source index identifies separate E3UB v7, PVIR v7, validation-plan v6 and algorithm-change v7 documents. Their links are supplied in the review; their PDF bodies were not read in R01. Those are next empirical-methods tasks, not presumed completed work.

No older draft or ECOMOD package was restored into the workspace. The review is a small add-only repository package; original PDF uploads remain unchanged and newly fetched chunks remain in snapshot-excluded cache.
