import numpy as np
from numpy.random import rand
# Import the new module.
from ftridiag import ftridiag as tridiag

# Construct arguments to pass to the function.
n=10
a, b, c, x = rand(n-1), rand(n), rand(n-1), rand(n)
# Construct a matrix A to test that the result is correct.
A = np.zeros((n,n))
A.ravel()[A.shape[1]::A.shape[1]+1] = a
A.ravel()[::A.shape[1]+1] = b
A.ravel()[1::A.shape[1]+1] = c
# Store x so we can verify the algorithm returned
# the correct values
x_copy = x.copy()
# Call the function.
tridiag(a, b, c, x)
# Test to see if the result is correct.
# Print the result in the command line.
if np.absolute(A.dot(x) - x_copy).max() < 1E-12:
    print "Test Passed"
else:
    print "Test Failed"
