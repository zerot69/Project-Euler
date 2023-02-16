# Project Euler

# Problem 71: Ordered fractions

# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced
# proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator
# of the fraction immediately to the left of 3/7.

from math import gcd
import time


def generate_fractions():
    fractions = []
    for d in range(2, 1000001):
        n = d * 3 // 7
        while gcd(n, d) != 1:
            n -= 1
        fractions.append((n, d))
    return fractions


def main():
    start_time = time.time()
    fractions = generate_fractions()
    fractions.sort(key=lambda x: x[0] / x[1])
    for i in range(len(fractions)):
        if fractions[i][0] / fractions[i][1] >= 3 / 7:
            break
    print('Problem 71:', fractions[i-1][0])
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == "__main__":
    main()
