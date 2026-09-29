#!/usr/bin/env python3
"""Promote the two model-form campaigns (depensation / Fox) to the v3 basis.

The srcyear editions of both campaigns are already source-year in their
residual classes, but they are unusable on this machine for three reasons
(defect class: a campaign can resample one pool while freezing another's
constant -- the same defect that made campaign_srcyear.py unusable):

  1. REPO is hardcoded to /tmp/liverepo, so the module cannot be imported.
  2. They import run_intervention_srcyear.py, whose docstring is a verbatim
     copy of the v2 runner's and falsely claims bit-identity with it. The
     promoted run_intervention_v3.py is the honest source-year runner.
  3. They self-check against results/intervention_results.json, which is the
     REGISTERED (v1/v2) artifact carrying floors -460.03/-318.76/-114.85.
     Under v3 the check compares two different conventions and can only fail.

Additionally the Fox campaign hardcodes the v2 Schaefer constructive bound
57.61 in its comparison table and its print label. That value is
g(K*) - |e_q10| with the v2 floor 114.85; on v3 the floor is 80.87 and the
bound is 91.59. Hardcoded expected-value rows are exactly the defect that
lets a wrong basis survive a green run, so both sites are now computed
from the fit.
"""
from pathlib import Path

SRC = Path("/home/user/fam/e2/src")
OUTDIR = "results_forms_v3"

# ---------------------------------------------------------------- depensation
p = SRC / "campaign_e2_depensation_srcyear.py"
t = p.read_text(encoding="utf-8")

reps = [
    ('REPO = Path("/tmp/liverepo")', 'REPO = Path("/home/user/repo")'),
    ('ri = _import("run_intervention", COD / "run_intervention_srcyear.py")',
     'ri = _import("run_intervention", COD / "run_intervention_v3.py")'),
    ('OUT = Path(__file__).resolve().parent / "results"',
     f'OUT = Path(__file__).resolve().parent / "{OUTDIR}"'),
    ('"intervention_results.json"', '"intervention_results_v3.json"'),
    ('"campaign_e2_depensation.csv"', '"campaign_e2_depensation_v3.csv"'),
    ('"campaign_e2_depensation.txt"', '"campaign_e2_depensation_v3.txt"'),
    # docstring honesty
    ('Writes results to rerun_campaigns/results/; modifies nothing committed.',
     'v3 (SOURCE-YEAR) EDITION. Imports run_intervention_v3.py, so the frozen\n'
     'classes are -328.97 / -287.36 / -80.87 kt, and self-checks against\n'
     'results/intervention_results_v3.json -- the only artifact on the same\n'
     'basis. Writes results_forms_v3/; modifies nothing committed.'),
]
for a, b in reps:
    assert t.count(a) == 1, (a, t.count(a))
    t = t.replace(a, b)

# make the self-check a hard gate rather than a printed by-eye comparison
old_print = '    print("=== self-check: grid vs committed Schaefer boundaries ===")\n    chk = df[df.variant == "grid_schaefer_check"]\n'
new_print = (
    '    print("=== self-check: grid vs committed Schaefer boundaries (V3 BASIS) ===")\n'
    '    chk = df[df.variant == "grid_schaefer_check"]\n'
    '    bad = chk[(chk.boundary_grid.isna() != chk.boundary_committed.isna())\n'
    '              | ((chk.boundary_grid - chk.boundary_committed).abs() > TOL_KT)]\n'
    '    dev = (chk.boundary_grid - chk.boundary_committed).abs().max()\n'
    '    print(f"  max |grid - committed| = {dev:.3f} kt (declared tolerance {TOL_KT} kt)")\n'
    '    assert bad.empty, ("grid kernel fails to reproduce the v3 committed "\n'
    '                       "boundaries:\\n" + bad.to_string(index=False))\n'
)

