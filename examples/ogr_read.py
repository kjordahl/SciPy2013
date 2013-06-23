"""
Read a shapefile with OGR

Adapted from OGR API tutorial
http://www.gdal.org/ogr/ogr_apitut.html

Kelsey Jordahl, Enthought
Scipy 2013 geospatial tutorial

"""

import os
import ogr

# OGR does not use python exceptions by default
ogr.UseExceptions()

cwd = os.path.dirname(__file__)
datadir = os.path.join(os.path.split(cwd)[0], 'data')
# unzip if it doesn't already exist
shpfile = os.path.join(datadir, 'NJgeol_dd', 'njgeol_poly_dd.shp')
ds = ogr.Open(shpfile)

lyr = ds.GetLayer(0)
print lyr.GetName()

polygons, rocktypes = [], []
for feat in lyr:
    assert feat.GetFieldDefnRef(9).GetName() == 'ROCKTYPE1'
    rocktypes.append(feat.GetField(9))
    geom = feat.GetGeometryRef()
    if geom is not None and geom.GetGeometryType() == ogr.wkbPolygon:
        # geom.GetGeometryRef(0).GetPoints() # (for outer ring only)
        for ring in geom:
            pts = ring.GetPoints()
            polygons.append(pts)
    else:
        print 'geometry type is', geom.GetGeometryName()

print 'Got %d polygons' % len(polygons)
print len(set(rocktypes)), 'unique rock types'
#close the file
del ds
