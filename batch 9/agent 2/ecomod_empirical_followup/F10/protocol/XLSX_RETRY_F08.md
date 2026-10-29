# F08 author-requested XLSX retry and editorial update

Date 2026-10-29. User requests ORCID as in ECOMOD, seven discoverability/novelty keywords, exact new AI-declaration wording, another Excel retrieval attempt and direct links to unavailable/unread inputs. Preserve F07 and earlier packages. The ORCID is copied from the unchanged ECOMOD C17 author metadata, not invented: 0000-0002-0019-1842.

## Narrow limit exception before complete workbook decoding

The former 25MB transfer / 250MB uncompressed-member guards were operational safeguards, not evidence of an inaccessible source. For this expressly requested retry only, allow at most 40,000,000 bytes for the already identified Excel file, 400,000,000 uncompressed bytes per worksheet member and 500,000,000 in total. All native biomass, country-raster and other source limits remain unchanged. The HEAD identity remains 33,714,740 bytes and ETag recorded from F07; F08 HEAD is inspected before freezing this specification. No silent general cap increase.

Pin URL, ETag and length; stream the source with a hard transfer bound, hash the full workbook after successful retrieval, inspect ZIP member paths/sizes and stream worksheet rows using read-only parsing. Do not execute macros, formulas, external links or archive contents. Retain the raw workbook externally, not in the distributed package. Cap at 100,000 data rows and 500 columns; fail closed on unexpected schema, duplicate identifiers, formulas in annual reference fields or changed source identity.

## Audit, not map validation

Profile complete sheet names, schemas, row/ID counts, annual label fields, endpoint nonblank/numeric/text label counts, role flags and weight/probability fields. Compare with the exact F06 public CSV, recovered under its old SHA/ETag and 25MB guard. Normalize only field-name case/whitespace, textual whitespace/Unicode normalization and integral numeric serialization; do not impose an unverified class-code/name crosswalk. Compare per-ID hashes of all common annual CLASS/COUNT/BORDA field payloads and separately inspect 2015/2023 label equality. These are representation/equivalence checks, never map-accuracy estimates or independent reference replications.

For local coverage, join TARGETID to the CSV positions already verified against WGS84 vector geometry in F06. Check Excel coordinate attributes against those positions directly and transposed; do not silently repair axes. Unmatched IDs do not acquire a claimed local position. The unchanged fixed Brazil window must not be moved or enlarged. Missing/unobserved reference labels are not ecological absence. All previous cover, reference and conditional allocation outcomes are already known; this is not an untouched held-out validation or external registration.

No class confusion, transition accuracy, independent-validation certification, biomass recalculation or national inference is authorized by this audit alone. Report the actual workbook result even if it repeats or contradicts the CSV. Explicitly distinguish retrieval failure, cap deferral, metadata-only inspection and successfully fetched but unread documents. Supply direct URLs for remaining gaps, including the previously unread CCI ATBD, and working alternatives to obsolete links. Do not label intentionally bounded global/national rasters as inaccessible.
