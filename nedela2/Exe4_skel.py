# Exercise 4. Car Suspension System Response
#
# To run the code, type in the terminal:
#   python Exe4_skel.py

import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1500.0  # mass (kg)
k = 20000.0  # spring constant (N/m)
c = 1500.0  # damping coefficient (Ns/m)
x0 = 0.05  # initial displacement (m)
v0 = 0.0  # initial velocity (m/s)
dt = 0.01  # time step (s)
t_max = 5.0  # maximum time (s)

# Time array
t = linspace(0,t_max,100) #np.arange(0,t_max,dt)

# Arrays to store displacement and velocity
x = np.zeros(len(t))
v = np.zeros(len(t))

# Initial conditions
x[0] = x0
v[0] = v0

# Euler method
for i in range(1, len(t)):
    #__your code__

# Plotting
plt.plot(t, x)
plt.title('Car Suspension System Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.show()
