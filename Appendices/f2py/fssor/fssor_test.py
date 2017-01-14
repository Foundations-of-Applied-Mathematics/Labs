import numpy as np
from matplotlib import pyplot as plt
from fssor import fssor
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Construct initial values for iteration.
resolution = 501
U = np.zeros((resolution, resolution))
X = np.linspace(0, 1, resolution)
U[0] = np.sin(2 * np.pi * X)
U[-1] = - U[0]
# Call Fortran subroutine through F2PY.
# Notice that we pass it a Fortran ordered array.
# We do not have to specify array dimensions, but
# we hav not set default values for the tolerance
# or the maximum number of iterations, so we must
# pass those as arguments to the function.
fssor(U.T, 1.9, 1E-8, 10000)

# Plot the results.
X, Y = np.meshgrid(X, X, copy=False)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, U, rstride=20)
plt.show()
