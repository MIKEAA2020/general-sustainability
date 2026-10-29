import unittest,json,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.linalg import expm
from periodic_orbits_v42 import field,physical,from_physical,Collocation,resize
from local_verification_v42 import coefficients,protective,hold_matrix,monodromy
ROOT=Path(__file__).resolve().parents[1]
def data(name):return json.loads((ROOT/'data'/name).read_text())
class ElevationTests(unittest.TestCase):
    def test_coordinate_roundtrip(self):
        y=np.array([[1,.01,.001],[90,.07,2],[38,1.3,29.91]]);np.testing.assert_allclose(physical(from_physical(y)),y,rtol=2e-12)
    def test_invalid_physical_seed(self):
        for e in [0,30,-1,31]:
            with self.assertRaises(ValueError):from_physical(np.array([[90,.07,e]]))
    def test_transformed_rhs_against_original(self):
        rng=np.random.default_rng(41)
        for _ in range(80):
            n,z,e=rng.uniform(1,100),rng.uniform(.001,3),rng.uniform(.001,29.999);zd=rng.uniform(.001,3);x=from_physical(np.array([[n,z,e]]));f=field(x,np.array([zd]))[0];d=.02*n*(1-n/100)-.001*e*n
            expected=np.array([d,(np.logaddexp(0,-10*d)/10-z)/5,(1-e/30)*(.914*e*(zd-e/30)+.01*zd/(1+zd))]);np.testing.assert_allclose(f*np.array([n,1,e*(1-e/30)]),expected,rtol=2e-12,atol=3e-14)
    def test_transformed_instantaneous_jacobian(self):
        x=from_physical(np.array([[38.,.4,29.8],[90,.07,2.]]));z=np.array([.1,.5]);_,A,B=field(x,z,True);h=1e-5
        for j in range(3):
            xp=x.copy();xm=x.copy();xp[:,j]+=h;xm[:,j]-=h;np.testing.assert_allclose((field(xp,z)-field(xm,z))/(2*h),A[:,:,j],rtol=2e-6,atol=2e-8)
    def test_transformed_delay_jacobian(self):
        x=from_physical(np.array([[38.,.4,29.8],[90,.07,2.]]));z=np.array([.1,.5]);_,A,B=field(x,z,True);h=1e-6;np.testing.assert_allclose((field(x,z+h)-field(x,z-h))/(2*h),B,rtol=1e-8,atol=2e-10)
    def test_odd_grid_required(self):
        with self.assertRaises(ValueError):Collocation(64)
    def test_spectral_derivative(self):
        c=Collocation(15);t=np.arange(15)/15;np.testing.assert_allclose(c.D@np.sin(2*np.pi*t),2*np.pi*np.cos(2*np.pi*t),atol=4e-14)
    def test_spectral_delay(self):
        c=Collocation(15);t=np.arange(15)/15;s=.137;S=c.matrix(np.exp(-2j*np.pi*c.k*s));np.testing.assert_allclose(S@np.sin(2*np.pi*t),np.sin(2*np.pi*(t-s)),atol=2e-15)
    def test_complete_collocation_jacobian(self):
        c=Collocation(9);t=np.arange(9)/9;Y=np.column_stack([90+np.cos(2*np.pi*t),.07+.01*np.sin(2*np.pi*t),2+.2*np.sin(2*np.pi*t)]);w=np.r_[from_physical(Y).ravel(),155.];r,J=c.residual(w,64.);h=2e-5
        for j in range(len(w)):
            e=np.zeros_like(w);e[j]=h;fd=(c.residual(w+e,64.,False)-c.residual(w-e,64.,False))/(2*h);np.testing.assert_allclose(fd,J[:,j],rtol=4e-6,atol=2e-7)
    def test_resize_preserves_period(self):
        a=np.load(ROOT/'data/upper_arm_orbits_v42.npz');w=a[a.files[0]];self.assertEqual(resize(w,257)[-1],w[-1])
    def test_continuation_completion(self):
        r=data('upper_arm_continuation_v42.json');self.assertEqual(r['status'],'target_reached');self.assertEqual(len(r['records']),131);self.assertEqual(r['last_tau'],155)
    def test_all_orbits_remain_interior(self):
        a=np.load(ROOT/'data/upper_arm_orbits_v42.npz')
        for key in a.files:
            y=physical(a[key][:-1].reshape(-1,3));self.assertGreater(y[:,0].min(),0);self.assertGreater(y[:,1].min(),0);self.assertGreater(y[:,2].min(),0);self.assertLess(y[:,2].max(),30)
    def test_all_floquet_records_stable_numerically(self):
        r=data('upper_arm_floquet_v42.json')['records'];self.assertEqual(len(r),131)
        for x in r:self.assertLess(x['dominant_nontrivial_modulus'],.944);self.assertGreater(x['neutral_alignment'],.99999);self.assertLess(abs(complex(*x['neutral_multiplier'])-1),2e-5)
    def test_refinement_defects(self):
        r=data('upper_arm_refinement_v42.json')['records'];self.assertEqual(len(r),6)
        for x in r:
            self.assertEqual([y['nodes']for y in x['meshes']],[257,513,1025]);self.assertLess(abs(x['meshes'][-1]['period']-x['meshes'][-2]['period']),1e-9);self.assertLess(max(x['meshes'][-1]['offgrid_abs_residual_N_Z_E']),1.3e-11)
    def test_refinement_floquet_steps(self):
        for x in data('upper_arm_refinement_v42.json')['records']:
            self.assertEqual([y['dt_target']for y in x['floquet_steps']],[.04,.02,.01]);self.assertLess(abs(x['floquet_steps'][-1]['dominant_nontrivial_modulus']-x['floquet_steps'][-2]['dominant_nontrivial_modulus']),2e-5)
    def test_capture_positive_and_negative_histories(self):
        r=data('nonlinear_capture_check_v42.json')['records'];self.assertEqual([x['capture_waveform_supported']for x in r],[True,True,False,False,True,True])
        for x in r:self.assertFalse(x['boundary_clipping']);self.assertIn('one phase shift only',x['waveform_fit'])
        for i in [1,5]:self.assertLess(r[i]['normalised_waveform_rms'],8.4e-8)
        self.assertGreater(r[3]['normalised_waveform_rms'],.5)
    def test_capture_step_halving_improves_match(self):
        r=data('nonlinear_capture_check_v42.json')['records']
        for i in [0,4]:self.assertLess(r[i+1]['normalised_waveform_rms'],r[i]['normalised_waveform_rms'])
    def test_A_nonlinear_hopf_intervals(self):
        for x in data('hopf_cubic_interval_v42.json')['records']:
            for key in ['l1_physical_time','Delta_prime_modulus_squared','zero_root_value','second_harmonic_resolvent_modulus_squared']:self.assertGreater(float(x[key][0]),0)
    def test_B_nonlinear_hopf_intervals(self):
        a,b=data('hopf_cubic_B_interval_v42.json')['records'];self.assertLess(float(a['l1_physical_time'][1]),0);self.assertGreater(float(b['l1_physical_time'][0]),0)
    def test_all_scalar_combinations(self):
        r=data('all_scalar_hopf_v42.json')['records'];self.assertEqual(len(r),8)
        for x in r:self.assertTrue(x['simple_scalar_root']);self.assertGreater(float(x['tau_enclosure'][0]),0)
    def test_analytic_hopf_derivatives(self):
        for x in data('hopf_derivative_checks_v42.json')['checks']:self.assertLess(float(x['max_error']),3.5e-84)
    def test_impulse_norm_independent_quadrature(self):
        c=coefficients();a=-c['AN'];d=c['d'];b=c['BE'];t0=np.log(d/a)/(d-a);g=lambda t:b*(d*np.exp(-d*t)-a*np.exp(-a*t))/(d-a);num=quad(g,0,t0,epsabs=1e-14)[0]-quad(g,t0,np.inf,epsabs=1e-14)[0];exact=2*b/d*(a/d)**(a/(d-a));self.assertAlmostEqual(num,exact,13)
    def test_protective_margin_and_box(self):
        x=data('protective_all_cadences_v42.json');self.assertLess(float(x['mu_gamma_times_k_over_c'][1]),.138027);self.assertLess(float(x['theta_0p57_uniform_gain_bound'][1]),1);self.assertLess(float(x['parameter_box_gain_upper_bound'][1]),.274);self.assertGreater(float(x['parameter_box_a_lower_bound'][0]),0)
    def test_theta_review_sampled_checks(self):
        c=protective();F=hold_matrix(c)
        for theta in [.57,.64,1.]:
            for t in np.geomspace(1e-4,1e4,60):
                R=np.eye(3);R[2]=[0,t*c['CZ']/(1-theta*t*c['CE']),(1+(1-theta)*t*c['CE'])/(1-theta*t*c['CE'])];self.assertLess(max(abs(np.linalg.eigvals(R@expm(F*t)))),1)
    def test_exact_quota_map_invariance(self):
        E0=2.2344650543950643;rng=np.random.default_rng(17)
        for _ in range(200):
            e=rng.uniform(0,E0);z=rng.uniform(0,10);t=10**rng.uniform(-5,5);cap=E0/(1+z);y=(e-cap)/(30-e);yy=y*np.exp(-.914*(1-cap/30)*t);new=(cap+30*yy)/(1+yy);self.assertGreaterEqual(new,min(e,cap)-1e-14);self.assertLessEqual(new,max(e,cap)+1e-14)
    def test_exact_quota_map_jacobian_matches_review(self):
        c=protective();e=c['E'];z=c['Z'];E0=e*(1+z);t=3.;h=1e-6
        def update(e,z):
            cap=E0/(1+z);y=(e-cap)/(30-e);y*=np.exp(-.914*(1-cap/30)*t);return(cap+30*y)/(1+y)
        de=(update(e+h,z)-update(e-h,z))/(2*h);dz=(update(e,z+h)-update(e,z-h))/(2*h);self.assertAlmostEqual(de,np.exp(c['CE']*t),8);self.assertAlmostEqual(dz,np.expm1(c['CE']*t)*c['CZ']/c['CE'],8)
    def test_stock_floor_inward_boundary(self):
        E0=2.2344650543950643;nb=100*(1-.001*E0/.02)
        for e in np.linspace(0,E0,30):self.assertGreaterEqual(.02*nb*(1-nb/100)-.001*e*nb,-1e-15)
    def test_tether_full_state_bistability(self):
        x=data('tether_equilibria_v42.json');self.assertLess(float(x['alpha'][1]),.02);a,b=x['positive_equilibria'];self.assertLess(float(a['characteristic_coefficients'][-1][1]),0);self.assertGreater(float(b['Hurwitz_second_minor'][0]),0);self.assertGreater(float(b['Hurwitz_third_minor'][0]),0);self.assertLess(float(x['independent_Jacobian_max_error']),6e-88)
    def test_empirical_event_clock_dependence_and_precision(self):
        x=data('empirical_event_evidence_v42.json');self.assertEqual(x['distinct_episodes'],2);self.assertEqual(x['derived_clocks'],5);p=x['pairs'];self.assertGreater(p[3]['lag_lo_years'],.5);self.assertLess(p[3]['lag_hi_years'],1.26);self.assertEqual(p[4]['lag_lo_years'],0);self.assertLess(p[4]['lag_hi_years'],.67)
    def test_empirical_not_a_delay_distribution(self):
        x=data('empirical_event_evidence_v42.json');self.assertIn('Not achieved',x['dynamic_validation']);self.assertIn('not confidence',x['date_bounds'])
    def test_effort_scaling_symmetry(self):
        n,e,q,M,d0,E0=80,3,.001,30,.01,2.3;s=4.;z=.2;zp=.15;f=lambda e,q,M,d0:(1-e/M)*(.914*e*(zp-e/M)+d0*zp/(1+zp));self.assertAlmostEqual(q*e*n,(q/s)*(s*e)*n,14);self.assertAlmostEqual(s*f(e,q,M,d0),f(s*e,q/s,s*M,s*d0),14)
    def test_approved_declaration_and_hyperlinked_orcid(self):
        s=(ROOT/'manuscript/paper4_delay_dynamics_v42.tex').read_text();self.assertIn('Arena.ai Agent Mode was used to assist with computational methods and literature review.',s);self.assertIn('https://orcid.org/0000-0002-0019-1842',s)
    def test_old_tex_and_SI_are_preserved(self):
        p=ROOT/'inherited/paper4_supplementary_v8_pinned_2efaa.md';self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),'ac8180e2f2953137e81a7a26932428ca5e2f44b00894eea5a674db74a14d3bd6')
    def test_manuscript_no_stale_certification_or_empirical_claims(self):
        s=(ROOT/'manuscript/paper4_delay_dynamics_v42.tex').read_text()
        for bad in ['Each consistent scheme therefore restabilises','0.9928','an unverified conjecture','pre-rebuild state','hence no lower\nfold']:self.assertNotIn(bad,s)
    def test_PDFs_complete_and_searchable(self):
        from pypdf import PdfReader
        for n,minimum in [('paper4_delay_dynamics_v42',45),('paper4_supplementary_v9',10)]:
            r=PdfReader(ROOT/'manuscript'/(n+'.pdf'));self.assertGreaterEqual(len(r.pages),minimum)
            self.assertTrue(all(len(p.extract_text().strip())>50 for p in r.pages))
    def test_PDF_metadata(self):
        from pypdf import PdfReader
        for n in ['paper4_delay_dynamics_v42','paper4_supplementary_v9']:
            m=PdfReader(ROOT/'manuscript'/(n+'.pdf')).metadata;self.assertEqual(m['/Author'],'Amin Abaee');self.assertTrue(m['/Title']);self.assertIn('Hopf bifurcation',m['/Keywords'])
    def test_PDF_ORCID_hyperlink(self):
        from pypdf import PdfReader
        p=PdfReader(ROOT/'manuscript/paper4_delay_dynamics_v42.pdf').pages[0];uris=[a.get_object().get('/A',{}).get('/URI','')for a in p.get('/Annots',[])];self.assertIn('https://orcid.org/0000-0002-0019-1842',uris)
    def test_manuscript_builders_reproduce_sources(self):
        import subprocess,sys
        for name,target in [('build_manuscript_v42.py','paper4_delay_dynamics_v42.tex'),('build_supplement_v9.py','paper4_supplementary_v9.md')]:
            before=(ROOT/'manuscript'/target).read_bytes();subprocess.run([sys.executable,str(ROOT/'src'/name)],check=True,stdout=subprocess.PIPE);self.assertEqual(before,(ROOT/'manuscript'/target).read_bytes())
if __name__=='__main__':unittest.main(verbosity=2)
