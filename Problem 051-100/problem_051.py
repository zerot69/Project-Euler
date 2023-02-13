# Project Euler

# Problem 51: Prime digit replacements
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently, 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

import collections
import time

start_time = time.time()


def sieve(n):
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


def families(s):
    s = str(s)
    sol = []
    for duplicate in (collections.Counter(s) - collections.Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        b = [int(s.replace(duplicate, x)) for x in a]
        sol.append(b)
    return sol


def check(li):
    for n in li:
        checked.append(n)
        if n not in primes:
            li.remove(n)
    return li


primes = sieve(1000000)
primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]
checked = []
boolean = True
x = 0
ans_project_51 = int(0)

while boolean:
    if primes[x] not in checked:
        replacements = families(primes[x])
        for y in replacements:
            if len(check(y)) == 8:
                ans_project_51 = y[0]
                boolean = False
                break
    x += 1

print("Problem 51:", ans_project_51)
print("Total time:", time.time() - start_time)
