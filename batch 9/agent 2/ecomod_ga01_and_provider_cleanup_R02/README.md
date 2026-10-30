# ECOMOD GA01 and provider-PDF cleanup R02

**Date:** 2026-10-31  
**Scope:** additive graphical-abstract improvement and disclosure of a second, verified local cleanup.  
**Frozen work:** no C17/C18/C19 manuscript, release asset, numerical dependency, or completed publisher is changed.

## Outcomes

1. **The repository graphical abstract merits improvement.** The reviewed repository PNG/PDF still use the older title/design, a 1961–2022 empirical strip, standing-value wording, `R_fc`, and broader collapse/delay language than C19 supports. The older S14 candidate is also obsolete. See [GRAPHICAL_ABSTRACT_REVIEW.md](GRAPHICAL_ABSTRACT_REVIEW.md).
2. **A current replacement candidate is supplied.** GA01 uses C19’s actual selected delayed-quality fixed-demand simulation and the primary NFA 1961–2023 fields. It separates the conditional model run from measured account evidence and explicitly scopes the reduced-branch and recovery claims.
3. **Four provider PDFs were removed locally only after exact fresh-provider matches.** This freed **11,078,811 bytes**. Text extracts, metadata, source URLs, hashes, and the original retrieval workflow remain. See [PROVIDER_PDF_CLEANUP.md](PROVIDER_PDF_CLEANUP.md).

## Graphical-abstract files

Under `graphical_abstract_GA01/`:

- `ecomod_C19_GA01_graphical_abstract.png` — opaque RGB, 1328×531 px, 200 dpi.
- `ecomod_C19_GA01_graphical_abstract.tiff` — opaque RGB, 1328×531 px, 200 dpi, lossless LZW.
- `ecomod_C19_GA01_graphical_abstract.pdf` — one-page vector version, 478.08×191.16 pt.
- `ecomod_C19_GA01_graphical_abstract.svg` — editable vector version with pinned metadata.
- `graphical_abstract_claims_C19_GA01.json` — exact numerical values, scope statements, and source hashes.
- `build_graphical_abstract_C19_GA01.py` — deterministic builder.
- `source_snapshot/` — byte-exact copies of the four C19 model/data inputs used by the builder, making this package independently rebuildable.

The legacy repository graphics are documented by path and Git blob identity but are **not overwritten**. GA01 is a new candidate for the next submission/update, not a silent revision of C19.

NFA-derived empirical values and associated adaptations retain the Lo et al. (2026) attribution and **CC BY-SA 4.0** notice; see `graphical_abstract_GA01/source_snapshot/README.md` and the preserved C19 data-license notice. No provider endorsement is implied.

## Rebuild and verify

```bash
python graphical_abstract_GA01/build_graphical_abstract_C19_GA01.py
python code/verify_package.py --rebuild
```

The verifier builds twice and requires byte-identical PNG, PDF, SVG, TIFF, and claims JSON. It independently recomputes the selected model endpoints and NFA fields; checks source hashes, geometry, RGB/dpi/compression, vector metadata, and scoped wording; verifies the cleanup arithmetic and local deletion invariants; and checks the frozen C18, C19, and R01 manifests when run in the original workspace.

For a standalone downloaded package without those sibling workspace directories:

```bash
python code/verify_package.py --rebuild --skip-workspace-checks
```

The tested environment is recorded in `requirements.txt` and `metadata/verification_result.json`. Renderer/library changes can alter bytes even when the science and layout are unchanged.

## Restore the deleted provider documents

The PDFs are not redistributed in this package. To retrieve the exact provider copies again:

```bash
python code/restore_provider_pdfs.py --workspace-root /path/to/workspace
```

The restoration script refuses hash mismatches and will not overwrite a different existing file. Full pinned URLs, byte counts, and SHA-256 hashes are in `metadata/provider_pdf_cleanup_result.json`.

## Verification and publication

- `metadata/verification_result.json` records the passing two-build verification and frozen-manifest checks.
- `artifact_manifest.json` covers every package file other than the manifest itself.
- `code/publish_GA01_R02.py` is a separate additive publisher. It preserves every pre-existing remote path/mode/hash, publishes only this package and a parent-level receipt, and byte-verifies the uploaded blobs.
- The original C18/C19/R01 publishers were not run.
