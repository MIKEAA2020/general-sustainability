import unittest,json,hashlib,sys,math
from pathlib import Path
from decimal import Decimal
import numpy as np,pandas as pd
from scipy.integrate import solve_ivp
from mpmath import iv,mp
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'inherited_v42/src'))
from local_verification_v42 import coefficients,frequency_records
from field_response_test_v43 import arrays,flow,metrics
from field_stock_and_closed_loop_v43 import stock_flow
from interval_fourier_residual_v43 import fft,padded
from interval_decimal_v42 import outward_bounds
D=lambda n:json.loads((ROOT/'data'/n).read_text())
def spectrum():return D('global_equilibrium_spectrum_v43.json')['records']
def formula(c,t):
 r=frequency_records(c);return 2+sum((-2 if i==0 else 2)*max(0,math.floor((t-x['tau'])*x['omega']/(2*math.pi))+1)for i,x in enumerate(r))
class GlobalBasinTests(unittest.TestCase):
 def test_point_gain(self):
  d=D('global_protective_basin_v43.json');e=coefficients()['E']*(1+np.log(2)/10);g=.001*100*e*(1+1/(1-.001*e/.02));self.assertLess(float(d['global_gain'][0]),g+1e-15);self.assertGreater(float(d['global_gain'][1]),g-1e-15);self.assertAlmostEqual(g,.4749970566879342,13)
 def test_box_constraints(self):
  d=D('global_protective_basin_v43.json');self.assertGreater(float(d['parameter_box_positive_stock_fraction'][0]),0);self.assertLess(float(d['parameter_box_global_gain'][1]),.686294);self.assertLess(2.4*1.08,26)
 def test_random_box_gains(self):
  rng=np.random.default_rng(43)
  for _ in range(2000):
   r,K,q,e,z=rng.uniform(.018,.022),rng.uniform(90,110),rng.uniform(.0009,.0011),rng.uniform(1.8,2.4),rng.uniform(.06,.08);e0=e*(1+z);g=q*K*e0*(1+1/(1-q*e0/r));self.assertLess(g,.686294)
 def test_log_mean_identity(self):
  rng=np.random.default_rng(44);ns=89.5518830113;es=(.02/.001)*(1-ns/100)
  for _ in range(100):
   n=rng.uniform(.001,100);e=rng.uniform(0,30);x=np.log(n/ns);a=.02/100*(n-ns)/x;self.assertGreaterEqual(a,.02/100*min(n,ns));self.assertLessEqual(a,.02/100*max(n,ns));self.assertAlmostEqual(-a*x-.001*(e-es),.02*(1-n/100)-.001*e,14)
 def test_quota_lipschitz(self):
  for z in np.linspace(0,500,100):self.assertLessEqual(abs(-2.235/(1+z)**2),2.235)
 def test_softplus_lipschitz(self):
  x=np.linspace(-100,100,5000);v=np.logaddexp(0,10*x)/10;self.assertTrue(np.all(abs(np.diff(v))<=np.diff(x)+1e-13));self.assertTrue(np.all(v>=0))
 def test_exact_review_convexity(self):
  for e,c in [(0,2.3),(29.999,2.3),(10,.001),(2,2)]:
   sol=solve_ivp(lambda t,x:[.914*(1-x[0]/30)*(c-x[0])],[0,8],[e],rtol=1e-11,atol=1e-12);v=sol.y[0,-1];self.assertGreaterEqual(v,min(e,c)-1e-10);self.assertLessEqual(v,max(e,c)+1e-10)
 def test_excluded_faces(self):
  d=D('global_protective_basin_v43.json');self.assertEqual(len(d['excluded_boundary_faces']),2);self.assertEqual(len(d['operators']),3);self.assertIn('explicit-Euler command map',d['not_transferred'])
