"""Figures for paper05 v20 from results.json and the exact module."""
import json, pathlib, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "work"))
from p05_core import cells, D, distance_graph, maximal_cliques, winning_word, HOLD, ip

R = json.load(open(root / "work" / "results.json"))
figs = root / "figs"
figs.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "figure.dpi": 150})

# ---------------- Figure 1: census of the six-cube by level
C6 = R["classification"]["6"]
levels = [c["L"] for c in C6["census"]] + [6, 7]
surv = [c["n_survivable"] for c in C6["census"]] + [C6["census"][-1]["n_survivable"]] * 2
adm = C6["n_cliques_nonempty"]
types = {"balls (7)": [], "cylinders (12)": [], "punctured subcubes (7)": [], "boundary ten-sets (10)": [], "subcubes (8)": []}
for c in C6["census"] + [C6["census"][-1]] * 2:
    d = dict((s, n) for s, n in c["maximal_sizes"])
    L = c["L"]
    types["balls (7)"].append(d.get(7, 0) if L == 0 else 0)
    types["punctured subcubes (7)"].append(d.get(7, 0) if L >= 1 else 0)
    types["cylinders (12)"].append(d.get(12, 0))
    types["boundary ten-sets (10)"].append(d.get(10, 0))
    types["subcubes (8)"].append(d.get(8, 0))
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
ax[0].step(levels, [s / 1000 for s in surv], where="post", color="k", lw=1.8, label="blind-survivable sets")
ax[0].axhline(adm / 1000, ls="--", color="gray", label="pairwise-admissible (853,680)")
ax[0].set_xlabel("slack L (tenths above the floor)")
ax[0].set_ylabel("sets (thousands)")
ax[0].set_title("Six-cube census by level")
ax[0].set_xticks(levels)
ax[0].legend(loc="lower right", fontsize=8)
bottom = np.zeros(len(levels))
colors = ["#4477aa", "#228833", "#ccbb44", "#ee6677", "#aa3377"]
for (name, vals), col in zip(types.items(), colors):
    vals = np.array(vals, dtype=float)
    ax[1].bar(levels, vals, bottom=bottom, color=col, label=name, width=0.8)
    bottom += vals
ax[1].set_xlabel("slack L (tenths above the floor)")
ax[1].set_ylabel("maximal sets")
ax[1].set_title("Maximal survivable sets by type")
ax[1].set_xticks(levels)
ax[1].set_ylim(0, 2400)
ax[1].legend(fontsize=7, loc="upper left", ncol=3)
fig.tight_layout()
fig.savefig(figs / "fig_census.pdf")
fig.savefig(figs / "fig_census.png")
plt.close(fig)

