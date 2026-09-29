#!/usr/bin/env python3
"""v29l: make the printed margin series reproducible from its stated inputs.

Section 3.4 prints r_1..r_8 and K*+r_T and introduces them as computed
"with the committed eps = 329.0 kt and a_max = 1.1531".  Recomputing from
those two stated inputs gives 708.4, 1145.8, ... 4567.8 -- not the printed
708.3, 1145.7, ... 4567.4.  The series was in fact generated from the
UNROUNDED archived defect 328.97250244 with the ROUNDED archived
a_max = 1.1531, which reproduces all eight values exactly.  A reader who
checks the arithmetic with the printed inputs is off by up to 0.4 kt.

State the input that was actually used.
"""
import io
import shutil

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
shutil.copy(TEX, "/tmp/v29k_before_margin.tex")
tex = io.open(TEX, encoding="utf-8").read()

old = ("with the committed \\(\\varepsilon = 329.0\\) kt and\n"
       "\\(a_{\\max} = 1.1531\\): ")
new = ("with the committed \\(\\varepsilon = 328.9725\\) kt --- the\n"
       "perpetual-worst class of Section 2.3, printed there to one decimal as\n"
       "\\(329.0\\) --- and \\(a_{\\max} = 1.1531\\): ")
assert tex.count(old) == 1, tex.count(old)
io.open(TEX, "w", encoding="utf-8").write(tex.replace(old, new, 1))
print("margin-series inputs stated as used")
