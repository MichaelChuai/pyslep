from distutils.core import setup, Extension
from Cython.Build import cythonize
from numpy import get_include

ext_main = Extension('mtLeastR', ['mtLeastR.pyx', 'ep21R.c', 'eppMatrix.c', 'epph.c'], include_dirs=['.', get_include()])

setup(ext_modules=cythonize([ext_main]))
