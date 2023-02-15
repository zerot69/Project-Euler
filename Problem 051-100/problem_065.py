# Project Euler

# Problem 65: Convergents of e

# The square root of 2 can be written as an infinite continued fraction.
# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...))) = 1.414213...
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
# Hence the sequence of the first ten convergents for sqrt(2) are:
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.


import time


def e_continued_fraction(n):
    a = [2]
    for i in range(1, n):
        if i % 3 == 2:
            a.append((i//3+1)*2)
        else:
            a.append(1)
    return a


def nth_convergent(a, n):
    p0, p1 = 1, a[0]
    q0, q1 = 0, 1
    for i in range(1, n):
        p, q = a[i]*p1+p0, a[i]*q1+q0
        p0, p1 = p1, p
        q0, q1 = q1, q
    return p1, q1


def main():
    start_time = time.time()
    a = e_continued_fraction(100)
    numerator = nth_convergent(a, 100)[0]
    ans_problem_065 = sum(int(digit) for digit in str(numerator))
    print('Problem 65', ans_problem_065)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
