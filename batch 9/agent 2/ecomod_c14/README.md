# Biocapacity composition model: manuscripts, data and code

## Manuscripts

- [Main article](ecomod_main.pdf) and [LaTeX source](ecomod_main.tex)
- [Supplementary Information](ecomod_supplement.pdf) and [LaTeX source](ecomod_supplement.tex)

## Computational materials

`code/simulate_budgets.py` evaluates the static identification example and the four numerical conditions. `code/verify_budgets.py` checks identities, endpoint/cumulative outputs, numerical bounds and the integrated budgets. The simulation data contain all seven timesteps; trajectories and cumulative integrals are exported at 0.05 yr intervals. Quadrature uses every simulation node.

```sh
python -m pip install -r requirements.txt
python code/simulate_budgets.py
python code/verify_budgets.py --full
bash code/build.sh
```

The computations implement the model equations and the time/history convention specified in the article. Contribution budgets characterize model trajectories, not observational causal effects. The computations do not estimate empirical physical-stock changes. Figure origins and computational verification are recorded in `metadata/`.

Compilation requires TeX Live with latexmk, elsarticle, recommended fonts, CM-Super, xurl and the LaTeX packages declared in the sources. All figure and table dependencies are local. Recompilation can change PDF byte hashes because of timestamps or software/font versions; numerical reproducibility is assessed separately from file integrity. `artifact_manifest.json` provides SHA-256 hashes and byte sizes for the distributed files, excluding the manifest itself.
