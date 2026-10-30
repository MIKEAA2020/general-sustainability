# Additional provider-PDF cleanup disclosure

**Action date:** 2026-10-31  
**Status:** complete locally; deletion record included in this additive package.

## Safeguard applied before deletion

Each PDF was freshly retrieved from its pinned provider URL. The fresh response had HTTP 200 and was **byte-identical** to the local copy, including byte count and SHA-256. Only after that exact reproducibility check was the local PDF deleted. No provider PDF is redistributed in this package.

| Deleted local file | Provider | Bytes removed |
|---|---|---:|
| `source_followup_documents_2026-10-30/finland/Hiilinielulaskennan_epavarmuusanalyysi_6_2026.pdf` | Luke/Jukuri, Report 6/2026 | 4,368,237 |
| `source_followup_documents_2026-10-30/finland/luke-luobio_12_2026.pdf` | Luke/Jukuri, Report 12/2026 | 4,371,033 |
| `source_followup_documents_2026-10-30/canada/Estimation_procedures_v1.13.pdf` | Canada NFI | 384,451 |
| `source_followup_documents_2026-10-30/canada/NFI-Business-Process-Version-8.0.pdf` | Canada NFI | 1,955,090 |
| **Total** | **4 files** | **11,078,811** |

The complete pinned URLs and SHA-256 hashes are in `metadata/provider_pdf_cleanup_result.json`; they are also embedded in the restoration script’s input record.

## Retained material

No other files were deleted in this action. In particular, the following remain:

- all three text extracts listed in the cleanup result;
- source retrieval metadata and URL records;
- `deeper_source_audit_followup_2026-10-30/scripts/retrieve_followup_sources.py`;
- every C18/C19 numerical/package dependency, including F11–F15 materials needed by F16;
- all frozen release and governance files.

The workspace’s logical file total immediately before this deletion was **101,085,700 bytes**; immediately afterward it was **90,006,889 bytes**, matching the 11,078,811-byte reduction. Subsequent GA01/R02 documentation and verification files are new retained work and are not counted as cleanup.

## Recovery

From this package, run:

```bash
python code/restore_provider_pdfs.py --workspace-root /path/to/workspace
```

The script downloads only these four documents, verifies both size and SHA-256 before writing, uses atomic file replacement, and refuses to overwrite a different existing file. A provider-side change or outage would prevent exact restoration until the pinned copy is again available; no claim of permanent provider availability is made.
