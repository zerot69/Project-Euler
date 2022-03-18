# Project Euler

# Problem 38: Pan-digital multiples
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pan-digital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pan-digital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pan-digital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time

start_time = time.time()
ans_project_38 = int(0)
for x in range(1, 10000):
    pan_digital = ''
    i = 1
    while len(pan_digital) < 9:
        pan_digital += str(x * i)
        i += 1
    if (len(pan_digital) == 9) and (len(set(pan_digital)) == 9) and ('0' not in pan_digital):
        if int(pan_digital) > ans_project_38:
            ans_project_38 = int(pan_digital)
print("Problem 38:", ans_project_38)
print("Total time:", time.time() - start_time)
