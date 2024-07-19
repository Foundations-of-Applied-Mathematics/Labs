#hello.py
from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()

print(f"Hello world! I'm process number {RANK}.")