# ---------------- Figure 2: knife-edge word of the boundary ten-set
V, adj = distance_graph(6, 3)
cl = maximal_cliques(V, adj)
ten = sorted([c for c in cl if len(c) == 10], key=sorted)[0]
pre, per = winning_word(ten, 3, 12)
S = sorted(ten)
T = 24
word = pre + per * ((T - len(pre)) // len(per) + 1)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
for th in S:
    s = [3]
    for u in word[:T]:
        s.append(s[-1] + D(u, th))
    ax[0].plot(range(T + 1), s, marker=".", lw=1, ms=3)
ax[0].axhline(0, color="k", lw=1)
ax[0].set_xlabel("step")
ax[0].set_ylabel("slack (tenths)")
ax[0].set_title("A boundary ten-set: certified winning word from L = 3")
ax[0].set_ylim(-2, 40)
ax[0].annotate("two cells touch the floor\nevery fourth step", xy=(8, 0), xytext=(10, 12), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=0.8))
# deviation of floating-point stocks from the exact trajectory for the second
# ten-set (sorted order), whose word is lost in float64 under the ratio coding
ten2 = sorted([c for c in cl if len(c) == 10], key=sorted)[1]
pre2, per2 = winning_word(ten2, 3, 12)
word2 = pre2 + per2 * ((T - len(pre2)) // len(per2) + 1)
S2 = sorted(ten2)
# pinned cell: zero net drift per period and touching the floor
def traj(th, word):
    s = [3]
    for u in word:
        s.append(s[-1] + D(u, th))
    return s
pinned = [th for th in S2 if min(traj(th, word2[:T])) == 0][0]
ex = traj(pinned, word2[:T])
dev = {"float64, -0.5+0.2k": [], "float64, (2k-5)/10": [], "float32, -0.5+0.2k": []}
za = 1.3; zr = 1.3; z32 = np.float32(1.3)
dev["float64, -0.5+0.2k"].append(0.0); dev["float64, (2k-5)/10"].append(0.0); dev["float32, -0.5+0.2k"].append(0.0)
for t, u in enumerate(word2[:T]):
    k = ip(u, pinned)
    za = za + (-0.5 + 0.2 * k)
    zr = zr + (2 * k - 5) / 10
    z32 = np.float32(z32 + (np.float32(-0.5) + np.float32(0.2) * np.float32(k)))
    exact = 1 + ex[t + 1] / 10
    dev["float64, -0.5+0.2k"].append((za - exact) * 1e16)
    dev["float64, (2k-5)/10"].append((zr - exact) * 1e16)
    dev["float32, -0.5+0.2k"].append((float(z32) - exact) * 1e16)
touch = [t for t, e in enumerate(ex) if e == 0]
for (name, vals), sty in zip(list(dev.items())[:2], ("b-", "r--")):
    ax[1].plot(range(T + 1), vals, sty, lw=1.2, label=name)
ax[1].axhline(0, color="k", lw=0.8)
for t in touch:
    ax[1].axvline(t, color="gray", lw=0.6, ls=":")
ax[1].set_xlabel("step (dotted lines: exact slack 0, the floor test is decided by the sign)")
ax[1].set_ylabel("float stock minus exact stock (units of 1e-16)")
ax[1].set_title("The pinned cell in float64, two codings")
ax[1].legend(fontsize=7, loc="lower left")
first_r = next((t for t, v in enumerate(dev["float64, (2k-5)/10"]) if t in touch and v < 0), None)
if first_r is not None:
    ax[1].annotate("declared below the floor\nat step %d" % first_r, xy=(first_r, dev["float64, (2k-5)/10"][first_r]),
                   xytext=(first_r + 3, dev["float64, (2k-5)/10"][first_r] - 1.5), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
f32dev = dev["float32, -0.5+0.2k"][3]
ax[1].text(0.98, 0.40, "float32 error at step 3: %.1e" % (f32dev * 1e-16), transform=ax[1].transAxes, ha="right", va="top", fontsize=8)
fig.tight_layout()
fig.savefig(figs / "fig_knife.pdf")
fig.savefig(figs / "fig_knife.png")
plt.close(fig)

# ---------------- Figure 3: horizons and the feedback price
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
for m, col in (("4", "#4477aa"), ("5", "#228833"), ("6", "#ee6677")):
    for r in R["pairs"][m]:
        if not r["survivable"] and r["h"] == int(m) - 2:
            Ls = [h["L"] for h in r["horizon"]]
            ax[0].plot(Ls, [h["exact"] for h in r["horizon"]], marker="o", color=col, label="m=%s far pair (h=%d), exact" % (m, r["h"]))
            ax[0].plot(Ls, [h["bound"] for h in r["horizon"]], ls="--", color=col, lw=0.8)
ob = R["observation"]["4"]["deadline"]["rows"]
ax[0].plot([r["L"] for r in ob], [r["exact_horizon"] for r in ob], marker="s", color="k", label="whole cube (all m), exact = floor(L/5)")
ax[0].set_xlabel("slack L")
ax[0].set_ylabel("maximal survival horizon (steps)")
ax[0].set_title("Finite horizons: exact vs LP bound (dashed)")
ax[0].legend(fontsize=7)
# feedback
for m, col, off in (("4", "#4477aa", -0.15), ("5", "#228833", 0.15)):
    fb = R["observation"][m]["feedback"]
    js = sorted(int(j) for j in fb["subcubes"])
    vals = [fb["subcubes"][str(j)] for j in js] + [fb["cube"]]
    xs = [j + off for j in js] + [int(m) + off]
    ax[1].bar(xs, vals, width=0.3, color=col, label="m=%s feedback threshold F*" % m)
    blind = [fb["subcubes_blind"][str(j)] for j in js] + [None]
    for x, b in zip(xs, blind):
        if b is not None:
            ax[1].plot([x], [b], marker="_", color="k", ms=12, mew=2)
ax[1].plot([], [], marker="_", color="k", ms=12, mew=2, ls="none", label="blind threshold L* (finite cases)")
ax[1].set_xlabel("class dimension j (subcube; j = m: whole cube)")
ax[1].set_ylabel("slack (tenths)")
ax[1].set_title("Price of observation: feedback vs blind")
ax[1].set_xticks([1, 2, 3, 4, 5])
ax[1].legend(fontsize=7, loc="upper left")
fig.tight_layout()
fig.savefig(figs / "fig_horizon.pdf")
fig.savefig(figs / "fig_horizon.png")
plt.close(fig)
print("figures written")
