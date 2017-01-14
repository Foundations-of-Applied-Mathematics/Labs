from numpy.distutils.core import setup, Extension
ext = Extension('ftridiag',
                sources=['ftridiag.f90', 'ftridiag.pyf'],
                extra_f90_compile_args=['-O3', '-march=native'])
setup(ext_modules=[ext])
