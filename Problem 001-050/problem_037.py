# Project Euler

# Problem 37: Truncatable primes
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
# from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly, we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time
import math


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_truncatable_left(n):
    while is_prime_number(n) and n >= 10:
        n = int(str(n)[:-1])
    if is_prime_number(n):
        return True
    return False


def is_truncatable_right(n):
    while is_prime_number(n) and n >= 10:
        n = int(str(n)[1:])
    if is_prime_number(n):
        return True
    return False


start_time = time.time()
ans_project_37 = int(0)
count = int(0)
x = int(10)
while count < 11:
    if is_truncatable_left(x) and is_truncatable_right(x):
        print(x)
        ans_project_37 += x
        count += 1
    x += 1
print("Problem 37:", ans_project_37)
print("Total time:", time.time() - start_time)
