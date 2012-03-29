from __future__ import print_function

from pr10 import gen_primes

def main():
    limit = 50000000

    s = gen_primes(10000)

    s4 = []
    s3 = []
    s2 = []
    for i in s:
        if i ** 4 < limit:
            s4.append(i)
        if i ** 3 < limit:
            s3.append(i)
        if i ** 2 < limit:
            s2.append(i)

    a = 0
    pr_set = set()
    for i in s4:
        for j in s3:
            for k in s2:
                q = i ** 4 + j ** 3 + k ** 2
                if q < limit:
                    pr_set.add(q)
                else:
                    break

    print(len(pr_set))

if __name__ == '__main__':
    main()
