#hello.py
from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()

print "Hello world! I'm process number {}.".format(RANK)
