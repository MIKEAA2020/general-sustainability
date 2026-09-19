# JIE supplement v1 validation and audit record

Date: 2026-09-19 (Asia/Tehran)

## Deliverables

- `paper3_JIE_supplement_v1.tex` — standalone source.
- `paper3_JIE_supplement_v1.pdf` — compiled 13-page PDF.
- `paper3_JIE_supplement_v1.log` — retained TeX log.

## Build

Command:

```text
/home/user/tools/tectonic --keep-logs --outdir /home/user/revision/jie_latest /home/user/revision/jie_latest/paper3_JIE_supplement_v1.tex
```

Result: exit status 0. Tectonic completed its auxiliary rerun and PDF conversion. The final log reports:

```text
Output written on paper3_JIE_supplement_v1.xdv (13 pages, 63100 bytes).
```

The PDF was written successfully. The final TeX log contains no `!`, `error:`, `Warning`, `Overfull`, `Underfull`, `undefined`, `Missing` or unresolved-reference diagnostics.

## Scope/content audit

The source was checked for the following required modules:

- PASS — typed-ledger certification stack (`typed -> balanced -> conserved -> admissible -> safe -> closure-certified`).
- PASS — extended theorem inventory: flux reconstruction, conservation, flux envelopes, barriers, uniform-drift horizons, critical-margin budgets, finite-donor mass/positivity/no-rest/integrability results, compartmental depletion, first-passage limits, aggregation obstruction and double-counting safeguard.
- PASS — delay-dynamics interface with the exact identity `q E N - R = -dot N`, abstract memory/lag terms, open versus closed completion distinction, frozen-donor limit and explicit non-claims about reduction, Hopf transfer and periodic-orbit transfer.
- PASS — full groundwater, phosphate and fisheries numeric tables.
- PASS — application contract table with observable, unit, denominator, barrier/reference, interpretation, source status and explicit non-claim columns.
- PASS — operational weak- and strong-sustainability definitions, closure capacity, componentwise barriers, substitution constraints and the aggregate-versus-componentwise boundary.
- PASS — record-relative and source-vintage caveats retained; no new calibrated empirical claim or forecast introduced.
- PASS — credentials scan: no password, API key, access token or private-key text in the TeX source.

## Structural checks

A dependency-free source check returned PASS for:

- exactly one `document` environment;
- balanced `equation`, `align` and `longtable` environments;
- all three application table labels (`tab:g3p`, `tab:phosphate`, `tab:fisheries`);
- required delay, double-counting, weak/strong and non-claim strings.

The main JIE word-count limit is unaffected: this is a separate supplementary file and is not part of the 6,000-word main-text count.

## SHA-256

```text
1331761b0aad6c189ccc5bec2a72fce279c9a74db6abede22141d74e4316bdf3  paper3_JIE_supplement_v1.tex
1b471fc68bf27f511521d1804ab704895971160bb1d78f54cb2aad580648cd1d  paper3_JIE_supplement_v1.pdf
cdbadc48fcb04ac7316e40f33aad6f500ed9b92177e5a7e024eedc26be8a8b67  paper3_JIE_supplement_v1.log
```

## Evidence/status note

The supplement is traced to `/home/user/revision/v7/paper3_material_ledgers_v49.md` and preserves the v49 distinctions between closed finite-donor accounting, open institutional completion, record-relative public-data arithmetic and non-claims. The Figshare DOI is used only as a contextual public record pointer; this local supplement is not represented as an externally uploaded DOI record.
