from __future__ import print_function

from pr64 import period
from pr57 import Rat

def frac(s):
    pos, a = period(s)
    for i in a:
        yield i

    l = len(a)

    while True:
        for i in a[l - pos:]:
            yield i

def find_sol(d):
    l = 500
    a = []
    f = frac(d)
    for i in range(l):
        a.append(next(f))

    for i in range(0, l):
        r = Rat(a[i])
        end = i - 1
        while end >= 0:
            r = Rat(a[end]) + Rat(1) / r
            end -= 1
        if r.p * r.p - d * r.q * r.q == 1:
            return r.p, r.q

def main():
    m = 0
    ans = -1
    for d in range(2, 1001):
        k = int(d ** 0.5)
        if k*k == d: continue
        x, y = find_sol(d)
        if x > m:
            m = x
            ans = d

    print(ans)

if __name__ == '__main__':
    main()
