# Simple matrix multiplication problem.
# MPI for parallelization.

import numpy as np
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the matrix size
N = 1000
A = np.random.rand(N, N)
B = np.random.rand(N, N)
C = np.zeros((N, N))

# Define the number of rows to be computed by each process
nrows = N // size

# Start the timer
start = time.time()

# Scatter the rows of A to all processes
local_A = np.zeros((nrows, N))
comm.Scatter(A, local_A, root=0)

# Broadcast B to all processes
comm.Bcast(B, root=0)

# Perform the matrix multiplication
local_C = np.dot(local_A, B)

# Gather the results
comm.Gather(local_C, C, root=0)

# Stop the timer
end = time.time()

# Print the time taken
if rank == 0:
    print("Time taken: ", end - start)
