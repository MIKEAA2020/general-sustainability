# Paper08 v50 delivery

- `v50.tex`: layout-corrected successor to v49; equations, numbers, and claims are unchanged.
- `paper08_governance_delay_v50_src/`: figure assets and build notes.
- `paper08_governance_delay_v50_supplementary_delay.md` and `paper08_governance_delay_v50_supplementary_governance.md`: v50 companions, carried forward from v49 with provenance metadata updated.

Build from this directory with Tectonic 0.15.0:

```sh
tectonic --keep-logs --keep-intermediates -o build/v50 v50.tex
```
