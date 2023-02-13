# Project Euler

# Problem 48: Self powers
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time

start_time = time.time()
ans_project_48 = int(0)
sums = int(0)
for x in range(1, 1001):
    sums += x ** x
ans_project_48 = sums % 10000000000
print("Problem 48:", ans_project_48)
print("Total time:", time.time() - start_time)
