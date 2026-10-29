"""Kernel properties, independent LP checks and fixed-support result regressions.
These tests verify arithmetic/identification, not ecological validity of maps.
"""
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
import unittest
import numpy as np
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from identification_F11 import (block_sum, topology_bounds, canonical_fractions,
    contrast_fractions, contrast_interval, cancellation, witness, GROUPS, SCALES)

def rows(name):
    with (ROOT/'data'/name).open() as f:return list(csv.DictReader(f))

class IdentificationKernelTests(unittest.TestCase):
    def test_block_sum_preserves_mass(self):
        a=np.arange(64).reshape(8,8)
        for side in (1,2,4,8):self.assertEqual(block_sum(a,side).sum(),a.sum())
    def test_block_partition_exact_example(self):
        np.testing.assert_array_equal(block_sum(np.arange(16).reshape(4,4),2),[[10,18],[42,50]])
    def test_invalid_block_sides_rejected(self):
        for side in (0,-1,3,1.5):
            with self.assertRaises(ValueError):block_sum(np.ones((4,4)),side)
    def test_one_dimensional_block_input_rejected(self):
        with self.assertRaises(ValueError):block_sum(np.ones(4),1)
    def test_pure_absent_and_mixed_bounds(self):
        q=np.array([[10.,20.],[30.,40.]]);c=np.array([[0,1],[2,2]]);n=np.full((2,2),2)
        self.assertEqual(topology_bounds(q,c,n),(70.,90.))
    def test_coarse_mixed_block_bounds(self):
        q=np.ones((2,2));c=np.array([[0,1],[2,2]]);n=np.full((2,2),2)
        self.assertEqual(topology_bounds(q,c,n,2),(0.,4.))
    def test_all_pure_remains_pure_on_coarsening(self):
        for s in (1,2,4):self.assertEqual(topology_bounds(np.ones((4,4)),np.ones((4,4),int),np.ones((4,4),int),s),(16.,16.))
    def test_all_absent_remains_absent(self):
        self.assertEqual(topology_bounds(np.ones((4,4)),np.zeros((4,4),int),np.ones((4,4),int),4),(0.,0.))
    def test_noninteger_topology_rejected(self):
        with self.assertRaises(ValueError):topology_bounds(np.ones((2,2)),np.ones((2,2)),np.ones((2,2),int))
    def test_negative_missing_mass_rejected(self):
        for bad in (-1.,math.nan,math.inf):
            with self.assertRaises(ValueError):topology_bounds(np.full((2,2),bad),np.ones((2,2),int),np.ones((2,2),int))
    def test_random_partition_nesting(self):
        rng=np.random.default_rng(4101)
        for repeat in range(20):
            q=rng.uniform(0,100,(8,8));n=np.full((8,8),3);c=rng.integers(0,4,(8,8))
            bounds=[topology_bounds(q,c,n,s)for s in (1,2,4,8)]
            for (l,u),(lc,uc) in zip(bounds,bounds[1:]):
                self.assertLessEqual(lc,l+1e-9);self.assertGreaterEqual(uc,u-1e-9)
    def test_block_bounds_against_independent_linear_program(self):
        q=np.array([[5.,3.],[7.,11.]]);c=np.array([[0,1],[2,2]]);n=np.full((2,2),2)
        limits=[(0,0),(0,3),(7,7),(11,11)]
        lower=linprog(np.ones(4),bounds=limits,method='highs')
        upper=linprog(-np.ones(4),bounds=limits,method='highs')
        self.assertTrue(lower.success and upper.success)
        self.assertEqual(topology_bounds(q,c,n),(lower.fun,-upper.fun))
    def test_certified_endpoint_canonicalization(self):
        f=canonical_fractions(np.array([0.,1.-2e-16,1.+2e-16,.4]),np.array([0,2,2,1]),np.full(4,2))
        np.testing.assert_array_equal(f,[0.,1.,1.,.4])
    def test_near_pure_mixed_not_reclassified(self):
        x=1.-1e-14
        f=canonical_fractions([x],[1],[2]);self.assertEqual(f[0],x)
        lo,hi=contrast_fractions(f,math.inf);self.assertEqual((lo[0],hi[0]),(0.,1.))
    def test_false_pure_fraction_disagreement_rejected(self):
        with self.assertRaises(ValueError):canonical_fractions([.9],[2],[2])
    def test_noninterior_mixed_fraction_rejected(self):
        for f in (0.,1.,1.+1e-16):
            with self.assertRaises(ValueError):canonical_fractions([f],[1],[2])
    def test_contrast_one_is_homogeneous(self):
        f=np.linspace(0,1,11);lo,hi=contrast_fractions(f,1.)
        np.testing.assert_allclose(lo,f);np.testing.assert_allclose(hi,f)
    def test_contrast_infinity_matches_topology(self):
        lo,hi=contrast_fractions(np.array([0.,.2,.8,1.]),math.inf)
        np.testing.assert_array_equal(lo,[0,0,0,1]);np.testing.assert_array_equal(hi,[0,1,1,1])
    def test_invalid_contrast_rejected(self):
        for ratio in (0.,.99,math.nan):
            with self.assertRaises(ValueError):contrast_fractions([.5],ratio)
    def test_invalid_fractions_rejected(self):
        for f in (-.1,1.1,math.nan):
            with self.assertRaises(ValueError):contrast_fractions([f],2.)
    def test_contrast_nested_intervals(self):
        f=np.linspace(.001,.999,100)
        lastlo,lasthi=contrast_fractions(f,1.)
        for r in (1.1,1.5,2,10,100,math.inf):
            lo,hi=contrast_fractions(f,r)
            self.assertTrue((lo<=lastlo+1e-15).all());self.assertTrue((hi>=lasthi-1e-15).all())
            lastlo,lasthi=lo,hi
    def test_contrast_sharpness_against_independent_LP(self):
        # Variables are densities (not mass fractions); independent mixture constraints.
        for f in (.01,.2,.5,.9,.999):
            for ratio in (1.,1.5,2.,10.,100.):
                d=7.;obj=np.array([f,0.]);eq=np.array([[f,1-f]])
                aub=np.array([[1.,-ratio],[-ratio,1.]])
                mn=linprog(obj,A_ub=aub,b_ub=[0.,0.],A_eq=eq,b_eq=[d],bounds=[(0,None)]*2,method='highs')
                mx=linprog(-obj,A_ub=aub,b_ub=[0.,0.],A_eq=eq,b_eq=[d],bounds=[(0,None)]*2,method='highs')
                lo,hi=contrast_fractions([f],ratio)
                self.assertTrue(mn.success and mx.success)
                self.assertAlmostEqual(mn.fun,d*lo[0],places=8);self.assertAlmostEqual(-mx.fun,d*hi[0],places=8)
    def test_zero_mass_density_ratio_does_not_divide_by_zero(self):
        self.assertEqual(contrast_interval([0.],[0.],[.2],[.8],2.),(0.,0.))
    def test_cross_endpoint_extremes_not_like_endpoints(self):
        self.assertEqual(contrast_interval([10.],[20.],[.5],[.5],math.inf),(-10.,20.))
    def test_cancellation_known_example(self):
        x=cancellation(np.zeros((2,2)),np.array([[4.,-2.],[3.,-1.]]),1)
        self.assertEqual(x['net_Mg'],4.);self.assertEqual(x['gains_Mg'],7.);self.assertEqual(x['losses_Mg'],3.)
        self.assertAlmostEqual(x['cancellation'],.6)
    def test_cancellation_undefined_all_zero(self):
        self.assertIsNone(cancellation(np.zeros((2,2)),np.zeros((2,2)),1)['cancellation'])
    def test_cancellation_one_for_zero_net_nonzero_offsets(self):
        self.assertEqual(cancellation(np.zeros((2,2)),np.array([[1.,-1.],[1.,-1.]]),1)['cancellation'],1.)
    def test_random_cancellation_monotonicity(self):
        rng=np.random.default_rng(6203)
        for k in range(20):
            q0=rng.uniform(0,20,(8,8));q1=rng.uniform(0,20,(8,8))
            data=[cancellation(q0,q1,s)for s in (1,2,4,8)]
            for a,b in zip(data,data[1:]):
                self.assertAlmostEqual(a['net_Mg'],b['net_Mg'],places=10)
                self.assertGreaterEqual(a['cancellation']+1e-12,b['cancellation'])
    def test_witnesses_attain_toy_bounds(self):
        q0=np.array([[10.,20.],[30.,40.]]);q1=q0+1;c=np.array([[0,1],[2,2]]);n=np.full((2,2),2)
        b0=topology_bounds(q0,c,n);b1=topology_bounds(q1,c,n)
        mn=witness(q0,q1,c,c,n,n,'minimum');mx=witness(q0,q1,c,c,n,n,'maximum')
        self.assertEqual(mn['difference_Mg'],b1[0]-b0[1]);self.assertEqual(mx['difference_Mg'],b1[1]-b0[0])
    def test_witness_convex_interpolation_feasible(self):
        q=np.array([0.,3.,7.]);c=np.array([0,1,2]);n=np.full(3,2)
        lo=np.where(c==n,q,0);hi=np.where(c>0,q,0)
        for a in np.linspace(0,1,11):
            x=lo+a*(hi-lo)
            self.assertTrue(((x>=0)&(x<=q)).all());self.assertEqual(x[0],0);self.assertEqual(x[2],7.)

