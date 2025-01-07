from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Create different arrays for each process
local_array = np.arange(10) + rank*10
print(f"Process {rank}: Local array = {local_array}")

# Gather all arrays to process 0
gathered_arrays = comm.gather(local_array, root=0)

if rank == 0:
    print(f"Process 0 gathered arrays: {gathered_arrays}")
    # Combine all arrays
    combined = np.concatenate(gathered_arrays)
    print(f"Combined array: {combined}")