"""Interval constants for the analytical L-infinity small-gain proof.
The proof, not a time-grid search, establishes all-cadences stability.
No empirical parameter uncertainty is implied by the illustrative parameter box.
"""
from pathlib import Path
import json
from mpmath import mp,iv
from interval_decimal_v42 import outward_bounds
ROOT=Path(__file__).resolve().parents[1]

def run():
    mp.dps=90;iv.dps=80;f=lambda s:iv.mpf(str(s))
    z=iv.log(f(2))/10;aa=30*z;bb=30*f('.01')*z/(f('.914')*(1+z));E=(aa+iv.sqrt(aa*aa+4*bb))/2;N=100*(1-E/20);a=f('.02')*N/100;d=f('.2');BE=f('.001')*N/10
    gamma=2*BE/d*iv.exp(iv.log(a/d)*a/(d-a));ratio=E/(1+z);mu=gamma*ratio
    if mp.mpf(mu._mpi_[1])>=1:raise ValueError('No strict protective gain margin')
    theta=f('.57');theta_gain=mu/(2*theta-1)
    # A deliberately broad mathematical box; no claimed measurement confidence set.
    r=iv.mpf(['.018','.022']);K=iv.mpf(['90','110']);q=iv.mpf(['.0009','.0011']);estar=iv.mpf(['1.8','2.4']);delta=iv.mpf(['.06','.08'])
    amin=r-q*estar;robust=q*K*estar/(1+delta)
    if mp.mpf(amin._mpi_[0])<=0 or mp.mpf(robust._mpi_[1])>=1:raise ValueError('Parameter box not certified')
    E0=E*(1+z);stock_floor=100*(1-f('.001')*E0/f('.02'));box_E0=estar*(1+delta);box_floor=K*(1-q*box_E0/r)
    out={'nonlinear_parameter_box_additional_restriction':'E_max in [26,34] (in particular greater than every quota cap in this box)','nonlinear_quota_E0':outward_bounds(E0),'nonlinear_invariant_stock_floor':outward_bounds(stock_floor),'parameter_box_nonlinear_floor':outward_bounds(box_floor),'nonlinear_scope':'For 0<=E_initial<=E0<Emax, N_initial>=stock_floor and Z history>=0, the stock floor is invariant for continuous protective delay, native ZOH and the exact nonlinear frozen-effort quota review, at every fixed finite cadence and delay.','method':'Analytic impulse-response L1 norm followed by L-infinity small gain; interval evaluation of constants','ecological_transfer':'G(s)=B_E s/[(s+a)(s+d)]','gamma_formula':'2 B_E/d * (a/d)^[a/(d-a)], with continuous value 2 B_E/(a exp(1)) at a=d','gamma':outward_bounds(gamma),'quota_slope_to_damping':outward_bounds(ratio),'mu_gamma_times_k_over_c':outward_bounds(mu),'theta_0p57_uniform_gain_bound':outward_bounds(theta_gain),'theorem_scope':['protective endpoint: all eta_p>0 at the same equilibrium','continuous pure deployment delay: every fixed finite delay','native signal ZOH: every fixed finite review interval, with any fixed finite additional measurement latency','exact frozen-effort review: every fixed positive review interval','theta reviewed frozen effort: all intervals for theta>=0.57'],'not_claimed':['global nonlinear convergence','mixed mobilising-protective all-delay stability','uniform exponential decay rate as delay/cadence tend to infinity','empirical calibration of the mathematical parameter box'],'parameter_box':{'r':[.018,.022],'K':[90,110],'q':[.0009,.0011],'E_star':[1.8,2.4],'delta':[.06,.08],'Z_ref':1,'E_max':'any > E_star','tau_m':'any > 0','eta_p':'any > 0'},'parameter_box_a_lower_bound':outward_bounds(amin),'parameter_box_gain_upper_bound':outward_bounds(robust)}
    (ROOT/'data/protective_all_cadences_v42.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out
if __name__=='__main__':run()
