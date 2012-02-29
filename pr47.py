from __future__ import print_function

from pr10 import gen_primes

def main():
    limit = 1000001
    rlimit = 4000000
    pr = gen_primes(limit)
    s1 = set(pr)

    def f(n):
        i = 0
        s = set()
        while n > 1:
            while n % pr[i] == 0:
                n /= pr[i]
                s.add(pr[i])
            i += 1
        return s

    for i in range(644, rlimit):
        a = [f(i), f(i+1), f(i+2), f(i+3)]
        if all(map(lambda x: len(x) >= 4, a)):
            print(i)
            break

if __name__ == '__main__':
    main()
