from __future__ import print_function

from pr10 import gen_primes

def main():
    limit = 1000001
    pr = gen_primes(limit)
    s = set(pr)

    r = 0
    m = 0
    ll = len(pr)

    for i in range(len(pr)):
        k = m
        if i + m >= ll: break
        a = sum(pr[i:i+k])

        while a < limit:
            a += pr[i+k]
            if a in s:
                r = a
                if k > m:
                    m = k
            k += 1

    print(r)

if __name__ == '__main__':
    main()
