# Project Euler

# Problem 15: Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

import time
import math


start_time = time.time()
grid_size_x = 20
grid_size_y = 20
ans_project_15 = math.factorial(grid_size_x + grid_size_y) // math.factorial(grid_size_x) // math.factorial(grid_size_y)
print("Problem 15:", ans_project_15)
print("Total time:", time.time() - start_time)
