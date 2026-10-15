#!/usr/bin/env python3
"""Compute every audited quantity of paper11c v5 and write results.json."""
import json, time, collections, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ws_core import *

T0 = time.time()
R = {}


def lab_list(fam):
    return [blabel(B) for B in sorted(fam, key=lambda B: (len(B), sorted(B)))]


def jq(x):
    if isinstance(x, Q):
        return fr(x)
    if isinstance(x, (list, tuple)):
        return [jq(v) for v in x]
    if isinstance(x, dict):
        return {str(k): jq(v) for k, v in x.items()}
    if isinstance(x, (set, frozenset)):
        return sorted(jq(v) for v in x)
    return x

# ---- system ---------------------------------------------------------------
R['system'] = dict(cap=CAP, n_states=len(STATES), n_safe=len(SAFE),
                   safe=[label(x) for x in SAFE], corner=label(CORNER),
                   corner_free=[label(x) for x in CORNER_FREE],
                   R={label(x): safe_actions(x) for x in SAFE},
                   succ={label(x): {str(u): label(step(x, u)) for u in (0, 1, 2)} for x in SAFE},
                   alternation_phases={label(x): [a for a in (1, 2) if alternation_safe(x, a)] for x in SAFE},
                   n_pairs=len(PAIRS))

# ---- class kernels on pairs and on the universe -----------------------------
CONVS = [('audited', None), ('branch', 'branch'), ('optimistic', 'optimistic'),
         ('first', 'first'), ('last', 'last')]
K = {}
for cname, conv in CONVS:
    K[cname] = {'pairs': class_kernels(conv, PAIRS), 'universe': class_kernels(conv, UNIVERSE)}
    # instrument 0 admitted leaves the audited kernels unchanged
R['kernels'] = {}
for cname, _ in CONVS:
    R['kernels'][cname] = {}
    for key in ('inst', 'agg', 'codex', 'full'):
        kp = K[cname]['pairs'][key]['kernel']
        ku = K[cname]['universe'][key]['kernel']
        bysize = collections.Counter(len(B) for B in ku)
        R['kernels'][cname][key] = dict(
            pairs=len(kp), universe=len(ku),
            by_size={str(s): bysize[s] for s in sorted(bysize)},
            maximal=lab_list(maximal_sets(ku)),
            n_maximal=len(maximal_sets(ku)),
            history_pairs=K[cname]['pairs'][key]['history'],
            history_universe=K[cname]['universe'][key]['history'],
            downset=is_downset(ku),
            dead_pairs=lab_list(set(PAIRS) - kp),
            pairs_universe_consistent=(kp == frozenset(B for B in ku if len(B) == 2)))
A = {key: K['audited']['pairs'][key]['kernel'] for key in ('inst', 'agg', 'codex', 'full')}
AU = {key: K['audited']['universe'][key]['kernel'] for key in ('inst', 'agg', 'codex', 'full')}
BU = {key: K['branch']['universe'][key]['kernel'] for key in ('inst', 'agg', 'codex', 'full')}
OU = {key: K['optimistic']['universe'][key]['kernel'] for key in ('inst', 'agg', 'codex', 'full')}
R['identities'] = dict(
    meet_is_inst=(A['agg'] & A['codex'] == A['inst']),
    join_missing=lab_list(A['full'] - (A['agg'] | A['codex'])),
    agg_minus_codex=lab_list(A['agg'] - A['codex']),
    codex_minus_agg=lab_list(A['codex'] - A['agg']),
    full_minus_agg=lab_list(A['full'] - A['agg']),
    full_minus_codex=lab_list(A['full'] - A['codex']),
    full_is_corner_free=(A['full'] == frozenset(B for B in PAIRS if CORNER not in B)),
    chain_pairs=[A['inst'] <= A['agg'] <= A['full'], A['inst'] <= A['codex'] <= A['full'],
                 not (A['agg'] <= A['codex']), not (A['codex'] <= A['agg'])],
    universe_meet_is_inst=(AU['agg'] & AU['codex'] == AU['inst']),
    universe_chain=[AU['inst'] <= AU['agg'] <= AU['full'], AU['inst'] <= AU['codex'] <= AU['full']],
    universe_agg_codex_incomparable=[not (AU['agg'] <= AU['codex']), not (AU['codex'] <= AU['agg'])],
    audited_subset_branch={k: AU[k] <= BU[k] for k in AU},
    audited_subset_optimistic={k: AU[k] <= OU[k] for k in AU},
    branch_inst_equals_agg=(BU['inst'] == AU['agg']),
    branch_codex_vs_optimistic_codex=dict(equal=(BU['codex'] == OU['codex']),
                                          branch_minus_opt=lab_list(BU['codex'] - OU['codex']),
                                          opt_minus_branch=lab_list(OU['codex'] - BU['codex'])),
    optimistic_codex_pairs=len(K['optimistic']['pairs']['codex']['kernel']),
    optimistic_regains=lab_list(K['optimistic']['pairs']['codex']['kernel'] - A['codex']),
    fixed_thread={c: [K[c]['pairs'][k]['size'] for k in ('inst', 'agg', 'codex', 'full')] for c in ('first', 'last')},
    fixed_thread_disagree=(K['first']['pairs']['inst']['kernel'] != K['last']['pairs']['inst']['kernel']),
)
# instrument 0 admitted
K0 = class_kernels(None, UNIVERSE, actions=(0, 1, 2))
R['identities']['instrument0_unchanged'] = all(K0[k]['kernel'] == AU[k] for k in AU)
# closed forms
R['closed_forms'] = {}
for key, name, obs, conv in CLASSES:
    if conv == 'ledger':
        R['closed_forms'][key] = dict(
            ledger=(ledger_kernel_closed_form(UNIVERSE, obs) == AU[key]),
            branch=(branch_kernel_closed_form(UNIVERSE, obs) == BU[key]))
