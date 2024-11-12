# Exercise 7. Simplified Car Suspension System
#
# To run the code, type in the terminal:
#   python Exe7_skel.py
#

import numpy as np
import matplotlib.pyplot as plt

# Given parameters
M = 1500           # Mass in kg
k1 = 20000         # Stiffness of left spring in N/m
k2 = 20000         # Stiffness of right spring in N/m
c = 1500           # Damping coefficient in Ns/m
x0 = 0.1           # Initial displacement in m
v0 = 0.1           # Initial velocity in m/s
time_duration = 10 # Duration of simulation in seconds
dt = 0.01          # Time step for Euler's method

# Calculate equivalent stiffness


# Initialize variables for Euler's method
n_steps = int(time_duration / dt)
time = np.linspace(0, time_duration, n_steps)
x = np.zeros(n_steps)  # Displacement
v = np.zeros(n_steps)  # Velocity

# Set initial conditions
x[0] = x0
v[0] = v0

# Euler's method for solving ODE
for i in range(1, n_steps):


# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(time, x, label="Displacement $x(t)$")
plt.title("Free Vibration Response of a Damped System using Euler's Method")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend()
plt.grid(True)
plt.show()
