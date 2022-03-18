# Project Euler

# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math
import time


start_time = time.time()


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


ans_project_3 = int(1)
for x in range(1, 600851475143):
    if 600851475143 % x == 0 and is_prime_number(x) and x > ans_project_3:
        ans_project_3 = x
print("Problem 3:", ans_project_3)
print("Total time:", time.time() - start_time)
