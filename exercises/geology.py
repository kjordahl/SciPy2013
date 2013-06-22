"""
Exercise: Reading a shapefile with Fiona

1. Create a list of all the unique rock types in the data
   (in properties ROCKTYPE1 and ROCKTYPE2).

2. Calculate the total area of each primary rocktype (ROCKTYPE1) by summing
   the property AREA.

3. Plot the polygons in the data with basemap, coloring by primary rock type.

BONUS:

4. Calculate the total area again, this time by using Shapely to calculate the
   area of each polygon.  HINT: You may want to use New Jersey State Plane
   coordinates, EPSG:32111


Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""

import os
import zipfile

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import fiona

# check that shapefile exists and unzip if necessary
cwd = os.path.dirname(__file__)
datadir = os.path.join(os.path.split(cwd)[0], 'data')
geodir = os.path.join(datadir, 'NJgeol_dd')
shpfile = os.path.join(geodir, 'njgeol_poly_dd.shp')
if not os.path.exists(shpfile):
    zf = zipfile.ZipFile(geodir + '.zip', 'r')
    os.mkdir(geodir)
    zf.extractall(geodir)
