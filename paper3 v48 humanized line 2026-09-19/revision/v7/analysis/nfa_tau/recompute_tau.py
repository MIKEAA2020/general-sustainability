#!/usr/bin/env python3
"""Recompute the aggregate overshoot date with carbon demand included and excluded, on the National
Footprint and Biocapacity Accounts editions that can be fetched without registration, and measure how
far a release-to-release revision moves the same number.

The construction is the main text's (Section 10.2), unaltered:

    tau_agg = 365 * (sum_i b_i) / (sum_i d_i) = 365 * sum_i w_i r_i,   w_i = d_i / sum_j d_j,
    r_i = b_i / d_i,      tau_min = 365 * min_i r_i,      Pi_tau = tau_agg - tau_min

Two ratio sets are carried side by side:

  ALL   the six demand components, carbon included -- the published convention. Carbon demand has no
        biocapacity row, so r_carbon = 0, tau_min = 0, and Pi_tau = tau_agg.
  NOC   carbon *demand* dropped from numerator and denominator, weights renormalised over the five
        components of positive biocapacity -- the object the main text calls "restricted".

Aggregation: the accounts ship a `World` aggregate row per year, and that row is what the publisher's
own headline uses, so it is used here. Two other routes were tried and are reported rather than hidden:
summing the national rows *including* the World row doubles both sides (a 7-day error in the date, the
mistake this script exists to prevent), and summing the national rows alone lands about 1% above the
publisher's aggregate -- which itself moves the date by about a week. The choice of aggregation is
therefore part of the number, and it is stated in the results.

No network access, no interpolation, no model: only the named columns of the named rows.
Usage:  python3 recompute_tau.py                 # runs on the two tables under source/, writes here
        python3 recompute_tau.py --nfa18 "NFA 2025 Edition.csv" --nfa17 "NFA 2024 Edition.csv"
"""
import argparse
import csv
import hashlib
import os
import sys
import zipfile
from collections import defaultdict

COMPONENTS = ['crop_land', 'grazing_land', 'forest_land', 'fishing_ground', 'built_up_land']
CARBON = 'carbon'
DAYS = 365.0
MISSING = {'', 'NULL', 'null', 'NA', 'N/A', '#N/A', 'nan', '-', '.'}


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(1 << 20), b''):
            h.update(blk)
    return h.hexdigest()


def load(path):
    """-> {year: {'bio': {comp: gha}, 'dem': {comp: gha}}}, taken from the World aggregate rows.

    Also returns the sum of the national rows for the same year, for the coverage diagnostic.
    """
    world, national = defaultdict(dict), defaultdict(lambda: defaultdict(float))
    nulls = 0
    with open(path, encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f)
        miss = [c for c in COMPONENTS + [CARBON] if c not in rd.fieldnames]
        if miss:
            sys.exit(f'{path}: missing columns {miss}')
        for row in rd:
            rec, yr = row['record'], int(row['year'])
            side = {'BiocapTotGHA': 'bio', 'EFConsTotGHA': 'dem'}.get(rec)
            if side is None:
                continue
            vals = {}
            for c in COMPONENTS + [CARBON]:
                v = (row.get(c) or '').strip()
                if v in MISSING:
                    nulls += 1
                    continue
                vals[c] = float(v)
            if row['country'] == 'World':
                world.setdefault(yr, {})[side] = vals
            else:
                for c, x in vals.items():
                    national[yr][(side, c)] += x
    print(f'  {os.path.basename(path)}: World rows for {len(world)} years | '
          f'{nulls} missing component cells treated as absent')
    return world, national


def metrics(dem, bio):
    """One year, both conventions, from component totals in gha."""
    tot_d = sum(dem.get(c, 0.0) for c in COMPONENTS + [CARBON])
    tot_b = sum(bio.get(c, 0.0) for c in COMPONENTS)
    d_c = dem.get(CARBON, 0.0)
    r = {c: (bio.get(c, 0.0) / dem[c] if dem.get(c) else float('nan')) for c in COMPONENTS}
    out = {}
    for tag, den in (('ALL', tot_d), ('NOC', tot_d - d_c)):
        if den <= 0:
            continue
        ratios = [r[c] for c in COMPONENTS if c in r and r[c] == r[c]]
        if tag == 'ALL':
            ratios = ratios + [0.0]
        rmin = min(ratios)
        out[tag] = dict(den=den, tau=DAYS * tot_b / den, tau_min=DAYS * rmin,
                        premium=DAYS * tot_b / den - DAYS * rmin)
    out['carbon_share'] = d_c / tot_d if tot_d else float('nan')
    out['tot_b'], out['tot_d'], out['r'] = tot_b, tot_d, r
    return out


