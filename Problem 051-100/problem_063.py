# Project Euler

# Problem 63: Powerful digit counts
# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

import time


def main():
    start_time = time.time()
    count = 0
    for a in range(1, 10):
        for n in range(1, 23):
            if len(str(a ** n)) == n:
                count += 1
    print('Problem 63:', count)
    print('Total time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
