"""Conceptual Figure 1 for paper5 v38 (Nature Sustainability elevation).

Panel A: the three institutional architectures (purely conceptual).
Panel B: review-interval stability slice - SCHEMATIC curves; ONLY the
markers are computed values (paper5 v37 Section 3.4):
  extractive exact: annual rho=1.00035, crossing at 6.501 yr (unstable->stable)
  protective exact: annual rho=0.9838, max 0.9967 over tested range, no crossing.
No curve shape between markers is a computed result.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.size': 8, 'font.family': 'sans-serif',
                     'axes.linewidth': 0.8})
fig, (axA, axB) = plt.subplots(1, 2, figsize=(7.5, 3.9),
                               gridspec_kw={'width_ratios': [1.05, 1]})
fig.subplots_adjust(left=0.06, right=0.97, top=0.90, bottom=0.11, wspace=0.22)

# ---------------- Panel A ----------------
axA.set_xlim(0, 10); axA.set_ylim(0, 12.9); axA.axis('off')
axA.text(0.2, 12.80, 'A  Institutional architectures', fontsize=9,
         weight='bold', va='top', ha='left')

def box(ax, x, y, w, h, txt, ec='#1f5fa8', fc='#eaf1fa', fs=7.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                                ec=ec, fc=fc, lw=1.0))
    ax.text(x + w / 2, y + h / 2, txt, ha='center', va='center', fontsize=fs)

def arrow(ax, x1, y1, x2, y2, style='-|>', lw=1.0, color='#333333'):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=9, lw=lw, color=color,
                                 shrinkA=1, shrinkB=1))

rows = [
    ('Continuous delay', 'Stock', 'Assessment\n(continuous)',
     'Effort\n(continuous)', 'delayed signal in evolving law'),
    ('Annual step', 'Stock', 'Annual map\n(single step)', 'Effort',
     'between-decision dynamics compressed'),
    ('Sample-and-hold (this paper)', 'Stock', 'Review at $T_r$\n(sample)',
     'Hold command\n(zero-order hold)', 'observe at reviews, hold between'),
]
for i, (lab, b1, b2, b3, note) in enumerate(rows):
    y = 10.4 - i * 3.7
    axA.text(0.2, y + 1.30, lab, fontsize=8, weight='bold', va='bottom',
             ha='left')
    box(axA, 2.6, y, 1.9, 1.1, b1)
    box(axA, 5.1, y, 2.1, 1.1, b2)
    box(axA, 7.8, y, 1.9, 1.1, b3)
    arrow(axA, 4.5, y + 0.55, 5.05, y + 0.55)
    arrow(axA, 7.2, y + 0.55, 7.75, y + 0.55)
    arrow(axA, 7.8, y - 0.30, 2.6, y - 0.30)  # harvest feedback, below boxes
    axA.text(5.2, y - 0.72, note, fontsize=6.5, style='italic',
             color='#555555', ha='center', va='top')

# ---------------- Panel B ----------------
axB.text(-0.18, 1.05, 'B  Review-interval stability slice (schematic)',
         fontsize=9, weight='bold', va='top', ha='left',
         transform=axB.transAxes)
axB.set_xlim(0.2, 8.4); axB.set_ylim(0.975, 1.035)
axB.set_xlabel('Review interval $T_r$ (yr)', fontsize=8.5)
axB.set_ylabel('Spectral radius $\\rho$', fontsize=8.5)
axB.axhspan(1.0, 1.035, color='#f6d5d5', zorder=0)
axB.axhspan(0.975, 1.0, color='#d9ead3', zorder=0)
axB.text(7.9, 1.029, 'unstable', fontsize=7, color='#a33d3d', ha='right',
         va='top')
axB.text(0.45, 0.9775, 'stable', fontsize=7, color='#2e7d32', ha='left',
         va='bottom')
axB.axhline(1.0, color='#333333', lw=0.9, ls='--', dashes=(3, 2))

tr = np.linspace(0.2, 8.4, 400)
# shape-preserving schematic through the computed anchors (stays >=1 until 6.501)
ax = np.array([0.2, 0.6, 1.0, 2.5, 4.5, 6.501, 7.5, 8.4])
ay = np.array([1.022, 1.004, 1.00035, 1.0055, 1.0025, 1.0, 0.994, 0.990])
ext = PchipInterpolator(ax, ay)(tr)
pro = 0.984 + 0.0015 * np.sin(tr * 1.3) - 0.001 * (tr - 1.0) / 8.0
axB.plot(tr, ext, color='#b0b0b0', lw=1.1, zorder=2)
axB.plot(tr, pro, color='#b0b0b0', lw=1.1, zorder=2)

axB.plot(1.0, 1.00035, marker='o', ms=6, color='#c00000', zorder=4)
axB.plot(6.501, 1.0, marker='D', ms=6, color='#c00000', zorder=4)
axB.plot(1.0, 0.9838, marker='s', ms=6, color='#1f5fa8', zorder=4)
axB.annotate('annual: $\\rho=1.00035$\nextractive, exact',
             xy=(1.0, 1.00035), xytext=(2.1, 1.022), fontsize=6.5,
             arrowprops=dict(arrowstyle='-', color='#555555', lw=0.7),
             ha='left', va='center', color='#333333')
axB.annotate('crossing $\\approx 6.5$ yr\nunstable $\\to$ stable',
             xy=(6.501, 1.0), xytext=(4.3, 0.9878), fontsize=6.5,
             arrowprops=dict(arrowstyle='-', color='#555555', lw=0.7),
             ha='center', va='center', color='#333333')
axB.annotate('protective: $\\rho=0.9838$\nstable throughout',
             xy=(1.0, 0.9838), xytext=(1.7, 0.9795), fontsize=6.5,
             arrowprops=dict(arrowstyle='-', color='#555555', lw=0.7),
             ha='left', va='center', color='#1f5fa8')
axB.text(0.98, 0.04, 'curves schematic;\nmarkers computed (§3.4)',
         transform=axB.transAxes, fontsize=6, style='italic',
         color='#555555', ha='right', va='bottom')
axB.set_xticks([1, 2, 4, 6.5, 8])
axB.tick_params(labelsize=7.5)

fig.savefig('/home/user/_openitems/fig_concept_v38.png', dpi=300)
print('wrote fig_concept_v38.png')
