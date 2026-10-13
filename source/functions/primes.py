import sympy as sp

def primes(x):
    return len(list(sp.primerange(1, x + 1)))