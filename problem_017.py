# Project Euler

# Problem 17: Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

import time


start_time = time.time()
ans_project_17 = int(0)
words = [1000]
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
decades = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
for x in decades:
    words.append(x)
    for y in range(9):
        words.append(str(x + words[y]))
for i in range(9):
    words.append(str(words[i] + "hundred"))
    for j in range(99):
        words.append(str(words[i] + "hundred" + "and" + words[j]))
words.append("one" + "thousand")
for w in words:
    print(w)
    ans_project_17 += len(w)
print("Problem 17:", ans_project_17)
print("Total time:", time.time() - start_time)
