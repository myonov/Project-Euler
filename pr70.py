from __future__ import print_function
from itertools import combinations, permutations

from pr69 import compute_func
from pr10 import gen_primes

def main():
#    mn = 1
#    mp = 1000.0

#    phi = compute_func()

#    for i in range(2, 8):
#        for c in combinations(range(10), i):
#            for p in permutations(c):
#                s = int(''.join(map(str, p)))

#                if p[0] == 0: continue
#                l = phi(s)

#                if set(str(l)) == set(str(s)) and float(s) / l < mp:
#                    mp = float(s) / l
#                    mn = s

#    print(mn, phi(mn))

    limit = 10000001
    pr = gen_primes(limit)
    s = set(pr)
    k = limit ** 0.5 * 2
    i, j = 0, 0
    l = 1000.0
    ph = 1

    while pr[i] < k:
        for j in pr:
            num = pr[i] * j
            if num > limit: break
            phi = (pr[i] - 1) * (j - 1)
            if sorted(str(phi)) == sorted(str(num)):
                l1 = float(num) / phi
                if l1 < l:
                    l = l1
                    ph = num
        i += 1

    phi = compute_func()
    print(ph, phi(ph))

if __name__ == '__main__':
    main()