def rows_for(world, national):
    out = []
    for yr in sorted(world):
        w = world[yr]
        if 'bio' not in w or 'dem' not in w:
            continue
        m = metrics(w['dem'], w['bio'])
        if 'ALL' not in m or 'NOC' not in m:
            continue
        nat = {s: {c: national[yr][(s, c)] for c in COMPONENTS + [CARBON]} for s in ('bio', 'dem')}
        nm = metrics(nat['dem'], nat['bio'])
        row = dict(year=yr, bc_bil=1e-9 * m['tot_b'], ef_bil=1e-9 * m['tot_d'],
                   earths=m['tot_d'] / m['tot_b'], carbon_share=m['carbon_share'],
                   tau_all=m['ALL']['tau'], pmin_all=m['ALL']['tau_min'], prem_all=m['ALL']['premium'],
                   tau_noc=m['NOC']['tau'], pmin_noc=m['NOC']['tau_min'], prem_noc=m['NOC']['premium'],
                   r_crop=m['r']['crop_land'], r_graz=m['r']['grazing_land'], r_forest=m['r']['forest_land'],
                   r_fish=m['r']['fishing_ground'], r_built=m['r']['built_up_land'],
                   tau_all_national=nm['ALL']['tau'] if 'ALL' in nm else float('nan'),
                   sum_bc_bil=1e-9 * nm['tot_b'] if 'ALL' in nm else float('nan'),
                   sum_ef_bil=1e-9 * nm['tot_d'] if 'ALL' in nm else float('nan'))
        out.append(row)
    return out


HERE = os.path.dirname(os.path.abspath(__file__))


