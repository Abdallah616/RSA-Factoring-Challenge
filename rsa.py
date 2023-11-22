#!/usr/bin/python3
import sys
from sympy import isprime, factorint

def factorize_rsa_number(n):
    if isprime(n):
        print(f"{n} is a prime number.")
    else:
        factors = factorint(n)
        p, q = factors.keys()
        print(f"{n} = {p} * {q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa_factors <number>")
        sys.exit(1)

    rsa_number = int(sys.argv[1])
    factorize_rsa_number(rsa_number)
