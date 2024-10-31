from grover_algorithm import run_grover_algorithm
from shor_algorithm import run_shor_algorithm
from utils.visualization import plot_histogram

def main():
    print("Quantum Algorithm Simulator")
    choice = input("Choose algorithm to run (1: Grover's Algorithm, 2: Shor's Algorithm): ")

    if choice == "1":
        print("Running Grover's Algorithm...")
        grover_counts = run_grover_algorithm()
        plot_histogram(grover_counts, title="Grover's Algorithm Results")
    elif choice == "2":
        print("Running Shor's Algorithm...")
        factors = run_shor_algorithm(N=15)
        print(f"Factors of 15 found: {factors}")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
