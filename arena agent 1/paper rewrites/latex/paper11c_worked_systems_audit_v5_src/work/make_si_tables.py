#!/usr/bin/env python3
"""Generate every LaTeX table (main text and supplement) from results.json."""
import json, os, pathlib, re, collections
root = pathlib.Path(__file__).resolve().parent.parent
R = json.load(open(root / 'work' / 'results.json'))
OUT = root / 'si_parts'
OUT.mkdir(exist_ok=True)


def w(name, body):
    (OUT / name).write_text(body if body.endswith('\n') else body + '\n')
    print('wrote', name)


def st(s):
    """state/belief label -> \\st{..} with | separators"""
    return '$\\st{' + s.replace('|', '|') + '}$'


def fr(s):
    s = str(s)
    if '/' in s:
        n, d = s.split('/')
        sign = '-' if n.startswith('-') else ''
        return f"${sign}\\tfrac{{{n.lstrip('-')}}}{{{d}}}$"
    return f"${s}$"


def mark(b):
    return '$\\bullet$' if b else '$\\cdot$'


K = R['kernels']
CL = [('full', 'full', '$\\ofull$', '$\\free$'), ('codex', 'codex', '$\\ofull$', '$\\nr$'),
      ('agg', 'aggregate', '$\\oagg$', '$\\free$'), ('inst', 'institutional', '$\\oagg$', '$\\nr$')]

# ---------------------------------------------------------------- main: kernels
rows = []
for key, name, o, p in CL:
    a, b, c = K['audited'][key], K['branch'][key], K['optimistic'][key]
    mx = collections.Counter(len(m.split('|')) for m in a['maximal'])
    mxs = ', '.join(f"{v}$\\times${k}" for k, v in sorted(mx.items(), reverse=True))
    if p == '$\\free$':
        rows.append(f"{name} & {o} & {p} & {a['pairs']} & {a['universe']} & \\multicolumn{{2}}{{c}}{{(same)}} & \\multicolumn{{2}}{{c}}{{(same)}} & {mxs} \\\\")
    else:
        bmx = collections.Counter(len(m.split('|')) for m in b['maximal'])
        rows.append(f"{name} & {o} & {p} & {a['pairs']} & {a['universe']} & {b['pairs']} & {b['universe']} & {c['pairs']} & {c['universe']} & {mxs} \\\\")
