from __future__ import print_function

from pr31 import memoize

@memoize
def f(n, d1, d2):
    if n == 0:
        if d1 == 0:
            return 0
        return 1

    a = 0
    for i in range(10):
        if i + d1 + d2 > 9:
            break
        a += f(n-1, i, d1)

    return a

def main():
    print(f(20, 0, 0))

if __name__ == '__main__':
    main()
