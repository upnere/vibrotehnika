# An engine mount system 
#
# Usage: python Exe8_skel.py
#

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# System parameters for the engine mount
F0 = 10         # Base force amplitude (N)
m = 50          # Mass of the engine (kg)
k = 20000       # Spring stiffness (N/m)
c = 100         # Damping coefficient (Ns/m)

#______ your code for omega_n and zeta _____


# Define the frequency range for the excitation (corresponding to engine RPM)
frequencies = np.linspace(0.1 * omega_n, 2 * omega_n, 50)

# Define time points for the simulation
t = np.linspace(0, 2, 1000)  # Duration and time steps

# Function to calculate magnification factor
def magnification_factor(r):
    #______ your code for M _____
    
    return M

# Differential equation model of the system
def engine_mount_model(y, t, omega):
    #______ your code for dydt and dvdt _____
    
    return [dydt, dvdt]

# Arrays to store results
amplitudes = []
peak_displacements = []

# Loop over different excitation frequencies
for omega in frequencies:
    # Frequency ratio r
    r = omega / omega_n
    
    # Calculate magnification factor M(r) and r^2 * M(r)
    M = magnification_factor(r)
    amplitude_factor = r**2 * M
    amplitudes.append(amplitude_factor)
    
    # Solve the system using odeint
    y_init = [0, 0]  # Initial conditions: [displacement, velocity]
    y = odeint(engine_mount_model, y_init, t, args=(omega,))
    y_displacement = y[:, 0]  # Extract displacement

    # Record peak displacement for each frequency (steady-state approximation)
    peak_displacements.append(np.max(np.abs(y_displacement[-500:])))  # Use last half of time series

    # Plot displacement response for a few key frequencies
    if np.isclose(omega, omega_n, rtol=0.1) or omega in [0.5 * omega_n, 1.5 * omega_n]:
        plt.plot(t, y_displacement, label=f'ω={omega:.2f} rad/s (r={r:.2f})')

# Plot displacement response over time for selected frequencies
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.title('Displacement response at selected excitation frequencies')
plt.grid(True)
plt.savefig('displacement.png')

# Plot r^2 * M(r) vs. frequency ratio
plt.figure()
plt.plot(frequencies / omega_n, amplitudes, 'b-', label=r'$r^2 \times M(r)$')
plt.xlabel('Frequency Ratio (r)')
plt.ylabel(r'$\Lambda$')
plt.title('Effect of Frequency-Squared Excitation on Magnification')
plt.grid(True)
plt.legend()
plt.savefig('lambda_freq.png')

# Plot peak displacements vs. frequency ratio
plt.figure()
plt.plot(frequencies / omega_n, peak_displacements, 'r-', label='Peak Displacement')
plt.xlabel('Frequency Ratio (r)')
plt.ylabel('Peak Displacement (m)')
plt.title('Peak Displacement Response vs. Frequency Ratio')
plt.grid(True)
plt.legend()
plt.savefig('displ_frqratio.png')
