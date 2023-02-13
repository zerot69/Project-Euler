# Project Euler

# Problem 57: Square root convergences
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# √2 = 1 + 1/(2 + 1/(2 + 1/2 + ... )
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 1.5
# 1 + 1/(2 + 1/2) = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 1.41379...
# The next three expansions are 90/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example
# where the number of digits in the numerator exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

import time

start_time = time.time()
ans_project_57 = int(0)
a = b = int(1)
for x in range(1000):
    numerator = a + 2*b
    denominator = a + b
    if len(str(numerator)) > len(str(denominator)):
        ans_project_57 += 1
    a = numerator
    b = denominator
print("Problem 57:", ans_project_57)
print("Total time:", time.time() - start_time)
