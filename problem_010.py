# Project Euler

# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


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


ans_project_10 = int(0)
x = 2
while x < 2000000:
    if is_prime_number(x):
        ans_project_10 += x
    x += 1
print("Problem 10:", ans_project_10)
print("Total time:", time.time() - start_time)