bl = R['blind']
rows.append(f"blind & $\\oblind$ & $\\free$ & {bl['pairs']} & {bl['size']} & \\multicolumn{{2}}{{c}}{{(same)}} & \\multicolumn{{2}}{{c}}{{(same)}} & 2$\\times$6 \\\\")
d = R['decentralised']
dmx = collections.Counter(len(m.split('|')) for m in d['maximal'])
rows.append(f"decentralised & --- & unanimity & {d['pairs']} & {d['universe']} & \\multicolumn{{2}}{{c}}{{---}} & \\multicolumn{{2}}{{c}}{{---}} & {', '.join(f'{v}$\\times${k}' for k, v in sorted(dmx.items(), reverse=True))} \\\\")
body = r"""\begin{table}[t]
\centering\small
\caption{Kernel census. For each class: viable pairs among the $36$ pairs of safe states and viable beliefs among the $255$ nonempty subsets of the eight viable states, under the shared ledger ($\led$), the private register ($\priv$) and the optimistic ledger ($\opt$); the last column counts the inclusion-maximal viable beliefs under the shared ledger by size (count$\times$size). The free-protocol classes do not involve a register. The blind row is the one-cell observation; the decentralised row is Section~\ref{sec:dec}.}
\label{tab:kernels}
\begin{tabular}{llccccccccl}
\toprule
 & & & \multicolumn{2}{c}{$\led$} & \multicolumn{2}{c}{$\priv$} & \multicolumn{2}{c}{$\opt$} & maximal \\
\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}
class & $o$ & $P$ & pairs & beliefs & pairs & beliefs & pairs & beliefs & beliefs \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_kernels_main.tex', body)

# ---------------------------------------------------------------- main: design by cells
D = R['design']
rows = []
for k, v in D['by_cells'].items():
    rows.append(f"{k} & {v['partitions']} & {v['adequate']} & {v['min_kernel']} & {v['max_kernel']} & {v['min_pairs']}--{v['max_pairs']} \\\\")
body = r"""\begin{table}[t]
\centering\small
\caption{The monitoring-design census by number of cells: partitions of the eight viable states, dynamically adequate partitions (kernel $255$), smallest and largest kernel, and range of the pair kernels (out of $28$).}
\label{tab:design}
\begin{tabular}{rrrrrc}
\toprule
cells & partitions & adequate & min kernel & max kernel & pair kernels \\
\midrule
""" + '\n'.join(rows) + f"""
\\midrule
all & {D['partitions']} & {D['adequate']} & {D['min_kernel']} & 255 & 24--28 \\\\
\\bottomrule
\\end{{tabular}}
\\end{{table}}
"""
w('tab_design_main.tex', body)

# ---------------------------------------------------------------- SI: master table
rows = []
for m in R['master']:
    rows.append(f"{st(m['pair'])} & {mark(m['inst'])} & {mark(m['agg'])} & {mark(m['codex'])} & {mark(m['full'])} & {mark(m['b_inst'])} & {mark(m['b_codex'])} & {mark(m['o_codex'])} & {mark(m['pair'] in d['pairs_list'])} \\\\")
half = len(rows) // 2
body = r"""\begin{table}[H]
\centering\footnotesize
\caption{Master table: the $36$ pairs of safe states and their membership ($\bullet$) in the kernels. Columns: institutional, aggregate, codex and full under the shared ledger; institutional and codex under the private register ($\priv$); codex under the optimistic ledger ($\opt$); decentralised unanimity. Pairs through the corner $\st{11}$ are in no kernel.}
\label{tab:master}
\begin{tabular}{lcccccccc}
\toprule
pair & inst & agg & codex & full & inst$^{\priv}$ & codex$^{\priv}$ & codex$^{\opt}$ & dec \\
\midrule
""" + '\n'.join(rows[:half]) + r"""
\bottomrule
\end{tabular}\hfill
\begin{tabular}{lcccccccc}
\toprule
pair & inst & agg & codex & full & inst$^{\priv}$ & codex$^{\priv}$ & codex$^{\opt}$ & dec \\
\midrule
""" + '\n'.join(rows[half:]) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
body = body.replace('\\end{tabular}\\hfill', '\\end{tabular}\\quad')
w('tab_master.tex', body)

# ---------------------------------------------------------------- SI: universe census by size
sizes = [str(s) for s in range(1, 9)]
rows = []
for conv, cname in [('audited', '$\\led$'), ('branch', '$\\priv$'), ('optimistic', '$\\opt$')]:
    for key, name, o, p in CL:
        if p == '$\\free$' and conv != 'audited':
            continue
        v = K[conv][key]
        cells = [str(v['by_size'].get(s, 0)) for s in sizes]
        label = name if p == '$\\free$' else f"{name} ({cname})"
        hist = v['history_universe']
        rows.append(f"{label} & " + ' & '.join(cells) + f" & {v['universe']} & {len(hist) - 2} \\\\")
cells = [str(d['by_size'].get(s, 0)) for s in sizes]
rows.append("decentralised & " + ' & '.join(cells) + f" & {d['universe']} & --- \\\\")
cells_blind = collections.Counter()
body = r"""\begin{table}[H]
\centering\small
\caption{Viable beliefs by size for each class and convention (columns $1$--$8$ are belief sizes), with the total and the number $h^{\ast}$ of applications of $\Phi$ after which the horizon family on the whole node set is stationary ($\calK=\calW_{h^{\ast}}$).}
\label{tab:universe}
\begin{tabular}{lrrrrrrrrrr}
\toprule
class & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & total & $h^{\ast}$ \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_universe.tex', body)

# ---------------------------------------------------------------- SI: maximal beliefs
rows = []
for conv, cname in [('audited', '$\\led$'), ('branch', '$\\priv$'), ('optimistic', '$\\opt$')]:
    for key, name, o, p in CL:
        if p == '$\\free$' and conv != 'audited':
            continue
        v = K[conv][key]
        label = name if p == '$\\free$' else f"{name} ({cname})"
        rows.append(f"{label} & " + ', '.join(st(m) for m in v['maximal']) + " \\\\")
