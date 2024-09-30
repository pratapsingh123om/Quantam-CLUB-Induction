
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Create a Grover's algorithm circuit
def grover_algorithm(target_state):
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)

    # Step 2: Apply Hadamard gate to both qubits to create superposition
    qc.h([0, 1])

    # Oracle: Mark the target state
    if target_state == '00':
        qc.x(0)
        qc.x(1)
    elif target_state == '01':
        qc.x(0)
    elif target_state == '10':
        qc.x(1)
    elif target_state == '11':
        pass  # No X gate needed as this is the target

    qc.h([0, 1])
    qc.cz(0, 1)  # Controlled-Z gate
    qc.h([0, 1])

    # Step 3: Apply Hadamard again to both qubits
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)  # Controlled-Z gate
    qc.x([0, 1])
    qc.h([0, 1])

    # Step 4: Measurement
    qc.measure([0, 1], [0, 1])

    return qc

# Define target state
target_state = '11'
grover_circuit = grover_algorithm(target_state)

# Step 5: Draw the circuit
grover_circuit.draw('mpl')
plt.show()

# Step 6: Use AerSimulator instead of execute
simulator = Aer.get_backend('qasm_simulator')  # Use Aer.get_backend instead of AerSimulator

# Run the simulation on the qasm_simulator backend
job = simulator.run(grover_circuit, shots=1024)
result = job.result()

# Step 7: Get results and plot
counts = result.get_counts(grover_circuit)
print("Measurement results:", counts)

# Plot the results
plot_histogram(counts)
plt.show()
