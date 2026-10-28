# Paper06 v77 — final local build and QA record

**QA date:** 2026-10-27  
**Status:** Successful local build. This record does not authorize an external release.

## Build and source synchronization

- Engine: Tectonic 0.17.0 (version recorded in `tectonic.version.txt`).
- Command: `TEX_ENGINE=/tmp/paper06-tectonic-0.17.0/tectonic ./build_v77.sh` from the v77 package directory.
- `assemble_v77.py` regenerated both assembled sources from 9 main modules and 4 SI modules. `python3 assemble_v77.py --check` passed after the final source edits.
- Main article compiled before SI; both Tectonic builds exited successfully. TeX scratch intermediates were removed by the build script.

## PDF, reference, and page checks

| File | Pages | Page size | Bytes | SHA-256 |
|---|---:|---|---:|---|
| `paper06_assessment_separation_v77.pdf` | 47 | 612 × 792 pt | 1,225,419 | `e574faf46185a54f63365beffec9921f421d2572c32090b7406553d4e13abc88` |
| `paper06_assessment_separation_v77_supplementary.pdf` | 29 | 612 × 792 pt | 258,124 | `213ed33a0978d79deac13c50054721c956146e9bdf2fb0458ff59ed39558362f` |

PyMuPDF extraction found no blank pages and no `??` markers in either PDF. Build-log checks found no unresolved references or citations, duplicate labels, missing-file errors, or fatal TeX errors. The main article ends with references on p. 47; the SI ends with references on p. 29.

The logs retain nonfatal layout/font/metadata warnings, not suppressed:

- One 2.43091 pt output-active overfull box in each PDF build.
- One 1.73424 pt SI paragraph overfull box at assembled SI lines 179–194; it was checked in-page and is not visibly clipped.
- Underfull boxes remain in both documents.
- The main log retains hyperref PDF-string warnings for author-note commands; both logs retain `TU/lmr/m/scit` font-shape substitution warnings.

No oversized-float warning was reported after the terminology map was split.

## Visual review

Final-PDF renders were inspected for Figure 2 and the modified verification/benchmark passages:

- Main: pp. 18 (Figure 2, including a 4× render and enlarged crops of both labels), 26 (common-shock verdict and model-relative wording), and 47 (references).
- SI: pp. 7 (common-shock proof), 11–14 (historical verification qualifications and coupled-shock discussion/table), 18 (terminology map), and 29 (references).

Figure 2 was also inspected as a full source PNG and enlarged panel crops. In both panels, each `$s_1+s_2=2$` label is parallel and immediately adjacent to the diagonal, on the unhatched gray side; the raster and PDF crops show a small gap, with no contact or overlap. The equality text no longer reads as a label for the hatched region. The SI S4 table and S6 acceptance-gap definition fit in-page; the terminology row states the all-weight licensing/no-common-typed-plan criterion.

The benchmark figure and caption remain labeled in MBU/yr. No clipping or blank-page issue was observed in the reviewed pages.

## Evidence and release limits

- No Lean build was run for v77.
- Historical verifier counts are identified as finite reports only. The corresponding historical checker files/run logs were not found in the inspected versioned packages; they are not represented as reproduced v77 artifacts or continuum certificates.
- The coupled-shock readings are presented as distinct, non-ordered model specifications, not as bounds on physical truth. Benchmark implications are model-relative, not empirical estimates or management prescriptions.
- DFO values are an assessment-vintage historical scale comparison only; no fit, forecast, validation, current-threshold, or empirical-performance claim is made.
- V76 and earlier releases remain unchanged. ECOMOD c10 and its pins, c8/c9, `main`, checksums, and DOI deposits were not edited. V77 remains local; no push or deposit occurred.

## Reproduction

From the package directory, verify the delivered snapshot with `sha256sum -c SHA256SUMS_v77.txt`. To rebuild, run `python3 assemble_v77.py --check` and `TEX_ENGINE=/path/to/tectonic-0.17.0 ./build_v77.sh`. After any intentional edit/rebuild, refresh the snapshot with `./checksum_v77.sh`, then run `sha256sum -c SHA256SUMS_v77.txt`.
