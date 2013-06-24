"""
Heatmap of geolocated tweets in New York City area for approximately one week
Data file tweets.dat contains binary lon/lat data only

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm

N = 405146
west, south, east, north = -74.26, 40.50, -73.70, 40.92
#west, south, east, north = -74.03, 40.69, -73.93, 40.82
cwd = os.path.dirname(os.path.abspath(__file__))
datadir = os.path.join(os.path.split(cwd)[0], 'data')
tweetfile = os.path.join(datadir, 'tweets.dat')
ll = np.dtype([('lon', np.float32), ('lat', np.float32)])
tweets = np.memmap(tweetfile, dtype=ll, mode='r', shape=(N,))

fig = plt.figure()
ax = fig.add_subplot(111)
m = Basemap(projection='merc', llcrnrlat=south, urcrnrlat=north,
            llcrnrlon=west, urcrnrlon=east, lat_ts=south, resolution='i')
x, y = m(tweets['lon'], tweets['lat'])
m.hexbin(x, y, gridsize=400,
         bins='log', cmap=cm.YlOrRd_r)
plt.title("Twitter Heatmap")
plt.savefig('tweets.png', dpi=300, bbox_inches='tight')
plt.show()
