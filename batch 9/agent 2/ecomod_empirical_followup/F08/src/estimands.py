"""Small auditable kernels. These functions do not resolve map uncertainty or eligibility."""
import math
import numpy as np


def wgs84_rectangle_area_ha(west, east, south, north):
    """Area between meridians and parallels on WGS84, not equal-area pixel counts.
    Longitudes must form a non-dateline-crossing interval; split crossings first.
    """
    if not (-180 <= west <= east <= 180 and -90 <= south <= north <= 90):
        raise ValueError('Invalid rectangular bounds; split dateline crossings')
    a=6378137.; f=1/298.257223563; e2=f*(2-f); e=math.sqrt(e2)
    def primitive(lat):
        s=math.sin(math.radians(lat))
        return s/(2*(1-e2*s*s))+math.atanh(e*s)/(2*e)
    return a*a*(1-e2)*math.radians(east-west)*(primitive(north)-primitive(south))/1e4


def extent_density_decomposition(area0_ha,area1_ha,stock0_Mg,stock1_Mg):
    """Exact symmetric two-factor identity at one aggregate support.
    Both areas must be positive; this does not invent unobserved density on
    newly appearing/disappearing strata, and is not causal attribution.
    """
    if area0_ha<=0 or area1_ha<=0 or stock0_Mg<0 or stock1_Mg<0:
        raise ValueError('Positive areas and nonnegative stocks required')
    d0=stock0_Mg/area0_ha; d1=stock1_Mg/area1_ha
    extent=(area1_ha-area0_ha)*(d0+d1)/2
    density=(d1-d0)*(area0_ha+area1_ha)/2
    return dict(extent_Mg=extent,density_Mg=density,total_Mg=stock1_Mg-stock0_Mg)


def spatial_cancellation(local_stock_changes_Mg):
    """Observed-support descriptor only; noisy point estimates create cancellation.
    These are offsetting *local net changes*, not observed gross biomass flows.
    An all-zero input has undefined cancellation fraction (None), not a score.
    """
    x=np.asarray(local_stock_changes_Mg,dtype=float)
    if x.ndim!=1 or not np.all(np.isfinite(x)):raise ValueError('Finite 1-D support required')
    gains=float(np.maximum(x,0).sum());losses=float(np.maximum(-x,0).sum());gross=gains+losses
    return dict(positive_local_net_changes_Mg=gains,negative_local_net_changes_Mg=losses,
                net_Mg=gains-losses,offset_Mg=min(gains,losses),
                cancellation_fraction=None if gross==0 else 1-abs(gains-losses)/gross)
