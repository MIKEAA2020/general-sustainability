# Journal variants implementation record

**Date:** 2026-09-19  
**Source:** full-length v49 line  
**Status:** working submission drafts; manuscript content unchanged; final archive package notes mechanically cleaned

## Implemented

### Journal of Industrial Ecology cut

`paper3_JIE_submission_v1.md` and rendered PDF:

- body count: **4,311 / 6,000** under the local math-excluding word gate;
- PDF: **11 pages**;
- focus: MFA, typed material stocks and flows, incidence structure, closure, double-counting, componentwise certification and the three application records;
- full proofs delegated to `technical_supplement_v1.md`;
- includes the reader route, material-flow audit questions, closure interpretation and the new figure.

### Ecological Economics cut

`paper3_EE_submission_v1.md` and rendered PDF:

- body count: **4,245 / 8,000** under the same gate;
- PDF: **11 pages**;
- focus: weak comparability, compensatory aggregation, weak/strong sustainability as a scoped operational interpretation, natural-capital/support-pool drawdown, policy salience and status-labelled applications;
- does **not** promote the weak/strong synthesis to a theorem without the missing closure assumptions;
- includes the reader-facing policy crosswalk and the new figure.

The cuts are intentionally below the ceilings rather than padded with proofs. The technical supplement carries the full proof-bearing sections extracted verbatim from the v49 source. The full-length deposit remains the place for the complete article, supplementary records, companions and computational evidence.

### Shared figure

`assets/typed_ledger_readout.svg` and `.png` implement the accessibility recommendation without changing the accounting claims. The diagram distinguishes:

1. typed state and donor-limited fluxes;
2. service readouts outside conserved mass; and
3. arithmetic compensation versus support-pool drawdown.

### Standalone supplement rendering

`technical_supplement_v1.md` is shipped as an auditable source extract, while the full-length deposit already contains the stable rendered supplementary PDF and both companion PDFs. The shared Markdown renderer was corrected so a leading vertical bar in multiline mathematics is not mistaken for a table. A trial standalone supplement PDF now compiles, but it still has overfull boxes from dense proof tables and is therefore **not** presented as a submission-ready supplement; the existing full-length PDF remains the stable rendered record.

### Route-C prototype

`route_c_prototype/` contains a dependency-free reference core with four passing tests. It implements:

- typed transfer/conversion declarations;
- incidence construction;
- balance residuals;
- componentwise barrier checks; and
- a non-compensation witness.

It is honestly labelled a **prototype**, not a supported EMS package. The remaining requirements for a serious software submission are documented in its README: complete predicate/programme coverage, input schema, API/CLI, solver handling, examples, benchmarks, failure fixtures, packaging, documentation and licence.

## Verification

- journal-variant validator: **PASS**;
- JIE PDF: 11 pages, no empty pages, no `??`, no overfull boxes;
- Ecological Economics PDF: 11 pages, no empty pages, no `??`, no overfull boxes;
- route-C tests: **4 passed**;
- full-length v49 verifier remains: `FAILURES: none / *** v49 verified ***`.

## Figshare-ready full-length deposit

`revision/figshare_deposit/paper3_full_length_figshare_v1.zip`

- 49 zip records / 48 files in the deposit tree at the latest build;
- the current byte count and sha256 are recorded in the sidecar `paper3_full_length_figshare_v1.sha256`, not inside the zip;
- sidecar: `paper3_full_length_figshare_v1.sha256`;
- metadata: `paper3_full_length_figshare_v1/metadata.json`;
- includes the full-length four-document v49 source and PDFs, code and analysis records, technical supplement, both journal cuts and rendered PDFs, figure assets and route-C prototype;
- deliberately excludes the third-party GFN NFA source tables, retaining their manifest/checksums and licence boundary instead.

No Figshare upload or DOI assignment was attempted because no Figshare destination or credential was supplied. The package is ready for that deposit step.

## Editorial status

These are **v1 target drafts**, not silently substituted replacements for the author's full-length article. The manuscript content is unchanged; the final v49 archive package was re-pushed only to clean the NOTES prose and refresh the sidecar/package bytes. Before submission, the author should choose whether each cut needs additional target-specific prose, tables or journal formatting; any approved change should then be line-read, page-checked and re-packaged from the relevant source.
