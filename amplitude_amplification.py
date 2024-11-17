from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def create_oracle(circuit, n):
    circuit.cz(0, 1)  # Applying a controlled-Z gate for |11>
    return circuit

def create_diffuser(circuit, n):
    for qubit in range(n):
        circuit.h(qubit)  
    for qubit in range(n):
        circuit.x(qubit)
    circuit.h(n - 1)  # Applying Hadamard to the last qubit
    
    circuit.mcx(list(range(n - 1)), n - 1) 
    
    circuit.h(n - 1) 
    for qubit in range(n):
        circuit.x(qubit) 
    for qubit in range(n):
        circuit.h(qubit)
    return circuit

def run_amplitude_amplification(n, iterations):
    circuit = QuantumCircuit(n)
    
    # Uniform superposition
    for qubit in range(n):
        circuit.h(qubit)

    # Apply amplitude amplification iterations
    for _ in range(iterations):
        create_oracle(circuit, n) 
        create_diffuser(circuit, n)

    # Measure qubits
    circuit.measure_all()

    # using AerSimulator
    backend = AerSimulator()

    # Transpiling the circuit
    transpiled_circuit = transpile(circuit, backend)

    # Executing the circuit
    job = backend.run(transpiled_circuit, shots=1024)
    results = job.result()
    
    return results.get_counts(transpiled_circuit)
