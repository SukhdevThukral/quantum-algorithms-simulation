# utils/visualization.py
from qiskit.visualization import plot_histogram as qiskit_plot_histogram
import matplotlib.pyplot as plt

def plot_histogram(counts, title="Quantum Simulation Results"):
    """Function to plot histogram of counts."""
    qiskit_plot_histogram(counts)
    plt.title(title)
    plt.show()