# blind kernel
Wb, hb = kernel_free_bitmask([list(CORNER_FREE)])
blind = frozenset(mask_to_set(m) for m in Wb)
R['blind'] = dict(size=len(blind), equals_inst=(blind == AU['inst']),
                  maximal=lab_list(maximal_sets(blind)), history=hb,
                  pairs=sum(1 for B in blind if len(B) == 2))
# master table rows
R['master'] = []
for B in PAIRS:
    R['master'].append(dict(
        pair=blabel(B),
        inst=B in A['inst'], agg=B in A['agg'], codex=B in A['codex'], full=B in A['full'],
        b_inst=B in K['branch']['pairs']['inst']['kernel'],
        b_codex=B in K['branch']['pairs']['codex']['kernel'],
        o_codex=B in K['optimistic']['pairs']['codex']['kernel']))
print('kernels done', time.time() - T0)

# ---- stationary policies ------------------------------------------------------
st = {}
r = stationary_union(obs_agg, memory=False, beliefs=UNIVERSE)
st['agg_memoryless'] = dict(policies=r['policies'], union=len(r['union']), max_states=r['max_states'])
r = stationary_union(obs_agg, memory=True, beliefs=UNIVERSE)
st['agg_memory1'] = dict(policies=r['policies'], union=len(r['union']), max_states=r['max_states'],
                         equals_agg_kernel=(r['union'] == AU['agg']))
r = stationary_union(obs_agg, memory=True, no_repeat=True, beliefs=UNIVERSE)
st['agg_alternation'] = dict(policies=r['policies'], union=len(r['union']), max_states=r['max_states'],
                             equals_agg_kernel=(r['union'] == AU['agg']),
                             sustained_sets=lab_list(r['sustained'][:4]))
r = stationary_union(obs_full, memory=False, beliefs=UNIVERSE)
st['full_memoryless'] = dict(policies=r['policies'], union=len(r['union']), max_states=r['max_states'],
                             equals_full_kernel=(r['union'] == AU['full']))
# blind alternation: the two global phases
for a in (1, 2):
    S = frozenset(x for x in SAFE if alternation_safe(x, a))
    st[f'global_phase_{a}'] = lab_list([S])
R['stationary'] = st
print('stationary done', time.time() - T0)

# ---- decentralised -----------------------------------------------------------
S = sustainers()
dec_pairs = decentralised_kernel(PAIRS, S)
dec_univ = decentralised_kernel(UNIVERSE, S)
aud = frozenset({(1, 2), (2, 1)})
sust = [(law_str(l1), law_str(l2)) for l1, l2 in LAW_PAIRS if law_sustains_belief(aud, l1, l2)]
L1 = sorted({a for a, b in sust}); L2 = sorted({b for a, b in sust})
auth = {}
for agency, vote in ((1, 1), (1, 2), (2, 1), (2, 2)):
    idxs = frozenset(i for i, (l1, l2) in enumerate(LAW_PAIRS)
                     if (l1 if agency == 1 else l2)[1] == vote)
    Sr = {x: S[x] & idxs for x in SAFE}
    auth[f'agency{agency}_vote{vote}'] = lab_list(decentralised_kernel(PAIRS, Sr))
