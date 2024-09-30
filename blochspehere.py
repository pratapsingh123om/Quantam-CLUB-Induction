#first instll qiskit and matplotlib in system  
#qiskit helps us to plot the qubit  on bloch  spehere while matplotlib help us to print out the plot as output

import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_vector
from numpy import pi, cos, sin

# Define the state vector angles in radians
theta = 135 * pi / 180  # 135 degrees in radians
phi = 0  # 0 degrees in radians

# Calculate the x, y, z components of the Bloch vector uses poalr coordinates in a 3d system
x = sin(theta) * cos(phi)
y = sin(theta) * sin(phi)
z = cos(theta)

# Plot the Bloch vector
bloch_vector = [x, y, z]
plot_bloch_vector(bloch_vector, title="Qubit Bloch Sphere (45° from |1⟩, 135° from |0⟩)")

# Show the plot
plt.show()
