from __future__ import print_function
from itertools import permutations

from pr10 import gen_primes

def main():
    pr = filter(lambda x: len(str(x)) == 4, gen_primes(10000))
    s = set(pr)

    for p in pr:
        l = map(lambda x: int(''.join(x)), permutations(str(p)))
        for q in l:
            if len(str(q)) != 4: continue
            if q <= p: continue
            if q not in s: continue
            b = 2*q - p
            if b in s and b in l:
                print(p, q, b, sep='')
                break

if __name__ == '__main__':
    main()
