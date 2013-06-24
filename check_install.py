"""
Test import of required and optional packages for SciPy 2013 tutorial
Using Geospatial Data With Python

"""

import sys
print 'Using python in', sys.prefix
print sys.version

def import_version(pkg):
    try:
        exec('from %s import __version__' % pkg)
        print OK, '%s version %s' % (pkg, __version__)
    except ImportError:
        print FAIL, '%s not installed' % pkg

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

import_version('shapely')
import_version('fiona')
import_version('pyproj')

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

import_version('cartopy')
import_version('psycopg2')
import_version('sqlalchemy')