class CompleteSpectrumTests(unittest.TestCase):
 def test_all_four_vectors(self):self.assertEqual(len(spectrum()),4)
 def test_window_counts(self):self.assertEqual([len(r['all_positive_delay_stability_windows'])for r in spectrum()],[2,2,1,1])
 def test_event_order(self):
  for r in spectrum():
   events=r['finite_events_to_prove_complete_stability_windows'];self.assertTrue(all(Decimal(a['tau_interval'][1])<Decimal(b['tau_interval'][0])for a,b in zip(events,events[1:])))
 def test_count_bookkeeping(self):
  for r in spectrum():
   n=2
   for e in r['finite_events_to_prove_complete_stability_windows']:self.assertEqual(e['RHP_count_before'],n);n+=e['root_count_change'];self.assertEqual(e['RHP_count_after'],n);self.assertGreaterEqual(n,0)
 def test_second_windows(self):self.assertEqual(formula(coefficients(),280),0);self.assertEqual(formula(coefficients(gated=False),270),0)
 def test_eventual_no_stability(self):
  for r in spectrum():
   c=coefficients(r['candidate'],r['gated']);cut=float(r['no_stable_delay_above'][1]);self.assertTrue(all(formula(c,t)>0 for t in np.linspace(cut+.01,100000,2000)))
 def test_winding_count_independent(self):
  # Independent numerical argument-principle diagnostic, not the theorem certificate.
  for r in spectrum():
   c=coefficients(r['candidate'],r['gated']);a,d,cc,k=-c['AN'],c['d'],-c['CE'],c['CZ']*c['BE'];R=math.sqrt(k)*1.3+.01;eps=1e-9;corners=[eps-1j*R,R-1j*R,R+1j*R,eps+1j*R,eps-1j*R];z=np.r_[np.concatenate([np.linspace(x,y,16384,endpoint=False)for x,y in zip(corners,corners[1:])]),corners[0]]
   for t in [1,50,200,280,400,1000]:
    zz=z.copy()
    for refinement in range(16):
     delta=(zz+a)*(zz+d)*(zz+cc)-k*zz*np.exp(-zz*t);phase=np.unwrap(np.angle(delta));changes=abs(np.diff(phase))
     if max(changes)<.4:break
     refined=[]
     for j in range(len(zz)-1):
      refined.append(zz[j])
      if changes[j]>=.4:refined.append((zz[j]+zz[j+1])/2)
     zz=np.r_[refined,zz[-1]]
    w=(phase[-1]-phase[0])/(2*np.pi);self.assertAlmostEqual(w,formula(c,t),7);self.assertLess(max(abs(np.diff(phase))),.4)
 def test_recurrent_transversality_identity(self):
  for r in spectrum():
   c=coefficients(r['candidate'],r['gated']);a,d,cc=-c['AN'],c['d'],-c['CE']
   for f in frequency_records(c):
    w=f['omega'];l=1j*w;v=[]
    for m in [0,1,4,100]:v.append((-(1/(l+a)+1/(l+d)+1/(l+cc)-1/l+f['tau']+2*np.pi*m/w)/l).real)
    self.assertLess(np.ptp(v),1e-8);self.assertEqual(np.sign(v[0]),np.sign(f['dRe_dtau']))
