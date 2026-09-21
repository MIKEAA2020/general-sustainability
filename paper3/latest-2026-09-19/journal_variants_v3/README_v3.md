# Journal of Industrial Ecology v3 source bundle

This is a new, non-overwriting v3 source revision. The existing v1 and v2 packages are not modified.

## Target journal

Journal of Industrial Ecology, currently published by Springer Nature:

https://link.springer.com/journal/44498/submission-guidelines

The v3 formatting pass follows the current submission guidance relevant to this source bundle:

- author-year citations rather than numbered citations;
- an alphabetized reference list;
- same-year works distinguished consistently as 2026a, 2026b and 2026c;
- full DOI links where available;
- Arabic-numbered, cited tables and figures;
- figure and table captions supplied in the manuscript source;
- the figure supplied as an external PNG and the comparison table as an included TeX file.

## Source-only ZIP

`paper3_JIE_submission_v3_source.zip` contains exactly:

- `paper3_JIE_submission_v3.tex`
- `table_depletion_readings_v3.tex`
- `typed_ledger_readout.png`

The main TeX file and the two assets are at the ZIP root. From an extracted directory, compile with:

```text
tectonic paper3_JIE_submission_v3.tex
```

or with an installed LaTeX engine using the same main file.

## Verification

The extracted ZIP was compiled with Tectonic 0.15.0. The build completed successfully and produced an 11-page PDF. The abstract is 160 words and the keyword list contains six keywords. The source has one numbered/cited table and one numbered/cited figure.

The v3 package also contains the compiled PDF and log for local verification. They are deliberately not included in the source-only ZIP.

The v3 package also contains the separately compiled supplementary source and PDF. The author affiliation in both the main paper and supplementary source is `Independent Researcher, Tehran, Iran`.

No credential file or credential content is part of this package. Authentication credentials, if used for repository operations, remain outside the package and Git history.
