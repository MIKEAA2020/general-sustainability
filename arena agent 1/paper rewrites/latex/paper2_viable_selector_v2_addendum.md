# Viable-Selector Paper — v2 Addendum (layout repair)

**Version:** `paper2_viable_selector_v2` (lineage: `paper2_viable_selector_*`; base v1).
**Scope:** layout repair only. **No content, statement, proof, or numerical claim changed** — the verification record (`paper2_viable_selector_v1_verify.py`, 7/7) applies verbatim to v2; the script is unchanged and is shipped unchanged alongside v2.

## Defects repaired (all found in the v1 build log as Overfull \hbox)
1. **Table 1 exceeded the text width** (277.5 pt overfull) — the specialization table's four `l` columns overflowed the 180 mm page. Converted to wrapping ragged-right paragraph columns (24/50/46/38 mm, `>{\raggedright\arraybackslash}p{...}`), total within measure.
2. **The recursive-selector definition display** overflowed its column (328.5 pt) — split into an `align*` with the membership condition broken over three lines.
3. **The timing-identity display** (Proposition 4) and the **meta-theorem intersection display** overflowed (160.0 pt / 5.7 pt) — each split into two aligned rows.

## Build verification
- Tectonic 0.15.0; `main.pdf` 131,844 B, 4 pp; **zero Overfull \hbox warnings** in the build log (v1 had four).
- pymupdf probes: 0 unresolved `??`; Table 1 caption and body render.

## Files
- `paper2_viable_selector_v2.tex` / `.pdf`; `paper2_viable_selector_v1_verify.py` (unchanged verification record)
- `paper2_viable_selector_v2_source.zip` (README + tex + pdf + verify script)
- v1 files remain untouched in place.
