from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def grover_oracle(qc):
    qc.cz(0, 1)  # Apply controlled-Z gate to mark |11>

def grover_diffuser(qc):
    # Apply the Grover diffuser 
    qc.h([0, 1])  
    qc.x([0, 1])  
    qc.h(1)     
    qc.cz(0, 1)   
    qc.h(1)      
    qc.x([0, 1])  
    qc.h([0, 1])  

def run_grover_algorithm(iterations=1):
    qc = QuantumCircuit(2, 2) 
    qc.h([0, 1]) 

    for _ in range(iterations):
        grover_oracle(qc)    # Apply the oracle
        grover_diffuser(qc)  # Apply the diffuser
    
    qc.measure([0, 1], [0, 1])  # Measure the qubits

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)  # Transpile for simulator
    result = simulator.run(compiled_circuit, shots=16384).result()
    counts = result.get_counts()

    target_state = '11'  # Target state 
    accuracy = (counts.get(target_state, 0) / 16384) * 100  # accuracy
    print(f"Accuracy for target state '{target_state}': {accuracy:.2f}%")
    return counts, accuracy
