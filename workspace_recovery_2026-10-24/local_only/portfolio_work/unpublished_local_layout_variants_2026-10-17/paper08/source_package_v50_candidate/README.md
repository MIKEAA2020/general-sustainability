# Paper08 v50 source package

Versioned figure assets for the layout-corrected v50 main manuscript (`../v50.tex`). The files are copied forward from the v49 asset set; no figure data or underlying results were changed.

Build the main article from the Paper08 work directory with Tectonic 0.15.0:

```sh
tectonic --keep-logs --keep-intermediates -o build/v50 v50.tex
```

The manuscript locates these assets through `\graphicspath`. The v50 supplementary companions are published separately alongside the main source as `paper08_governance_delay_v50_supplementary_delay.md` and `paper08_governance_delay_v50_supplementary_governance.md`; their body text and calculations are carried forward unchanged from v49, with only edition/provenance metadata updated.
