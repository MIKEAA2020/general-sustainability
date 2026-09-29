#!/usr/bin/env python3
"""Create run_families_v3.py (source-year) and supersede the v2 families script.

run_families_v2.py was written on the registered/v2 (hybrid) basis. Under the
v3 ruling its numbers are wrong. Rather than delete it -- it is an untracked
addition with no history, but silently discarding work is worse -- it is moved
aside under src/superseded_v2/ with a banner that says what it is.
"""
import ast
import shutil
from pathlib import Path

SRC = Path("/home/user/repo/wave_e_cod/src")

# ---------------------------------------------------------------- supersede
old_py = SRC / "run_families_v2.py"
old_csv = SRC / "results" / "e2_families_v2.csv"
sup = SRC / "superseded_v2"
sup.mkdir(exist_ok=True)

BANNER = '''# ===========================================================================
# SUPERSEDED -- DO NOT USE, DO NOT CITE.
#
# This file was generated on the registered (v2) basis. v2 fits (r, K) under
# the SOURCE-YEAR catch convention (run_ladder.fit_params uses C[:-1]) and then
# measures the disturbance under the DESTINATION-YEAR convention. That hybrid
# is not a convention; see repo/wave_e_cod/src/run_intervention_v3.py.
#
# Authoritative replacement: run_families_v3.py  ->  results/e2_families_v3.csv
#
# Reverted 2026-09-28. Retained only so the record of what was done survives.
# ===========================================================================

'''

if old_py.exists():
    txt = old_py.read_text(encoding="utf-8")
    if "SUPERSEDED" not in txt:
        txt = BANNER + txt
    (sup / "run_families_v2.py").write_text(txt, encoding="utf-8")
    old_py.unlink()
    print("moved  run_families_v2.py -> src/superseded_v2/")

if old_csv.exists():
    shutil.move(str(old_csv), str(sup / "e2_families_v2.csv"))
    print("moved  e2_families_v2.csv -> src/superseded_v2/")

(sup / "README.md").write_text(
    "# Superseded v2 (hybrid-basis) artifacts\n\n"
    "`run_families_v2.py` and `e2_families_v2.csv` were produced on the\n"
    "registered v2 basis, which is a **hybrid**: parameters fitted under the\n"
    "source-year catch convention, disturbance classes measured under the\n"
    "destination-year convention.\n\n"
    "The hybrid is not a convention. Under the v3 ruling (source-year is\n"
    "authoritative) these numbers are wrong and must not be cited.\n\n"
    "| | v2 (superseded) | v3 (authoritative) |\n"
    "|---|---|---|\n"
    "| UC_min | -460.03 | -328.97 |\n"
    "| UC_q05 | -318.76 | -287.36 |\n"
    "| UC_q10 | -114.85 | -80.87 |\n"
    "| residual SD | 134.96 | 114.91 |\n\n"
    "Replacements: `run_intervention_v3.py`, `run_families_v3.py`.\n"
    "See `/home/user/E2_REMEDIATION_PLAN.md` for the full audit.\n",
    encoding="utf-8")
print("wrote  src/superseded_v2/README.md")

# ------------------------------------------------------------------ build v3
text = (SRC / "superseded_v2" / "run_families_v2.py").read_text(encoding="utf-8")
# strip the banner we just added
text = text.split("# ===========================================================================\n\n", 1)[-1]

header_old = '''# Regenerate E2 Table 1 on the registered (v2) basis, including the reactive
# families.  Same construction as run_v15b_existing.py, but importing the v2
# runner instead of the source-year runner, and WRITING an archive rather than
# printing to stdout.
'''
header_new = '''# Regenerate E2 Table 1 on the SOURCE-YEAR (v3) basis, including the reactive
# families.  Same construction as run_v15b_existing.py (which is already
# source-year) and of run_families_v2.py (which is NOT), but importing the v3
# runner and WRITING an archive rather than printing to stdout.
#
# v3 is authoritative: it is the only convention under which the committed
# (r, K) = (0.2368694, 5000) are the minimisers of the loss that defines the
# residuals.  See run_intervention_v3.py.
'''
assert header_old in text
text = text.replace(header_old, header_new)
text = text.replace("import run_intervention_v2 as base",
                    "import run_intervention_v3 as base")
text = text.replace('"e2_families_v2.csv"', '"e2_families_v3.csv"')
text = text.replace('print("Registered (v2) basis -- disturbance classes:")',
                    'print("Source-year (v3) basis -- disturbance classes:")')
# the v3 runner lives in src/, and results/ is at wave_e_cod/results
text = text.replace(
    'OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")',
    'OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")')

ast.parse(text)
(SRC / "run_families_v3.py").write_text(text, encoding="utf-8")
print("wrote  src/run_families_v3.py")
