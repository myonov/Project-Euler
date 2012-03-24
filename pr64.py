from __future__ import print_function

from pr33 import gcd

def period(s):
    a = []
    d = {}
    ss = s ** 0.5

    p = 0
    r = 1
    q = 1
    pos = 0

    while True:
        if (p, r, q) in d:
            return pos - d[(p, r, q)], a

        a.append(int(r * (ss + p) / q))
        d[(p, r, q)] = pos

        p1 = (a[-1] * q / r) - p
        q1 = s - p1 * p1
        r1 = q

        g = gcd(q1, r1)
        q1 /= g
        r1 /= g

        p, r, q = p1, r1, q1
        pos += 1

def main():
    limit = 10001
    cnt = 0

    for i in range(2, limit):
        k = int(i ** 0.5)
        if k*k == i: continue
        cnt += period(i)[0] % 2 == 1

    print(cnt)

if __name__ == '__main__':
    main()
