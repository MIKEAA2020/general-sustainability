#!/usr/bin/env python3
"""Independently re-read saved capacities and primal/dual LP witnesses, without solving."""
import collections,csv,gzip,json
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from accounts_F12 import require
from transition_path_bounds_F12 import cases,SCALE,TOL_HA
ROOT=Path(__file__).resolve().parents[1]


def audit():
 flows={}
 for country in ['BRA','IDN']:
  d=collections.defaultdict(dict);nation=collections.defaultdict(float)
  with gzip.open(ROOT/f'data/{country}_annual_transition_capacities_F12.csv.gz','rt')as f:
   for r in csv.DictReader(f):
    e=int(r['start']),int(r['class_from']),int(r['class_to']);v=float(r['area_ha']);d[r['unit']][e]=v;nation[e]+=v
  d['national']=dict(nation);flows[country]=dict(d)
 certificates=list(csv.DictReader((ROOT/'data/transition_path_LP_certificates_F12.csv').open()));w=np.load(ROOT/'data/transition_path_primal_dual_witnesses_F12.npz',allow_pickle=False);worst=collections.Counter()
 for r in certificates:
  country,unit=r['country'],r['unit'];flow=flows[country][unit];edges=sorted(flow);codes={a for y,a,b in edges}|{b for y,a,b in edges};forest,target=next((f,codes-f if t is None else t)for g,f,name,t in cases(country)if(g,name)==(r['group'],r['target']));key=r['witness_key'];x=w[key+'_x'];pi=w[key+'_eq_dual'];la=w[key+'_lo_dual'];mu=w[key+'_hi_dual'];cap=np.array([flow[e]/SCALE for e in edges]);lower=np.array([cap[k]if e[0]==2015 and e[1]in forest else 0. for k,e in enumerate(edges)]);upper=np.array([0. if e[0]==2015 and e[1]not in forest else cap[k]for k,e in enumerate(edges)]);c=np.array([(-1. if r['optimization']=='max'else 1.)if e[0]==2022 and e[2]in target else 0. for e in edges])
  nodes=sorted({(y+1,b)for y,a,b in edges if y<2022}|{(y,a)for y,a,b in edges if y>2015});ni={v:k for k,v in enumerate(nodes)};rr=[];cc=[];vv=[]
  for k,(y,a,b)in enumerate(edges):
   if y>2015:rr.append(ni[y,a]);cc.append(k);vv.append(-1.)
   if y<2022:rr.append(ni[y+1,b]);cc.append(k);vv.append(1.)
  A=coo_matrix((vv,(rr,cc)),shape=(len(nodes),len(edges))).tocsr();require(x.shape==cap.shape and pi.shape==(len(nodes),),'Witness dimensions invalid')
  eq=float(np.max(np.abs(A@x),initial=0))*SCALE;bound=max(float(np.max(lower-x,initial=0)),float(np.max(x-upper,initial=0)))*SCALE;stationarity=float(np.max(np.abs(c-A.T@pi-la-mu),initial=0));gap=abs(float(c@x-lower@la-upper@mu))*SCALE
  require(max(eq,bound,gap)<TOL_HA and stationarity<1e-7,'Invalid saved primal/dual witness')
  require(float(np.min(la,initial=0))>=-1e-7 and float(np.max(mu,initial=0))<=1e-7,'Invalid dual multiplier sign')
  objective=float(c@x)*SCALE*(-1 if r['optimization']=='max'else 1);require(abs(objective-float(r['objective_ha']))<TOL_HA,'Saved objective disagrees with witness')
  for k,v in [('primal_equation_residual_ha',eq),('bound_violation_ha',bound),('stationarity_residual',stationarity),('primal_dual_gap_ha',gap)]:worst[k]=max(worst[k],v)
 require(len(w.files)==4*len(certificates),'Unindexed or missing witness arrays');w.close()
 result=dict(saved_primal_dual_witnesses_independently_checked=len(certificates),solver_called=False,all_pass=True,maxima=dict(worst),not_ecological_validation=True)
 (ROOT/'metadata/transition_witness_audit_F12.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return result

if __name__=='__main__':audit()
