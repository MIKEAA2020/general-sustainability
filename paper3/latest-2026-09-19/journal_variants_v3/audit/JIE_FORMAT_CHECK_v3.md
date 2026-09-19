# JIE format check v3

Date: 2026-09-19

## Journal identification

The target is the Journal of Industrial Ecology, Springer Nature journal 44498. Current guidance:

- name-and-year citations in parentheses;
- reference-list entries alphabetized by first-author surname;
- DOI links supplied in full where available;
- tables numbered with Arabic numerals and cited consecutively;
- figures numbered with Arabic numerals and cited consecutively;
- captions supplied in the manuscript text;
- source files may be submitted in LaTeX.

## Applied corrections

- Replaced the previous unnumbered embedded comparison tabular with Table 1, a caption, a label and an in-text cross-reference.
- Kept the figure as a separate PNG and moved the full caption into the TeX source.
- Configured the figure label as `Fig. 1` and the table label as `Table 1`, with no numbered reference-list system.
- Reworked the reference list into separate hanging entries, alphabetized by first author.
- Formatted same-author 2026 works as Abaee (2026a), Abaee (2026b) and Abaee (2026c), with matching entries in the reference list.
- Used ampersands for two-author parenthetical citations and references, consistent with the current APA-oriented examples.
- Kept all three public companion records and their DOI links.
- Expanded the abstract to 160 words and reduced the keyword list to six terms.

## Build check

The source-only ZIP was extracted into a clean temporary directory and compiled with Tectonic 0.15.0. Result: successful 11-page PDF; no fatal TeX error, undefined reference, missing asset or emergency stop.

## Security check

The v3 source, assets, ZIP, PDF, log and audit files contain no credential markers. The credential file used for optional Git authentication is not staged, copied into the package, placed in a checksum file, or included in the ZIP.
