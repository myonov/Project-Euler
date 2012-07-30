from pr31 import memoize


@memoize
def ok(pos, l, last):
    if pos == 30:
            return 1

    res = 0
    if last != 'aa':
        res += ok(pos + 1, l, last[1] + 'a')

    if l == 0:
        res += ok(pos + 1, l + 1, last[1] + 'l')

    res += ok(pos + 1, l, last[1] + 'o')
    return res


def main():
    print(ok(0, 0, 'oo'))

if __name__ == '__main__':
    main()
