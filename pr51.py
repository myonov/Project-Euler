from __future__ import print_function
from itertools import *

from pr10 import gen_primes

def main():
    limit = 10000001
    pr = gen_primes(limit)
    wanted = 8 - 1

    s = set(pr)
    r = limit

    mx = limit

    for i, p in enumerate(pr):
        for d in range(10):
            str_p = list(str(p))
            pos = [j for j, l in enumerate(str_p) if l == str(d)]
            if pos == []: continue
            for l in range(1, len(pos)+1):
                for comb in combinations(pos, l):
                    cnt = 0
                    for dig in range(d+1, 10):
                        str_n = str_p
                        for k in comb:
                            str_n[k] = str(dig)
                        num = int(''.join(str_n))
                        if num in s:
                            cnt += 1
                        if cnt >= wanted:
                            mx = min(mx, p)
    print(mx)

if __name__ == '__main__':
    main()
