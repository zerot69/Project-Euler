# Project Euler

# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

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


max_num = 20
ans_project_5 = int(1)
for x in range(1, max_num + 1):
    if is_prime_number(x):
        y = x
        while y * x < max_num:
            y *= x
        ans_project_5 *= y
print("Problem 5:", ans_project_5)
print("Total time:", time.time() - start_time)
