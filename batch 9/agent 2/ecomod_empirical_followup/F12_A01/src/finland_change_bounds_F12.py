#!/usr/bin/env python3
"""Actual inventory-cycle volume inference without imposing cross-cycle independence.
Bonferroni endpoint intervals need marginal normal approximations, not joint normality.
A separate moment-bound sensitivity does not resolve the change sign.
"""
import argparse,csv,hashlib,json,math
from pathlib import Path
from statistics import NormalDist
from openpyxl import load_workbook
from accounts_F12 import require,save
ROOT=Path(__file__).resolve().parents[1]

def norm(s):return ' '.join(str(s).lower().split())

def extract(path,sheet,identity):
 require(hashlib.sha256(path.read_bytes()).hexdigest()==identity['sha256'],'Inventory workbook drift')
 s=load_workbook(path,read_only=True,data_only=True)[sheet];reg=site=None;found=[]
 for n,row in enumerate(s.values,1):
  if row[0]is not None:reg=norm(row[0])
  if row[1]is not None:site=norm(row[1])
  if reg=='whole country'and site in {'total','mineral soils and peatland total'}and norm(row[2])=='total':
   require(isinstance(row[13],(int,float))and isinstance(row[14],(int,float)),'Missing inventory total/SE')
   found.append(dict(inventory='NFI12'if sheet=='20a'else'NFI13',volume_million_m3=row[13]/1000,SE_million_m3=row[14]/1000,source_sha256=identity['sha256'],sheet=sheet,volume_cell=f'N{n}',SE_cell=f'O{n}',source_unit='1000 m3',national_domain='productive and poorly productive forest',sampling_not_total_model_uncertainty=True))
 require(len(found)==1,'Ambiguous country total');return found[0]

def bounds(d,se0,se1,alpha=.05):
 require(se0>=0 and se1>=0 and 0<alpha<1,'Invalid uncertainty parameters')
 z=NormalDist().inv_cdf(1-alpha/4);radius=z*(se0+se1)
 # Union bound: each marginal two-sided 1-alpha/2 interval; no assumed copula.
 return d-radius,d+radius,z

def run(paths):
 registry=json.loads((ROOT/'metadata/source_registry_F12.json').read_text())
 r0=extract(paths[0],'20a',registry['FIN_NFI12_tables.xlsx']);r1=extract(paths[1],'Table 55',registry['FIN_NFI13_tables.xlsx']);save('data/FIN_inventory_volume_SE_source_cells_F12.csv',[r0,r1])
 d=r1['volume_million_m3']-r0['volume_million_m3'];s0=r0['SE_million_m3'];s1=r1['SE_million_m3'];lo,hi,z=bounds(d,s0,s1);rounding_budget=.001+z*.001;lo-=rounding_budget;hi+=rounding_budget
 # Separate a normal-approximation result from a moment-bound sensitivity.
 worst_sd=s0+s1;moment_radius=math.sqrt(1/.05)*worst_sd
 biasrows=[]
 for b in [0,5,10,15,20,30,50]:
  biasrows.append(dict(differential_bias_bound_Mm3=b,lower_Mm3=lo-b,upper_Mm3=hi+b,positive_under_assumptions=lo-b>0,bias_budget_measured=False,marginal_normal_approximation=True))
 save('data/FIN_cycle_volume_bias_sensitivity_F12.csv',biasrows)
 account=list(csv.DictReader((ROOT/'data/FIN_forest_account_volume_2022_2023_F12.csv').open()));a={}
 for r in account:a.setdefault(int(r['year']),{})[r['item']]=None if r['volume_thousand_m3']==''else float(r['volume_thousand_m3'])/1000
 balances=[]
 for y,items in sorted(a.items()):
  opening,closing=items['Opening stocks'],items['Closing stocks'];net=items['Net increment']-items['Removals']-items['Irretrievable losses'];adjust=items['Statistical reclassification (+/-)']+items['Balancing item (+/-)'];residual=closing-opening-net-adjust
  require(abs(residual)<=.003,'Forest account stock-flow balance inconsistent')
  # Revaluation is not a physical volume flow; the table reports null, retained above.
  balances.append(dict(year=y,opening_Mm3=opening,closing_Mm3=closing,reported_stock_change_Mm3=closing-opening,net_increment_minus_removals_and_losses_Mm3=net,reclassification_and_balancing_Mm3=adjust,balance_residual_Mm3=residual,observational_ecological_loss_inferred=False))
 save('data/FIN_forest_account_stock_flow_balance_F12.csv',balances)
 summary=dict(target='National growing-stock volume on productive and poorly productive forest',periods=['NFI12 (2014-2018)','NFI13 (2019-2023)'],point_difference_Mm3=d,percent_change=100*d/r0['volume_million_m3'],marginal_standard_errors_Mm3=[s0,s1],unknown_cross_cycle_covariance=True,independence_assumed=False,normal_Bonferroni_quantile=z,conservative_point_and_SE_rounding_allowance_Mm3=rounding_budget,approx_95pct_simultaneous_endpoint_difference_interval_Mm3=[lo,hi],normal_approximation_sampling_sign='increase',differential_bias_break_even_Mm3=lo,bias_budget_measured=False,moment_only_95pct_two_sided_sensitivity_interval_Mm3=[d-moment_radius,d+moment_radius],moment_only_sign='unresolved',moment_result_conditional_on_unbiased_errors_and_reported_SEs_as_true_variances=True,primary_2015_2023_AGB_hold_lifted=False,secondary_inventory_cycle_volume_inference_admitted_under_stated_assumptions=True,exact_endpoint_biomass_not_inferred=True,total_ecological_condition_not_inferred=True)
 (ROOT/'metadata/FIN_cycle_volume_inference_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));print(balances)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--nfi12',type=Path,required=True);p.add_argument('--nfi13',type=Path,required=True);a=p.parse_args();run([a.nfi12,a.nfi13])
