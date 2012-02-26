from __future__ import print_function

def d(n):
    i = 2
    s = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                s -= i
            s += i + n / i
        i += 1
    return s

def main():
    s = 0
    for i in range(2, 10001):
        q = d(i)
        if d(q) == i and i != q and i < q:
            s += i + q

    print(s)

if __name__ == '__main__':
    main()
