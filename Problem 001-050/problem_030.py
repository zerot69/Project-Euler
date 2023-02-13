# Project Euler

# Problem 30: Digit fifth powers
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import time

start_time = time.time()
ans_project_30 = int(0)
for x in range(2, 354295):
    temp = int(0)
    for y in range(len(str(x))):
        temp += int(str(x)[y]) ** 5
    if x == temp:
        ans_project_30 += x
        print(x)
print("Problem 30:", ans_project_30)
print("Total time:", time.time() - start_time)
