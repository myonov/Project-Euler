from __future__ import print_function

from pr10 import gen_primes

def main():
    primes = gen_primes(1000000)
    pr_set = set(primes)

    bi = 0
    pr = 0
    m = 0
    while primes[bi] < 1000:
        b = primes[bi]
        for a in range(-999, 1001):
            s = lambda x: x*x + x*a + b
            q = 0
            for i in range(0, 1001):
                y = s(i)
                q += 1
                if y not in pr_set:
                    break
            if q > m:
                m = q
                pr = a * b
        bi += 1
    print(pr)

if __name__ == '__main__':
    main()
