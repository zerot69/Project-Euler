# Project Euler

# Problem 39: Integer right triangles
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

import time

start_time = time.time()
perimeters = []
for a in range(1, 500):
    for b in range(a, 500):
        c = (a ** 2 + b ** 2) ** 0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)
ans_project_39 = int(max(set(perimeters), key=perimeters.count))
print("Problem 39:", ans_project_39)
print("Total time:", time.time() - start_time)
