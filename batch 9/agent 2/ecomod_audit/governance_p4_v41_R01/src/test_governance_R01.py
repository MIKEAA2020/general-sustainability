import unittest, json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from verify_governance_R01 import coefficients,protective,frequency_records,characteristic,monodromy,radius,cubic,hold_matrix
ROOT=Path(__file__).resolve().parents[1]
class AuditTests(unittest.TestCase):
    def test_equilibrium_stock(self):self.assertAlmostEqual(coefficients()['N'],89.55188301131166,11)
    def test_equilibrium_effort(self):self.assertAlmostEqual(coefficients()['E'],2.089623397737668,12)
    def test_even_pairs_identity(self):
        c=coefficients();self.assertAlmostEqual(c['BE']*c['AN'],c['BN']*c['AE'],16)
    def test_characteristic_determinant(self):
        c=coefficients();l=.001+.031j;t=7.;A=hold_matrix(c).astype(complex);A[2,2]=c['CE'];A[2,1]=c['CZ']*np.exp(-l*t)
        self.assertAlmostEqual(abs(np.linalg.det(l*np.eye(3)-A)-characteristic(l,t,c)),0,15)
    def test_A_gated_crossings(self):
        for r,t in zip(frequency_records(coefficients()),[3.6661490142741,150.3584773101414]):self.assertAlmostEqual(r['tau'],t,9)
    def test_A_ungated_crossings(self):
        for r,t in zip(frequency_records(coefficients(gated=False)),[6.88141063047798,132.374903454401]):self.assertAlmostEqual(r['tau'],t,9)
    def test_B_gated_crossings(self):
        for r,t in zip(frequency_records(coefficients('B')),[5.51284073144347,80.4245267142273]):self.assertAlmostEqual(r['tau'],t,9)
    def test_B_ungated_crossings(self):
        for r,t in zip(frequency_records(coefficients('B',False)),[6.21359873401819,76.2906356879514]):self.assertAlmostEqual(r['tau'],t,9)
    def test_hopf_crossing_directions(self):
        a,b=frequency_records(coefficients());self.assertLess(a['dRe_dtau'],0);self.assertGreater(b['dRe_dtau'],0)
    def test_characteristic_residuals(self):
        for c in [coefficients(),coefficients(gated=False),coefficients('B'),coefficients('B',False)]:
            for r in frequency_records(c):self.assertLess(r['characteristic_residual'],1e-14)
    def test_protective_cubic_coefficients_positive(self):self.assertTrue(np.all(cubic(protective())>0))
    def test_protective_undelayed_hurwitz(self):
        c=protective();J=hold_matrix(c);J[2,1]=c['CZ'];J[2,2]=c['CE'];self.assertLess(max(np.linalg.eigvals(J).real),0)
    def test_mobilising_undelayed_unstable(self):
        c=coefficients();J=hold_matrix(c);J[2,1]=c['CZ'];J[2,2]=c['CE'];self.assertGreater(max(np.linalg.eigvals(J).real),0)
    def test_native_mobilising_against_ode(self):self._native_ode(coefficients())
    def test_native_protective_against_ode(self):self._native_ode(protective())
    def _native_ode(self,c):
        cols=[]
        for i in range(3):
            y0=np.eye(3)[:,i];sample=y0[1]
            def f(t,y):
                n,z,e=y;return [c['AN']*n+c['AE']*e,c['BN']*n-c['d']*z+c['BE']*e,c['CE']*e+c['CZ']*sample]
            sol=solve_ivp(f,[0,1],y0,method='DOP853',rtol=1e-12,atol=1e-14);self.assertTrue(sol.success);cols.append(sol.y[:,-1])
        np.testing.assert_allclose(np.column_stack(cols),monodromy(1,c,'native'),rtol=2e-11,atol=2e-13)
    def test_native_protective_radius_not_printed_value(self):
        self.assertAlmostEqual(radius(1,protective(),'native'),.9838194826251283,12);self.assertGreater(abs(radius(1,protective(),'native')-.9928),.008)
    def test_all_schemes_consistent(self):
        c=coefficients();J=hold_matrix(c);J[2,1]=c['CZ'];J[2,2]=c['CE'];h=1e-6
        for scheme in ['euler','exact','native']:np.testing.assert_allclose((monodromy(h,c,scheme)-np.eye(3))/h,J,rtol=1e-5,atol=2e-7)
    def test_euler_mobilising_stable_window(self):
        c=coefficients();self.assertGreater(radius(1,c,'euler'),1);self.assertLess(radius(60,c,'euler'),1);self.assertGreater(radius(90,c,'euler'),1)
    def test_exact_and_native_named_crossings(self):
        c=coefficients()
        for name,t in [('exact',6.501294948075),('native',6.727850067339)]:self.assertAlmostEqual(radius(t,c,name),1,11)
    def test_protective_euler_threshold(self):self.assertAlmostEqual(radius(2.306354424447415,protective(),'euler'),1,11)
    def test_spectral_ordering_exact(self):
        from scipy.linalg import expm
        c=coefficients();T=4.;F=expm(hold_matrix(c)*T);R=monodromy(T,c,'euler')@np.linalg.inv(F)
        np.testing.assert_allclose(np.sort_complex(np.linalg.eigvals(R@F)),np.sort_complex(np.linalg.eigvals(F@R)),rtol=1e-11,atol=1e-12)
    def test_interval_scalar_certificates_recorded(self):
        r=json.loads((ROOT/'data/verification_results_R01.json').read_text())
        for q in r['scalar_interval_checks']['roots']:
            self.assertTrue(q['endpoint_sign_change_proved']);self.assertTrue(q['derivative_excludes_zero']);self.assertTrue(q['inside_published_delay_enclosure'])
    def test_mixed_interval_certificates_recorded(self):
        r=json.loads((ROOT/'data/mixed_delay_check_R01.json').read_text());a,b=r['roots']
        self.assertTrue(a['strict_krawczyk_inclusion']);self.assertTrue(a['root_certified_in_left_half_plane']);self.assertTrue(b['strict_krawczyk_inclusion']);self.assertTrue(b['root_certified_in_right_half_plane'])
        c=coefficients();p=protective();ch=.9988;lam=complex(*map(float,b['point_root']));J=hold_matrix(c).astype(complex);J[2,2]=ch*c['CE']+(1-ch)*p['CE'];J[2,1]=ch*c['CZ']+(1-ch)*p['CZ']*np.exp(-110*lam)
        self.assertLess(abs(np.linalg.det(lam*np.eye(3)-J)),1e-15)
    def test_interval_decimal_outward(self):
        from mpmath import iv,mp
        from interval_decimal_R01 import outward_bounds
        mp.dps=90;iv.dps=80
        for t in ['.33333333333333333333333333333333333333333333333333333333333333333333','-.12345678912345678912345678912345678912345678912345678912345678912345']:
            x=iv.mpf(t);a,b=outward_bounds(x)
            self.assertLessEqual(mp.mpf(a),mp.mpf(x._mpi_[0]));self.assertGreaterEqual(mp.mpf(b),mp.mpf(x._mpi_[1]))
    def test_mixed_undelayed_routh_certificate(self):
        r=json.loads((ROOT/'data/mixed_delay_check_R01.json').read_text());self.assertTrue(r['tau_M_tau_p_zero']['hurwitz_interval_certified']);self.assertGreater(r['weighted_small_gain']['F_at_witness'],1)
    def test_invalid_scheme(self):
        with self.assertRaises(ValueError):monodromy(1,coefficients(),'unknown')
if __name__=='__main__':unittest.main(verbosity=2)
