#!/usr/bin/env python3
"""Create run_intervention_v3.py: the source-year runner, promoted.

v3 is run_intervention_srcyear.py with:
  * an HONEST docstring (the srcyear copy's docstring is a verbatim copy of
    v2's and still claims "all other entries are bit-identical to the
    committed results", which is false);
  * OUT = results/ (not results_srcyear/);
  * outputs named _v3 so they are never confused with the v2 artifacts.

The v1/v2 artifacts stay untouched, exactly as v2 left v1 untouched.
"""
import ast
import re
from pathlib import Path

SRC = Path("/home/user/repo/wave_e_cod/src/run_intervention_srcyear.py")
DST = Path("/home/user/repo/wave_e_cod/src/run_intervention_v3.py")

text = SRC.read_text(encoding="utf-8")

OLD_DOC_START = '"""\nWave E intervention-selection leg'
NEW_DOC = '''"""
Wave E intervention-selection leg — Northern cod (NAFO 2J3KL), Omega_2016.

Executes protocol_intervention.md (frozen 2026-08-26, before any kernel,
boundary, replay, or retention score was computed): robust viability kernels
of the LRP safe set for a declared catch-policy family under persistent
productivity-shock floors, with the Cor2/Cor5 erosion conversion (expansive
or contraction form, whichever the fitted map admits), supply and stress
replays, a T=5 classification of the observed states, and the frozen
retention rule. The cod-side analogue of wave_e_edwards/src/run_intervention.py.

No forecast module is promoted or demoted here. The survey-start variant, the
oracle, and capelin modules play no role. No Omega_xte row is produced. No
Allee term (the M2 class). Deterministic; no randomness anywhere.

==============================================================================
Batch-6 corrected edition (v3): CATCH-TIMING CONVENTION.
==============================================================================

v3 is the authoritative runner. It differs from v2 by ONE line, and that line
is the whole point.

    v2: pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j + 1]   (DESTINATION year)
    v3: pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j]       (SOURCE year)

WHY THE SOURCE YEAR IS CORRECT
------------------------------
Every parameter estimate in this project comes from run_ladder.fit_params,
which regresses

    dS = np.diff(S)          S[j+1] - S[j]
    C_use = C[:-1]           C[j]                 <-- source-year catch
    resid = dS - (surplus(S[:-1], r, K) - C_use)

i.e. the loss being minimised is  S[j+1] = S[j] + g(S[j]) - C[j].

v2 therefore fitted (r, K) under the source-year convention and then measured
the disturbance classes under the destination-year convention: parameters
from one model, disturbance from another. That hybrid is not a convention and
is indefensible on any view -- if the destination year were correct, the loss
that produced (r, K) would be misspecified and (r, K) would have to be refit
(that refit gives r = 0.2084, g_max = 260.5, classes -442.19/-307.18/-99.79).

Independent evidence that the source year is right (see
E2_CONVENTION_ROOT_CAUSE_v2.md):

  * fitting the blended catch  w*C_j + (1-w)*C_{j+1}  over w in [0,1] gives a
    MSE MONOTONE in w with its optimum at the boundary w = 1 (source year):
    17,713 at w=0  ->  15,026 at w=0.5  ->  12,772 at w=1 (in sample);
    749.5 -> 719.3 -> 696.7 (out of sample, 2008-2015);
    residual lag-1 autocorrelation 0.660 -> 0.620 -> 0.554;
  * it is the convention under which the committed (r, K) were estimated;
  * the project's own campaign_srcyear.py applies a "SINGLE-CONVENTION
    OVERRIDE ... (the map's own convention)" for exactly this reason.

CONSEQUENCES (all differ from the v2/hybrid numbers)
----------------------------------------------------
    residual SD          134.96  ->  114.91
    residual mean        -20.44  ->  -10.88
    residual min        -460.03  ->  -328.97
    residual max        +179.76  ->  +206.55   (signed; v2 stored |max|)
    lag-1 acf             0.652  ->     0.554
    UC_min              -460.03  ->  -328.97
    UC_q05              -318.76  ->  -287.36
    UC_q10              -114.85  ->   -80.87
    vacuous classes       2 of 3 ->     1 of 3   (only the worst)
    q05 BAU kernel T=inf   empty ->  2219.6 kt
    constructive bound    57.61  ->    91.59 kt

v1 and v2 artifacts are left untouched; v3 writes _v3 files.

Run:  python3 src/run_intervention_v3.py
Out:  results/intervention_results_v3.json
      results/intervention_boundaries_v3.csv
"""'''

i = text.index(OLD_DOC_START)
j = text.index('"""', i + 3) + 3
text = text[:i] + NEW_DOC + text[j:]

# output directory: results/ (not results_srcyear/)
text = text.replace('OUT = ROOT / "results_srcyear"', 'OUT = ROOT / "results"')
assert 'ROOT / "results"' in text

# output filenames: _v3
text = text.replace('"intervention_results_v2.json"', '"intervention_results_v3.json"')
text = text.replace('"intervention_boundaries_v2.csv"',
                    '"intervention_boundaries_v3.csv"')
text = text.replace('intervention_results_v2.json and "\n          "results/intervention_boundaries_v2.csv',
                    'intervention_results_v3.json and "\n          "results/intervention_boundaries_v3.csv')

ast.parse(text)
DST.write_text(text, encoding="utf-8")
print("wrote", DST)

# sanity: the residual line must be the source-year one
for ln, line in enumerate(text.splitlines(), 1):
    if "c_ann[" in line and "pred" in line:
        print(f"  line {ln}: {line.strip()}")
        assert "c_ann[j]" in line, "NOT the source-year convention!"
print("  convention verified: SOURCE-YEAR (c_ann[j])")
print("  remaining '_v2' filename references:",
      re.findall(r"intervention_(?:results|boundaries)_v\d+\.\w+", text))
