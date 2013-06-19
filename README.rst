This repository contains materials for the tutorial *Using Geospatial Data With Python* to be held Jun 25, 2013, at the SciPy 2013 conference.

Required packages
-----------------

- `pyproj`_ 
- `Basemap`_ plot on map projections using matplotlib
- `gdal`_
- `shapely`_
- `fiona`_
- `psycopg2`_ for connection to PostgreSQL/PostGIS database

Optional packages
------------------

- `Cartopy`_
- `geoJSON`_
- `SQLAlchemy`_

.. _pyproj: http://code.google.com/p/pyproj
.. _Basemap: https://github.com/matplotlib/basemap
.. _Cartopy: http://scitools.org.uk/cartopy
.. _geoJSON: https://pypi.python.org/pypi/geojson
.. _gdal: https://pypi.python.org/pypi/GDAL
.. _shapely: http://toblerity.github.io/shapely
.. _fiona: http://toblerity.github.io/fiona
.. _psycopg2: https://pypi.python.org/pypi/psycopg2
.. _SQLAlchemy: http://www.sqlalchemy.org

Installation instructions
-------------------------

The standard `scientific python stack`_ is a prerequisite for this tutorial before installing the specific packages listed above.  I recommend starting with a standard scientific python distribution such as `Enthought Canopy`_ or `anaconda`_.  All students for SciPy tutorials will have received a free license for Canopy for a limited period of time (also free for `academic use`_, and anyone can use the free Canopy Express).  Other package managers such as Linux distribution tools or `homebrew` for OS X will work for a starting point as well, though I have not tested these.

Install the above packages via your standard package manager when possible.  For packages not available in this way (or if you wish to use a different version than available), you may install directly with `pip` or `easy_install`.  For example, to install Shapely, you may use::

    pip install shapely

Finally, if all else fails, or you wish to be on the bleeding edge, you may install packages from source.  For example::

    git clone https://github.com/Toblerity/Shapely
    cd Shapely
    python setup.py install

will install the current development version of Shapely.



.. _Enthought Canopy: https://www.enthought.com/products/canopy
.. _anaconda: https://store.continuum.io/cshop/anaconda
.. _scientific python stack: http://www.scipy.org/install.html
.. _academic use: https://www.enthought.com/products/canopy/academic

Known installation issues
-------------------------

- Importing shapely in Canopy version 1.0.1 on OS X `fails`_ while loading the GEOS library, and throws an exception of the form `OSError: Could not find library c or load any of its variants`.  This can be fixed by upgrading to Canopy 1.0.3 (available soon) or worked around by setting the following environment variable::

    export DYLD_FALLBACK_LIBRARY_PATH=$(HOME)/lib:/usr/local/lib:/lib:/usr/lib

- The GDAL 1.9.0 package in Canopy fails to find the PROJ.4 library for some operations.  It should work for other use cases.

- Dependency errors installing `psycopg2` in Canopy and EPD.  This may be overcome by downloading the `psycopg2` .egg file from the `Enthought PyPI mirror`_ and installing it manually with the `egginst` command.

.. _fails: http://stackoverflow.com/questions/17072797/enthought-canopy-cytpes-util-find-library-cant-find-libc
.. _Enthought PyPI mirror: https://www.enthought.com/repo/pypi/eggs
