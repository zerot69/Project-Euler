# Project Euler

# Problem 60: Prime pair sets
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_concat_prime(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


def lowest_sum_of_five_primes():
    primes = [2] + [i for i in range(3, 10000, 2) if is_prime(i)]
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if not is_concat_prime(primes[i], primes[j]):
                continue
            for k in range(j+1, len(primes)):
                if not (is_concat_prime(primes[i], primes[k]) and is_concat_prime(primes[j], primes[k])):
                    continue
                for l in range(k+1, len(primes)):
                    if not (is_concat_prime(primes[i], primes[l]) and is_concat_prime(primes[j], primes[l]) and is_concat_prime(primes[k], primes[l])):
                        continue
                    for m in range(l+1, len(primes)):
                        if (is_concat_prime(primes[i], primes[m]) and is_concat_prime(primes[j], primes[m]) and is_concat_prime(primes[k], primes[m]) and is_concat_prime(primes[l], primes[m])):
                            return [primes[i], primes[j], primes[k], primes[l], primes[m]]


def main():
    start_time = time.time()
    print("Problem 60:", sum(lowest_sum_of_five_primes()))
    print("Total time: {}".format(time.time() - start_time))


if __name__ == "__main__":
    main()