class DataAndArticleRegressionTests(unittest.TestCase):
    def test_eighteen_scale_cases_all_unidentified(self):
        r=rows('resolution_frontier_F11.csv');self.assertEqual(len(r),18)
        self.assertEqual({int(x['block_side_native_cells'])for x in r},set(SCALES))
        self.assertTrue(all(float(x['difference_lower_Mg'])<0<float(x['difference_upper_Mg']) for x in r))
    def test_native_intervals_match_unchanged_F10(self):
        with (ROOT/'inherited_F10/data/allocation/difference_envelopes_F07.csv').open()as f:old=list(csv.DictReader(f))
        new=[r for r in rows('resolution_frontier_F11.csv')if r['block_side_native_cells']=='1']
        for a,b in zip(old,new):
            self.assertEqual(a['group'],b['group'])
            # Header spelling is inspected from the inherited artifact, not guessed.
            low=next(k for k in a if 'lower' in k);up=next(k for k in a if 'upper' in k)
            self.assertAlmostEqual(float(a[low]),float(b['difference_lower_Mg']),places=7)
            self.assertAlmostEqual(float(a[up]),float(b['difference_upper_Mg']),places=7)
    def test_scale_widths_nested_and_native_reductions(self):
        for group,expected in zip(GROUPS,[49.05044003558552,55.9310134883671]):
            r=[x for x in rows('resolution_frontier_F11.csv')if x['group']==group]
            widths=[float(x['width_Mg'])for x in r]
            self.assertTrue(all(a<=b+1e-7 for a,b in zip(widths,widths[1:])))
            self.assertAlmostEqual(100*(1-widths[0]/widths[-1]),expected,places=8)
    def test_cancellation_full_data_and_net_invariance(self):
        r=rows('cancellation_by_scale_F11.csv');self.assertEqual(len(r),9)
        self.assertAlmostEqual(float(r[0]['cancellation']),.7023402134614583,places=12)
        for x in r:self.assertAlmostEqual(float(x['net_Mg']),65242.36652986525,places=7)
        self.assertEqual([float(x['cancellation'])for x in r[-3:]],[0.,0.,0.])
    def test_all_four_full_data_witnesses_valid_and_opposite_sign(self):
        r=rows('extremal_witness_certificates_F11.csv');self.assertEqual(len(r),4)
        for group in GROUPS:
            x=[a for a in r if a['group']==group]
            self.assertLess(float(x[0]['difference_Mg']),0);self.assertGreater(float(x[1]['difference_Mg']),0)
            for a in x:
                self.assertEqual(a['cell_constraints_satisfied'],'True');self.assertEqual(a['cells_per_endpoint'],'65536')
    def test_full_data_contrast_boundaries(self):
        r=rows('density_contrast_sign_boundaries_F11.csv')
        for x,expected in zip(r,[1.4555078889054214,1.9495126064661252]):
            self.assertAlmostEqual(float(x['positive_sign_boundary_ratio']),expected,places=9)
            self.assertEqual(x['ratio_is_assumed_not_measured'],'True')
    def test_unrestricted_contrast_recovers_primary_sets(self):
        a=[x for x in rows('density_contrast_sensitivity_F11.csv')if x['max_density_ratio']=='inf']
        b=[x for x in rows('resolution_frontier_F11.csv')if x['block_side_native_cells']=='1']
        for x,y in zip(a,b):
            for k in ('difference_lower_Mg','difference_upper_Mg'):
                self.assertAlmostEqual(float(x[k]),float(y[k]),places=7)
    def test_finite_contrasts_never_claim_calibration(self):
        r=rows('density_contrast_sensitivity_F11.csv');self.assertEqual(len(r),16)
        self.assertTrue(all(x['empirically_validated_ratio']=='False'for x in r))
    def test_eight_national_holds_retained(self):
        with (ROOT/'inherited_F10/data/support/physical_admission_F08.csv').open()as f:r=list(csv.DictReader(f))
        self.assertEqual(len(r),8);self.assertTrue(all(x['admission']=='hold_not_admitted'for x in r))
    def test_coverage_copy_exact_and_sixteen_rows(self):
        a=ROOT/'data/native_probe_coverage_F11.csv';b=ROOT/'inherited_F10/data/support/native_probe_coverage.csv'
        self.assertEqual(a.read_bytes(),b.read_bytes());r=rows('native_probe_coverage_F11.csv');self.assertEqual(len(r),16)
        self.assertTrue(all(x['joint_agb_sd_valid_cells']=='65536'for x in r))
    def test_both_articles_explain_unrounded_difference(self):
        for name in ('main','SI'):
            s=(ROOT/f'followup_F11_A01_{name}.tex').read_text()
            self.assertIn('All difference bounds were calculated from unrounded endpoint bounds',s)
            self.assertIn('biomass-change identifiability',s)
    def test_original_ecological_questions_retained_as_prospective(self):
        old=(ROOT/'inherited_F10/followup_F10_main.tex').read_text()
        section=old[old.index('The empirical comparison addresses four questions:'):old.index('The first question establishes')]
        new=(ROOT/'src/SI_addition_F11.tex').read_text()
        for line in section.splitlines():
            if line.startswith('\\item '):self.assertIn(line,new)
    def test_author_orcid_and_exact_ai_declaration_retained(self):
        s=(ROOT/'followup_F11_A01_main.tex').read_text()
        self.assertIn('https://orcid.org/0000-0002-0019-1842',s)
        self.assertIn('Agent Mode was used to assist with computational methods and literature review.',s)
        self.assertIn('Amin Abaee',s)
    def test_new_analysis_flags_distinguish_identification_from_validation(self):
        x=json.loads((ROOT/'metadata/analysis_F11.json').read_text())
        for name in ('validated_change','national_inference','raw_arrays_redistributed'):self.assertFalse(x[name])
        self.assertTrue(x['primary_model_has_no_finite_density_contrast_cap'])
    def test_fresh_native_SD_counts_reproduce_R03(self):
        new=rows('native_sd_reproduction_F11.csv')
        with (ROOT/'inherited_F10/data/reference/native_sd_summary_R03.csv').open()as f:old=list(csv.DictReader(f))
        self.assertEqual(len(new),2)
        for a,b in zip(old,new):
            self.assertEqual(set(a),set(b))
            for key in a:self.assertEqual(float(a[key]),float(b[key]),key)
    def test_figure_one_F06_preserved(self):
        s=(ROOT/'followup_F11_A01_main.tex').read_text();self.assertIn('{account_coverage_F06.pdf}',s)
    def test_no_raw_native_or_full_provider_documents_in_deliverable(self):
        for name in ('BRA_2015.ascii','BRA_2023.ascii','E3UB.pdf','PVIR.pdf','PVP.pdf','ADPC.pdf'):
            found=[p for p in ROOT.rglob(name)if '.cache'not in p.parts]
            self.assertEqual(found,[])

if __name__=='__main__':unittest.main()
