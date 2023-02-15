# Project Euler

# Problem 62: Cubic permutations
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import defaultdict
import time


def get_digit_counts(n):
    counts = defaultdict(int)
    for d in str(n):
        counts[d] += 1
    return counts


def main():
    start_time = time.time()
    cubes = set(i**3 for i in range(10000))
    digit_counts = defaultdict(list)

    for cube in cubes:
        key = ''.join(sorted(str(cube)))
        digit_counts[key].append(cube)

    for key in digit_counts:
        if len(digit_counts[key]) == 5:
            print('Problem 62:', min(digit_counts[key]))
            break

    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
