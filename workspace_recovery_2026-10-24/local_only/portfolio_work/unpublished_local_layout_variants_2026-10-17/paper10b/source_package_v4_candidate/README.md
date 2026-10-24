# Paper10b v4 post-freeze coefficient-sensitivity package

`verify_660_attractor_bootstrap.py` extends the existing Section 3.7 residual bootstrap to the institutional 660-ft level. It reproduces the E4 audit's 1934–1990 OLS fit, iid residual resampling, 5,000 refits, seed `20260905`, UC-min recharge floor, and 500-step policy iteration from 650 ft. It reports policy-attractor distributions against both the 618-ft physical threshold and the 660-ft institutional threshold. The script checks the existing 618-ft bootstrap shares and uses the zero-pumping affine fixed point as a numerical cross-check.

The annual panel is copied from `wave_e_edwards/data/annual_panel.csv`; its SHA-256 is written into the zero-pumping output row. Run from this directory with Python 3 and NumPy:

```sh
python3 verify_660_attractor_bootstrap.py
```

Outputs are `policy_attractor_bootstrap_660.csv` and `zero_pumping_660_bootstrap.csv`. The v4 figure is in `figs_e4/fig1_attractors.png`.

The 660-ft statistic remains a **post-freeze model-fit sensitivity**, not a new retention gate. It conditions on the fitted one-pool structure, constant UC-min recharge floor, observed training window, and iid residual resampling. It does not recompute viability kernels, test the live 10-day CPM algorithm, propagate recharge-floor uncertainty, or estimate the probability of real-world safety. A refit share above 660 is evidence that the point-fit no-invariance conclusion is coefficient-sensitive, not evidence that pumping policy maintains the threshold in the aquifer.
