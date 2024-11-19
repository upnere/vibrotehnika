# Magnification factor for a given building
#
# This script calculates the magnification factor (M) of the building's 
# response to the ground motion.
#
# To run the code in the terminal, use the command:
#       python Exe6_skel.py
#

import numpy as np

# Function to calculate the magnification factor M
def magnification_factor(r, zeta):
    #____your code to return M____

# Function to calculate the frequency ratio r
def frequency_ratio(omega_n, omega):
    #____your code to return r____

# Function to calculate the natural frequency omega_n
def natural_frequency(k, m):
    #____your code to return omega_n ____

# Given parameters
m = 1000  # mass of the building (kg)
k = 50e3  # stiffness of the building (N/m)
zeta = 0.05  # damping ratio
omega = 2 * np.pi  # frequency of the ground motion (rad/s)

# Calculate the natural frequency
omega_n = natural_frequency(k, m)
# Calculate the frequency ratio
r = frequency_ratio(omega_n, omega)
# Calculate the magnification factor
M = magnification_factor(r, zeta)

# Output the results
print(f"Natural frequency (omega_n): {omega_n:.2f} rad/s")
print(f"Frequency ratio (r): {r:.2f}")
print(f"Magnification factor (M): {M:.2f}")