# Project Euler

# Problem 52: Permuted multiples
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time

start_time = time.time()
ans_project_52 = int(0)
x = int(100000)
temp = False

while not temp:
    num_as_list_1 = [int(y) for y in str(x)]
    num_as_list_1.sort()
    num_as_list_2 = [int(y) for y in str(x * 2)]
    num_as_list_2.sort()
    if num_as_list_2 == num_as_list_1:
        num_as_list_3 = [int(y) for y in str(x * 3)]
        num_as_list_3.sort()
        if num_as_list_3 == num_as_list_1:
            num_as_list_4 = [int(y) for y in str(x * 4)]
            num_as_list_4.sort()
            if num_as_list_4 == num_as_list_1:
                num_as_list_5 = [int(y) for y in str(x * 5)]
                num_as_list_5.sort()
                if num_as_list_5 == num_as_list_1:
                    num_as_list_6 = [int(y) for y in str(x * 6)]
                    num_as_list_6.sort()
                    if num_as_list_6 == num_as_list_1:
                        ans_project_52 = x
                        temp = True
                        print(x)
                        break
    x += 1

print("Problem 52:", ans_project_52)
print("Total time:", time.time() - start_time)
