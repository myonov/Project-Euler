from __future__ import print_function

from pr10 import gen_primes

def main():
    l = 1000001
    p = gen_primes(l)
    s = set(p)
    c = 0

    for r in p:
        q = []
        b = str(r)
        f = True
        for i in range(len(b)):
            q.append(int(b[i:] + b[:i]))
        for l in q:
            if l not in s:
                f = False
                break
        if f:
            c += 1
    print(c)

if __name__ == '__main__':
    main()
