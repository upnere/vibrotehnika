import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

x=3
y=np.sin(x)
print(x+y)

print(f"I am process {rank}") 