# Project Euler

# Problem 68: Magic 5-gon ring

# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
# https://projecteuler.net/project/images/p068_1.png
# Working clockwise, and starting from the group of three with the numerically lowest external node
# (4,3,2 in this example), each solution can be described uniquely.
# For example, the above solution can be described by the set:
# 4,3,2; 6,2,1; 5,1,3.
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
# There are eight solutions in total.
# Total           Solution Set
# 9               4,2,3; 5,3,1; 6,1,2
# 9               4,3,2; 6,2,1; 5,1,3
# 10              2,3,5; 4,5,1; 6,1,3
# 10              2,5,3; 6,3,1; 4,1,5
# 11              1,4,6; 3,6,2; 5,2,4
# 11              1,6,4; 5,4,2; 3,2,6
# 12              1,5,6; 2,6,4; 3,4,5
# 12              1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?
# https://projecteuler.net/project/images/p068_2.png

import time
from itertools import permutations


def is_magic_ring(p):
    s = p[0] + p[5] + p[6]
    if p[1] + p[6] + p[7] != s:
        return False
    if p[2] + p[7] + p[8] != s:
        return False
    if p[3] + p[8] + p[9] != s:
        return False
    if p[4] + p[9] + p[5] != s:
        return False
    if min(p[0], p[1], p[2], p[3], p[4]) != p[0]:
        return False
    return True


def main():
    start_time = time.time()
    max_string = 0
    for p in permutations(range(1, 11)):
        if is_magic_ring(p):
            s = ''.join(
                map(str, (p[i] for i in (0, 5, 6, 1, 6, 7, 2, 7, 8, 3, 8, 9, 4, 9, 5))))
            if len(s) == 16:
                max_string = max(max_string, int(s))

    print('Problem 68:', max_string)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
