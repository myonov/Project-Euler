from __future__ import print_function

from pr10 import gen_primes

def main():
    limit = 10001
    pr = gen_primes(limit)
    s1 = set(pr)
    s2 = set(range(3, limit, 2)).difference(s1)

    s3 = set()

    for p in pr:
        ul = int((limit - p) ** 0.5 + 2)
        for i in range(1, ul):
            s3.add(p + 2*i*i)

    print(min(s2.difference(s3)))

if __name__ == '__main__':
    main()
