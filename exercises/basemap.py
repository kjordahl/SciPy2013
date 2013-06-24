"""
Exercise: Plotting with basemap

1. Draw a world map centered on Austin, Texas (if possible) 
   in the following projections:
    a) Mercator
    b) Robinson
    c) Orthographic

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
# or choose your own colors...
