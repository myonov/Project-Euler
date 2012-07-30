from __future__ import print_function


def main():
    l = 10 ** 6

    ans = 0

    for n in range(1, l / 4):
        f = lambda x: (x + 1) * (2 * n + x + 1)

        x1, x2 = 0, l
        while x1 <= x2:
            x = (x1 + x2) / 2
            if f(x) > l:
                x2 = x - 1
            else:
                x1 = x + 1

        ans += (x2 + 1) / 2

    print(ans)


if __name__ == '__main__':
    main()
