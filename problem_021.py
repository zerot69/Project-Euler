# Project Euler

# Problem 21: Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import time


start_time = time.time()
ans_project_21 = int(0)
for x in range(1, 10001):
    sum_of_divisors_1 = 0
    sum_of_divisors_2 = 0
    for y in range(1, x):
        if x % y == 0:
            sum_of_divisors_1 += y
    if sum_of_divisors_1 > 0:
        for z in range(1, sum_of_divisors_1):
            if sum_of_divisors_1 % z == 0:
                sum_of_divisors_2 += z
    if x == sum_of_divisors_2 and sum_of_divisors_1 != x:
        ans_project_21 += x
print("Problem 21:", ans_project_21)
print("Total time:", time.time() - start_time)
