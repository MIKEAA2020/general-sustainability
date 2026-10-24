import time, json, collections
from ws_core import *
t0=time.time()
rows, edges = design_census()
print('partitions', len(rows), 'edges', sorted((label(a),label(b)) for a,b in edges), 't', time.time()-t0)
dyn = [r for r in rows if r['full_viable']]
one = [r for r in rows if r['one_step']]
print('dynamic adequate', len(dyn), 'one-step adequate', len(one), 'dyn subset one', all(r['one_step'] for r in dyn))
print('by ncells dyn', collections.Counter(r['ncells'] for r in dyn))
print('by ncells one', collections.Counter(r['ncells'] for r in one))
print('by ncells all', collections.Counter(r['ncells'] for r in rows))
coarsest = min(r['ncells'] for r in dyn)
print('coarsest dyn', coarsest, [r['cells'] for r in dyn if r['ncells']==coarsest])
print('kernel size distribution', collections.Counter(r['kernel'] for r in rows).most_common(12))
print('max belief distribution', collections.Counter(r['max_belief'] for r in rows))
print('pairs distribution', collections.Counter(r['pairs'] for r in rows))
print('stab', collections.Counter(r['stab'] for r in rows))
# one-step adequate but not dynamic: examples
gap=[r for r in rows if r['one_step'] and not r['full_viable']]
print('gap', len(gap), 'examples', [ (r['cells'], r['kernel'], r['max_belief']) for r in gap[:5]])
# aggregation partition row
aggP=[sorted(c) for c in {}.values()]
cells={}
for x in CORNER_FREE: cells.setdefault(sum(x),[]).append(x)
aggcells=sorted(sorted(c) for c in cells.values())
for r in rows:
    if r['cells']==aggcells: print('agg row', r)
# partitions with kernel == 143 (same as aggregation)?
print('kernel 143 count', sum(1 for r in rows if r['kernel']==143))
# minimal (coarsest) one-step adequate
c1=min(r['ncells'] for r in one); print('coarsest one-step', c1, sum(1 for r in one if r['ncells']==c1))
json.dump(rows, open('census_rows.json','w'), default=str)
print('t', time.time()-t0)
