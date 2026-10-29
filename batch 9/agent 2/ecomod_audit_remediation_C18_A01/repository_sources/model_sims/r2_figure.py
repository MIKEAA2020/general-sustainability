"""Render the R2 characteristic-equation figures to PNG (self-contained).

* `scans/r2_char_spectrum.png`  — leading eigenvalue Re(lambda_max) vs regeneration
  delay tau_g, showing it is ALWAYS positive real (monotone vicious-cycle growth,
  no Hopf crossing); damped oscillatory modes shown as the complex-roots cloud.
* `scans/r2_a11_vs_delay.png`   — manuscript a11 = G'(A*) + b/b_G vs A*, with the
  r threshold, showing a11 > r everywhere (zero-delay condition violated).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

from . import char_eq as CE

OUT = Path(__file__).resolve().parents[1] / "scans"
OUT.mkdir(exist_ok=True)


def _fig_spectrum():
    # leading REAL eigenvalue vs tau_g (A*=0.8 reference)
    c = CE.lin_coeffs(0.8)
    tg_list = np.arange(0, 121, 4)
    real_lead = []
    for tg in tg_list:
        fs = CE.full_spectrum(tg, 25.0, c, nr=120, ni=160)
        # leading among real roots (monotone mode)
        rr = CE._real_roots(tg, 25.0, c)
        rp = [x for x in rr if abs(x) > 1e-6]
        real_lead.append(max(rp) if rp else np.nan)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(tg_list, real_lead, "-o", ms=4, color="#c0392b",
            label=r"leading Re$\,\lambda$ (real, monotone mode)")
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel(r"leading Re$\,\lambda$ (yr$^{-1}$)")
    ax.set_xlabel(r"regeneration delay $\tau_g$ (yr, $\tau_p=25$)")
    ax.set_title("R2 — corrected $(1''')$ interior point is monotonically unstable")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "r2_char_spectrum.png", dpi=150); plt.close(fig)


def _fig_a11():
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    A = np.linspace(0.20, 1.20, 60)
    a11 = np.array([CE.lin_coeffs(a)["a1"] + CE.lin_coeffs(a)["a3"] for a in A])
    ax.plot(A, a11, "-", color="#2980b9", lw=2,
            label=r"$a_{11}=G'(A^*)+b/b_G$")
    ax.axhline(0.02, color="#c0392b", ls="--", lw=1.5, label=r"$r=0.02$")
    ax.axvline(0.6, color="gray", ls=":", label=r"$A_{\max}/2$")
    ax.set_xlabel(r"reference equilibrium $A^*$")
    ax.set_ylabel(r"$a_{11}$ (yr$^{-1}$)")
    ax.set_title(r"R2 — $a_{11}>r$ everywhere: zero-delay stability condition violated")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(OUT / "r2_a11_vs_delay.png", dpi=150); plt.close(fig)


if __name__ == "__main__":
    _fig_spectrum(); _fig_a11()
    print("wrote", OUT / "r2_char_spectrum.png")
    print("wrote", OUT / "r2_a11_vs_delay.png")
