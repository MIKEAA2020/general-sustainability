# Biocapacity composition model: main article and Supplementary Information

- [Main article](ecomod_main.pdf), [LaTeX](ecomod_main.tex)
- [Supplementary Information](ecomod_supplement.pdf), [LaTeX](ecomod_supplement.tex)

The article includes the orchard and elevator analogies, their concluding synthesis, explicit research questions, the worked identification example, sharp static bounds and integrated contribution budgets. Mathematical and numerical assumptions are stated scientifically; production history is recorded separately in `metadata/`.

## Reproduce the numerical calculations and compile

```sh
python -m pip install -r requirements.txt
python code/simulate_budgets.py
python code/verify_budgets.py --full
python code/verify_manuscript_sources.py
python code/verify_reference_refinement.py
bash code/build.sh
```

The computations evaluate four specified conditions at seven timesteps. Exported trajectories/cumulative integrals use 0.05 yr reporting intervals; numerical integration uses every simulation node. The static identification implementation uses `L` for total area, consistent with the corrected main equation and SI proof. Numerical trajectory and budget exports are unchanged. Reference-grid diagnostics in the text match the declared computation; their current values are recorded separately in `metadata/reference_refinement.json`.

Compilation requires TeX Live with latexmk, elsarticle, xurl, recommended fonts and CM-Super. All figure/table dependencies are local. PDF byte hashes may change on recompilation because of timestamps, fonts or software versions; numerical reproducibility is distinct from file integrity.

`metadata/provenance.json` records source assets and the numerical implementation. `metadata/author_text_integrity.json` records exact restored author/expository text segments. Computational checks and document checks are separate and do not constitute exhaustive empirical validation. `metadata/revision_record.md` is an external author-facing record, not part of the article. `artifact_manifest.json` lists distributed file hashes and sizes, excluding itself.
