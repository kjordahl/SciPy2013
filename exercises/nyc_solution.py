"""

Exercise: Boroughs of New York City

1. Read the borough boundaries shapefile from data/nybb_13a/nybb.shp
   into a dictionary of Shapely geometries keyed by the property BoroName.
   
2. Calculate the area of each borough.  What are the units?

3. Calculate the fraction of the area of each borough that lies more than 1 km
   (3281 feet) from its boundary

BONUS

4. Extract the simple polygon representing the island (not the borough) of
   Manhattan.  HINT: It will be the largest polygon in the borough.

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import fiona
from shapely.geometry import shape
import geojson

cwd = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(os.path.split(cwd)[0], 'data')
nycdir = os.path.join(datadir, 'nybb_13a')
shpfile = os.path.join(nycdir, 'nybb.shp')

colors = ['red', 'green', 'orange', 'brown', 'purple']

def plot_polygon(ax, poly, color='red'):
    a = np.asarray(poly.exterior)
    ax.add_patch(Polygon(a, facecolor=color, alpha=0.3))
    ax.plot(a[:, 0], a[:, 1], color='black')

def plot_multipolygon(ax, geom, color='red'):
    """ Can safely call with either Polygon or Multipolygon geometry
    """
    if geom.type == 'Polygon':
        plot_polygon(ax, geom, color)
    elif geom.type == 'MultiPolygon':
        for poly in geom.geoms:
            plot_polygon(ax, poly, color)

fig = plt.figure()
fig.add_subplot(111, aspect='equal')
ax = fig.gca()
nyc_geom = {}

# 1. Read the borough boundaries shapefile into a dictionary

with fiona.open(shpfile) as f:
    crs = f.crs
    units = crs['units']
    print 'units', units
    for rec in f:
        color = colors.pop()
        print rec['geometry']['type']
        boro = rec['properties']['BoroName']
        nyc_geom[boro] = shape(rec['geometry'])
        plot_multipolygon(ax, nyc_geom[boro], color=color)

# 2. Calculate the area of each borough.

for boro, geom in nyc_geom.iteritems():
    print '%s area %10.0f square feet (%5.2f sq miles)' % (boro,
                                                           geom.area,
                                                           (geom.area / 27878400))

# 3. Fraction of the area of each borough that lies more than 1 km from boundary

for boro, geom in nyc_geom.iteritems():
    interior = geom.buffer(-3281)
    plot_multipolygon(ax, interior, color='gray')
    print '%4.1f%% of %s more than 1 km from boundary' % (100 * interior.area / geom.area,
                                                          boro)

# 4. Extract the simple polygon representing the island of Manhattan

idx = np.argmax([s.area for s in nyc_geom['Manhattan'].geoms])
manhattan_i = nyc_geom['Manhattan'].geoms[idx]

plt.show()
