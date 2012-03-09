from __future__ import print_function

from itertools import product

def main():
    possible_digits = [[chr(ord('0') + x) for x in range(10)]
                       for i in range(8)] + [['0']]

    fixed = '1234567890'

    for p in product(*possible_digits):
        s = ''
        for j in range(9):
            s += fixed[j] + p[j]
        s += fixed[-1]

        k = int(s)
        r = int(k ** 0.5)
        if r*r == k:
            print(r)
            break

if __name__ == '__main__':
    main()
