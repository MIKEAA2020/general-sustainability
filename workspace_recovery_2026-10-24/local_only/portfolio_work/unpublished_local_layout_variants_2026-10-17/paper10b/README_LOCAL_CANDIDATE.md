# Paper10b v4 delivery

- `v4.tex`: layout-corrected successor to v3; the two URLs and code-availability references are reflowed; computation, data, protocols, and substantive claims are unchanged.
- `paper10b_edwards_aquifer_v4_src/`: annual panel, reproducible sensitivity verifier and outputs, figure asset, and package README.

Build from this directory with Tectonic 0.15.0:

```sh
tectonic --keep-logs --keep-intermediates -o build/v4 v4.tex
```

Run the package's post-freeze sensitivity verifier with Python 3 and NumPy from the package directory:

```sh
python3 verify_660_attractor_bootstrap.py
```
