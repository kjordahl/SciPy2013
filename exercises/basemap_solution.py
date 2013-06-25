"""
Exercise: Plotting with basemap

1. Draw a world map centered on Austin, Texas (if possible) 
   in the following projections:
    a) Mercator
    b) Robinson
    c) Orthographic
    d) Azimuthal equidistant

2. Plot the following great circle routes on a global map:
    a) Hawaii to Hong Kong
    b) Hong Kong to Moscow
    c) Moscow to Havana, Cuba
    d) Havana to Quito, Ecuador
   Coordinates of these locations are given below.  Try to choose
   projection parameters that allow you to see all of the great circles at once.
   Plot black dots at the start and end points as well.

Author: Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# (lon, lat)
austin = (-97.75, 30.25)
hawaii = (-157.8, 21.3)
hongkong = (114.16, 22.28)
moscow = (37.62, 55.75)
havana = (-82.38, 23.13)
quito = (-78.58, -0.25)

land_color = 'lightgray'
water_color = 'lightblue'

# 1a.
plt.subplot(2, 2, 1)
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, lon_0=austin[0],
            llcrnrlon=-180, urcrnrlon=180, lat_ts=austin[1], resolution='l')
m.drawcoastlines()
m.fillcontinents(color=land_color, lake_color=water_color)
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color=water_color)
plt.title('Mercator')

# 1b.
plt.subplot(2, 2, 2)
m = Basemap(projection='robin', llcrnrlat=-80, urcrnrlat=80, lon_0=austin[0],
            llcrnrlon=-180, urcrnrlon=180, lat_0=austin[1], resolution='l')
m.drawcoastlines()
m.fillcontinents(color=land_color, lake_color=water_color)
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color=water_color)
plt.title('Robinson')

# 1c.
plt.subplot(2, 2, 3)
m = Basemap(projection='ortho', lon_0=austin[0], lat_0=austin[1], resolution='l')
m.drawcoastlines()
m.fillcontinents(color=land_color, lake_color=water_color)
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color=water_color)
plt.title('Orthographic')

# 1d.
plt.subplot(2, 2, 4)
m = Basemap(projection='aeqd', lat_0=austin[1], lon_0=austin[0])
m.drawcoastlines()
m.fillcontinents(color=land_color, lake_color=water_color)
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,420.,60.))
m.drawmapboundary(fill_color=water_color)
plt.title('Azimuthal equidistant')

# 2.
plt.figure()
water_color = 'white'
m = Basemap(projection='robin', llcrnrlat=-80, urcrnrlat=80, lon_0=40,
            llcrnrlon=-180, urcrnrlon=180, lat_0=0, resolution='l')
m.drawcoastlines()
m.fillcontinents(color=land_color, lake_color=water_color)
m.drawgreatcircle(hawaii[0], hawaii[1], hongkong[0], hongkong[1], color='red')
m.drawgreatcircle(hongkong[0], hongkong[1], moscow[0], moscow[1], color='red')
m.drawgreatcircle(moscow[0], moscow[1], havana[0], havana[1], color='red')
m.drawgreatcircle(havana[0], havana[1], quito[0], quito[1], color='red')
x, y = m(*zip(*[hawaii, hongkong, moscow, havana, quito]))
#m.scatter(x, y, marker='o', size=10, color='black')
m.plot(x, y, marker='o', markersize=6, markerfacecolor='black', linewidth=0)
m.drawmapboundary(fill_color=water_color)
plt.title('Great Circle Escape')

plt.show()
