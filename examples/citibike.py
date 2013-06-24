"""
Plot locations of Citibike stations in Manhattan

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial
"""
import os
import json
import numpy as np
from descartes.patch import PolygonPatch
import geojson
from pyproj import Proj, transform
import matplotlib.pyplot as plt
from shapely.geometry import shape, Point, MultiPoint, LineString

def plot_polygon(ax, poly, color='red'):
    a = np.asarray(poly.exterior)
    # without Descartes, we could make a Patch of exterior
    ax.add_patch(PolygonPatch(poly, facecolor=color, alpha=0.3))
    ax.plot(a[:, 0], a[:, 1], color='black')

def plot_multipolygon(ax, geom, color='red'):
    """ Can safely call with either Polygon or Multipolygon geometry
    """
    if geom.type == 'Polygon':
        plot_polygon(ax, geom, color)
    elif geom.type == 'MultiPolygon':
        for poly in geom.geoms:
            plot_polygon(ax, poly, color)

cwd = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(os.path.split(cwd)[0], 'data')
jsonfile = os.path.join(datadir, 'manhattan_island_proj.json')
citibikefile = os.path.join(datadir, 'citibike.json')
manhattan = shape(geojson.load(open(jsonfile)))
man_arr = np.asarray(manhattan.exterior)

# load citbike station locations, transform to map coordinates,
# and filter for only those in Manhattan
c = json.load(open(citibikefile))
stations = [(x['longitude'], x['latitude']) for x in c['stationBeanList']]
lon, lat = zip(*stations)
nyp = Proj('+datum=NAD83 +lat_0=40.1666666667 +lat_1=40.6666666667 '
           '+lat_2=41.0333333333 +lon_0=-74 +no_defs +proj=lcc +units=us-ft '
           '+x_0=300000 +y_0', preserve_units=True)
wgs84 = Proj(init='epsg:4326')
x, y = transform(wgs84, nyp, lon, lat)
points = MultiPoint(zip(x, y))
points = MultiPoint([p for p in points.geoms if manhattan.contains(p)])
pt_arr = np.asarray(points)

# make a small buffer that aproximates 59th Street
mp = MultiPoint([Point([978887, 224975]), Point([1009023, 207566])])
s59 = LineString(mp).buffer(0.5)
sp = manhattan.difference(s59)
lower_manhattan = sp.geoms[1]
man_arr = np.asarray(manhattan.exterior)
# TODO: calculate area fractions below 59th Street

# draw buffers around bike stations with 1, 2, and 3 block radius
block = 260 # Manhattan city block (feet)
buffer = points.buffer(1 * block)
one_block = buffer.intersection(manhattan)
buffer = points.buffer(2 * block)
two_blocks = buffer.intersection(manhattan)
buffer = points.buffer(3 * block)
three_blocks = buffer.intersection(manhattan)

fig = plt.figure()
fig.add_subplot(111, aspect='equal')
ax = plt.gca()
west, south, east, north = manhattan.bounds
plt.plot(man_arr[:,0], man_arr[:, 1], 'black')
plot_multipolygon(ax, one_block, 'blue')
plot_multipolygon(ax, two_blocks, 'blue')
plot_multipolygon(ax, three_blocks, 'blue')
plt.plot(pt_arr[:,0], pt_arr[:,1], marker='o', markersize=1, linestyle='None')
plt.ylim(193000, 222000)
plt.xlim(975000, 997000)
plt.show()