whole = {}
for agency in (1, 2):
    for v in (1, 2):
        idxs = frozenset(i for i, (l1, l2) in enumerate(LAW_PAIRS)
                         if all((l1 if agency == 1 else l2)[z] == v for z in range(CAP + 1)))
        Sr = {x: S[x] & idxs for x in SAFE}
        whole[f'agency{agency}_all{v}'] = len(decentralised_kernel(PAIRS, Sr))
beh = {(behavioural_class(l1), behavioural_class(l2)) for l1, l2 in LAW_PAIRS}
sust_beh = {(behavioural_class(dict(zip(range(4), map(int, a)))), behavioural_class(dict(zip(range(4), map(int, b))))) for a, b in sust}
fix1 = sum(1 for (a, b) in sust if a[1] == '1')
fix2 = sum(1 for (a, b) in sust if b[1] == '1')
R['decentralised'] = dict(
    laws=len(LAWS), law_pairs=len(LAW_PAIRS), behavioural_pairs=len(beh),
    sustainers={label(x): len(S[x]) for x in SAFE},
    pairs=len(dec_pairs), pairs_list=lab_list(dec_pairs),
    universe=len(dec_univ), maximal=lab_list(maximal_sets(dec_univ)),
    by_size={str(s): c for s, c in sorted(collections.Counter(len(B) for B in dec_univ).items())},
    lost_pairs=len(A['full'] - dec_pairs), subset_of_full=(dec_pairs <= A['full']),
    sustaining_12_21=len(sust), product=(set(sust) == {(a, b) for a in L1 for b in L2}),
    L1=L1, L2=L2, sustaining_behavioural=len(sust_beh),
    fix_agency1_vote1=fix1, fix_agency2_vote1=fix2, authority=auth, whole_law=whole,
    swap_symmetric=(sorted(auth['agency1_vote2']) == sorted(blabel(frozenset((y, x) for x, y in B))
                                                             for B in [frozenset((int(s[0]), int(s[1])) for s in p.split('|')) for p in auth['agency2_vote1']])))
print('decentralised done', time.time() - T0)

# ---- design census -----------------------------------------------------------
rows, edges = design_census()
dyn = [r for r in rows if r['full_viable']]
one = [r for r in rows if r['one_step']]
byk = {}
for k in sorted({r['ncells'] for r in rows}):
    rs = [r for r in rows if r['ncells'] == k]
    byk[str(k)] = dict(partitions=len(rs), adequate=sum(1 for r in rs if r['full_viable']),
                       min_kernel=min(r['kernel'] for r in rs), max_kernel=max(r['kernel'] for r in rs),
                       min_pairs=min(r['pairs'] for r in rs), max_pairs=max(r['pairs'] for r in rs))
distinct = {}
for r in rows:
    W, _ = kernel_free_bitmask([[tuple(x) for x in c] for c in r['cells']])
    distinct.setdefault(frozenset(W), 0)
    distinct[frozenset(W)] += 1
ksizes = collections.Counter(r['kernel'] for r in rows)
minK = min(ksizes)
coarsest = min(r['ncells'] for r in dyn)
# ledger census (closed form)
ledger_adequate = 0; ledger_max = 0
for r in rows:
    lab = {x: i for i, c in enumerate(r['cells']) for x in c}
    obs = (lambda x, lab=lab: lab.get(x, -1))
    Kl = ledger_kernel_closed_form(UNIVERSE, obs)
    ledger_adequate += (frozenset(CORNER_FREE) in Kl)
    ledger_max = max(ledger_max, len(Kl))
