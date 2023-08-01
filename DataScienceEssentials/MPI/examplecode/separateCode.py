#separateCode.py
from mpi4py import MPI
RANK = MPI.COMM_WORLD.Get_rank()

a = 2
b = 3
if RANK == 0:
  print a + b
elif RANK == 1:
  print a*b
elif RANK == 2:
  print max(a, b)
