from qiskit import QuantumCircuit
from math import gcd
import numpy as np

def find_period(a, N):
    """ Find the period of a modulo N using classical computation """
    r = 1
    while pow(a, r, N) != 1:
        r += 1
    return r

def run_shor_algorithm(N):
    """ Classical approximation of Shor's factoring algorithm """
    a = np.random.randint(2, N)
    if gcd(a, N) != 1:
        return f"{a} is a factor of {N}"

    r = find_period(a, N)
    if r % 2 != 0:
        return "Period is odd; retrying Shor's algorithm"

    factor1 = gcd(a**(r//2) - 1, N)
    factor2 = gcd(a**(r//2) + 1, N)
    
    if factor1 == 1 or factor2 == 1:
        return "Factors not found; retry Shor's algorithm"
    return factor1, factor2

#usage
if __name__ == "__main__":
    N = 15  # Replace with the number you want to factorize
    result = run_shor_algorithm(N)
    print("Factors of", N, ":", result)
