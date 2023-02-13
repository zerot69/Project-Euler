# Project Euler

# Problem 7: 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

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


ans_project_7 = int(0)
x = 1
y = 2
while x <= 10001:
    if is_prime_number(y):
        x += 1
    y += 1
ans_project_7 = y-1
print("Problem 7:", ans_project_7)
print("Total time:", time.time() - start_time)