R['design'] = dict(
    partitions=len(rows), edges=[[label(a), label(b)] for a, b in sorted(edges)],
    adequate=len(dyn), one_step=len(one), equal=(set(map(id, dyn)) == set(map(id, one))),
    dyn_eq_one=all(r['full_viable'] == r['one_step'] for r in rows),
    by_cells=byk, coarsest_cells=coarsest,
    coarsest=[["|".join(label(x) for x in c) for c in r['cells']] for r in dyn if r['ncells'] == coarsest],
    n_coarsest=sum(1 for r in dyn if r['ncells'] == coarsest),
    distinct_kernels=len(distinct), kernel_sizes={str(k): ksizes[k] for k in sorted(ksizes)},
    min_kernel=minK, n_min_kernel=ksizes[minK],
    min_kernel_all_merge_critical=all(any({(1, 2), (1, 3), (2, 1), (3, 1)} <= set(map(tuple, c)) for c in r['cells'])
                                      for r in rows if r['kernel'] == minK),
    max_belief_sizes={str(k): v for k, v in sorted(collections.Counter(r['max_belief'] for r in rows).items())},
    pairs_sizes={str(k): v for k, v in sorted(collections.Counter(r['pairs'] for r in rows).items())},
    stabilisation={str(k): v for k, v in sorted(collections.Counter(r['stab'] for r in rows).items())},
    agg_row=next(dict(r) for r in rows if r['cells'] == sorted(sorted(c) for c in {s: [x for x in CORNER_FREE if sum(x) == s] for s in range(3, 7)}.values())),
    ledger_adequate=ledger_adequate, ledger_max_kernel=ledger_max)
R['design']['agg_row']['cells'] = [[label(x) for x in c] for c in R['design']['agg_row']['cells']]
print('design census done', time.time() - T0)

# ---- target census ------------------------------------------------------------
tc = target_census()
R['target'] = dict(n=tc['n'], adequate=tc['n_adequate'],
                   adequate_list=[["|".join(label(x) for x in F) for F in P] for P in tc['adequate']],
                   all_list=[["|".join(label(x) for x in F) for F in P] for P in tc['partitions']],
                   edges=[[label(a), label(b)] for a, b in tc['edges']], n_e=tc['n_e'], n_both=tc['n_both'],
                   R={label(x): list(v) for x, v in tc['R'].items()},
                   maxcommon=lab_list(tc['maxcommon']),
                   two_cell=[["|".join(label(x) for x in F) for F in P] for P in tc['two_cell']],
                   helly2=tc['helly2'], helly3=tc['helly3'])

# ---- regimes, timing ----------------------------------------------------------
rr = regime_results()
R['regimes'] = dict(frozen_states={str(r): len(rr['frozen'][r]) for r in (1, 2)}, pin=rr['pin'],
                    frozen_pairs=rr['frozen_pairs'], mode_blind_states=len(rr['mode_blind']),
                    mode_blind_pairs=rr['mb_pairs'], mode_blind_is_full=(frozenset(rr['mode_blind']) == frozenset(CORNER_FREE)))
tg = timing_grid()
R['timing'] = dict(cells=tg['cells'], viable_free=tg['viable_free'], viable_alt=tg['viable_alt'],
                   alt_by_T=tg['alt_by_T'], strict_real_bad=[[fr(z), T] for z, T in tg['strict_real_bad']],
                   strict_floor_bad=len(tg['strict_floor_bad']), dp_ok=tg['dp_ok'],
                   worst3=[fr(v) for v in tg['worst3']],
                   worst_alt=[fr(worst_damage_alt(T)) for T in range(1, 7)],
                   rows=[[fr(z), sig, [[int(a), int(b)] for a, b in row]] for z, sig, row in tg['rows']])

# ---- continuous fibre ----------------------------------------------------------
R['benchmark'] = jq(benchmark())
R['duality'] = jq(duality())
R['drift'] = jq(drift())
R['floors'] = jq(floors())

# ---- family scaling --------------------------------------------------------------
fam = {}
for cap in (3, 4, 5):
    sysd = make_system(cap)
    pairs = sorted(frozenset({x, y}) for x in sysd['safe'] for y in sysd['safe'] if x < y)
    row = dict(safe=len(sysd['safe']), pairs=len(pairs))
    for key, name, obs, conv in CLASSES:
        g = BeliefGame(obs, conv, (1, 2), sysd); Kk, h = g.kernel(pairs); row[key] = len(Kk)
        if conv == 'ledger':
            g = BeliefGame(obs, 'branch', (1, 2), sysd); Kk, h = g.kernel(pairs); row['b_' + key] = len(Kk)
    row['corner_free_pairs'] = sum(1 for B in pairs if (1, 1) not in B)
    fam[str(cap)] = row
R['family'] = fam
R['runtime_s'] = round(time.time() - T0, 1)
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.json'), 'w'), indent=1, default=str)
print('done', R['runtime_s'])
