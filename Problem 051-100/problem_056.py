# Project Euler

# Problem 56: Powerful digit sum
# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

import time

start_time = time.time()
ans_project_56 = int(0)
for x in range(1, 101):
    for y in range(1, 101):
        digit_sum = 0
        for c in str(x ** y):
            digit_sum += int(c)
        if digit_sum > ans_project_56:
            ans_project_56 = digit_sum
print("Problem 56:", ans_project_56)
print("Total time:", time.time() - start_time)
