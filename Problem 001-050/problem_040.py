# Project Euler

# Problem 40: Champernowne's constant
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time

start_time = time.time()
ans_project_40 = int(0)
num_as_string = "0."
x = int(1)
while len(num_as_string) < 1000000 + 2:
    num_as_string += (str(x))
    x += 1
ans_project_40 = (int(num_as_string[1 + 1]) * int(num_as_string[10 + 1]) * int(num_as_string[100 + 1]) *
                  int(num_as_string[1000 + 1]) * int(num_as_string[10000 + 1]) * int(num_as_string[100000 + 1]) *
                  int(num_as_string[1000000 + 1]))
print("Problem 40:", ans_project_40)
print("Total time:", time.time() - start_time)
