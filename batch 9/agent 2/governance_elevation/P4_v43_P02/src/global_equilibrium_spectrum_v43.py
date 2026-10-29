"""All-positive-delay characteristic-root count from exhaustive frequencies.
Uses the analytic root-count theorem, not a truncated root search.
"""
from pathlib import Path
import json,sys,math
from mpmath import mp,iv
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'inherited_v42/src'))
from interval_decimal_v42 import outward_bounds

def run():
    mp.dps=90;iv.dps=80;source=json.loads((ROOT/'inherited_v42/data/all_scalar_hopf_v42.json').read_text())['records'];out=[]
    def lo(x):return mp.mpf(x._mpi_[0])
    def hi(x):return mp.mpf(x._mpi_[1])
    for candidate in ['A','B']:
      for gated in [True,False]:
        f=lambda s:iv.mpf(str(s));eta=f('.914'if candidate=='A'else'2.756');M=f(30 if candidate=='A'else 26);z=iv.log(f(2))/10;aa=M*z;bb=M*f('.01')*z/(eta*(1+z));E=(aa+iv.sqrt(aa*aa+4*bb))/2;N=100*(1-E/20);a=f('.02')*N/100;d=f('.2');BE=f('.001')*N/10;g=1-E/M if gated else f(1);c=-g*eta*(z-2*E/M);CZ=g*(eta*E+f('.01')/(1+z)**2);k=CZ*BE
        p2=a+d+c;p1=a*d+a*c+d*c-k;p0=a*d*c;rh=p2*p1-p0
        if not(lo(a)>0 and lo(c)>0 and lo(p2)>0 and lo(p0)>0 and hi(rh)<0):raise ValueError('Undelayed Routh count failed')
        rr=[r for r in source if r['candidate']==candidate and r['gated']==gated];low,high=rr;wm=iv.mpf(low['omega_enclosure']);wp=iv.mpf(high['omega_enclosure']);tm=iv.mpf(low['tau_enclosure']);tp=iv.mpf(high['tau_enclosure']);Pm=2*iv.pi/wm;Pp=2*iv.pi/wp
        def Hp(x):return(x+d*d)*(x+c*c)+(x+a*a)*(x+c*c)+(x+a*a)*(x+d*d)-k*k
        if not(hi(Hp(wm*wm))<0 and lo(Hp(wp*wp))>0):raise ValueError('All-recurrence crossing directions failed')
        cutoff=(tp/Pp-tm/Pm)/(1/Pp-1/Pm)
        upper_stop=int(mp.ceil(hi(cutoff)))+1;events=[]
        for direction,tau,period in [(-2,tm,Pm),(2,tp,Pp)]:
            for j in range(int(upper_stop/float(lo(period)))+3):
                t=tau+j*period
                if lo(t)>upper_stop:break
                events.append({'family':'lower'if direction<0 else'upper','recurrence':j,'tau_interval':outward_bounds(t),'root_count_change':direction})
        events.sort(key=lambda r:mp.mpf(r['tau_interval'][0]));count=2;stable=[];start=None
        for i,event in enumerate(events):
            if i and mp.mpf(events[i-1]['tau_interval'][1])>=mp.mpf(event['tau_interval'][0]):raise ValueError('Finite event ordering unresolved')
            before=count;count+=event['root_count_change']
            if count<0:raise ValueError('Negative root count')
            event['RHP_count_before']=before;event['RHP_count_after']=count
            if count==0:start=event['tau_interval']
            elif before==0:stable.append({'left_Hopf_interval':start,'right_Hopf_interval':event['tau_interval'],'endpoints_excluded':True})
        out.append({'candidate':candidate,'gated':gated,'Routh_p2p1_minus_p0':outward_bounds(rh),'undelayed_RHP_count':2,'uniform_RHP_root_radius_bound':outward_bounds(iv.sqrt(k)),'no_stable_delay_above':outward_bounds(cutoff),'finite_events_to_prove_complete_stability_windows':events,'all_positive_delay_stability_windows':stable,'count_formula':'U(tau)=2-2 N_lower(tau)+2 N_upper(tau); N_j counts tau_j+2 pi k/omega_j strictly below tau','asymptotic_unstable_root_growth_slope':outward_bounds((wp-wm)/iv.pi)})
    result={'status':'Complete characteristic-root count on the full positive delay axis at the four fixed registered vectors, via exhaustive imaginary frequencies, Routh count and invariant crossing directions','not_claimed':'Nonlinear mobilising basin completeness or the full Floquet spectrum of non-equilibrium periodic orbits','theorem_identity':'Re[(d lambda/d tau)^(-1)] = H_prime(omega^2)/abs(P(i omega))^2','records':out}
    (ROOT/'data/global_equilibrium_spectrum_v43.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return result
if __name__=='__main__':run()
