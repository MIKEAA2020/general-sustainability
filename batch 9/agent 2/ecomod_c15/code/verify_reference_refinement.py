"""Reproduce the fixed-demand reference-grid diagnostics stated in main and SI."""
from pathlib import Path
import json,numpy as np
import simulate_budgets as model
ROOT=Path(__file__).resolve().parents[1]

def main():
    case=model.CASES[0]
    reference_dt=.003125
    _,reference,_,_=model.simulate(case,reference_dt)
    results=[]
    for dt in [.05,.025]:
        _,state,_,_=model.simulate(case,dt)
        error=np.max(np.abs(state-reference[::round(dt/reference_dt)]),axis=0)
        results.append(dict(dt_yr=dt,reference_dt_yr=reference_dt,
                            max_Ac_difference_ha=float(error[1]),
                            max_B_difference_gha=float(error[6]),
                            max_P_difference_persons=float(error[3]),
                            max_D_difference_gha_yr=float(error[4])))
    assert abs(results[0]['max_P_difference_persons']-.00024493384231494275)<1e-12
    assert abs(results[1]['max_P_difference_persons']-.00011444148150774325)<1e-12
    # The exact baseline quality path is min(1, q0+v*t).
    q0=.9;velocity=.08*q0*(1-q0);contact=(1-q0)/velocity
    quality=[]
    for dt in [.1,.0125]:
        left=np.floor(contact/dt)*dt;right=left+dt
        qleft=q0+velocity*left
        at_contact=qleft+(1-qleft)*(contact-left)/(right-left)
        quality.append(dict(dt_yr=dt,maximum_piecewise_linear_contact_error=float(1-at_contact)))
    for name in ['ecomod_main.tex','ecomod_supplement.tex']:
        text=(ROOT/name).read_text()
        assert '$0.000245$' in text and '$0.000114$' in text
        assert r'8.9\times10^{-6}' in text
    output=dict(case=case,comparison='Maximum absolute differences at matching reference-grid times',
                reference_results=results,quality_contact_results=quality,
                scope='The stated fixed-demand numerical comparison; not an additional delay-history experiment')
    (ROOT/'metadata/reference_refinement.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
