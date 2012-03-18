from __future__ import print_function

from pr31 import memoize

@memoize
def f(n, k):
    if n == 0: return 1

    a = 0
    for i in range(k, n+1):
        a += f(n-i, i)

    return a

def main():
    print(f(100, 1)-1)

if __name__ == '__main__':
    main()
