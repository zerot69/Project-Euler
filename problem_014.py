# Project Euler

# Problem 14: Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time


start_time = time.time()
ans_project_14 = int(0)
t = int(1)
max_count = int(0)
max_count_t = int(1)
while t < 1000000:
    x = t
    count = int(0)
    while x != 1:
        if x % 2 == 0:
            x /= 2
            count += 1
        else:
            x = 3 * x + 1
            count += 1
    print(t, ":", count)
    if max_count < count:
        max_count = count
        max_count_t = t
    t += 1
ans_project_14 = max_count_t
print("Problem 14:", ans_project_14)
print("Total time:", time.time() - start_time)
