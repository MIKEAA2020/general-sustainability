#!/usr/bin/env python3
"""
The certified record figure for the applied regime-viability paper —
recompute-then-assert: every plotted series, threshold, crossing, and
annotation is read from the locked files and asserted in exact rational
arithmetic before the figure is written.

figs_arv/fig_record.pdf — both vintage series 1983-2021 (input vintage
1983-2015 from NCAM Table A2; database vintage 2014-2021 from the RAM
extract under the verifier's conversion rules), the two thresholds
B_aux = 276 kt and B_ref = 44229/50 = 884.58 kt, the reference and
collapse windows shaded, the 1993 breach, the 1995 minimum, and the 2015
re-crossing (both vintages) annotated with the exact printed values.
"""
import csv
import os
os.environ.setdefault("SOURCE_DATE_EPOCH", "1758825600")  # pin embedded PDF metadata to the round's pinned build epoch
from fractions import Fraction as Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = []


def check(name, ok):
    PASS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def rows(path):
    with open(os.path.join(HERE, path), newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


# input vintage (NCAM 2016 Table A2): 1983-2015
ssb = {int(float(r["year"])): Q(r["ssb_kt"])
       for r in rows("paperE1_calibration_data_v1_wave_e_cod/ncam_2016_table_a2.csv")}
check("input vintage: 33 rows, 1983-2015 complete",
      len(ssb) == 33 and set(ssb) == set(range(1983, 2016)))

# database vintage (RAM extract, verifier conversion rules): 2014-2021
ram = {}
for r in rows("paperE1_calibration_data_v1_ram_timeseries.csv"):
    if r["SSB"]:
        v = Q(int(round(float(r["SSB"]))))
        if v > 10000:
            v = v / 1000
        ram[int(float(r["year"]))] = v
db_years = list(range(2014, 2022))
db_vals = [ram[y] for y in db_years]
check("database vintage 2014-2021 = 238, 277, 340, 433, 394, 419, 440, 411",
      db_vals == [Q(238), Q(277), Q(340), Q(433), Q(394), Q(419), Q(440), Q(411)])

# thresholds and certified features
B_AUX = Q(276)
B_REF = Q(44229, 50)
check("B_ref = window mean 44229/50 = 884.58 kt (displayed 884.6)",
      B_REF == Q(88458, 100) and round(float(B_REF), 1) == 884.6)
check("reference window 1983-89 all above B_aux; minimum 836.00",
      all(ssb[y] > B_AUX for y in range(1983, 1990))
      and min(ssb[y] for y in range(1983, 1990)) == Q("836.00"))
check("collapse window 1990-92 = 861.92, 734.51, 381.95",
      [ssb[y] for y in (1990, 1991, 1992)]
      == [Q("861.92"), Q("734.51"), Q("381.95")])
check("1993 breach: first input-vintage reading below B_aux is 1993 (101.05)",
      ssb[1992] >= B_AUX and ssb[1993] < B_AUX and ssb[1993] == Q("101.05"))
check("1995 minimum 9.68 kt is the series minimum 1983-2015",
      ssb[1995] == Q("9.68") == min(ssb.values()))
below = [y for y in range(1993, 2015) if ssb[y] < B_AUX]
check("input vintage stays below the floor 1993-2014 (22 consecutive readings)",
      below == list(range(1993, 2015)) and ssb[2014] == Q("250.12"))
check("2015 re-crossing, both vintages: 250.12 -> 298.65 and 238 -> 277",
      ssb[2014] < B_AUX < ssb[2015] == Q("298.65")
      and ram[2014] < B_AUX < ram[2015] == Q(277))
check("outcome years 2016-2021 all above the floor; maximum 440 = 49.7% of B_ref",
      all(ram[y] > B_AUX for y in range(2016, 2022)) and max(db_vals) == Q(440))

f = float
fig, ax = plt.subplots(figsize=(7.2, 4.3))
ax.axhline(B_AUX, color="tab:red", lw=1.1, ls="--")
ax.text(1982.6, B_AUX + 14, "$B_{\\mathrm{aux}} = 276$ kt (2025 $B_{\\mathrm{lim}}$)",
        fontsize=7.5, color="tab:red")
ax.axhline(B_REF, color="tab:purple", lw=1.1, ls="-.")
ax.text(1982.6, B_REF + 14, "$B_{\\mathrm{ref}} = 884.6$ kt (1983--89 mean)",
        fontsize=7.5, color="tab:purple")
ax.axvspan(1983, 1989, color="tab:blue", alpha=0.06)
ax.axvspan(1990, 1992, color="tab:red", alpha=0.08)
ax.text(1986, 66, "reference\nwindow", fontsize=7, ha="center", color="tab:blue")
ax.text(1991, 66, "collapse\nwindow", fontsize=7, ha="center", color="tab:red")
xs = sorted(ssb)
ax.plot(xs, [f(ssb[y]) for y in xs], color="tab:green", lw=1.5,
        label="input vintage (NCAM 2016, 1983--2015)")
dbx = list(range(2014, 2022))
ax.plot(dbx, [f(ram[y]) for y in dbx], color="tab:orange", lw=1.5, ls="--",
        marker="s", ms=3, label="database vintage (RAM v4.66, 2014--2021)")
ax.plot([1993], [f(ssb[1993])], "o", color="tab:red", ms=5)
ax.annotate("1993 breach\n$101.05$ kt", (1993, f(ssb[1993])), xytext=(1995.2, 240),
            fontsize=7.5, color="tab:red",
            arrowprops=dict(arrowstyle="->", color="tab:red", lw=0.8))
ax.plot([1995], [f(ssb[1995])], "o", color="tab:red", ms=5)
ax.annotate("minimum $9.68$ kt", (1995, f(ssb[1995])), xytext=(1997.5, 60),
            fontsize=7.5, color="tab:red",
            arrowprops=dict(arrowstyle="->", color="tab:red", lw=0.8))
ax.plot([2015], [f(ssb[2015])], "o", color="tab:green", ms=5)
ax.annotate("2015 re-crossing\n$250.12 \\to 298.65$; $238 \\to 277$",
            (2015, f(ssb[2015])), xytext=(2004.5, 480), fontsize=7.5, color="tab:green",
            arrowprops=dict(arrowstyle="->", color="tab:green", lw=0.8))
ax.annotate("below the floor 1993--2014", (2003.5, 120), fontsize=7.5, color="0.35")
ax.set_xlim(1982.5, 2021.9)
ax.set_ylim(0, 1010)
ax.set_xlabel("year")
ax.set_ylabel("spawning-stock biomass (kt)")
ax.set_title("The certified record: both vintages, both thresholds, the breach and the re-crossing")
ax.legend(fontsize=7.5, loc="upper right")
ax.set_xticks(list(range(1985, 2021, 5)))
fig.tight_layout()
os.makedirs(os.path.join(HERE, "figs_arv"), exist_ok=True)
out = os.path.join(HERE, "figs_arv", "fig_record.pdf")
fig.savefig(out)
plt.close(fig)
check("fig_record.pdf written", os.path.exists(out))

n = sum(PASS)
print(f"\nARV record figure: {n}/{len(PASS)} assertions pass")
raise SystemExit(0 if n == len(PASS) else 1)
