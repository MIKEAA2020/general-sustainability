# JIE Supplementary Information validation record

Date: 2026-09-19 (Asia/Tehran)

## Deliverables

- `paper3_JIE_supplement_v1.tex` — standalone Supplementary Information source.
- `paper3_JIE_supplement_v1.pdf` — compiled 13-page PDF.
- `paper3_JIE_supplement_v1.log` — retained TeX log.

## Build

```text
/home/user/tools/tectonic --keep-logs --outdir . paper3_JIE_supplement_v1.tex
```

Result: exit status 0. The final log reports:

```text
Output written on paper3_JIE_supplement_v1.xdv (13 pages, 63348 bytes).
```

The Supplementary Information log contains no TeX errors, unresolved references, overfull boxes, underfull boxes or missing-delimiter diagnostics.

## Content and style audit

- PASS — typed-ledger certification stack and extended theorem inventory.
- PASS — finite-donor mass, positivity, no-rest, integrability, aggregation and double-counting results.
- PASS — first-passage limits and explicit distinction between surrogate processes and physical ledger hitting times.
- PASS — institutional-delay interface, decline-pressure identity, memory/lag notation and non-reduction result.
- PASS — full groundwater, phosphate and fisheries application tables.
- PASS — observable, unit, denominator, barrier/reference, interpretation, source-status and explicit non-claim fields.
- PASS — operational weak- and strong-sustainability definitions with closure capacity and componentwise barriers.
- PASS — formal author block with linked ORCID and email.
- PASS — formal citations to the principal article and the two related papers: Figshare records `33942451`, `33942469` and `33942487`; the institutional-delay analysis is cited separately by its Zenodo DOI.
- PASS — no references to superseded manuscript versions, internal change logs or unpublished project history.
- PASS — credential scan: no password, API key, access token or private-key text in the source.

## Structural checks

- exactly one `document` environment;
- balanced `equation`, `align` and `longtable` environments;
- all required application-table labels present;
- author, ORCID, email, DOI and non-claim strings present;
- no unresolved references or TeX errors.

The Supplementary Information is separate from the JIE main-text word count.

## SHA-256

```text
50a08577a625e3e82ea8e0a6af51889e7ce8417e6756187e597a725cb16c9ffe  paper3_JIE_supplement_v1.tex
f72cf6053afb79b09650a3d0d65f0e833247be8132346ac526125c5af6a732a0  paper3_JIE_supplement_v1.pdf
f7e88537ecbd1bfbe5b999d45fbe972ade0fa719e0cb97be348a02b2ba2b9598  paper3_JIE_supplement_v1.log
```
