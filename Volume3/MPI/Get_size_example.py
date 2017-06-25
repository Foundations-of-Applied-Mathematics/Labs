#Get_size_example.py
from mpi4py import MPI
SIZE = MPI.COMM_WORLD.Get_size()
print "The number of processes is {}.".format(SIZE)