# declare the tolerance, with the reason, next to the resolution
old = "DS = 0.05  # kt grid resolution on [K_star, S_HI]"
new = old + '''
# Tolerance for the grid-vs-committed self-check, DECLARED not fitted. The grid
# iterates a boolean mask with F(x) rounded to DS/2 at every step; next to the
# repelling boundary (F' > 1 there) that rounding compounds along the orbit, so
# a grid boundary sits up to ~1 kt BELOW the same boundary from the committed
# interval-arithmetic engine. This is why Table 2's registered row (committed
# engine) and its Allee/Fox rows (grid engine) are not to be differenced at
# the 0.1 kt level.
TOL_KT = 1.0'''
assert t.count(old) == 1
t = t.replace(old, new)
assert t.count(old_print) == 1
t = t.replace(old_print, new_print)

(SRC / "campaign_e2_depensation_v3.py").write_text(t, encoding="utf-8")

# ----------------------------------------------------------------------- Fox
p = SRC / "campaign_e2_fox_form_srcyear.py"
t = p.read_text(encoding="utf-8")

reps = [
    ('REPO = Path("/tmp/liverepo")', 'REPO = Path("/home/user/repo")'),
    ('ri = _import("run_intervention", COD / "run_intervention_srcyear.py")',
     'ri = _import("run_intervention", COD / "run_intervention_v3.py")'),
    ('OUT = HERE / "results"', f'OUT = HERE / "{OUTDIR}"'),
    ('"e2_fox_form.csv"', '"e2_fox_form_v3.csv"'),
    ('"e2_fox_kernels.csv"', '"e2_fox_kernels_v3.csv"'),
    # the v2 constructive bound, hardcoded in the print label
    ('f"F\'(K*) = {Fp_F:.4f} (1.1531); constructive q10 = {cstar_F:.2f} (57.61)")',
     'f"F\'(K*) = {Fp_F:.4f} (1.1531); constructive q10 = {cstar_F:.2f} "\n'
     '          f"(Schaefer v3 {cstar_S:.2f})")'),
    # ... and in the comparison table
    ('             MSE_kt2=round(float(p_sch["sse"]), 1), g_max=296.1, g_Kstar=172.48,\n'
     '             Fp_Kstar=1.1531, constructive_q10=57.61),',
     '             MSE_kt2=round(float(p_sch["sse"]), 1), g_max=296.1,\n'
     '             g_Kstar=round(g_K_S, 2),\n'
     '             Fp_Kstar=1.1531,\n'
     '             constructive_q10=round(cstar_S, 2)),'),
]
for a, b in reps:
    assert t.count(a) == 1, (a, t.count(a))
    t = t.replace(a, b)

# define the Schaefer reference quantities from the committed fit, not by hand
old = '    g_max_F = rF * KF / np.e\n'
new = (
    '    # Schaefer reference constructive bound, COMPUTED on the v3 floor\n'
    '    # (it was hardcoded at the v2 value 57.61; on v3 it is 91.59)\n'
    '    g_K_S = float(rl.surplus(K_STAR, r0, K0))\n'
    '    cstar_S = g_K_S - abs(e_q10)\n'
    '    assert abs(cstar_S - 91.59) < 0.01, cstar_S\n'
    '    g_max_F = rF * KF / np.e\n'
)
assert t.count(old) == 1
t = t.replace(old, new)

old = 'g(K*) = {g_K_F:.2f} (172.48); '
new = 'g(K*) = {g_K_F:.2f} (Schaefer {g_K_S:.2f}); '
assert t.count(old) == 1
t = t.replace(old, new)

# docstring honesty
old = '"""E2 cod intervention: Fox surplus form as the third co-equal model form (wave 7).'
new = ('"""E2 cod intervention: Fox surplus form as the third co-equal model form\n'
       '(wave 7) -- v3 / SOURCE-YEAR EDITION.\n\n'
       'Imports run_intervention_v3.py, so the frozen classes are the source-year\n'
       'ones (-328.97 / -287.36 / -80.87 kt) and the Schaefer constructive bound\n'
       'printed for comparison is computed from the fit, not hardcoded.')
assert t.count(old) == 1
t = t.replace(old, new)

(SRC / "campaign_e2_fox_form_v3.py").write_text(t, encoding="utf-8")
print("wrote campaign_e2_depensation_v3.py and campaign_e2_fox_form_v3.py")
