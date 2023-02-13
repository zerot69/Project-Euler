# Project Euler

# Problem 50: Prime permutations
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time
import math

start_time = time.time()


def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = []
limit = 1000000
x = 2
while sum(prime_numbers) < limit:
    if is_prime_number(x):
        prime_numbers.append(x)
    x = x + 1
final_sequence = []
length = len(prime_numbers)
y = length
while y != 0:
    x = 0
    while x + y < length + 1:
        sequence = prime_numbers[x:x + y]
        if sum(sequence) <= limit:
            if is_prime_number(sum(sequence)):
                if len(sequence) > len(final_sequence):
                    final_sequence = sequence
        x = x + 1
    y = y - 1
ans_project_50 = sum(final_sequence)
print("Problem 50:", ans_project_50)
print("Total time:", time.time() - start_time)
