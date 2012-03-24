from __future__ import print_function

def count(n, m):
    return n * (n + 1) * m * (m + 1) / 4

def main():
    limit = 2000000

    m = limit
    ans = -1

    for i in range(1, 2000):
        for j in range(1, 2000):
            l = count(i, j)
            if abs(l -  limit) < m:
                m = abs(l - limit)
                ans = i * j

    print(ans)

if __name__ == '__main__':
    main()
