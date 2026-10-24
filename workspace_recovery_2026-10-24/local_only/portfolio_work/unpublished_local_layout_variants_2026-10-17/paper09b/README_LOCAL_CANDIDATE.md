# Paper09b v6 source package

This versioned package contains the assessment/catch transcription extracts, the version-specific threshold verifier, and the inherited record figure. The v6 source reflows the conditional-accounting equation and widens/wraps the summary table; recorded data, rational-arithmetic checks, threshold values, interpretation, and conclusions are unchanged from v5.

Build the main article from this directory with Tectonic 0.15.0:

```sh
tectonic --keep-logs --keep-intermediates -o build/v6 v6.tex
```

Run the independent source/data verifier from this directory:

```sh
python3 paper09b_arv_certification_v6_src/verify_kappa_thresholds.py
```

The verifier uses the included `source_data/` extracts and reports its exact checks; it does not claim to reproduce every descriptive statement in the paper.
