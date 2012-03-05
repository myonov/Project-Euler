from __future__ import print_function

from pr31 import memoize

@memoize
def c(n, k):
    if n == 0:
        if k == 0: return 1
        return 0
    if n == k: return 1
    return c(n-1, k-1) + c(n-1, k)

def main():
    limit = 1000000
    cnt = 0

    for i in range(1, 101):
        for j in range(1, i+1):
            if c(i, j) > limit:
                cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
