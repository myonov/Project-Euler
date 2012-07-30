from __future__ import print_function

from pr10 import gen_primes


def main():
    limit = 10 ** 8

    pr = gen_primes(10 ** 8)
    s = set()
    l = len(pr)

    for i in range(l):
        for j in range(i, l):
            if pr[i] * pr[j] < limit:
                s.add(pr[i] * pr[j])
            else:
                break

    print(len(s))

if __name__ == '__main__':
    main()
