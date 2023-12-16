#!/usr/bin/python3
import sys


def factorize(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            factors.append((i, number // i))
            break
    return factors


def factorize_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for num in numbers:
            num = int(num.strip())
            factor_pairs = factorize(num)
            for pair in factor_pairs:
                print(f"{num}={pair[0]}*{pair[1]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_numbers(file_path)