rows.append("blind & " + ', '.join(st(m) for m in bl['maximal']) + " \\\\")
rows.append("decentralised & " + ', '.join(st(m) for m in d['maximal']) + " \\\\")
body = r"""\begin{table}[H]
\centering\footnotesize
\caption{Inclusion-maximal viable beliefs (the antichains that generate the kernels by sub-belief closure).}
\label{tab:maximal}
\begin{tabular}{lp{0.78\textwidth}}
\toprule
class & maximal beliefs \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_maximal.tex', body)

# ---------------------------------------------------------------- SI: stationary
S = R['stationary']
body = r"""\begin{table}[H]
\centering\small
\caption{Stationary-policy unions: number of deterministic policies, number of beliefs (of $255$) sustained by at least one of them, and the largest number of states sustained by a single policy.}
\label{tab:stationary}
\begin{tabular}{llrrr}
\toprule
observation & policy class & policies & beliefs & max states \\
\midrule
""" + f"""$\\oagg$ & memoryless, $\\oagg(V)\\to A$ & {S['agg_memoryless']['policies']} & {S['agg_memoryless']['union']} & {S['agg_memoryless']['max_states']} \\\\
$\\oagg$ & one period of instrument memory & {S['agg_memory1']['policies']} & {S['agg_memory1']['union']} & {S['agg_memory1']['max_states']} \\\\
$\\oagg$ & alternation (first instrument per cell) & {S['agg_alternation']['policies']} & {S['agg_alternation']['union']} & {S['agg_alternation']['max_states']} \\\\
$\\ofull$ & memoryless, $V\\to A$ & {S['full_memoryless']['policies']} & {S['full_memoryless']['union']} & {S['full_memoryless']['max_states']} \\\\
""" + r"""\bottomrule
\end{tabular}
\end{table}
"""
w('tab_stationary.tex', body)

# ---------------------------------------------------------------- SI: decentralised
rows = [f"{st(x)} & {n} \\\\" for x, n in d['sustainers'].items()]
body = r"""\begin{table}[H]
\centering\small
\caption{Number of law pairs (of $256$) sustaining each safe state as a singleton.}
\label{tab:sustainers}
\begin{tabular}{lr}
\toprule
state & $|\calS(x)|$ \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_dec_sustainers.tex', body)
rows = []
for a in d['L1']:
    rows.append(f"{a} & " + ' & '.join(f"({a},{b})" for b in d['L2']) + " \\\\")
body = r"""\begin{table}[H]
\centering\small
\caption{The $16$ law pairs sustaining $\st{12|21}$: the product $L_1\times L_2$ (rows $L_1$, columns $L_2$; laws written as the votes at $z=0,1,2,3$).}
\label{tab:laws}
\begin{tabular}{l""" + 'c' * len(d['L2']) + r"""}
\toprule
$l_1\backslash l_2$ & """ + ' & '.join(d['L2']) + r""" \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_dec_laws.tex', body)
rows = []
names = {'agency1_vote1': '$l_1(1)=1$ (owner)', 'agency1_vote2': '$l_1(1)=2$ (against)',
         'agency2_vote1': '$l_2(1)=1$ (against)', 'agency2_vote2': '$l_2(1)=2$ (owner)'}
for k, v in d['authority'].items():
    rows.append(f"{names[k]} & {len(v)} & " + ', '.join(st(x) for x in v) + " \\\\")
for k, v in d['whole_law'].items():
    ag = k[6]; val = k[-1]
    rows.append(f"$l_{ag}\\equiv {val}$ & {v} & --- \\\\")
body = r"""\begin{table}[H]
\centering\footnotesize
\caption{Authority census: the pair kernel when one vote at the floor is fixed, and when a whole law is fixed to a constant.}
\label{tab:authority}
\begin{tabular}{lrp{0.62\textwidth}}
\toprule
restriction & pairs & sustained pairs \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_dec_authority.tex', body)

# ---------------------------------------------------------------- SI: design sizes, coarsest
rows = [f"{k} & {v} \\\\" for k, v in D['kernel_sizes'].items()]
body = r"""\begin{table}[H]
\centering\small
\caption{Distribution of kernel sizes over the $4{,}140$ monitoring partitions ($18$ sizes, $74$ distinct kernels).}
\label{tab:design_sizes}
\begin{tabular}{rr}
\toprule
kernel size & partitions \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_design_sizes.tex', body)
rows = [' $\\mid$ '.join(st(c) for c in P) + ' \\\\' for P in D['coarsest']]
body = r"""\begin{table}[H]
\centering\footnotesize
\caption{The $16$ coarsest (two-cell) dynamically adequate monitoring designs.}
\label{tab:coarsest}
\begin{tabular}{l}
\toprule
design \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_coarsest.tex', body)

# ---------------------------------------------------------------- SI: target census
T = R['target']
rows = []
for P in T['all_list']:
    ad = P in T['adequate_list']
    rows.append(' $\\mid$ '.join(st(c) for c in P) + f" & {len(P)} & {mark(ad)} \\\\")
body = r"""\begin{table}[H]
\centering\small
\caption{The $15$ partitions of the four-state target $\{\st{12},\st{21},\st{22},\st{31}\}$ and their one-step adequacy ($\bullet$: every cell has a common safe instrument).}
\label{tab:target}
\begin{tabular}{lcc}
\toprule
partition & cells & adequate \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_target.tex', body)

# ---------------------------------------------------------------- SI: timing grid
tg = R['timing']
rows = []
for z, sig, row in tg['rows']:
    zz = z if '/' not in z else None
    from fractions import Fraction
    zf = Fraction(z)
    rows.append(f"{float(zf):.1f} & {sig} & " + ' & '.join(f"{mark(a)} & {mark(b)}" for a, b in row) + " \\\\")
body = r"""\begin{table}[H]
\centering\footnotesize
\caption{The $93$-cell timing grid: for each initial level $z_0$ (slack $z_0-1$, integer count $\lfloor z_0-1\rfloor$) and review period $T$, viability under free switching with unit damage (f) and under alternation with damages $(1,\tfrac12)$ (a).}
\label{tab:timing}
\begin{tabular}{rrcccccc}
\toprule
$z_0$ & $\lfloor z_0-1\rfloor$ & $T{=}1$ f & a & $T{=}2$ f & a & $T{=}3$ f & a \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_timing.tex', body)

