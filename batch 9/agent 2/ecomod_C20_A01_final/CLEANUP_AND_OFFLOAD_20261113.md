# Offload manifest — 2026-11-13 (C20 / ECOMOD)

Purpose: workspace relief without losing access. Every archive below was uploaded to Dropbox
`/ECOMOD_C20_A01/` and **verified byte-identical** (local Dropbox content-hash computed over the
file == content_hash reported by the Dropbox API, sizes equal).

## Streamed (no copy kept, symlinks only)
Live read-only listing: `public_downloads/` served on port 8000 → `https://8000-<sandbox>.e2b.app`
- `EM_upload_C20/` → `../ecomod_C20_EM_upload`
- `C20_package/` → `../ecomod_deposit_doi_C20_A01`
- `ecomod_C20_preprints_source_20261031.zip`
- `ECOMOD_C20_A01_reproduction_package.zip` → `../ecomod_zenodo_deposit/`
- `WORKSPACE_CLEANUP_AND_PUSH_20261031.md`, `READ_ME_FIRST_portal_compile_fix.md`

## Dropbox `/ECOMOD_C20_A01/` (13 files, 51.0 MB of archives + 8.3 MB of packages)

| Archive | Bytes | Dropbox content_hash (verified) |
|---|---|---|
| ecomod_audit_remediation_C18_A01.zip | 12,482,391 | 51173bd53e187685353c1f0677622cea2ffe8aacb5913fa7edc304ff55c015da |
| ecomod_empirical_elevation_F11_A01.zip | 11,816,739 | e55039804047a0f65d0103b4a56258de7a5daa91eb7135ba4a284daac0bfeffa |
| governance_elevation_P4_v43_P02.zip | 8,320,036 | 5ff576eda872b86f0da1dd5835c9acdc0f2ebdba351094e482801a6a8a131ef5 |
| ecomod_empirical_closure_F12_A01.zip | 6,690,743 | 03d692fa694506ff6c46ba2afaa5847828597cad785eed951d655a6a84b4810c |
| ecomod_editorial_division_C19_A01.zip | 6,581,138 | 6161ad56ff51971e86f3fbe401bbd93977b978b124480ce405841a419a417658 |
| ecomod_empirical_elevation_F16_A01.zip | 2,219,757 | b662fe698e4a4d171629faa9bfd0107ec96932c4718b27c5e38583904542eb69 |
| ecomod_editorial_restoration_F15_A01.zip | 1,908,987 | 6b98bf691dab290932a83c2d17a03510de5e56f6f0b4777314725106f111dd53 |
| ecomod_editorial_integration_F14_A01.zip | 1,747,077 | 0bc95342b628e9d226bdbe94c1f5c7a1f7cfbcdfc412fc07c273979d17926cdf |
| ecomod_empirical_integration_F13_A01.zip | 1,614,808 | a90c94618c002a4f378587cb902b2b2f87779298c763057678327453f5f6bf4a |
| ECOMOD_C20_A01_EM_upload_set.zip | 2,005,172 | 4a524691cb36eeb6c917ef889748440ae047fe0740f7e61f422bd56aa4e05aa3 |
| ECOMOD_C20_A01_reproduction_package.zip | 6,021,179 | 8bfee8f8829885957c086fe964c0dc5bf1eebf1bc28b8b59ddfdce0911901436 |
| ecomod_C20_preprints_source_20261031.zip | 228,852 | e764328bfaf4f85bf450ced3135e7fa84f187bd1a0b95015965947ee324b83df |

## Independent anchors (not dependent on Dropbox)
- Zenodo Dataset DOI `10.5281/zenodo.24092131` — reproduction package, 6,021,179 B, md5 `8a51345b76609063d10c8a282c1b8387` (matches published record).
- GitHub `MIKEAA2020/general-sustainability` @ `main`, `batch 9/agent 2/ecomod_C20_A01_final/` — commits `b26504d…`, `2a63509…`.
- Preprint of record: `10.20944/preprints202611.0852.v1`.

## Restore any offloaded root
```
# from Dropbox /ECOMOD_C20_A01/<name>.zip
unzip <name>.zip -d /home/user/
# and/or, for the reproduction package:
curl -L -o ECOMOD_C20_A01_reproduction_package.zip \
  https://zenodo.org/records/24092131/files/ECOMOD_C20_A01_reproduction_package.zip
md5sum ECOMOD_C20_A01_reproduction_package.zip   # expect 8a51345b76609063d10c8a282c1b8387
```

Dropbox usage after upload: 1,444,784,827 B of 2,147,483,648 B (~1.35 / 2 GB, 67%).
