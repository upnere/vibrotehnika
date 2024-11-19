# A high-speed train structure
#
# Usage: python Exe7_skel.py
#

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Given constants
F0 = 10        # N
omega = 5      # rad/s
m = 2          # kg
c = 0.5        # Ns/m
k = 20         # N/m

# Define the system of first-order ODEs
# y[0] = displacement (y), y[1] = velocity (dy/dt)
def model(y, t):
    #______ your code for dydt and dvdt _____

    return [dydt, dvdt]

# Initial conditions
y_init = [0, 0]  # Initial displacement and velocity

# Time points for the solution
t = np.linspace(0, 10, 1000)  # From 0 to 10 seconds

# Numerical solution
y_num = odeint(model, y_init, t)
y_displacement = y_num[:, 0]

# Plotting the results
plt.figure(figsize=(10, 6))
#_____ your code to plot solution ______

plt.savefig('train_structure.png')
