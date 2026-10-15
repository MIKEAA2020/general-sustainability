"""Figure 1 of v63: the finite-menu geometric characterisation (Theorem 1).
(a) a three-plan menu in the plane; (b) the witness menu {FAST, SLOW} with D = {(2,0),(0,2)}.
Scalarized acceptance = conv(D) + R^2_+ ; coordinate-wise acceptance = union of orthants d_a + R^2_+ ;
the gap is the difference. Membership in conv(D)+R^2_+ is tested by the dual criterion of Theorem 1(ii)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def regions(D, xs, ys, nw=721):
    th = np.linspace(0, np.pi/2, nw); W = np.stack([np.cos(th), np.sin(th)], 1)   # w in the closed cone (unit vectors)
    X, Y = np.meshgrid(xs, ys); S = np.stack([X.ravel(), Y.ravel()], 1)
    minwd = (W @ np.array(D).T).min(1)                     # min_a w.d_a for each w
    scal = np.ones(len(S), bool)
    for k in range(0, len(S), 20000):
        scal[k:k+20000] = np.all(S[k:k+20000] @ W.T >= minwd[None, :] - 1e-12, axis=1)
    scal = scal.reshape(X.shape)
    coord = np.zeros_like(scal)
    for d in D:
        coord |= (X >= d[0] - 1e-12) & (Y >= d[1] - 1e-12)
    return scal, coord

def panel(ax, D, lim, title, labels, offsets):
    xs = np.linspace(0, lim, 401); ys = np.linspace(0, lim, 401)
    scal, coord = regions(D, xs, ys)
    gap = scal & ~coord
    ax.contourf(xs, ys, coord.astype(float), levels=[0.5, 1.5], colors=["#cfe8cf"])
    ax.contourf(xs, ys, gap.astype(float), levels=[0.5, 1.5], colors=["#f4b6b6"])
    ax.contourf(xs, ys, gap.astype(float), levels=[0.5, 1.5], colors="none", hatches=["////"])
    # boundary of conv(D)+R^2_+ : lower-left chain
    ax.contour(xs, ys, scal.astype(float), levels=[0.5], colors="k", linewidths=1.6)
    ax.contour(xs, ys, coord.astype(float), levels=[0.5], colors="#2e7d32", linewidths=1.2, linestyles="--")
    for d, lab, off in zip(D, labels, offsets):
        ax.plot(*d, "ko", ms=6, clip_on=False); ax.annotate(lab, d, xytext=off, textcoords="offset points", fontsize=9)
    ax.set_xlim(0, lim); ax.set_ylim(0, lim); ax.set_aspect("equal")
    ax.set_xlabel(r"$s_1$ (margin above floor 1)"); ax.set_ylabel(r"$s_2$ (margin above floor 2)")
    ax.set_title(title, fontsize=10.5)

fig, axs = plt.subplots(1, 2, figsize=(10.6, 5.3))
D3 = [(3.2, 0.4), (1.6, 1.3), (0.5, 3.0)]
panel(axs[0], D3, 4.2, r"(a) a three-plan menu with required margins $d_1,d_2,d_3$",
      [r"$d_1$", r"$d_2$", r"$d_3$"], [(6, -14), (8, -14), (8, 2)])
panel(axs[1], [(2.0, 0.0), (0.0, 2.0)], 3.0, r"(b) the witness menu $\{$FAST, SLOW$\}$: gap $=\mathcal{Q}$",
      [r"$d_{\mathrm{FAST}}=(2,0)$", r"$d_{\mathrm{SLOW}}=(0,2)$"], [(-62, 8), (8, 4)])
axs[1].plot(6/5, 6/5, "k*", ms=11); axs[1].annotate("witness point (6/5, 6/5)", (6/5, 6/5), xytext=(8, 8), textcoords="offset points", fontsize=9)
axs[1].text(0.35, 0.35, r"rejected by both" "\n" r"($s_1+s_2<2$)", fontsize=8.5, color="0.3")
axs[1].text(2.25, 2.4, "accepted by both", fontsize=8.5, color="#2e7d32")
axs[0].text(2.4, 2.6, "accepted by both\n(some plan dominates)", fontsize=8.5, color="#2e7d32")
axs[0].text(0.25, 0.3, "rejected by both", fontsize=8.5, color="0.3")
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
h = [Patch(facecolor="#cfe8cf", edgecolor="#2e7d32", label=r"coordinate-wise acceptance $\bigcup_a(d_a+\mathbb{R}^n_+)$"),
     Patch(facecolor="#f4b6b6", hatch="////", label=r"acceptance gap (every weight licenses a plan; no plan dominates)"),
     Line2D([0], [0], color="k", lw=1.6, label=r"boundary of scalarized acceptance $\mathrm{conv}(\mathcal{D})+\mathbb{R}^n_+$")]
fig.legend(handles=h, loc="lower center", ncol=2, fontsize=8.8, frameon=False, bbox_to_anchor=(0.5, 0.0))
fig.tight_layout(rect=(0, 0.12, 1, 0.99))
fig.savefig("../figs/fig_finite_menu_geometry.pdf"); fig.savefig("../figs/fig_finite_menu_geometry.png", dpi=170)
print("ok")
