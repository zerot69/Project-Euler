# Project Euler

# Problem 28: Number spiral diagonals
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import time

start_time = time.time()
ans_project_28 = int(1)
grid = 1001
x = 1
y = 0
d = 2
while x <= grid * grid:
    y += 1
    if y > 4:
        d += 2
        y = 1
    x += d
    if x <= grid * grid:
        ans_project_28 += x
print("Problem 28:", ans_project_28)
print("Total time:", time.time() - start_time)
