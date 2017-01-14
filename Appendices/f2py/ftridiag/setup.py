from numpy.distutils.core import setup, Extension
ext = Extension('ftridiag',
                sources=['ftridiag.f90'],
                extra_f90_compile_args=['-O3', '-march=native'])
setup(ext_modules=[ext])
