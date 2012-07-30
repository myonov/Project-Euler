from __future__ import print_function

from pr53 import c
from pr10 import gen_primes


def main():
    limit = 51
    l = 12 * 10 ** 6
    s = set()

    pr_sq = [x * x for x in gen_primes(l)]

    for i in range(limit):
        for j in range(i + 1):
            s.add(c(i, j))

    a = 0

    for num in s:
        f = True
        for j in pr_sq:
            if j > num:
                break
            if num % j == 0:
                f = False
                break
        if f:
            a += num

    print(a)

if __name__ == '__main__':
    main()
