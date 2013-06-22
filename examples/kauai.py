"""
Read a raster file a numpy array with GDAL

IMG format files of Kauai downloaded from The National Map
http://nationalmap.gov

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from osgeo import gdal

# GDAL does not use python exceptions by default
gdal.UseExceptions()

cwd = os.path.dirname(__file__)
datadir = os.path.join(os.path.split(cwd)[0], 'data')

img_n = os.path.join(datadir,'kauai_north', 'imgn23w160_1.img')
img_s = os.path.join(datadir,'kauai_south', 'imgn22w160_1.img')
geo = gdal.Open(img_n)
drv = geo.GetDriver()
print drv.GetMetadataItem('DMD_LONGNAME')
north = geo.ReadAsArray()
geo = gdal.Open(img_s)
south = geo.ReadAsArray()
topo = np.vstack((north, south))
i, j = np.where(topo>0)
topo = topo[min(i):max(i)+1, min(j):max(j)+1]
topo[topo==0] = np.nan
print topo.shape

fig = plt.figure(frameon=False)
plt.imshow(topo, cmap=cm.BrBG_r)
plt.axis('off')
cbar = plt.colorbar(shrink=0.75)
cbar.set_label('meters')
plt.savefig('kauai.png', dpi=300, bbox_inches='tight')
plt.show()
