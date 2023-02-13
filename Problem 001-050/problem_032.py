# Project Euler

# Problem 32: Pan-digital products
# We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pan-digital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
# and product is 1 through 9 pan-digital.
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pan-digital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import time

start_time = time.time()
pan_digital = set()
number_digits = set('123456789')
for i in range(9):
    for j in range(999, 9999):
        s = str(i) + str(j) + str(i * j)
        if len(s) == 9 and set(s) == number_digits:
            pan_digital.add(i * j)
        elif len(s) > 9:
            break
for i in range(9, 99):
    for j in range(99, 999):
        s = str(i) + str(j) + str(i * j)
        if len(s) == 9 and set(s) == number_digits:
            pan_digital.add(i * j)
        elif len(s) > 9:
            break
ans_project_32 = sum(pan_digital)
print("Problem 32:", ans_project_32)
print("Total time:", time.time() - start_time)
