#!/usr/bin/env python3
"""Sharp conditional endpoint-conversion bounds from annual aggregate transitions.
A marked flow follows land that is forest at the 2015 endpoint. Annual pairwise
matrices constrain, but do not identify, its 2023 destinations. No event sums are
called unique areas. No map-error, biomass, causality or reference calibration claim.
"""
import argparse,collections,csv,gzip,hashlib,io,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from openpyxl import load_workbook
from accounts_F12 import require,save
ROOT=Path(__file__).resolve().parents[1]
SCALE=100000. # Source hectares are converted to 100,000 ha for the LP.
TOL_HA=.02


def extract(country,path):
 j=json.loads((ROOT/'metadata/source_registry_F12.json').read_text());key='BRA_C11_biome_state.xlsx'if country=='BRA'else'IDN_C41.xlsx';require(hashlib.sha256(path.read_bytes()).hexdigest()==j[key]['sha256'],'Transition source drift')
 w=load_workbook(path,read_only=True,data_only=True);sheet='TRANSITION_11'if country=='BRA'else'TRANSITION';it=iter(w[sheet].values);h=next(it)
 if country=='BRA':geo=[h.index('state'),h.index('biome')]
 else:geo=[h.index('territory_level_2_3'),h.index('territory_level_3_3')]
 ai=h.index('class_from');bi=h.index('class_to');cols={y:h.index(f'p{y}_{y+1}')for y in range(2015,2023)};d=collections.defaultdict(dict);allflow=collections.defaultdict(float)
 for row in it:
  if row[0]is None:continue
  unit=' | '.join(str(row[k])for k in geo);a,b=int(row[ai]),int(row[bi])
  for y,k in cols.items():
   v=float(row[k]);require(v>=0 and math.isfinite(v),'Invalid transition capacity')
   if v>0:d[unit][y,a,b]=v;allflow[y,a,b]+=v
 # A compressed derived table makes the complete aggregate constraints portable.
 rows=[dict(unit=u,start=y,end=y+1,class_from=a,class_to=b,area_ha=v)for u,flow in sorted(d.items())for(y,a,b),v in sorted(flow.items())]
 buffer=io.StringIO();wr=csv.DictWriter(buffer,list(rows[0]));wr.writeheader();wr.writerows(rows)
 (ROOT/f'data/{country}_annual_transition_capacities_F12.csv.gz').write_bytes(gzip.compress(buffer.getvalue().encode(),mtime=0))
 return dict(d),dict(allflow)


