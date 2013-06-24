"""
Exercise: Read a geotiff file as a numpy array and display with matplotlib.

1. Download the data file from http://public.enthought.com/~kjordahl/scipy/manhattan.tif

2. Open the file with GDAL.  What projection is it in?

3. Read the image data into a numpy array and plot as a 3-color image
   with matplotlib.

4. Set the plot axis limits to the proper map coordinates.

BONUS

5. plot the locations of the Citibike stations in the file citibike.json
   (or real-time from http://citibikenyc.com/stations/json)
   
Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""

import os
from osgeo import gdal
import matplotlib.pyplot as plt

# GDAL does not use python exceptions by default
gdal.UseExceptions()

cwd = os.path.dirname(__file__)
datadir = os.path.join(os.path.split(cwd)[0], 'data')

# 1. download from http://public.enthought.com/~kjordahl/scipy/manhattan.tif

# 2.
gtif = os.path.join(datadir, 'manhattan.tif')
geo = gdal.Open(gtif)
print geo.GetProjectionRef()

# 3.
arr = geo.ReadAsArray()
#plt.imshow(arr[:3,:,:].transpose((1, 2, 0)))
#plt.show()

# 4.
trans = geo.GetGeoTransform()
extent = (trans[0], trans[0] + geo.RasterXSize*trans[1],
          trans[3] + geo.RasterYSize*trans[5], trans[3])
plt.imshow(arr[:3,:,:].transpose((1, 2, 0)), extent=extent)
plt.show()
# Could also do this with basemap

# 5.
# As an exercise...