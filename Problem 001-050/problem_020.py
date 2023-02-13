# Project Euler

# Problem 20: Factorial digit sum
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

import time

start_time = time.time()
ans_project_20 = int(0)
factorial = int(1)
for x in range(1, 101):
    factorial *= x
for y in str(factorial):
    ans_project_20 += int(y)
print("Problem 20:", ans_project_20)
print("Total time:", time.time() - start_time)
