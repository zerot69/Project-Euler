# Project Euler

# Problem 45: Triangular, pentagonal, and hexagonal
# Triangle, pentagonal, and hexagonal numbers are generated by the following formular:
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

import time

start_time = time.time()


def is_pentagonal_number(n):
    if (1 + (24 * n + 1) ** 0.5) % 6 == 0:
        return True
    return False


def is_hexagonal_number(n):
    if (1 + (8 * n + 1) ** 0.5) % 4 == 0:
        return True
    return False


ans_project_45 = int(0)
x = 286
temp = False
while not temp:
    triangle_number = x * (x + 1)/2
    if is_hexagonal_number(triangle_number) and is_pentagonal_number(triangle_number):
        ans_project_45 = int(triangle_number)
        temp = True
    x += 1
print("Problem 45:", ans_project_45)
print("Total time:", time.time() - start_time)