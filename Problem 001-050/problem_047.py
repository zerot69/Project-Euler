# Project Euler

# Problem 47: Distinct primes factors
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import time

start_time = time.time()


def number_of_prime_factors(n):
    i = 2
    a = set()
    while i < n ** 0.5 or n == 1:
        if n % i == 0:
            n = n / i
            a.add(i)
            i -= 1
        i += 1
    return len(a) + 1


x = 2 * 3 * 5 * 7
while True:
    if number_of_prime_factors(x) == 4:
        x += 1
        if number_of_prime_factors(x) == 4:
            x += 1
            if number_of_prime_factors(x) == 4:
                x += 1
                if number_of_prime_factors(x) == 4:
                    break
    x += 1
ans_project_47 = int(x - 3)
print("Problem 47:", ans_project_47)
print("Total time:", time.time() - start_time)