def solve(flow,forest,target,maximize=False):
 edges=sorted(flow);n=len(edges);require(n>0,'Empty flow network');capacities=np.array([flow[e]/SCALE for e in edges]);lower=np.zeros(n);upper=capacities.copy();objective=np.zeros(n);rr=[];cc=[];vv=[]
 nodes=sorted({(y+1,b)for(y,a,b)in edges if y<2022}|{(y,a)for(y,a,b)in edges if y>2015});ni={key:k for k,key in enumerate(nodes)}
 for k,(y,a,b)in enumerate(edges):
  if y==2015:
   if a in forest:lower[k]=capacities[k]
   else:upper[k]=0
  if y>2015:rr.append(ni[y,a]);cc.append(k);vv.append(-1.)
  if y<2022:rr.append(ni[y+1,b]);cc.append(k);vv.append(1.)
  if y==2022 and b in target:objective[k]=-1. if maximize else 1.
 A=coo_matrix((vv,(rr,cc)),shape=(len(nodes),n)).tocsr();rhs=np.zeros(len(nodes));result=linprog(objective,A_eq=A,b_eq=rhs,bounds=np.column_stack([lower,upper]),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 require(result.success,'Transition path LP failed: '+result.message)
 eq=float(np.max(np.abs(A@result.x),initial=0))*SCALE;bound=max(float(np.max(lower-result.x,initial=0)),float(np.max(result.x-upper,initial=0)))*SCALE
 dual=float(rhs@result.eqlin.marginals+lower@result.lower.marginals+upper@result.upper.marginals);gap=abs(float(result.fun)-dual)*SCALE
 l1eq=float(np.sum(np.abs(A@result.x)))*SCALE;source_l1=float(np.sum(np.abs(A@capacities)))*SCALE;bound_l1=float(np.sum(np.maximum(lower-result.x,0))+np.sum(np.maximum(result.x-upper,0)))*SCALE
 require(max(eq,bound,gap,l1eq+source_l1+bound_l1)<TOL_HA,'LP certificate exceeds hectare tolerance')
 mass0=sum(flow[e]for e in edges if e[0]==2015 and e[1]in forest);mass1=sum(result.x[k]*SCALE for k,e in enumerate(edges)if e[0]==2022)
 require(abs(mass1-mass0)<max(TOL_HA,len(nodes)*.0001),'Marked forest mass not conserved')
 value=float(result.fun)*SCALE*(-1 if maximize else 1)
 return value,dict(variables=n,conservation_constraints=len(nodes),max_conservation_residual_ha=eq,max_bound_violation_ha=bound,l1_conservation_residual_ha=l1eq,source_conservation_imbalance_l1_ha=source_l1,l1_bound_violation_ha=bound_l1,primal_dual_gap_ha=gap,marked_mass_initial_ha=mass0,marked_mass_terminal_ha=mass1,all_solver_constraints_satisfied=True),dict(x=result.x,eq_dual=result.eqlin.marginals,lo_dual=result.lower.marginals,hi_dual=result.upper.marginals)


def cases(country):
 if country=='BRA':
  form={3,5,6,49}
  return [('formations',form,'nonforest',None),('formations',form,'cropland',{39,20,40,62,41,46,47,35,48}),('formations_plus_savanna',form|{4,7},'nonforest',None),('formations_plus_savanna',form|{4,7},'cropland',{39,20,40,62,41,46,47,35,48})]
 return [('mapped_forest',{3,5,76},'nonforest',None),('mapped_forest',{3,5,76},'oil_palm',{35}),('mapped_forest',{3,5,76},'agriculture',{9,21,35,40})]


def run(bra,idn):
 bounds=[];certificates=[];count=0;witnesses={}
 for country,path in [('BRA',bra),('IDN',idn)]:
  units,national=extract(country,path);codes={a for y,a,b in national}|{b for y,a,b in national}
  for group,forest,target_name,provided in cases(country):
   target=codes-forest if provided is None else provided
   national_values=[];fine_values=[0.,0.]
   for mx in [False,True]:
    value,cert,witness=solve(national,forest,target,mx);key=f'lp_{count:04d}';witnesses.update({key+'_'+k:v for k,v in witness.items()});national_values.append(value);certificates.append(dict(witness_key=key,country=country,group=group,target=target_name,unit='national',optimization='max'if mx else'min',objective_ha=value,**cert));count+=1
    for u,flow in sorted(units.items()):
     value,cert,witness=solve(flow,forest,target,mx);key=f'lp_{count:04d}';witnesses.update({key+'_'+k:v for k,v in witness.items()});fine_values[int(mx)]+=value;certificates.append(dict(witness_key=key,country=country,group=group,target=target_name,unit=u,optimization='max'if mx else'min',objective_ha=value,**cert));count+=1
   require(fine_values[0]>=national_values[0]-len(units)*TOL_HA and fine_values[1]<=national_values[1]+len(units)*TOL_HA,'Finer geographic constraints did not tighten bounds')
   for label,values in [('national_aggregate',national_values),('finest_reported_geography',fine_values)]:
    # Outward numerical allowance per independent LP; endpoints remain conditional on maps.
    allowance=TOL_HA*(1 if label=='national_aggregate'else len(units));lo=max(0.,values[0]-allowance);hi=values[1]+allowance
    bounds.append(dict(country=country,initial_group=group,final_target=target_name,start=2015,end=2023,constraint_level=label,lower_unique_endpoint_area_ha=lo,upper_unique_endpoint_area_ha=hi,raw_lower_objective_ha=values[0],raw_upper_objective_ha=values[1],outward_numerical_allowance_ha=allowance,spatial_units=1 if label=='national_aggregate'else len(units),within_period_recurrence_possible=True,calibrated_true_conversion=False,associational_or_causal_effect=False))
    print(country,group,target_name,label,lo,hi,flush=True)
 np.savez_compressed(ROOT/'data/transition_path_primal_dual_witnesses_F12.npz',**witnesses)
 save('data/endpoint_conversion_path_bounds_F12.csv',bounds);save('data/transition_path_LP_certificates_F12.csv',certificates)
 summary=dict(method='Marked flow on layered annual class-transition network',LP_count=count,all_LPs_successful=True,max_conservation_residual_ha=max(r['max_conservation_residual_ha']for r in certificates),max_primal_dual_gap_ha=max(r['primal_dual_gap_ha']for r in certificates),numerical_tolerance_per_LP_ha=TOL_HA,geographic_constraints_never_weakened_bounds=True,sharp_for_aggregate_capacity_model_up_to_documented_source_and_solver_rounding=True,no_observed_pixel_trajectories_reconstructed=True,not_reference_calibrated=True,not_biomass=True,not_causal=True,estimand='Area mapped as initial group in 2015 and target in 2023, not first clearing, repeated event sum, or converted ecological capital')
 (ROOT/'metadata/transition_path_inference_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--brazil',type=Path,required=True);p.add_argument('--indonesia',type=Path,required=True);a=p.parse_args();run(a.brazil,a.indonesia)
