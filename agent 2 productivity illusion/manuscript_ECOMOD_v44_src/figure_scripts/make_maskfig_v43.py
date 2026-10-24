"""Rebuild the two-panel masking-window comparator for ECOMOD v43 SI Figure S2.

Run from the package root: python figure_scripts/make_maskfig_v43.py
The simulation/data are unchanged from v42. The mask-window label is moved to
whitespace immediately below-right of the shaded window; legends name units.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mask_rk4 import run

OUT = Path(__file__).resolve().parents[1] / "figures" / "S6_masking_window.png"

def win(A, B, t, mindyrs=1.0):
    on = (np.diff(B) > 1e-9) & (np.diff(A) < -1e-9)
    dt = t[1] - t[0]
    best = None
    i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]:
                j += 1
            span = (j - i) * dt
            if span >= mindyrs and (best is None or span > best[0]):
                a_seg = A[i:j+1]
                a_min_idx = i + int(np.argmin(a_seg))
                a_min = a_seg.min()
                best = (span, t[i], t[j], B[i], B[i:j+1].max(),
                        B[i:j+1].max() - B[i], A[i], a_min,
                        A[i] - a_min, t[a_min_idx])
            i = j
        i += 1
    return best

p = dict(rho=0.05, Amax=1.2, b0=0.5, bG=0.8, eta=0.05, alpha=0.03,
         kappa=0.2, tw=15, deltab=1.5, Aext=0.02, w=0.05)
A0 = 1.0
bA0 = 0.5 * A0
fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))

# Panel A: representative mask trajectory (deficit = 0.06 gha per annual account)
E_rep = 0.56
r_rep = run(p, T=250, dt=0.02, A0=A0, E=E_rep)
t_rep, A_rep, B_rep, D_rep = r_rep["t"], r_rep["A"], r_rep["B"], r_rep["D"]
s_rep = win(A_rep, B_rep, t_rep)
ax[0].plot(t_rep, A_rep, label="stock A (model units)", color="#1f77b4", lw=2)
ax[0].plot(t_rep, B_rep, label="biocapacity B (gha)", color="#d62728", lw=2)
if s_rep:
    t0, t1 = int(s_rep[1]), int(s_rep[2])
    ax[0].axvspan(t0, t1, color="gold", alpha=.35)
    ax[0].axvline(t0, color="orange", ls="--", lw=1.2)
    ax[0].axvline(t1, color="orange", ls="--", lw=1.2)
    # Bottom-right of and adjacent to the highlighted window, with a short leader.
    ax[0].annotate("mask window\n%.1f yr" % s_rep[0],
                   xy=(t1, 0.30), xytext=(t1 + 1.6, 0.19),
                   ha="left", va="bottom", fontsize=9, color="#8a6500",
                   arrowprops=dict(arrowstyle="->", color="orange", lw=1.0,
                                   shrinkA=2, shrinkB=2))
ax[0].set_xlim(0, 120)
ax[0].set_ylim(0, 1.4)
ax[0].set_xlabel("time t (yr)")
ax[0].set_ylabel("value (units differ)")
ax[0].set_title('(a) Representative "productivity illusion" run\nB rises %.3f→%.3f gha (peak) while A falls %.2f→%.2f model units'
                % (B_rep[0], s_rep[4], A_rep[0], s_rep[7]), fontsize=10)
ax[0].legend(fontsize=8, loc="upper left")
ax[0].grid(alpha=.3)
ax[0].annotate("hidden A decline for ~5 yr", xy=(s_rep[9], s_rep[7]), xytext=(60, 1.25),
               fontsize=9, arrowprops=dict(arrowstyle="->", color="orange"))

# Panel B: mask-window width versus initial deficit.
Es = [0.505, 0.515, 0.525, 0.535, 0.545, 0.555, 0.565, 0.575,
      0.585, 0.595, 0.61, 0.63, 0.66, 0.70, 0.80, 1.00]
spans = []
crit = None
for E in Es:
    r = run(p, T=250, dt=0.05, A0=A0, E=E)
    s = win(r["A"], r["B"], r["t"])
    if s:
        spans.append(s[0])
    else:
        spans.append(0.0)
        if crit is None:
            crit = E - bA0
ax[1].bar(np.arange(len(Es)), spans, color="#2ca02c", alpha=.85)
ax[1].set_xticks(np.arange(len(Es)))
ax[1].set_xticklabels(["%.3f" % (E - bA0) for E in Es], rotation=90, fontsize=7)
ax[1].set_ylabel("mask window width (yr)")
ax[1].set_xlabel("initial deficit  E − b₀A₀  (gha)")
ax[1].set_title("(b) The mask collapses beyond a small deficit\nwindow vanishes for deficit ≳ %.3f gha"
                % (crit if crit else 0.075), fontsize=10)
ax[1].grid(alpha=.3, axis="y")
ax[1].set_ylim(0, 7)
plt.tight_layout()
plt.savefig(OUT, dpi=150)
print(f"saved {OUT} | critical deficit={crit:.4f} gha")
print("representative run: B0=%.3f gha, Bpeak=%.3f gha, A0=%.2f model units, Amin=%.3f model units, span=%.1f yr"
      % (B_rep[0], s_rep[4], A_rep[0], s_rep[7], s_rep[0]))
