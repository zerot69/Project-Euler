# Project Euler

# Problem 72: Counting fractions

# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced
# proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

import time


def euler_totient_sieve(n):
    totients = list(range(n + 1))
    for i in range(2, n + 1):
        if totients[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                totients[j] = totients[j] // i * (i - 1)
    return totients


def main():
    start_time = time.time()
    totients = euler_totient_sieve(1000000)
    ans_problem_072 = sum(totients[2:])
    print('Problem 72:', ans_problem_072)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == "__main__":
    main()
