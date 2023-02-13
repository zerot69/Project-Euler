# Project Euler

# Problem 24: Lexicographic permutations
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:#
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time
from itertools import permutations


start_time = time.time()
permutations = list(permutations('0123456789'))
ans_project_24 = ''.join(permutations[999999])
print("Problem 24:", ans_project_24)
print("Total time:", time.time() - start_time)
