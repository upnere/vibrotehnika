# The code calculate the response of a single degree of freedom system
# with a mass of 5 kg, a stiffness of 3EI/L^3, and a length of 2.1 m.
# The initial velocity is 0.5 m/s and the initial deflection is 0.001 m.
#
# To run the code, type in the terminal: python Exe1_skel.py

import numpy as np
import matplotlib.pyplot as plt

# Given constants
m_eq = 5
v_0 = 0.5
E = 210e+9
L = 2.1
I = 3e-6

# Calculates stiffnes k & natural frequency w_n
# ____ your code here ____

print('k =',k_eq,'\nw_n =',w_n)

# Calculate the static deflection or initial deflection x_0
# ____ your code here ____

print('x_0 =',x_0)

# Calculate amplitude A & phase shift phi
# ____ your code here ____

print('A =',A,'\nphi =',phi)

# Define time interval & calculate the solution
t = np.linspace(0,3.14,1000)
x = A*np.sin(w_n*t+phi)

# Plot graph
plt.plot(t, x)
plt.ylabel('Response x')
plt.xlabel('Time t')

plt.show()