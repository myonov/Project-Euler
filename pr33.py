from __future__ import print_function

def gcd(x, y):
    if y == 0: return x
    if x == 0: return y
    if x > y: return gcd(y, x%y)
    return gcd(x, y%x)

def main():

    a, b = 1, 1

    for i in range(10, 100):
        for j in range(i+1, 100):
            if i % 10 != 0 and j % 10 != 0:
                a1, a2 = float(i / 10), float(i % 10)
                b1, b2 = float(j / 10), float(j % 10)

                s = float(i) / float(j)
                if s == a1 / b1 and a2 == b2 or \
                   s == a1 / b2 and a2 == b1 or \
                   s == a2 / b1 and a1 == b2 or \
                   s == a2 / b2 and a1 == b1:

                    a *= i
                    b *= j

    c = gcd(a, b)
    print(a, b, c)
    print(b/c)

if __name__ == '__main__':
    main()
