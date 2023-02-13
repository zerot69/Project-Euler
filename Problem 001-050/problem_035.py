# Project Euler

# Problem 35: Circular primes
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import itertools
import time
import math


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


start_time = time.time()
ans_project_35 = int(4)
nb_digits = 9
final_numbers = {'1', '3', '7', '9'}
for x in range(2, nb_digits + 1):
    for y in itertools.product(final_numbers, repeat=x):
        y_int = int(''.join(y))
        permutations = {int(''.join(y[i:] + y[:i])) for i in range(len(y))}
        if y_int == min(permutations) and all(is_prime_number(n) for n in permutations):
            ans_project_35 += len(permutations)
print("Problem 35:", ans_project_35)
print("Total time:", time.time() - start_time)
