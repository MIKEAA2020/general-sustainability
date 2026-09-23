"""Certificate-chain figure (joint-audit enhancement 13.1): the trusted
computing base as a flow from the supplied datum through the library's
certificate families to canonical JSON, the independent checker, and the
dashboard provenance block. Deterministic; floats only as coordinates."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "..", "figs_p3"))
os.makedirs(OUT, exist_ok=True)

fig, ax = plt.subplots(figsize=(13.0, 3.4), dpi=300)
ax.set_xlim(0, 122)
ax.set_ylim(0, 34)
ax.axis("off")

DARK, MID, LIGHT, RED, GREEN = "#1c1c1c", "#4a4a4a", "#eef0f2", "#c0392b", "#2e8b57"

boxes = [
    ("supplied datum", "typed floors; declared\npaths; EXACT or\nCONSERVATIVE status", LIGHT, MID),
    ("library", "operators;\nrecursions;\nweight partition", LIGHT, MID),
    ("certificates", "Farkas; partition;\nbenchmark+tube;\nbelief failure", LIGHT, MID),
    ("canonical JSON", "sorted keys; tight\nseparators; \"num/den\"\nstrings; no timestamps", LIGHT, MID),
    ("independent\nchecker", "stdlib-only; imports no\nSafeTransition modules", "#fdf3e7", RED),
    ("verdicts", "identities re-checked;\nthresholds, regions,\nvalues, failures\nre-derived", "#eaf4ec", GREEN),
    ("dashboard\nprovenance", "SHA-256 hashes;\nversion;\nre-run command", LIGHT, MID),
]
W, GAP, X0, Y0, H = 15.0, 2.6, 1.5, 9.5, 16.0
for i, (title, sub, fc, ec) in enumerate(boxes):
    x = X0 + i * (W + GAP)
    ax.add_patch(FancyBboxPatch((x, Y0), W, H, boxstyle="round,pad=0.4",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + W / 2, Y0 + H - 3.4, title, ha="center", va="center",
            fontsize=8.4, color=DARK, weight="bold")
    ax.text(x + W / 2, Y0 + (H - 6.2) / 2 + 0.6, sub, ha="center",
            va="center", fontsize=6.2, color="#444")
    if i:
        xa = x - GAP
        ax.annotate("", xy=(xa + GAP - 0.3, Y0 + H / 2), xytext=(xa + 0.3, Y0 + H / 2),
                    arrowprops=dict(arrowstyle="-|>", color=MID, lw=1.6))
ax.text(61, 31.6,
        "trusted computing base: exact rational verification conditional on the supplied datum",
        ha="center", fontsize=9.4, color=DARK, weight="bold")
ax.text(61, 4.4,
        "the checker validates certificates against the supplied system data; it does not certify\n"
        "the scientific validity of the datum or the correspondence of an enclosure to an\n"
        "unmodelled continuous system",
        ha="center", va="center", fontsize=7.4, color=RED)
path = os.path.join(OUT, "fig_certificate_chain.png")
fig.savefig(path, dpi=300, facecolor="white", bbox_inches="tight")
print(f"wrote {path}")
