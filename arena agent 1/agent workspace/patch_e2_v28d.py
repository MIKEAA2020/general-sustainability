#!/usr/bin/env python3
"""v28d: correct the Section 2 residual summary to the REGISTERED (v2) basis,
and sign the two bare 318.8 sites so R8l's no_variant check passes.

Registered-basis residual summary (24 training residuals, 1984-2007),
computed from wave_e_cod/src/run_intervention_v2.py::fit_surplus():
    mean               = -20.4400
    SD (ddof=1)        = 134.9610
    min                = -460.0285
    max (SIGNED)       = +179.7606
    |max|              = 460.0285
    q05                = -318.7636
    q10                = -114.8477
    lag-1 autocorrelation = 0.6523

Printed values being replaced came from the SOURCE-YEAR fit
(run_intervention_srcyear.py): mean -10.9, SD 114.9, acf 0.5539.
(+206.6 matches neither runner; it is the Fox campaign's frozen max.)

NOT touched: line 870's 0.55 -- Section 3.8/Table 4 explicitly use the
SOURCE-YEAR residual pool, where 0.55 is correct.
"""
import ast
import re
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"

EDITS = []


def E(label, old, new):
    EDITS.append((label, old, new))


# --- 1. Section 2 residual summary (mean / SD / range / lag-1) -------------
E("sec2 residual summary",
  r"""The training-window residuals of the fitted map have mean \(-10.9\) kt,
SD \(114.9\) kt, range \([-460.0, +206.6]\) kt, and lag-1
autocorrelation \(0.55\). The 1992 transition residual is the minimum""",
  r"""The training-window residuals of the fitted map have mean \(-20.4\) kt,
SD \(135.0\) kt, range \([-460.0, +179.8]\) kt, and lag-1
autocorrelation \(0.65\). The 1992 transition residual is the minimum""")

# --- 2. Fit residual SD in the r/K paragraph -------------------------------
E("sec2 fit residual SD",
  r"""Fit
residual SD is \(114.9\) kt.""",
  r"""Fit
residual SD is \(135.0\) kt.""")

# --- 3. Sign the two bare 318.8 sites (R8l no_variant) ---------------------
E("vacuity prose floor sign",
  r"""because the
\(318.8\) kt floor also exceeds \(g_{\max}\) and the class is vacuous;""",
  r"""because the
\(-318.8\) kt floor also exceeds \(g_{\max}\) and the class is vacuous;""")

E("K-sensitivity floor sign",
  r"""short of the \(318.8\) kt floor, and the grid first reports that class""",
  r"""short of the \(-318.8\) kt floor, and the grid first reports that class""")


src = open(__file__, encoding="utf-8").read()
ast.parse(src)

tex = open(TEX, encoding="utf-8").read()
print(f"loaded {TEX}  ({len(tex)} chars)\n")

applied = 0
for label, old, new in EDITS:
    n = tex.count(old)
    if n == 0:
        print(f"  MISS  {label}")
        continue
    if n > 1:
        print(f"  AMBIGUOUS ({n} matches)  {label}  -- left unchanged")
        continue
    tex = tex.replace(old, new, 1)
    applied += 1
    print(f"  ok    {label}")

open(TEX, "w", encoding="utf-8").write(tex)
print(f"\napplied {applied}/{len(EDITS)}")

# --- residual sweep over every superseded / corrected constant -------------
print("\n=== residual sweep ===")
SUPERSEDED = {
    "2219.6": "Fox q05/T=inf kernel (stale)",
    "2070.9": "Fox q05 finite kernel (stale)",
    "920.2":  "Fox A phi=0.75 q10 T=1 (stale)",
    "989.0":  "Fox misc (stale)",
    "1025.5": "Fox misc (stale)",
    "1064.7": "Fox misc (stale)",
    "1111.3": "Fox misc (stale)",
    "1161.0": "Fox misc (stale)",
    "114.9":  "SOURCE-YEAR SD -- only legal with an explicit source-year label",
    "206.6":  "Fox campaign max residual (stale)",
    "0.906":  "Fox Table 3 (stale)",
    "0.862":  "Fox Table 3 (stale)",
    "0.958":  "Fox Table 3 (stale)",
    "0.647":  "Fox Table 3 (stale)",
    "0.835":  "Fox Table 3 (stale)",
    "0.903":  "Fox Table 3 (stale)",
    "0.857":  "Fox Table 3 (stale)",
    "0.955":  "Fox Table 3 (stale)",
}
clean = True
for tok, why in SUPERSEDED.items():
    for m in re.finditer(re.escape(tok), tex):
        i = m.start()
        ctx = tex[max(0, i - 90):i + 90].replace("\n", " ")
        ln = tex[:i].count("\n") + 1
        print(f"  LIVE  {tok!r} ({why})")
        print(f"        line {ln}: ...{ctx}...")
        clean = False

# unsigned 318.8 / 114.9 magnitude uses (R8l no_variant)
for tok in ("318.8", "114.9", "460.0"):
    for m in re.finditer(r"(?<!-)" + re.escape(tok), tex):
        i = m.start()
        ctx = tex[max(0, i - 70):i + 70].replace("\n", " ")
        ln = tex[:i].count("\n") + 1
        print(f"  UNSIGNED {tok!r}  line {ln}: ...{ctx}...")
        clean = False

print("  CLEAN" if clean else "  ^ review each hit above")
print('\n"seven" occurrences:', len(re.findall(r"\bseven\b", tex)))
sys.exit(0 if clean else 1)
