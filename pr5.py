from __future__ import print_function

def gcd(x, y):
    if y == 0: return x
    if x == 0: return y
    if x > y: return gcd(y, x%y)
    return gcd(x, y%x)

def main():
    r = 1
    for i in range(1, 20):
        q = gcd(r, i)
        r = r * i / q
    print(r)

if __name__ == '__main__':
    main()
