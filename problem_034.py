# Project Euler

# Problem 34: Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import time
import math

start_time = time.time()
ans_project_34 = int(0)
for x in range(10, 1500000):
    temp = 0
    for y in range(len(str(x))):
        temp += math.factorial(int(str(x)[y]))
    print(x, temp)
    if x == temp:
        ans_project_34 += x
print("Problem 34:", ans_project_34)
print("Total time:", time.time() - start_time)
