# Setting up requirements for *Using Geospatial Data with Python* tutorial using Anaconda on Mac OS X

**Serge Rey** `<sjsrey@gmail.com>`

`2013-06-21`


Below I explain how to set up an Anaconda environment that isolates the new dependencies required for the [scipy13 tutorial](https://github.com/kjordahl/SciPy2013/blob/master/README.rst).

The installation is done on OS X 10.8.4.

## Set up an Anaconda environment

1. Download [Anaconda](https://store.continuum.io/cshop/anaconda)  
     Get the 64bit version
2. `cd ~/Downloads`
3. `bash <Downloaded file>`  
     During this accept all the defaults and say `yes` when it asks to prepend anaconda to your PATH variable in your .bashrc
4. `cd`
5. `source .bashrc`
6. `ipython`
7.  You should see ipython fire up with info that it is part of Anaconda 1.X or so
8. Quit python and get back to the terminal.
1. `conda create -n scipygis scikit-learn`  
I am using scikit-learn as a departure point for some of the core dependencies (numpy, scipy, etc)
2. Install `setuptools` into this env
	1. Download [setuptools](https://pypi.python.org/packages/source/s/setuptools/setuptools-0.7.4.tar.gz)
	2. `tar xzvf setuptools-0.7.4.tar.gz`
	3. `cd setuptools-0.7.4`
	4. `~/anaconda/envs/scipygis/bin/python setup.py install`
1. Install `pip`
	1. Download [pip](https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz)
	2. `tar xzvf pip-1.3.1.tar.gz`
	3. `cd pip-1.3.1`
	4. `~/anaconda/envs/scipygis/bin/python setup.py install`
	
## Install KingChaos Frameworks


These will get the GDAL and GEOS frameworks installed. If you already have installed these as part of getting [QGIS on the Mac](http://www.kyngchaos.com/software/qgis) up and running, you won't need to reinstall. If so skip to the next section.

1. Download [GDAL Framework](http://www.kyngchaos.com/files/software/frameworks/GDAL_Complete-1.9.dmg)
2. Open the dmg.
3. Double click the `GDAL Complete.pkg` file and install.

## Install GDAL Python wrappers
1. Download [gdal](https://pypi.python.org/packages/source/G/GDAL/GDAL-1.9.1.tar.gz)
2. `cd ~/Downloads`
2. `tar xzvf GDAL-1.9.1.tar.gz`
3. `cd GDAL-1.9.1`
4. `~/anaconda/envs/scipygis/bin/python setup.py build_ext -I/Library/Frameworks/GDAL.framework/Versions/1.9/unix/include -L/Library/Frameworks/GDAL.framework/Versions/1.9/unix/lib -lgdal install`


## Installing Fiona

1. `git clone git://github.com/Toblerity/Fiona.git`
2. `cd Fiona`
1.  `~/anaconda/envs/scipygis/bin/python setup.py build_ext -I/Library/Frameworks/GDAL.framework/Versions/1.9/unix/include -L/Library/Frameworks/GDAL.framework/Versions/1.9/unix/lib -lgdal install`

## Installing Basemap

1. Download [basemap](http://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.6/basemap-1.0.6.tar.gz/download)
2. `tar xzvf basemap-1.0.6.tar.gz`
3. `cd basemap-1.0.6`
3. `export GEOS_DIR=/Library/Frameworks/GEOS.framework/unix`
4. `~/anaconda/envs/scipygis/bin/python setup.py install`



## Other dependencies
All other [dependencies](https://github.com/kjordahl/SciPy2013/blob/master/README.rst) were installed with:

       ~/anaconda/envs/scipygis/bin/pip install <package>
       
The only exception to this is [cartopy](https://github.com/SciTools/cartopy) which I could not get installed within the Anaconda env. I didn't want to go the brew route so I left it out since the [testing script](https://github.com/kjordahl/SciPy2013/blob/master/check_install.py) passes.
       
       
       
       
