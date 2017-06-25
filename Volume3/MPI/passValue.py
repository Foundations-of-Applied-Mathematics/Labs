#passValue.py
import numpy as np
from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()

if RANK == 1:  # This process chooses and sends a random value
    num_buffer = np.random.rand(1)
    print "Process 1: Sending: {} to process 0.".format(num_buffer)
    COMM.Send(num_buffer, dest=0)
    print "Process 1: Message sent."
if RANK == 0:  # This process recieves a value from process 1
    num_buffer = np.zeros(1)
    print "Process 0: Waiting for the message... current num_buffer={}.".format(num_buffer)
    COMM.Recv(num_buffer, source=1)
    print "Process 0: Message recieved! num_buffer={}.".format(num_buffer)
