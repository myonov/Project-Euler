from __future__ import print_function

from pr31 import memoize

def main():
    limit = 80

    m = [
        map(int, line.strip().split(','))
        for line in open('matrix.txt')
    ]

    INF = 10 ** 100
    r = [[INF for i in range(limit)] for i in range(limit)]

    for i in range(limit):
        r[i][0] = m[i][0]

    def accum(j, k, i):
        ind1 = min(k, i)
        ind2 = max(k, i) + 1

        s = 0
        for l in range(ind1, ind2):
            s += m[l][j]
        return s

    for j in range(1, limit):
        for i in range(0, limit):
            for k in range(0, limit):
                r[i][j] = min(r[i][j], r[k][j-1] + accum(j, k, i))

    ans = INF
    for i in range(0, limit):
        ans = min(ans, r[i][-1])

    print(ans)

if __name__ == '__main__':
    main()
