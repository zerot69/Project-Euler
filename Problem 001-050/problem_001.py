# Project Euler

# Problem 1: Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time


start_time = time.time()
ans_project_1 = int(0)
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        ans_project_1 += x
print("Problem 1:", ans_project_1)
end_time = time.time()
total_time = end_time - start_time
print("Total time:", str(total_time))
