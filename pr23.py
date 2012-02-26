from __future__ import print_function

def pdiv(n):
    i = 2
    s = 1
    while i*i <= n:
        if n % i == 0:
            if i*i == n:
                s -= i
            s += i + n / i
        i += 1
    return s

def main():
    l = 28123
    ab = set()
    for x in range(2, l+1):
        if pdiv(x) > x:
            ab.add(x)

    s = set()
    for x in ab:
        for y in ab:
            s.add(x+y)

    r = 0
    for x in range(1, l+1):
        if not x in s:
            r += x

    print(r)

if __name__ == '__main__':
    main()
