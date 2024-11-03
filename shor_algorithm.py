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
    for _ in range(10):  # Retry up to 10 times to increase the chance of success
        a = np.random.randint(2, N)
        if gcd(a, N) != 1:
            factor = gcd(a, N)
            if factor != 1 and factor != N:
                return f"{factor} is a factor of {N}"
        
        # Find the period r of a modulo N
        r = find_period(a, N)
        if r % 2 != 0:
            continue  # Retry if period is odd
        
        # potential factors
        factor1 = gcd(pow(a, r//2) - 1, N)
        factor2 = gcd(pow(a, r//2) + 1, N)
        
        if factor1 != 1 and factor1 != N and N % factor1 == 0:
            return factor1, N // factor1
        if factor2 != 1 and factor2 != N and N % factor2 == 0:
            return factor2, N // factor2

    return "Failed to find factors; retry Shor's algorithm"

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
