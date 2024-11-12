# Exercise 5. Free Vibration of a Torsional System
#
# To run the code, type in the terminal:
#   python Exe5_skel.py

import math

# Given data
L = 1.5  # meters
d = 0.05  # meters
Jd = 0.1  # kg·m^2
G = 79 * 10**9  # Pascals (GPa to Pa)

# Calculate the polar moment of inertia (J) of the shaft's cross-section
# use math.pi for pi
#__your code__

# Calculate the torsional stiffness (kt)
#__your code__

# Calculate the natural frequency (ωn)
#__your code__

# Convert to the frequency in Hz
#__your code__

print(f"The natural frequency of the torsional vibration is {f:.2f} Hz")
