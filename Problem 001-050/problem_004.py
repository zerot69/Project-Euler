# Project Euler

# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time


start_time = time.time()
ans_project_4 = int(0)
for x in range(100, 999):
    for y in range(100, 999):
        converted_num = str(int(x*y))
        if len(converted_num) == 5:
            if converted_num[0] == converted_num[4] and converted_num[1] == converted_num[3]:
                if x * y > ans_project_4:
                    ans_project_4 = x * y
        elif len(converted_num) == 6:
            if converted_num[0] == converted_num[5] and converted_num[1] == converted_num[4] and \
                    converted_num[2] == converted_num[3]:
                if x * y > ans_project_4:
                    ans_project_4 = x * y
print("Problem 4:", ans_project_4)
print("Total time:", time.time() - start_time)
