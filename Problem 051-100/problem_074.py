# Project Euler

# Problem 74: Digit factorial chains

# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
# it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop.
# For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import time


def main():
    start_time = time.time()
    factorials = [1]
    for i in range(1, 10):
        factorials.append(factorials[-1] * i)

    digit_factorials = [sum(factorials[int(d)] for d in str(n))
                        for n in range(1000000)]
    ans_problem_74 = 0

    for n in range(2, 1000000):
        chain = [n]
        while True:
            next_n = digit_factorials[chain[-1]]
            if next_n >= 1000000:
                break
            if next_n in chain:
                break
            chain.append(next_n)
        if len(chain) == 60:
            ans_problem_74 += 1

    print('Problem 74:', ans_problem_74)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
