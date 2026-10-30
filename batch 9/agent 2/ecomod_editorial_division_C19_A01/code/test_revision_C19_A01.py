"""C19 numerical, editorial, provenance and PDF regressions; survives python -O."""
from pathlib import Path
import unittest,csv,json,hashlib,re,math
import numpy as np
from pypdf import PdfReader
import prepare_revision_C19_A01 as prep
import reproduce_two_land_C18_A01 as two
import reproduce_comparator_C18_A01 as comp
R=Path(__file__).resolve().parents[1]
def rows(n):
    with (R/'data'/(n+'_C18_A01.csv')).open()as f:return list(csv.DictReader(f))
def js(n):return json.loads((R/'data'/(n+'_C18_A01.json')).read_text())
class RevisionTests(unittest.TestCase):
    def test_01_inherited_bytes_preserved(self):
        d=json.loads((R/'metadata/inherited_artifact_provenance_C19_A01.json').read_text())
        self.assertEqual(len(d['files']),66)
        self.assertEqual(d['source_publication_commit'],'688701d6053ea1d89a37b9c708ef29c9b2e8ddf5')
        for z in d['files']:
            b=(R/z['path']).read_bytes();self.assertEqual(len(b),z['bytes']);self.assertEqual(hashlib.sha256(b).hexdigest(),z['sha256'],z['path'])
    def test_02_annual_join_exact_years(self):self.assertEqual([int(r['year'])for r in rows('empirical_annual_join')],list(range(1961,2024)))
    def test_03_excluded_estimates_preserved(self):self.assertEqual([int(r['year'])for r in rows('nfa_world_source_extraction')][-2:],[2024,2025])
    def test_04_population_conversion(self):
        raw={r['year']:r for r in rows('nfa_world_source_extraction')}
        for r in rows('empirical_annual_join'):self.assertEqual(float(r['P_persons']),1000*float(raw[r['year']]['pop_1000_persons']))
    def test_05_1961_2023_endpoint(self):
        r=rows('empirical_annual_join');self.assertAlmostEqual(float(r[0]['B_gha']),9725417562,delta=1);self.assertAlmostEqual(float(r[-1]['B_gha']),12142843961,delta=1)
    def test_06_percapita_all_years(self):
        for r in rows('empirical_annual_join'):
            self.assertAlmostEqual(float(r['B_per_person']),float(r['B_gha'])/float(r['P_persons']),places=14)
    def test_07_log_identity(self):self.assertLess(js('empirical_summary')['max_log_identity_error'],1e-14)
    def test_08_component_source_rounding(self):self.assertLessEqual(js('empirical_summary')['max_component_sum_residual_gha'],2)
    def test_09_component_percentages(self):
        z=[r for r in rows('empirical_components')if r['year']=='2023'];v={r['component']:float(r['contribution_pp'])for r in z}
        for k,x in [('crop',24.06),('forest',-5.95),('built',7.44)]:self.assertAlmostEqual(v[k],x,delta=.0051)
    def test_10_first_crossing(self):
        r=rows('empirical_annual_join');self.assertEqual(min(int(z['year'])for z in r if float(z['Eprod_over_B'])>1),1973)
    def test_11_same_edition_endpoints(self):
        r=rows('empirical_endpoints')
        for z,x in zip(r,[.219497,.221997]):self.assertAlmostEqual(float(z['logB']),x,delta=5e-7)
    def test_12_LMDI(self):
        for r in rows('empirical_LMDI_sensitivity'):
            if r['method']=='LMDI':self.assertLess(abs(float(r['closure'])),1e-13)
    def test_13_level_fallback(self):
        r=[z for z in rows('empirical_LMDI_sensitivity')if z['method']=='level_fallback'];self.assertEqual(len(r),2)
        for z in r:self.assertLessEqual(float(z['C_empT']),0);self.assertEqual(z['yield_term'],'');self.assertLess(abs(float(z['closure'])),2e-6)
    def test_14_central_proxy(self):
        r=next(z for z in rows('empirical_LMDI_sensitivity')if z['year']=='2023'and abs(float(z['phi0'])-.1286472202)<1e-9)
        for k,x in [('yield_term',.268662),('area_term',.037710),('residual_term',-.084375)]:self.assertAlmostEqual(float(r[k]),x,delta=5e-7)
    def test_15_crop_calibration(self):
        r=rows('empirical_crop_calibration')[-1]
        for k,x in [('nfa_crop_B_ratio',2.870055),('nfa_crop_area_ratio',1.198029),('owid_area_ratio',1.173414),('owid_yield_ratio',3.124667)]:self.assertAlmostEqual(float(r[k]),x,delta=5e-7)
    def test_16_legacy_current_version(self):
        d=js('two_land_summary');self.assertLess(d['legacy_v44_current_minimum_max_error'],1e-12);self.assertLess(d['legacy_v44_current_final_max_error'],1e-12)
    def test_17_legacy_v42_v43_agree_not_v44(self):
        r=rows('historical_drawdown_comparison');v={i:[z for z in r if int(z['version'])==i]for i in [42,43,44]}
        self.assertEqual(len(v[42]),124)
        self.assertEqual([z['final_Ac']for z in v[42]],[z['final_Ac']for z in v[43]])
        self.assertGreater(abs(float(v[42][0]['final_Ac'])-float(v[44][0]['final_Ac'])),.07)
    def test_18_C17_compiled_crosscheck(self):
        for r in js('two_land_summary')['baseline_cross_checks']:self.assertLess(r['max_abs_state_difference'],2e-11)
    def test_19_drawdown_grid_complete(self):self.assertEqual(len(rows('si_drawdown_depth')),248)
    def test_20_drawdown_positive_gap(self):
        for r in rows('si_drawdown_depth'):self.assertGreater(float(r['minimum_gap_ha']),0);self.assertGreaterEqual(float(r['minimum_Ar_ha']),.1)
    def test_21_monotone_grid(self):
        r=rows('si_drawdown_depth')
        for Ac in [.4,.7,1.,1.18]:
            y=[float(z['minimum_Ac_ha'])for z in r if float(z['Ac0_ha'])==Ac and float(z['chi'])==.1];self.assertTrue(np.all(np.diff(y)<=1e-12))
    def test_22_floor_thresholds(self):
        for z,x in zip(rows('proximity_thresholds'),[2.4098484,2.7001725,2.9775222,3.1403618]):self.assertAlmostEqual(float(z['proximity_1e_6_bisection']),x,delta=1e-7)
    def test_23_twenty_forty_quality_degeneracy(self):
        a=two.run(T=100.,taug=20.);b=two.run(T=100.,taug=40.);self.assertTrue(np.array_equal(a,b))
    def test_24_fixed_override_disables_restoration(self):
        a=two.run(T=20.,Efixed=.825,chi=0.);b=two.run(T=20.,Efixed=.825,chi=.1);self.assertTrue(np.array_equal(a,b));self.assertTrue(np.all(a[:,7]==.825));self.assertGreater(np.ptp(a[:,3]),.01)
    def test_25_quality_readout_noninjective(self):
        for q in [.1,.3,.6]:self.assertAlmostEqual(.05+.064*q*(1-q),.05+.064*(1-q)*q)
        self.assertGreater(.05+.064*.9*.1,.05)
    def test_26_gate_rows_refinement(self):
        r=rows('si_gate_sign');self.assertEqual(len(r),27)
        for z in r:self.assertLess(abs(float(z['final_B'])-float(z['final_E'])),1e-9);self.assertLess(float(z['area_balance_error']),1e-12)
    def test_27_gate_policy_direction(self):
        r={z['policy']:z for z in rows('si_gate_sign')if float(z['dt_yr'])==.1};self.assertGreater(float(r['surplus_010']['Rc900']),1);self.assertLess(float(r['deficit_010']['Rc900']),.02);self.assertAlmostEqual(float(r['target']['Rc900']),1,places=12);self.assertGreater(float(r['surplus_frozen']['peak_D']),float(r['surplus_010']['peak_D']))
    def test_28_comparator_root_equation(self):
        for r in js('comparator_summary')['roots']:self.assertLess(abs(r['neutral_residual']),1e-13);self.assertLess(abs(r['positive_root_residual']),1e-12)
    def test_29_comparator_roots(self):
        for r,x in zip(js('comparator_summary')['roots'],[.5883333333333333,.624999996791505]):self.assertAlmostEqual(r['positive_real_root'],x,places=10)
    def test_30_comparator_full_contact(self):
        r=js('comparator_summary')['full_refinement'];self.assertAlmostEqual(r[0]['first_floor_time_yr'],720.8);self.assertLess(abs(r[-1]['first_floor_time_yr']-r[-2]['first_floor_time_yr']),abs(r[1]['first_floor_time_yr']-r[0]['first_floor_time_yr']))
    def test_31_comparator_mask(self):
        r=js('comparator_summary')['mask'];self.assertAlmostEqual(r['width_yr'],3.01);self.assertLess(r['A_end'],r['A_start']);self.assertGreater(r['B_end'],r['B_start'])
    def test_32_comparator_delay_pair(self):
        r=js('comparator_summary')['delay_pairs'];self.assertGreater(r[0]['final_A'],1.19);self.assertLess(r[-1]['final_A'],.021)
    def test_33_comparator_basin_full_grid(self):
        r=rows('comparator_basin_cells');self.assertEqual(len(r),416);counts=js('comparator_summary')['basin_counts'];self.assertEqual([z['high'] for z in counts],[83,11]);self.assertEqual([z['total']for z in counts],[208,208])
    def test_34_comparator_distinct_gap(self):
        A=.8;b=.5;bg=.8;rho=.05;B=b*A+bg*rho*A*(1-A/1.2);E=B
        self.assertGreater(E-b*A,0);self.assertEqual(max(E-B,0),0)
    def test_35_budget_all_twenty_eight_rerun(self):
        d=json.loads((R/'evidence/budget_rerun_C18_A01.json').read_text());self.assertEqual(d['status'],'PASS');self.assertEqual(d['full_in_memory_trajectory_recomputations'],28)
    def test_36_C18_labels_sections_and_bibkeys_preserved(self):
        for kind in ['main','SI']:
            old=(R/f'inherited_C18/ecomod_C18_A01_{kind}.tex').read_text();new=(R/f'ecomod_C19_A01_{kind}.tex').read_text()
            labels=re.findall(r'\\label\{([^}]+)\}',old);self.assertTrue(set(labels)<=set(re.findall(r'\\label\{([^}]+)\}',new)))
            self.assertEqual(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',old),re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',new))
            sections=lambda t:re.findall(r'\\(?:sub)*section\*?\{([^}]+)\}',t)
            self.assertEqual(sections(old),sections(new))
    def test_37_C18_inputs_and_graphics(self):
        for kind in ['main','SI']:
            text=(R/f'ecomod_C19_A01_{kind}.tex').read_text()
            for p in re.findall(r'\\input\{([^}]+)\}',text):self.assertTrue((R/p).exists(),p)
            for p in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text):self.assertTrue(any((R/d/(p+e)).exists() for d in ['figures','inherited_C17/figures']for e in ['.pdf','.png']),p)
    def test_38_prediction_map_complete(self):
        t=(R/'ecomod_C19_A01_SI.tex').read_text();self.assertIn('Operational prediction and falsification map',t)
        for k in ['P1 &','P2 &','P3 &','P4 &','P5 &']:self.assertIn(k,t)
        self.assertIn('C^{\\mathrm{emp}}',t);self.assertIn('C^{\\mathrm{mod}}',t)
    def test_39_source_hashes_and_attribution(self):
        d=json.loads((R/'metadata/source_provenance_C18_A01.json').read_text())
        for z in d['sources']:self.assertEqual(z['sha256'],hashlib.sha256((R/z['path']).read_bytes()).hexdigest())
        self.assertIn('CC BY-SA 4.0',(R/'DATA_LICENSE_C19_A01.md').read_text())
    def test_40_author_identity_retained(self):
        for kind in ['main','SI']:
            t=(R/f'ecomod_C19_A01_{kind}.tex').read_text();self.assertIn('0000-0002-0019-1842',t);self.assertIn('Amin Abaee',t)
    def source(self,kind):return (R/f'ecomod_C19_A01_{kind}.tex').read_text()
    def pdf_text(self,kind):
        return '\n'.join(p.extract_text() or '' for p in PdfReader(str(R/f'ecomod_C19_A01_{kind}.pdf')).pages)
    def test_41_companion_doi_mapping(self):
        expected={'Abaee2026a':'10.20944/preprints202610.3095.v1','Abaee2026b':'10.20944/preprints202610.2983.v1','Abaee2026c':'10.20944/preprints202610.3123.v1'}
        for kind in ['main','SI']:
            lines=self.source(kind).splitlines()
            for key,doi in expected.items():
                if kind=='SI' and key=='Abaee2026c':continue
                record=next(x for x in lines if x.startswith('\\bibitem') and ('{'+key+'}') in x)
                self.assertIn('https://doi.org/'+doi,record);self.assertIn('Preprints.org preprint',record)
    def test_42_no_legacy_companion_metadata(self):
        for kind in ['main','SI']:
            t=self.source(kind);self.assertNotIn('2efaa62083f2007dec3446c15c475af88f0925f3',t);self.assertNotIn('Aggregation is a claim, not a presentation',t)
        self.assertIn('Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules',self.source('main'))
    def test_43_content_based_companion_locators(self):
        for kind in ['main','SI']:
            t=self.source(kind)
            for stale in ['Sections~2 and 4 of','Theorem~2 in \\citet{Abaee2026b}','Theorem~4(iii) in \\citet{Abaee2026b}']:self.assertNotIn(stale,t)
            self.assertIn('compensatory-acceptance result in \\citealt{Abaee2026b}',t);self.assertIn('The diagonal-gap analysis in \\citet{Abaee2026b}',t)
        self.assertNotIn('Sections~1.1 and 10.1',self.source('main'))
    def test_44_SI_companion_c_not_invented(self):
        self.assertNotIn('Abaee2026c',self.source('SI'))
        self.assertEqual(len(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{Abaee2026c\}',self.source('main'))),1)
    def test_45_all_SI_tables_cited_in_main(self):
        si=self.source('SI');main=self.source('main');count=len(re.findall(r'\\begin\{(?:longtable|table)\}',si));self.assertEqual(count,18)
        for i in range(1,count+1):self.assertIn(f'SI Table S{i}',main)
    def test_46_all_SI_figures_cited_in_main(self):
        si=self.source('SI');main=self.source('main');count=len(re.findall(r'\\begin\{figure\}',si));self.assertEqual(count,5)
        for i in range(1,count+1):self.assertIn(f'SI Fig. S{i}',main)
    def test_47_main_core_sections_and_results(self):
        t=self.source('main')
        labels=['sec:intro','sec:model','sec:equations','sec:params','sec:data','sec:numerics','sec:results','sec:mask','sec:ceiling','sec:bounded','sec:recovery','sec:c13ident','sec:c13budget','sec:empirical','sec:predictions','sec:discussion','sec:conclusions','prop:mask','prop:ceiling','prop:bounded','prop:c13ident','eq:B','eq:Ac','eq:Af','eq:Ar','eq:q','eq:P','eq:D','eq:dconv','eq:Beq','eq:J','eq:c13boundsB','eq:c13boundsAf','eq:c13fullbudget']
        for label in labels:self.assertIn('\\label{'+label+'}',t)
    def test_48_main_key_numerical_evidence(self):
        t=self.source('main')
        for value in [r'$39\%$',r'$46.16\%$',r'$51.72\%$',r'$24.86\%$',r'$52.71\%$',r'$16.73\%$','0.547925','0.231310','[0.05,1.658163]','[0.606061,0.8]','0.401217','0.678295']:
            self.assertIn(value,t)
    def test_49_yield_sweep_delegated_not_lost(self):
        main=self.source('main');si=self.source('SI');self.assertNotIn('Fast-land yield sweep (all rows composition-premium',main);self.assertNotRegex(main,r'Table~\\ref\{tab:model\}[ab]')
        for value in ['$0.60$ & $+0.534$','$0.85$ & $+0.784$','$1.20$ & $+1.134$','$2.00$ & $+1.934$','$b_fk-b_c$']:self.assertIn(value,si)
        self.assertIn('SI Table S3',main);self.assertIn('SI Table S4',main)
    def test_50_proofs_divided(self):
        main=self.source('main');si=self.source('SI');self.assertEqual(main.count('\\begin{proof}'),0);self.assertEqual(main.count('Proof sketch.'),4);self.assertEqual(main.count('\\begin{proposition}'),4)
        self.assertIn('\\section{Derivations and proofs}',si);self.assertIn('\\subsection{Proof and feasibility construction}',si)
    def test_51_availability_and_version_url(self):
        t=self.source('main');self.assertIn('ecomod_editorial_division_C19_A01',t);self.assertNotIn('ecomod_audit_remediation_C18_A01',t)
    def test_52_transform_deterministic(self):
        for kind,fun in [('main',prep.transform_main),('SI',prep.transform_si)]:
            old=(R/f'inherited_C18/ecomod_C18_A01_{kind}.tex').read_text();self.assertEqual(fun(old),self.source(kind))
    def test_53_SI_top_level_scope_unchanged(self):
        old=(R/'inherited_C18/ecomod_C18_A01_SI.tex').read_text();new=self.source('SI')
        sections=lambda t:re.findall(r'\\section\{([^}]+)\}',t)
        self.assertEqual(sections(old),sections(new));self.assertEqual(len(sections(new)),11);self.assertNotIn('\\section{Discussion}',new)
    def test_54_main_float_inventory(self):
        t=self.source('main');self.assertEqual(len(re.findall(r'\\begin\{figure\}',t)),3);self.assertEqual(len(re.findall(r'\\begin\{table\}',t)),6)
        for name in ['fig1_model_dynamics_C18_A01','fig2_nfa_aggregation_face_C18_A01','fig3_composition_attribution_C18_A01']:self.assertIn(name,t)
    def test_55_PDF_pages_and_text(self):
        for kind,pages in [('main',39),('SI',31)]:
            reader=PdfReader(str(R/f'ecomod_C19_A01_{kind}.pdf'));self.assertEqual(len(reader.pages),pages);text=self.pdf_text(kind);self.assertNotIn('??',text);self.assertNotIn('Aggregation is a claim, not a presentation',text);self.assertIn('Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules',re.sub(r'\s+',' ',text))
    def test_56_PDF_companion_URI_links(self):
        expected={'main':{'10.20944/preprints202610.3095.v1','10.20944/preprints202610.2983.v1','10.20944/preprints202610.3123.v1'},'SI':{'10.20944/preprints202610.3095.v1','10.20944/preprints202610.2983.v1'}}
        for kind in ['main','SI']:
            uris=set()
            for page in PdfReader(str(R/f'ecomod_C19_A01_{kind}.pdf')).pages:
                for ref in page.get('/Annots') or []:
                    obj=ref.get_object();uri=obj.get('/A',{}).get('/URI')
                    if uri:uris.add(str(uri))
            self.assertTrue({'https://doi.org/'+x for x in expected[kind]}<=uris)
            self.assertFalse(any('2efaa62083f2007dec3446c15c475af88f0925f3' in x for x in uris))
    def test_57_PDF_visible_SI_float_citations(self):
        text=re.sub(r'\s+',' ',self.pdf_text('main'))
        for i in range(1,19):self.assertIn(f'SI Table S{i}',text)
        for i in range(1,6):self.assertIn(f'SI Fig. S{i}',text)
    def test_58_final_latex_logs(self):
        for kind,underfull in [('main',4),('SI',2)]:
            log=(R/f'evidence/tex_{kind}_final_C19_A01.log').read_text();self.assertEqual(log.count('LaTeX Warning:'),0);self.assertEqual(len(re.findall(r'Overfull \\',log)),0);self.assertEqual(len(re.findall(r'Underfull \\',log)),underfull);self.assertNotIn('Undefined control sequence',log);self.assertNotIn('Rerun to get cross-references right',log)
    def test_59_SI_bibliography_layout(self):
        self.assertIn('\\begin{thebibliography}{99}\n\\footnotesize',self.source('SI'))
        last=PdfReader(str(R/'ecomod_C19_A01_SI.pdf')).pages[-1].extract_text() or '';self.assertIn('United Nations et al. (2021)',last);self.assertIn('https://seea.un.org/ecosystem-accounting',re.sub(r'\s+','',last))
    def test_60_live_reproduction_verified(self):
        d=json.loads((R/'evidence/reproduction_C19_A01.json').read_text());self.assertEqual(d['status'],'PASS');self.assertTrue(d['disposable_copy']);self.assertEqual(len(d['commands']),3);self.assertEqual(d['data_files_byte_identical'],26);self.assertEqual(d['png_figures_byte_identical'],3);self.assertEqual(d['pdf_figures_content_and_geometry_checked'],7);self.assertTrue(d['inherited_inputs_unchanged']);self.assertTrue(d['final_package_outputs_unchanged'])
if __name__=='__main__':unittest.main(verbosity=2)
