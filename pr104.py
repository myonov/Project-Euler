from __future__ import print_function

from pr25 import fib
from pr31 import memoize

@memoize
def fib_k(k):
    if k == 0: return 0
    if k == 1: return 1

    if k % 2 == 0:
        n = k / 2
        return fib_k(n) * (2 * fib_k(n-1) + fib_k(n))
    else:
        n = k / 2 + 1
        return fib_k(n - 1) ** 2 + fib_k(n) ** 2

def fib():
    mod = 10 ** 9

    yield 1
    yield 1
    a, b = 1, 1,

    while True:
        c = (a + b) % mod
        yield c
        a, b = b, c

def main():
    c = list('123456789')

    for i, f in enumerate(fib()):
        s = str(f)
        if len(s) < 9: continue
        if sorted(s) == c:
            l = fib_k(i+1)
            q = str(l)
            if sorted(q[:9]) == c:
                print(i+1)
                break

if __name__ == '__main__':
    main()
