from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def grover_oracle(qc):
    qc.cz(0, 1)

def grover_diffuser(qc):
    qc.h([0, 1])
    qc.x([0, 1])
    qc.h(1)
    qc.cz(0, 1)
    qc.h(1)
    qc.x([0, 1])
    qc.h([0, 1])

def run_grover_algorithm():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])  # Initialize in superposition
    grover_oracle(qc)  # Apply oracle
    grover_diffuser(qc) 
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)  # Transpile for simulator
    result = simulator.run(compiled_circuit, shots=1024).result()
    return result.get_counts()

#usage
if __name__ == "__main__":
    counts = run_grover_algorithm()
    print("Measurement Results:", counts)
    plot_histogram(counts).show()
