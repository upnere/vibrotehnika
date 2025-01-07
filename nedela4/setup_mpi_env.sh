#!/bin/bash
rm -rf mpi_env

# Load required modules
module purge  # Clear all modules first
module load python/3.9.19  # Cluster's Python version
module load mpi
module load compilers/gcc/gcc-11.2.0

# Print loaded modules for verification
module list

# Create virtual environment
echo -e ">>Creating venv 'mpi_env'..."
python3 -m venv --upgrade-deps mpi_env

echo "venv created: $(readlink -f mpi_env )"

# Activate virtual environment
source mpi_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install NumPy and mpi4py
pip install numpy
pip install mpi4py

# Verify installations
python -c "import numpy; print('NumPy version:', numpy.__version__)"
python -c "import mpi4py; print('mpi4py version:', mpi4py.__version__)"

# Deactivate virtual environment
deactivate

echo "Setup complete! To start working:"
echo "1. Load modules: module load python openmpi compiler/gcc"
echo "2. Activate environment: source mpi_env/bin/activate"