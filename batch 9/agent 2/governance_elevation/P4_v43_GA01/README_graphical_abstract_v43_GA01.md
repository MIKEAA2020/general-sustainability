# Graphical abstract · governance v43 · GA01

A standalone submission asset accompanying the immutable [governance v43 / SI v10 package](https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/governance_elevation/P4_v43_P02).

## Files

- `figures/graphical_abstract_governance_v43_GA01.pdf` — vector submission/print version, 7.2 × 4.64 inches, scalable to a journal's required dimensions.
- `figures/graphical_abstract_governance_v43_GA01.svg` — editable vector, with live text and no external resources.
- `figures/graphical_abstract_governance_v43_GA01.png` — 3600 × 2320 pixels, 500 dpi.
- `CAPTION_graphical_abstract_v43_GA01.md` — full caption, scope, source references and accessible description.
- `data/graphical_abstract_claims_v43_GA01.json` — exact source hashes, numerical values and interpretation constraints.
- `src/build_graphical_abstract_v43_GA01.py` — reproducible vector drawing, not AI-generated decorative imagery or invented time-series data.

## Why the addition is merited

The visual organises the actual scientific argument: one feedback architecture, distinct response laws, delay versus review cadence, and different levels of evidence. It shows the second gated-A stability window, the protective theorem's sufficient conditions and invariant-face exclusions, and the weak/negative field results rather than presenting unconditional protection or validated policy recommendations. The continuum residual/existence distinction remains visible.

The published main manuscript and supplement are **not modified or repaginated**. This is the usual separate graphical-abstract submission asset, not a new scientific revision. ECOMOD C17, all earlier packages, ORCID/declarations and deposit/version-specific citations remain unchanged. No scientific content is deleted or compressed out of the manuscript. The schematic is a companion communication layer, not a substitute for the full assumptions/proofs.

## Reproduce / check

Requires Python, NumPy and Matplotlib, as used in the v43 environment, with the sibling `governance_elevation_P4_v43_P02` package available. Run:

```bash
OPENBLAS_NUM_THREADS=1 python src/build_graphical_abstract_v43_GA01.py
python -m unittest discover -s src -p 'test_*.py' -v
python -O -m unittest discover -s src -p 'test_*.py' -v
```

The builder reads published v43 evidence, verifies that text remains inside the canvas, and emits PDF/SVG/PNG from one layout. The drawing was visually inspected for readable labels, non-overlapping cards/arrows, the two interval bars, and visible field/fold limitations. Each existing remote file must retain its mode and hash during additive publication; every newly published byte is verified and a separate receipt archived. No old publisher is rerun.
