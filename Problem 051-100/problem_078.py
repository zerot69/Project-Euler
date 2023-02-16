# Project Euler

# Problem 78: Coin partitions

# Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

import time


def p(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    k, i = 1, 1
    result = 0
    while True:
        pent1 = i * (3 * i - 1) // 2
        pent2 = i * (3 * i + 1) // 2
        if pent1 > n and pent2 > n:
            break
        if pent1 <= n:
            result += (-1)**(k-1) * p(n - pent1, memo)
        if pent2 <= n:
            result += (-1)**(k-1) * p(n - pent2, memo)
        i += 1
        k += 1
    memo[n] = result
    return result


def main():
    start_time = time.time()
    ans_problem_078 = 1
    memo = {}
    while True:
        if p(ans_problem_078, memo) % 1000000 == 0:
            break
        ans_problem_078 += 1
    print('Problem 78:', ans_problem_078)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
