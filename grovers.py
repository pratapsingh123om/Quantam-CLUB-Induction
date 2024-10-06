
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1: Create a Grover's algorithm circuit for 4 qubits and 4 classical bits
def grover_algorithm(target_state):
    # Create a quantum circuit with 4 qubits and 4 classical bits
    qc = QuantumCircuit(4, 4)

    # Step 2: Apply Hadamard gate to all 4 qubits to create superposition
    qc.h([0, 1, 2, 3])

    # Oracle: Mark the target state (using X gates to flip the qubits accordingly)
    if target_state == '0000':
        qc.x([0, 1, 2, 3])
    elif target_state == '0001':
        qc.x([0, 1, 2])
    elif target_state == '0010':
        qc.x([0, 1, 3])
    elif target_state == '0011':
        qc.x([0, 1])
    elif target_state == '0100':
        qc.x([0, 2, 3])
    elif target_state == '0101':
        qc.x([0, 2])
    elif target_state == '0110':
        qc.x([0, 3])
    elif target_state == '0111':
        qc.x([0])
    elif target_state == '1000':
        qc.x([1, 2, 3])
    elif target_state == '1001':
        qc.x([1, 2])
    elif target_state == '1010':
        qc.x([1, 3])
    elif target_state == '1011':
        qc.x([1])
    elif target_state == '1100':
        qc.x([2, 3])
    elif target_state == '1101':
        qc.x([2])
    elif target_state == '1110':
        qc.x([3])
    elif target_state == '1111':
        pass  # No X gate needed as this is the target

    # Grover's Diffusion Operator
    qc.h([0, 1, 2, 3])
    qc.cz(0, 1)  # Controlled-Z gate between qubits 0 and 1
    qc.cz(2, 3)  # Controlled-Z gate between qubits 2 and 3
    qc.h([0, 1, 2, 3])

    # Step 3: Apply Hadamard again to all qubits
    qc.h([0, 1, 2, 3])
    qc.x([0, 1, 2, 3])
    qc.cz(0, 1)  # Controlled-Z gate between qubits 0 and 1
    qc.cz(2, 3)  # Controlled-Z gate between qubits 2 and 3
    qc.x([0, 1, 2, 3])
    qc.h([0, 1, 2, 3])

    # Step 4: Measurement
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

    return qc

# Define target state
target_state = '1111'  # You can change this to any 4-qubit state
grover_circuit = grover_algorithm(target_state)

# Step 5: Draw the circuit
grover_circuit.draw('mpl')
plt.show()

# Step 6: Use AerSimulator instead of execute
simulator = Aer.get_backend('qasm_simulator')

# Run simulations until the target state is found
num_runs = 0
found = False

while not found:
    num_runs += 1
    job = simulator.run(grover_circuit, shots=1)
    result = job.result()
    
    # Get results
    counts = result.get_counts(grover_circuit)

    # Check if the target state is found
    found = target_state in counts

# Print the number of runs until the target state was found
print(f"The target state '{target_state}' was found after {num_runs} runs.")
