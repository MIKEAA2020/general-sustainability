import time, json, collections
from ws_core import *
t0=time.time()
rows=json.load(open('census_rows.json'))
print('min kernel', min(r['kernel'] for r in rows), [ (r['cells'], r['kernel'], r['max_belief'], r['pairs']) for r in rows if r['kernel']==min(r['kernel'] for r in rows)])
print('distinct kernel sizes', sorted(set(r['kernel'] for r in rows)))
# distinct kernels as sets: recompute quickly for all partitions storing frozenset of masks
distinct={}
for r in rows:
    cells=[[tuple(x) for x in c] for c in r['cells']]
    W,_=kernel_free_bitmask(cells)
    distinct.setdefault(frozenset(W),[]).append(r['ncells'])
print('distinct kernels', len(distinct), 't', time.time()-t0)
# blind kernel (one cell)
Wb,_=kernel_free_bitmask([list(CORNER_FREE)])
print('blind kernel', len(Wb), 'maximal', [blabel(m) for m in maximal_sets(mask_to_set(m) for m in Wb)], 'pairs', sum(1 for m in Wb if bin(m).count('1')==2))
# ledger census via closed form: whole X' viable under any partition?
cnt=0; best=0
for r in rows:
    cells=[[tuple(x) for x in c] for c in r['cells']]
    lab={x:i for i,c in enumerate(cells) for x in c}
    obs=lambda x,lab=lab: lab.get(x,-1)
    K=ledger_kernel_closed_form(UNIVERSE, obs)
    if frozenset(CORNER_FREE) in K: cnt+=1
    best=max(best,len(K))
print('ledger: partitions with whole set viable', cnt, 'max kernel', best, 't', time.time()-t0)
# target census
tc=target_census(); print({k:v for k,v in tc.items() if k not in ('partitions','adequate')})
print('adequate', tc['adequate'])
# regimes
rr=regime_results(); print('regimes', {k:(len(v) if hasattr(v,'__len__') else v) for k,v in rr.items()}, rr['frozen_pairs'], rr['mb_pairs'], sorted(rr['mode_blind']))
# timing
tg=timing_grid(); print('timing', tg['cells'], tg['viable_free'], tg['viable_alt'], tg['alt_by_T'], tg['strict_real_bad'], len(tg['strict_floor_bad']), tg['dp_ok'], [fr(v) for v in tg['worst3']])
# benchmark
b=benchmark(); print('bench', fr(b['Ystar']), [(fr(r['Y']),fr(r['c1']),fr(r['c2']),fr(r['sum']),r['feasible'],fr(r['margin'])) for r in b['rows']], fr(b['margin6']), b['margin_law_check'], b['delta_half_feasible'], b['delta_full_feasible'])
d=duality(); print('dual', {k:(fr(v) if isinstance(v,Q) else v) for k,v in d.items()})
dr=drift(); print('drift', [(fr(r['s']),fr(r['naive']),fr(r['corrected'])) for r in dr['rows']], dr['formula_ok'], dr['sign_ok'])
print('floors', floors())
# family scaling: caps 4,5 on pairs
for cap in (4,5):
    sysd=make_system(cap)
    pairs=sorted(frozenset({x,y}) for x in sysd['safe'] for y in sysd['safe'] if x<y)
    out={}
    for key,name,obs,conv in CLASSES:
        g=BeliefGame(obs,conv,(1,2),sysd); K,h=g.kernel(pairs); out[key]=len(K)
    gb={}
    for key,name,obs,conv in CLASSES:
        g=BeliefGame(obs,'branch' if conv=='ledger' else conv,(1,2),sysd); K,h=g.kernel(pairs); gb[key]=len(K)
    print('cap',cap,'pairs',len(pairs),'audited',out,'branch',gb, 't', time.time()-t0)
