from __future__ import print_function
from itertools import permutations

def main():

    s = [2, 3, 5, 7, 11, 13, 17]
    a = 0

    for p in permutations(range(1, 10)):
        for k in range(1, 10):
            q = p[:k] + (0,) + p[k:]
            d = [int(''.join(map(str, q[i:i+3]))) for i in range(1, 8)]
            f = True
            for i in range(7):
                if d[i] % s[i] != 0:
                    f = False
                    break
            if f:
                a += int(''.join(map(str, q)))

    print(a)

if __name__ == '__main__':
    main()