# ---------------------------------------------------------------- SI: benchmark, drift
B = R['benchmark']
rows = []
for r in B['rows']:
    status = 'feasible' if r['feasible'] else f"obstructed, margin {fr(r['margin'])}"
    rows.append(f"{fr(r['Y'])} & {fr(r['c1'])} & {fr(r['c2'])} & {fr(r['sum'])} & {status} \\\\")
body = r"""\begin{table}[H]
\centering\small
\caption{The benchmark fibre: caps, cap sum and status against the demand $u_1+u_2\ge 2$; the margin is the dual-weighted deficiency $\mu(Y)=(Y-27/5)/10$ at $\lambda=(\tfrac12,\tfrac12)$.}
\label{tab:bench}
\begin{tabular}{lllll}
\toprule
$Y$ & $c_1(Y)$ & $c_2(Y)$ & $c_1+c_2$ & status \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_bench.tex', body)
Dr = R['drift']
rows = [f"{fr(r['s'])} & {fr(r['naive'])} & {fr(r['corrected'])} \\\\" for r in Dr['rows']]
body = r"""\begin{table}[H]
\centering\small
\caption{Certainty-equivalent drift under $g(s)=s^2$ with lead $\tfrac1{10}$: naive drift $s/5+1/100$ and corrected drift.}
\label{tab:drift}
\begin{tabular}{lll}
\toprule
$s$ & naive drift & corrected drift \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_drift.tex', body)

# ---------------------------------------------------------------- SI: family
F = R['family']
rows = []
for cap, v in F.items():
    rows.append(f"{cap} & {v['safe']} & {v['pairs']} & {v['inst']} & {v['agg']} & {v['codex']} & {v['full']} & {v['b_inst']} & {v['b_codex']} & {v['corner_free_pairs']} \\\\")
body = r"""\begin{table}[H]
\centering\small
\caption{Scaling of the pair census to larger caps: safe states, pairs of safe states, pair kernels of the four classes under the shared ledger, the institutional and codex pair kernels under the private register, and the number of corner-free pairs (which equals the full kernel in every case).}
\label{tab:family}
\begin{tabular}{rrrrrrrrrr}
\toprule
cap & safe & pairs & inst & agg & codex & full & inst$^{\priv}$ & codex$^{\priv}$ & corner-free \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_family.tex', body)

# ---------------------------------------------------------------- SI: checks (from verifier output if present)
out = root / 'paper11c_worked_systems_audit_v5_verification_output.txt'
if out.exists():
    lines = [l.rstrip() for l in out.read_text().splitlines() if l.startswith('PASS') or l.startswith('FAIL')]
    rows = []
    for l in lines:
        status, rest = l.split(' ', 1)
        rest = rest.replace('\\', '\\textbackslash{}').replace('_', '\\_').replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('{', '\\{').replace('}', '\\}').replace('^', '\\^{}').replace('~', '\\~{}').replace('<', '$<$').replace('>', '$>$').replace('|', '$|$')
        rows.append(f"{status} & {rest} \\\\")
    body = r"""\begin{longtable}{lp{0.86\textwidth}}
\caption{The named checks of the verifier and their status in the shipped run.}\label{tab:checks}\\
\toprule
status & check \\
\midrule
\endfirsthead
\toprule
status & check \\
\midrule
\endhead
\bottomrule
\endfoot
""" + '\n'.join(rows) + "\n\\end{longtable}\n"
    w('tab_checks.tex', body)

# ---------------------------------------------------------------- SI: lean names
lean_dir = root / 'src' / 'lean'
rows = []
for f in sorted(lean_dir.glob('*.lean')):
    for m in re.finditer(r'^(theorem|lemma|def)\s+([A-Za-z0-9_\'.]+)', f.read_text(), re.M):
        rows.append(f"\\texttt{{{f.name.replace('_', '\\_')}}} & {m.group(1)} & \\texttt{{{m.group(2).replace('_', '\\_')}}} \\\\")
body = r"""\begin{table}[H]
\centering\small
\caption{Declarations of the Lean modules shipped with the article.}
\label{tab:lean}
\begin{tabular}{lll}
\toprule
module & kind & name \\
\midrule
""" + '\n'.join(rows) + r"""
\bottomrule
\end{tabular}
\end{table}
"""
w('tab_lean.tex', body)
