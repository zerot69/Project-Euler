# Project Euler

# Problem 46: Goldbach's other conjecture
# It was proposed by Christian Goldbach that every odd composite number can be written
# as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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


ans_project_46 = int(3)
prime_numbers = [2]
temp = True
while temp:
    if is_prime_number(ans_project_46):
        prime_numbers.append(ans_project_46)
    else:
        for x in prime_numbers:
            if math.sqrt(((ans_project_46 - x) / 2)) == int(math.sqrt(((ans_project_46 - x) / 2))):
                break
        else:
            break
    ans_project_46 += 2
print("Problem 46:", ans_project_46)
print("Total time:", time.time() - start_time)
