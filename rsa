#!/usr/bin/python3
import sympy
import sys
import time


def factorize_prime(number):
    start_time = time.time()
    p, q = sympy.ntheory.factorint(number, limit=10**6).keys()
    end_time = time.time()

    print(f"{number}={p}*{q}")
    print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: prime_factors <number>")
        sys.exit(1)

    number = int(sys.argv[1])
    factorize_prime(number)
