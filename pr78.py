from __future__ import print_function

from pr31 import memoize

mod = 10 ** 6
limit = 60001

def main():

    pent = []
    for i in range(1, limit):
        pp = lambda k: k*(3*k - 1) / 2
        pent.append(pp(i))
        pent.append(pp(-i))

    f = [1, 1]

    for i in range(2, limit):

        j = 0
        s = 0

        while pent[j] <= i:
            s += ((-1) ** (j % 4 > 1)) * f[ i - pent[j] ]
            j += 1

        f.append(s)
        if s % mod == 0:
            print(i)
            break


if __name__ == '__main__':
    main()