class InfiniteResidualTests(unittest.TestCase):
 def test_fft_exact_delta(self):
  iv.dps=40;r=fft([iv.mpc(1)]+[iv.mpc(0)]*7)
  for x in r:self.assertTrue(1 in x.real);self.assertTrue(0 in x.imag)
 def test_fft_roundtrip(self):
  a=[iv.mpc(i,i*i)for i in range(8)];b=fft(fft(a),True)
  for i,x in enumerate(b):self.assertTrue(i in x.real);self.assertTrue(i*i in x.imag)
 def test_fourier_input_frozen(self):
  f=D('fold_exact_fourier_inputs_v43.json')['records']
  for r in D('interval_fourier_residual_v43.json')['records']:
   for key in f[r['fold']]:self.assertEqual(f[r['fold']][key],r[key])
 def test_polynomial_degrees(self):
  for r in D('interval_fourier_residual_v43.json')['records']:
   for key in ['polynomial_U_exact_decimal_coefficients','polynomial_V_exact_decimal_coefficients']:
    for c in r[key]:self.assertEqual(len(c['a']),128);self.assertEqual(len(c['b']),128)
 def test_nonzero_normalization(self):
  for r in D('interval_fourier_residual_v43.json')['records']:self.assertGreater(abs(float(r['polynomial_V_exact_decimal_coefficients'][0]['a'][0])),.1)
 def test_residual_upper_bounds(self):
  for r in D('interval_fourier_residual_v43.json')['records']:
   self.assertLess(max(map(float,r['residual_weighted_l1_component_upper_bounds'])),4e-10);self.assertLess(max(map(float,r['null_residual_weighted_l1_component_upper_bounds'])),7e-12);self.assertEqual(r['nfft'],4096)
 def test_phase_residuals(self):
  for r in D('interval_fourier_residual_v43.json')['records']:
   b=abs(Decimal(r['polynomial_U_exact_decimal_coefficients'][0]['b'][0]))/2;self.assertGreaterEqual(Decimal(r['phase_residual_upper_bound']),b)
 def test_analytic_strip(self):
  for r in D('fold_continuum_stage_v43.json')['records']:
   if r['nodes']==257:
    s=r['analytic_tails']['accepted_strips'][-1];self.assertLess(float(s['softplus_imaginary_argument_bound'][1]),np.pi/2);self.assertGreater(float(s['rational_denominator_real_lower_bound'][0]),0);self.assertEqual(len(s['complex_null_rhs_bounds']),3)
 def test_odd_grid_convergence(self):
  r=D('fold_continuum_stage_v43.json')['records'];up=[x for x in r if x['fold']=='upper'];v=[max(x['physical_orbit_defect'])for x in up];self.assertGreater(v[0],v[1]);self.assertGreater(v[1],v[2]);self.assertTrue(all(x['nodes']%2 for x in r))
 def test_finite_continuum_discrepancy(self):
  r=[x for x in D('fold_continuum_stage_v43.json')['records']if x['fold']=='upper'and x['nodes']==257][0];self.assertGreater(abs(r['tau']-64.40232720337),5e-7)
 def test_alias_bound_example(self):
  L=16;alpha=.05;M=1/(2-np.cosh(2*np.pi*alpha));x=np.arange(L)/L;y=1/(2-np.cos(2*np.pi*x));hat=np.fft.fft(y)/L;rho=2-np.sqrt(3)
  for k in range(-7,8):self.assertLessEqual(abs(hat[k%L]-rho**abs(k)/np.sqrt(3)),2*M*np.exp(-2*np.pi*alpha*(L-abs(k)))/(1-np.exp(-2*np.pi*alpha*L)))
 def test_outward_serialization(self):
  iv.dps=50;x=iv.mpf(1)/3;lo,hi=outward_bounds(x);self.assertLessEqual(Decimal(lo)*3,1);self.assertGreaterEqual(Decimal(hi)*3,1)
 def test_no_existence_claim(self):self.assertIn('NOT a continuum fold existence certificate',D('interval_fourier_residual_v43.json')['status'])
