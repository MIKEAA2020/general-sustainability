"""Draw observed mapped-cover fractions, not inferred biomass or validated change."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
ROOT=Path(__file__).resolve().parents[1]

def main():
    d=np.load(ROOT/'data/brazil/BRA_F05_support_fractions.npz');lon=d['longitude_centres'];lat=d['latitude_centres'];dx=lon[1]-lon[0];dy=abs(lat[1]-lat[0]);ext=[lon[0]-dx/2,lon[-1]+dx/2,lat[-1]-dy/2,lat[0]+dy/2]
    fig,axes=plt.subplots(1,2,figsize=(8,3.65),layout='constrained',sharex=True,sharey=True)
    for ax,year in zip(axes,[2015,2023]):
        im=ax.imshow(100*d[f'forest_formations_{year}'],extent=ext,origin='upper',vmin=0,vmax=100,cmap='Greens',interpolation='nearest',aspect=1/np.cos(np.deg2rad(lat.mean())));ax.set_title(str(year));ax.set_xlabel('Longitude (degrees)');ax.tick_params(labelsize=8)
    axes[0].set_ylabel('Latitude (degrees)');fig.colorbar(im,ax=axes,label='Mapped formation fraction (%)',shrink=.85);fig.suptitle('Same fixed local footprint; MapBiomas Collection 11',fontsize=11)
    fig.savefig(ROOT/'results/brazil/BRA_F05_support_fractions.pdf',metadata={'Title':'Mapped forest-formations fractions on the fixed Brazil footprint','Creator':'plot_brazil_support.py'});fig.savefig(ROOT/'results/brazil/BRA_F05_support_fractions.png',dpi=170);plt.close(fig)
if __name__=='__main__':main()
