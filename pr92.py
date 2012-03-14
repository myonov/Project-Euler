from __future__ import print_function

from pr31 import memoize

@memoize
def f(n):
    nn = sum(map(lambda x: int(x) ** 2, str(n)))

    if nn == 89: return 1
    if nn == 1: return 0

    return f(nn)

def main():
    limit = 10000001

    print(sum(f(i) for i in range(1, limit)))

if __name__ == '__main__':
    main()
