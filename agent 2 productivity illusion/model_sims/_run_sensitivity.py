"""Runner for the r1_r2_sensitivity computations, writing results to JSON.

Kept separate so the heavy RK4 grid sweeps run once in the background and
their exact outputs can be read into the manuscript edits + saved as a record.
"""
import json
import os
import time

from model_sims import r1_r2_sensitivity as S

OUT = os.path.join(os.path.dirname(__file__), "..", "data",
                   "r1_r2_sensitivity_results.json")
OUT = os.path.abspath(OUT)


def main():
    res = {}
    t0 = time.time()
    res["rho_validity"] = S.rho_validity()
    print("rho_validity %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time()
    res["bG"] = S.r1_sensitivity_bG([0.4, 0.6, 0.8, 1.0, 1.2])
    print("bG %.1fs" % (time.time() - t0), flush=True)

    # Grid check: finer IC grid (step 0.05) but SAME integration (dt=0.5, T=1200)
    # so the comparison isolates grid-resolution, not integration error.
    t0 = time.time()
    rows = []
    for tg in (30, 40, 50, 60):
        fine = S.recover_fraction(float(tg), 0.0, dt=0.5, T=1200.0,
                                  gridA=S.FINE_GRID["gridA"],
                                  gridP=S.FINE_GRID["gridP"])
        coarse = S.recover_fraction(float(tg), 0.0, dt=0.5, T=1200.0,
                                    gridA=S.COARSE_GRID["gridA"],
                                    gridP=S.COARSE_GRID["gridP"])
        rows.append(dict(tau_g=tg, fine=round(float(fine), 4),
                         coarse=round(float(coarse), 4),
                         ratio=round(float(fine) / float(coarse), 2) if coarse else None))
        print("tg=%s %.1fs (fine=%.4f coarse=%.4f)" % (tg, time.time() - t0, fine, coarse),
              flush=True)
    res["grid_check"] = rows
    print("grid_check done %.1fs" % (time.time() - t0), flush=True)

    with open(OUT, "w") as fh:
        json.dump(res, fh, indent=2)
    print("WROTE", OUT, flush=True)


if __name__ == "__main__":
    main()
