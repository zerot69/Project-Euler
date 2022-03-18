# Project Euler

# Problem 41: Pan-digital prime
# We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pan-digital and is also prime.
# What is the largest n-digit pan-digital prime that exists?

import time
import math
import itertools


start_time = time.time()


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


ans_project_41 = int(0)
p = itertools.permutations('1234567')
for x in list(p)[::-1]:
    if int(x[6]) % 2 != 0:
        y = int(''.join(x))
        if (y + 1) % 6 == 0 or (y - 1) % 6 == 0:
            if is_prime_number(y):
                ans_project_41 = y
                break
print("Problem 41:", ans_project_41)
print("Total time:", time.time() - start_time)
