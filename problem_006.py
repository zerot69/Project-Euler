# Project Euler

# Problem 6: Sum square difference
# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + 3^2 + ... + 10^2 = 3025
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + 3 + ... + 10)^2 = 55^2 = 385
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time


start_time = time.time()
ans_project_6 = int(0)
sum_of_squares = 0
sum_of_nums = 0
for x in range (1, 101):
    sum_of_nums += x
    sum_of_squares += x * x
    print(x, sum_of_nums, sum_of_squares)
ans_project_6 = abs(sum_of_squares - sum_of_nums * sum_of_nums)
print("Problem 6:", ans_project_6)
print("Total time:", time.time() - start_time)
