"""Generate all LaTeX tables (main + SI) from work/results.json."""
import json, pathlib
from fractions import Fraction as Q

root = pathlib.Path(__file__).resolve().parent.parent
R = json.load(open(root / "work" / "results.json"))
out = root / "si_parts"
out.mkdir(exist_ok=True)


def frac(s):
    q = Q(str(s))
    if q.denominator == 1:
        return f"${q.numerator}$"
    return f"$\\tfrac{{{q.numerator}}}{{{q.denominator}}}$"


def num(n):
    return f"{int(n):,}".replace(",", "{,}")


def cellstr(c):
    return "".join("+" if x == 1 else "-" for x in c)


def write(name, body):
    (out / name).write_text(body if body.endswith("\n") else body + "\n")
    print("wrote", name)


# ---------------- main: alpha table
P = R["pbvi"]
rows = []
for L in range(16):
    r4 = P["4"]["pbvi"]["levels"][str(L)]
    r5 = P["5"]["pbvi"]["levels"][str(L)]
    a4 = f"{r4['n_masks']['4']} ({r4['n_masks_survivable']['4']})"
    a5 = f"{num(r5['n_masks']['4'])} ({num(r5['n_masks_survivable']['4'])})"
    r6 = P["6"]["pbvi"]["levels"].get(str(L))
    a6 = f"{num(r6['n_masks']['3'])} ({num(r6['n_masks_survivable']['3'])})" if r6 else "--"
    rows.append(f"{L} & {a4} & {a5} & {a6}\\\\")
body = ("\\begin{tabular}{rlll}\n\\toprule\n$L$ & $m=4$, $k=4$ & $m=5$, $k=4$ & $m=6$, $k=3$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_alpha_main.tex", body)

# ---------------- runtime
T = R["times"]
rows = [("Classification $m=4,5,6$ (cliques, orbits, LPs, certified thresholds, census)", T["classification"]),
        ("Pair tables and horizons", T["pairs"]),
        ("Observation (ladders, feedback game $m=4,5$, deadline horizons)", T["observation"]),
        ("Point-based sweeps and obstructions", T["pbvi"]),
        ("Floating-point study ($10^5$-step simulations, $1{,}280$-set sweep)", T["float"]),
        ("Total", T["total"])]
