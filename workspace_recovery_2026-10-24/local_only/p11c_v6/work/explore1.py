import time
from ws_core import *
t0=time.time()
# full universe kernels
for conv in [None,'branch','optimistic']:
    ks = class_kernels(conv, beliefs=UNIVERSE)
    for k,v in ks.items():
        K=v['kernel']
        mx = maximal_sets(K)
        by_size = {}
        for B in K: by_size[len(B)] = by_size.get(len(B),0)+1
        print(conv or 'audited', k, v['size'], 'hist', v['history'], 'downset', is_downset(K), 'maximal', [(len(m), blabel(m)) for m in mx][:12], 'bysize', dict(sorted(by_size.items())))
print('t', time.time()-t0)
# closed forms
for key,name,obs,conv in CLASSES:
    if conv=='ledger':
        g=BeliefGame(obs,'ledger'); K,_=g.kernel(UNIVERSE)
        C=ledger_kernel_closed_form(UNIVERSE, obs)
        print(name,'ledger closed form equal:', K==C, len(K), len(C))
        g=BeliefGame(obs,'branch'); K,_=g.kernel(UNIVERSE)
        C=branch_kernel_closed_form(UNIVERSE, obs)
        print(name,'branch closed form equal:', K==C, len(K), len(C))
# alternation safety per state
print({label(x):[a for a in (1,2) if alternation_safe(x,a)] for x in SAFE})
print('t', time.time()-t0)
# stationary
for obs,nm in [(obs_agg,'agg'),(obs_full,'full')]:
    for mem in (False,True):
        r=stationary_union(obs,memory=mem,beliefs=UNIVERSE)
        print(nm,'memory',mem,'policies',r['policies'],'union',len(r['union']),'pairs',sum(1 for B in r['union'] if len(B)==2),'max states',r['max_states'],'best sets',[blabel(S) for S in r['sustained'][:4]])
    r=stationary_union(obs,memory=True,no_repeat=True,beliefs=UNIVERSE)
    print(nm,'memory+norepeat policies',r['policies'],'union',len(r['union']),'pairs',sum(1 for B in r['union'] if len(B)==2),'max',r['max_states'])
print('t', time.time()-t0)
