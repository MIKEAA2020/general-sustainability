#!/usr/bin/env python3
"""Generate the SI table bodies from results.json, p04_core and the verification output."""
import os, sys, json, re
from fractions import Fraction as Q
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import p04_core as C
RES = json.load(open(os.path.join(HERE, "results.json")))
SI = os.path.join(ROOT, "si_parts")
os.makedirs(SI, exist_ok=True)


def sa(u):
    """signed action"""
    return "0" if int(u) == 0 else f"{int(u):+d}"


def tf(x):
    """TeX fraction"""
    q = Q(x)
    if q.denominator == 1:
        return str(q.numerator)
    sign = "-" if q < 0 else ""
    return r"%s\tfrac{%d}{%d}" % (sign, abs(q.numerator), q.denominator)


def write(name, body):
    with open(os.path.join(SI, name), "w") as f:
        f.write(body if body.endswith("\n") else body + "\n")


# ---------------------------------------------------------------- Helly study
H = RES["helly"]
rows = []
for key in ("k1", "k2", "k3", "k3_rank1", "k4"):
    if key not in H:
        continue
    h = H[key]
    hist = h["hist"]
    cells = [hist.get(str(s), "0") for s in range(1, 6)]
    label = f"$k={h['k']}$" + (" (rank-one)" if "rank1" in key else "")
    rows.append(f"{label} & {h['m']} & {h['n']} & {h['infeasible']} & " + " & ".join(str(c) for c in cells) + f" & {'float screen + exact' if h['fast'] else 'exact'}\\\\")
write("tab_helly.tex", "\n".join(rows))

# ---------------------------------------------------------------- z0 sweep with couplings
sw = RES["two_window"]["sweep"]
scen = [tuple(w) for w in RES["two_window"]["scenarios"]]
rows = []
for z in sorted(sw, key=int):
    r = sw[z]
    mu = r.get("mu_star")
    if mu:
        supp = sum(1 for v in mu.values() if Q(v) != 0)
        uniform = all(Q(v) == Q(1, 8) for v in mu.values())
        mu_txt = "product prior" if uniform else f"{supp} paths"
    else:
        mu_txt = "--"
    rows.append(f"${z}$ & ${tf(r['Q0'])}$ & ${tf(r['openloop'])}$ & ${tf(r['Rplus'])}$ & ${tf(r['Rminus'])}$ & ${tf(Q(r['Q0'])-Q(r['openloop']))}$ & {mu_txt} & {r.get('w_star_size','--')}\\\\")
write("tab_sweep.tex", "\n".join(rows))

# coupling vertices
verts = RES["two_window"]["coupling_vertices"]
hdr = " & ".join("$(%s)$" % ",".join(("+" if x > 0 else "-") for x in w) for w in scen)
rows = [r"vertex & " + hdr + r"\\ \midrule"]
for i, v in enumerate(verts, 1):
    rows.append(f"$\\mu^{{({i})}}$ & " + " & ".join(f"${tf(x)}$" for x in v) + r"\\")
write("tab_vertices.tex", "\n".join(rows))

# ---------------------------------------------------------------- two-window tree: all first actions
P = C.two_window()
rows = []
for a in (-2, 0, 2):
    members = P.cell(0, (), ("blind",))
    labs = sorted({P.obs(1, w, (a,)) for w, _ in members})
    for z1 in labs:
        v, arg, per = P.node_value(1, (a,), ("blind", z1))
        # which s are compatible
        ss = sorted({w[0] for w, _ in members if P.obs(1, w, (a,)) == z1})
        mass = sum(p for w, p in members if P.obs(1, w, (a,)) == z1)
        rows.append(f"${sa(a)}$ & ${tf(z1)}$ & {', '.join(f'${s:+d}$' for s in ss)} & ${tf(mass)}$ & " +
                    ", ".join(f"${tf(per[u])}$" for u in (-2, 0, 2)) + f" & {', '.join(f'${sa(u)}$' for u in arg)} & ${tf(v)}$\\\\")
write("tab_tree.tex", "\n".join(rows))

