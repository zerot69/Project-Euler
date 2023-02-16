# Project Euler

# Problem 76: Counting summations

# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a sum of at least two positive integers?

import time


def count_summations(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]


def main():
    start_time = time.time()
    print('Problem 76:', count_summations(100))
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
