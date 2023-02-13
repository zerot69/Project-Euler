# Project Euler

# Problem 43: Sub-string divisibility
# The number, 1406357289, is a 0 to 9 pan-digital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2 * d3 * d4 = 406 is divisible by 2
# d3 * d4 * d5 = 063 is divisible by 3
# d4 * d5 * d6 = 635 is divisible by 5
# d5 * d6 * d7 = 357 is divisible by 7
# d6 * d7 * d8 = 572 is divisible by 11
# d7 * d8 * d9 = 728 is divisible by 13
# d8 * d9 * d10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pan-digital numbers with this property.

import time
import itertools

start_time = time.time()
ans_project_43 = int(0)
p = itertools.permutations('0123456789')
for i in p:
    if (int(''.join(i[7:10])) % 17 == 0 and int(''.join(i[6:9])) % 13 == 0 and int(''.join(i[5:8])) % 11 == 0 and
            int(''.join(i[4:7])) % 7 == 0 and int(''.join(i[3:6])) % 5 == 0 and int(''.join(i[2:5])) % 3 == 0 and
            int(''.join(i[1:4])) % 2 == 0):
        ans_project_43 += int(''.join(i))
print("Problem 43:", ans_project_43)
print("Total time:", time.time() - start_time)
