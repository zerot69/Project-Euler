# Project Euler

# Problem 31: Coin sums
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many ways can £2 be made using any number of coins?


import time

start_time = time.time()
ans_project_31 = int(0)
ways = [0] * 201
ways[0] = 1
for x in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(x, 201):
        ways[i] += ways[i - x]
ans_project_31 = ways[200]
print("Problem 31:", ans_project_31)
print("Total time:", time.time() - start_time)
