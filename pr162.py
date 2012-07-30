from __future__ import print_function

from pr53 import c

def f(n, a, z, o):
    # (A)s (Z)eros (O)nes
    s = 13 ** (n - (a + z + o))
    return s * c(n - 1, z) * c(n - z, o) * c(n - z - o, a)

def main():
    res = 0
    for i in range(3, 17):
        n = i
        for a in range(1, n - 1):
            for z in range(1, n - 1):
                for o in range(1, n - 1):
                    if a + z + o <= n:
                        res += f(n, a, z, o)

    res = hex(res)[2:].upper()
    if res[-1] == 'L':
        res = res[:-1]

    print(res)


if __name__ == '__main__':
    main()