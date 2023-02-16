# Project Euler

# Problem 77: Prime summations

# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

import time


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


def prime_summations(n):
    primes = sieve(1000)
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in primes:
        for i in range(p, n + 1):
            dp[i] += dp[i - p]
    for i in range(n + 1):
        if dp[i] > 5000:
            return i
    return None


def main():
    start_time = time.time()
    print('Problem 77:', prime_summations(100))
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