# ---------------------------------------------------------------- instance counts
M = RES["matching"]
rows = [
    r"two-window ($z_0=2$) & $\{\pm1\}^3$, product & 2 & 3, 3 & blind; $z_1$ & 171 & $\tfrac12$ & $\tfrac12$ (8 trees)\\",
    r"A & $\{\pm1\}^3$, uniform & 3 & 2, 2, 2 & $\operatorname{sign}d_1$; $(d_1,d_2)$; $d$ & 16384 & 0 & 0\\",
    r"B & $\{\pm1\}^2$, uniform & 2 & 3, 3 & blind; $d$ & 243 & 1 & 1\\",
    r"C coarse & $\{\pm1\}^3$, uniform & 2 & 2, 2 & $\operatorname{sign}d_1$; $d$ & 1024 & $\tfrac12$ & $\tfrac12$\\",
    r"C fine & $\{\pm1\}^3$, uniform & 2 & 2, 2 & $(d_1,d_2)$; $d$ & 4096 & $\tfrac34$ & $\tfrac34$\\",
    r"posterior-only & $\{0,1\}$, uniform & 2 & 2, 1 & blind; $s$ & 2 & $\tfrac12$ & $\tfrac12$\\",
]
write("tab_instances.tex", "\n".join(rows))
import ast
rows = []
for part, v in M.items():
    blocks = ast.literal_eval(part)
    lab = "$" + "\\,|\\,".join("\\{" + ",".join(str(x) for x in b) + "\\}" for b in blocks) + "$"
    rows.append(f"{lab} & ${tf(v)}$\\\\")
write("tab_matching.tex", "\n".join(rows))

# ---------------------------------------------------------------- check list from the verification output
out_path = os.path.join(ROOT, "paper04_minimax_dual_certificates_v20_verification_output.txt")
rows = []
if os.path.exists(out_path):
    for line in open(out_path):
        m = re.match(r"(PASS|FAIL) (\S+) (.*)", line.rstrip())
        if not m:
            continue
        status, cid, text = m.groups()
        text = text.replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%").replace("_", r"\_").replace("#", r"\#").replace("{", r"\{").replace("}", r"\}").replace("^", r"\^{}").replace("<", "$<$").replace(">", "$>$").replace("|", "$|$").replace("~", r"\textasciitilde{}")
        rows.append(f"{cid} & {text} & {status}\\\\")
write("tab_checks.tex", "\n".join(rows))
print("tables written:", len(rows), "checks")

# ---------------------------------------------------------------- benchmark table
U = C.bench_U()
rows = []
status = {Q(4): "viable", Q(5): r"viable; $(\tfrac65,\tfrac45)$ also safe", Q(27, 5): "boundary", Q(6): r"obstructed, certificate $(\tfrac12,\tfrac12)$", Q(69, 5): "corner 2 at its cap"}
for Y in (Q(4), Q(5), Q(27, 5), Q(6), Q(69, 5)):
    c1, c2 = C.bench_caps(Y)
    val, arg = C.lower_value(C.bench_rows(Y), U)
    argtxt = f"$({tf(arg[0])},{tf(arg[1])})$" if val >= 0 else "--"
    rows.append(f"${tf(Y)}$ & ${tf(c1)}$ & ${tf(c2)}$ & ${tf(c1 + c2)}$ & ${tf(val)}$ & {argtxt} & {status[Y]}\\\\")
write("tab_bench.tex", "\n".join(rows))
rows = []
for D, note in ((Q(0), r"physical: $\operatorname{cap}_2=0$ at corner 2"), (Q(8, 25), "both regimes meet"), (Q(1, 2), "epistemic + institutional"),
                (Q(1), "epistemic + institutional"), (Q(2), "epistemic + institutional (main text)"), (Q(57, 25), "last viable fibre is the corner fibre $Y=4$")):
    lin = Q(77, 5) - 5 * D
    Ys = min(lin, Q(69, 5))
    rows.append(f"${tf(D)}$ & ${tf(lin)}$ & ${tf(Ys)}$ & {note}\\\\")
rows.append(r"$>\tfrac{57}{25}$ & $<4$ & none & every fibre obstructed\\")
write("tab_floor.tex", "\n".join(rows))
print("benchmark tables written")

# ---------------------------------------------------------------- two-patch codex
rows = []
K2 = C.patch_kernel((0, 1))
for x in sorted(y for y in C.patch_states() if C.patch_safe(y)):
    s0, s1 = C.patch_step(x, 0), C.patch_step(x, 1)
    safe = C.patch_safe_actions(x)
    rows.append(f"$({x[0]},{x[1]})$ & $({s0[0]},{s0[1]})$ & $({s1[0]},{s1[1]})$ & {', '.join('spare %d' % (u + 1) for u in sorted(safe)) or 'none'} & {'yes' if x in K2 else 'no'}\\\\")
write("tab_patch.tex", "\n".join(rows))
print("patch table written")
