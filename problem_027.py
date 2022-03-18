# Project Euler

# Problem 27: Quadratic primes
# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product a*b of the coefficients, a and b, for the quadratic expression that
# produces the maximum number of primes for consecutive values of n, starting with n = 0.

import time
import math


start_time = time.time()


def is_prime_number(j):
    if j <= 1:
        return False
    for i in range(2, int(math.sqrt(j)) + 1):
        if j % i == 0:
            return False
    return True


prime_list = []
for x in range(1000):
    if is_prime_number(x):
        prime_list.append(x)
longest = 0
largest_a = 0
largest_b = 0
for a in range(-1000, 1000):
    for b in prime_list:
        n = 0
        term = n ** 2 + a * n + b
        while is_prime_number(term):
            term = n ** 2 + a * n + b
            n += 1
        if n > longest:
            longest = n
            largest_a = a
            largest_b = b
ans_project_27 = int(largest_a * largest_b)
print("Problem 27:", ans_project_27)
print("Total time:", time.time() - start_time)
