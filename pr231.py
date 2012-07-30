from __future__ import print_function

from pr10 import gen_primes

def f(n, k):
    a = 0
    r = k

    while k <= n:
        a = a + (n / k)
        k = k * r

    return a

def main():
    limit = 2 * 10 ** 7
    k = 15 * 10 ** 6
    l = limit - k

    pr = gen_primes(limit)
    a = 0
    for x in pr:
        a += x * (f(limit, x) - f(k, x) - f(l, x))

    print(a)

if __name__ == '__main__':
    main()