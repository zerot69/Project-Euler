# Project Euler

# Problem 66: Diophantine equation

# Consider quadratic Diophantine equations of the form:
# x^2 - Dy^2 = 1
# For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 3^2 - 2*2^2 = 1
# 2^2 - 3*1^2 = 1
# 9^2 - 5*4^2 = 1
# 5^2 - 6*2^2 = 1
# 8^2 - 7*3^2 = 1
# Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

import time
import math


def solve_diophantine_equation(D):
    a0 = int(math.sqrt(D))
    if a0 * a0 == D:
        return None
    m = 0
    d = 1
    a = a0
    num1 = 1
    num = a
    den1 = 0
    den = 1
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        num1, num = num, a * num + num1
        den1, den = den, a * den + den1
        if num * num - D * den * den == 1:
            return num


def main():
    start_time = time.time()
    max_x = 0
    max_D = 0
    for D in range(2, 1001):
        x = solve_diophantine_equation(D)
        if x is not None and x > max_x:
            max_x = x
            max_D = D

    print('Problem 66:', max_D)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
