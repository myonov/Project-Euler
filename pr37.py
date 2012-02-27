from __future__ import print_function
from itertools import product

from pr10 import gen_primes

def main():
    ends = ['2', '5', '3', '7']
    middle = ['1', '3', '7', '9']

    a = 0
    digits = 20
    res = 0

    primes = set(gen_primes(1000001))

    for i in range(2, digits):
        c = [ends]
        for j in range(i-2):
            c.append(middle)
        c.append(ends)
        for p in product(*c):
            t = True
            for k in range(1, digits):
                n = ''.join(p[:k])
                if int(n) not in primes:
                    t = False
                    break
            if not t: continue
            for k in range(1, digits):
                n = ''.join(p[-k:])
                if int(n) not in primes:
                    t = False
                    break
            if t:
                print(p)
                res += int(''.join(p))
                a += 1
                if a == 11:
                    print(res)
                    return

if __name__ == '__main__':
    main()
