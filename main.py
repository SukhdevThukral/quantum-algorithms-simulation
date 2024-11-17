from grover_algorithm import run_grover_algorithm
from shor_algorithm import run_shor_algorithm
from qft_algorithm import run_qft
from amplitude_amplification import run_amplitude_amplification
from utils.visualization import plot_histogram

def main():
    print("Quantum Algorithm Simulator")
    choice = input("Choose algorithm to run (1: Grover's, 2: Shor's, 3: QFT, 4: Amplitude Amplification): ")

    if choice == "1":
        print("Running Grover's Algorithm...")
        iterations = int(input("Enter the number of iterations for Grover's Algorithm (try 2 or more): "))
        grover_counts, accuracy = run_grover_algorithm(iterations)
        print(f"Final accuracy for target state '11': {accuracy:.2f}%")
        plot_histogram(grover_counts, title="Grover's Algorithm Results")
    elif choice == "3":
        n = int(input("Enter the number of qubits for QFT: "))
        print(f"Running Quantum Fourier Transform on {n} qubits...")
        qft_counts = run_qft(n)
        plot_histogram(qft_counts, title="QFT Results")
    elif choice == "4":
        n = int(input("Enter the number of qubits for Amplitude Amplification: "))
        iterations = int(input("Enter the number of iterations: "))
        print(f"Running Amplitude Amplification on {n} qubits for {iterations} iterations...")
        amp_counts = run_amplitude_amplification(n, iterations)
        plot_histogram(amp_counts, title="Amplitude Amplification Results")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
