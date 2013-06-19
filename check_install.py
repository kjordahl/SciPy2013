try:
    import shapely
    print 'Shapely version', shapely.__version__
except ImportError:
    print 'Shapely not installed'

try:
    import fiona
    print 'Fiona version', fiona.__version__
except ImportError:
    print 'Fiona not installed'

try:
    import pyproj
    print 'pyproj version', pyproj.__version__
except ImportError:
    print 'pyproj not installed'

try:
    import osgeo.gdal
    print 'GDAL version', osgeo.gdal.__version__
except:
    print 'GDAL not installed'

try:
    from mpl_toolkits.basemap import __version__
    print 'Basemap version', __version__
except ImportError:
    print 'Basemap not installed'

try:
    import geojson
except ImportError:
    print 'geoJSON not installed'
else:
    print 'geoJSON is installed'

