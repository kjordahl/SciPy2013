"""
Exercise: Reading a shapefile with Fiona

1. Create a list of all the unique rock types in the data
   (in properties ROCKTYPE1 and ROCKTYPE2).

2. Calculate the total area of each primary rocktype (ROCKTYPE1) by summing
   the property AREA.  NOTE: The areas are in square degrees, not true area.

3. Plot the polygons in the data with basemap, coloring by primary rock type.

BONUS:

4. Calculate the total area again, this time by using Shapely to calculate the
   area of each polygon.  HINT: You may want to use New Jersey State Plane
   coordinates (EPSG:32111) to get true area.


Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""

import os
import zipfile
from collections import defaultdict
import pprint

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import fiona

# check that shapefile exists and unzip if necessary
cwd = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(os.path.split(cwd)[0], 'data')
geodir = os.path.join(datadir, 'NJgeol_dd')
shpfile = os.path.join(geodir, 'njgeol_poly_dd.shp')
if not os.path.exists(shpfile):
    zf = zipfile.ZipFile(geodir + '.zip', 'r')
    os.mkdir(geodir)
    zf.extractall(geodir)

# 1. Create a list of all the unique rock types in the data
rocks = []
with fiona.open(shpfile) as f:
    for rec in f:
        rocks.append(rec['properties']['ROCKTYPE1'])
        rocks.append(rec['properties']['ROCKTYPE2'])
        if rec['geometry']['type'] != 'Polygon':
            print rec['geometry']['type']
rocks = list(set(rocks))
rocks.sort()
pprint.pprint(rocks)

# 2. Calculate the total area of each primary rocktype
area_dict = defaultdict(lambda: 0)
with fiona.open(shpfile) as f:
    for rec in f:
        rocktype = rec['properties']['ROCKTYPE1']
        area = rec['properties']['AREA']
        area_dict[rocktype] += area
rock_areas = area_dict.items()
# sort rock types in ascending order by area
rock_areas.sort(key=lambda x: x[1])
pprint.pprint(rock_areas)

# 3. Plot the polygons in the data with basemap, coloring by primary rock type.
fig = plt.figure(frameon=False)
west, east, south, north = -75.6, -73.5, 38.5, 41.5
m = Basemap(projection='merc', llcrnrlat=south, urcrnrlat=north,
            llcrnrlon=west, urcrnrlon=east, lat_ts=0, resolution='l')
ax = plt.gca()
plt.axis('off')
# generate a random colormap as needed
colormap = defaultdict(lambda: np.random.random(3))
with fiona.open(shpfile) as f:
    for rec in f:
        coords = rec['geometry']['coordinates'][0]
        rocktype = rec['properties']['ROCKTYPE1']
        x, y = m(*zip(*coords))
        poly = Polygon(zip(x, y), facecolor=colormap[rocktype])
        ax.add_patch(poly)
#m.drawcoastlines()
m.drawmapboundary() 
#plt.title('Bedrock Geology of New Jersey')
plt.show()
# TODO: generate a useful legend
# TODO: use more sensible, consistent colors

# 4. Calculate the total area again, this time by using Shapely
# Left as an exercise...
