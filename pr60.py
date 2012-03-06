from __future__ import print_function

from pr10 import gen_primes
from pr3 import isprime

def test_is_prime():
    limit = 1000000
    s = set(gen_primes(limit))
    mx = max(s)
    def inner(n):
        if mx > n:
            return n in s
        return isprime(n)
    return inner

def main():
    limit = 10000
    pr = gen_primes(limit)
    g = {k: [] for k in pr}

    dirty_hack = {'ans': limit * 10}
    test_prime = test_is_prime()

    pr1 = [3] + filter(lambda x: x%3 == 1, pr)
    pr2 = [3] + filter(lambda x: x%3 == 2, pr)

    def ok(q, n):
        l = len(q)
        for i in range(l):
            if not test_prime(int(str(q[i]) + str(n))) or\
               not test_prime(int(str(n) + str(q[i]))):
                return False
        return True

    def search(path, hack):
        if len(path) == 5:
            ns = sum(path)
            hack['ans'] = min(hack['ans'], ns)
            return

        n = path[-1]
        for k in g[n]:
            if k not in path and ok(path, k):
                path.append(k)
                search(path, hack)
                path.pop()

    for primes in [pr1, pr2]:
        for i, x in enumerate(primes):
            for q in primes[i+1:]:
                if test_prime(int(str(x) + str(q))) and\
                   test_prime(int(str(q) + str(x))):
                    g[x].append(q)
                    g[q].append(x)

    for p in pr:
        search([p], dirty_hack)

    print(dirty_hack['ans'])

if __name__ == '__main__':
    main()
