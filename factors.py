#!/usr/bin/python3
import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line) for line in file]

    for num in numbers:
        factors = factorize(num)
        if factors:
            p, q = factors
            print(f"{num}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
