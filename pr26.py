from __future__ import print_function

def period(a, b):
    d = b * [0]
    s = 1
    d[a] = 1
    while True:
        s += 1
        a *= 10
        while a < b:
            a *= 10
            s += 1
        if a >= b:
            a %= b
            if d[a] != 0:
                return s - d[a]
            d[a] = s
        if a == 0:
            return 0
    return -1

def main():
    m = 0
    q = 0
    for i in range(2, 1000):
        p = period(1, i)
        if m < p:
            m = p
            q = i
    print(q)

if __name__ == '__main__':
    main()
