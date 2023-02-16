# Project Euler

# Problem 75: Singular integer right triangles

# It turns out that 12 cm is the smallest length of wire that can be bent to form
# an integer sided right angle triangle in exactly one way,
# but there are many more examples.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
# and other lengths allow more than one solution to be found;
# for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000
# can exactly one integer sided right angle triangle be formed?

from math import gcd
import time


def main():
    start_time = time.time()
    L = 1500000
    triples = [0] * (L + 1)

    for m in range(2, int((L/2)**0.5)+1):
        for n in range(1, m):
            if (n + m) % 2 == 1 and gcd(n, m) == 1:
                a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
                p = a + b + c
                while p <= L:
                    triples[p] += 1
                    p += a + b + c

    ans_problem_075 = 0
    for t in triples:
        if t == 1:
            ans_problem_075 += 1

    print('Problem 75:', ans_problem_075)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
