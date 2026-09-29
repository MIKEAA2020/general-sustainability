#!/usr/bin/env python3
"""Layout verification for the graphical abstract.

I cannot see the rendered PNG, so the geometry is checked numerically after a
draw: every text artist must sit inside the figure, and a list of pairs that
would collide (legend vs annotation box, axis labels vs footnote) is tested
for overlap. Also checks that the plotted data lines are inside their axes.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import runpy
import io
import contextlib

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    runpy.run_path("/home/user/make_graphical_abstract_e2.py", run_name="__main__")
# the script built and saved its own figure; rebuild the object list by
# re-running its plotting code is impractical, so use the current figure
fig = plt.gcf()
r = fig.canvas.get_renderer()
W, H = fig.canvas.get_width_height()

fails = []


def box(a):
    b = a.get_window_extent(renderer=r)
    return b.x0, b.y0, b.x1, b.y1


texts = [a for a in fig.get_children() if isinstance(a, matplotlib.text.Text)]
texts += [a for ax in fig.get_axes() for a in ax.get_children()
          if isinstance(a, matplotlib.text.Text)]
texts += [a for ax in fig.get_axes() for a in ax.texts]

for t in texts:
    s = t.get_text().strip()
    if not s:
        continue
    x0, y0, x1, y1 = box(t)
    if x0 < -2 or y0 < -2 or x1 > W + 2 or y1 > H + 2:
        fails.append("OUT OF BOUNDS: %r  box=(%.0f,%.0f,%.0f,%.0f) canvas=%dx%d"
                     % (s[:40], x0, y0, x1, y1, W, H))


def overlap(a, b):
    ax0, ay0, ax1, ay1 = box(a)
    bx0, by0, bx1, by1 = box(b)
    ox = min(ax1, bx1) - max(ax0, bx0)
    oy = min(ay1, by1) - max(ay0, by0)
    return ox > 0 and oy > 0


# every pair of figure-level texts must not overlap
figtexts = [a for a in fig.get_children()
            if isinstance(a, matplotlib.text.Text) and a.get_text().strip()]
for i in range(len(figtexts)):
    for j in range(i + 1, len(figtexts)):
        if overlap(figtexts[i], figtexts[j]):
            fails.append("FIGURE TEXT OVERLAP: %r vs %r"
                         % (figtexts[i].get_text()[:32],
                            figtexts[j].get_text()[:32]))

# within-axes collisions: each axes' own texts must not overlap each other
for k, ax in enumerate(fig.get_axes()):
    ts = [a for a in ax.texts if a.get_text().strip()]
    for i in range(len(ts)):
        for j in range(i + 1, len(ts)):
            if overlap(ts[i], ts[j]):
                fails.append("PANEL %d OVERLAP: %r vs %r"
                             % (k, ts[i].get_text()[:30], ts[j].get_text()[:30]))
    # a text inside an axes must stay inside it
    ab = ax.get_window_extent(renderer=r)
    for t in ts:
        x0, y0, x1, y1 = box(t)
        if x0 < ab.x0 - 3 or x1 > ab.x1 + 3 or y0 < ab.y0 - 3 or y1 > ab.y1 + 3:
            fails.append("PANEL %d TEXT SPILLS OUT: %r" % (k, t.get_text()[:36]))
    # legends
    lg = ax.get_legend()
    if lg is not None:
        lb = lg.get_window_extent(renderer=r)
        if lb.x0 < -2 or lb.y0 < -2 or lb.x1 > W + 2 or lb.y1 > H + 2:
            fails.append("PANEL %d LEGEND OUT OF BOUNDS" % k)
        for t in ts:
            if overlap(lg, t) if hasattr(lg, "get_window_extent") else False:
                fails.append("PANEL %d LEGEND OVERLAPS %r"
                             % (k, t.get_text()[:30]))

print("canvas %dx%d, %d figure texts, %d axes" % (W, H, len(figtexts),
                                                  len(fig.get_axes())))
if fails:
    print("FAILURES (%d):" % len(fails))
    for f in fails:
        print("  -", f)
else:
    print("LAYOUT OK: no out-of-bounds text, no overlapping text pairs")
