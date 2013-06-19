"""
Test import of required and optional packages for SciPy 2013 tutorial
Using Geospatial Data With Python

"""

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

print
print 'Required packages:'

try:
    import shapely
    print OK, 'Shapely version', shapely.__version__
except ImportError:
    print FAIL, 'Shapely not installed'

try:
    import fiona
    print OK, 'Fiona version', fiona.__version__
except ImportError:
    print FAIL, 'Fiona not installed'

try:
    import pyproj
    print OK, 'pyproj version', pyproj.__version__
except ImportError:
    print FAIL, 'pyproj not installed'

try:
    import osgeo.gdal
    print OK, 'GDAL version', osgeo.gdal.__version__
except:
    print FAIL, 'GDAL not installed'

try:
    from mpl_toolkits.basemap import __version__
    print OK, 'Basemap version', __version__
except ImportError:
    print FAIL, 'Basemap not installed'

print
print 'Optional packages:'

try:
    import geojson
except ImportError:
    print FAIL, 'geoJSON not installed'
else:
    print OK, 'geoJSON is installed'

