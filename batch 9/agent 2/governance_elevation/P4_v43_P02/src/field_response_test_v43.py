"""Locked blocked retrospective field test of two observed-signal response laws.
NOT a fit/validation of the autonomous stock-memory-effort DDE.
"""
from pathlib import Path
import json,itertools,time,hashlib
import numpy as np,pandas as pd
from scipy.optimize import least_squares,nnls
from numba import njit
ROOT=Path(__file__).resolve().parents[1]
@njit(cache=True)
def flow(u,z,eta,second,M,protective,steps=64):
    out=u.copy();h=1./steps
    for i in range(len(u)):
        x=u[i];zz=z[i]
        for _ in range(steps):
            def f(x):
                if protective:return(1-x/M)*eta*(second*M/(1+zz)-x)
                return(1-x/M)*(eta*x*(zz-x/M)+second*zz/(1+zz))
            a=f(x);b=f(x+h*a/2);c=f(x+h*b/2);d=f(x+h*c);x+=h*(a+2*b+2*c+d)/6
        out[i]=x
    return out

def arrays(df,tm,lag,biomass='TBiomass',scales=None):
    b=df[biomass].to_numpy(float);catch=df.Catches.to_numpy(float);years=df.Year.to_numpy(int)
    train=(years>=1950)&(years<=1994)
    if scales is None:scales=[float(np.nanmedian(b[train])),float(np.nanmedian(catch[train]))]
    N=b/scales[0];U=(catch/scales[1])/N;signal=np.logaddexp(0,10*np.r_[0,N[:-1]-N[1:]])/10;z=np.empty(len(N));z[0]=np.log(2)/10;alpha=np.exp(-1/tm)
    for i in range(1,len(z)):z[i]=alpha*z[i-1]+(1-alpha)*signal[i]
    rows=[]
    for i in range(1,len(N)-1):
        if i-lag<0 or years[i+1]>2024:continue
        if np.isfinite(U[i])and np.isfinite(U[i+1])and np.isfinite(z[i-lag]):rows.append([years[i],years[i+1],U[i],z[i-lag],U[i+1]])
    return np.array(rows),scales

def fit(a,M,protective):
    u,z,target=a[:,2],a[:,3],a[:,4];gate=1-u/M
    if protective:
        ab=nnls(np.column_stack([gate/(1+z),-gate*u]),target-u)[0];eta=max(1e-4,min(15,ab[1]));fraction=np.clip(ab[0]/max(eta*M,1e-12),.001,.999)
        initial=[eta,fraction];bounds=([1e-7,1e-6],[20,.999999])
    else:
        ab=nnls(np.column_stack([gate*u*(z-u/M),gate*z/(1+z)]),target-u)[0];initial=np.clip(ab,[1e-6,1e-7],[15,15]);bounds=([1e-7,1e-8],[20,20])
    def fun(p):
        y=flow(u,z,p[0],p[1],M,protective)
        if not np.isfinite(y).all():return np.full(len(u),1e6)
        return y-target
    opt=least_squares(fun,initial,bounds=bounds,max_nfev=100,ftol=1e-9,xtol=1e-9,gtol=1e-9)
    return opt.x,float(np.sqrt(np.mean(fun(opt.x)**2))),bool(opt.success)

def metrics(y,p):return {'RMSE':float(np.sqrt(np.mean((p-y)**2))),'MAE':float(np.mean(abs(p-y))),'bias':float(np.mean(p-y))}

