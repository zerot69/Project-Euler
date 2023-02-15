# Project Euler

# Problem 70: Totient permutation

# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers
# less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
# relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

import time
import itertools
from math import sqrt


def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = list(range(3, n+1, 2))
    m_root = n ** 0.5
    half = (n + 1) // 2 - 1
    i = 0
    m = 3
    while m <= m_root:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [p for p in sieve if p]


def main():
    start_time = time.time()
    pairs = itertools.combinations(primes(2 * int(sqrt(1e7))), 2)
    minimum = (100, 0)
    for n, t in ((a * b, (a-1) * (b-1)) for a, b in pairs if a * b < 1e7):
        ratio = float(n) / t
        if ratio < minimum[0] and sorted(str(n)) == sorted(str(t)):
            minimum = (ratio, n)
    print('Problem 70:', minimum[1])
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == "__main__":
    main()
