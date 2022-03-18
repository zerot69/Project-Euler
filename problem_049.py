# Project Euler

# Problem 49: Prime permutations
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

import time
import itertools

start_time = time.time()


def sieve_of_erotosthenes(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def create_number(m):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            difference = m[j] - m[i]
            if m[j] + difference in m:
                return str(m[i]) + str(m[j]) + str(m[j] + difference)
    return False


ans_project_49 = int(0)
prime_numbers = sieve_of_erotosthenes(10000)
prime_numbers = [x for x in prime_numbers if x > 1487]
for x in prime_numbers:
    permutations = itertools.permutations(str(x))
    y = [int(''.join(x)) for x in permutations]
    y = list(set([x for x in y if x in prime_numbers]))
    y.sort()
    if len(y) >= 3:
        if create_number(y):
            ans_project_49 = create_number(y)
            break
print("Problem 49:", ans_project_49)
print("Total time:", time.time() - start_time)