class FieldTests(unittest.TestCase):
 def test_raw_hash(self):
  x=D('field_response_test_v43.json');self.assertEqual(hashlib.sha256((ROOT/'data/ICES_SAG_StockDownload_19373_raw_v43.json').read_bytes()).hexdigest(),x['source']['raw_sha256'])
 def test_temporal_support(self):
  x=D('field_response_test_v43.json');self.assertEqual(x['splits']['training_target_years'],[1960,1994])
  for s in x['scenarios'].values():
   for r in s.values():self.assertEqual(r['n_pretest'],50);self.assertEqual(r['test_years'],list(range(2010,2025)))
 def test_candidate_count(self):
  g=pd.read_csv(ROOT/'data/field_validation_grid_v43.csv');self.assertEqual(len(g),520)
 def test_selection_only_validation(self):
  g=pd.read_csv(ROOT/'data/field_validation_grid_v43.csv');x=D('field_response_test_v43.json')
  for law,r in x['selected_hyperparameters'].items():self.assertAlmostEqual(r['validation_RMSE'],g[g.law==law].validation_RMSE.min(),13)
 def test_recomputed_metrics(self):
  a=pd.read_csv(ROOT/'data/field_test_predictions_v43.csv');x=D('field_response_test_v43.json')
  for(s,law),g in a.groupby(['scenario','law']):self.assertAlmostEqual(metrics(g.observed_target_proxy,g.prediction)['RMSE'],x['scenarios'][s][law]['RMSE'],13)
 def test_common_baseline(self):
  r=D('field_response_test_v43.json')['scenarios']['TBiomass'];np.testing.assert_allclose(r['mobilising']['AR1']['coefficients'],r['protective']['AR1']['coefficients'],atol=1e-14)
 def test_future_predictor_nonleakage(self):
  df=pd.read_csv(ROOT/'data/herring_assessment_clean_v43.csv');a,_=arrays(df,.25,2);df.loc[df.Year>=2010,'TBiomass']*=10;df.loc[df.Year>=2010,'Catches']*=5;b,_=arrays(df,.25,2);np.testing.assert_allclose(a[a[:,1]==2010,:4],b[b[:,1]==2010,:4])
 def test_numerical_resolution(self):
  for s in D('field_response_test_v43.json')['scenarios'].values():
   for r in s.values():self.assertLess(r['numerical_step_halving_max_difference'],1e-11);self.assertEqual(r['predicted_outside_invariant_interval'],0)
 def test_response_negative_and_small_gain(self):
  r=D('field_response_test_v43.json')['scenarios']['TBiomass'];self.assertTrue(r['mobilising']['near_parameter_bound']);self.assertGreater(r['mobilising']['RMSE_ratio_to_AR1'],1);self.assertGreater(r['protective']['RMSE_ratio_to_AR1'],.99);self.assertLess(r['protective']['RMSE_ratio_to_AR1'],1)
 def test_stock_flow_exactness(self):
  for p in [[.65,.33,.36],[.4,.23,.35,.1]]:
   for u in [.1,1,4]:
    rr=.7 if len(p)==4 else None;v=stock_flow(np.array([1.2]),np.array([u]),np.array(p),None if rr is None else np.array([rr]))[0];sol=solve_ivp(lambda t,n:(p[0]-p[2]*u)*n-p[1]*n*n+(p[3]*rr if rr else 0),[0,1],[1.2],rtol=1e-12,atol=1e-13);self.assertAlmostEqual(v,sol.y[0,-1],10);self.assertGreater(v,0)
 def test_ecological_negative_endpoints(self):
  for r in D('field_stock_and_recursive_v43.json')['one_step_test'].values():self.assertGreater(r['RMSE_ratio_to_persistence'],1);self.assertGreater(r['RMSE_ratio_to_AR1'],1)
 def test_recursive_negative_stock(self):
  for r in D('field_stock_and_recursive_v43.json')['recursive_test'].values():self.assertGreater(r['stock_RMSE_ratio_to_VAR1'],1);self.assertGreater(r['stock_RMSE_ratio_to_constant_persistence'],1);self.assertEqual(r['domain_violations'],0)
 def test_recursive_no_future_inputs(self):self.assertFalse(D('field_stock_and_recursive_v43.json')['future_observed_stock_catch_recruitment_used'])
 def test_protocol_deviation_retained(self):
  self.assertTrue((ROOT/'data/initial_unequal_support_field_response_test_v43.json').exists());self.assertIn('after inspecting',D('field_response_test_v43.json')['protocol_amendment'])
class PreservationTests(unittest.TestCase):
 def test_inherited_bytes(self):
  m=json.loads((ROOT/'inherited_v42/MANIFEST_GOVERNANCE_P4_v42_P01.json').read_text())
  for r in m['files']:self.assertEqual(hashlib.sha256((ROOT/'inherited_v42'/r['path']).read_bytes()).hexdigest(),r['sha256'])
 def test_author_declaration_keywords(self):
  s=(ROOT/'manuscript/paper4_delay_dynamics_v43.tex').read_text();self.assertIn('https://orcid.org/0000-0002-0019-1842',s);self.assertIn('Arena.ai Agent Mode was used to assist with computational methods and literature review.',s);self.assertIn('institutional feedback;',s)
 def test_all_new_sections(self):
  s=(ROOT/'manuscript/paper4_delay_dynamics_v43.tex').read_text();self.assertIn('Theorem 5.2',s);self.assertIn('Theorem 7.5',s);self.assertIn('8.7 Infinite-series',s);self.assertIn('Quantitative dynamic field tests',s)
 def test_no_stale_residual_open_claim(self):
  s=(ROOT/'manuscript/paper4_delay_dynamics_v43.tex').read_text();self.assertNotIn('residual stage remains unimplemented',s);self.assertNotIn('continuum off-grid residual stage is still open',s);self.assertNotIn('continuum off-grid\nresidual stage and the continuous-delay lift remain open',s)
 def test_analogy_preserved(self):
  old=(ROOT/'inherited_v42/manuscript/paper4_delay_dynamics_v42.tex').read_text();new=(ROOT/'manuscript/paper4_delay_dynamics_v43.tex').read_text();a=old.index('The overshoot mechanism analysed throughout');b=old.index('The hen\'s loop',a);self.assertIn(old[a:b],new)
 def test_prior_figures_identical(self):
  for name in ['fig1_global_topology','fig2_upper_branch','fig3_waveform_match']:self.assertEqual((ROOT/'inherited_v42/figures'/f'{name}_v42.png').read_bytes(),(ROOT/'figures'/f'{name}_v43.png').read_bytes())
if __name__=='__main__':unittest.main()
