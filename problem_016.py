# Project Euler

# Problem 16: Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import time


start_time = time.time()
ans_project_16 = int(0)
num_as_string = str(2 ** 1000)
for x in num_as_string:
    ans_project_16 += int(x)
print("Problem 16:", ans_project_16)
print("Total time:", time.time() - start_time)
