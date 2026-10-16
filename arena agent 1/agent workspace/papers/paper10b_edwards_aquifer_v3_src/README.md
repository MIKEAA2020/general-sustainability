# Paper10b v3 post-freeze coefficient-sensitivity check

`verify_660_attractor_bootstrap.py` extends the existing Section 3.7 residual bootstrap to the institutional 660-ft level. It reproduces the E4 audit's 1934–1990 OLS fit, iid residual resampling, 5,000 refits, seed (`20260905`), UC-min recharge floor, and 500-step policy iteration from 650 ft. It reports all policy-attractor distributions against both the 618-ft physical threshold and the 660-ft institutional threshold. The script also checks the existing 618-ft bootstrap shares and uses the zero-pumping affine fixed point as a numerical cross-check.

The panel is copied from `wave_e_edwards/data/annual_panel.csv`; its SHA-256 is written into the zero-pumping output row. Run with Python 3 and NumPy:

```sh
python verify_660_attractor_bootstrap.py
```

Outputs:

- `policy_attractor_bootstrap_660.csv`: one row per policy, including bootstrap quantiles and shares at/above both thresholds.
- `zero_pumping_660_bootstrap.csv`: concise zero-pumping sensitivity summary.

The added 660-ft statistic is a **post-freeze model-fit sensitivity**, not a new retention gate. It conditions on the fitted one-pool structure, the constant UC-min recharge floor, the observed training window, and iid residual resampling. It does not recompute viability kernels, test the live 10-day CPM algorithm, propagate recharge-floor uncertainty, or estimate the probability of real-world safety. A refit share above 660 is evidence that the point-fit no-invariance conclusion is coefficient-sensitive, not evidence that pumping policy maintains the threshold in the aquifer.
