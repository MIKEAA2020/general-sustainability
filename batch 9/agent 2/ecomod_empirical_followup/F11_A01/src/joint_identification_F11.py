#!/usr/bin/env python3
"""Joint sharp identified set for nested mapped groups, retaining cell mass.
Three disjoint classes: formations A, added savanna S, and complement O.
Group H=A+S. Results condition on exact maps and unconstrained nonnegative
allocation, with no temporal coupling. No physical validation is implied.
"""
import argparse
import itertools
import json
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from identification_F11 import BASE, native, require, topology_bounds, write_csv


def polygon_vertices(a_bounds, h_bounds, s_bounds):
    """Joint polygon in coordinates (A,H), with S=H-A."""
    matrix=np.array([[1,0],[-1,0],[0,1],[0,-1],[-1,1],[1,-1]],float)
    rhs=np.array([a_bounds[1],-a_bounds[0],h_bounds[1],-h_bounds[0],s_bounds[1],-s_bounds[0]])
    points=[]
    for i,j in itertools.combinations(range(6),2):
        m=matrix[[i,j]]
        if abs(np.linalg.det(m))<1e-12:continue
        p=np.linalg.solve(m,rhs[[i,j]])
        if np.all(matrix@p<=rhs+1e-7) and not any(np.linalg.norm(p-v)<1e-7 for v in points):
            points.append(p)
    require(len(points)>=3,'Non-degenerate polygon required for this experiment')
    p=np.array(points);ordered=p[ConvexHull(p).vertices]
    return ordered,matrix,rhs


def pattern_masses(q, ca, ch, n):
    """Aggregate only cells with identical component-presence constraints.
    This reduction is exact because mass may be assigned freely among every
    available class within each cell; scaling pattern totals by cell mass
    reconstructs a feasible cell-level allocation.
    """
    ca,ch,n=np.asarray(ca,dtype=np.int64),np.asarray(ch,dtype=np.int64),np.asarray(n,dtype=np.int64)
    require(ca.shape==ch.shape==n.shape==q.shape and (0<=ca).all() and (ca<=ch).all()
            and (ch<=n).all() and (n>0).all(),'Nested topology violated')
    code=(ca>0).astype(np.int64)+2*(ch>ca).astype(np.int64)+4*(n>ch).astype(np.int64)
    require((code>0).all(),'Every cell must contain a component')
    masses=np.array([q[code==p].sum()for p in range(1,8)],float)
    return masses,code


def problem(masses0,masses1):
    """Variables x[t,pattern,component]; equality preserves each pattern mass."""
    masses=np.array([masses0,masses1]);require(masses.shape==(2,7),'Wrong pattern dimension')
    require(np.isfinite(masses).all() and (masses>=0).all(),'Invalid pattern mass')
    eq=np.zeros((14,42));bounds=[]
    for t in range(2):
        for p in range(1,8):
            for k in range(3):
                index=t*21+(p-1)*3+k;eq[t*7+p-1,index]=1
                bounds.append((0,None) if p&(1<<k) else (0,0))
    delta_a=np.zeros(42);delta_h=np.zeros(42)
    for t,sign in [(0,-1),(1,1)]:
        for p in range(7):
            delta_a[t*21+p*3]=sign
            delta_h[t*21+p*3:t*21+p*3+2]=sign
    return eq,masses.ravel(),bounds,delta_a,delta_h


def joint_witness(masses0,masses1,sign_a,sign_h):
    eq,rhs,bounds,da,dh=problem(masses0,masses1)
    objective=np.r_[np.zeros(42),-1.]
    aub=np.vstack([np.r_[-sign_a*da,1.],np.r_[-sign_h*dh,1.]])
    result=linprog(objective,A_ub=aub,b_ub=[0.,0.],A_eq=np.column_stack([eq,np.zeros(14)]),
                   b_eq=rhs,bounds=bounds+[(0,None)],method='highs')
    require(result.success,'Joint quadrant LP failed: '+result.message)
    return result.x[:42].reshape(2,7,3),dict(
        formations_sign=sign_a,formations_plus_savanna_sign=sign_h,
        formations_difference_Mg=float(da@result.x[:42]),
        formations_plus_savanna_difference_Mg=float(dh@result.x[:42]),
        maximized_common_signed_margin_Mg=float(result.x[-1]),
        all_components_nonnegative=bool(result.x[:42].min()>=-1e-7),
        maximum_pattern_mass_residual_Mg=float(np.max(np.abs(eq@result.x[:42]-rhs))))


def certify_cells(allocation,masses,codes,q):
    masses=np.asarray(masses,dtype=float)
    worst=0.
    for t in range(2):
        fractions=np.divide(allocation[t],masses[t,:,None],out=np.zeros((7,3)),
                            where=masses[t,:,None]>0)
        cell=fractions[codes[t]-1]*q[t][...,None]
        require((cell>=-1e-9).all(),'Negative reconstructed allocation')
        for k in range(3):
            require(np.all(cell[...,k][(codes[t]&(1<<k))==0]==0),'Mass in absent component')
        worst=max(worst,float(np.abs(cell.sum(axis=-1)-q[t]).max()))
    require(worst<1e-8,'Cell mass reconstruction failed')
    return worst


