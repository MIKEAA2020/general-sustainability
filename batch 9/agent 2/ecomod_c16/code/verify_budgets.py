"""Check model outputs; --full additionally recomputes all 28 trajectories in memory.
Writes data/model_independent_checks.json. No network and no inherited-figure rerun.
The word 'independent' refers to algebra/check paths and endpoint-vs-quadrature
comparisons, not to an independent software team or empirical validation.
"""
from pathlib import Path
import argparse
import csv
import json
import math
import numpy as np
import simulate_budgets as m

P=Path(__file__).resolve().parents[1]

def rows(path):
    return list(csv.DictReader((P/path).open()))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args()
    b,w,info=m.identification()
    assert info['known_q']==.9
    recorded=rows('data/model_identification_bounds.csv')
    for x,y in zip(b,recorded):
        for key in ['lower_Ac_ha','upper_Ac_ha','width_ha']:assert abs(x[key]-float(y[key]))<1e-12
    # Separate scalar algebra: chain rule versus five signed RHS channels.
    rng=np.random.default_rng(13029);worst=0.
    for _ in range(1000):
        Af,Ac,Ar=rng.dirichlet([2,2,2])*2.5
        q=rng.uniform(.01,.99);dq=rng.uniform(-.03,.03);bf=rng.uniform(.2,1.9)
        uc,R=rng.uniform(0,.1,2);D,dD=rng.uniform(0,.5),rng.uniform(-.1,.1)
        tbprime=rng.uniform(0,.025);u=.05+.064*q*(1-q);up=.064*(1-2*q)
        dbf=math.exp(-.03*D)*tbprime-.03*bf*dD
        M=.06*Ar-.05*Af
        chain=dbf*Af+bf*(uc+M)+up*dq*Ac+u*(-uc+R)
        channels=(bf-u)*uc+bf*M+u*R+up*Ac*dq+Af*dbf
        worst=max(worst,abs(chain-channels))
    assert worst<1e-12
    r=rows('data/model_budget_refinement.csv');assert len(r)==28
    fine={x['case']:x for x in r if float(x['dt_yr'])==m.DTS[-1]}
    assert set(fine)=={c['id']for c in m.CASES}
    for x in r:
        sums=sum(float(x[t+'_gha'])for t in m.TERMS)
        assert abs(sums-float(x['integral_sum_gha']))<1e-12
        assert abs(float(x['delta_B_gha'])-sums-float(x['closure_residual_gha']))<1e-12
        assert abs(float(x['technology_subterm_gha'])+float(x['debt_subterm_gha'])-float(x['fast_yield_gha']))<1e-10
        assert float(x['other_state_clips'])==0 and float(x['quality_ceiling_clips'])==1
        assert float(x['conversion_availability_limiter_nodes'])==0
        assert float(x['minimum_Ar_ha'])>.1
        assert float(x['max_area_balance_error_ha'])<1e-12
    monotone={}
    for case in m.CASES:
        group=[x for x in r if x['case']==case['id']]
        errors=[abs(float(x['closure_residual_gha']))for x in group]
        monotone[case['id']]=all(a>b for a,b in zip(errors,errors[1:]))
        assert monotone[case['id']]
        assert float(group[-1]['relative_closure_abs'])<.001
    # Verify endpoint and cumulative exports against the actual finest quadrature.
    endpoints={};counts={}
    for x in rows('data/model_trajectories_reporting_grid.csv'):
        endpoints[x['case']]=x;counts[x['case']]=counts.get(x['case'],0)+1
    for case in m.CASES:
        x=endpoints[case['id']];ref=fine[case['id']]
        assert counts[case['id']]==round(case['T']/.05)+1
        assert abs(float(x['B'])-float(ref['BT_gha']))<1e-10
        assert abs(float(x['Ac'])-float(ref['final_Ac_ha']))<1e-10
        for term in m.TERMS:assert abs(float(x['cum_'+term+'_gha'])-float(ref[term+'_gha']))<1e-10
    # Retained specified check at the original reported wave step.
    wave=[]
    for case,target,time in [(m.CASES[2],.008126,86.15),(m.CASES[3],.020205,115.60)]:
        _,_,_,res=m.simulate(case,.05)
        assert abs(res['peak_D_gha_yr']-target)<.0000006
        assert abs(res['peak_D_time_yr']-time)<1e-10
        wave.append(dict(case=case['id'],peak=res['peak_D_gha_yr'],time=res['peak_D_time_yr']))
    recomputed=0
    if args.full:
        for x in r:
            case=next(c for c in m.CASES if c['id']==x['case']);_,_,_,check=m.simulate(case,float(x['dt_yr']))
            for k,v in check.items():
                if k!='case':assert abs(float(x[k])-v)<1e-10,(x['case'],x['dt_yr'],k)
            recomputed+=1
    report=dict(status='PASS',static_bounds_match=True,endpoint_witnesses_reconstruct_B=True,
                synthetic_chain_rule_samples=1000,max_chain_rule_discrepancy=worst,
                budget_rows_checked=len(r),finest_cases=len(fine),strictly_decreasing_closure_abs=monotone,
                all_finest_relative_closure_below_0_001=True,all_selected_bounds_and_guards_pass=True,
                trajectory_export_counts=counts,wave_coarse_step_checks=wave,full_in_memory_trajectory_recomputations=recomputed,
                scope_exclusions=['No empirical physical-stock identification','Numerical results are conditional on the specified histories and delays','Numerical verification covers the stated contribution-budget calculations'])
    (P/'data/model_independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