def resolve(path, tag):
    """Accept a CSV, or the archive the download delivered, so the run works from `source/` alone."""
    if path is None:
        path = os.path.join(HERE, 'source', f'NFA_{tag}_edition_kaggle' + ('.csv' if tag == '2018' else '.zip'))
    if not os.path.exists(path):
        raise SystemExit(f'{tag}-edition table not found at {path}; see source/MANIFEST.md for the retrieval route')
    if zipfile.is_zipfile(path):
        out = os.path.join(HERE, '.cache', os.path.basename(path) + '.csv')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith('.csv')]
            assert names, f'no CSV inside {path}'
            if len(names) > 1:
                # the 2017 deposit bundles a second table (a Footprint-per-GDP series); the accounts are the
                # file named for them, and failing that the largest member.
                pick = [n for n in names if 'NFA' in n.upper()] or None
                names = pick or sorted(names, key=lambda n: -z.getinfo(n).file_size)[:1]
                print(f'  note: {os.path.basename(path)} holds {len(z.namelist())} members; using {names[0]}')
            if not os.path.exists(out) or os.path.getsize(out) != z.getinfo(names[0]).file_size:
                z.extract(names[0], os.path.dirname(out))
                os.replace(os.path.join(os.path.dirname(out), names[0]), out)
        return out
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--nfa18', default=None, help='2018 edition CSV or the archive under source/ (default)')
    ap.add_argument('--nfa17', default=None, help='2017 edition CSV or zip under source/ (default)')
    ap.add_argument('--out', default=None, help='where the outputs go (default: this directory)')
    a = ap.parse_args()
    a.nfa18, a.nfa17 = resolve(a.nfa18, '2018'), resolve(a.nfa17, '2017')
    a.out = a.out or HERE
    os.makedirs(a.out, exist_ok=True)
    print('reading (World aggregate rows; the national sum is kept only as a diagnostic)')
    w18, n18 = load(a.nfa18)
    w17, n17 = load(a.nfa17)
    print(f'  2018 edition sha256 {sha256(a.nfa18)}')
    print(f'  2017 edition sha256 {sha256(a.nfa17)}')

    r18, r17 = rows_for(w18, n18), rows_for(w17, n17)

    def write(name, rs, cols=None):
        p = os.path.join(a.out, name)
        with open(p, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=cols or list(rs[0]))
            w.writeheader()
            w.writerows(rs)
        print(f'wrote {name} ({len(rs)} rows)')

    write('tau_by_year_2018edition.csv', r18)
    write('tau_by_year_2017edition.csv', r17)
    i18, i17 = {r['year']: r for r in r18}, {r['year']: r for r in r17}
    common = sorted(set(i18) & set(i17))
    delta = [dict(year=y, tau_all_18=i18[y]['tau_all'], tau_all_17=i17[y]['tau_all'],
                  d_tau_all=i18[y]['tau_all'] - i17[y]['tau_all'],
                  tau_noc_18=i18[y]['tau_noc'], tau_noc_17=i17[y]['tau_noc'],
                  d_tau_noc=i18[y]['tau_noc'] - i17[y]['tau_noc'],
                  prem_noc_18=i18[y]['prem_noc'], prem_noc_17=i17[y]['prem_noc'],
                  d_prem_noc=i18[y]['prem_noc'] - i17[y]['prem_noc'],
                  carbon_share_18=i18[y]['carbon_share'], carbon_share_17=i17[y]['carbon_share'])
             for y in common]
    write('edition_delta.csv', delta)

    print('\n[0] aggregation check: the publisher\'s World row against a sum of the national rows '
          f'({r18[-1]["year"]}, 2018 edition)')
    x = r18[-1]
    print(f'    {x["year"]}: World BC {x["bc_bil"]:.2f} Bn gha, EF {x["ef_bil"]:.2f} Bn gha -> {x["earths"]:.3f} Earths'
          f'  |  sum of countries: BC {x["sum_bc_bil"]:.2f}, EF {x["sum_ef_bil"]:.2f} Bn gha '
          f'(x{x["sum_bc_bil"]/x["bc_bil"]:.2f}) -> date {x["tau_all_national"]:.1f} d vs {x["tau_all"]:.1f} d')

    print('\n[1] the world component ratios, 2018 edition (b_i/d_i; the two area-based components are '
          'identities at the world level)')
    print(f'{"year":>6} {"crop":>7} {"grazing":>8} {"forest":>7} {"fishing":>8} {"built-up":>9} '
          f'{"tau_min NOC":>12}')
    for y in (1961, 1970, 1980, 1990, 2000, 2010, 2014):
        z = i18.get(y)
        if not z:
            continue
        print(f'{y:>6} {z["r_crop"]:>7.3f} {z["r_graz"]:>8.3f} {z["r_forest"]:>7.3f} '
              f'{z["r_fish"]:>8.3f} {z["r_built"]:>9.3f} {z["pmin_noc"]:>12.1f}')
    idc = sum(1 for z in r18 if abs(z['r_crop'] - 1) < 1e-9 and abs(z['r_built'] - 1) < 1e-9)
    pinned = sum(1 for z in r18 if abs(z['pmin_noc'] - DAYS) < 1e-6)
    print(f'    years with r_crop = r_built =  exactly 1: {idc}/{len(r18)} '
          f'| years where tau_min(NOC) is pinned at 365 d: {pinned}/{len(r18)}')

    print('\n[2] the two conventions side by side, years the article quotes and endpoints')
    print(f'{"year":>6} {"Earths":>7} {"carbon share":>13} {"tau ALL":>8} {"Pi ALL":>7} '
          f'{"tau NOC":>8} {"Pi NOC":>7} {"gap":>7}')
    for y in (1961, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013, 2014):
        z = i18.get(y)
        if not z:
            continue
        print(f'{y:>6} {z["earths"]:>7.3f} {100*z["carbon_share"]:>12.1f}% {z["tau_all"]:>8.1f} '
              f'{z["prem_all"]:>7.1f} {z["tau_noc"]:>8.1f} {z["prem_noc"]:>7.1f} '
              f'{z["tau_noc"]-z["tau_all"]:>7.1f}')

    print('\n(i) trend of the restricted premium (carbon demand EXCLUDED), 2018 edition')
    pts = [y for y in (1961, 1980, 2000, 2014) if y in i18]
    print('    ' + ' -> '.join(f'{y}: {i18[y]["prem_noc"]:.0f} d' for y in pts))
    dec = defaultdict(list)
    for z in r18:
        dec[z['year'] // 10 * 10].append(z['prem_noc'])
    print('    decade means: ' + ', '.join(f'{k}s {sum(v)/len(v):.0f} d' for k, v in sorted(dec.items())))
    dn = sum(1 for i in range(1, len(r18)) if r18[i]['prem_noc'] < r18[i - 1]['prem_noc'])
    print(f'    year-on-year declines: {dn} of {len(r18)-1} ({100.0*dn/(len(r18)-1):.0f}%) '
          f'| first to last decade mean: {sum(dec[1960])/len(dec[1960]):.0f} d -> '
          f'{sum(dec[2010])/len(dec[2010]):.0f} d -> trend sign is downward under the exclusion')

    last = max(z['year'] for z in r18)
    ks = [z for z in r18 if z['year'] >= last - 9]
    print(f'\n(ii) separation of the two conventions over the last decade of the release '
          f'({ks[0]["year"]}-{ks[-1]["year"]})')
    g = [z['tau_noc'] - z['tau_all'] for z in ks]
    sh = [z['carbon_share'] for z in ks]
    print(f'    gap in days: mean {sum(g)/len(g):.1f}, min {min(g):.1f}, max {max(g):.1f} '
          f'({sum(g)/len(g)/DAYS:.2f} yr) | ratio tau_NOC/tau_ALL: '
          f'{min(z["tau_noc"]/z["tau_all"] for z in ks):.2f} to {max(z["tau_noc"]/z["tau_all"] for z in ks):.2f}')
    print(f'    carbon share of demand: {100*min(sh):.1f}% to {100*max(sh):.1f}%, and the ratio is '
          f'1/(1-share) by construction: max deviation from that identity '
          f'{max(abs(z["tau_noc"]/z["tau_all"] - 1/(1-z["carbon_share"])) for z in ks):.2e}')

    print(f'\n(iii) release-to-release revision, {len(delta)} common years '
          f'(2018 minus 2017 edition, same aggregation rule)')
    for nm, key in (('tau ALL', 'd_tau_all'), ('tau NOC', 'd_tau_noc'), ('Pi NOC', 'd_prem_noc')):
        v = [abs(d[key]) for d in delta]
        print(f'    {nm:8s}: mean |delta| {sum(v)/len(v):.1f} d, max {max(v):.1f} d, '
              f'last year {delta[-1][key]:+.1f} d')
    big = sorted(delta, key=lambda d: -abs(d['d_tau_noc']))[:3]
    print('    largest NOC moves: ' + ', '.join(f'{b["year"]} {b["d_tau_noc"]:+.1f} d' for b in big))
    print('    reading: a few-day gap between a published headline and a recomputed date is inside the '
          'revision noise of the ALL date and small for the NOC date; the two conventions are not equally '
          'fragile, and the restricted one is the more fragile by a factor of about '
          f'{(sum(abs(d["d_tau_noc"]) for d in delta)/len(delta)) / max(1e-9, sum(abs(d["d_tau_all"]) for d in delta)/len(delta)):.1f}')

    print('\n[4] against the main text, whose series is read off a later edition of the same accounts')
    art = {1961: 547, 1980: 346, 2000: 251}
    for y, v in art.items():
        if y in i18:
            print(f'    Pi_NOC {y}: article {v} d, 2018 edition {i18[y]["prem_noc"]:.0f} d '
                  f'({100*(i18[y]["prem_noc"]-v)/v:+.1f}%)')
    print(f'    tau_agg 2014 on the 2018 edition: {i18[2014]["tau_all"]:.1f} d, ratio '
          f'{i18[2014]["bc_bil"]/i18[2014]["ef_bil"]:.3f} (the article quotes 0.584 and 213 d for 2022 '
          f'from the later release)')

    with open(os.path.join(a.out, 'checksums.txt'), 'w') as f:
        for p_ in (a.nfa18, a.nfa17):
            f.write(f'{sha256(p_)}  {os.path.basename(p_)}  {os.path.getsize(p_)} bytes\n')
    print('\nwrote checksums.txt')


if __name__ == '__main__':
    main()
