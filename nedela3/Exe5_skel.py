# Magnification factor for a SDOF system
# ---------------------------------------
# This script plots the magnification factor M as a function of the frequency ratio r 
# for three damping ratios: 0.01, 0.05, and 0.1.
#
# To run the code in the terminal, use the command:
#       python Exe5_skel.py
#

import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the magnification factor M
def magnification_factor(r, zeta):
    #____your code to return M____

# Frequency ratio range (r = omega/omega_n)
r_values = np.linspace(0.1, 3.0, 500)

# Damping ratios to consider
zeta_values = [0.01, 0.05, 0.1]

# Plotting the magnification factor for different damping ratios
plt.figure(figsize=(10, 6))
for zeta in zeta_values:
    M_values = magnification_factor(r_values, zeta)
    plt.plot(r_values, M_values, label=f'Damping ratio (zeta) = {zeta}')

# Plot settings
plt.title('Magnification Factor vs Frequency Ratio (r)', fontsize=16)
plt.xlabel('Frequency Ratio (r = $\omega$ / $\omega_n$)', fontsize=14)
plt.ylabel('Magnification Factor (M)', fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('magnif1.png')
