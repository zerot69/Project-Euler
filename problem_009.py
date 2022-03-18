# Project Euler

# Problem 9: Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time


start_time = time.time()
ans_project_9 = int(0)
for a in range(1, 500):
    for b in range(1, 500):
        c = 1000 - a - b
        if a < b < c:
            if a*a + b*b == c*c:
                ans_project_9 = a*b*c
print("Problem 9:", ans_project_9)
print("Total time:", time.time() - start_time)
