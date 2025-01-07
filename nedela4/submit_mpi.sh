#!/bin/bash
#PBS -N mpi_python
#PBS -q batch
#PBS -l walltime=00:30:00
#PBS -l nodes=1:ppn=4
#PBS -j oe

# Load modules
module purge
module load python/3.9.19  # Cluster's Python version
module load mpi
module load compilers/gcc/gcc-11.2.0

# Activate virtual environment
source mpi_env/bin/activate

# Run the MPI program
mpirun -n 4 python test.py

# Deactivate virtual environment
deactivate