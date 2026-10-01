#!/usr/bin/env python3
"""Independent exact-source witnesses, ARV source v9 and live paper09b v2.
Run from any working directory: python3 witnesses.py.
"""
from csv import DictReader
from fractions import Fraction as F
from pathlib import Path

p = Path(__file__).resolve().parent

def rows(name):
    with (p/name).open(encoding='utf-8-sig', newline='') as f:
        return list(DictReader(f))

ssb = {int(row['year']): F(row['ssb_kt']) for row in rows('paperE1_calibration_data_v1_wave_e_cod/ncam_2016_table_a2.csv')}
ref = list(range(1983, 1990))
windows = [(i,k) for k in range(1,7) for i in range(7-k)]
net_growing = [(ref[i],ref[i+k]) for i,k in windows if ssb[ref[i+k]] > ssb[ref[i]]]
annual_all_growing = [(ref[i],ref[i+k]) for i,k in windows
                      if all(ssb[ref[j+1]] > ssb[ref[j]] for j in range(i,i+k))]
assert len(windows)==21 and len(net_growing)==15 and len(annual_all_growing)==5
assert (1984,1987) in net_growing and (1984,1987) not in annual_all_growing
print('prop:profile: 15/21 windows have net endpoint growth, but only 5/21 grow at EVERY annual step; 1984->1987 grows in net but declines in 1985->1986')

ram = {}
for row in rows('paperE1_calibration_data_v1_ram_timeseries.csv'):
    if row['SSB']:
        v=F(int(round(float(row['SSB']))))
        if v>10000: v/=1000
        ram[int(float(row['year']))]=v
landings={int(float(row['year'])):F(row['catch_t']) for row in rows('paperE1_calibration_data_v1_wave_e_cod/dfo_2025_table1_landings.csv')}
assert ram[2015]==277 and ssb[2015]==F('298.65') and landings[2015]==4436
share_ram=landings[2015]/(1000*ram[2015]);share_ncam=landings[2015]/(1000*ssb[2015])
assert share_ram==F(1109,69250)<F(23,1000)
assert share_ncam<F(23,1000)
print('prop:recovery: 2015 catch share of same-vintage RAM biomass = 4436/(277000) =',share_ram,'~ 1.60%, not in stated 2.3%-3.0% for 2015-2021; NCAM share also ~ 1.49%')

# prop:discrimination states a mean threshold puts roughly half a window
# below it 'by construction'. For any positive seven-element window,
# mean guarantees straddling (unless all equal), but not near-half counts.
x=[F(1)]+[F(10)]*6
mean=sum(x)/len(x)
assert mean==F(61,7) and sum(v<mean for v in x)==1
print('prop:discrimination generalized mean claim: seven strictly positive readings [1,10,10,10,10,10,10] have only one of seven below their mean, not roughly half by construction')
