"""
Generate maps of the continental United States in several projections
and save to PNG files

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Options common to all projections
common_opts = dict(resolution='l', area_thresh=10000)
water_color = (0.8, 0.75, 1.0)
land_color = 'white'
dpi = 300
# Projection-specific options
proj_opts = {}
proj_opts['merc'] = dict(llcrnrlat=24, urcrnrlat=50,
                         llcrnrlon=-126, urcrnrlon=-65,
                         lat_ts=27)
proj_opts['laea'] = dict(lat_0=39, lon_0=-95,
                         llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
                         urcrnrlat=49)
proj_opts['lcc'] = dict(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
                        urcrnrlat=49, lat_1=33, lat_2=45,
                        lon_0=-95)
proj_opts['cyl'] = proj_opts['merc'].copy()

fig = plt.figure(frameon=False)

def draw(m, proj):
    m.drawcoastlines()
    m.fillcontinents(color=land_color, lake_color=water_color)
    m.drawcountries(linewidth=1)
    m.drawstates()
    # draw parallels and meridians.
    #m.drawparallels(np.arange(20.,50.,5.))
    #m.drawmeridians(np.arange(-120.,-60.,5.))
    m.drawmapboundary(fill_color=water_color)
    plt.savefig(proj, dpi=dpi, bbox_inches='tight')

for proj, opts in proj_opts.iteritems():
    opts['projection'] = proj
    opts.update(common_opts)
    m = Basemap(**opts)
    draw(m, proj)
    plt.clf()
