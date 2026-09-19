# paper3 supplementary package, v49 line (2026-09-19)

The article text of this line is `manuscript/paper3_material_ledgers_v49.{md,tex,pdf}` (54 pages).
Alongside it: the supplementary material (19 pp), the certification-procedure companion (10 pp) and
the standards-horizon companion (8 pp). The three companion documents are byte-identical to the
delivered v48 line — v49 changes the article only — and the hashes are in `MANIFEST.md`.

## What v49 changes

The abstract and Section 1 are the author's own adaptation of the article, repaired against the
deposited article: the renamed vocabulary is reverted to the deposit's terms, the four invented
assertions are gone, the two-level headings are cut while the deposited article's two-senses
passage is carried over verbatim, and Section 1's numbers and citations are gated like any other
section's. The body is the v48 body with six sentences restored that v48's rewrite pass had dropped
(`NOTES_v49.md`, and E8 in `ERRATA_v48.md`).

## How the build was checked

`disclosure/v49_verification.json` (FAILURES: none) and `disclosure/v49_gate_report.json`
(flag_count 0, 14 disclosures, Section 1 checked against 140 ledger rows):

* verbatim-protected reuse rows outside the waived region: 143/143 present in the body;
  1 sat in the waived region and are freed by the ruling;
* back matter (references, availability statements, declarations) byte-identical to v48: True;
* body numerals unchanged: 365 → 365; no Section 1 numeral without deposit support;
  17 Section 1 citations all resolved;
* the compiled PDF carries 187/187 flowing markdown paragraphs; unresolved refs 0;
  no overfull box ≥ 6pt in any document; the LaTeX body is byte-identical to v48's after undoing the
  six sentences this build inserted: True;
* the delivered v48 package was not touched: 2202539 B, sha256 3ad72c04…564fa7.

## Recompile and re-verify

```sh
python3 builders/build_v49_base.py     # writes revision/v7/paper3_material_ledgers_v49.md + logs
python3 builders/build_v49_tex.py       # transpiles, compiles, fits; writes the compile report
python3 builders/verify_v49_base.py     # the nine checks above; exit code is the failure count
python3 builders/v49_waiver_gate_v1.py --control   # demonstrates the checks bite (7 flags on the v48 front matter)
```

`tools/tectonic` (0.17.0) is needed to compile; it is kept out of the package and of the archive
because of its size, and is described in `builders/texkit_v1.py`'s header.

## Licence and third-party material

The article is CC BY 4.0. The scripts in `builders/` accompany it under the same licence; attribution
as the article's. The GFN NFA tables (16 MB of third-party data) are deliberately not in this
package: the notice in `disclosure/open_items_v48.md` records where they came from and that they
remain untouched outside the archive. No other third-party data is included.
