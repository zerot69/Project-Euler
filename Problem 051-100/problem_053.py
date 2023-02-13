# Project Euler

# Problem 53: Combinatorics selections
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, (5 3) = 10.
# In general, (n r) = n! / (r! * (n-r)!), where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: (23 10) = 1144066.#
# How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?

import time
import math

start_time = time.time()
ans_project_53 = int(0)
for n in range(1, 101):
    for r in range(1, n + 1):
        combinatorics = int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
        if combinatorics > 1000000:
            print(n, r, combinatorics)
            ans_project_53 += 1
print("Problem 53:", ans_project_53)
print("Total time:", time.time() - start_time)
