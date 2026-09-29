#!/usr/bin/env python3
"""Sabotage harness for v29_battery.py.

A green battery is not evidence of coverage. Each mutation here is a
single-site corruption of a number or provenance string the battery claims to
protect; the battery must turn RED on every one. A mutation that leaves the
battery green is a hole in the battery, not a pass.

Replacements are applied to the FIRST occurrence only. For values that recur
legitimately (91.59, 2219.6), a single-site flip is the right test: the battery
must catch it either by an absence check on the foreign value or by a scoped
check on the site, not by a naive whole-document presence count.
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_sib = HERE / "paperE2_cod_intervention_v29.tex"
SRC = _sib if _sib.exists() else Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
_BAT = HERE / "paperE2_cod_intervention_v29_verification.py"
BATTERY = str(_BAT if _BAT.exists() else "/home/user/v29_battery.py")
TMP = Path("/tmp/sab_v29.tex")
base = SRC.read_text(encoding="utf-8")

MUT = [
    ("constructive 91.59 -> 57.61", "91.59", "57.61"),
    ("worst class -329.0 -> -460.0", "-329.0", "-460.0"),
    ("q05 class -287.4 -> -318.8", "-287.4", "-318.8"),
    ("q10 class -80.9 -> -114.9", "-80.9", "-114.9"),
    ("Result 3.4 phi threshold 0.727 -> 0.612", "80.87/296.09 = 0.727", "114.85/296.09 = 0.612"),
    ("Result 3.4 criterion 48.5 -> 84.5", "margin is " + chr(92) + "(48.5" + chr(92) + ")",
     "margin is " + chr(92) + "(84.5" + chr(92) + ")"),
    ("Result 3.4 criterion 5.4 -> 55.4", "(" + chr(92) + "(5.4" + chr(92) + ")) kt",
     "(" + chr(92) + "(55.4" + chr(92) + ")) kt"),
    ("Result 3.4 criterion -37.8 -> -73.8", "margin " + chr(92) + "(-37.8" + chr(92) + ")",
     "margin " + chr(92) + "(-73.8" + chr(92) + ")"),
    ("Section 3.3 q05 arithmetic -114.9 -> -146.3", "172.46 - 287.36 = -114.9", "172.46 - 287.36 = -146.3"),
    ("Section 3.3 worst arithmetic -156.5 -> -287.6", "172.46 - 328.97 = -156.5", "172.46 - 328.97 = -287.6"),
    ("Section 3.7 K=1000 constructive -28.87 -> -62.9", "-28.87", "-62.9"),
    ("Section 3.10 F' median 1.142 -> 1.134", "1.142", "1.134"),
    ("Section 3.10 F' interval [1.010, 1.179] -> [1.001, 1.177]", "[1.010, 1.179]", "[1.001, 1.177]"),
    ("bootstrap interval 121.1 -> 84.8", "121.1", "84.8"),
    ("abstract survival 0.91 -> 0.87", chr(92) + "(0.91" + chr(92) + ")",
     chr(92) + "(0.87" + chr(92) + ")"),
    ("abstract survival 0.65 -> 0.58", "to " + chr(92) + "(0.65" + chr(92) + ") between",
     "to " + chr(92) + "(0.58" + chr(92) + ") between"),
    ("certified horizon T=7 -> T=6", r"from \(T = 7\) under the perpetual", r"from \(T = 6\) under the perpetual"),
    ("certified horizon T=8 -> T=7", r"from \(T = 8\) under the 10th-percentile", r"from \(T = 7\) under the 10th-percentile"),
    ("certified set 4560.3 -> 4942.7", "4560.3", "4942.7"),
    ("certified set 5132.9 -> 5132.0", "5132.9", "5132.0"),
    ("certified set 4593.2 -> 4593.0", "4593.2", "4593.0"),
    ("one-year claim -> two years", "lengthens the horizon by one year at every class", "lengthens the horizon by two years at every class"),
    ("naive criterion reinstated", "What fails is the trajectory, not the", "The certified kernel is nonempty only while K* + r_T < K; what fails is the trajectory, not the"),
    ("Table 1 BAU q05 T=inf cell", "BAU (5 kt) & 1025.5", "BAU (5 kt) & 1025.5X"),
    ("Table 1 Family A phi=0.75 q10", "1161.0 & empty & 1119.9 & empty & 920.2", "1161.0 & empty & 1119.9 & empty & 925.2"),
    ("Table 2 Allee q05 T=1 939.4 -> 939.9", "= 642.3) & 939.4", "= 642.3) & 939.9"),
    ("Table 2 declared q05 T=inf 1024.1 -> 1034.1", "1024.1", "1034.1"),
    ("Table 2 Fox q05 T=1 1008.4 -> 1008.9", "1008.4", "1008.9"),
    ("Table 3 K=1000 T=1 943.2 -> 1009.2", "943.2", "1009.2"),
    ("Table 3 K=5000 r cell", "5000 (registered) & 0.2369", "5000 (registered) & 0.2569"),
    ("Table 4 120 kt i.i.d. 0.647 -> 0.580", "120 kt & 0.647", "120 kt & 0.580"),
    ("Table 5 zero-catch q05 n=5 1280.8 -> 1285.0", "zero catch & 1280.8", "zero catch & 1285.0"),
    ("Table 6 xteNCAM constructive -48.0 -> 57.0", "48.0", "57.0"),
    ("Fox constructive 79.05 -> 45.08", "159.92 - 80.87 = 79.05", "159.92 - 80.87 = 45.08"),
    ("Fox r 0.1044 -> 0.2084", "0.1044", "0.2084"),
    ("Allee g_max 372.4 -> 372.9", "372.4", "372.9"),
    ("declared row g_max 883.6 -> 893.6", "883.6", "893.6"),
    ("Section 3.6 120-kt qualification removed (922.7 -> 922.9)", "922.7", "922.9"),
    ("Section 3.11 convention reverted", "refitted in the same source-year convention", "refitted in the registered convention"),
    ("figure directory reverted (all 7)", "figs_e2_v3/", "figs_e2/"),
    ("provenance: runner de-promoted", r"run\_intervention\_v3.py", r"run\_intervention\_v2.py"),
    ("provenance: elevation campaign de-promoted", r"campaign\_e2\_elevation\_v3.py", r"campaign\_e2\_elevation.py"),
    ("provenance: fox campaign de-promoted", r"campaign\_e2\_fox\_form\_v3.py", r"campaign\_e2\_fox\_form.py"),
    ("determinism claim restored", "The analysis is reproducible", "The analysis is fully deterministic (no random components)"),
    ("Section 2.3 deleted", chr(92) + "subsubsection{2.3 The catch-timing convention}", chr(92) + "subsubsection{2.3 XXX}"),
    ("Section 2.3 provenance gap deleted", "archived source documentation records whether", "archived source documentation settles whether"),
    # the triples are written as \(-329.0\)/\(-287.4\)/\(-80.9\), so the
    # mutation has to carry the LaTeX delimiters to target Section 2.3
    ("Section 2.3 source-year third class corrupted", "-80.9" + chr(92) + ") kt against", "-114.9" + chr(92) + ") kt against"),
    ("Section 2.3 source-year first class corrupted", chr(92) + "(-329.0" + chr(92) + ")/", chr(92) + "(-460.0" + chr(92) + ")/"),

    # --- the prose-coherence pass (R17/R18) --------------------------------
    # Each of these is a claim the end-to-end read had to repair or add; if the
    # battery does not turn red on it, the repaired prose is unprotected.
    ("3.8 i.i.d. P>=0.9 crossing 13.5 -> 31.5", "interpolated crossing is " + chr(92) + "(13.5",
     "interpolated crossing is " + chr(92) + "(31.5"),
    ("3.8 i.i.d. ceiling 0.906 -> 0.806", "ceiling of " + chr(92) + "(0.906" + chr(92) + ") at",
     "ceiling of " + chr(92) + "(0.806" + chr(92) + ") at"),
    ("3.8 block ceiling 0.852 -> 0.802", "there being " + chr(92) + "(0.852" + chr(92) + ")",
     "there being " + chr(92) + "(0.802" + chr(92) + ")"),
    ("3.8 block sweep value 0.849 -> 0.894", chr(92) + "(0.849" + chr(92) + ") in the crossing sweep",
     chr(92) + "(0.894" + chr(92) + ") in the crossing sweep"),
    ("3.8 60-kt survival 0.835 -> 0.385", "fallen to " + chr(92) + "(0.835" + chr(92) + ")",
     "fallen to " + chr(92) + "(0.385" + chr(92) + ")"),
    ("3.8 no-1992 survival at the bound 0.84 -> 0.85", chr(92) + "(0.84" + chr(92) + ") when",
     chr(92) + "(0.85" + chr(92) + ") when"),
    ("3.8 the bar claim reinstated (i.i.d. not attained)",
     "it is attained, but only by near-moratorium catches",
     "it is not attained by any tested constant catch"),
    ("3.8 the block bar claim flipped",
     "Under block resampling it is not attained at all", "Under block resampling it is attained"),
    ("3.8 the seed caveat dropped", "carries its own fixed seed", "carries the same fixed seed"),
    ("3.8 evaluated grid catch 92.5 -> 29.5", chr(92) + "(92.5" + chr(92) + ") kt on the campaign",
     chr(92) + "(29.5" + chr(92) + ") kt on the campaign"),
    ("3.8 immediate-breach probability 0.083 -> 0.038", "2/24 = 0.083", "2/24 = 0.038"),
    ("3.8 total failure probability 0.094 -> 0.099", chr(92) + "(0.094" + chr(92) + "),",
     chr(92) + "(0.099" + chr(92) + "),"),
    ("3.8 second fatal residual -323.5 -> -332.5", chr(92) + "(-323.5" + chr(92) + ") kt)",
     chr(92) + "(-332.5" + chr(92) + ") kt)"),
    ("3.8 breach threshold -172.5 -> -127.5", "worse than " + chr(92) + "(-172.5",
     "worse than " + chr(92) + "(-127.5"),
    ("3.8 grown-clear threshold 1020 -> 1200", "past about " + chr(92) + "(1020" + chr(92) + ") kt",
     "past about " + chr(92) + "(1200" + chr(92) + ") kt"),
    ("3.8 1/24-only ceiling 0.427 -> 0.472", "= 0.427", "= 0.472"),
    ("3.6 Allee g(K*) 196.06 -> 169.06", "196.06 - 80.87 = 115.2", "169.06 - 80.87 = 115.2"),
    ("3.6 Allee constructive 115.2 -> 151.2", "196.06 - 80.87 = 115.2", "196.06 - 80.87 = 151.2"),
    ("3.6 declared-strength constructive 123.3 -> 132.3", chr(92) + "(123.3" + chr(92) + ") kt on the declared",
     chr(92) + "(132.3" + chr(92) + ") kt on the declared"),
    ("3.6 Allee 60-kt q05 boundary 1131.1 -> 1113.1", chr(92) + "(1131.1" + chr(92) + ") kt against BAU",
     chr(92) + "(1113.1" + chr(92) + ") kt against BAU"),
    ("3.6 the margin-not-emptiness clause dropped",
     "the block operates through a margin rather than through emptiness",
     "the block operates through emptiness"),
    ("3.6 grid/interval cell count 81 -> 80", chr(92) + "(81" + chr(92) + ") cells the campaign checks",
     chr(92) + "(80" + chr(92) + ") cells the campaign checks"),
    ("3.6 grid/interval agreement loosened 0.06 -> 0.6",
     "at most " + chr(92) + "(0.06" + chr(92) + ") kt", "at most " + chr(92) + "(0.6" + chr(92) + ") kt"),
    ("3.6 a T=inf difference corrupted 0.9 -> 0.5", chr(92) + "(0.1" + chr(92) + "), " + chr(92) + "(0.3" + chr(92) + "), " + chr(92) + "(0.6" + chr(92) + ") and " + chr(92) + "(0.9" + chr(92) + ") kt",
     chr(92) + "(0.1" + chr(92) + "), " + chr(92) + "(0.3" + chr(92) + "), " + chr(92) + "(0.6" + chr(92) + ") and " + chr(92) + "(0.5" + chr(92) + ") kt"),
    ("3.6 the 'not tabulated' label dropped", "not carried in Table 2", "carried in Table 2"),
    ("2.3 'whole analysis' overclaim reinstated",
     "the primary kernels and their boundary tables were also computed",
     "the whole analysis was also computed"),
    ("abstract class-vacuity verb reverted", "reading narrows", "reading reverses"),
    ("code availability reverted to the v24 script", chr(92) + "_v29" + chr(92) + "_verification.py",
     chr(92) + "_v24" + chr(92) + "_verification.py"),
    ("data availability convergence guard dropped",
     "refuses to return an unconverged iterate", "returns the final iterate"),

    # --- the structural pass (R19) and the identification pass (R20/R21) -----
    ("C_vac 215.2 -> 251.2", "C_{\\mathrm{vac}} = 215.2",
     "C_{\\mathrm{vac}} = 251.2"),
    ("safe-set threshold 0.531 -> 0.731", "1 - 80.87/172.46 = 0.531",
     "1 - 80.87/172.46 = 0.731"),
    ("nonempty threshold 0.727 -> 0.531", "1 - 80.87/296.09 = 0.727",
     "1 - 80.87/296.09 = 0.531"),
    ("Family A margin 5.4 -> 67.2 (the superseded value)",
     "the margin is " + chr(92) + "(48.5" + chr(92) + ") (" + chr(92) + "(5.4"
     + chr(92) + ")) kt",
     "the margin is " + chr(92) + "(48.5" + chr(92) + ") (" + chr(92) + "(67.2"
     + chr(92) + ")) kt"),
    ("Family A margin -37.8 -> -6.8 (the superseded value)",
     "margin " + chr(92) + "(-37.8" + chr(92) + ") kt",
     "margin " + chr(92) + "(-6.8" + chr(92) + ") kt"),
    ("the phi=0.60 Table 1 row corrupted",
     "=0.60 & 1131.2 & empty & 1091.0 & empty & 895.2 &\n1074.8",
     "=0.60 & 1131.2 & empty & 1091.0 & empty & 895.2 &\n884.6"),
    ("Proposition 2.1 deleted", "Proposition 2.1 (Constructive bound",
     "Proposition 2.1 (Constructive"),
    ("a proposition proof deleted", "emph{Proof.} One step from " + chr(92) + "(K^*" + chr(92) + ") gives",
     "One step from " + chr(92) + "(K^*" + chr(92) + ") gives"),
    ("the budget identity weakened to an inequality",
     "margin plus its catch equal", "margin plus its catch are at most"),
    # a plain space: apply_mut rejoins the words with \s+, which is what
    # matches the source's line break.  A literal backslash-n in the pattern
    # matches nothing, because the file holds a real newline there.
    ("profile set endpoint: the grid top replaced by the box edge",
     "set running from " + chr(92) + "(1500" + chr(92) + ") kt to the top of the grid",
     "set running from " + chr(92) + "(1500" + chr(92) + ") kt to "
     + chr(92) + "(5000" + chr(92) + ") kt"),
    ("profile ratio 1.027 -> 1.27", "1.027" + chr(92) + ") times the profiled",
     "1.27" + chr(92) + ") times the profiled"),
    ("g(K*) profile range corrupted",
     chr(92) + "([148.8, 176.1]" + chr(92) + ")",
     chr(92) + "([138.8, 176.1]" + chr(92) + ")"),
    ("C* profile range corrupted", chr(92) + "([67.9, 95.2]" + chr(92) + ")",
     chr(92) + "([57.9, 95.2]" + chr(92) + ")"),
    ("joint bootstrap median 88.1 -> 8.1",
     "bound has median " + chr(92) + "(88.1" + chr(92) + ")",
     "bound has median " + chr(92) + "(8.1" + chr(92) + ")"),
    ("observation-error endpoint 112.1 -> 121.1",
     "to " + chr(92) + "(112.1" + chr(92) + ") kt at "
     + chr(92) + "(" + chr(92) + "lambda = 0.5" + chr(92) + ")",
     "to " + chr(92) + "(121.1" + chr(92) + ") kt at "
     + chr(92) + "(" + chr(92) + "lambda = 0.5" + chr(92) + ")"),
    ("Table 7 NCAM 1995-2015 C* corrupted",
     "NCAM 1995--2015 & 20 & 0.2731 & 5000 (ub) & 198.9 & 27.4 & 171.4 & 1.176",
     "NCAM 1995--2015 & 20 & 0.2731 & 5000 (ub) & 198.9 & 27.4 & 117.4 & 1.176"),
    ("Table 7 xteNCAM 2005-2024 C* corrupted",
     "xteNCAM 2005--2024 & 19 & 0.4439 & 472 (lb) & 50.9 & 58.5 & -7.7 & 0.925",
     "xteNCAM 2005--2024 & 19 & 0.4439 & 472 (lb) & 50.9 & 58.5 & -0.7 & 0.925"),
    ("the regime finding softened", "0 " + chr(92) + "pm 8" + chr(92) + ") kt",
     "0 " + chr(92) + "pm 80" + chr(92) + ") kt"),
    ("the bound-status caveat dropped", "at a bound, so these are regime readings",
     "at a bound, so these are estimates"),
    ("a new figure reference reverted", "fig9_identification.png",
     "fig9_identification_old.png"),
]


# CONTROL: the battery must be green on the unmutated file. Without this, a
# permanently-failing check makes every mutation "caught" and the harness
# reports a perfect score on a battery that never passed. (This actually
# happened: a Section 2.3 check kept its LaTeX markup and failed always.)
r0 = subprocess.run([sys.executable, BATTERY, str(SRC)],
                    capture_output=True, text=True)
print("CONTROL: battery on the unmutated tex -> exit %d" % r0.returncode)
if r0.returncode != 0:
    print("ABORT: the battery is not green, so 'CAUGHT' below would be "
          "meaningless. Fix the battery first.")
    print("\n".join(l for l in r0.stdout.splitlines() if l.startswith("FAIL")))
    sys.exit(1)

def apply_mut(text, old, new, count=1):
    """Splice `old` -> `new`, tolerating the source's mid-sentence line wraps.

    A literal splice is tried first. If `old` is absent it is almost always
    because the phrase is split across two source lines, in which case the
    words are rejoined with <whitespace>. A pattern that is nowhere to be
    found is
    reported as a setup failure rather than silently doing nothing -- a
    mutation that never lands proves nothing about the battery.
    """
    if old in text:
        return text.replace(old, new, count), text.count(old)
    # written with chr(92) so the source carries exactly one backslash:
    # a doubled one (r"\\s+") matches a literal backslash,
    # never the line break it was meant to span.
    _WS = chr(92) + "s+"
    rx = re.compile(_WS.join(re.escape(w) for w in old.split()))
    hits = len(rx.findall(text))
    if not hits:
        return None, 0
    return rx.sub(lambda m: new, text, count=count), hits


bad = []
for name, old, new in MUT:
    n = 7 if "figure directory" in name else 1
    mutated, c = apply_mut(base, old, new, n)
    if mutated is None:
        bad.append("SETUP %s: pattern not found" % name)
        print("SETUP-FAIL  " + name)
        continue
    TMP.write_text(mutated, encoding="utf-8")
    r = subprocess.run([sys.executable, BATTERY, str(TMP)],
                       capture_output=True, text=True)
    red = r.returncode != 0
    print(("CAUGHT  " if red else "MISSED  ") + name + ("  (x%d)" % c if c > 1 else ""))
    if not red:
        bad.append("MISSED " + name)
        tail = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
        print("   " + ("\n   ".join(tail) if tail else r.stdout[-300:]))

print()
print("%d mutations, %d holes" % (len(MUT), len(bad)))
for b in bad:
    print("  " + b)
sys.exit(1 if bad else 0)