def run(cache,offline=False):
    source=json.loads((BASE/'metadata/native_probe_provenance.json').read_text())['native_payloads']
    source=[r for r in source if r['ISO3']=='BRA']
    d={r['year']:native(r,cache,offline)['agb']for r in source}
    f=np.load(BASE/'data/brazil/BRA_F05_support_fractions.npz')
    top=np.load(BASE/'data/allocation/overlap_certificates_F07.npz')
    masses=[];codes=[];qs=[];intervals={k:[] for k in ('A','H','S')};pattern_rows=[]
    for y in (2015,2023):
        q=d[y]*f['cell_area_ha'];ca=top[f'forest_formations_intersections_{y}'].astype(np.int64)
        ch=top[f'formations_plus_savanna_intersections_{y}'].astype(np.int64)
        n=top[f'total_intersections_{y}'].astype(np.int64)
        mm,code=pattern_masses(q,ca,ch,n);masses.append(mm);codes.append(code);qs.append(q)
        for k,c in [('A',ca),('H',ch),('S',ch-ca)]:intervals[k].append(topology_bounds(q,c,n))
        for p in range(1,8):
            pattern_rows.append(dict(year=y,availability_pattern=p,
                formations_present=bool(p&1),added_savanna_present=bool(p&2),complement_present=bool(p&4),
                native_cells=int((code==p).sum()),mass_Mg=float(mm[p-1])))
    differences={k:(v[1][0]-v[0][1],v[1][1]-v[0][0])for k,v in intervals.items()}
    vertices,matrix,rhs=polygon_vertices(differences['A'],differences['H'],differences['S'])
    certificates=[]
    for sa,sh in itertools.product((-1,1),repeat=2):
        x,certificate=joint_witness(masses[0],masses[1],sa,sh)
        residual=certify_cells(x,masses,codes,qs)
        require(certificate['maximized_common_signed_margin_Mg']>1e-7,'Strict quadrant not attained')
        certificate.update(cells_per_endpoint=65536,cell_mass_preservation_residual_Mg=residual,
                           native_cell_totals_and_nested_geometry_preserved=True)
        certificates.append(certificate)
    # Independent support-function LP: polygon formula versus original pattern constraints.
    eq,eqrhs,bounds,da,dh=problem(masses[0],masses[1]);worst=0.
    for angle in np.linspace(0,2*np.pi,73):
        direction=np.array([np.cos(angle),np.sin(angle)])
        res=linprog(-direction[0]*da-direction[1]*dh,A_eq=eq,b_eq=eqrhs,bounds=bounds,method='highs')
        require(res.success,'Support-function LP failed')
        worst=max(worst,abs(float((vertices@direction).max()+res.fun)))
    require(worst<1e-6,'Joint polygon fails independent support-function LP')
    write_csv(ROOT/'data/joint_availability_patterns_F11.csv',pattern_rows)
    write_csv(ROOT/'data/joint_quadrant_certificates_F11.csv',certificates)
    write_csv(ROOT/'data/joint_polygon_vertices_F11.csv',
              [dict(vertex=i,formations_difference_Mg=float(p[0]),formations_plus_savanna_difference_Mg=float(p[1]))
               for i,p in enumerate(vertices)])
    summary=dict(disjoint_components=['formations','added_savanna','complement'],
                 endpoint_component_bounds_Mg=intervals,difference_component_bounds_Mg=differences,
                 all_four_strict_sign_quadrants_feasible=True,polygon_vertices=len(vertices),
                 support_function_directions_checked=73,
                 worst_support_function_LP_discrepancy_Mg=worst,
                 joint_allocation_validated_as_ecological_change=False,
                 primary_unrestricted_model=True)
    (ROOT/'metadata/joint_identification_F11.json').write_text(json.dumps(summary,indent=2)+'\n')
    render(vertices,certificates,differences)
    print(json.dumps(summary,indent=2));print('Joint quadrant certificates:',certificates)


def render(vertices,certificates,differences):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon,Rectangle
    plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
    fig,ax=plt.subplots(figsize=(5.8,4.5),layout='constrained')
    v=vertices/1000
    ax.add_patch(Polygon(v,closed=True,facecolor='#d4e8f3',edgecolor='#2166ac',lw=1.4,
                         label='Coherent joint set'))
    aa,hh=differences['A'],differences['H']
    ax.add_patch(Rectangle((aa[0]/1000,hh[0]/1000),(aa[1]-aa[0])/1000,(hh[1]-hh[0])/1000,
                          fill=False,ls='--',lw=1,edgecolor='#777777',label='Separate marginal ranges'))
    ax.axhline(0,color='black',lw=.7);ax.axvline(0,color='black',lw=.7)
    for r in certificates:
        x=r['formations_difference_Mg']/1000;y=r['formations_plus_savanna_difference_Mg']/1000
        ax.plot(x,y,'o',ms=4,color='#b35806')
    ax.plot([],[],'o',ms=4,color='#b35806',label='Coherent quadrant witnesses')
    ax.set(xlabel=r'Formations difference ($10^3$ Mg)',
           ylabel=r'Formations + savanna difference ($10^3$ Mg)')
    ax.set_xlim(aa[0]/1000-25,aa[1]/1000+25);ax.set_ylim(hh[0]/1000-25,hh[1]/1000+25)
    ax.legend(frameon=False,fontsize=9,loc='lower center',bbox_to_anchor=(.5,1.01));ax.grid(alpha=.15)
    for ext in ('pdf','png','svg'):fig.savefig(ROOT/'results'/f'joint_identification_F11.{ext}',dpi=220)
    plt.close(fig)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache',type=Path,default=ROOT/'.cache/native');p.add_argument('--offline',action='store_true')
    a=p.parse_args();run(a.cache,a.offline)
