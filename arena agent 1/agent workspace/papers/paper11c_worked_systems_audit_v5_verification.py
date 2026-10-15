#!/usr/bin/env python3
"""
Verifier for paper11c v5 (worked systems audit).

Recomputes every audited object from work/ws_core.py and evaluates named
Boolean checks; then (if the compiled PDFs are present) confirms that the
numbers quoted in the manuscript and the supplement match.  Exit status 1
on any failure.  `--quick` reuses the stored design census (work/results.json)
instead of recomputing the 4,140 kernels.
"""
import sys, os, json, time, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
# the exact core lives in work/ (edition folder) or in the shipped source folder
SRC = HERE if os.path.isdir(os.path.join(HERE, 'work')) else os.path.join(HERE, 'paper11c_worked_systems_audit_v5_src')
sys.path.insert(0, os.path.join(SRC, 'work'))
from fractions import Fraction as Q
from ws_core import *  # noqa

QUICK = '--quick' in sys.argv
NCHECKS_EXPECTED = 64   # quoted in the manuscript (\\NCHECKS); X2 fails if the count drifts
T0 = time.time()
LINES = []
NPASS = NFAIL = 0


def check(name, cond):
    global NPASS, NFAIL
    ok = bool(cond)
    NPASS += ok
    NFAIL += (not ok)
    line = ('PASS ' if ok else 'FAIL ') + name
    LINES.append(line)
    print(line, flush=True)


def lab(B):
    return blabel(B)


def labs(fam):
    return sorted(blabel(B) for B in fam)


# ------------------------------------------------------------------ 1. system
check("S1 state grid 16 states, 9 safe, corner 11 has no safe instrument, eight other safe states have R as in eq. (R)",
      len(STATES) == 16 and len(SAFE) == 9 and safe_actions(CORNER) == []
      and {label(x): tuple(safe_actions(x)) for x in CORNER_FREE} ==
      {'12': (1,), '13': (1,), '21': (2,), '31': (2,), '22': (1, 2), '23': (1, 2), '32': (1, 2), '33': (1, 2)})
check("S2 aggregate z1+z2 is non-increasing under instruments 1 and 2 on all safe states (and falls only when the raised stock is at its cap)",
      all(sum(SYS['step'](x, u)) <= sum(x) for x in SAFE for u in (1, 2))
      and all((sum(SYS['step'](x, u)) < sum(x)) == (x[u - 1] == 3) for x in SAFE for u in (1, 2)))
check("S3 36 pairs of safe states, 28 corner-free; 511 nonempty beliefs of safe states, 255 of viable states",
      len(PAIRS) == 36 and sum(1 for B in PAIRS if CORNER not in B) == 28 and len(UNIVERSE) == 511
      and len(all_beliefs(CORNER_FREE)) == 255)

