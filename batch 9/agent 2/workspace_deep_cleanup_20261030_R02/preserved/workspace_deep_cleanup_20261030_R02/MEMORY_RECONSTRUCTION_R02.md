# Recoverable cache work — reconstructed from retained conversation context

This is a **reconstruction**, not a claim to have recovered an original cache file or console transcript byte-for-byte. No scientific result is newly inferred from memory; published sources, data and verification reports remain authoritative.

## Recoverable operational content

1. **Repository acquisition workflow.** C18 started from main commit `d21febdf35aff3b2f38c4f61b1cdbd551a220373`. The initial acquisition recovered 169 files; a further 20 came from the older audit package, including the Edition 2026 workbook and exact OWID inputs. Git blob identities and SHA-256 values were checked. The original temporary `acquire.py` is not available exactly; `code/recover_C18_sources_R02.py` replaces its useful recovery function using the retained 189-file manifest.
2. **Version correspondence investigation.** v42/v43 drawdown values agreed; v44 recovery endpoints differed. C18's current-quality implementation matched v44, whereas the selected law was delayed quality. This was why an older CSV was preserved as a reference rather than relabelled as the selected result. Full-precision comparisons and the selected regenerated grid are already published with C18.
3. **Budget execution sequence.** The original C17 budget checker was run with `--full` in a disposable copy, then its reference-refinement checker was run. The purpose was to avoid altering `inherited_C17/`. All 28 recomputations passed. C18's retained `reproduce_baseline_budgets_C18_A01.py` now implements that isolation directly.
4. **Reproduction sequence.** Run the empirical pipeline, two-land supplemental pipeline, one-stock comparator pipeline, then the source constructor/document builder and the normal/optimized 40-test regression suite. These are retained executable scripts, not instructions to recompute scientific conclusions from remembered numbers.
5. **Build troubleshooting.** The transient environment initially lacked `pdflatex`; the failed attempt returned command-not-found. Installing `texlive-latex-extra`, `texlive-publishers` and `poppler-utils` supplied the build/render tools. A `Misplaced \\noalign` error at a generated supplementary table was resolved by placing its final `\\bottomrule` inside the row-input file, as in the inherited tables. The retained constructor incorporates that fix.
6. **Comparator CSV troubleshooting.** A refinement CSV initially had an extra key absent from the first row's field list. The writer was changed to use the union of keys. The published comparator pipeline contains the corrected implementation.
7. **Visual QA.** All pages were rendered for contact-view review; changed figures/tables were also examined at readable resolution. Closely spaced Figure 1 demand labels were moved apart with leaders, triangle colors were matched to the curves, and plotting text was enlarged. The final PDFs and figure-producing code preserve the result; original unarchived thumbnails can be regenerated from those PDFs.
8. **Publication.** C18 package commit `688701d6053ea1d89a37b9c708ef29c9b2e8ddf5`; receipt commit `f729cce6881ed0ad876cabbceafe7f6675235900`. The published receipt records 272 byte-verified new files, 8,812 prior paths preserved, 41 main pages, 31 SI pages, 28 recomputations and 40 tests in each Python mode. The archived receipt is authoritative, rather than a newly invented console transcript.

## What this does not recover

Unrecorded timings, exact temporary filenames, deleted binary build intermediates, all original parser/environment diagnostics, and the byte layout of unarchived stdout are not recoverable reliably from memory. They are not fabricated here. Rebuilding may produce different PDF hashes because of timestamps and tool versions; numerical and source integrity checks remain separate.

## Useful replacement artifacts

- `code/recover_C18_sources_R02.py`: selective, hash-checked retrieval of missing C18 source inputs from their exact Git blobs; refuses differing local files.
- `metadata/C18_pinned_tree_reconstructed_R02.json.gz`: repository tree regenerated from the immutable pre-C18 source commit. Its repository content is authoritative; serialization is new, not the original cache file.
- Existing C18 build, pipeline, budget and test scripts: regenerate useful outputs instead of retaining disposable caches indefinitely.

No manuscript, numerical CSV, figure, or historical report is modified by this reconstruction.