body = ("\\begin{tabular}{lr}\n\\toprule\nStage & seconds\\\\\n\\midrule\n"
        + "\n".join(f"{a} & {b:.1f}\\\\" for a, b in rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_runtime.tex", body)
C6 = R["classification"]["6"]
detail = ("\\begin{tabular}{lr}\n\\toprule\nSix-cube classification stage & seconds\\\\\n\\midrule\n"
          + "Complete six-cube classification (inside the stage above) & %.1f\\\\\n" % C6["time_s"]
          + "Float sweep over the $1{,}280$ boundary sets & %.1f\\\\\n" % R["float"]["sweep"]["time_s"]
          + "\\bottomrule\n\\end{tabular}")
write("tab_runtime_detail.tex", detail)

# ---------------- pairs
rows = []
for m in ("4", "5", "6"):
    for r in R["pairs"][m]:
        if r["survivable"]:
            rows.append(f"{m} & {r['h']} & {frac(r['V'])} & yes & {r['threshold']} & -- \\\\")
        else:
            hz = "; ".join(f"{h['L']}: {h['exact']} ({h['bound']})" for h in r["horizon"])
            rows.append(f"{m} & {r['h']} & {frac(r['V'])} & no & -- & {hz}\\\\")
body = ("\\begin{tabular}{rrrlll}\n\\toprule\n$m$ & $h$ & $V$ & survivable & $L^\\ast$ & exact horizon (LP bound) from $L=0,5,10,15,20$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_pairs.tex", body)

# ---------------- clique orbits m=5, m=6
for m in ("5", "6"):
    rows = []
    for o in R["classification"][m]["maximal_clique_orbits"]:
        y = "(" + ",".join(str(Q(v)) for v in o["y"]) + ")"
        rows.append(f"{o['size']} & {num(o['orbit'])} & {frac(o['V'])} & ${y}$ & {'yes' if o['survivable'] else 'no'}\\\\")
    body = ("\\begin{tabular}{rrrll}\n\\toprule\nsize & orbit & $V$ & maximiser $y$ & survivable\\\\\n\\midrule\n"
            + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
    write(f"tab_m{m}_cliques.tex", body)

# ---------------- maximal survivable orbits with certificates
for m in ("4", "5", "6"):
    rows = []
    for o in R["classification"][m]["maximal_survivable_orbits"]:
        c = o["threshold_cert"]
        lost = c.get("lower_steps") if c.get("lower_steps") is not None else "--"
        cap = c.get("cap") if o["threshold"] else "--"
        rows.append(f"{o['size']} & {num(o['orbit'])} & {frac(o['V'])} & {o['first_step_bound']} & {o['threshold']} & {cap} & {c.get('antichain','--')} & {lost} & {o['word_period']} / {o['word_dip']} & {o['subset_knife_edge']}\\\\")
    body = ("\\begin{tabular}{rrrrrrrrlr}\n\\toprule\nsize & orbit & $V$ & $f(S)$ & $L^\\ast$ & cap & antichain & lost after & word period / dip & boundary subsets\\\\\n\\midrule\n"
            + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
    write(f"tab_m{m}_maximal.tex", body)

# representative cells and subset threshold histograms (m=6)
rows = []
for o in R["classification"]["6"]["maximal_survivable_orbits"]:
    cells = ", ".join("\\texttt{" + cellstr(c) + "}" for c in o["cells"])
    hist = ", ".join(f"$L^\\ast={k}$: {num(v)}" for k, v in o["subset_threshold_hist"])
    y = "(" + ",".join(str(Q(v)) for v in o["y"]) + ")"
    rows.append(f"\\item[{o['size']} cells, orbit {num(o['orbit'])}.] $y={y}$. Cells: {cells}. Nonempty subsets by threshold: {hist}.")
write("tab_m6_reps.tex", "\\begin{description}[leftmargin=1.5em,style=nextline]\n" + "\n".join(rows) + "\n\\end{description}")

# ---------------- census per level
rows = []
for m in ("4", "5", "6"):
    cl = R["classification"][m]
    for c in cl["census"]:
        sizes = ", ".join(f"${s}\\times{num(n)}$" for s, n in c["maximal_sizes"])
        rows.append(f"{m} & {c['L']} & {num(c['n_survivable'])} & {num(c['n_maximal'])} & {sizes} & {num(cl['n_cliques_nonempty'])} & $2^{{{cl['n_cells']}}}$\\\\")
body = ("\\begin{tabular}{rrrrlrl}\n\\toprule\n$m$ & $L$ & survivable & maximal & sizes & admissible & power set\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_census_full.tex", "\\resizebox{\\textwidth}{!}{%\n" + body + "}")

# ---------------- threshold histograms and knife edge
rows = []
for m in ("4", "5", "6"):
    cl = R["classification"][m]
    hist = ", ".join(f"$L^\\ast={k}$: {num(v)}" for k, v in cl["threshold_hist"])
    rows.append(f"{m} & {num(cl['n_survivable_some_level'])} & {hist} & {num(cl['knife_edge_sets'])} & {cl['n_uncertified_thresholds']}\\\\")
body = ("\\begin{tabular}{rrlrr}\n\\toprule\n$m$ & survivable sets & threshold histogram & $V=\\tfrac52$ exactly & uncertified\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_thresholds.tex", "\\resizebox{\\textwidth}{!}{%\n" + body + "}")

# ---------------- obstructions
rows = []
for m in ("4", "5", "6"):
    ob = R["pbvi"][m]["obstructions"]
    fp = ", ".join(f"$h={h}$: {num(n)} ($V={frac(ob['far_pair_V'][str(h)]).strip('$')}$)" for h, n in ob["far_pairs_by_distance"])
    inside = ", ".join(f"{s} cells: {num(n)} ($V={frac(v).strip('$')}$)" for (s, v), n in ob["by_size_V"]) or "none"
    rows.append(f"{m} & {fp} & {num(ob['n_nonsurvivable_cliques'])} & {inside} & {frac(ob['V_max_all'])}\\\\")
body = ("\\begin{tabular}{rp{4.2cm}rp{4.5cm}r}\n\\toprule\n$m$ & far pairs by distance & admissible non-survivable & minimal obstructions inside the admissible family & $\\max V$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_obstructions.tex", "\\resizebox{\\textwidth}{!}{%\n" + body + "}")

# ---------------- ladder (full)
rows = []
for m in ("4", "5", "6"):
    lad = R["observation"][m]["ladder"]
    for L, row in sorted(lad.items(), key=lambda kv: int(kv[0])):
        cells = " & ".join(frac(v) for v in row)
        pad = " & ".join([""] * (6 - int(m)))
        rows.append(f"{m} & {L} & {pad}{' & ' if pad else ''}{cells}\\\\")
body = ("\\begin{tabular}{rrccccccc}\n\\toprule\n$m$ & $L$ & $j=6$ & $5$ & $4$ & $3$ & $2$ & $1$ & $0$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_ladder_full.tex", body)

# ---------------- feedback
rows = []
for m in ("4", "5"):
    fb = R["observation"][m]["feedback"]
    rows.append(f"{m} & whole cube & $2^{m}$ & $\\infty$ & {fb['cube']}\\\\")
    for j, v in sorted(fb["subcubes"].items(), key=lambda kv: int(kv[0])):
        bl = fb["subcubes_blind"][str(j)]
        bl = "$\\infty$" if bl is None else bl
        rows.append(f"{m} & subcube $j={j}$ & $2^{j}$ & {bl} & {v}\\\\")
    for h, d in sorted(fb["shells"].items(), key=lambda kv: int(kv[0])):
        b = d["blind"] if d["blind"] is not None else "$\\infty$"
        rows.append(f"{m} & shell $h={h}$ & {d['size']} & {b} & {d['feedback']}\\\\")
body = ("\\begin{tabular}{rlrrr}\n\\toprule\n$m$ & class & cells & blind $L^\\ast$ & feedback $F^\\ast$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_feedback.tex", body)

# ---------------- deadline
rows = []
for m in ("4", "5", "6"):
    d = R["observation"][m]["deadline"]
    cs = R["observation"][m]["cell_sum"]
    for r in d["rows"]:
        rows.append(f"{m} & {r['L']} & {r['exact_horizon']} & {r['lp_bound']} & {r['hold_steps']}\\\\")
body = ("\\begin{tabular}{rrrrr}\n\\toprule\n$m$ & $L$ & exact horizon & LP bound $\\lfloor L/5\\rfloor$ & hold steps\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_deadline.tex", body)

# ---------------- alpha full tables m=4, m=5
for m in ("4", "5"):
    rows = []
    for L in range(16):
        r = P[m]["pbvi"]["levels"][str(L)]
        cells = " & ".join(f"{num(r['n_masks'][str(k)])} ({num(r['n_masks_survivable'][str(k)])})" for k in range(1, 5))
        rows.append(f"{L} & {cells}\\\\")
    body = ("\\begin{tabular}{rllll}\n\\toprule\n$L$ & $k=1$ & $k=2$ & $k=3$ & $k=4$\\\\\n\\midrule\n"
            + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
    write(f"tab_alpha{m}.tex", body)

# ---------------- values at beliefs
names = [("uniform", "uniform"), ("far_pair", "far pair"), ("antipodal_pair", "antipodal pair"),
         ("ball_plus_antipode", "ball + antipode"), ("random1", "random 1"), ("random2", "random 2"), ("random3", "random 3")]
for m in ("4", "5"):
    rows = []
    for L in range(16):
        r = P[m]["pbvi"]["levels"][str(L)]["values"]
        cells = []
        for key, lab in names:
            v = r[key]
            cells.append("/".join(frac(v[str(k)]).strip("$") for k in range(1, 5)) + " $\\mid$ " + frac(v["inf"]).strip("$"))
        rows.append(f"{L} & " + " & ".join("$" + c.replace("$\\mid$", "\\mid") + "$" for c in cells) + "\\\\")
    head = " & ".join(lab for _, lab in names)
    body = ("\\begin{tabular}{r" + "l" * len(names) + "}\n\\toprule\n$L$ & " + head + "\\\\\n\\midrule\n"
            + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
    write(f"tab_values{m}.tex", "\\resizebox{\\textwidth}{!}{%\n" + body + "}")

# ---------------- float
F = R["float"]
rows = []
for k, v in F["simulation"].items():
    rows.append(f"ten-set, $L=3$ & {k.replace('_', ' ')} & {v['n_false_deaths']} & {v['first_false_death_step'] if v['first_false_death_step'] is not None else '--'} & {float(v['max_abs_deviation']):.2e}\\\\")
for k, v in F["pair_m4"].items():
    rows.append(f"adjacent pair $m=4$, $L=1$ & {k.replace('_', ' ')} & {v['n_false_deaths']} & {v['first_false_death_step'] if v['first_false_death_step'] is not None else '--'} & {float(v['max_abs_deviation']):.2e}\\\\")
body = ("\\begin{tabular}{llrrr}\n\\toprule\ninstance & arithmetic / coding & false collapses & first at step & max.\\ deviation\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_float.tex", body)
sw = F["sweep"]
ea = sw["earliest_false_death"]["affine"]
sweep_tab = ("\\begin{tabular}{lrr}\n\\toprule\ncoding (float64) & sets with a false collapse & earliest step\\\\\n\\midrule\n"
             + "$-0.5+0.2\\langle u,\\theta\\rangle$ & %d & %s\\\\\n" % (sw["sets_with_false_death"]["affine"], ea if ea is not None else "--")
             + "$(2\\langle u,\\theta\\rangle-5)/10$ & %s & %s\\\\\n" % (num(sw["sets_with_false_death"]["ratio"]), sw["earliest_false_death"]["ratio"])
             + "\\bottomrule\n\\end{tabular}")
write("tab_float_sweep.tex", sweep_tab)

# ---------------- lean
rows = []
for name, d in R["lean"]["modules"].items():
    rows.append(f"\\texttt{{{name.replace('_', '\\_')}}} & {d['theorems']} & {d['sorry']}\\\\")
rows.append(f"\\textbf{{total}} & {R['lean']['total_theorems']} & {R['lean']['total_sorry']}\\\\")
body = ("\\begin{tabular}{lrr}\n\\toprule\nmodule & theorem declarations & \\texttt{sorry}\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_lean.tex", body)
names_all = []
for name, d in R["lean"]["modules"].items():
    names_all.append("\\textbf{" + name.replace("_", "\\_") + "}: " + ", ".join("\\texttt{" + n.replace("_", "\\_\\allowbreak{}") + "}" for n in d["names"]) + ".")
write("tab_lean_names.tex", "\\footnotesize\n" + "\n\n".join(names_all))

# ---------------- drift table (SI)
rows = []
for m, d in R["cube"].items():
    dr = " & ".join(str(d["drift_by_distance"][str(h)]) if str(h) in d["drift_by_distance"] else "" for h in range(9))
    rows.append(f"{m} & {dr} & {d['rstar']} & {d['ball_size']} & {d['pair_distance_bound']} & {d['kleitman']} & {d['first_split_cost']}\\\\")
body = ("\\begin{tabular}{r" + "r" * 9 + "|rrrrr}\n\\toprule\n$m$ & $h{=}0$ & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & $r^\\ast$ & ball & $\\delta_m$ & $K(m)$ & $2m+5$\\\\\n\\midrule\n"
        + "\n".join(rows) + "\n\\bottomrule\n\\end{tabular}")
write("tab_cube.tex", body)


# ---------------------------------------------------------------- check list from the verification output (longtable)
import re, os
out_path = root / "paper05_exact_belief_computation_v20_verification_output.txt"
rows = []
if out_path.exists():
    for line in open(out_path):
        m = re.match(r"(PASS|FAIL) (\S+) (.*)", line.rstrip())
        if not m:
            continue
        status, cid, text = m.groups()
        text = text.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%").replace("_", r"\_").replace("#", r"\#").replace("{", r"\{").replace("}", r"\}").replace("^", r"\^{}").replace("<", "$<$").replace(">", "$>$").replace("|", "$|$").replace("~", r"\textasciitilde{}")
        rows.append(f"{cid} & {text} & {status}\\\\")
body = ("\\begin{longtable}{@{}l p{0.80\\textwidth} l@{}}\n"
        "\\caption{Verification checks of the full run (identifier, statement, result). Items marked [full] are recomputed only in the full mode and read from the record in \\texttt{--quick} mode.}\\label{tab:S8checks}\\\\\n"
        "\\toprule id & check & result\\\\ \\midrule\n\\endfirsthead\n"
        "\\toprule id & check (continued) & result\\\\ \\midrule\n\\endhead\n"
        "\\bottomrule\n\\endfoot\n" + "\n".join(rows) + "\n\\end{longtable}")
write("tab_checks.tex", body)
print("tables written:", len(rows), "checks")
