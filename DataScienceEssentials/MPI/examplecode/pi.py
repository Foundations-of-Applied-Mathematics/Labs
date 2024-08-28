# pi.py
import numpy as np
from scipy import linalg as la


# Get 2000 random points in the 2-D domain [-1,1]x[-1,1].
points = np.random.uniform(-1, 1, (2, 2000))

# Determine how many points are within the unit circle.
lengths = la.norm(points, axis=0)
num_within = np.count_nonzero(lengths < 1)

# Estimate the circle's area.
print(4 * (num_within / 2000))
