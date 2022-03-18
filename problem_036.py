# Project Euler

# Problem 36: Double-base palindromes
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time

start_time = time.time()
ans_project_36 = int(0)
for x in range(1, 1000000, 2):
    if str(x) == str(x)[::-1]:
        if bin(x)[2:] == bin(x)[2:][::-1]:
            ans_project_36 += x
print("Problem 36:", ans_project_36)
print("Total time:", time.time() - start_time)
