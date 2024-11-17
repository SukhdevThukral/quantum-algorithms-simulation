import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def qft(circuit, n):
    """Apply the Quantum Fourier Transform to the first n qubits in the circuit."""
    for j in range(n):
        circuit.h(j)  #Hadamard gate
        for k in range(j + 1, n):
            circuit.cp(np.pi / (2 ** (k - j)), j, k) 

    for i in range(n // 2):
        circuit.swap(i, n - i - 1)

def run_qft(n):
    """Run QFT on n qubits."""
    circuit = QuantumCircuit(n, n) 
    qft(circuit, n)
    circuit.measure(range(n), range(n))  # Measure all qubits

    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1024).result()
    return result.get_counts()
