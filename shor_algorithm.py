from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator as Aer
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
from math import gcd
import numpy as np

def modular_exponentiation(a, x, N):
    """ Computes (a^x) mod N efficiently. """
    result = 1
    a = a % N
    while x > 0:
        if (x % 2) == 1:
            result = (result * a) % N
        a = (a * a) % N
        x //= 2
    return result

def qpe_amod15(a):
    """ Quantum Phase Estimation to find the period of a mod N """
    N = 15
    n_count = 4  # Number of counting qubits
    qc = QuantumCircuit(n_count, n_count)

    # Apply Hadamard gates to counting qubits
    for q in range(n_count):
        qc.h(q)

    # Controlled modular exponentiation
    for q in range(n_count):
        qc.append(controlled_mod_exp(a, 2**q, N), [q] + list(range(n_count, n_count + n_count)))

    # Apply the inverse quantum Fourier transform
    qc.append(QFT(n_count, inverse=True), range(n_count))

    # Measurement
    qc.measure(range(n_count), range(n_count))

    return qc

def controlled_mod_exp(a, power, N):
    """ Controlled modular exponentiation gate. """
    circuit = QuantumCircuit(1, name='CME')
    circuit.append(modular_exponentiation(a, power, N), [0])  # Add controlled operations
    return circuit.to_gate()

def extract_period(counts):
    """ Extract the period from the measurement results. """
    return np.random.randint(1, 10)  # Dummy value for the period

def run_shor_algorithm(N):
    """ Run Shor's algorithm to factor N. """
    for _ in range(10):  # Retry up to 10 times
        a = np.random.randint(2, N)
        if gcd(a, N) != 1:
            factor = gcd(a, N)
            return f"{factor} is a factor of {N}"

        # Prepare the quantum circuit to find the period
        qc = qpe_amod15(a)
        
        # Simulate the circuit
        backend = Aer.get_backend('qasm_simulator')
        transpiled_circuit = transpile(qc, backend)
        
        # Execute the circuit and get the counts
        result = backend.run(transpiled_circuit, shots=1024).result()
        counts = result.get_counts()

        # Extract the period from the measurement results
        r = extract_period(counts)

        if r % 2 != 0:
            continue  # Retry if the period is odd

        # Calculate potential factors
        factor1 = gcd(modular_exponentiation(a, r // 2, N) - 1, N)
        factor2 = gcd(modular_exponentiation(a, r // 2, N) + 1, N)

        if factor1 not in [1, N]:
            return factor1, N // factor1
        if factor2 not in [1, N]:
            return factor2, N // factor2

    return "Failed to find factors; retry Shor's algorithm."

if __name__ == "__main__":
    try:
        N = int(input("Enter the number to factorize: "))
        if N < 2:
            print("Please enter a valid number greater than 1.")
        else:
            result = run_shor_algorithm(N)
            print(f"Factors of {N}: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
