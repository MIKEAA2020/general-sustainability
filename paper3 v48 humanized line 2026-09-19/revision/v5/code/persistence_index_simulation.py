r"""Section 8.1 exhibit: boundedness of the persistence index on the declared linear-trend class.

Reproduces the computation quoted in the article. Nothing here is a claim about any basin: the
series are simulated inside the class the article declares for the anomaly index (linear trend plus
iid noise), and the statistic is the article's own fitted-distance-over-fitted-rate form.

Run:  python3 revision/v5/code/persistence_index_simulation.py
"""
import numpy as np

BETA = 1.0
SIGMA = 1.0
REPS = 400
SEED = 7
LENGTHS = (10**2, 10**3, 10**4, 10**5)


def index_for_one_series(a):
    """Section 8.1's statistic: the fitted distance from the current level up to the series' own
    historical minimum, divided by the fitted decline rate.  A downward trend puts the minimum at
    or near the end of the record, so this gap is a noise-scale quantity."""
    n = a.size
    k = np.arange(n, dtype=float)
    slope = float(np.polyfit(k, a, 1)[0])          # least squares, negative under the declared class
    if slope >= 0:
        return np.nan
    return (a[-1] - a.min()) / (-slope)


def main():
    rng = np.random.default_rng(SEED)
    print("beta = %g, sigma = %g, %d replicates per length, seed %d" % (BETA, SIGMA, REPS, SEED))
    print("%8s %14s %14s %14s %14s %12s" % ("n", "index median", "index mean", "index q90", "stock drop", "n usable"))
    for n in LENGTHS:
        vals, drops = [], []
        for _ in range(REPS):
            a = -BETA * np.arange(n) + SIGMA * rng.standard_normal(n)
            v = index_for_one_series(a)
            vals.append(v)
            drops.append(a[0] - a[-1])
        vals = np.array([v for v in vals if np.isfinite(v)])
        print("%8d %14.3f %14.3f %14.3f %14.1f %12d"
              % (n, np.median(vals), np.mean(vals), np.quantile(vals, 0.9), np.mean(drops), vals.size))
    print()
    print("The index stays at the noise-to-trend scale (sigma/beta = %g) while the stock implied by"
          % (SIGMA / BETA))
    print("the same series falls by five orders of magnitude across these record lengths: the")
    print("statistic is a trend-detection quantity expressed in years, not a horizon.")


if __name__ == "__main__":
    main()
