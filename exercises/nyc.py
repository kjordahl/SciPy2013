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
import fiona
from shapely.geometry import shape

cwd = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(os.path.split(cwd)[0], 'data')
nycdir = os.path.join(datadir, 'nybb_13a')
shpfile = os.path.join(nycdir, 'nybb.shp')
