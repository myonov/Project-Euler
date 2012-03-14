from __future__ import print_function

def main():
    limit = 80

    m = [
        map(int, line.strip().replace(',', ' ').split())
        for line in open('matrix.txt')
    ]

    r = [[0 for i in range(limit)] for i in range(limit)]
    r[0][0] = m[0][0]

    for i in range(1, limit):
        r[0][i] = m[0][i] + r[0][i-1]
        r[i][0] = m[i][0] + r[0][i-1]

    for i in range(1, limit):
        for j in range(1, limit):
            r[i][j] = min(r[i-1][j], r[i][j-1]) + m[i][j]

    print(r[-1][-1])

if __name__ == '__main__':
    main()