def run():
    raw=ROOT/'data/ICES_SAG_StockDownload_19373_raw_v43.json';df=pd.DataFrame(json.loads(raw.read_text()))
    for c in ['Year','TBiomass','Low_TBiomass','High_TBiomass','Catches','FishingPressure','Recruitment']:df[c]=pd.to_numeric(df[c],errors='coerce')
    df=df.sort_values('Year');central,scales=arrays(df,1,0);grids=[];selected={};t0=time.time()
    for protective in [False,True]:
        best=None;label='protective'if protective else'mobilising'
        for tm,lag,mult in itertools.product([.25,1,2,5,10],range(13),[1.05,1.5,2,4]):
            a,_=arrays(df,tm,lag,scales=scales);train=a[(a[:,1]>=1960)&(a[:,1]<=1994)];val=a[(a[:,1]>=1995)&(a[:,1]<=2009)];M=mult*float(max(train[:,2].max(),train[:,4].max()));p,loss,ok=fit(train,M,protective);pred=flow(val[:,2],val[:,3],p[0],p[1],M,protective);vl=metrics(val[:,4],pred)['RMSE'];row={'law':label,'memory':tm,'lag':lag,'ceiling_multiplier':mult,'training_RMSE':loss,'validation_RMSE':vl,'fit_success':ok,'parameters':p.tolist()};grids.append(row)
            if ok and np.isfinite(vl)and(best is None or vl<best['validation_RMSE']):best=row.copy()
        if best is None:raise ValueError('No converged candidate')
        selected[label]=best;print('Selected',label,json.dumps(best),'seconds',time.time()-t0,flush=True)
    details=[];results={};scenarios=['TBiomass','Low_TBiomass','High_TBiomass']
    for column in scenarios:
        scenario={}
        for label,best in selected.items():
            protective=label=='protective';a,_=arrays(df,best['memory'],best['lag'],column,scales);pre=a[(a[:,1]>=1960)&(a[:,1]<=2009)];test=a[(a[:,1]>=2010)&(a[:,1]<=2024)];M=best['ceiling_multiplier']*float(max(pre[:,2].max(),pre[:,4].max()));p,loss,ok=fit(pre,M,protective);pred=flow(test[:,2],test[:,3],p[0],p[1],M,protective);fine=flow(test[:,2],test[:,3],p[0],p[1],M,protective,128)
            ar=np.linalg.lstsq(np.column_stack([np.ones(len(pre)),pre[:,2]]),pre[:,4],rcond=None)[0];ar_pred=ar[0]+ar[1]*test[:,2];persistence=test[:,2]
            met=metrics(test[:,4],pred);mp=metrics(test[:,4],persistence);ma=metrics(test[:,4],ar_pred);met.update({'RMSE_ratio_to_persistence':met['RMSE']/mp['RMSE'],'RMSE_ratio_to_AR1':met['RMSE']/ma['RMSE'],'beats_both_baselines':met['RMSE']<min(mp['RMSE'],ma['RMSE']),'parameters':p.tolist(),'effort_ceiling':M,'training_refit_RMSE':loss,'test_years':test[:,1].astype(int).tolist(),'n_pretest':len(pre),'n_test':len(test),'numerical_step_halving_max_difference':float(max(abs(pred-fine))),'predicted_outside_invariant_interval':int(np.sum((pred<0)|(pred>M))),'test_origin_outside_model_ceiling':int(np.sum(test[:,2]>=M)),'test_target_outside_model_ceiling':int(np.sum(test[:,4]>=M)),'fit_success':ok,'near_parameter_bound':bool(p[0]<1e-5 or p[0]>19.9 or (not protective and(p[1]<1e-6 or p[1]>19.9))or(protective and(p[1]<1e-4 or p[1]>.999))),'persistence':mp,'AR1':{**ma,'coefficients':ar.tolist()}});scenario[label]=met
            for row,pp,ap in zip(test,pred,ar_pred):details.append({'scenario':column,'law':label,'origin_year':int(row[0]),'target_year':int(row[1]),'current_proxy':row[2],'delayed_memory':row[3],'observed_target_proxy':row[4],'prediction':pp,'persistence_prediction':row[2],'AR1_prediction':ap})
        results[column]=scenario
    pd.DataFrame(details).to_csv(ROOT/'data/field_test_predictions_v43.csv',index=False);pd.DataFrame(grids).to_csv(ROOT/'data/field_validation_grid_v43.csv',index=False)
    clean=df[['Year','TBiomass','Low_TBiomass','High_TBiomass','Catches','FishingPressure','Recruitment']].copy();clean['role']=np.where(clean.Year>=2025,'excluded_terminal_row',np.where(clean.Year<1960,'memory_warmup',np.where(clean.Year<=1994,'training',np.where(clean.Year<=2009,'validation','test'))));clean.to_csv(ROOT/'data/herring_assessment_clean_v43.csv',index=False)
    out={'protocol_amendment':'Common support starts in 1960 so all delay candidates have observed predictor history; initial unequal-support run retained separately; correction made after inspecting initial results, not presented as a preregistration','status':'Blocked retrospective assessment-based test of the observed-signal governance RESPONSE COMPONENT; not autonomous DDE validation or causal identification','source':{'stock':'her.27.3a47d','assessment_year':2025,'assessment_key':19373,'url':'https://sag.ices.dk/SAG_API/api/StockDownload?assessmentKey=19373','raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'reported_stock_size':'SSB','chosen_stock_observable':'TBiomass, not StockSize/SSB','total_biomass_unit_metadata':'blank; not imputed','catch_unit_metadata':'tonnes','catch_intensity_proxy':'U=(C/C_training_median)/(TBiomass/B_training_median); dimensionless and invariant to separate unit rescalings','reported_F_age':'2-6; not substituted for total-stock removal'},'reference_scales':{'biomass_training_median':scales[0],'catch_training_median':scales[1]},'splits':{'training_target_years':[1960,1994],'validation_target_years':[1995,2009],'test_target_years':[2010,2024],'terminal_2025_excluded':True},'selection':'fit two coefficients on training; select memory/lag/ceiling by validation RMSE; refit two coefficients pretest; never select on test','candidate_count_per_law':260,'selected_hyperparameters':selected,'scenarios':results,'scenario_scope':'Low/high biomass paths are stress scenarios, not joint confidence sets or independent observations','limitations':['catch intensity is a derived proxy, not directly observed institutional effort','stock/catch estimates share a retrospective age-structured assessment','a single revised assessment vintage is not a real-time hindcast','the endogenous ecological equation, recruitment/environmental alternatives and latent institution are not jointly validated','selected lags are predictive tuning values, not identified deployment delays'],'seconds':time.time()-t0}
    (ROOT/'data/field_response_test_v43.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));return out
if __name__=='__main__':run()
