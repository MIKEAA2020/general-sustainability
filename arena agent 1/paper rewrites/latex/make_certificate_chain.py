"""Certificate-chain figure (joint-audit enhancement 13.1): the trusted
computing base as a flow from the supplied datum through the library's
certificate families to canonical JSON, the independent checker, and the
dashboard provenance block. Deterministic; floats only as coordinates."""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "..", "figs_p3"))
os.makedirs(OUT, exist_ok=True)

fig, ax = plt.subplots(figsize=(10.4, 3.1), dpi=300)
ax.set_xlim(0, 104)
ax.set_ylim(0, 31)
ax.axis("off")

DARK, MID, LIGHT, RED, GREEN = "#1c1c1c", "#4a4a4a", "#eef0f2", "#c0392b", "#2e8b57"

boxes = [
    (1, "supplied rational datum", "typed floors; declared paths;\nexact or certified-enclosure status", LIGHT, MID),
    (15.5, "library\n(safe transitions)", "operators; recursions;\nweight partition", LIGHT, MID),
    (30, "certificate families", "Farkas; partition;\nbenchmark+tube; belief failure", LIGHT, MID),
    (45.5, "canonical JSON", "sorted keys; no whitespace;\n\"num/den\" strings; no timestamps", LIGHT, MID),
    (62, "independent checker", "stdlib-only; imports no\nSafeTransition modules", "#fdf3e7", RED),
    (79, "verdicts", "algebraic identities;\nre-derived thresholds,\nregions, values, failures", "#eaf4ec", GREEN),
    (93, "dashboard\nprovenance", "SHA-256 hashes;\nversion; re-run command", LIGHT, MID),
]
for x, title, sub, fc, ec in boxes:
    ax.add_patch(FancyBboxPatch((x, 9), 12.5, 15, boxstyle="round,pad=0.4",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + 6.25, 20.4, title, ha="center", va="center", fontsize=8.6,
            color=DARK, weight="bold")
    ax.text(x + 6.25, 14.2, sub, ha="center", va="center", fontsize=6.4,
            color="#444")
for x in (13.6, 28.1, 43.6, 59.1, 76.1, 91.1):
    ax.annotate("", xy=(x + 1.6, 16.5), xytext=(x, 16.5),
                arrowprops=dict(arrowstyle="-|>", color=MID, lw=1.6))
ax.text(52, 27.6, "trusted computing base: exact rational verification conditional on the supplied datum",
        ha="center", fontsize=9.2, color=DARK, weight="bold")
ax.text(52, 3.2, "the checker validates certificates against the supplied system data; it does not\n"
                 "certify the scientific validity of the datum or the correspondence of an enclosure\n"
                 "to an unmodelled continuous system",
        ha="center", va="center", fontsize=7.2, color=RED)
path = os.path.join(OUT, "fig_certificate_chain.png")
fig.savefig(path, dpi=300, facecolor="white", bbox_inches="tight")
print(f"wrote {path}")