# ------------------------------------------------------------------ 2. kernels
KA = class_kernels(None, PAIRS)
KU = class_kernels(None, UNIVERSE)
KB = class_kernels('branch', UNIVERSE)
KBp = class_kernels('branch', PAIRS)
KO = class_kernels('optimistic', UNIVERSE)
KOp = class_kernels('optimistic', PAIRS)
A = {k: KA[k]['kernel'] for k in KA}
AU = {k: KU[k]['kernel'] for k in KU}
BU = {k: KB[k]['kernel'] for k in KB}
OU = {k: KO[k]['kernel'] for k in KO}
check("K1 shared-ledger pair kernels (inst, agg, codex, full) = (24, 26, 25, 28)",
      tuple(KA[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (24, 26, 25, 28))
check("K2 shared-ledger belief kernels on the 511 beliefs = (111, 143, 119, 255), all contained in the corner-free beliefs",
      tuple(KU[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (111, 143, 119, 255)
      and all(CORNER not in B for k in AU for B in AU[k]))
check("K3 full kernel = all nonempty subsets of the eight viable states; on pairs = the 28 corner-free pairs",
      AU['full'] == frozenset(all_beliefs(CORNER_FREE)) and A['full'] == frozenset(B for B in PAIRS if CORNER not in B))
check("K4 monotonicity inclusions inst <= agg <= full and inst <= codex <= full hold on all beliefs and all are strict",
      AU['inst'] < AU['agg'] < AU['full'] and AU['inst'] < AU['codex'] < AU['full'])
check("K5 aggregate and codex kernels incomparable; witnesses 12|31, 13|21 in agg \\ codex and 13|31 in codex \\ agg",
      not (AU['agg'] <= AU['codex']) and not (AU['codex'] <= AU['agg'])
      and labs(A['agg'] - A['codex']) == ['12|31', '13|21'] and labs(A['codex'] - A['agg']) == ['13|31'])
check("K6 meet of the middle classes is the institutional kernel on pairs and on all beliefs",
      (A['agg'] & A['codex']) == A['inst'] and (AU['agg'] & AU['codex']) == AU['inst'])
D = AU['full'] - (AU['agg'] | AU['codex'])
c1221 = frozenset({(1, 2), (2, 1)}); c1331 = frozenset({(1, 3), (3, 1)})
check("K7 join of the middle classes misses the full kernel by exactly 12|21 on pairs and by 104 beliefs (64 containing 12|21, the rest containing 13|31 plus one of 12, 21, 22); minimal members 12|21, 12|13|31, 13|21|31, 13|22|31",
      labs(A['full'] - (A['agg'] | A['codex'])) == ['12|21'] and len(D) == 104
      and sum(1 for B in D if c1221 <= B) == 64
      and all(c1221 <= B or (c1331 <= B and B & {(1, 2), (2, 1), (2, 2)}) for B in D)
      and labs(B for B in D if not any(C < B for C in D)) == ['12|13|31', '12|21', '13|21|31', '13|22|31'])
check("K8 every kernel (all classes, all conventions) is closed under nonempty sub-beliefs",
      all(is_downset(K) for K in list(AU.values()) + list(BU.values()) + list(OU.values())))
check("K9 maximal beliefs: inst 2x6, agg 4x6, codex 2x6+1x5, full 1x8 (shared ledger)",
      [sorted(len(m) for m in maximal_sets(AU[k])) for k in ('inst', 'agg', 'codex', 'full')] ==
      [[6, 6], [6, 6, 6, 6], [5, 6, 6], [8]])
check("K10 horizon family on the whole node set stabilises after one application for the free classes and two for the ledger classes",
      [len(KU[k]['history']) - 2 for k in ('inst', 'agg', 'codex', 'full')] == [2, 1, 2, 1])
check("K11 pair kernels are the size-2 members of the belief kernels (consistency of the two populations)",
      all(A[k] == frozenset(B for B in AU[k] if len(B) == 2) for k in A))
check("K12 admitting the idle instrument 0 leaves all four shared-ledger kernels unchanged",
      all(class_kernels(None, UNIVERSE, actions=(0, 1, 2))[k]['kernel'] == AU[k] for k in AU))

# ------------------------------------------------------------------ 3. alternation and closed forms
PH = {a: frozenset(x for x in SAFE if alternation_safe(x, a)) for a in (1, 2)}
check("A1 alternation-safe sets Phi_1 = {12,13,22,23,32,33}, Phi_2 = {21,22,23,31,32,33}; union = viable states, intersection = {22,23,32,33}",
      labs([PH[1]]) == ['12|13|22|23|32|33'] and labs([PH[2]]) == ['21|22|23|31|32|33']
      and PH[1] | PH[2] == frozenset(CORNER_FREE) and labs([PH[1] & PH[2]]) == ['22|23|32|33'])
check("A2 every alternating trajectory in Phi_a is 2-periodic after at most one step",
      all(alternation_trajectory(x, a, 6)[1] == alternation_trajectory(x, a, 6)[3] == alternation_trajectory(x, a, 6)[5]
          for a in (1, 2) for x in PH[a]))
check("A3 shared-ledger closed form reproduces the institutional and codex kernels on all 511 beliefs",
      ledger_kernel_closed_form(UNIVERSE, obs_agg) == AU['inst'] and ledger_kernel_closed_form(UNIVERSE, obs_full) == AU['codex'])
check("A4 private-register closed form (phase coherence) reproduces the private institutional and codex kernels on all 511 beliefs",
      branch_kernel_closed_form(UNIVERSE, obs_agg) == BU['inst'] and branch_kernel_closed_form(UNIVERSE, obs_full) == BU['codex'])
Wb, hb = kernel_free_bitmask([list(CORNER_FREE)])
blind = frozenset(mask_to_set(m) for m in Wb)
check("A5 blind kernel = (2^Phi_1 U 2^Phi_2) minus empty, 111 beliefs, equal to the shared-ledger institutional kernel",
      blind == (frozenset(all_beliefs(sorted(PH[1]))) | frozenset(all_beliefs(sorted(PH[2])))) and len(blind) == 111 and blind == AU['inst'])
check("A6 codex minus institutional (shared ledger) = the 8 beliefs {13,31} U S, S subset of {23,32,33}",
      AU['codex'] - AU['inst'] == frozenset(c1331 | S for S in [frozenset()] + all_beliefs([(2, 3), (3, 2), (3, 3)])))
check("A7 private-register kernels (inst, agg, codex, full) = (143, 143, 191, 255) on beliefs and (26, 26, 27, 28) on pairs; private institutional = aggregate setwise",
      tuple(KB[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (143, 143, 191, 255)
      and tuple(KBp[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (26, 26, 27, 28)
      and BU['inst'] == AU['agg'])
check("A8 shared ledger and private register incomparable at full observation: 13|31 ledger-viable and private-dead, 12|21 the reverse",
      c1331 in AU['codex'] and c1331 not in BU['codex'] and c1221 in BU['codex'] and c1221 not in AU['codex'])
check("A9 optimistic-ledger kernels = (127, 143, 191, 255) on beliefs, (26, 26, 27, 28) on pairs; contain the shared-ledger kernels; optimistic codex differs setwise from private codex",
      tuple(KO[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (127, 143, 191, 255)
      and tuple(KOp[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (26, 26, 27, 28)
      and all(AU[k] <= OU[k] for k in AU) and OU['codex'] != BU['codex'])
KF = class_kernels('first', PAIRS); KL = class_kernels('last', PAIRS)
check("A10 fixed-thread conventions (first / last fibre) give (25, 26, 26, 28) on pairs and disagree with each other setwise",
      tuple(KF[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (25, 26, 26, 28)
      and tuple(KL[k]['size'] for k in ('inst', 'agg', 'codex', 'full')) == (25, 26, 26, 28)
      and KF['inst']['kernel'] != KL['inst']['kernel'])

# ------------------------------------------------------------------ 4. stationary
r0 = stationary_union(obs_agg, memory=False, beliefs=UNIVERSE)
r1 = stationary_union(obs_agg, memory=True, no_repeat=True, beliefs=UNIVERSE)
r2 = stationary_union(obs_full, memory=False, beliefs=UNIVERSE)
check("P1 32 memoryless aggregate policies sustain no state",
      r0['policies'] == 32 and r0['union'] == frozenset() and r0['max_states'] == 0)
check("P2 32 alternation policies realise exactly the aggregate kernel (143 beliefs; four sustained sets of size 6 = the maximal beliefs)",
      r1['policies'] == 32 and r1['union'] == AU['agg'] and labs(r1['sustained'][:4]) == labs(maximal_sets(AU['agg'])))
if not QUICK:
    r3 = stationary_union(obs_agg, memory=True, beliefs=UNIVERSE)
    check("P3 all 32768 one-period-memory aggregate policies realise the same set as the 32 alternation policies",
          r3['policies'] == 32768 and r3['union'] == AU['agg'])
else:
    check("P3 (quick mode) stored result: 32768 memory policies realise the aggregate kernel",
          json.load(open(os.path.join(SRC, 'work', 'results.json')))['stationary']['agg_memory1']['equals_agg_kernel'])
pol = {(1, 2): 1, (1, 3): 1, (2, 3): 1, (3, 3): 1, (2, 1): 2, (2, 2): 2, (3, 1): 2, (3, 2): 2, (1, 1): 1}
check("P4 512 memoryless full-observation policies realise the full kernel; the displayed policy sustains all eight viable states",
      r2['policies'] == 512 and r2['union'] == AU['full'] and all(closed_loop_safe(x, pol, obs_full) for x in CORNER_FREE))

# ------------------------------------------------------------------ 5. decentralised
S = sustainers()
dec_p = decentralised_kernel(PAIRS, S)
dec_u = decentralised_kernel(UNIVERSE, S)
direct = frozenset(B for B in UNIVERSE if any(law_sustains_belief(B, l1, l2) for l1, l2 in LAW_PAIRS))
check("D1 16 laws, 256 law pairs, 64 behavioural classes",
      len(LAWS) == 16 and len(LAW_PAIRS) == 256 and len({(behavioural_class(a), behavioural_class(b)) for a, b in LAW_PAIRS}) == 64)
check("D2 statewise factoring: the factored kernel equals the direct orbit computation on all 511 beliefs",
      dec_u == direct)
check("D3 decentralised kernel: 12 pairs, 30 beliefs (8+12+8+2), maximal beliefs 12|21|23|32 and 13|22|31|33; 16 of 28 coordinated-viable pairs lost; contains 12|21, misses 12|13",
      len(dec_p) == 12 and len(dec_u) == 30 and dict(collections.Counter(len(B) for B in dec_u)) == {1: 8, 2: 12, 3: 8, 4: 2}
      and labs(maximal_sets(dec_u)) == ['12|21|23|32', '13|22|31|33'] and len(A['full'] - dec_p) == 16
      and c1221 in dec_p and frozenset({(1, 2), (1, 3)}) not in dec_p)
check("D4 sustained pairs are exactly the pairs inside the two maximal beliefs (Helly property of the sustainer family on this instance)",
      dec_p == frozenset(frozenset(p) for M in maximal_sets(dec_u) for p in combinations(sorted(M), 2)))
sust = {(law_str(l1), law_str(l2)) for l1, l2 in LAW_PAIRS if law_sustains_belief(c1221, l1, l2)}
L1 = ['1121', '1122', '2121', '2122']; L2 = ['1211', '1212', '2211', '2212']
check("D5 the 16 law pairs sustaining 12|21 form the product L1 x L2 (4 behavioural classes x 4 unconsulted votes)",
      sust == {(a, b) for a in L1 for b in L2} and len(sust) == 16
      and len({(a[1:], b[1:]) for a, b in sust}) == 4)


def auth(agency, vote):
    idx = frozenset(i for i, (l1, l2) in enumerate(LAW_PAIRS) if (l1 if agency == 1 else l2)[1] == vote)
    return decentralised_kernel(PAIRS, {x: S[x] & idx for x in SAFE})


def whole(agency, v):
    idx = frozenset(i for i, (l1, l2) in enumerate(LAW_PAIRS) if all((l1 if agency == 1 else l2)[z] == v for z in range(4)))
    return decentralised_kernel(PAIRS, {x: S[x] & idx for x in SAFE})


swap = lambda B: frozenset((y, x) for x, y in B)
check("D6 authority census: l1(1)=1 and l2(1)=2 leave 12 pairs; l2(1)=1 leaves {13|22,13|33,22|33,23|32}; l1(1)=2 its swap image; constant laws leave 0",
      auth(1, 1) == dec_p and auth(2, 2) == dec_p and labs(auth(2, 1)) == ['13|22', '13|33', '22|33', '23|32']
      and auth(1, 2) == frozenset(swap(B) for B in auth(2, 1))
      and all(len(whole(a, v)) == 0 for a in (1, 2) for v in (1, 2)))
check("D7 fixing l1(1)=1 leaves 16 sustaining pairs for 12|21, fixing l2(1)=1 leaves 0",
      sum(1 for a, b in sust if a[1] == '1') == 16 and sum(1 for a, b in sust if b[1] == '1') == 0)

# ------------------------------------------------------------------ 6. monitoring design
edges = incompatibility_edges(CORNER_FREE)
check("M1 incompatibility graph on the eight viable states = K_{2,2} between {12,13} and {21,31} (4 edges)",
      {(label(a), label(b)) for a, b in edges} == {('12', '21'), ('12', '31'), ('13', '21'), ('13', '31')})
tc = target_census()
check("M2 four-state target: 15 partitions, 7 adequate = 15-(5+5-2); edges 12-21, 12-31; two adequate two-cell partitions; maximal common-action sets 12|22 and 21|22|31",
      tc['n'] == 15 and tc['n_adequate'] == 7 and tc['n_e'] == [5, 5] and tc['n_both'] == 2
      and [(label(a), label(b)) for a, b in tc['edges']] == [('12', '21'), ('12', '31')]
      and len(tc['two_cell']) == 2 and labs(tc['maxcommon']) == ['12|22', '21|22|31'])
check("M3 Helly numbers of the two- and three-instrument universes are 2 and 3",
      tc['helly2'] == 2 and tc['helly3'] == 3)
from math import comb
bell = [1, 1, 2, 5, 15]
formula = sum(comb(4, m) * bell[m] * 2 ** (4 - m) for m in range(5)) + 2 * sum(comb(4, m) * bell[m] * 3 ** (4 - m) for m in range(5)) + sum(comb(4, m) * bell[m] * 4 ** (4 - m) for m in range(5))
if QUICK:
    Rj = json.load(open(os.path.join(SRC, 'work', 'results.json')))['design']
    n_part, n_ad, dyn_eq, n_co, n_dist, minK, n_min, sizes, ledg, ledmax = (Rj['partitions'], Rj['adequate'], Rj['dyn_eq_one'], Rj['n_coarsest'], Rj['distinct_kernels'], Rj['min_kernel'], Rj['n_min_kernel'], len(Rj['kernel_sizes']), Rj['ledger_adequate'], Rj['ledger_max_kernel'])
    minmerge = Rj['min_kernel_all_merge_critical']; maxb = Rj['max_belief_sizes']; prs = Rj['pairs_sizes']; agg_row = Rj['agg_row']
    tag = ' (quick mode: stored census)'
else:
    rows, _ = design_census()
    n_part = len(rows); dyn = [r for r in rows if r['full_viable']]; n_ad = len(dyn)
    dyn_eq = all(r['full_viable'] == r['one_step'] for r in rows)
    n_co = sum(1 for r in dyn if r['ncells'] == 2)
    distinct = set()
    for r in rows:
        W, _ = kernel_free_bitmask(r['cells']); distinct.add(frozenset(W))
    n_dist = len(distinct)
    ks = collections.Counter(r['kernel'] for r in rows); minK = min(ks); n_min = ks[minK]; sizes = len(ks)
    minmerge = all(any({(1, 2), (1, 3), (2, 1), (3, 1)} <= set(c) for c in r['cells']) for r in rows if r['kernel'] == minK)
    maxb = {str(k): v for k, v in collections.Counter(r['max_belief'] for r in rows).items()}
    prs = {str(k): v for k, v in collections.Counter(r['pairs'] for r in rows).items()}
    aggcells = sorted(sorted(c) for c in {s: [x for x in CORNER_FREE if sum(x) == s] for s in range(3, 7)}.values())
    agg_row = next(r for r in rows if r['cells'] == aggcells)
    ledg = 0; ledmax = 0
    for r in rows:
        lb = {x: i for i, c in enumerate(r['cells']) for x in c}
        Kl = ledger_kernel_closed_form(UNIVERSE, lambda x, lb=lb: lb.get(x, -1))
        ledg += (frozenset(CORNER_FREE) in Kl); ledmax = max(ledmax, len(Kl))
    tag = ''
check("M4 design census: 4140 partitions, 1694 dynamically adequate, dynamic adequacy = one-step adequacy on every partition" + tag,
      n_part == 4140 and n_ad == 1694 and dyn_eq)
check("M5 closed-form count 151 + 2*372 + 799 = 1694 agrees with the census" + tag, formula == 1694 == n_ad)
check("M6 16 coarsest (two-cell) adequate designs; 74 distinct kernels; 18 kernel sizes; minimum 111 attained by exactly the 52 partitions merging the four critical states" + tag,
      n_co == 16 and n_dist == 74 and sizes == 18 and minK == 111 and n_min == 52 and minmerge
      and 52 == sum(comb(4, m) * bell[m] for m in range(5)))
check("M7 maximal-belief sizes 6/7/8 for 927/1519/1694 partitions; pair kernels 24/26/27/28 for 52/906/1488/1694; aggregate partition: kernel 143, 4 maximal beliefs, 26 pairs, not one-step adequate" + tag,
      maxb == {'6': 927, '7': 1519, '8': 1694} and prs == {'24': 52, '26': 906, '27': 1488, '28': 1694}
      and agg_row['kernel'] == 143 and agg_row['n_max'] == 4 and agg_row['pairs'] == 26 and not agg_row['one_step'])
check("M8 under the shared ledger no partition is adequate and the largest kernel over all partitions is 119" + tag,
      ledg == 0 and ledmax == 119)

# ------------------------------------------------------------------ 7. regimes and timing
rr = regime_results()
check("R1 frozen regimes: pinning identity, all 9 states viable, 36 pairs each",
      rr['pin'] and all(len(rr['frozen'][r]) == 9 for r in (1, 2)) and rr['frozen_pairs'] == {1: 36, 2: 36})
check("R2 mode-blind kernel = the eight corner-free states (28 pairs), equal to the full-information kernel; corner lost",
      frozenset(rr['mode_blind']) == frozenset(CORNER_FREE) and rr['mb_pairs'] == 28)
mbW = [frozenset(x for x in SAFE if mode_blind_win(x, h)) for h in range(4)]
check("R3 mode-blind horizon family stabilises after one application (W_1 = W_2 = W_3)", mbW[1] == mbW[2] == mbW[3] and len(mbW[1]) == 8)
tg = timing_grid()
check("T1 timing grid: 93 cells, 33 viable under free switching, 43 under alternation (21, 16, 6)",
      tg['cells'] == 93 and tg['viable_free'] == 33 and tg['viable_alt'] == 43 and tg['alt_by_T'] == {1: 21, 2: 16, 3: 6})
check("T2 strict form fails exactly at (2,1), (3,2), (4,3); floored strict form fails on 21 cells",
      tg['strict_real_bad'] == [(Q(2), 1), (Q(3), 2), (Q(4), 3)] and len(tg['strict_floor_bad']) == 21)
check("T3 alternation worst damage 1, 3/2, 5/2, 3, 4, 9/2 = ceil(T/2) + floor(T/2)/2; max-plus recursion equals path enumeration on the 3-regime graph",
      [worst_damage_alt(T) for T in range(1, 7)] == [Q(1), Q(3, 2), Q(5, 2), Q(3), Q(4), Q(9, 2)]
      and all(worst_damage_alt(T) == -(-T // 2) + Q(T // 2, 2) for T in range(1, 13)) and tg['dp_ok']
      and tg['worst3'] == [Q(1), Q(3, 2), Q(5, 2), Q(3), Q(4), Q(9, 2)])

# ------------------------------------------------------------------ 8. continuous fibre
b = benchmark()
check("C1 benchmark crossover Y* = 27/5; margin law (Y-27/5)/10; Y=6 caps 11/10, 39/50, sum 47/25, margin 3/50; Y=5 witness (6/5, 4/5)",
      b['Ystar'] == Q(27, 5) and b['margin_law_check'] and cap1(Q(6)) == Q(11, 10) and cap2(Q(6)) == Q(39, 50)
      and cap1(Q(6)) + cap2(Q(6)) == Q(47, 25) and b['margin6'] == Q(3, 50) and b['witness5'] == (Q(6, 5), Q(4, 5)))
check("C2 radius: per-cap increase below 3/50 leaves the Y=6 obstruction, 3/50 removes it",
      b['radius6'] == Q(3, 50) and b['below_radius_still_obstructed'] and b['at_radius_feasible'])
d = duality()
check("C3 two-floor duality: primal = dual = -1/10 at u = 1/2, lambda = (1/2, 1/2)",
      d['primal'] == d['dual'] == Q(-1, 10) and d['ustar'] == [Q(1, 2)] and d['lstar'] == [(Q(1, 2), Q(1, 2))])
check("C4 nonconvex gap: primal -1 against dual 0; feasible contrast +1/10 on both sides at u = 3/10",
      d['nonconvex_primal'] == Q(-1) and d['nonconvex_dual'] == Q(0) and d['feasible_primal'] == d['feasible_dual'] == Q(1, 10)
      and d['feasible_u'] == [Q(3, 10)])
check("C5 Helly-tight triple pairwise feasible, jointly infeasible", d['helly_pairwise'] and not d['helly_triple'])
dr = drift(); fl = floors()
check("C6 drift: naive s/5 + 1/100 (21/100 ... 41/100), corrected 0, sign law",
      dr['formula_ok'] and all(r['corrected'] == 0 for r in dr['rows']) and dr['sign_ok']
      and [r['naive'] for r in dr['rows']] == [Q(21, 100), Q(13, 50), Q(31, 100), Q(9, 25), Q(41, 100)])
check("C7 floors: each satisfiable, no common instrument, value -1/2", fl['each'] and not fl['common'] and fl['value'] == Q(-1, 2))

# ------------------------------------------------------------------ 9. family scaling
fam = {}
for cap in (4, 5):
    sysd = make_system(cap)
    pairs = sorted(frozenset({x, y}) for x in sysd['safe'] for y in sysd['safe'] if x < y)
    row = {}
    for key, name, obs, conv in CLASSES:
        row[key] = len(BeliefGame(obs, conv, (1, 2), sysd).kernel(pairs)[0])
    row['b_inst'] = len(BeliefGame(obs_agg, 'branch', (1, 2), sysd).kernel(pairs)[0])
    row['cf'] = sum(1 for B in pairs if (1, 1) not in B)
    row['n'] = len(pairs)
    fam[cap] = row
check("F1 cap 4: 120 pairs, kernels (98, 102, 100, 105), full = corner-free, private institutional = aggregate",
      fam[4]['n'] == 120 and (fam[4]['inst'], fam[4]['agg'], fam[4]['codex'], fam[4]['full']) == (98, 102, 100, 105)
      and fam[4]['full'] == fam[4]['cf'] and fam[4]['b_inst'] == fam[4]['agg'])
check("F2 cap 5: 300 pairs, kernels (266, 272, 269, 276), full = corner-free, private institutional = aggregate",
      fam[5]['n'] == 300 and (fam[5]['inst'], fam[5]['agg'], fam[5]['codex'], fam[5]['full']) == (266, 272, 269, 276)
      and fam[5]['full'] == fam[5]['cf'] and fam[5]['b_inst'] == fam[5]['agg'])

# ------------------------------------------------------------------ 10. results.json consistency
rj = json.load(open(os.path.join(SRC, 'work', 'results.json')))
check("J1 results.json agrees with the recomputation on the headline counts",
      [rj['kernels']['audited'][k]['universe'] for k in ('inst', 'agg', 'codex', 'full')] == [111, 143, 119, 255]
      and rj['decentralised']['universe'] == 30 and rj['design']['adequate'] == 1694 and rj['blind']['size'] == 111)

# ------------------------------------------------------------------ 11. Lean declarations
lean_dir = next((d for d in (os.path.join(SRC, 'lean'), os.path.join(SRC, 'src', 'lean')) if os.path.isdir(d)), os.path.join(SRC, 'lean'))
names = ''
for f in ('WS_WorkedSystems.lean', 'WS_WorkedSystems_v2.lean'):
    p = os.path.join(lean_dir, f)
    if os.path.exists(p):
        names += open(p).read()
check("L1 Lean modules present with theorems Wk_mono_obs, master_action_axis, master_memory_axis, master_monotone and no sorry",
      all(('theorem ' + n) in names for n in ('Wk_mono_obs', 'master_action_axis', 'master_memory_axis', 'master_monotone'))
      and 'sorry' not in names)

# ------------------------------------------------------------------ 12. text checks
def pdf_text(path):
    try:
        import pymupdf
    except Exception:
        try:
            import fitz as pymupdf
        except Exception:
            return None
    if not os.path.exists(path):
        return None
    t = ''.join(pg.get_text() for pg in pymupdf.open(path))
    return re.sub(r'[\s\u00ad]+', ' ', t.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff'))


main = pdf_text(os.path.join(HERE, 'paper11c_worked_systems_audit_v5.pdf'))
si = pdf_text(os.path.join(HERE, 'paper11c_worked_systems_audit_v5_supplementary.pdf'))
MAIN_NEEDLES = ['111', '143', '119', '255', '4,140', '1,694', '74 distinct kernels', '27/5', '3/50', '−1/10',
                '12 of the 28', '16 coarsest', '32 alternation policies', '33 and 43', '93-cell']
SI_NEEDLES = ['104 members', '151+372+372+799', '4 behavioural classes', '52 partitions', '(25, 26, 26, 28)', '(127,143,191,255)']
if main is None:
    check("X1 (main PDF not available: text checks skipped)", True)
else:
    missing = [n for n in MAIN_NEEDLES if n.replace('−', '-') not in main.replace('−', '-').replace('\u2212', '-')]
    check("X1 main text quotes the recomputed headline numbers (" + ', '.join(n.replace('−', '-') for n in MAIN_NEEDLES) + ")", not missing)
    check("X2 main text states the check count (" + str(NCHECKS_EXPECTED) + " named checks) consistently with this script",
          (str(NCHECKS_EXPECTED) + " named checks") in main and NPASS + NFAIL + 2 == NCHECKS_EXPECTED)
if si is None:
    check("X3 (supplement PDF not available: text checks skipped)", True)
else:
    missing = [n for n in SI_NEEDLES if n.replace(' ', '') not in si.replace(' ', '')]
    check("X3 supplement quotes the recomputed numbers (" + ', '.join(SI_NEEDLES) + ")", not missing)

# ------------------------------------------------------------------ summary
total = NPASS + NFAIL
summary = f"{NPASS}/{total} checks passed in {time.time() - T0:.1f} s" + (" (quick mode)" if QUICK else "")
print(summary)
LINES.append(summary)
if not QUICK:   # the shipped record is always a full run
    with open(os.path.join(HERE, 'paper11c_worked_systems_audit_v5_verification_output.txt'), 'w') as f:
        f.write('\n'.join(LINES) + '\n')
sys.exit(0 if NFAIL == 0 else 1)
